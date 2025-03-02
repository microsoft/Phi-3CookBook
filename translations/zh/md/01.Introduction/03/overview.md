在 Phi-3-mini 的上下文中，推理指的是使用模型根据输入数据进行预测或生成输出的过程。以下是关于 Phi-3-mini 及其推理能力的更多详细信息。

Phi-3-mini 是 Microsoft 发布的 Phi-3 系列模型的一部分。这些模型旨在重新定义小型语言模型 (SLM) 的可能性。

以下是关于 Phi-3-mini 和其推理能力的一些关键点：

## **Phi-3-mini 概述：**
- Phi-3-mini 的参数规模为 38 亿。
- 它不仅可以运行在传统计算设备上，还可以运行在边缘设备上，例如移动设备和物联网设备。
- Phi-3-mini 的发布使个人和企业能够在不同硬件设备上部署 SLM，特别是在资源受限的环境中。
- 它支持多种模型格式，包括传统的 PyTorch 格式、量化后的 gguf 格式，以及基于 ONNX 的量化版本。

## **访问 Phi-3-mini：**
要访问 Phi-3-mini，可以在 Copilot 应用中使用 [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。Semantic Kernel 通常兼容 Azure OpenAI Service、Hugging Face 的开源模型，以及本地模型。
您还可以使用 [Ollama](https://ollama.com) 或 [LlamaEdge](https://llamaedge.com) 调用量化模型。Ollama 允许个人用户调用不同的量化模型，而 LlamaEdge 提供了 GGUF 模型的跨平台支持。

## **量化模型：**
许多用户更倾向于使用量化模型进行本地推理。例如，您可以直接运行 Ollama run Phi-3，或者使用 Modelfile 离线配置。Modelfile 指定了 GGUF 文件路径和提示格式。

## **生成式 AI 的可能性：**
结合像 Phi-3-mini 这样的 SLM 开启了生成式 AI 的新可能性。推理只是第一步；这些模型可以用于资源受限、延迟敏感和成本受限的各种场景中的多种任务。

## **利用 Phi-3-mini 解锁生成式 AI：推理与部署指南**
了解如何使用 Semantic Kernel、Ollama/LlamaEdge 和 ONNX Runtime 访问并推理 Phi-3-mini 模型，并探索生成式 AI 在各种应用场景中的可能性。

**功能**
在以下环境中推理 phi3-mini 模型：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

总之，Phi-3-mini 让开发者能够探索不同的模型格式，并在各种应用场景中利用生成式 AI。

**免责声明**：  
本文档使用基于机器的人工智能翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档为权威来源。对于关键信息，建议寻求专业的人类翻译服务。对于因使用本翻译而引起的任何误解或误读，我们不承担任何责任。