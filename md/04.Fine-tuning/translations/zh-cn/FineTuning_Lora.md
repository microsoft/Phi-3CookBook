# **使用 Lora 对 Phi-3 进行微调**

使用LoRA（低秩适应）在自定义聊天指令数据集上微调Microsoft的Phi-3 Mini语言模型。[LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo)。 

LoRA将有助于提高对话理解和响应生成能力。

## 如何微调Phi-3 Mini模型的步骤指南:

**导入和设置** 

安装 loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

首先导入所需库，如 datasets, transformers, peft, trl 和 torch。设置日志记录以跟踪训练过程。

您可以选择通过将某些层替换为loralib中实现的对应层来进行适应。目前我们仅支持nn.Linear、nn.Embedding和nn.Conv2d。我们还支持MergedLinear，适用于单个nn.Linear表示多个层的情况，例如在某些注意力qkv投影的实现中（有关更多信息，请参阅附加说明）。

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

将 loralib 导入为 lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

在训练循环开始之前，只将LoRA参数标记为可训练。

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

在保存检查点时，生成一个仅包含LoRA参数的state_dict。

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

When loading a checkpoint using load_state_dict, be sure to set strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

现在，可以像往常一样进行训练。

**超参数** 

定义两个字典：training_config和peft_config。training_config包含用于训练的超参数，例如学习率、批量大小和日志记录设置。

peft_config指定与LoRA相关的参数，如秩、dropout和任务类型。

**模型和分词器加载** 

指定预训练Phi-3模型的路径（例如 "microsoft/Phi-3-mini-4k-instruct"）。配置模型设置，包括缓存使用、数据类型（混合精度使用bfloat16）和注意力实现。

**训练** 

使用自定义聊天指令数据集对Phi-3模型进行微调。使用peft_config中的LoRA设置进行高效适应。使用指定的日志记录策略监控训练进度。评估和保存：评估微调后的模型。在训练过程中保存检查点以供后续使用。

**示例**
- [Learn More with this sample notebook](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Example of Python FineTuning Sample](../../../../code/04.Finetuning/FineTrainingScript.py)
- [Example of Hugging Face Hub Fine Tuning with LORA](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Example Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Example of Hugging Face Hub Fine Tuning with QLORA](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

