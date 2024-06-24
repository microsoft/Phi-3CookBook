在 Phi-3-mini 的上下文中，推論是指使用模型根據輸入數據進行預測或生成輸出。讓我為您提供有關 Phi-3-mini 及其推論能力的更多詳細資訊。

Phi-3-mini 是 Microsoft 推出的 Phi-3 系列模型的一部分。這些模型旨在重新定義小型語言模型（SLM）的可能性。

以下是關於 Phi-3-mini 及其推論能力的一些關鍵點：

## **Phi-3-mini 概述:**

- Phi-3-mini 具有 3.8 billion 的參數大小。
- 它不僅可以在傳統計算設備上執行，還可以在移動設備和 IoT 設備等邊緣設備上運行。
- Phi-3-mini 的發布使個人和企業能夠在不同的硬體設備上部署 SLM，特別是在資源受限的環境中。
- 它涵蓋了各種模型格式，包括傳統的 PyTorch 格式、gguf 格式的量化版本和基於 ONNX 的量化版本。

## **存取 Phi-3-mini:**

要存取 Phi-3-mini，你可以在 Copilot 應用程式中使用 [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。Semantic Kernel 通常與 Azure OpenAI Service、Hugging Face 上的開源模型以及本地模型相容。
你也可以使用 [Ollama](https://ollama.com) 或 [LlamaEdge](https://llamaedge.com) 來呼叫量化模型。Ollama 允許個別用戶呼叫不同的量化模型，而 LlamaEdge 提供 GGUF 模型的跨平台可用性。

## **量化模型:**

許多使用者偏好使用量化模型進行本地推論。例如，你可以直接執行 Ollama run Phi-3 或使用 Modelfile 離線配置。Modelfile 指定 GGUF 檔案路徑和提示格式。

## **生成式 AI 的可能性:**

結合像 Phi-3-mini 這樣的 SLMs 開啟了生成式 AI 的新可能性。推論只是第一步；這些模型可以用於資源受限、延遲受限和成本受限的各種任務。

## **使用 Phi-3-mini 解鎖生成式 AI: 推論和部署指南**

學習如何使用 Semantic Kernel、Ollama/LlamaEdge 和 ONNX Runtime 來存取和推斷 Phi-3-mini 模型，並探索生成式 AI 在各種應用場景中的可能性。

**功能**
在以下環境中推論 phi3-mini 模型:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

總結來說，Phi-3-mini 允許開發者探索不同的模型格式並在各種應用場景中利用生成式 AI。

