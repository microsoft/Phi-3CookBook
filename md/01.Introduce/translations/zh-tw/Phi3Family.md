# **Phi-3 Family**

Phi-3 模型是目前最強大且具成本效益的小型語言模型 (SLMs)，在各種語言、推論、程式碼和數學基準測試中，表現優於同尺寸和更大尺寸的模型。此版本擴展了高品質模型的選擇，為客戶提供了更多實用的選擇，用於撰寫和建構生成式 AI 應用程式。

Phi-3 家族包括迷你、小型、中型和視覺版本，基於不同的參數量進行訓練，以服務於各種應用場景。每個模型都經過指令調整，並根據 Microsoft 的負責任 AI、安全和安全標準進行開發，以確保其隨時可用。

## Phi-3 任務範例

 | |
|-|-|
|任務|Phi-3|
|語言任務|是|
|數學與推論|是|
|程式碼|是|
|函式呼叫|否|
|自我編排 (助手)|否|
|專用嵌入模型|否

## **Phi-3-Mini**

Phi-3-mini 是一個 3.8B 參數語言模型，有兩種上下文長度 [128K](https://ai.azure.com/explore/models/Phi-3-mini-128k-instruct/version/7/registry/azureml) 和 [4K](https://ai.azure.com/explore/models/Phi-3-mini-4k-instruct/version/7/registry/azureml)。

Phi-3-Mini 是一個基於 Transformer 的語言模型，擁有 38 億個參數。它使用包含教育性有用資訊的高品質數據進行訓練，並增強了由各種 NLP 合成文本和內部及外部聊天數據集組成的新數據來源，這顯著提高了聊天能力。此外，Phi-3-Mini 在預訓練後通過監督微調（SFT）和直接偏好優化（DPO）進行了聊天微調。在這次後訓練之後，Phi-3-Mini 在多項能力上顯示出顯著的改進，特別是在對齊性、魯棒性和安全性方面。該模型是 Phi-3 家族的一部分，並以 Mini 版本推出，有兩個變體，4K 和 128K，代表它可以支持的上下文長度（以 tokens 計）。

## **Phi-3-Small**

Phi-3-small 是一個 7B 參數語言模型，有兩種上下文長度 [128K](https://ai.azure.com/explore/models/Phi-3-small-128k-instruct/version/1/registry/azureml) 和 [8K](https://ai.azure.com/explore/models/Phi-3-small-8k-instruct/version/1/registry/azureml)。

Phi-3-Small 是一個基於 Transformer 的語言模型，擁有 7B 參數。它使用包含教育性有用資訊的高品質數據進行訓練，並增強了由各種 NLP 合成文本和內部及外部聊天數據集組成的新數據源，這顯著提高了聊天能力。此外，Phi-3-Small 在預訓練後通過監督微調（SFT）和直接偏好優化（DPO）進行了聊天微調。在這次後訓練之後，Phi-3-Small 在多項能力上顯示出顯著的改進，特別是在對齊性、魯棒性和安全性方面。與 Phi-3-Mini 相比，Phi-3-Small 在多語言數據集上的訓練更為密集。該模型家族提供兩個變體，8K 和 128K，代表它可以支持的上下文長度（以 tokens 計）。

## **Phi-3-Medium**

Phi-3-medium 是一個 14B 參數的語言模型，有兩種上下文長度 [128K](https://ai.azure.com/explore/models/Phi-3-medium-128k-instruct/version/1/registry/azureml) 和 [4K](https://ai.azure.com/explore/models/Phi-3-medium-4k-instruct/version/1/registry/azureml)。

Phi-3-Medium 是一個基於 Transformer 的語言模型，擁有 140 億個參數。它使用包含教育性有用資訊的高品質數據進行訓練，並增強了包含各種 NLP 合成文本的新數據來源，以及內部和外部的聊天數據集，這顯著提高了聊天能力。此外，Phi-3-Medium 在預訓練後通過監督微調（SFT）和直接偏好優化（DPO）進行了聊天微調。經過這些後期訓練，Phi-3-Medium 在多項能力上顯示出顯著的改進，特別是在對齊性、魯棒性和安全性方面。該模型家族提供兩個變體，4K 和 128K，代表它可以支持的上下文長度（以 token 計）。

## **Phi-3-vision**

[Phi-3-vision](https://ai.azure.com/explore/models/Phi-3-vision-128k-instruct/version/1/registry/azureml) 是一個具有語言和視覺能力的 42 億參數多模態模型。

Phi-3-vision 是 Phi-3 系列中的第一個多模態模型，將文字和圖像結合在一起。Phi-3-vision 可以用於對現實世界圖像進行推論，並從圖像中提取和推論文字。它還針對圖表和原理圖理解進行了優化，可以用於生成見解和回答問題。Phi-3-vision 建立在 Phi-3-mini 的語言能力之上，繼續在小尺寸中包裝強大的語言和圖像推論品質。

## **Phi Silica**

我們準備推出 Phi Silica，它是從 Phi 系列模型建構而成，專為 Copilot+ PC 中的 NPU 設計。Windows 是第一個擁有為 NPU 定制並內建的先進小型語言模型（SLM）的平台。
Phi Silica API 以及 OCR、Studio Effects、Live Captions、Recall User Activity API 將在 6 月於 Windows Copilot 函式庫中提供。更多的 API，如 Vector Embedding、RAG API、Text Summarization 將在稍後推出。

## **尋找所有 Phi-3 型號**

- [Azure AI](https://ai.azure.com/explore/models?&selectedCollection=phi)
- [Hugging Face.](https://huggingface.co/collections/microsoft/phi-3-6626e15e9585a200d2d761e3)

## ONNX Models

兩個 ONNX 模型 “cpu-int4-rtn-block-32” 和 “cpu-int4-rtn-block-32-acc-level-4” 之間的主要區別在於準確性等級。帶有 “acc-level-4” 的模型旨在平衡延遲與準確性，通過在準確性上做出輕微的妥協來獲得更好的性能，這可能特別適合移動設備。

## 模型選擇範例

 | | | |
|-|-|-|-|
|Customer Need|Task|Start with|More Details|
|需要一個簡單總結訊息線索的模型|對話總結|Phi-3 text model|決定因素是客戶有一個定義明確且直截了當的語言任務|
|免費的兒童數學輔導應用程式|數學和推論|Phi-3 text models|因為應用程式是免費的，客戶希望解決方案不會產生持續的費用|
|自動巡邏車攝像頭|視覺分析|Phi-Vision|需要一個可以在無網際網路的邊緣設備上工作的解決方案|
|想要建立一個基於 AI 的旅行預訂代理|需要複雜的計劃、函式呼叫和協調|GPT models|需要能夠計劃、呼叫 API 以收集資訊並執行|
|想要為員工建立一個副駕駛|RAG、多領域、複雜且開放式|GPT models|開放式情境，需要更廣泛的世界知識，因此更適合使用較大的模型

