## 微調場景

![使用微軟服務進行微調](../../../../translated_images/FinetuningwithMS.25759a0154a97ad90e43a6cace37d6bea87f0ac0236ada3ad5d4a1fbacc3bdf7.hk.png)

**平台** 包括各種技術，例如 Azure AI Foundry、Azure Machine Learning、AI Tools、Kaito 和 ONNX Runtime。

**基礎設施** 包括 CPU 和 FPGA，這些是微調過程中的重要組成部分。讓我展示一下這些技術的圖標。

**工具與框架** 包括 ONNX Runtime 和 ONNX Runtime。讓我展示一下這些技術的圖標。
[插入 ONNX Runtime 和 ONNX Runtime 的圖標]

使用微軟技術進行微調的過程涉及多種組件和工具。通過了解和使用這些技術，我們可以有效地微調應用程式，並創造更好的解決方案。

## 模型即服務

使用托管微調來微調模型，無需創建和管理計算資源。

![MaaS 微調](../../../../translated_images/MaaSfinetune.6184d80a336ea9d7bb67a581e9e5d0b021cafdffff7ba257c2012e2123e0d77e.hk.png)

無伺服器微調適用於 Phi-3-mini 和 Phi-3-medium 模型，使開發人員能夠快速輕鬆地針對雲端和邊緣場景定制模型，而無需安排計算資源。我們還宣布 Phi-3-small 現已通過我們的模型即服務提供，開發人員可以快速輕鬆地開始 AI 開發，而無需管理底層基礎設施。

## 模型即平台

用戶需要管理自己的計算資源來微調模型。

![Maap 微調](../../../../translated_images/MaaPFinetune.cf8b08ef05bf57f362da90834be87562502f4370de4a7325a9fb03b8c008e5e7.hk.png)

[微調範例](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## 微調場景

| | | | | | | |
|-|-|-|-|-|-|-|
|場景|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|將預訓練的 LLM 調整到特定任務或領域|是|是|是|是|是|是|
|針對 NLP 任務（如文本分類、命名實體識別和機器翻譯）進行微調|是|是|是|是|是|是|
|針對問答任務進行微調|是|是|是|是|是|是|
|針對聊天機器人生成類人響應進行微調|是|是|是|是|是|是|
|生成音樂、藝術或其他創意形式的微調|是|是|是|是|是|是|
|降低計算和財務成本|是|是|否|是|是|否|
|減少內存使用|否|是|否|是|是|是|
|使用更少的參數進行高效微調|否|是|是|否|否|是|
|一種內存高效的數據並行形式，可使用所有 GPU 設備的總內存|否|否|否|是|是|是|

## 微調性能範例

![微調性能](../../../../translated_images/Finetuningexamples.9dbf84557eef43e011eb7cadf51f51686f9245f7953e2712a27095ab7d18a6d1.hk.png)

**免責聲明**：  
此文件經由機器翻譯服務進行翻譯。儘管我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件為最終權威來源。如涉及關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解讀概不負責。