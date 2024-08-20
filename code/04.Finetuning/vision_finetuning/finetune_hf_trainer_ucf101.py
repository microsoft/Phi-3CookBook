"""
example for finetuning Phi-3-V on UCF-101 video classification using the Hugging Face Trainer API
Modified from Idefics-2 finetuning notebook:
https://colab.research.google.com/drive/1rm3AGquGEYXfeeizE40bbDtcWh5S4Nlq?usp=sharing

Install dependencies:
    pip install transformers==4.38.1 \
        datasets \
        accelerate==0.30.1 \
        peft \
        Levenshtein \
        deepspeed==0.13.1
minimal run:
    torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py
"""
import argparse
import json
import os
from pathlib import Path

import torch
from accelerate import Accelerator
from accelerate.utils import gather_object
from peft import LoraConfig
from tqdm import tqdm
from transformers import (
    AutoModelForCausalLM,
    AutoProcessor,
    BitsAndBytesConfig,
    Trainer,
    TrainingArguments,
)

from phi3v_dataset import Phi3VDataCollator, Phi3VDataset, Phi3VEvalDataCollator, Phi3VEvalDataset

# suggested deepspeed config
DS_CONFIG_DICT = {
    'zero_optimization': {
        'stage': 2,
        'allgather_partitions': True,
        'allgather_bucket_size': 5e8,
        'overlap_comm': True,
        'reduce_scatter': True,
        'reduce_bucket_size': 5e8,
        'contiguous_gradients': True,
        'round_robin_gradients': True,
    },
    'fp16': {
        'enabled': 'auto',
        'loss_scale': 0,
        'loss_scale_window': 1000,
        'initial_scale_power': 16,
        'hysteresis': 2,
        'min_loss_scale': 1,
    },
    'bf16': {'enabled': 'auto'},
    'train_micro_batch_size_per_gpu': 'auto',
    'train_batch_size': 'auto',
    'gradient_accumulation_steps': 'auto',
    'gradient_clipping': 'auto',
}


def create_dataset(data_dir, processor):
    """
    UCF-101 dataset from preprocessed folder
    """
    data_path = Path(data_dir)
    train_dataset = Phi3VDataset(
        jsonl_file=str(data_path / 'ucf101_train.jsonl'),
        image_dir=str(data_path / 'images'),
        processor=processor,
    )
    eval_dataset = Phi3VEvalDataset(
        jsonl_file=str(data_path / 'ucf101_val.jsonl'),
        image_dir=str(data_path / 'images'),
        processor=processor,
    )

    return train_dataset, eval_dataset


def create_lora_config(rank, alpha_to_rank_ratio=2.0, dropout=0.0, freeze_vision_model=False):
    linear_modules = [
        # Phi language modules
        'qkv_proj',  # attention
        'o_proj',
        'down_proj',  # MLP
        'gate_up_proj',
        'lm_head',
    ]
    if not freeze_vision_model:
        vision_linear_modules = [
            # CLIP modules
            'q_proj',  # attention
            'k_proj',
            'v_proj',
            'out_proj',
            'fc1',  # MLP
            'fc2',
            # image projection
            'img_projection.0',
            'img_projection.2',
        ]
        linear_modules.extend(vision_linear_modules)
    lora_config = LoraConfig(
        r=rank,
        lora_alpha=round(rank * alpha_to_rank_ratio),
        lora_dropout=dropout,
        target_modules=linear_modules,
        init_lora_weights='gaussian',
    )
    return lora_config


def create_model(model_name_or_path, use_flash_attention=False, use_qlora=False):
    bnb_config = (
        BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type='nf4',
            bnb_4bit_compute_dtype=torch.bfloat16 if use_flash_attention else torch.float16,
        )
        if use_qlora
        else None
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_name_or_path,
        # Phi-3-V is originally trained in bf16 + flash attn
        # For fp16 mixed precision training, load in f32 to avoid hf accelerate error
        torch_dtype=torch.bfloat16 if use_flash_attention else torch.float32,
        trust_remote_code=True,
        _attn_implementation='flash_attention_2' if use_flash_attention else 'eager',
        quantization_config=bnb_config,
    )

    return model


