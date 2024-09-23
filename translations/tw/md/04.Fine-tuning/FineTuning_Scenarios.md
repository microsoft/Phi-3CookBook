## 微調場景

![使用 MS 服務進行微調](../../../../translated_images/FinetuningwithMS.921fa8c240611562e7c4a5ceb7eca04f458ad6f3c899d5a0dc120030398d9e08.tw.png)

**平台** 包括各種技術，如 Azure AI Studio、Azure Machine Learning、AI Tools、Kaito 和 ONNX Runtime。

**基礎設施** 包括 CPU 和 FPGA，這些是微調過程中的關鍵。讓我展示這些技術的圖標。

**工具與框架** 包括 ONNX Runtime 和 ONNX Runtime。讓我展示這些技術的圖標。
[插入 ONNX Runtime 和 ONNX Runtime 的圖標]

使用 Microsoft 技術進行微調涉及各種組件和工具。通過理解和利用這些技術，我們可以有效地微調我們的應用程序並創建更好的解決方案。

## 模型即服務

使用托管的微調來微調模型，無需創建和管理計算資源。

![MaaS 微調](../../../../translated_images/MaaSfinetune.1678f33544c36b9016d8c018ce9c4c1622fb3bc2d72751291c39813f88bce052.tw.png)

無伺服器微調可用於 Phi-3-mini 和 Phi-3-medium 模型，使開發人員能夠快速且輕鬆地自定義雲端和邊緣場景中的模型，無需安排計算資源。我們還宣布 Phi-3-small 現已通過我們的模型即服務提供，讓開發人員能夠快速且輕鬆地開始 AI 開發，無需管理底層基礎設施。

[微調範例](https://github.com/microsoft/Phi-3CookBook/blob/main/md/04.Fine-tuning/FineTuning_AIStudio.md)

## 模型即平台

用戶管理自己的計算資源來微調他們的模型。

![Maap 微調](../../../../translated_images/MaaPFinetune.f88828d32d16ced1198525fceed9184ce17516f5c1a404c264d87a4ca816947f.tw.png)

[微調範例](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## 微調場景

| | | | | | | |
|-|-|-|-|-|-|-|
|場景|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|將預訓練的 LLM 適應特定任務或領域|是|是|是|是|是|是|
|微調 NLP 任務如文本分類、命名實體識別和機器翻譯|是|是|是|是|是|是|
|微調 QA 任務|是|是|是|是|是|是|
|微調以生成類似人類的聊天機器人回應|是|是|是|是|是|是|
|微調以生成音樂、藝術或其他形式的創作|是|是|是|是|是|是|
|減少計算和財務成本|是|是|否|是|是|否|
|減少內存使用|否|是|否|是|是|是|
|使用較少的參數進行高效微調|否|是|是|否|否|是|
|內存高效的數據並行形式，允許訪問所有可用 GPU 設備的總內存|否|否|否|是|是|是|

## 微調性能範例

![微調性能](../../../../translated_images/Finetuningexamples.88bad3a5350927b08b1f06e4bced95cfd3715caa933d21c9ff658dcf0db94f73.tw.png)

免责声明：此翻译由AI模型从原文翻译而来，可能不够完美。请审阅输出并进行必要的修改。