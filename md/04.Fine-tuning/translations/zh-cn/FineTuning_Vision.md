# Phi-3-V 微调秘诀

这是使用 Hugging Face 库对 Phi-3-V 进行微调的官方支持。
请在运行以下命令之前，使用 `cd` 命令切换到代码目录 [vision_finetuning](../../../../code/04.Finetuning/vision_finetuning) 。

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

## 快速入门

我们提供了两个示例微调脚本，一个用于 DocVQA，另一个用于仇恨表情分类。

经过测试，最低硬件要求为 4x RTX8000（每个 GPU 需要 48GB RAM）。
```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

## 使用指导
根据硬件情况，用户可以选择不同的微调策略。我们支持完全微调（使用 Deepspeed Zero-2），可以选择frozen vision参数，还支持 LoRA（包括 4 位 QLoRA）。一般来说，我们建议尽可能使用 flash attention 和 bf16 进行完全微调。

## 请求Azure GPU配额

### 先决条件
一个具有贡献者角色（或包含贡献者访问权限的其他角色）的 Azure 帐户。

如果您还没有 Azure 帐户，请在开始之前创建一个免费帐户： [创建免费账户](https://azure.microsoft.com)。

### 申请增加配额
您可以直接从“My quotas”页面提交配额增加请求。按照以下步骤请求增加配额。在此示例中，您可以选择订阅中的任何可调配额。

登录 Azure 门户：[Azure portal](https://portal.azure.com).

在搜索框中输入“quotas”，然后选择“quotas”。
![Quota](https://learn.microsoft.com/en-us/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

在概览页面上，选择一个provider，例如 Compute 或 AML。

**注意** 对于 Compute 之外的所有provider，您将看到“请求增加”列，而不是下面描述的“可调”列。在那里，您可以请求增加特定配额，或为增加创建支持请求。

在“My quotas”页面下的“Quota name”下，选择您要增加的配额。确保此配额的“可调”列显示为“是”。

在页面顶部附近，选择“New Quota Request”，然后选择“输入新限额”。

![Increase Quota](https://learn.microsoft.com/en-us/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

在“New Quota Request”窗格中，为新的配额限制输入一个数值，然后选择“Submit”。

您的请求将被审查，如果请求可以满足，您将收到通知。这个过程通常需要几分钟。

如果您的请求未得到满足，您将看到一个创建支持请求的链接。当您使用此链接时，支持工程师将协助您处理增加请求。

## Azure 中包含 GPU 资源的虚拟机建议

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/en-us/azure/virtual-machines/ndv2-series)

以下是一些示例：

### 如果你有 A100 或者 H100 的 GPU
完全微调通常可以获得最佳性能。您可以使用以下命令对 Phi-3-V 进行仇恨表情分类的微调。

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
在仇恨表情分类任务上完全微调 Phi-3-V 仍然是可行的。然而，由于缺乏flash attention的支持，与 A100 或 H100 GPU 相比，吞吐量可能会降低很多。同时，由于缺乏 bf16 的支持（取而代之的是使用 fp16 混合精度训练），准确性也可能受到影响。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```


### 如果您无法获取数据中心的GPU
Lora可能是您唯一的选择。您可以使用以下命令对 Phi-3-V 进行仇恨表情分类的微调。

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

对于Turing+ GPU的场景，QLoRA是支持的

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```


## 建议的超参数和期望的精度

### DocVQA
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
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |


### 仇恨表情分类
```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

训练方法 | 数据类型 | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |



## 速度基准测试

速度基准测试是在 DocVQA 数据集上执行的。该数据集的平均序列长度为 2443.23 个 tokens (对于图像模型，使用 `num_crops=16` )。

### 8x A100-80GB (Ampere)
训练方法 | \# 节点数量 | GPU数量 | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
full-finetuning | 1 | 8 | &#x2714; | 64 | 8.657 | 1.72x | ~36
full-finetuning | 2 | 16 | &#x2714; | 64 | 16.903 | 3.35x | ~29
full-finetuning | 4 | 32 | &#x2714; | 64 | 33.433 | 6.63x | ~26
frozen image model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
frozen image model | 1 | 8 | &#x2714; | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | &#x2714; | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | &#x2714; | 64 | 10.545 | 2.09x | ~10



### 8x V100-32GB (Volta)
训练方法 | \# 节点数量 | GPU数量 | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30


## 已知问题

- 无法在 fp16 下运行 flash attention（在可用时，总是推荐使用 bf16，而且所有支持 flash attention 的 GPU 也支持 bf16）。
- 暂时不支持保存中间检查点和恢复训练。
