在 Phi-3-mini 的上下文中，推理是指使用模型根據輸入數據進行預測或生成輸出的過程。以下是有關 Phi-3-mini 及其推理能力的更多詳細資訊。

Phi-3-mini 是 Microsoft 推出的 Phi-3 系列模型的一部分。這些模型旨在重新定義小型語言模型 (SLMs) 的可能性。

以下是有關 Phi-3-mini 及其推理能力的一些關鍵點：

## **Phi-3-mini 概述：**
- Phi-3-mini 的參數規模為 38 億。
- 它不僅可以在傳統計算設備上運行，還可以在邊緣設備（如移動設備和物聯網設備）上運行。
- Phi-3-mini 的推出使個人和企業能夠在不同硬體設備上部署 SLM，特別是在資源有限的環境中。
- 它涵蓋了多種模型格式，包括傳統的 PyTorch 格式、量化版本的 gguf 格式，以及基於 ONNX 的量化版本。

## **訪問 Phi-3-mini：**
要訪問 Phi-3-mini，可以在 Copilot 應用中使用 [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。Semantic Kernel 通常與 Azure OpenAI Service、Hugging Face 的開源模型以及本地模型兼容。
您還可以使用 [Ollama](https://ollama.com) 或 [LlamaEdge](https://llamaedge.com) 調用量化模型。Ollama 允許個人用戶調用不同的量化模型，而 LlamaEdge 提供了 GGUF 模型的跨平台支持。

## **量化模型：**
許多用戶更喜歡使用量化模型進行本地推理。例如，您可以直接運行 Ollama 執行 Phi-3，或者使用 Modelfile 離線配置。Modelfile 指定了 GGUF 文件的路徑和提示格式。

## **生成式 AI 的可能性：**
結合像 Phi-3-mini 這樣的 SLM 為生成式 AI 開啟了新的可能性。推理只是第一步；這些模型可以用於資源有限、延遲受限以及成本受限的各種場景中的多種任務。

## **解鎖 Phi-3-mini 的生成式 AI：推理與部署指南** 
學習如何使用 Semantic Kernel、Ollama/LlamaEdge 和 ONNX Runtime 訪問並推理 Phi-3-mini 模型，並探索生成式 AI 在各種應用場景中的可能性。

**功能**
在以下平台推理 phi3-mini 模型：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

總而言之，Phi-3-mini 讓開發者能夠探索不同的模型格式，並在各種應用場景中利用生成式 AI。

**免責聲明**：  
本文件已使用機器翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或誤讀概不負責。