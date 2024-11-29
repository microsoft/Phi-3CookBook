# **在 Android 上进行 Phi-3 推理**

让我们来探讨如何在 Android 设备上使用 Phi-3-mini 进行推理。Phi-3-mini 是微软推出的新系列模型，使得在边缘设备和物联网设备上部署大型语言模型（LLMs）成为可能。

## 语义内核和推理

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) 是一个应用框架，允许您创建兼容 Azure OpenAI 服务、OpenAI 模型，甚至本地模型的应用程序。如果您是语义内核的新手，我们建议您查看 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。

### 使用语义内核访问 Phi-3-mini

您可以将其与语义内核中的 Hugging Face 连接器结合使用。请参阅此 [示例代码](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)。

默认情况下，它对应于 Hugging Face 上的模型 ID。不过，您也可以连接到本地构建的 Phi-3-mini 模型服务器。

### 使用 Ollama 或 LlamaEdge 调用量化模型

许多用户更喜欢使用量化模型来本地运行模型。[Ollama](https://ollama.com/) 和 [LlamaEdge](https://llamaedge.com) 允许个人用户调用不同的量化模型：

#### Ollama

您可以直接运行 `ollama run Phi-3` 或通过创建一个 `Modelfile` 并指向您的 `.gguf` 文件路径来离线配置它。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[示例代码](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

如果您希望在云端和边缘设备上同时使用 `.gguf` 文件，LlamaEdge 是一个很好的选择。您可以参考这个 [示例代码](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) 开始使用。

### 在 Android 手机上安装和运行

1. **下载 MLC Chat 应用**（免费）用于 Android 手机。
2. 下载 APK 文件（148MB）并安装到您的设备上。
3. 启动 MLC Chat 应用。您会看到包括 Phi-3-mini 在内的 AI 模型列表。

总之，Phi-3-mini 为边缘设备上的生成式 AI 开启了令人兴奋的可能性，您可以开始在 Android 上探索其功能。

**免责声明**：
本文件使用基于机器的AI翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原文档视为权威来源。对于关键信息，建议进行专业的人类翻译。对于因使用此翻译而产生的任何误解或误读，我们不承担任何责任。