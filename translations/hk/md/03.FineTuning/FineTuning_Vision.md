# Phi-3.5-vision 微調配方

呢份係使用 Huggingface libraries 進行 Phi-3.5-vision 微調嘅官方指引。  
請 `cd` 到 [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) 呢個程式碼目錄，然後再執行以下指令。

## 安裝

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

## 快速開始

我哋提供咗兩個微調嘅示例腳本，一個係用於 DocVQA，另一個係用於仇恨 meme 分類。

最低硬件需求：4x RTX8000 (每張 GPU 有 48GB RAM)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision 而家正式支援多圖片輸入。以下係用 NLVR2 進行微調嘅示例：

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 使用指南

根據硬件條件，使用者可以選擇唔同嘅微調策略。我哋支援全微調（使用 Deepspeed Zero-2）同可選擇性凍結視覺參數，亦支援 LoRA（包括 4bit QLoRA）。  
一般情況下，我哋建議盡可能使用全微調，加上 flash attention 同 bf16。

### 自定數據集格式轉換指南

我哋會用一個最少嘅視頻分類數據集（UCF-101 子集）作為端到端示例，示範點樣將自定數據集轉換為所需格式，並喺上面微調 Phi-3.5-vision。

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

轉換後嘅數據會係咁樣嘅：

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

至於 `jsonl` 註解，每行應該係一個字典，例如：

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

請注意，`conversations` 係一個列表，所以如果有多輪對話數據，都可以支援。

## 申請 Azure GPU 配額 

### 先決條件

擁有 Contributor 角色（或其他包含 Contributor 訪問權限嘅角色）嘅 Azure 帳戶。

如果你仲未有 Azure 帳戶，可以先創建一個 [免費帳戶](https://azure.microsoft.com)。

### 申請配額提升

你可以直接喺 My quotas 提交配額提升申請。以下係申請提升配額嘅步驟。喺呢個例子中，你可以選擇訂閱中任何可調整嘅配額。

登入 [Azure portal](https://portal.azure.com)。

喺搜尋框輸入 "quotas"，然後揀選 Quotas。
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

喺概覽頁面，揀選一個供應商，例如 Compute 或 AML。

**注意** 除咗 Compute 嘅供應商外，你會見到 Request increase 呢一欄，而唔係 Adjustable 呢一欄。你可以為特定配額申請提升，或者創建支援請求嚟提升配額。

喺 My quotas 頁面，喺 Quota name 下揀選你想提升嘅配額。確保 Adjustable 呢一欄顯示為 Yes。

喺頁面頂部揀選 New Quota Request，然後揀選 Enter a new limit。

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

喺 New Quota Request 面板中，輸入新配額限制嘅數值，然後揀選 Submit。

你嘅請求會被審核，並喺幾分鐘內通知你請求是否被批准。

如果請求未被批准，你會見到一個連結，用嚟創建支援請求。使用呢個連結時，支援工程師會協助處理你嘅提升請求。

## Azure Compute GPU 機器 SKU 建議

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

以下係幾個例子：

### 如果你有 A100 或 H100 GPUs

全微調通常能提供最佳性能。你可以用以下指令微調 Phi-3-V 用於仇恨 meme 分類。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### 如果你有 Standard_ND40rs_v2 8x V100-32GB GPUs

你仍然可以完全微調 Phi-3-V 用於仇恨 meme 分類。不過，由於缺乏 flash attention 支援，吞吐量會比 A100 或 H100 GPUs 低得多。  
由於缺乏 bf16 支援（改用 fp16 混合精度訓練），準確度亦可能會受影響。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### 如果你冇數據中心 GPUs

LoRA 可能係唯一選擇。你可以用以下指令微調 Phi-3-V 用於仇恨 meme 分類。

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

對於 Turing+ GPU，支援 QLoRA。

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## 建議超參數同預期準確度
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

訓練方法 | 凍結視覺模型 | 數據類型 | LoRA rank | LoRA alpha | 批次大小 | 學習率 | epochs | 準確度
--- | --- | --- | --- | --- | --- | --- | --- | --- |
全微調 |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
全微調 | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA 結果即將公佈 |  |  |  |  |  |  |  |  |

### 注意
以下 DocVQA 同仇恨 meme 嘅結果基於舊版本（Phi-3-vision）。  
新版本 Phi-3.5-vision 嘅結果會盡快更新。

### DocVQA （注意：Phi-3-vision）

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

訓練方法 | 數據類型 | LoRA rank | LoRA alpha | 批次大小 | 學習率 | epochs | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
全微調 | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
全微調 | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
凍結圖像模型| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
凍結圖像模型| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### 仇恨 meme （注意：Phi-3-vision）

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

訓練方法 | 數據類型 | LoRA rank | LoRA alpha | 批次大小 | 學習率 | epochs | 準確度
--- | --- | --- | --- | --- | --- | --- | --- |
全微調 | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
全微調 | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
凍結圖像模型| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
凍結圖像模型| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## 性能基準測試（注意：Phi-3-vision）

基於 Phi-3.5-vision 嘅新測試結果會盡快更新。

性能基準測試係喺 DocVQA 數據集上進行嘅。呢個數據集嘅平均序列長度係 2443.23 tokens（對圖像模型使用 `num_crops=16`）。

### 8x A100-80GB (Ampere)

訓練方法 | 節點數量 | GPUs | flash attention | 有效批次大小 | 吞吐量 (img/s) | 加速比 | 峰值 GPU 記憶體 (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
全微調 | 1 | 8 |  | 64 | 5.041 |  1x | ~42
全微調 | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
全微調 | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
全微調 | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
凍結圖像模型 | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
凍結圖像模型 | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

訓練方法 | 節點數量 | GPUs | flash attention | 有效批次大小 | 吞吐量 (img/s) | 加速比 | 峰值 GPU 記憶體 (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
全微調 | 1 | 8 | | 64 | 2.462 |  1x | ~32
全微調 | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
全微調 | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
凍結圖像模型 | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## 已知問題

- 無法用 fp16 運行 flash attention（建議有 bf16 時使用 bf16，所有支援 flash attention 嘅 GPU 都支援 bf16）。
- 暫時唔支援保存中間檢查點同恢復訓練。

**免責聲明**:  
本文件使用機器人工智能翻譯服務進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀概不負責。