@torch.no_grad()
def evaluate(
    model, processor, eval_dataset, save_path=None, disable_tqdm=False, eval_batch_size=1
):
    rank = int(os.environ.get('RANK', 0))
    local_rank = int(os.environ.get('LOCAL_RANK', 0))
    world_size = int(os.environ.get('WORLD_SIZE', 1))

    model.eval()
    answers_unique = []
    generated_texts_unique = []

    eval_dataset_shard = eval_dataset.shard(world_size, rank)
    eval_dataloader = torch.utils.data.DataLoader(
        eval_dataset_shard,
        batch_size=eval_batch_size,
        collate_fn=Phi3VEvalDataCollator(processor.tokenizer.pad_token_id),
        shuffle=False,
        drop_last=False,
        num_workers=4,
        prefetch_factor=2,
        pin_memory=True,
    )
    for batch in tqdm(eval_dataloader, disable=(rank != 0) or disable_tqdm):
        unique_ids = batch.pop('unique_ids')
        answers = batch.pop('answers')
        answers_unique.extend(
            {'id': i, 'answer': a.strip().strip('.').lower()} for i, a in zip(unique_ids, answers)
        )

        inputs = {k: v.to(f'cuda:{local_rank}') for k, v in batch.items()}
        generated_ids = model.generate(
            **inputs, eos_token_id=processor.tokenizer.eos_token_id, max_new_tokens=64
        )

        input_len = inputs['input_ids'].size(1)
        generated_texts = processor.batch_decode(
            generated_ids[:, input_len:],
            skip_special_tokens=True,
            clean_up_tokenization_spaces=False,
        )
        generated_texts_unique.extend(
            {'id': i, 'generated_text': g.strip().strip('.').lower()}
            for i, g in zip(unique_ids, generated_texts)
        )

    # gather outputs from all ranks
    answers_unique = gather_object(answers_unique)
    generated_texts_unique = gather_object(generated_texts_unique)

    if rank == 0:
        assert len(answers_unique) == len(generated_texts_unique)
        acc = sum(
            a['answer'] == g['generated_text']
            for a, g in zip(answers_unique, generated_texts_unique)
        ) / len(answers_unique)
        if save_path:
            with open(save_path, 'w') as f:
                save_dict = {
                    'answers_unique': answers_unique,
                    'generated_texts_unique': generated_texts_unique,
                    'accuracy': acc,
                }
                json.dump(save_dict, f)

        return acc
    return None


