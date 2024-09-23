## GitHub Models - 公開測試版

歡迎來到 [GitHub Models](https://github.com/marketplace/models)！我們已經準備好讓你探索 Azure AI 上的 AI 模型。

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.a652f32407f52c16c528c26d70462aba0e55e3ff90d17ebbc9dffd9533c39363.tw.png)

想了解更多關於 GitHub Models 上可用的模型，請查看 [GitHub Model Marketplace](https://github.com/marketplace/models)

## 可用模型

每個模型都有專屬的 playground 和範例代碼

![Phi-3Model_Github](../../../../translated_images/GitHub_ModelPlay.e87859d6934a9e70830479431732ecc1826348036ebb998882091be8fa5d4fe7.tw.png)

### GitHub Model Catalog 中的 Phi-3 模型

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## 開始使用

我們已經準備了一些基本範例供你運行。你可以在 samples 目錄中找到它們。如果你想直接跳到你喜歡的語言，可以在以下語言中找到範例：

- Python
- JavaScript
- cURL

我們還提供了一個專用的 Codespaces 環境來運行範例和模型。

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.7eddfc63957b37d8cf9803ec7073b3545f5002d3dae7ab3034ad5fec267e6beb.tw.png)

## 範例代碼

以下是一些用例的範例代碼片段。想了解更多關於 Azure AI Inference SDK 的信息，請查看完整的文檔和範例。

## 設置

1. 創建一個個人訪問令牌
你不需要給這個令牌任何權限。請注意，這個令牌將被發送到 Microsoft 服務。

要使用下面的代碼片段，請創建一個環境變量，將你的令牌設置為客戶端代碼的密鑰。

如果你使用 bash:
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```
如果你在 powershell 中：

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```

如果你使用 Windows 命令提示符：

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```

## Python 範例

### 安裝依賴
使用 pip 安裝 Azure AI Inference SDK (要求：Python >=3.8)：

```
pip install azure-ai-inference
```
### 運行一個基本代碼範例

這個範例演示了如何基本調用 chat completion API。它利用了 GitHub AI 模型推理端點和你的 GitHub 令牌。這個調用是同步的。

```
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.inference.ai.azure.com"
# 替換 Model_Name
model_name = "Phi-3-small-8k-instruct"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="What is the capital of France?"),
    ],
    model=model_name,
    temperature=1.,
    max_tokens=1000,
    top_p=1.
)

print(response.choices[0].message.content)
```

### 運行多輪對話

這個範例演示了如何進行多輪對話。當你在聊天應用中使用這個模型時，你需要管理對話的歷史記錄，並將最新的消息發送給模型。

```
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
# 替換 Model_Name
model_name = "Phi-3-small-8k-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    UserMessage(content="What is the capital of France?"),
    AssistantMessage(content="The capital of France is Paris."),
    UserMessage(content="What about Spain?"),
]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

### 流式輸出

為了提供更好的用戶體驗，你會希望流式輸出模型的響應，這樣第一個 token 會更早顯示，避免等待長時間的響應。

```
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
# 替換 Model_Name
model_name = "Phi-3-small-8k-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    stream=True,
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="Give me 5 good reasons why I should exercise every day."),
    ],
    model=model_name,
)

for update in response:
    if update.choices:
        print(update.choices[0].delta.content or "", end="")

client.close()
```
## JavaScript

### 安裝依賴

安裝 Node.js。

將以下文本複製並保存為 package.json 文件，放在你的文件夾內。

```
{
  "type": "module",
  "dependencies": {
    "@azure-rest/ai-inference": "latest",
    "@azure/core-auth": "latest",
    "@azure/core-sse": "latest"
  }
}
```

注意：@azure/core-sse 只有在你流式輸出 chat completions 響應時才需要。

在這個文件夾中打開終端窗口，運行 npm install。

對於下面的每個代碼片段，將內容複製到一個名為 sample.js 的文件中，並使用 node sample.js 運行。

### 運行一個基本代碼範例

這個範例演示了如何基本調用 chat completion API。它利用了 GitHub AI 模型推理端點和你的 GitHub 令牌。這個調用是同步的。

```
import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";
// 更新你的 modelname
const modelName = "Phi-3-small-8k-instruct";

export async function main() {

  const client = new ModelClient(endpoint, new AzureKeyCredential(token));

  const response = await client.path("/chat/completions").post({
    body: {
      messages: [
        { role:"system", content: "You are a helpful assistant." },
        { role:"user", content: "What is the capital of France?" }
      ],
      model: modelName,
      temperature: 1.,
      max_tokens: 1000,
      top_p: 1.
    }
  });

  if (response.status !== "200") {
    throw response.body.error;
  }
  console.log(response.body.choices[0].message.content);
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
```

