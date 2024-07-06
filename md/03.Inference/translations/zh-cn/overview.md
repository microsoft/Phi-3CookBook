在Phi-3-mini的背景下，推理是指使用模型根据输入数据进行预测或生成输出的过程。让我为您提供有关Phi-3-mini及其推理功能的更多详细信息。

Phi-3-mini是Microsoft发布的Phi-3系列模型的一个分支。这些模型旨在重新定义Small Language Models（SLMs）的可能性。

以下是有关Phi-3-mini及其推理功能的一些关键点:

## **Phi-3-mini 概览:**
- Phi-3-mini是一款参数规模为38亿的小型语言模型。
- 它不仅可以在传统计算设备上运行，还可以在边缘设备如移动设备和物联网设备上运行。
- Phi-3-mini的发布使个人和企业能够在不同的硬件设备上部署SLM，特别是在资源受限的环境中。
- 它涵盖了多种模型格式，包括传统的PyTorch格式、量化的gguf格式版本以及基于ONNX的量化版本。

## **访问Phi-3-mini:**
要访问Phi-3-mini，您可以在Copilot应用中使用 [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。Semantic Kernel通常兼容Azure OpenAI服务、Hugging Face上的开源模型和本地模型。
您还可以使用 [Ollama](https://ollama.com) 或 [LlamaEdge](https://llamaedge.com) 来调用量化模型。Ollama允许个人用户调用不同的量化模型，而LlamaEdge为GGUF模型提供了跨平台可用性。

## **量化模型:**
许多用户更喜欢使用量化模型进行本地推理。例如，您可以直接运行ollama run Phi-3或使用Modelfile进行离线配置。Modelfile指定了GGUF文件路径和提示词格式。

## **生成式AI的可能性:**
结合像Phi-3-mini这样的SLM为生成式AI开辟了新的可能性。推理仅仅是第一步；这些模型可以应用在资源受限、延迟受限和成本受限场景下的各种任务。

## **使用Phi-3-mini解锁生成式AI：推理与部署指南** 
学习如何使用Semantic Kernel、Ollama/LlamaEdge和ONNX Runtime访问和推理Phi-3-mini模型，并在各种应用场景中探索生成式AI的可能性。

**特性**
在以下环境中使用 phi3-mini 模型进行推理:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

总之，Phi-3-mini使开发人员能够探索不同的模型格式，并在各种应用场景中充分利用生成式AI。
