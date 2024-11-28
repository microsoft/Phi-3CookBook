**使用QLoRA微調Phi-3**

使用[QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)微調微軟的Phi-3 Mini語言模型。

QLoRA將有助於提升對話理解和回應生成的能力。

要使用transformers和bitsandbytes在4bits下加載模型，您需要從源代碼安裝accelerate和transformers，並確保您擁有最新版本的bitsandbytes庫。

**範例**
- [從這個範例筆記本學習更多](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python微調範例](../../../../code/04.Finetuning/FineTrainingScript.py)
- [使用LORA在Hugging Face Hub上的微調範例](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [使用QLORA在Hugging Face Hub上的微調範例](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責聲明**:
本文件使用基於機器的AI翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始語言的文件視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對使用此翻譯所引起的任何誤解或誤讀不承擔任何責任。