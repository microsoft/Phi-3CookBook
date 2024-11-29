# Ollama C# Playground

这个实验室旨在通过在GitHub Codespaces中直接使用C#示例来测试Phi-3，这是让任何人在浏览器中尝试SLM（小语言模型）的简单方法。

## 如何创建C# + Ollama + Phi-3的Codespace

1. 使用仓库顶部的`Code`按钮创建一个新的Codespace。选择[+ New with options ...]
![创建带选项的Codespace](../../../../../translated_images/10NewCodespacesWithOptions.b50796422fc7f6d13721a50b72de8b62d83a7951fdace787a0dc12edc22ce807.zh.png)

1. 在选项页面中，选择名为`Ollama with Phi-3 for C#`的配置

![选择Ollama with Phi-3 for C#选项以创建Codespace](../../../../../translated_images/12NewCSOllamaCodespace.38aab1c942efe444653b4141918ce6d081ce6e9638e0d16117f5b93ce1deee42.zh.png)

1. 一旦Codespace加载完成，它应该已经预装了[ollama](https://ollama.com/)，下载了最新的Phi-3模型，并安装了[.NET 8](https://dotnet.microsoft.com/download)。

1. （可选）使用Codespace终端，要求Ollama运行[phi3](https://ollama.com/library/phi3)模型：

    ```shell
    ollama run phi3
    ```

4. 你可以从提示符向该模型发送消息。

    ```shell
    >>> Write a joke about kittens
    ```

5. 几秒钟后，你应该会看到模型的响应流。

    ![运行ollama并要求讲一个笑话](../../../../../md/07.Labs/CsharpOllamaCodeSpaces/20ollamarunphi.gif)

1. 想了解与语言模型相关的不同技术，请查看`.\src` folder:

| Project | Description |
|---------|-------------|
| Sample01  | This is a sample project that uses a the Phi-3 hosted in ollama model to answer a question.  |
| Sample02  | This is a sample project that implement a Console chat using Semantic Kernel. |
| [Sample03](./src/Sample03/readme.md)  | This is a sample project that implement a RAG using local embeddings and Semantic Kernel. Check the details of the local RAG [here](./src/Sample03/readme.md) |

## How to run a sample

1. Open a terminal and navigate to the desired project. In example, let's run `Sample02`中的示例项目，控制台聊天。

    ```bash
    cd .\src\Sample02\
    ```

1. 使用以下命令运行项目

    ```bash
    dotnet run
    ```

1. 项目`Sample02`定义了一个自定义系统消息：

    ```csharp
    var history = new ChatHistory();
    history.AddSystemMessage("You are a useful chatbot. If you don't know an answer, say 'I don't know!'. Always reply in a funny ways. Use emojis if possible.");

    ```

1. 因此，当用户提出问题，例如`What is the capital of Italy?`，聊天会使用本地模式进行回复。

    输出类似于这个：

    ![聊天运行演示](../../../../../translated_images/20SampleConsole.22997336ed0fa683bcc3238bb8e953b3a533d28196bc42e7cd1527261dd0689b.zh.png)

## 视频教程

如果你想了解更多关于如何在GitHub仓库中使用Codespaces和Ollama的信息，请查看以下3分钟视频：

[![观看视频](../../../../../translated_images/40ytintro.09cf17cbf9dd4cf8faa91668c42172417f86851025ef325454ce65903606bb9e.zh.jpg)](https://youtu.be/HmKpHErUEHM)

**免责声明**：
本文件已使用基于机器的人工智能翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原文档的母语版本视为权威来源。对于关键信息，建议进行专业人工翻译。对于因使用本翻译而产生的任何误解或误读，我们不承担任何责任。