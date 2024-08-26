# **在 Ollama 中使用 Phi-3**

[Ollama](https://ollama.com) 允許更多人通過簡單的腳本直接部署開源 LLM 或 SLM，並且還可以建構 API 來幫助本地 Copilot 應用場景。

## **1. 安裝**

Ollama 支援在 Windows、macOS 和 Linux 上執行。你可以通過這個連結安裝 Ollama ([https://ollama.com/download](https://ollama.com/download))。安裝成功後，你可以直接使用 Ollama 腳本通過終端視窗呼叫 Phi-3。你可以查看 [Ollama 中所有可用的函式庫](https://ollama.com/library)。如果你在 Codespace 中打開這個儲存庫，它將已經安裝了 Ollama。

```bash

ollama run phi3

```

***注意:*** 第一次執行時將先下載模型。當然，你也可以直接指定已下載的 Phi-3 模型。我們以 WSL 為例來執行命令。模型下載成功後，你可以直接在終端機上互動。

![執行](../../../../imgs/02/Ollama/ollama_run.png)

## **2. 從 Ollama 呼叫 phi-3 API**

如果你想呼叫由 ollama 產生的 Phi-3 API，你可以在終端機中使用此命令來啟動 Ollama 伺服器。

```bash

ollama serve

```

***注意:*** 如果執行 MacOS 或 Linux，請注意您可能會遇到以下錯誤 <b>"Error: listen tcp 127.0.0.1:11434: bind: address already in use"</b>。當呼叫執行該命令時，您可能會遇到此錯誤。您可以忽略該錯誤，因為這通常表示伺服器已經在執行，或者您可以停止並重新啟動 Ollama:

**macOS**

```bash

brew services restart ollama

```

**Linux**

```bash

sudo systemctl stop ollama

```

Ollama 支援兩個 API: generate 和 chat。你可以根據需要呼叫 Ollama 提供的模型 API，通過向執行在 11434 埠的本地服務發送請求。

**聊天**

```bash

curl http://127.0.0.1:11434/api/chat -d '{
  "model": "phi3",
  "messages": [
    {
      "role": "system",
      "content": "你是一名 Python 開發者。"
    },
    {
      "role": "user",
      "content": "幫我生成一個冒泡排序算法"
    }
  ],
  "stream": false

}'

```

這是 Postman 的結果

![JSON 結果的截圖，用於聊天請求](../../../../imgs/02/Ollama/ollama_chat.png)

```bash

curl http://127.0.0.1:11434/api/generate -d '{
  "model": "phi3",
  "prompt": "<|system|>你是我的 AI 助理。<|end|><|user|>告訴我如何學習 AI<|end|><|assistant|>",
  "stream": false
}'

```

這是 Postman 的結果

![JSON 生成請求結果的截圖](../../../../imgs/02/Ollama/ollama_gen.png)

# 其他資源

查看 Ollama 中可用模型的列表在[他們的函式庫](https://ollama.com/library)。

使用此命令從 Ollama 伺服器拉取您的模型

```bash
ollama pull phi3
```

使用此命令執行模型

```bash
ollama run phi3
```

***注意:*** 訪問此連結 [https://github.com/ollama/ollama/blob/main/docs/api.md](https://github.com/ollama/ollama/blob/main/docs/api.md) 以了解更多資訊

## 從 Python 呼叫 Ollama

你可以使用 `requests` 或 `urllib3` 向上述使用的本地伺服器端點發出請求。然而，一種在 Python 中使用 Ollama 的流行方法是通過 [openai](https://pypi.org/project/openai/) SDK，因為 Ollama 也提供與 OpenAI 相容的伺服器端點。

這裡是 phi3-mini 的一個範例:

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
        {"role": "system", "content": "你是一個有幫助的助手。"},
        {"role": "user", "content": "寫一首關於飢餓貓咪的俳句"},
    ],
)

print("回應:")
print(response.choices[0].message.content)
```

## 從 JavaScript 呼叫 Ollama

```javascript
// 範例：使用 Phi-3 摘要檔案
script({
    model: "ollama:phi3",
    title: "使用 Phi-3 摘要",
    system: ["system"],
})

// 摘要範例
const file = def("FILE", env.files)
$`將 ${file} 摘要為一個段落。`
```

## 從 C# 呼叫 Ollama

建立一個新的 C# Console 應用程式並新增以下的 NuGet 套件:

```bash
dotnet add package Microsoft.SemanticKernel --version 1.13.0
```

然後在 `Program.cs` 文件中替換此程式碼

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;

// 使用本地 ollama 伺服器端點添加聊天完成服務
#pragma warning disable SKEXP0001, SKEXP0003, SKEXP0010, SKEXP0011, SKEXP0050, SKEXP0052
builder.AddOpenAIChatCompletion(
    modelId: "phi3.5",
    endpoint: new Uri("http://localhost:11434/"),
    apiKey: "non required");

// 向聊天服務呼叫一個簡單的提示
string prompt = "寫一個關於小貓的笑話";
var response = await kernel.InvokePromptAsync(prompt);
Console.WriteLine(response.GetValue<string>());
```

執行應用程式的指令:

```bash
dotnet run
```

