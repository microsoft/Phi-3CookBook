**使用QLoRA微调Phi-3**

使用[QLoRA（量子低秩适应）](https://github.com/artidoro/qlora)微调微软的Phi-3 Mini语言模型。

QLoRA将有助于提高对话理解和响应生成能力。

要使用transformers和bitsandbytes在4位模式下加载模型，你需要从源代码安装accelerate和transformers，并确保你拥有最新版本的bitsandbytes库。

**样例**
- [通过这个样例笔记本了解更多](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python微调样例](../../../../code/04.Finetuning/FineTrainingScript.py)
- [使用LORA进行Hugging Face Hub微调的示例](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [使用QLORA进行Hugging Face Hub微调的示例](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免责声明**：
本文档使用基于机器的人工智能翻译服务进行翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。