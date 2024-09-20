# AI Toolkit for VScode (Windows)

[AI Toolkit for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) 通过汇集来自 Azure AI Studio Catalog 和 Hugging Face 等其他目录的前沿 AI 开发工具和模型，简化了生成式 AI 应用开发。你可以浏览由 Azure ML 和 Hugging Face 提供支持的 AI 模型目录，下载到本地，进行微调、测试并在应用中使用它们。

AI Toolkit Preview 将在本地运行。根据你选择的模型，有些任务仅支持 Windows 和 Linux。

本地推理或微调，根据你选择的模型，可能需要像 NVIDIA CUDA GPU 这样的 GPU。

如果你在云端运行，云资源需要有 GPU，请确保检查你的环境。对于在 Windows + WSL 上本地运行，应该安装并设置默认的 WSL Ubuntu 发行版 18.4 或更高版本，然后再使用 AI Toolkit。

## 开始

[了解更多关于如何安装 Windows 子系统 Linux](https://learn.microsoft.com/windows/wsl/install?WT.mc_id=aiml-137032-kinfeylo)

和 [更改默认发行版](https://learn.microsoft.com/windows/wsl/install#change-the-default-linux-distribution-installed)。

[AI Tooklit GitHub 仓库](https://github.com/microsoft/vscode-ai-toolkit/)

- Windows 或 Linux。
- **MacOS 支持即将推出**
- 对于在 Windows 和 Linux 上进行微调，你需要一个 Nvidia GPU。此外，**Windows** 需要安装 Ubuntu 发行版 18.4 或更高版本的 Linux 子系统。[了解更多关于如何安装 Windows 子系统 Linux](https://learn.microsoft.com/windows/wsl/install) 和 [更改默认发行版](https://learn.microsoft.com/windows/wsl/install#change-the-default-linux-distribution-installed)。

### 安装 AI Toolkit

AI Toolkit 作为 [Visual Studio Code 扩展](https://code.visualstudio.com/docs/setup/additional-components#_vs-code-extensions)发布，因此你需要先安装 [VS Code](https://code.visualstudio.com/docs/setup/windows?WT.mc_id=aiml-137032-kinfeylo)，然后从 [VS Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) 下载 AI Toolkit。
[AI Toolkit 在 Visual Studio Marketplace 中可用](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)，可以像安装其他 VS Code 扩展一样安装。

如果你不熟悉安装 VS Code 扩展，请按照以下步骤操作：

### 登录

1. 在 VS Code 的活动栏中选择 **Extensions**
1. 在扩展搜索栏中输入 "AI Toolkit"
1. 选择 "AI Toolkit for Visual Studio code"
1. 选择 **Install**

现在，你已经准备好使用这个扩展了！

系统会提示你登录 GitHub，请点击 "Allow" 继续。你将被重定向到 GitHub 登录页面。

请登录并按照步骤操作。成功完成后，你将被重定向到 VS Code。

扩展安装完成后，你会在活动栏中看到 AI Toolkit 图标。

让我们探索可用的操作！

### 可用操作

AI Toolkit 的主侧边栏组织成  

- **Models**
- **Resources**
- **Playground**  
- **Fine-tuning**

这些都在 Resources 部分。要开始，选择 **Model Catalog**。

### 从目录下载模型

从 VS Code 侧边栏启动 AI Toolkit 后，你可以选择以下选项：

![AI toolkit model catalog](../../../../translated_images/AItoolkitmodel_catalog.49200354ddc7aceecdcab2080769d898b1fd50424ef9f7014aafeb790028c49d.zh.png)

- 从 **Model Catalog** 中找到一个支持的模型并下载到本地
- 在 **Model Playground** 中测试模型推理
- 在 **Model Fine-tuning** 中本地或远程微调模型
- 通过 AI Toolkit 的命令面板将微调后的模型部署到云端

> [!NOTE]
>
> **GPU 与 CPU**
>
> 你会注意到模型卡片显示了模型大小、平台和加速器类型（CPU、GPU）。对于 **Windows 设备至少有一个 GPU** 的优化性能，选择仅针对 Windows 的模型版本。
>
> 这确保你有一个为 DirectML 加速器优化的模型。
>
> 模型名称的格式为
>
> - `{model_name}-{accelerator}-{quantization}-{format}`。
>
>要检查你的 Windows 设备是否有 GPU，请打开 **任务管理器**，然后选择 **性能** 选项卡。如果有 GPU，它们会列在 "GPU 0" 或 "GPU 1" 等名称下。

### 在 playground 中运行模型

设置所有参数后，点击 **Generate Project**。

模型下载后，在目录的模型卡片中选择 **Load in Playground**：

- 启动模型下载
- 安装所有先决条件和依赖项
- 创建 VS Code 工作区

![Load model in playground](../../../../translated_images/AItoolkitload_model_into_playground.f78799b4838c6521be6a296729279525958dec6cfb9a26c64752e397dfe19ef2.zh.png)

模型下载完成后，你可以从 AI Toolkit 启动项目。

> ***Note*** 如果你想尝试预览功能进行远程推理或微调，请按照 [本指南](https://aka.ms/previewFinetune)

### 为 Windows 优化的模型

你应该看到模型响应流回给你：

AI Toolkit 提供了一系列已经为 Windows 优化的公开可用 AI 模型。这些模型存储在不同的位置，包括 Hugging Face、GitHub 等，但你可以浏览模型并在一个地方找到所有准备下载和在 Windows 应用中使用的模型。

![Generation stream](../../../../imgs/04/04/AItoolkitgeneration-gif.gif)

### 模型选择

如果你的 *Windows* 设备上**没有**可用的 **GPU**，但你选择了

- Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx 模型

模型响应将会*非常慢*。

你应该下载 CPU 优化版本：

- Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx。

还可以更改：

**上下文说明：** 帮助模型理解你的请求的整体背景。这可以是背景信息、你想要的示例/演示或解释你的任务目的。

**推理参数：**

- *最大响应长度*: 模型返回的最大标记数。
- *温度*: 模型温度是一个控制语言模型输出随机性的参数。较高的温度意味着模型会冒更多风险，给你一个多样化的词汇组合。相反，较低的温度使模型更保守，保持更集中和可预测的响应。
- *Top P*: 也称为核采样，是一个控制语言模型在预测下一个词时考虑多少可能词或短语的设置。
- *频率惩罚*: 这个参数影响模型在输出中重复词语或短语的频率。值越高（接近 1.0），鼓励模型*避免*重复词语或短语。
- *存在惩罚*: 这个参数用于生成式 AI 模型中，鼓励生成文本的多样性和特异性。值越高（接近 1.0），鼓励模型包含更多新颖和多样的标记。较低的值更可能使模型生成常见或陈词滥调的短语。

### 在应用中使用 REST API 

AI Toolkit 附带一个本地 REST API Web 服务器 **在端口 5272**，使用 [OpenAI 聊天完成格式](https://platform.openai.com/docs/api-reference/chat/create)。

这使你可以在本地测试应用程序，而无需依赖云端 AI 模型服务。例如，以下 JSON 文件显示如何配置请求的主体：

```json
{
    "model": "Phi-3-mini-4k-directml-int4-awq-block-128-onnx",
    "messages": [
        {
            "role": "user",
            "content": "what is the golden ratio?"
        }
    ],
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 10,
    "max_tokens": 100,
    "stream": true
}
```

你可以使用 [Postman](https://www.postman.com/) 或 CURL（客户端 URL）工具测试 REST API：

```bash
curl -vX POST http://127.0.0.1:5272/v1/chat/completions -H 'Content-Type: application/json' -d @body.json
```

### 使用 OpenAI Python 客户端库

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
            "content": "what is the golden ratio?",
        }
    ],
    model="Phi-3-mini-4k-cuda-int4-onnx",
)

print(chat_completion.choices[0].message.content)
```

### 使用 Azure OpenAI .NET 客户端库

使用 NuGet 将 [Azure OpenAI .NET 客户端库](https://www.nuget.org/packages/Azure.AI.OpenAI/) 添加到你的项目：

```bash
dotnet add {project_name} package Azure.AI.OpenAI --version 1.0.0-beta.17
```

将一个名为 **OverridePolicy.cs** 的 C# 文件添加到你的项目并粘贴以下代码：

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

接下来，将以下代码粘贴到你的 **Program.cs** 文件中：

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

## 使用 AI Toolkit 进行微调

- 从模型发现和 playground 开始。
- 使用本地计算资源进行模型微调和推理。
- 使用 Azure 资源进行远程微调和推理。

[使用 AI Toolkit 进行微调](../04.Fine-tuning/Finetuning_VSCodeaitoolkit.md)

## AI Toolkit 问答资源

请参考我们的 [问答页面](https://github.com/microsoft/vscode-ai-toolkit/blob/main/QA.md) 了解最常见的问题和解决方案。

免责声明：此翻译由人工智能模型从原文翻译而来，可能不够完美。请审阅输出内容并进行必要的修改。