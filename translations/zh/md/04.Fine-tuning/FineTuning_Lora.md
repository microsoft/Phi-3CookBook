# **使用 Lora 微调 Phi-3**

使用 [LoRA (低秩适应)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) 在自定义聊天指令数据集上微调微软的 Phi-3 Mini 语言模型。

LORA 将有助于提升对话理解和响应生成的能力。

## 微调 Phi-3 Mini 的分步指南：

**导入和设置**

安装 loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

首先导入必要的库，如 datasets、transformers、peft、trl 和 torch。
设置日志记录以跟踪训练过程。

你可以选择通过将某些层替换为 loralib 中实现的对应部分来适应它们。目前我们只支持 nn.Linear、nn.Embedding 和 nn.Conv2d。我们还支持 MergedLinear，用于单个 nn.Linear 表示多个层的情况，例如在某些注意力 qkv 投影的实现中（参见附加说明了解更多）。

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

在训练循环开始之前，仅标记 LoRA 参数为可训练的。

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

在保存检查点时，生成一个仅包含 LoRA 参数的 state_dict。

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

使用 load_state_dict 加载检查点时，确保设置 strict=False。

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

现在可以像往常一样进行训练了。

**超参数**

定义两个字典：training_config 和 peft_config。training_config 包含训练的超参数，如学习率、批量大小和日志记录设置。

peft_config 指定了与 LoRA 相关的参数，如 rank、dropout 和任务类型。

**模型和分词器加载**

指定预训练 Phi-3 模型的路径（例如 "microsoft/Phi-3-mini-4k-instruct"）。配置模型设置，包括缓存使用、数据类型（bfloat16 用于混合精度）和注意力实现。

**训练**

使用自定义聊天指令数据集微调 Phi-3 模型。利用 peft_config 中的 LoRA 设置进行高效适应。使用指定的日志记录策略监控训练进度。
评估和保存：评估微调后的模型。
在训练过程中保存检查点以备后用。

**样例**
- [通过此示例笔记本了解更多](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微调示例](../../../../code/04.Finetuning/FineTrainingScript.py)
- [使用 LORA 微调 Hugging Face Hub 示例](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face 模型卡示例 - LORA 微调示例](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [使用 QLORA 微调 Hugging Face Hub 示例](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免责声明**:
本文档使用基于机器的人工智能翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用本翻译而引起的任何误解或误读承担责任。