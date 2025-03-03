**使用 QLoRA 微調 Phi-3**

使用 [QLoRA (量子低秩適配)](https://github.com/artidoro/qlora) 微調 Microsoft 的 Phi-3 Mini 語言模型。

QLoRA 將有助於提升對話理解和回應生成的能力。

若要使用 transformers 和 bitsandbytes 以 4 位元格式載入模型，您需要從原始碼安裝 accelerate 和 transformers，並確保您擁有最新版本的 bitsandbytes 函式庫。

**範例**
- [透過此範例筆記本了解更多](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微調範例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [使用 LORA 在 Hugging Face Hub 上進行微調的範例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [使用 QLORA 在 Hugging Face Hub 上進行微調的範例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責聲明**：  
本文檔是使用機器翻譯AI服務進行翻譯的。我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋概不負責。