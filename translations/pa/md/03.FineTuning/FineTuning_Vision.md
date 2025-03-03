# Phi-3.5-vision ਫਾਈਨਟਿਊਨਿੰਗ ਰੇਸਿਪੀ

ਇਹ ਹੈ Phi-3.5-vision ਨੂੰ huggingface ਲਾਇਬ੍ਰੇਰੀਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਾਈਨਟਿਊਨ ਕਰਨ ਲਈ ਅਧਿਕਾਰਕ ਸਮਰਥਨ।  
ਕਿਰਪਾ ਕਰਕੇ `cd` ਕੋਡ ਡਾਇਰੈਕਟਰੀ [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) ਵਿੱਚ ਜਾਣ ਤੋਂ ਪਹਿਲਾਂ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਚਲਾਓ।

## ਇੰਸਟਾਲੇਸ਼ਨ

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

## ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ

ਅਸੀਂ ਦੋ ਉਦਾਹਰਣ ਫਾਈਨਟਿਊਨਿੰਗ ਸਕ੍ਰਿਪਟ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਾਂ, ਇੱਕ DocVQA ਲਈ ਅਤੇ ਇੱਕ hateful meme ਕਲਾਸੀਫਿਕੇਸ਼ਨ ਲਈ।

ਘੱਟੋ-ਘੱਟ ਹਾਰਡਵੇਅਰ 4x RTX8000 (ਪ੍ਰਤੀ GPU 48GB RAM) 'ਤੇ ਟੈਸਟ ਕੀਤਾ ਗਿਆ ਹੈ।

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ਹੁਣ ਬਹੁ-ਇਮੇਜ ਇਨਪੁਟਸ ਨੂੰ ਅਧਿਕਾਰਕ ਤੌਰ 'ਤੇ ਸਮਰਥਨ ਕਰਦਾ ਹੈ। ਇੱਥੇ NLVR2 ਨੂੰ ਫਾਈਨਟਿਊਨ ਕਰਨ ਲਈ ਇੱਕ ਉਦਾਹਰਣ ਹੈ।

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## ਵਰਤੋਂ ਗਾਈਡ

ਹਾਰਡਵੇਅਰ ਦੇ ਆਧਾਰ 'ਤੇ, ਯੂਜ਼ਰ ਵੱਖ-ਵੱਖ ਫਾਈਨਟਿਊਨਿੰਗ ਰਣਨੀਤੀਆਂ ਦੀ ਚੋਣ ਕਰ ਸਕਦੇ ਹਨ। ਅਸੀਂ ਸਮੂਹ ਫਾਈਨਟਿਊਨਿੰਗ (Deepspeed Zero-2 ਨਾਲ) ਅਤੇ ਜ਼ਰੂਰੀ ਤੌਰ 'ਤੇ ਫ੍ਰੀਜ਼ ਕੀਤੇ ਗਏ ਵਿਜ਼ਨ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ, ਅਤੇ LoRA (4bit QLoRA ਸਮੇਤ) ਨੂੰ ਸਮਰਥਨ ਕਰਦੇ ਹਾਂ।  
ਆਮ ਤੌਰ 'ਤੇ, ਜਿੱਥੇ ਸੰਭਵ ਹੋਵੇ, ਅਸੀਂ flash attention ਅਤੇ bf16 ਦੇ ਨਾਲ ਸਮੂਹ ਫਾਈਨਟਿਊਨਿੰਗ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ।

### ਤੁਹਾਡੇ ਕਸਟਮ ਡੇਟਾਸੈਟ ਨੂੰ ਲੋੜੀਂਦੇ ਫਾਰਮੈਟ ਵਿੱਚ ਕਨਵਰਟ ਕਰਨ ਲਈ ਗਾਈਡ

ਅਸੀਂ ਘੱਟੋ-ਘੱਟ ਵੀਡੀਓ ਕਲਾਸੀਫਿਕੇਸ਼ਨ ਡੇਟਾਸੈਟ (UCF-101 ਦਾ ਇੱਕ ਸਬਸੈਟ) ਨੂੰ ਇੱਕ ਅੰਤ-ਤੱਕ-ਅੰਤ ਉਦਾਹਰਣ ਵਜੋਂ ਵਰਤਦੇ ਹਾਂ, ਇਹ ਦਿਖਾਉਣ ਲਈ ਕਿ ਤੁਹਾਡੇ ਕਸਟਮ ਡੇਟਾਸੈਟ ਨੂੰ ਲੋੜੀਂਦੇ ਫਾਰਮੈਟ ਵਿੱਚ ਕਿਵੇਂ ਕਨਵਰਟ ਕਰਨਾ ਹੈ ਅਤੇ ਇਸ 'ਤੇ Phi-3.5-vision ਨੂੰ ਕਿਵੇਂ ਫਾਈਨਟਿਊਨ ਕਰਨਾ ਹੈ।

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

