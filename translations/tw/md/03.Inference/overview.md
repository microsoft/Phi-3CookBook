在 Phi-3-mini 的背景下，推理指的是使用模型根据输入数据进行预测或生成输出的过程。让我为你提供更多关于 Phi-3-mini 及其推理能力的详细信息。

Phi-3-mini 是微软发布的 Phi-3 系列模型的一部分。这些模型旨在重新定义小型语言模型（SLM）的可能性。

以下是一些关于 Phi-3-mini 及其推理能力的关键点：

## **Phi-3-mini 概述：**
- Phi-3-mini 的参数规模为 38 亿。
- 它不仅可以在传统计算设备上运行，还可以在移动设备和物联网设备等边缘设备上运行。
- Phi-3-mini 的发布使个人和企业能够在不同硬件设备上部署 SLM，特别是在资源受限的环境中。
- 它涵盖了多种模型格式，包括传统的 PyTorch 格式、量化版的 gguf 格式和基于 ONNX 的量化版本。

## **访问 Phi-3-mini：**
要访问 Phi-3-mini，你可以在 Copilot 应用中使用 [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。Semantic Kernel 通常与 Azure OpenAI Service、Hugging Face 上的开源模型以及本地模型兼容。
你也可以使用 [Ollama](https://ollama.com) 或 [LlamaEdge](https://llamaedge.com) 来调用量化模型。Ollama 允许个人用户调用不同的量化模型，而 LlamaEdge 提供 GGUF 模型的跨平台可用性。

## **量化模型：**
许多用户更喜欢使用量化模型进行本地推理。例如，你可以直接运行 Ollama run Phi-3 或使用 Modelfile 离线配置。Modelfile 指定了 GGUF 文件路径和提示格式。

## **生成式 AI 的可能性：**
结合像 Phi-3-mini 这样的 SLM 开启了生成式 AI 的新可能性。推理只是第一步；这些模型可以用于资源受限、延迟敏感和成本受限的各种任务。

## **解锁 Phi-3-mini 的生成式 AI：推理和部署指南**
了解如何使用 Semantic Kernel、Ollama/LlamaEdge 和 ONNX Runtime 访问和推理 Phi-3-mini 模型，并探索在各种应用场景中的生成式 AI 可能性。

**功能**
在以下平台推理 phi3-mini 模型：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

总之，Phi-3-mini 允许开发者探索不同的模型格式，并在各种应用场景中利用生成式 AI。

**免責聲明**：
本文檔是使用機器翻譯服務翻譯的。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文檔為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或誤讀不承擔責任。