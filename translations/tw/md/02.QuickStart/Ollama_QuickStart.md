# **在 Ollama 中使用 Phi-3**

[Ollama](https://ollama.com) 讓更多人可以通過簡單的腳本直接部署開源 LLM 或 SLM，也可以構建 API 來幫助本地 Copilot 應用場景。

## **1. 安裝**

Ollama 支持在 Windows、macOS 和 Linux 上運行。你可以通過這個鏈接 ([https://ollama.com/download](https://ollama.com/download)) 安裝 Ollama。安裝成功後，你可以直接在終端窗口使用 Ollama 腳本調用 Phi-3。你可以看到所有 [Ollama 可用的庫](https://ollama.com/library)。如果你在 Codespace 中打開這個存儲庫，它已經安裝了 Ollama。

```bash

ollama run phi3

```

> [!NOTE]
> 第一次運行時，模型會先下載。當然，你也可以直接指定下載的 Phi-3 模型。我們以 WSL 為例來運行這個命令。模型下載成功後，你可以直接在終端上進行交互。

![run](../../../../translated_images/ollama_run.302aa6484e50a7f8f09b40c787dc22eea10525cac6287c92825c8fc80c012c48.tw.png)

## **2. 從 Ollama 調用 phi-3 API**

如果你想調用 Ollama 生成的 Phi-3 API，可以在終端中使用這個命令啟動 Ollama 服務器。

```bash

ollama serve

```

> [!NOTE]
> 如果運行 MacOS 或 Linux，請注意你可能會遇到以下錯誤 **"Error: listen tcp 127.0.0.1:11434: bind: address already in use"** 你可能會在運行命令時遇到這個錯誤。你可以忽略這個錯誤，因為它通常表示服務器已經在運行，或者你可以停止並重新啟動 Ollama：

**macOS**

```bash

brew services restart ollama

```

**Linux**

```bash

sudo systemctl stop ollama

```

Ollama 支持兩個 API：generate 和 chat。你可以根據需要調用 Ollama 提供的模型 API，向運行在端口 11434 的本地服務發送請求。

**Chat**

```bash

curl http://127.0.0.1:11434/api/chat -d '{
  "model": "phi3",
  "messages": [
    {
      "role": "system",
      "content": "Your are a python developer."
    },
    {
      "role": "user",
      "content": "Help me generate a bubble algorithm"
    }
  ],
  "stream": false
  
}'


```

這是在 Postman 中的結果

![Screenshot of JSON results for chat request](../../../../translated_images/ollama_chat.25d29e9741e1daa8efd30ca36e60008b6f2841edb544ca8167645e0ec750c72a.tw.png)

```bash

curl http://127.0.0.1:11434/api/generate -d '{
  "model": "phi3",
  "prompt": "<|system|>Your are my AI assistant.<|end|><|user|>tell me how to learn AI<|end|><|assistant|>",
  "stream": false
}'


```

這是在 Postman 中的結果

![Screenshot of JSON results for generate request](../../../../translated_images/ollama_gen.523df35c3c34f0ada4770f77c9bb68f55442958adffe73ba5ae03e417ff9a781.tw.png)

## 其他資源

查看 Ollama 中可用模型的列表在 [他們的庫](https://ollama.com/library)。

使用這個命令從 Ollama 服務器拉取你的模型

```bash
ollama pull phi3
```

使用這個命令運行模型

```bash
ollama run phi3
```

***注意:*** 訪問這個鏈接 [https://github.com/ollama/ollama/blob/main/docs/api.md](https://github.com/ollama/ollama/blob/main/docs/api.md) 了解更多

## 從 Python 調用 Ollama

你可以使用 `requests` or `urllib3` 向上述本地服務器端點發送請求。然而，一種在 Python 中使用 Ollama 的流行方式是通過 [openai](https://pypi.org/project/openai/) SDK，因為 Ollama 提供了與 OpenAI 兼容的服務器端點。

這是 phi3-mini 的一個例子：

```python
import openai

client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)

response = client.chat.completions.create(
    model="phi3",
    temperature=0.7,
    n=1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about a hungry cat"},
    ],
)

print("Response:")
print(response.choices[0].message.content)
```

## 從 JavaScript 調用 Ollama 

```javascript
// Example of Summarize a file with Phi-3
script({
    model: "ollama:phi3",
    title: "Summarize with Phi-3",
    system: ["system"],
})

// Example of summarize
const file = def("FILE", env.files)
$`Summarize ${file} in a single paragraph.`
```

## 從 C# 調用 Ollama

創建一個新的 C# 控制台應用程序並添加以下 NuGet 包：

```bash
dotnet add package Microsoft.SemanticKernel --version 1.13.0
```

然後在 `Program.cs` 文件中替換這段代碼

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;

// add chat completion service using the local ollama server endpoint
#pragma warning disable SKEXP0001, SKEXP0003, SKEXP0010, SKEXP0011, SKEXP0050, SKEXP0052
builder.AddOpenAIChatCompletion(
    modelId: "phi3.5",
    endpoint: new Uri("http://localhost:11434/"),
    apiKey: "non required");

// invoke a simple prompt to the chat service
string prompt = "Write a joke about kittens";
var response = await kernel.InvokePromptAsync(prompt);
Console.WriteLine(response.GetValue<string>());
```

使用這個命令運行應用程序：

```bash
dotnet run
```

**免責聲明**:
本文件使用基於機器的人工智能翻譯服務進行翻譯。雖然我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原語言的原始文件視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。