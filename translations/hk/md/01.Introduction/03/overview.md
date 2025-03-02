在 Phi-3-mini 的情境下，推理係指利用模型根據輸入數據進行預測或者生成輸出嘅過程。以下會提供更多關於 Phi-3-mini 同埋其推理能力嘅詳細資訊。

Phi-3-mini 係 Microsoft 推出嘅 Phi-3 系列模型之一。呢啲模型旨在重新定義小型語言模型（SLMs）嘅可能性。

以下係關於 Phi-3-mini 同埋其推理能力嘅幾個重點：

## **Phi-3-mini 概述：**
- Phi-3-mini 擁有 38 億參數。
- 它唔單止可以喺傳統計算設備上運行，仲可以喺邊緣設備（例如移動設備同物聯網設備）上運行。
- Phi-3-mini 嘅推出令個人同企業可以喺資源受限嘅環境中，喺唔同硬件設備上部署 SLMs。
- 它支持多種模型格式，包括傳統嘅 PyTorch 格式、量化版本嘅 gguf 格式同基於 ONNX 嘅量化版本。

## **如何訪問 Phi-3-mini：**
要訪問 Phi-3-mini，可以喺 Copilot 應用中使用 [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。Semantic Kernel 通常兼容 Azure OpenAI Service、Hugging Face 上嘅開源模型同本地模型。
你仲可以使用 [Ollama](https://ollama.com) 或 [LlamaEdge](https://llamaedge.com) 調用量化模型。Ollama 允許個人用戶調用唔同嘅量化模型，而 LlamaEdge 為 GGUF 模型提供跨平台支持。

## **量化模型：**
好多用戶會選擇使用量化模型進行本地推理。例如，你可以直接運行 Ollama run Phi-3，或者通過 Modelfile 喺離線狀態下配置。Modelfile 會指定 GGUF 文件路徑同提示格式。

## **生成式 AI 嘅可能性：**
結合 SLMs（例如 Phi-3-mini）可以開啟生成式 AI 嘅新可能性。推理只係第一步，呢啲模型可以用喺資源受限、延遲敏感同成本受限嘅場景中完成多種任務。

## **解鎖 Phi-3-mini 嘅生成式 AI：推理同部署指南**
了解如何使用 Semantic Kernel、Ollama/LlamaEdge 同 ONNX Runtime 訪問同推理 Phi-3-mini 模型，探索生成式 AI 喺唔同應用場景中嘅可能性。

**功能**
使用以下工具進行 Phi-3-mini 模型推理：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

總結，Phi-3-mini 讓開發者可以探索唔同嘅模型格式，並喺多種應用場景中運用生成式 AI。

**免責聲明**:  
此文件是使用機器翻譯人工智能服務進行翻譯的。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。