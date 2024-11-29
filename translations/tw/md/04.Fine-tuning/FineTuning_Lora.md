# **使用Lora微调Phi-3**

使用[LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo)在自定义聊天指令数据集上微调微软的Phi-3 Mini语言模型。

LORA将有助于改善对话理解和响应生成。

## 微调Phi-3 Mini的逐步指南：

**导入和设置**

安装loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

首先导入必要的库，如datasets、transformers、peft、trl和torch。
设置日志记录以跟踪训练过程。

你可以选择通过用loralib实现的对应层替换某些层来进行适应。目前我们只支持nn.Linear、nn.Embedding和nn.Conv2d。对于一些实现中，单个nn.Linear表示多个层（例如在注意力qkv投影中），我们也支持MergedLinear（详见附加说明）。

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

在训练循环开始之前，只标记LoRA参数为可训练。

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

使用load_state_dict加载检查点时，确保设置strict=False。

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

现在可以像往常一样进行训练。

**超参数**

定义两个字典：training_config和peft_config。training_config包括训练的超参数，如学习率、批处理大小和日志设置。

peft_config指定与LoRA相关的参数，如rank、dropout和任务类型。

**模型和分词器加载**

指定预训练Phi-3模型的路径（例如 "microsoft/Phi-3-mini-4k-instruct"）。配置模型设置，包括缓存使用、数据类型（混合精度的bfloat16）和注意力实现。

**训练**

使用自定义聊天指令数据集微调Phi-3模型。利用peft_config中的LoRA设置进行高效适应。使用指定的日志策略监控训练进度。
评估和保存：评估微调后的模型。
在训练过程中保存检查点以供后续使用。

**样例**
- [通过这个样例笔记本了解更多](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python微调样例示例](../../../../code/04.Finetuning/FineTrainingScript.py)
- [使用LORA进行Hugging Face Hub微调的示例](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face模型卡示例 - LORA微调样例](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [使用QLORA进行Hugging Face Hub微调的示例](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責聲明**：
本文件是使用基於機器的人工智能翻譯服務翻譯的。儘管我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用本翻譯而引起的任何誤解或誤釋不承擔責任。