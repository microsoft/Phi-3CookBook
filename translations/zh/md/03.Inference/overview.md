在Phi-3-mini的上下文中，推理是指使用模型基于输入数据进行预测或生成输出的过程。让我为你提供更多关于Phi-3-mini及其推理能力的详细信息。

Phi-3-mini是微软发布的Phi-3系列模型的一部分。这些模型旨在重新定义小型语言模型（SLM）的可能性。

以下是关于Phi-3-mini及其推理能力的一些关键点：

## **Phi-3-mini概述：**
- Phi-3-mini的参数规模为38亿。
- 它不仅可以在传统计算设备上运行，还可以在移动设备和物联网设备等边缘设备上运行。
- Phi-3-mini的发布使个人和企业能够在不同硬件设备上部署SLM，尤其是在资源受限的环境中。
- 它涵盖了各种模型格式，包括传统的PyTorch格式、gguf格式的量化版本和基于ONNX的量化版本。

## **访问Phi-3-mini：**
要访问Phi-3-mini，你可以在Copilot应用程序中使用[Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。Semantic Kernel通常与Azure OpenAI Service、Hugging Face上的开源模型以及本地模型兼容。
你也可以使用[Ollama](https://ollama.com)或[LlamaEdge](https://llamaedge.com)来调用量化模型。Ollama允许个人用户调用不同的量化模型，而LlamaEdge则为GGUF模型提供跨平台的可用性。

## **量化模型：**
许多用户更喜欢使用量化模型进行本地推理。例如，你可以直接运行Ollama run Phi-3或使用Modelfile离线配置。Modelfile指定了GGUF文件路径和提示格式。

## **生成式AI的可能性：**
结合像Phi-3-mini这样的SLM，开启了生成式AI的新可能性。推理只是第一步；这些模型可以用于资源受限、延迟敏感和成本受限的各种任务中。

## **使用Phi-3-mini解锁生成式AI：推理和部署指南**
了解如何使用Semantic Kernel、Ollama/LlamaEdge和ONNX Runtime访问和推理Phi-3-mini模型，并探索生成式AI在各种应用场景中的可能性。

**功能**
在以下环境中进行phi3-mini模型的推理：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

总之，Phi-3-mini使开发人员能够探索不同的模型格式，并在各种应用场景中利用生成式AI。

**免责声明**:
本文件已使用基于机器的人工智能翻译服务进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文件视为权威来源。对于关键信息，建议进行专业人工翻译。对于因使用本翻译而引起的任何误解或误读，我们不承担责任。