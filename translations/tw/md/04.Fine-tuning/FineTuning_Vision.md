# Phi-3.5-vision 微調教學

這是使用 huggingface 庫進行 Phi-3.5-vision 微調的官方支持。
在執行以下指令前，請先 `cd` 到代碼目錄 [vision_finetuning](../../../../code/04.Finetuning/vision_finetuning)。

## 安裝

```bash
# 創建一個新的 conda 環境
conda create -n phi3v python=3.10
conda activate phi3v

# 安裝 pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# 安裝運行示例代碼所需的其他庫
pip install -r requirements.txt

# (可選) 安裝 flash attention -- Ampere+ GPU (例如，A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (可選) 安裝 QLoRA -- Turing+ GPU (例如，RTX 8000)
pip install bitsandbytes==0.43.1
```

## 快速開始

我們提供了兩個示例微調腳本，一個用於 DocVQA，一個用於仇恨表情分類。

最低硬件需求為 4x RTX8000 (每個 GPU 有 48GB RAM)
```bash
# 在 DocVQA 的 mini-train split 上運行最簡單的腳本
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision 現在正式支持多圖像輸入。以下是微調 NLVR2 的示例
```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 使用指南
根據硬件配置，使用者可以選擇不同的微調策略。我們支持全量微調（使用 Deepspeed Zero-2），可選擇凍結視覺參數，以及 LoRA（包括 4bit QLoRA）。一般來說，我們建議在可能的情況下使用全量微調並啟用 flash attention 和 bf16。

### 將自定義數據集轉換為所需格式的指南

我們使用一個最小的視頻分類數據集（UCF-101 的子集）作為端到端示例，展示如何將自定義數據集轉換為所需格式並在其上微調 Phi-3.5-vision。

```bash
# 轉換數據
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# 訓練
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

轉換後的數據將如下所示：
```
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

對於 `jsonl` 標註，每行應該是一個類似這樣的字典：
```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

注意 `conversations` 是一個列表，因此如果有多輪對話數據，也可以支持。

## 申請 Azure GPU 配額 

### 先決條件
擁有具備 Contributor 角色（或其他包含 Contributor 訪問權限的角色）的 Azure 帳戶。

如果您還沒有 Azure 帳戶，請先創建一個 [免費帳戶](https://azure.microsoft.com)。

### 申請配額增加
您可以直接從 "My quotas" 提交配額增加請求。按照以下步驟申請配額增加。以本例為例，您可以選擇訂閱中的任何可調整配額。

登入 [Azure 入口網站](https://portal.azure.com)。

在搜索框中輸入 "quotas"，然後選擇 Quotas。
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

在概覽頁面中，選擇一個提供者，例如 Compute 或 AML。

**注意** 對於 Compute 以外的所有提供者，您將看到 "Request increase" 列，而不是下面描述的 "Adjustable" 列。在這裡，您可以申請特定配額的增加，或創建支持請求以增加配額。

在 "My quotas" 頁面中，在 "Quota name" 下選擇您要增加的配額。確保該配額的 "Adjustable" 列顯示為 Yes。

在頁面頂部附近，選擇 "New Quota Request"，然後選擇 "Enter a new limit"。

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

在 "New Quota Request" 窗格中，輸入您的新配額限制的數值，然後選擇 "Submit"。

您的請求將被審核，並通知您是否可以滿足該請求。通常會在幾分鐘內完成。

如果您的請求未能滿足，您將看到一個鏈接以創建支持請求。使用此鏈接時，支持工程師將協助您增加配額。

## Azure Compute GPU 機器 SKU 建議

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

以下是一些示例：

### 如果您擁有 A100 或 H100 GPU
全量微調通常能提供最佳性能。您可以使用以下命令在仇恨表情分類上微調 Phi-3-V。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### 如果您擁有 Standard_ND40rs_v2 8x V100-32GB GPU
仍然可以在仇恨表情分類上全量微調 Phi-3-V。然而，由於缺乏 flash attention 支持，吞吐量會顯著降低。由於缺乏 bf16 支持（改用 fp16 混合精度訓練），準確性也可能受到影響。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### 如果您無法使用數據中心 GPU
Lora 可能是您唯一的選擇。您可以使用以下命令在仇恨表情分類上微調 Phi-3-V。

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

訓練方法 | 凍結視覺模型 | 數據類型 | LoRA rank | LoRA alpha | 批次大小 | 學習率 | 紀元 | 準確性
--- | --- | --- | --- | --- | --- | --- | --- | --- |
全量微調 |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
全量微調 | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA 結果即將發布 |  |  |  |  |  |  |  |  |

### 注意
以下 DocVQA 和 Hateful memes 結果基於之前版本（Phi-3-vision）。
使用 Phi-3.5-vision 的新結果將很快更新。

### DocVQA (注意：Phi-3-vision)
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

訓練方法 | 數據類型 | LoRA rank | LoRA alpha | 批次大小 | 學習率 | 紀元 | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
全量微調 | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
全量微調 | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
凍結圖像模型 | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
凍結圖像模型 | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (注意：Phi-3-vision)
```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>
```

訓練方法 | 數據類型 | LoRA rank | LoRA alpha | 批次大小 | 學習率 | 紀元 | 準確性
--- | --- | --- | --- | --- | --- | --- | --- |
全量微調 | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
全量微調 | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
凍結圖像模型 | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
凍結圖像模型 | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## 速度基準測試 (注意：Phi-3-vision)
使用 Phi-3.5-vision 的新基準測試結果將很快更新。速度基準測試是在 DocVQA 數據集上進行的。該數據集的平均序列長度為 2443.23 個標記（對圖像模型使用 `num_crops=16`）。

### 
| 1x | ~42 full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36 full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29 full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26 frozen image model | 1 | 8 | | 64 | 17.578 | 3.49x | ~29 frozen image model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27 LoRA | 1 | 8 | | 64 | 5.591 | 1.11x | ~50 LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16 QLoRA | 1 | 8 | | 64 | 4.831 | 0.96x | ~32 QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10 ### 8x V100-32GB (Volta) Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB) --- | --- | --- | --- | --- | --- | --- | --- | full-finetuning | 1 | 8 | | 64 | 2.462 | 1x | ~32 full-finetuning | 2 | 16 | | 64 | 4.182 | 1.70x | ~32 full-finetuning | 4 | 32 | | 64 | 5.465 | 2.22x | ~32 frozen image model | 1 | 8 | | 64 | 8.942 | 3.63x | ~27 LoRA | 1 | 8 | | 64 | 2.807 | 1.14x | ~30 ## Known issues - Cannot run flash attention with fp16 (bf16 is always recommended when available, and all GPUs supporting flash attention also support bf16). - Do not support saving intermediate checkpoints and resuming training yet.

免責聲明：此翻譯由AI模型從原文翻譯而來，可能不夠完美。請檢查翻譯結果並進行必要的修正。