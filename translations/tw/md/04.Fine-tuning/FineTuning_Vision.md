# Phi-3.5-vision 微调教程

這是使用 huggingface 庫進行 Phi-3.5-vision 微调的官方支持。
請將`cd`複製到代碼目錄 [vision_finetuning](../../../../code/04.Finetuning/vision_finetuning) 之後運行以下命令。

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

我們提供了兩個示例微调腳本，一個用於 DocVQA，另一個用於仇恨模因分類。

最低硬件要求：4x RTX8000（每個 GPU 48GB RAM）

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision 現在正式支持多圖像輸入。這裡是一個微调 NLVR2 的示例

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 使用指南

根據硬件的不同，用戶可以選擇不同的微调策略。我們支持全量微调（使用 Deepspeed Zero-2），可選擇凍結視覺參數，以及 LoRA（包括 4bit QLoRA）。
一般來說，我們建議在可能的情況下使用帶有 flash attention 和 bf16 的全量微调。

### 將自定義數據集轉換為所需格式的指南

我們使用一個最小的視頻分類數據集（UCF-101 的子集）作為端到端示例，演示如何將自定義數據集轉換為所需格式並在其上微调 Phi-3.5-vision。

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

轉換後的數據將如下所示：

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

對於 `jsonl` 註釋，每行應該是一個字典，如：

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

請注意，`conversations` 是一個列表，因此如果有多輪對話數據，也可以支持。

## 請求 Azure GPU 配額 

### 先決條件

擁有具有貢獻者角色（或包含貢獻者訪問權限的其他角色）的 Azure 帳戶。

如果你還沒有 Azure 帳戶，請在開始之前創建一個[免費帳戶](https://azure.microsoft.com)。

### 請求配額增加

你可以直接從我的配額提交配額增加請求。按照以下步驟請求增加配額。在此示例中，你可以選擇訂閱中的任何可調整配額。

登錄 [Azure 入口網站](https://portal.azure.com)。

在搜索框中輸入 "quotas"，然後選擇 Quotas。
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

在概覽頁面中，選擇一個提供者，例如 Compute 或 AML。

**注意** 對於除 Compute 之外的所有提供者，你將看到一個請求增加列，而不是下面描述的可調整列。在那裡，你可以請求增加特定配額，或創建支持請求以增加配額。

在我的配額頁面中，在配額名稱下，選擇你想增加的配額。確保此配額的可調整列顯示為 Yes。

在頁面頂部附近，選擇新配額請求，然後選擇輸入新限制。

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

在新配額請求窗格中，輸入新配額限制的數值，然後選擇提交。

你的請求將被審核，如果請求可以滿足，你將收到通知。這通常在幾分鐘內發生。

如果你的請求未能滿足，你將看到創建支持請求的鏈接。使用此鏈接時，支持工程師將協助你進行增加請求。

## Azure 計算 GPU 機器 SKU 建議

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

以下是一些示例：

### 如果你有 A100 或 H100 GPU

全量微调通常能提供最佳性能。你可以使用以下命令對仇恨模因分類進行微调 Phi-3-V。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### 如果你有 Standard_ND40rs_v2 8x V100-32GB GPU

仍然可以對仇恨模因分類進行全量微调 Phi-3-V。然而，由於缺乏 flash attention 支持，預期吞吐量會比 A100 或 H100 GPU 低得多。
由於缺乏 bf16 支持（使用 fp16 混合精度訓練代替），準確性也可能受到影響。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### 如果你無法訪問數據中心 GPU
Lora 可能是你唯一的選擇。你可以使用以下命令對仇恨模因分類進行微调 Phi-3-V。

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

對於 Turing+ GPU，支持 QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## 建議的超參數和預期準確性
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

訓練方法 | 凍結視覺模型 | 數據類型 | LoRA 等級 | LoRA alpha | 批次大小 | 學習率 | 週期 | 準確性
--- | --- | --- | --- | --- | --- | --- | --- | --- |
全量微调 |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
全量微调 | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA 結果即將發布 |  |  |  |  |  |  |  |  |

### 注意
以下 DocVQA 和仇恨模因結果基於先前版本（Phi-3-vision）。
使用 Phi-3.5-vision 的新結果將很快更新。

### DocVQA（注意：Phi-3-vision）

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

訓練方法 | 數據類型 | LoRA 等級 | LoRA alpha | 批次大小 | 學習率 | 週期 | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
全量微调 | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
全量微调 | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
凍結圖像模型| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
凍結圖像模型| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### 仇恨模因（注意：Phi-3-vision）

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

訓練方法 | 數據類型 | LoRA 等級 | LoRA alpha | 批次大小 | 學習率 | 週期 | 準確性
--- | --- | --- | --- | --- | --- | --- | --- |
全量微调 | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
全量微调 | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
凍結圖像模型| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
凍結圖像模型| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## 速度基準測試（注意：Phi-3-vision）

使用 Phi-3.5-vision 的新基準測試結果將很快更新。

速度基準測試在 DocVQA 數據集上進行。此數據集的平均序列長度為 2443.23 個標記（對圖像模型使用 `num_crops=16`）。

### 8x A100-80GB（Ampere）

訓練方法 | \# 節點 | GPUs | flash attention | 有效批次大小 | 吞吐量（img/s） | 加速 | 峰值 GPU 記憶體（GB）
--- | --- | --- | --- | --- | --- | --- | --- |
全量微调 | 1 | 8 |  | 64 | 5.041 |  1x | ~42
全量微调 | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
全量微调 | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
全量微调 | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
凍結圖像模型 | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
凍結圖像模型 | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB（Volta）

訓練方法 | \# 節點 | GPUs | flash attention | 有效批次大小 | 吞吐量（img/s） | 加速 | 峰值 GPU 記憶體（GB）
--- | --- | --- | --- | --- | --- | --- | --- |
全量微调 | 1 | 8 | | 64 | 2.462 |  1x | ~32
全量微调 | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
全量微调 | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
凍結圖像模型 | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## 已知問題

- 無法使用 fp16 運行 flash attention（在可能的情況下總是推薦使用 bf16，所有支持 flash attention 的 GPU 也支持 bf16）。
- 尚不支持保存中間檢查點和恢復訓練。

**免責聲明**：
本文件使用機器翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或誤讀不承擔責任。