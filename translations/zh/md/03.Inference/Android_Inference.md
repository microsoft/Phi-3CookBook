# **在 Android 上推理 Phi-3**

让我们来看看如何在 Android 设备上使用 Phi-3-mini 进行推理。Phi-3-mini 是微软推出的新系列模型，能够在边缘设备和物联网设备上部署大型语言模型（LLM）。

## 语义内核和推理

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) 是一个应用框架，允许你创建兼容 Azure OpenAI 服务、OpenAI 模型，甚至本地模型的应用。如果你是 Semantic Kernel 的新手，我们建议你查看 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。

### 使用 Semantic Kernel 访问 Phi-3-mini

你可以将其与 Semantic Kernel 中的 Hugging Face Connector 结合使用。参考这个 [示例代码](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)。

默认情况下，它对应于 Hugging Face 上的模型 ID。不过，你也可以连接到本地构建的 Phi-3-mini 模型服务器。

### 使用 Ollama 或 LlamaEdge 调用量化模型

许多用户更喜欢使用量化模型来本地运行模型。[Ollama](https://ollama.com/) 和 [LlamaEdge](https://llamaedge.com) 允许个人用户调用不同的量化模型：

#### Ollama

你可以直接运行 `ollama run Phi-3`，或者通过创建一个包含 `.gguf` 文件路径的 `Modelfile` 离线配置。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> {{.Prompt}}<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[示例代码](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

如果你希望在云端和边缘设备上同时使用 `.gguf` 文件，LlamaEdge 是一个很好的选择。你可以参考这个 [示例代码](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) 开始。

### 在 Android 手机上安装和运行

1. **下载 MLC Chat 应用**（免费）用于 Android 手机。
2. 下载 APK 文件（148MB）并安装到你的设备上。
3. 启动 MLC Chat 应用。你会看到一个 AI 模型列表，包括 Phi-3-mini。

总之，Phi-3-mini 为边缘设备上的生成式 AI 开辟了令人兴奋的可能性，你可以在 Android 设备上开始探索其功能。

免责声明：本翻译由人工智能模型从原文翻译而来，可能并不完美。请审查输出并进行必要的修改。