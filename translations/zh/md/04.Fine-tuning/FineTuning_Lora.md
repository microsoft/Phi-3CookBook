# **使用 Lora 微调 Phi-3**

使用 [LoRA (低秩适应)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) 在自定义聊天指令数据集上微调微软的 Phi-3 Mini 语言模型。

LORA 将帮助改善对话理解和响应生成。

## 微调 Phi-3 Mini 的分步指南：

**导入和设置**

安装 loralib

```
pip install loralib
# 或者
# pip install git+https://github.com/microsoft/LoRA
```

首先导入必要的库，如 datasets、transformers、peft、trl 和 torch。
设置日志记录以跟踪训练过程。

你可以选择通过用 loralib 实现的对应部分替换一些层来进行适应。我们目前只支持 nn.Linear、nn.Embedding 和 nn.Conv2d。我们还支持 MergedLinear，用于单个 nn.Linear 表示多个层的情况，例如在一些注意力 qkv 投影的实现中（详见附加说明）。

```
# ===== 修改前 =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== 修改后 =====
```

import loralib as lora

```
# 添加一对秩为 r=16 的低秩适应矩阵
layer = lora.Linear(in_features, out_features, r=16)
```

在训练循环开始之前，仅标记 LoRA 参数为可训练。

```
import loralib as lora
model = BigModel()
# 这将所有不包含字符串 "lora_" 的参数的 requires_grad 设置为 False
lora.mark_only_lora_as_trainable(model)
# 训练循环
for batch in dataloader:
```

保存检查点时，生成仅包含 LoRA 参数的 state_dict。

```
# ===== 修改前 =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== 修改后 =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

使用 load_state_dict 加载检查点时，确保设置 strict=False。

```
# 先加载预训练检查点
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# 然后加载 LoRA 检查点
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

现在可以像往常一样进行训练。

**超参数**

定义两个字典：training_config 和 peft_config。training_config 包含训练的超参数，如学习率、批量大小和日志设置。

peft_config 指定与 LoRA 相关的参数，如秩、dropout 和任务类型。

**模型和分词器加载**

指定预训练 Phi-3 模型的路径（例如 "microsoft/Phi-3-mini-4k-instruct"）。配置模型设置，包括缓存使用、数据类型（bfloat16 用于混合精度）和注意力实现。

**训练**

使用自定义聊天指令数据集微调 Phi-3 模型。利用 peft_config 中的 LoRA 设置进行高效适应。使用指定的日志策略监控训练进度。

**评估和保存**

评估微调后的模型。
在训练过程中保存检查点以备后用。

**示例**
- [通过这个示例笔记本了解更多](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微调示例](../../../../code/04.Finetuning/FineTrainingScript.py)
- [使用 LORA 进行 Hugging Face Hub 微调的示例](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face 模型卡片 - LORA 微调示例](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [使用 QLORA 进行 Hugging Face Hub 微调的示例](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

免责声明：本翻译由人工智能模型从原文翻译而来，可能不够完美。请审核输出内容并进行必要的修改。