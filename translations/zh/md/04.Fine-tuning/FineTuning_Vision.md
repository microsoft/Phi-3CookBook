# Phi-3.5-vision 微调方案

这是使用 huggingface 库对 Phi-3.5-vision 进行微调的官方支持。
请先 `cd` 到代码目录 [vision_finetuning](../../../../code/04.Finetuning/vision_finetuning) 然后再运行以下命令。

## 安装

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

## 快速开始

我们提供了两个示例微调脚本，一个用于 DocVQA，另一个用于仇恨言论分类。

测试的最低硬件配置为 4x RTX8000 (每个 GPU 48GB RAM)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision 现在正式支持多图像输入。以下是微调 NLVR2 的示例

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 使用指南

根据硬件的不同，用户可以选择不同的微调策略。我们支持全量微调（使用 Deepspeed Zero-2），可选冻结视觉参数，以及 LoRA（包括 4bit QLoRA）。一般来说，我们推荐尽可能使用全量微调并结合 flash attention 和 bf16。

### 自定义数据集转换为所需格式的指南

我们使用一个最小的视频分类数据集（UCF-101 的子集）作为端到端示例，演示如何将自定义数据集转换为所需格式并在其上微调 Phi-3.5-vision。

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

转换后的数据将如下所示：

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

对于 `jsonl` 注释，每行应为一个字典，如下所示：

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

请注意，`conversations` 是一个列表，因此如果有多轮对话的数据，也可以支持。

## 请求 Azure GPU 配额

### 先决条件

拥有 Contributor 角色（或包含 Contributor 访问权限的其他角色）的 Azure 帐户。

如果您还没有 Azure 帐户，请先创建一个 [免费帐户](https://azure.microsoft.com)。

### 请求配额增加

您可以直接从我的配额提交配额增加请求。按照以下步骤请求配额增加。在此示例中，您可以选择订阅中的任何可调整配额。

登录到 [Azure 门户](https://portal.azure.com)。

在搜索框中输入“quotas”，然后选择配额。
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

在概览页面上，选择一个提供程序，例如 Compute 或 AML。

**注意** 对于 Compute 以外的所有提供程序，您将看到一个请求增加列，而不是下面描述的可调整列。在那里，您可以请求增加特定配额，或创建支持请求以增加配额。

在我的配额页面上，在配额名称下选择您要增加的配额。确保此配额的可调整列显示为是。

在页面顶部附近，选择新建配额请求，然后选择输入新限制。

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

在新配额请求窗格中，输入您的新配额限制的数值，然后选择提交。

您的请求将被审核，如果请求可以满足，您将收到通知。通常会在几分钟内完成。

如果您的请求未被满足，您将看到一个链接以创建支持请求。使用此链接时，支持工程师将协助您处理增加请求。

## Azure Compute GPU 机器 SKU 建议

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

以下是一些示例：

### 如果您有 A100 或 H100 GPU

全量微调通常能提供最佳性能。您可以使用以下命令微调 Phi-3-V 进行仇恨言论分类。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### 如果您有 Standard_ND40rs_v2 8x V100-32GB GPU

仍然可以对 Phi-3-V 进行全量微调进行仇恨言论分类。然而，由于缺乏 flash attention 支持，预计吞吐量会比 A100 或 H100 GPU 低得多。由于缺乏 bf16 支持（改用 fp16 混合精度训练），准确性也可能受到影响。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### 如果您无法访问数据中心 GPU
Lora 可能是您的唯一选择。您可以使用以下命令微调 Phi-3-V 进行仇恨言论分类。

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

训练方法 | 冻结视觉模型 | 数据类型 | LoRA 等级 | LoRA alpha | 批次大小 | 学习率 | 轮数 | 准确率
--- | --- | --- | --- | --- | --- | --- | --- | --- |
全量微调 |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
全量微调 | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA 结果即将发布 |  |  |  |  |  |  |  |  |

### 注意
以下 DocVQA 和仇恨言论分类结果基于之前的版本（Phi-3-vision）。
使用 Phi-3.5-vision 的新结果将很快更新。

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

训练方法 | 数据类型 | LoRA 等级 | LoRA alpha | 批次大小 | 学习率 | 轮数 | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
全量微调 | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
全量微调 | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
冻结图像模型| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
冻结图像模型| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### 仇恨言论分类（注意：Phi-3-vision）

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

训练方法 | 数据类型 | LoRA 等级 | LoRA alpha | 批次大小 | 学习率 | 轮数 | 准确率
--- | --- | --- | --- | --- | --- | --- | --- |
全量微调 | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
全量微调 | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
冻结图像模型| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
冻结图像模型| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## 速度基准测试（注意：Phi-3-vision）

使用 Phi-3.5-vision 的新基准测试结果将很快更新。

速度基准测试是在 DocVQA 数据集上进行的。该数据集的平均序列长度为 2443.23 个标记（使用 `num_crops=16` 进行图像模型）。

### 8x A100-80GB (Ampere)

训练方法 | \# 节点 | GPU | flash attention | 有效批次大小 | 吞吐量 (img/s) | 加速 | 峰值 GPU 内存 (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
全量微调 | 1 | 8 |  | 64 | 5.041 |  1x | ~42
全量微调 | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
全量微调 | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
全量微调 | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
冻结图像模型 | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
冻结图像模型 | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

训练方法 | \# 节点 | GPU | flash attention | 有效批次大小 | 吞吐量 (img/s) | 加速 | 峰值 GPU 内存 (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
全量微调 | 1 | 8 | | 64 | 2.462 |  1x | ~32
全量微调 | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
全量微调 | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
冻结图像模型 | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## 已知问题

- 无法在 fp16 下运行 flash attention（建议始终使用 bf16，当可用时，所有支持 flash attention 的 GPU 也支持 bf16）。
- 目前不支持保存中间检查点和恢复训练。

**免责声明**：
本文档是使用基于机器的AI翻译服务翻译的。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原文档的母语版本视为权威来源。对于关键信息，建议使用专业的人类翻译。对于因使用本翻译而引起的任何误解或误读，我们不承担责任。