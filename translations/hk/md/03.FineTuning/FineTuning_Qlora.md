**使用 QLoRA 微調 Phi-3**

使用 [QLoRA (量子低秩調適)](https://github.com/artidoro/qlora) 微調 Microsoft 的 Phi-3 Mini 語言模型。

QLoRA 將有助於提升對話理解能力以及回應生成的效果。

要使用 transformers 和 bitsandbytes 以 4bits 的格式載入模型，您需要從源頭安裝 accelerate 和 transformers，並確保您擁有最新版本的 bitsandbytes 函式庫。

**範例**
- [透過此範例筆記本了解更多](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微調範例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [使用 LORA 的 Hugging Face Hub 微調範例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [使用 QLORA 的 Hugging Face Hub 微調範例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責聲明**:  
本文件經由機器翻譯人工智能服務翻譯而成。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文檔的母語版本作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。