# **在本地服务器上推理 Phi-3**

我们可以在本地服务器上部署 Phi-3。用户可以选择 [Ollama](https://ollama.com) 或 [LM Studio](https://llamaedge.com) 解决方案，或者他们可以编写自己的代码。您可以通过 [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) 或 [Langchain](https://www.langchain.com/) 连接 Phi-3 的本地服务来构建 Copilot 应用程序。

## **使用 Semantic Kernel 访问 Phi-3-mini**

在 Copilot 应用程序中，我们通过 Semantic Kernel / LangChain 创建应用程序。这种类型的应用程序框架通常兼容 Azure OpenAI Service / OpenAI 模型，并且还可以支持 Hugging Face 上的开源模型和本地模型。如果我们想使用 Semantic Kernel 访问 Phi-3-mini 该怎么办？以 .NET 为例，我们可以将其与 Semantic Kernel 中的 Hugging Face Connector 结合使用。默认情况下，它可以对应 Hugging Face 上的模型 ID（首次使用时，模型将从 Hugging Face 下载，耗时较长）。您也可以连接到自建的本地服务。相比之下，我们推荐使用后者，因为它具有更高的自主性，尤其是在企业应用中。

![sk](../../../../translated_images/sk.fc8f38bb6ac491315099aa29a2704de109fc0b052448c9bc3d7c02586c196ca4.zh.png)

从图中可以看出，通过 Semantic Kernel 访问本地服务可以轻松连接到自建的 Phi-3-mini 模型服务器。以下是运行结果

![skrun](../../../../translated_images/skrun.f579fcb28592ba4644af8b578e66fb01923bf032b670cef44874c6550e85876d.zh.png)

***示例代码*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

免责声明：本翻译由AI模型从原文翻译而来，可能不够完美。请检查翻译结果并进行必要的修改。