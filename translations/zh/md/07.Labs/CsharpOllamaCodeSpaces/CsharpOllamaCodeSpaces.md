# Ollama C# Playground

这个实验室旨在直接在 GitHub Codespaces 中使用 C# 示例测试 Phi-3，为任何人提供一种在浏览器中尝试 SLMs（小语言模型）的简便方法。

## 如何创建 C# + Ollama + Phi-3 Codespace

1. 使用仓库顶部的 `Code` 按钮创建一个新的 Codespace。选择 [+ New with options ...]
![创建带选项的 Codespace](../../../../../translated_images/10NewCodespacesWithOptions.b50796422fc7f6d13721a50b72de8b62d83a7951fdace787a0dc12edc22ce807.zh.png)

1. 在选项页面中，选择名为 `Ollama with Phi-3 for C#` 的配置

![选择 Ollama with Phi-3 for C# 选项以创建 Codespace](../../../../../translated_images/12NewCSOllamaCodespace.38aab1c942efe444653b4141918ce6d081ce6e9638e0d16117f5b93ce1deee42.zh.png)

1. 一旦 Codespace 加载完成，它应该已经预安装了 [ollama](https://ollama.com/)，下载了最新的 Phi-3 模型，并安装了 [.NET 8](https://dotnet.microsoft.com/download)。

1. （可选）使用 Codespace 终端，要求 Ollama 运行 [phi3](https://ollama.com/library/phi3) 模型：

    ```shell
    ollama run phi3
    ```

4. 你可以从提示符向该模型发送消息。

    ```shell
    >>> Write a joke about kittens
    ```

5. 几秒钟后，你应该会看到模型返回的响应流。

    ![运行 ollama 并请求一个笑话](../../../../../md/07.Labs/CsharpOllamaCodeSpaces/20ollamarunphi.gif)

1. 要了解与语言模型相关的不同技术，请查看 `.\src` 文件夹中的示例项目：

| 项目 | 描述 |
|---------|-------------|
| Sample01  | 这是一个使用 Ollama 模型中的 Phi-3 回答问题的示例项目。 |
| Sample02  | 这是一个使用 Semantic Kernel 实现控制台聊天的示例项目。 |
| [Sample03](./src/Sample03/readme.md)  | 这是一个使用本地嵌入和 Semantic Kernel 实现 RAG 的示例项目。查看本地 RAG 的详细信息 [这里](./src/Sample03/readme.md) |

## 如何运行一个示例

1. 打开终端并导航到所需的项目。例如，我们运行 `Sample02`，控制台聊天。

    ```bash
    cd .\src\Sample02\
    ```

1. 使用以下命令运行项目

    ```bash
    dotnet run
    ```

1. 项目 `Sample02` 定义了一个自定义系统消息：

    ```csharp
    var history = new ChatHistory();
    history.AddSystemMessage("You are a useful chatbot. If you don't know an answer, say 'I don't know!'. Always reply in a funny ways. Use emojis if possible.");

    ```

1. 因此，当用户提出问题，如 `What is the capital of Italy?`，聊天会使用本地模式回复。
   
    输出类似如下：

    ![聊天运行演示](../../../../../translated_images/20SampleConsole.22997336ed0fa683bcc3238bb8e953b3a533d28196bc42e7cd1527261dd0689b.zh.png)

## 视频教程

如果你想了解更多关于如何在 GitHub 仓库中使用 Codespaces 和 Ollama，请查看以下 3 分钟视频：

[![观看视频](../../../../../translated_images/40ytintro.09cf17cbf9dd4cf8faa91668c42172417f86851025ef325454ce65903606bb9e.zh.jpg)](https://youtu.be/HmKpHErUEHM)

免责声明：本翻译由AI模型从原文翻译而来，可能不够完美。请审核输出内容并进行必要的修改。