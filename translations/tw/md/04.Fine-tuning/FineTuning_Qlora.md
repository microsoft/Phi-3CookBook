**微調Phi-3使用QLoRA**

使用[QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)來微調Microsoft的Phi-3 Mini語言模型。

QLoRA將有助於改善對話理解和回應生成。

要使用transformers和bitsandbytes以4位元載入模型，你需要從源頭安裝accelerate和transformers，並確保你擁有最新版本的bitsandbytes庫。

**範例**
- [了解更多這個範例筆記本](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python微調範例](../../../../code/04.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub使用LORA微調範例](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub使用QLORA微調範例](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