### 運行多輪對話

這個範例演示了如何進行多輪對話。當你在聊天應用中使用這個模型時，你需要管理對話的歷史記錄，並將最新的消息發送給模型。

```
import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";
// 更新你的 modelname
const modelName = "Phi-3-small-8k-instruct";

export async function main() {

  const client = new ModelClient(endpoint, new AzureKeyCredential(token));

  const response = await client.path("/chat/completions").post({
    body: {
      messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "What is the capital of France?" },
        { role: "assistant", content: "The capital of France is Paris." },
        { role: "user", content: "What about Spain?" },
      ],
      model: modelName,
    }
  });

  if (response.status !== "200") {
    throw response.body.error;
  }

  for (const choice of response.body.choices) {
    console.log(choice.message.content);
  }
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
```

### 流式輸出

為了提供更好的用戶體驗，你會希望流式輸出模型的響應，這樣第一個 token 會更早顯示，避免等待長時間的響應。

```
import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";
import { createSseStream } from "@azure/core-sse";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";
// 更新你的 modelname
const modelName = "Phi-3-small-8k-instruct";

export async function main() {

  const client = new ModelClient(endpoint, new AzureKeyCredential(token));

  const response = await client.path("/chat/completions").post({
    body: {
      messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "Give me 5 good reasons why I should exercise every day." },
      ],
      model: modelName,
      stream: true
    }
  }).asNodeStream();

  const stream = response.body;
  if (!stream) {
    throw new Error("The response stream is undefined");
  }

  if (response.status !== "200") {
    stream.destroy();
    throw new Error(`Failed to get chat completions, http operation failed with ${response.status} code`);
  }

  const sseStream = createSseStream(stream);

  for await (const event of sseStream) {
    if (event.data === "[DONE]") {
      return;
    }
    for (const choice of (JSON.parse(event.data)).choices) {
        process.stdout.write(choice.delta?.content ?? ``);
    }
  }
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
```

## REST

### 運行一個基本代碼範例

將以下內容粘貼到 shell 中：

```
curl -X POST "https://models.inference.ai.azure.com/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -d '{
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What is the capital of France?"
            }
        ],
        "model": "Phi-3-small-8k-instruct"
    }'
```
### 運行多輪對話

調用 chat completion API 並傳遞聊天歷史記錄：

```
curl -X POST "https://models.inference.ai.azure.com/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -d '{
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What is the capital of France?"
            },
            {
                "role": "assistant",
                "content": "The capital of France is Paris."
            },
            {
                "role": "user",
                "content": "What about Spain?"
            }
        ],
        "model": "Phi-3-small-8k-instruct"
    }'
```
### 流式輸出

這是一個調用端點並流式輸出響應的範例。

```
curl -X POST "https://models.inference.ai.azure.com/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -d '{
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Give me 5 good reasons why I should exercise every day."
            }
        ],
        "stream": true,
        "model": "Phi-3-small-8k-instruct"
    }'
```

## GitHub Models 的免費使用和速率限制

![Model Catalog](../../../../translated_images/GitHub_Model.7cf5115ec8870189517837690a06a18f35716f5b491a315303414a42cf9f9a4e.tw.png)

[playground 和免費 API 使用的速率限制](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) 是為了幫助你實驗模型和原型你的 AI 應用。超過這些限制的使用，以及將你的應用擴展到規模，你必須從 Azure 帳戶中提供資源，並從那裡進行身份驗證，而不是使用你的 GitHub 個人訪問令牌。你不需要更改代碼中的任何其他內容。使用此鏈接了解如何超越 Azure AI 的免費層限制。

### 聲明

記住，在與模型交互時，你是在實驗 AI，所以內容錯誤是可能的。

該功能受到各種限制（包括每分鐘請求數、每天請求數、每次請求的 token 數量和並發請求數量），不適用於生產環境。

GitHub Models 使用 Azure AI Content Safety。這些過濾器在 GitHub Models 體驗中無法關閉。如果你決定通過付費服務使用模型，請配置你的內容過濾器以滿足你的要求。

此服務受 GitHub 的預發布條款約束。

免責聲明：此翻譯是由人工智慧模型從原文翻譯而來，可能不完美。請檢查輸出並進行必要的修正。