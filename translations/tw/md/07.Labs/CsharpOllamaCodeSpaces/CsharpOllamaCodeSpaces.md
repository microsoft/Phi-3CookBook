# Ollama C# Playground

這個實驗室旨在測試 Phi-3 與 C# 範例，直接在 GitHub Codespaces 中進行，讓任何人都能輕鬆地在瀏覽器中嘗試使用小型語言模型（SLMs）。

## 如何創建 C# + Ollama + Phi-3 Codespace

1. 使用倉庫頂部的 `Code` 按鈕創建一個新的 Codespace。選擇 [+ New with options ...]
![Create Codespace with options](../../../../../translated_images/10NewCodespacesWithOptions.b50796422fc7f6d13721a50b72de8b62d83a7951fdace787a0dc12edc22ce807.tw.png)

1. 在選項頁面中，選擇名為 `Ollama with Phi-3 for C#` 的配置

![Select the option Ollama with Phi-3 for C#, to create the CodeSpace](../../../../../translated_images/12NewCSOllamaCodespace.38aab1c942efe444653b4141918ce6d081ce6e9638e0d16117f5b93ce1deee42.tw.png)

1. 一旦 Codespace 加載完成，應該已經預先安裝了 [ollama](https://ollama.com/)，下載了最新的 Phi-3 模型，並安裝了 [.NET 8](https://dotnet.microsoft.com/download)。

1. （可選）使用 Codespace 終端，請 Ollama 運行 [phi3](https://ollama.com/library/phi3) 模型：

    ```shell
    ollama run phi3
    ```

4. 你可以從提示符向該模型發送消息。

    ```shell
    >>> Write a joke about kittens
    ```

5. 幾秒鐘後，你應該會看到模型的回應。

    ![run ollama and ask for a joke](../../../../../md/07.Labs/CsharpOllamaCodeSpaces/20ollamarunphi.gif)

1. 要了解使用語言模型的不同技術，請查看 `.\src` 文件夾中的範例項目：

| 項目 | 描述 |
|------|------|
| Sample01  | 這是一個範例項目，使用託管在 ollama 模型中的 Phi-3 來回答問題。 |
| Sample02  | 這是一個範例項目，使用 Semantic Kernel 實現一個控制台聊天。 |
| [Sample03](./src/Sample03/readme.md)  | 這是一個範例項目，使用本地嵌入和 Semantic Kernel 實現 RAG。查看本地 RAG 的詳細信息 [這裡](./src/Sample03/readme.md) |

## 如何運行範例

1. 打開終端並導航到所需的項目。例如，讓我們運行 `Sample02`，控制台聊天。

    ```bash
    cd .\src\Sample02\
    ```

1. 使用以下命令運行項目

    ```bash
    dotnet run
    ```

1. 項目 `Sample02` 定義了一個自定義系統消息：

    ```csharp
    var history = new ChatHistory();
    history.AddSystemMessage("You are a useful chatbot. If you don't know an answer, say 'I don't know!'. Always reply in a funny ways. Use emojis if possible.");

    ```

1. 當用戶問一個問題，例如 `What is the capital of Italy?`，聊天將使用本地模式回應。
   
    輸出類似於這個：

    ![Chat running demo](../../../../../translated_images/20SampleConsole.22997336ed0fa683bcc3238bb8e953b3a533d28196bc42e7cd1527261dd0689b.tw.png)

## 視頻教程

如果你想了解更多關於如何在 GitHub Repository 中使用 Codespaces 和 Ollama，請查看以下3分鐘視頻：

[![Watch the video](../../../../../translated_images/40ytintro.09cf17cbf9dd4cf8faa91668c42172417f86851025ef325454ce65903606bb9e.tw.jpg)](https://youtu.be/HmKpHErUEHM)

免責聲明：此翻譯由AI模型從原文翻譯而來，可能並不完美。請審閱輸出內容並進行必要的修正。