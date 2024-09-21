# Phi-3.5-vision 微调教程

这是使用 Huggingface 库进行 Phi-3.5-vision 微调的官方支持。请在运行以下命令之前，先 `cd` 到代码目录 [vision_finetuning](../../../../code/04.Finetuning/vision_finetuning)。

## 安装

```bash
# 创建一个新的 conda 环境
conda create -n phi3v python=3.10
conda activate phi3v

# 安装 pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# 运行示例代码所需的其他库
pip install -r requirements.txt

# （可选）flash attention -- Ampere+ GPU (例如 A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# （可选）QLoRA -- Turing+ GPU (例如 RTX 8000)
pip install bitsandbytes==0.43.1
```

## 快速开始

我们提供了两个示例微调脚本，一个用于 DocVQA，一个用于仇恨言论分类。

在 4x RTX8000 (每个 GPU 48GB RAM) 上测试的最低硬件要求
```bash
# 在 DocVQA 的 mini-train 分割上运行最小脚本
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision 现在正式支持多图像输入。以下是微调 NLVR2 的示例
```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 使用指南
根据硬件的不同，用户可以选择不同的微调策略。我们支持全微调（使用 Deepspeed Zero-2）并可选冻结视觉参数，以及 LoRA（包括 4bit QLoRA）。一般来说，我们建议尽可能使用 flash attention 和 bf16 进行全微调。

### 将自定义数据集转换为所需格式的指南

我们使用一个最小的视频分类数据集（UCF-101 的子集）作为端到端示例，展示如何将自定义数据集转换为所需格式并在其上微调 Phi-3.5-vision。

```bash
# 转换数据
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# 训练
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

转换后的数据将如下所示：
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

对于 `jsonl` 注释，每一行应为一个字典，如：
```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

注意 `conversations` 是一个列表，因此如果有这样的数据，可以支持多轮对话。

## 请求 Azure GPU 配额

### 先决条件
拥有 Contributor 角色（或其他包含 Contributor 访问权限的角色）的 Azure 账户。

如果你还没有 Azure 账户，请在开始之前创建一个 [免费账户](https://azure.microsoft.com)。

### 请求配额增加
你可以直接从“我的配额”提交配额增加请求。按照以下步骤为配额请求增加。对于这个示例，你可以选择订阅中的任何可调配额。

登录 [Azure 门户](https://portal.azure.com)。

在搜索框中输入“配额”，然后选择配额。
![配额](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

在概览页面中，选择一个提供者，例如 Compute 或 AML。

**注意** 对于 Compute 以外的所有提供者，你将看到一个“请求增加”列，而不是下面描述的“可调”列。在那里，你可以请求增加特定配额，或创建支持请求来增加。

在“我的配额”页面中，在“配额名称”下选择你想增加的配额。确保该配额的“可调”列显示为“是”。

在页面顶部附近，选择“新配额请求”，然后选择“输入新限制”。

![增加配额](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

在“新配额请求”窗格中，输入新配额限制的数值，然后选择“提交”。

你的请求将被审核，如果请求可以实现，你将收到通知。通常在几分钟内完成。

如果你的请求没有实现，你将看到一个创建支持请求的链接。当你使用此链接时，支持工程师将协助你增加请求。

## Azure Compute GPU 机器 SKU 建议

[ND A100 v4 系列](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5 系列](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

以下是一些示例：

### 如果你有 A100 或 H100 GPU
全微调通常能提供最佳性能。你可以使用以下命令微调 Phi-3-V 进行仇恨言论分类。

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
仍然可以完全微调 Phi-3-V 进行仇恨言论分类。然而，由于缺乏 flash attention 支持，预期吞吐量会比 A100 或 H100 GPU 低得多。由于缺乏 bf16 支持（而是使用 fp16 混合精度训练），准确性也可能受到影响。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### 如果你没有数据中心 GPU
LoRA 可能是你的唯一选择。你可以使用以下命令微调 Phi-3-V 进行仇恨言论分类。

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

对于 Turing+ GPU，支持 QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## 建议的超参数和预期准确率
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

训练方法 | 冻结视觉模型 | 数据类型 | LoRA rank | LoRA alpha | batch size | learning rate | epochs | 准确率
--- | --- | --- | --- | --- | --- | --- | --- | --- |
全微调 |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
全微调 | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA 结果即将公布 |  |  |  |  |  |  |  |  |

### 注意
以下 DocVQA 和仇恨言论结果基于之前版本（Phi-3-vision）。
使用 Phi-3.5-vision 的新结果将很快更新。

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

训练方法 | 数据类型 | LoRA rank | LoRA alpha | batch size | learning rate | epochs | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
全微调 | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
全微调 | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
冻结图像模型 | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
冻结图像模型 | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### 仇恨言论（注意：Phi-3-vision）
```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>
```

训练方法 | 数据类型 | LoRA rank | LoRA alpha | batch size | learning rate | epochs | 准确率
--- | --- | --- | --- | --- | --- | --- | --- |
全微调 | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
全微调 | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
冻结图像模型 | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
冻结图像模型 | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## 速度基准测试（注意：Phi-3-vision）
使用 Phi-3.5-vision 的新基准测试结果将很快更新。
速度基准测试在 DocVQA 数据集上进行。该数据集的平均序列长度为 2443.23 个标记（使用 `num_crops=16` 对于图像模型）。

### 8x A100-80GB (Ampere)
训练方法 | \# 节点 | GPU | flash attention | 有效 batch size | 吞吐量 (img/s) | 加速 | 峰值 GPU 内存 (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
全微调 | 1 | 8 | | 64 | 5.041
| 1x | ~42 全微调 | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36 全微调 | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29 全微调 | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26 冻结图像模型 | 1 | 8 | | 64 | 17.578 | 3.49x | ~29 冻结图像模型 | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27 LoRA | 1 | 8 | | 64 | 5.591 | 1.11x | ~50 LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16 QLoRA | 1 | 8 | | 64 | 4.831 | 0.96x | ~32 QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10 ### 8x V100-32GB (Volta) 训练方法 | \# 节点 | GPUs | flash attention | 有效批量大小 | 吞吐量 (img/s) | 加速 | 峰值 GPU 内存 (GB) --- | --- | --- | --- | --- | --- | --- | --- | 全微调 | 1 | 8 | | 64 | 2.462 | 1x | ~32 全微调 | 2 | 16 | | 64 | 4.182 | 1.70x | ~32 全微调 | 4 | 32 | | 64 | 5.465 | 2.22x | ~32 冻结图像模型 | 1 | 8 | | 64 | 8.942 | 3.63x | ~27 LoRA | 1 | 8 | | 64 | 2.807 | 1.14x | ~30 ## 已知问题 - 无法在 fp16 下运行 flash attention（当可用时，始终推荐使用 bf16，并且所有支持 flash attention 的 GPU 也支持 bf16）。 - 目前不支持保存中间检查点和恢复训练。

免责声明：该翻译由AI模型从原文翻译而来，可能不完美。请审阅输出并进行必要的修正。