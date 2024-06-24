# AI Toolkit for VScode (Windows)

[AI Toolkit for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) 通過整合來自 Azure AI Studio Catalog 和其他如 Hugging Face 的目錄中的尖端 AI 開發工具和模型，簡化了生成式 AI 應用程式的開發。您將能夠瀏覽由 Azure ML 和 Hugging Face 提供支持的 AI 模型目錄，將它們下載到本地，進行微調、測試並在您的應用程式中使用。

AI Toolkit Preview 將在本地執行。根據您選擇的模型，一些任務僅支援 Windows 和 Linux，

根據你選擇的模型，本地推論或微調可能需要 GPU，例如 NVIDIA CUDA GPU。

如果你遠端執行，雲端資源需要有 GPU，請確保檢查你的環境。對於在 Windows + WSL 上本地執行，應安裝 WSL Ubuntu 發行版 18.4 或更高版本，並在使用 AI Toolkit 之前設置為預設。

## 開始使用

[了解更多如何安裝 Windows 子系統 for Linux](https://learn.microsoft.com/windows/wsl/install)

和 [changing default distribution](https://learn.microsoft.com/windows/wsl/install#change-the-default-linux-distribution-installed)。

[AI Tooklit GitHub Repo](https://github.com/microsoft/vscode-ai-toolkit/)。

- Windows 或 Linux。
- **MacOS 支援即將推出**

- 在 Windows 和 Linux 上進行微調時，你需要一個 Nvidia GPU。此外，**Windows** 需要 Linux 子系統，並且使用 Ubuntu 18.4 或更高版本。 [了解更多如何安裝 Windows 子系統 for Linux](https://learn.microsoft.com/windows/wsl/install) 和 [更改預設的發行版](https://learn.microsoft.com/windows/wsl/install#change-the-default-linux-distribution-installed)。

### 安裝 AI 工具包

AI Toolkit 以 [Visual Studio Code Extension](https://code.visualstudio.com/docs/setup/additional-components#_vs-code-extensions) 的形式提供，因此你需要先安裝 [VS Code](https://code.visualstudio.com/docs/setup/windows)，並從 [VS Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) 下載 AI Toolkit。
[AI Toolkit 可在 Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) 中找到，並且可以像其他 VS Code 擴展一樣安裝。

如果你不熟悉安裝 VS Code 擴充功能，請按照以下步驟操作:

### 登入

1. 在 VS Code 的活動列中選擇 **Extensions**
1. 在 Extensions 搜尋欄中輸入 "AI Toolkit"
1. 選擇 "AI Toolkit for Visual Studio code"
1. 選擇 **Install**

現在，你已經準備好使用這個擴充功能了！

您將被提示登入 GitHub，請點擊 "Allow" 以繼續。您將被重定向到 GitHub 登入頁面。

請登入並按照流程步驟操作。完成後，您將被重定向到 VS Code。

一旦擴充功能安裝完成，你會在活動欄中看到 AI Toolkit 圖示。

讓我們探索可用的操作吧!

### 從目錄下載模型

### 可用動作

AI 工具包的主要側邊欄組織成

- **模型**
- **資源**
- **遊樂場**
- **微調**

資源部分提供。要開始，請選擇

**模型目錄**:

啟動 AI Toolkit 從 VS Code 側邊欄後，你可以從以下選項中選擇:

![AI 工具包模型目錄](../../../../imgs/04/04/AItoolkitmodel_catalog.png)

- 從 **Model Catalog** 中找到支援的模型並下載到本地
- 在 **Model Playground** 中測試模型推論
- 在 **Model Fine-tuning** 中本地或遠端微調模型
- 通過命令調色盤將微調後的模型部署到雲端以使用 AI Toolkit

**GPU Vs CPU**

你會注意到模型卡片顯示了模型大小、平台和加速器類型 (CPU, GPU)。為了在**至少有一個 GPU 的 Windows 裝置**上獲得最佳效能，請選擇僅針對 Windows 的模型版本。

這確保您擁有為 DirectML 加速器優化的模型。

模型名稱的格式為

-  `{model_name}-{accelerator}-{quantization}-{format}`.

>要檢查你的 Windows 裝置是否有 GPU，請打開 **Task Manager**，然後選擇 **Performance** 標籤。如果你有 GPU，它們會列在像 "GPU 0" 或 "GPU 1" 這樣的名稱下。

### 在 playground 中執行模型

在所有參數設定完成後，點擊 **Generate Project**。

一旦您的模型已下載，請在目錄中的模型卡上選擇 **Load in Playground**:

- 開始下載模型
- 安裝所有先決條件和相依套件
- 建立 VS Code 工作區

![在 playground 中載入模型](../../../../imgs/04/04/AItoolkitload_model_into_playground.png)

當模型下載完成後，你可以從 AI Toolkit 啟動專案。

> ***注意*** 如果你想嘗試預覽功能來遠端進行推論或微調，請遵循[此指南](https://aka.ms/previewFinetune)。

### Windows 優化模型

你應該會看到模型回應串流回來：

AI Toolkit 提供了已經為 Windows 優化的公開可用 AI 模型集合。這些模型存儲在不同的位置，包括 Hugging Face、GitHub 和其他地方，但你可以瀏覽這些模型，並在一個地方找到所有準備下載和用於你的 Windows 應用程式的模型。

![生成流](../../../../imgs/04/04/AItoolkitgeneration-gif.gif)

### 模型選擇

> 如果您的 *Windows* 裝置上**沒有**可用的 **GPU**，但您選擇了

- Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx 模型

模型回應會*非常慢*。

你應該下載 CPU 優化版本:

- Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx.

也可以更改:

**上下文說明:** 幫助模型了解您請求的更大背景。這可以是背景資訊、您想要的範例/展示或解釋您任務的目的。

**推論參數:**

- *最大回應長度*: 模型將返回的最大 token 數量。
  - *溫度*: 模型溫度是一個控制語言模型輸出隨機性的參數。較高的溫度意味著模型會承擔更多風險，給你多樣化的詞語組合。另一方面，較低的溫度使模型更保守，專注於更具預測性的回應。
  - *Top P*: 也稱為核取樣，是一個控制語言模型在預測下一個詞時考慮多少可能詞語或短語的設定。
  - *頻率懲罰*: 此參數影響模型在輸出中重複詞語或短語的頻率。較高的值（接近 1.0）鼓勵模型*避免*重複詞語或短語。
  - *存在懲罰*: 此參數用於生成式 AI 模型中，以鼓勵生成文本的多樣性和特異性。較高的值（接近 1.0）鼓勵模型包含更多新穎和多樣的 token。較低的值則更可能使模型生成常見或陳詞濫調的短語。

### 在你的應用程式中使用 REST API

AI 工具包附帶一個本地 REST API 網頁伺服器 **在 5272 埠**，使用 [OpenAI chat completions format](https://platform.openai.com/docs/api-reference/chat/create)。

這使您能夠在本地測試您的應用程式，而不必依賴雲端 AI 模型服務。例如，以下 JSON 文件顯示如何配置請求的主體:

```json
{
    "model": "Phi-3-mini-4k-directml-int4-awq-block-128-onnx",
    "messages": [
        {
            "role": "user",
            "content": "黃金比例是什麼？"
        }
    ],
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 10,
    "max_tokens": 100,
    "stream": true
}
```

你可以使用（例如）[Postman](https://www.postman.com/) 或 CURL（Client URL）工具來測試 REST API:

```bash
curl -vX POST http://127.0.0.1:5272/v1/chat/completions -H 'Content-Type: application/json' -d @body.json
```

### 使用 OpenAI 用於 Python 的函式庫

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:5272/v1/",
    api_key="x" # required for the API but not used
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "黃金比例是什麼？",
        }
    ],
    model="Phi-3-mini-4k-cuda-int4-onnx",
)

print(chat_completion.choices[0].message.content)
```

### 使用 Azure OpenAI 客戶端函式庫 for .NET

將 [Azure OpenAI client 函式庫 for .NET](https://www.nuget.org/packages/Azure.AI.OpenAI/) 使用 NuGet 添加到您的專案中:

```bash
dotnet add {project_name} package Azure.AI.OpenAI --version 1.0.0-beta.17
```

將一個名為 **OverridePolicy.cs** 的 C# 文件添加到你的專案中，並貼上以下程式碼:

```csharp
// OverridePolicy.cs
using Azure.Core.Pipeline;
using Azure.Core;

internal partial class OverrideRequestUriPolicy(Uri overrideUri)
    : HttpPipelineSynchronousPolicy
{
    private readonly Uri _overrideUri = overrideUri;

    public override void OnSendingRequest(HttpMessage message)
    {
        message.Request.Uri.Reset(_overrideUri);
    }
}
```

接下來，將以下程式碼貼到你的 **Program.cs** 檔案中:

```csharp
// Program.cs
using Azure.AI.OpenAI;

Uri localhostUri = new("http://localhost:5272/v1/chat/completions");

OpenAIClientOptions clientOptions = new();
clientOptions.AddPolicy(
    new OverrideRequestUriPolicy(localhostUri),
    Azure.Core.HttpPipelinePosition.BeforeTransport);
OpenAIClient client = new(openAIApiKey: "unused", clientOptions);

ChatCompletionsOptions options = new()
{
    DeploymentName = "Phi-3-mini-4k-directml-int4-awq-block-128-onnx",
    Messages =
    {
        new ChatRequestSystemMessage("You are a helpful assistant. Be brief and succinct."),
        new ChatRequestUserMessage("What is the golden ratio?"),
    }
};

StreamingResponse<StreamingChatCompletionsUpdate> streamingChatResponse
    = await client.GetChatCompletionsStreamingAsync(options);

await foreach (StreamingChatCompletionsUpdate chatChunk in streamingChatResponse)
{
    Console.Write(chatChunk.ContentUpdate);
}
```

## 使用 AI 工具包進行微調

- 開始使用模型發現和 playground。
- 使用本地計算資源進行模型微調和推論。
- 使用 Azure 資源進行遠端微調和推論。

[使用 AI 工具包進行微調](../04.Fine-tuning/Finetuning_VSCodeaitoolkit.md)

## AI Toolkit Q&A Resources

請參考我們的 [Q&A 頁面](https://github.com/microsoft/vscode-ai-toolkit/blob/main/QA.md) 了解最常見的問題和解決方案。