ਕਨਵਰਟ ਕੀਤਾ ਡਾਟਾ ਇਸ ਤਰ੍ਹਾਂ ਦੇਖੇਗਾ:

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

`jsonl` ਐਨੋਟੇਸ਼ਨ ਲਈ, ਹਰ ਲਾਈਨ ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

ਨੋਟ ਕਰੋ ਕਿ `conversations` ਇੱਕ ਸੂਚੀ ਹੈ, ਇਸ ਲਈ ਜੇਕਰ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਡਾਟਾ ਉਪਲਬਧ ਹੈ, ਤਾਂ ਬਹੁ-ਟਰਨ ਗੱਲਬਾਤ ਦਾ ਸਮਰਥਨ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

## Azure GPU ਕੋਟਾ ਦੀ ਬੇਨਤੀ ਕਰਨਾ

### ਪੂਰਵ ਸ਼ਰਤਾਂ

Contributor ਰੋਲ (ਜਾਂ Contributor ਐਕਸੈੱਸ ਵਾਲੇ ਕਿਸੇ ਹੋਰ ਰੋਲ) ਦੇ ਨਾਲ ਇੱਕ Azure ਖਾਤਾ।  
ਜੇ ਤੁਹਾਡੇ ਕੋਲ Azure ਖਾਤਾ ਨਹੀਂ ਹੈ, ਤਾਂ [ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਮੁਫ਼ਤ ਖਾਤਾ ਬਣਾਓ](https://azure.microsoft.com)।

### ਕੋਟਾ ਵਾਧੇ ਦੀ ਬੇਨਤੀ

ਤੁਸੀਂ My quotas ਤੋਂ ਸਿੱਧੇ ਹੀ ਕੋਟਾ ਵਾਧੇ ਦੀ ਬੇਨਤੀ ਕਰ ਸਕਦੇ ਹੋ। ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ। ਇਸ ਉਦਾਹਰਣ ਲਈ, ਤੁਸੀਂ ਆਪਣੇ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਵਿੱਚ ਕਿਸੇ ਵੀ ਸਮਰਥਨਯੋਗ ਕੋਟਾ ਦੀ ਚੋਣ ਕਰ ਸਕਦੇ ਹੋ।

[Azure ਪੋਰਟਲ](https://portal.azure.com) ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ।

ਖੋਜ ਬਾਕਸ ਵਿੱਚ "quotas" ਦਾਖਲ ਕਰੋ, ਅਤੇ ਫਿਰ Quotas ਚੁਣੋ।  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

ਓਵਰਵਿਊ ਪੇਜ 'ਤੇ, ਇੱਕ ਪ੍ਰੋਵਾਈਡਰ ਚੁਣੋ, ਜਿਵੇਂ ਕਿ Compute ਜਾਂ AML।

**ਨੋਟ** Compute ਤੋਂ ਇਲਾਵਾ ਬਾਕੀ ਸਾਰੇ ਪ੍ਰੋਵਾਈਡਰਾਂ ਲਈ, ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਵਰਣਨ ਕੀਤੇ Adjustable ਕਾਲਮ ਦੀ ਬਜਾਏ Request increase ਕਾਲਮ ਦੇਖਣ ਨੂੰ ਮਿਲੇਗਾ। ਇੱਥੇ, ਤੁਸੀਂ ਕਿਸੇ ਖਾਸ ਕੋਟਾ ਲਈ ਵਾਧੇ ਦੀ ਬੇਨਤੀ ਕਰ ਸਕਦੇ ਹੋ ਜਾਂ ਵਾਧੇ ਲਈ ਸਹਾਇਤਾ ਬੇਨਤੀ ਬਣਾ ਸਕਦੇ ਹੋ।

My quotas ਪੇਜ 'ਤੇ, Quota name ਦੇ ਹੇਠਾਂ, ਉਹ ਕੋਟਾ ਚੁਣੋ ਜਿਸ ਵਿੱਚ ਤੁਸੀਂ ਵਾਧਾ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਇਸ ਕੋਟਾ ਲਈ Adjustable ਕਾਲਮ "Yes" ਦਿਖਾਉਂਦਾ ਹੈ।

ਪੇਜ ਦੇ ਸਿਖਰ 'ਤੇ, New Quota Request ਚੁਣੋ, ਫਿਰ Enter a new limit ਚੁਣੋ।  
![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request ਪੈਨ ਵਿੱਚ, ਆਪਣੇ ਨਵੇਂ ਕੋਟਾ ਸੀਮਾ ਲਈ ਇੱਕ ਨੰਬਰਕ ਮੁੱਲ ਦਾਖਲ ਕਰੋ, ਫਿਰ Submit ਚੁਣੋ।

ਤੁਹਾਡੀ ਬੇਨਤੀ ਦੀ ਸਮੀਖਿਆ ਕੀਤੀ ਜਾਵੇਗੀ, ਅਤੇ ਤੁਹਾਨੂੰ ਸੂਚਿਤ ਕੀਤਾ ਜਾਵੇਗਾ ਕਿ ਕੀ ਬੇਨਤੀ ਪੂਰੀ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। ਇਹ ਆਮ ਤੌਰ 'ਤੇ ਕੁਝ ਮਿੰਟਾਂ ਵਿੱਚ ਹੁੰਦਾ ਹੈ।

ਜੇਕਰ ਤੁਹਾਡੀ ਬੇਨਤੀ ਪੂਰੀ ਨਹੀਂ ਕੀਤੀ ਜਾਂਦੀ, ਤਾਂ ਤੁਹਾਨੂੰ ਸਹਾਇਤਾ ਬੇਨਤੀ ਬਣਾਉਣ ਲਈ ਇੱਕ ਲਿੰਕ ਦੇਖਣ ਨੂੰ ਮਿਲੇਗਾ। ਜਦੋਂ ਤੁਸੀਂ ਇਸ ਲਿੰਕ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋ, ਤਾਂ ਇੱਕ ਸਹਾਇਤਾ ਇੰਜੀਨੀਅਰ ਤੁਹਾਡੀ ਵਾਧੇ ਦੀ ਬੇਨਤੀ ਵਿੱਚ ਤੁਹਾਡੀ ਮਦਦ ਕਰੇਗਾ।

## Azure Compute GPU ਮਸ਼ੀਨ SKU ਸੁਝਾਅ

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

ਇੱਥੇ ਕੁਝ ਉਦਾਹਰਣ ਹਨ:

### ਜੇ ਤੁਹਾਡੇ ਕੋਲ A100 ਜਾਂ H100 GPUs ਹਨ

ਪੂਰੀ ਫਾਈਨਟਿਊਨਿੰਗ ਆਮ ਤੌਰ 'ਤੇ ਸਭ ਤੋਂ ਵਧੀਆ ਪ੍ਰਦਰਸ਼ਨ ਦਿੰਦੀ ਹੈ। ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3-V ਨੂੰ hateful memes ਕਲਾਸੀਫਿਕੇਸ਼ਨ 'ਤੇ ਫਾਈਨਟਿਊਨ ਕਰ ਸਕਦੇ ਹੋ।

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### ਜੇ ਤੁਹਾਡੇ ਕੋਲ Standard_ND40rs_v2 8x V100-32GB GPUs ਹਨ

ਤੁਹਾਡੇ ਲਈ Phi-3-V ਨੂੰ hateful memes ਕਲਾਸੀਫਿਕੇਸ਼ਨ 'ਤੇ ਪੂਰੀ ਤਰ੍ਹਾਂ ਫਾਈਨਟਿਊਨ ਕਰਨਾ ਸੰਭਵ ਹੈ। ਪਰ, A100 ਜਾਂ H100 GPUs ਨਾਲ ਤੁਲਨਾ ਕਰਦੇ ਹੋਏ throughput ਕਾਫ਼ੀ ਘੱਟ ਹੋਵੇਗਾ ਕਿਉਂਕਿ flash attention ਸਮਰਥਨ ਦੀ ਘਾਟ ਹੈ।  
ਅਕੁਰਸੀ 'ਤੇ ਵੀ ਪ੍ਰਭਾਵ ਪੈ ਸਕਦਾ ਹੈ ਕਿਉਂਕਿ bf16 ਸਮਰਥਨ ਦੀ ਘਾਟ ਹੈ (fp16 ਮਿਕਸਡ-ਪ੍ਰਿਸੀਜ਼ਨ ਟ੍ਰੇਨਿੰਗ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ)।

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਡਾਟਾ ਸੈਂਟਰ GPUs ਤੱਕ ਪਹੁੰਚ ਨਹੀਂ ਹੈ

LoRA ਤੁਹਾਡਾ ਇੱਕੋ ਮਾਤਰ ਵਿਕਲਪ ਹੋ ਸਕਦਾ ਹੈ। ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3-V ਨੂੰ hateful memes ਕਲਾਸੀਫਿਕੇਸ਼ਨ 'ਤੇ ਫਾਈਨਟਿਊਨ ਕਰ ਸਕਦੇ ਹੋ।

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU ਲਈ, QLoRA ਸਮਰਥਿਤ ਹੈ।

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## ਸੁਝਾਏ ਗਏ ਹਾਈਪਰਪੈਰਾਮੀਟਰ ਅਤੇ ਉਮੀਦਵਾਰ ਅਕੁਰਸੀ

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

Training method | Frozen vision model | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
LoRA results comming soon |  |  |  |  |  |  |  |  |

### ਨੋਟ

ਹੇਠਾਂ ਦਿੱਤੇ DocVQA ਅਤੇ Hateful memes ਦੇ ਨਤੀਜੇ ਪਿਛਲੇ ਵਰਜਨ (Phi-3-vision) 'ਤੇ ਆਧਾਰਿਤ ਹਨ।  
ਨਵੇਂ ਨਤੀਜੇ Phi-3.5-vision ਨਾਲ ਜਲਦ ਅਪਡੇਟ ਕੀਤੇ ਜਾਣਗੇ।

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

Training method | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
frozen image model | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
frozen image model | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
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

Training method | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
frozen image model | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
frozen image model | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## ਗਤੀ ਬੈਂਚਮਾਰਕਿੰਗ (NOTE: Phi-3-vision)

Phi-3.5-vision ਨਾਲ ਨਵੇਂ ਬੈਂਚਮਾਰਕਿੰਗ ਨਤੀਜੇ ਜਲਦ ਅਪਡੇਟ ਕੀਤੇ ਜਾਣਗੇ।

ਗਤੀ ਬੈਂਚਮਾਰਕਿੰਗ DocVQA ਡੇਟਾਸੈਟ 'ਤੇ ਕੀਤੀ ਗਈ ਹੈ। ਇਸ ਡੇਟਾਸੈਟ ਦੀ ਔਸਤ ਸੀਕਵੈਂਸ ਲੰਬਾਈ 2443.23 ਟੋਕਨ ਹੈ (`num_crops=16` ਇਮੇਜ ਮਾਡਲ ਲਈ ਵਰਤਿਆ ਗਿਆ)।

### 8x A100-80GB (Ampere)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 | 1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
frozen image model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
frozen image model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 2.462 | 1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## ਜਾਣੇ-ਪਛਾਣੇ ਮੁੱਦੇ

- fp16 ਨਾਲ flash attention ਨਹੀਂ ਚੱਲ ਸਕਦਾ (bf16 ਹਮੇਸ਼ਾ ਸਿਫਾਰਸ਼ੀ ਹੈ ਜਿੱਥੇ ਉਪਲਬਧ ਹੋਵੇ, ਅਤੇ ਸਾਰੇ GPUs ਜੋ flash attention ਨੂੰ ਸਮਰਥਨ ਕਰਦੇ ਹਨ ਉਹ bf16 ਨੂੰ ਵੀ ਸਮਰਥਨ ਕਰਦੇ ਹਨ)।  
- ਵਿਚਕਾਰਲੇ ਚੈਕਪੋਇੰਟਸ ਨੂੰ ਸੇਵ ਕਰਨ ਅਤੇ ਟ੍ਰੇਨਿੰਗ ਨੂੰ ਮੁੜ ਸ਼ੁਰੂ ਕਰਨ ਦਾ ਸਮਰਥਨ ਅਜੇ ਤੱਕ ਨਹੀਂ ਹੈ।

**ਅਸਵੀਕਾਰਨਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ-ਅਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੱਜੇਪਨ ਹੋ ਸਕਦੇ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਪ੍ਰਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।