# **使用 LoRA 微调 Phi-3**

使用 [LoRA（低秩适应）](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) 在自定义对话指令数据集上微调微软的 Phi-3 Mini 语言模型。

LoRA 将有助于提升对话理解和响应生成的能力。

## 微调 Phi-3 Mini 的分步指南：

**导入和设置**

安装 loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

首先导入必要的库，例如 datasets、transformers、peft、trl 和 torch。  
设置日志记录以跟踪训练过程。

你可以选择通过用 loralib 实现的对应层替换某些层进行适配。目前我们仅支持 nn.Linear、nn.Embedding 和 nn.Conv2d。对于某些实现中一个 nn.Linear 表示多个层（例如注意力 qkv 投影）的情况，我们还支持 MergedLinear（详见附加说明）。

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

在训练循环开始之前，仅将 LoRA 参数标记为可训练。

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

保存检查点时，生成仅包含 LoRA 参数的 state_dict。

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

现在可以像往常一样开始训练。

**超参数**

定义两个字典：training_config 和 peft_config。  
training_config 包括训练的超参数，例如学习率、批量大小和日志记录设置。

peft_config 指定与 LoRA 相关的参数，如 rank、dropout 和任务类型。

**模型和分词器加载**

指定预训练 Phi-3 模型的路径（例如 "microsoft/Phi-3-mini-4k-instruct"）。  
配置模型设置，包括缓存使用、数据类型（bfloat16 用于混合精度）和注意力实现。

**训练**

使用自定义对话指令数据集微调 Phi-3 模型。  
利用 peft_config 中的 LoRA 设置进行高效适配。  
通过指定的日志记录策略监控训练进度。  
评估与保存：评估微调后的模型。  
在训练过程中保存检查点以供后续使用。

**示例**
- [通过此示例笔记本了解更多](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微调示例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [使用 Hugging Face Hub 和 LORA 的微调示例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face 模型卡示例 - LORA 微调示例](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [使用 Hugging Face Hub 和 QLORA 的微调示例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免责声明**：  
本文档通过机器翻译服务生成。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的原始文档作为权威来源。对于关键信息，建议寻求专业人工翻译。因使用此翻译而引起的任何误解或误读，我们概不负责。