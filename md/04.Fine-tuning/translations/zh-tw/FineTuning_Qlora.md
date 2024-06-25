**微調 Phi-3 與 QLoRA**

微調 Microsoft 的 Phi-3 Mini 語言模型使用 [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)。

QLoRA 將有助於提升對話理解和回應生成。

要使用 transformers 和 bitsandbytes 以 4bits 載入模型，您必須從源碼安裝 accelerate 和 transformers，並確保您擁有最新版本的 bitsandbytes 函式庫。

**範例**

- [了解更多範例筆記本](../../../../code/04.Finetuning/translations/zh-tw/Phi_3_Inference_Finetuning.ipynb)
- [Python 微調範例](../../../../code/04.Finetuning/translations/zh-tw/FineTrainingScript.py)
- [使用 LORA 的 Hugging Face Hub 微調範例](../../../../code/04.Finetuning/translations/zh-tw/Phi-3-finetune-lora-python.ipynb)
- [使用 QLORA 的 Hugging Face Hub 微調範例](../../../../code/04.Finetuning/translations/zh-tw/Phi-3-finetune-qlora-python.ipynb)