def patch_clip_for_lora(model):
    # remove unused parameters and then monkey patch
    def get_img_features(self, img_embeds):
        clip_vision_model = self.img_processor.vision_model
        hidden_states = clip_vision_model.embeddings(img_embeds)
        hidden_states = clip_vision_model.pre_layrnorm(hidden_states)
        patch_feature = clip_vision_model.encoder(
            inputs_embeds=hidden_states, output_hidden_states=True
        ).hidden_states[-1][:, 1:]
        return patch_feature

    image_embedder = model.model.vision_embed_tokens
    layer_index = image_embedder.layer_idx
    clip_layers = image_embedder.img_processor.vision_model.encoder.layers
    if layer_index < 0:
        layer_index = len(clip_layers) + layer_index
    del clip_layers[layer_index + 1 :]
    del image_embedder.img_processor.vision_model.post_layernorm
    image_embedder.get_img_features = get_img_features.__get__(image_embedder)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--model_name_or_path',
        type=str,
        default='microsoft/Phi-3.5-vision-instruct',
        help='Model name or path to load from',
    )
    parser.add_argument('--data_dir', type=str, required=True, help='Path to UCF-101 dataset')
    parser.add_argument('--use_flash_attention', action='store_true', help='Use Flash Attention')
    parser.add_argument('--bf16', action='store_true', help='Use BF16')
    parser.add_argument('--use_lora', action='store_true', help='Use LoRA')
    parser.add_argument('--use_qlora', action='store_true', help='Use QLora')
    parser.add_argument('--output_dir', type=str, default='./output/', help='Output directory')
    parser.add_argument('--batch_size', type=int, default=16, help='Batch size')
    parser.add_argument(
        '--batch_size_per_gpu',
        type=int,
        default=1,
        help='Batch size per GPU (adjust this to fit in GPU memory)',
    )
    parser.add_argument(
        '--num_crops',
        type=int,
        default=4,
        help='Number of maximum image crops (For videos the default is 4 to reduce memory usage)',
    )
    parser.add_argument(
        '--num_train_epochs', type=int, default=1, help='Number of training epochs'
    )
    parser.add_argument('--learning_rate', type=float, default=4.0e-5, help='Learning rate')
    parser.add_argument('--wd', type=float, default=0.01, help='Weight decay')
    parser.add_argument('--no-tqdm', dest='tqdm', action='store_false', help='Disable tqdm')
    parser.add_argument('--lora_rank', type=int, default=64, help='LoRA rank')
    parser.add_argument(
        '--lora_alpha_ratio', type=float, default=2, help='LoRA alpha to rank ratio'
    )
    parser.add_argument('--lora_dropout', type=float, default=0.0, help='LoRA dropout')
    parser.add_argument('--freeze_vision_model', action='store_true', help='Freeze vision model')
    args = parser.parse_args()

    assert args.num_crops <= 16, 'num_crops must be less than or equal to 16'
    if args.use_qlora:
        args.use_lora = True
    if args.use_flash_attention:
        args.bf16 = True

    accelerator = Accelerator()

    with accelerator.local_main_process_first():
        processor = AutoProcessor.from_pretrained(
            args.model_name_or_path, trust_remote_code=True, num_crops=args.num_crops
        )
        model = create_model(
            args.model_name_or_path,
            use_flash_attention=args.use_flash_attention,
            use_qlora=args.use_qlora,
        )

    train_dataset, eval_dataset = create_dataset(args.data_dir, processor)

    num_gpus = accelerator.num_processes
    print(f'training on {num_gpus} GPUs')
    assert (
        args.batch_size % (num_gpus * args.batch_size_per_gpu) == 0
    ), 'Batch size must be divisible by the number of GPUs'
    gradient_accumulation_steps = args.batch_size // (num_gpus * args.batch_size_per_gpu)
    if args.bf16:
        fp16 = False
        bf16 = True
    else:
        fp16 = True
        bf16 = False

    # hard coded training args
    training_args = TrainingArguments(
        num_train_epochs=args.num_train_epochs,
        per_device_train_batch_size=args.batch_size_per_gpu,
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={'use_reentrant': False},
        gradient_accumulation_steps=gradient_accumulation_steps,
        optim='adamw_torch',
        adam_beta1=0.9,
        adam_beta2=0.95,
        adam_epsilon=1e-7,
        learning_rate=args.learning_rate,
        weight_decay=args.wd,
        max_grad_norm=1.0,
        lr_scheduler_type='linear',
        warmup_steps=50,
        logging_steps=10,
        output_dir=args.output_dir,
        save_strategy='no',
        save_total_limit=10,
        save_only_model=True,
        bf16=bf16,
        fp16=fp16,
        remove_unused_columns=False,
        report_to='none',
        deepspeed=None if args.use_lora else DS_CONFIG_DICT,
        disable_tqdm=not args.tqdm,
        dataloader_num_workers=4,
        dataloader_prefetch_factor=2,
        ddp_find_unused_parameters=False,
    )
    data_collator = Phi3VDataCollator(pad_token_id=processor.tokenizer.pad_token_id)

    # eval before fine-tuning
    out_path = Path(training_args.output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    if not args.use_qlora:
        local_rank = int(os.environ.get('LOCAL_RANK', 0))
        model = model.to(f'cuda:{local_rank}')
    acc = evaluate(
        model,
        processor,
        eval_dataset,
        save_path=out_path / 'eval_before.json',
        disable_tqdm=not args.tqdm,
        eval_batch_size=args.batch_size_per_gpu,
    )
    if accelerator.is_main_process:
        print(f'Accuracy before finetuning: {acc}')

    if args.use_lora:
        patch_clip_for_lora(model)
        lora_config = create_lora_config(
            rank=args.lora_rank,
            alpha_to_rank_ratio=args.lora_alpha_ratio,
            dropout=args.lora_dropout,
            freeze_vision_model=args.freeze_vision_model,
        )
        model.add_adapter(lora_config)
        model.enable_adapters()

    if args.freeze_vision_model:
        model.model.vision_embed_tokens.requires_grad_(False)

    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=train_dataset,
    )
    trainer.train()
    trainer.save_model()
    if accelerator.is_main_process:
        processor.save_pretrained(training_args.output_dir)
    accelerator.wait_for_everyone()

    # eval after fine-tuning (load saved checkpoint)
    if args.use_lora:
        # first try to clear GPU memory
        del model
        del trainer
        __import__('gc').collect()
        torch.cuda.empty_cache()

        # reload the model for inference
        # this part also serves as an example of how to load a trained model
        model = AutoModelForCausalLM.from_pretrained(
            args.model_name_or_path,
            # Phi-3-V is originally trained in bf16 + flash attn
            # For fp16 mixed precision training, load in f32 to avoid hf accelerate error
            torch_dtype=torch.bfloat16 if args.use_flash_attention else torch.float32,
            trust_remote_code=True,
            _attn_implementation='flash_attention_2' if args.use_flash_attention else 'eager',
        )
        patch_clip_for_lora(model)
        model.load_adapter(training_args.output_dir)
    else:
        # for full finetuning, GPU memory can't be cleared (likely caused by deepspeed
        # https://github.com/microsoft/DeepSpeed/issues/3677)
        # so we don't reload the model
        model = accelerator.unwrap_model(model, keep_fp32_wrapper=not args.bf16)

        # below is a sample code snippet to load fully-finetuned model
        # model = AutoModelForCausalLM.from_pretrained(
        #     training_args.output_dir,
        #     # Phi-3-V is originally trained in bf16 + flash attn
        #     # For fp16 mixed precision training, load in f32 to avoid hf accelerate error
        #     torch_dtype=torch.bfloat16 if args.use_flash_attention else torch.float32,
        #     trust_remote_code=True,
        #     _attn_implementation='flash_attention_2' if args.use_flash_attention else 'eager',
        # )

    rank = int(os.environ.get('RANK', 0))
    local_rank = int(os.environ.get('LOCAL_RANK', 0))
    model = model.to(f'cuda:{local_rank}')
    acc = evaluate(
        model,
        processor,
        eval_dataset,
        save_path=out_path / 'eval_after.json',
        disable_tqdm=not args.tqdm,
        eval_batch_size=args.batch_size_per_gpu,
    )
    if rank == 0:
        print(f'Accuracy after finetuning: {acc}')


if __name__ == '__main__':
    main()
