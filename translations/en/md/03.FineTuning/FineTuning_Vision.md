# Phi-3.5-vision finetuning recipe

This is the official guide for fine-tuning Phi-3.5-vision using Huggingface libraries.  
Please `cd` to the code directory [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) before running the following commands.

## Installation

```bash
# create a new conda environment
conda create -n phi3v python=3.10
conda activate phi3v

# install pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# other libraries needed to run the example code
pip install -r requirements.txt

# (optional) flash attention -- Ampere+ GPUs (e.g., A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (optional) QLoRA -- Turing+ GPUs (e.g., RTX 8000)
pip install bitsandbytes==0.43.1
```

## Quick start

We provide two example fine-tuning scripts: one for DocVQA and another for hateful meme classification.

Minimal hardware requirements: 4x RTX8000 GPUs (48GB RAM per GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision now officially supports multi-image inputs. Here's an example for fine-tuning NLVR2:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Usage guide

Depending on the hardware, users can choose different fine-tuning strategies. We support:  
- Full fine-tuning (with Deepspeed Zero-2), with the option to freeze vision parameters  
- LoRA (including 4bit QLoRA)  

In general, we recommend using full fine-tuning with flash attention and bf16 whenever possible.

### Guide for converting your custom dataset to the required format

We use a minimal video classification dataset (a subset of UCF-101) as an end-to-end example to demonstrate how to convert your custom dataset to the required format and fine-tune Phi-3.5-vision on it.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

The converted data will look like this:

```bash
> tree --filelimit=10 /path/to/converted_ucf101
/path/to/converted_ucf101
├── images
│   ├── test
│   │   ├── ApplyEyeMakeup [48 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [32 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [56 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [72 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [32 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [72 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [80 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [88 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [48 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [72 entries exceeds filelimit, not opening dir]
│   ├── train
│   │   ├── ApplyEyeMakeup [240 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [240 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [240 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [240 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [240 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [240 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [240 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [240 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [240 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [240 entries exceeds filelimit, not opening dir]
│   └── val
│       ├── ApplyEyeMakeup [24 entries exceeds filelimit, not opening dir]
│       ├── ApplyLipstick [24 entries exceeds filelimit, not opening dir]
│       ├── Archery [24 entries exceeds filelimit, not opening dir]
│       ├── BabyCrawling [24 entries exceeds filelimit, not opening dir]
│       ├── BalanceBeam [24 entries exceeds filelimit, not opening dir]
│       ├── BandMarching [24 entries exceeds filelimit, not opening dir]
│       ├── BaseballPitch [24 entries exceeds filelimit, not opening dir]
│       ├── Basketball [24 entries exceeds filelimit, not opening dir]
│       ├── BasketballDunk [24 entries exceeds filelimit, not opening dir]
│       └── BenchPress [24 entries exceeds filelimit, not opening dir]
├── ucf101_test.jsonl
├── ucf101_train.jsonl
└── ucf101_val.jsonl

34 directories, 3 files
```

For the `jsonl` annotation, each line should be a dictionary like this:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Note that `conversations` is a list, which means multi-turn conversations can be supported if such data is available.

## Requesting Azure GPU Quota 

### Prerequisites

You need an Azure account with the Contributor role (or another role that includes Contributor access).  

If you don't have an Azure account, create a [free account before you begin](https://azure.microsoft.com).

### Request a quota increase

You can request a quota increase directly from My Quotas. Follow these steps to request an increase for a quota. For this example, you can select any adjustable quota in your subscription.

1. Sign in to the [Azure portal](https://portal.azure.com).  
2. Enter "quotas" into the search box, and then select Quotas.  
   ![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)  
3. On the Overview page, select a provider, such as Compute or AML.  

   **Note:** For all providers other than Compute, you'll see a "Request increase" column instead of the "Adjustable" column described below. Here, you can request an increase for a specific quota or create a support request for the increase.  

4. On the My Quotas page, under "Quota name," select the quota you want to increase. Make sure that the "Adjustable" column shows "Yes" for this quota.  
5. Near the top of the page, select "New Quota Request," then select "Enter a new limit."  
   ![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)  
6. In the "New Quota Request" pane, enter a numerical value for your new quota limit, then select "Submit."  

Your request will be reviewed, and you'll be notified if the request can be fulfilled. This usually happens within a few minutes.  

If your request isn't fulfilled, you'll see a link to create a support request. When you use this link, a support engineer will assist you with your increase request.

## Azure Compute GPU machine SKU suggestions

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)  
[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)  
[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)  

Here are some examples:

### If you have A100 or H100 GPUs

Full fine-tuning typically gives the best performance. Use the following command to fine-tune Phi-3-V on hateful meme classification:

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### If you have Standard_ND40rs_v2 8x V100-32GB GPUs

It’s still possible to fully fine-tune Phi-3-V on hateful meme classification. However, expect much lower throughput compared to A100 or H100 GPUs due to the lack of flash attention support. Accuracy may also be affected due to the lack of bf16 support (fp16 mixed-precision training is used instead).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### If you don't have access to data center GPUs

LoRA might be your only option. Use the following command to fine-tune Phi-3-V on hateful meme classification:

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

For Turing+ GPUs, QLoRA is supported:

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Suggested hyperparameters and expected accuracy

### NLVR2

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_nlvr2.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Training method | Frozen vision model | Data type | LoRA rank | LoRA alpha | Batch size | Learning rate | Epochs | Accuracy  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
Full fine-tuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
Full fine-tuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
LoRA results coming soon |  |  |  |  |  |  |  |  |

### NOTE  
The following DocVQA and Hateful Memes results are based on the previous version (Phi-3-vision).  
The new results with Phi-3.5-vision will be updated soon.

### DocVQA (NOTE: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_docvqa.py \
  --full_train \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Training method | Data type | LoRA rank | LoRA alpha | Batch size | Learning rate | Epochs | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
Full fine-tuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
Full fine-tuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
Frozen image model | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
Frozen image model | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  

### Hateful memes (NOTE: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Training method | Data type | LoRA rank | LoRA alpha | Batch size | Learning rate | Epochs | Accuracy  
--- | --- | --- | --- | --- | --- | --- | --- |  
Full fine-tuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
Full fine-tuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
Frozen image model | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
Frozen image model | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |  

## Speed benchmarking (NOTE: Phi-3-vision)

New benchmarking results with Phi-3.5-vision will be updated soon.  

Speed benchmarking is performed on the DocVQA dataset. The average sequence length of this dataset is 2443.23 tokens (using `num_crops=16` for the image model).

### 8x A100-80GB (Ampere)

Training method | \# nodes | GPUs | Flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
Full fine-tuning | 1 | 8 |  | 64 | 5.041 | 1x | ~42 |  
Full fine-tuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36 |  
Full fine-tuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29 |  
Full fine-tuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26 |  
Frozen image model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29 |  
Frozen image model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27 |  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50 |  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16 |  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32 |  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10 |  

### 8x V100-32GB (Volta)

Training method | \# nodes | GPUs | Flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
Full fine-tuning | 1 | 8 |  | 64 | 2.462 | 1x | ~32 |  
Full fine-tuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32 |  
Full fine-tuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32 |  
Frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27 |  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30 |  

## Known issues

- Flash attention cannot be used with fp16 (bf16 is always recommended when available, and all GPUs supporting flash attention also support bf16).  
- Saving intermediate checkpoints and resuming training is not supported yet.  

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.