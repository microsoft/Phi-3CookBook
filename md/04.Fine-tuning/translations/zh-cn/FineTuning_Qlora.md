**使用 QLoRA 对 Phi-3 进行微调**

使用 [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)对 Microsoft 的 Phi-3 Mini 语言模型进行微调。

QLoRA 将有助于提高对话理解和响应生成的能力。

要使用 transformers 和 bitsandbytes 以 4bits加载模型，您需要从源码安装 accelerate 和 transformers，并确保拥有最新版本的 bitsandbytes 库。

**示例**
- [Learn More with this sample notebook](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Example of Python FineTuning Sample](../../../../code/04.Finetuning/FineTrainingScript.py)
- [Example of Hugging Face Hub Fine Tuning with LORA](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Example of Hugging Face Hub Fine Tuning with QLORA](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)