# **在 Android 中使用 Phi-3 进行推理**

让我们探讨如何在安卓设备上使用 Phi-3-mini 进行推理。Phi-3-mini 是微软推出的一款新型模型系列，可在边缘设备和物联网设备上部署大型语言模型（LLMs）。

## Semantic Kernel 和推理:
[Semantic Kernel](https://github.com/microsoft/semantic-kernel) 是一个应用框架，它允许您创建与 Azure OpenAI 服务、OpenAI 模型、甚至本地模型兼容的应用程序。如果您对 Semantic Kernel 不熟悉，建议您查阅 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。

### 使用 Semantic Kernel 访问 Phi-3-mini:
您可以在 Semantic Kernel 中将其与 Hugging Face 连接器结合使用。 [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)

默认情况下，它对应于 Hugging Face 上的模型 ID。然而，您还可以连接到本地搭建的 Phi-3-mini 模型服务器。

### 使用 Ollama 或 LlamaEdge 调用量化模型:

许多用户更喜欢在本地运行量化模型。
[Ollama](https://ollama.com/) 和 [LlamaEdge](https://llamaedge.com) 允许个人用户调用不同的量化模型。:

**Ollama**

您可以直接运行"ollama run Phi-3"，或者通过创建一个包含gguf文件路径的模型文件来离线配置它。

```
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> {{.Prompt}}<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096

```
[示例代码](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

**LlamaEdge** 

如果您想同时在云和边缘设备上使用gguf，LlamaEdge是一个很好的选择。
[示例代码](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)

### 在Android手机上安装并运行:
下载免费的MLC Chat Android手机应用程序。您需要下载APK文件（148MB）并进行安装。启动MLC Chat应用程序，您将看到一个AI模型列表，其中包括Phi-3-mini。

综上所述，Phi-3-mini为边缘设备上的生成式AI带来了令人兴奋的可能性，您可以在Android上开始探索其功能。