# **在本地服务器中使用 Phi-3 进行推理**

我们可以在本地服务器上部署 Phi-3。 用户可以选择 [Ollama](https://ollama.com) 或 [LM Studio](https://llamaedge.com) 解决方案，或者编写自己的代码。您可以通过  [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) 或 [Langchain](https://www.langchain.com/) 连接到 Phi-3 的本地服务，以构建 Copilot 类型的应用程序。


## **使用 Semantic Kernel 接入 Phi-3-mini**

在 Copilot 类型的应用中，我们通过 Semantic Kernel / LangChain 创建应用程序。这种应用框架通常兼容 Azure OpenAI Service / OpenAI 模型，并且还可以支持 Hugging Face 上的开源模型和本地模型。如果我们想使用 Semantic Kernel 访问 Phi-3-mini，应该怎么做呢？以 .NET 为例，我们可以将其与 Semantic Kernel 中的 Hugging Face Connector 结合使用。默认情况下，它可以对应 Hugging Face 上的模型 ID（首次使用时，模型将从 Hugging Face 下载，耗时较长）。您还可以连接到搭建好的本地服务。在这两者之间，我们建议使用后者，因为它具有更高的自主性，尤其是在企业应用中。

![sk](../../../../imgs/03/LocalServer/sk.png)


从图中可知，通过 Semantic Kernel 访问本地服务可以轻松地连接到自建的 Phi-3-mini 模型服务器。以下是运行结果。


![skrun](../../../../imgs/03/LocalServer/skrun.png)

***示例代码：*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

