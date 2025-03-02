**使用QLoRA微调Phi-3**

使用[QLoRA（量子低秩适配）](https://github.com/artidoro/qlora)微调微软的Phi-3 Mini语言模型。

QLoRA将有助于提高对话理解和响应生成的能力。

要使用transformers和bitsandbytes以4位加载模型，您需要从源代码安装accelerate和transformers，并确保您拥有最新版本的bitsandbytes库。

**示例**
- [通过此示例笔记本了解更多](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python微调示例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [使用LORA在Hugging Face Hub上微调的示例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [使用QLORA在Hugging Face Hub上微调的示例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免责声明**：  
本文件通过机器翻译服务进行翻译。尽管我们尽力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文件为权威来源。对于关键信息，建议使用专业人工翻译。我们对于因使用此翻译而引起的任何误解或误读概不负责。