**微调 Phi-3 使用 QLoRA**

使用 [QLoRA (量子低秩适应)](https://github.com/artidoro/qlora) 微调微软的 Phi-3 Mini 语言模型。

QLoRA 将有助于提高对话理解和响应生成的能力。

要使用 transformers 和 bitsandbytes 以 4bits 加载模型，你需要从源码安装 accelerate 和 transformers，并确保你拥有最新版本的 bitsandbytes 库。

**示例**
- [通过这个示例笔记本了解更多](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微调示例](../../../../code/04.Finetuning/FineTrainingScript.py)
- [使用 LORA 在 Hugging Face Hub 上微调的示例](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [使用 QLORA 在 Hugging Face Hub 上微调的示例](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

