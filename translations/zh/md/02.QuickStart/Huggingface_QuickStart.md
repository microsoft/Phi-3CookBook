# **在 Hugging Face 上使用 Phi-3**

[Hugging Face](https://huggingface.co/) 是一个非常受欢迎的 AI 社区，拥有丰富的数据和开源模型资源。不同的厂商会通过 Hugging Face 发布开源的 LLM 和 SLM，比如微软、Meta、Mistral、苹果、谷歌等。

![Phi3](../../../../translated_images/Hg_Phi3.dc94956455e775c886b69f7430a05b7a42aab729a81fa4083c906812edb475f8.zh.png)

微软的 Phi-3 已经在 Hugging Face 上发布。开发者可以根据场景和业务需求下载相应的 Phi-3 模型。除了在 Hugging Face 上部署 Phi-3 的 Pytorch 模型外，我们还发布了量化模型，使用 GGUF 和 ONNX 格式，给终端用户更多选择。

## **1. 从 Hugging Face 下载 Phi-3**

```bash

git lfs install 

git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

```

## **2. 了解 Phi-3 提示模板**

在训练 Phi-3 时有特定的数据模板，所以在使用 Phi-3 时，发送提示需要通过模板来设置。在微调时，数据也需要根据模板进行扩展。

模板有三个角色，包括系统、用户和助手。

```txt

<|system|>
Your Role<|end|>
<|user|>
Your Question?<|end|>
<|assistant|>

```

例如

```txt

<|system|>
Your are a python developer.<|end|>
<|user|>
Help me generate a bubble algorithm<|end|>
<|assistant|>

```

## **3. 使用 Python 进行 Phi-3 推理**

使用 Phi-3 进行推理是指使用 Phi-3 模型根据输入数据生成预测或输出的过程。Phi-3 模型是一系列小型语言模型（SLM），包括 Phi-3-Mini、Phi-3-Small 和 Phi-3-Medium 等变体，每个变体设计用于不同的应用场景，并具有不同的参数规模。这些模型经过高质量数据的训练，并进行了聊天功能、对齐性、鲁棒性和安全性的微调。它们可以使用 ONNX 和 TensorFlow Lite 部署在边缘和云平台上，符合微软的负责任 AI 原则。

例如，Phi-3-Mini 是一个轻量级、最先进的开源模型，拥有 38 亿参数，适用于使用聊天格式的提示，支持最长 128K 的上下文长度。它是其重量级别中第一个支持如此长上下文的模型。

Phi-3 模型可在 Azure AI MaaS、HuggingFace、NVIDIA、Ollama、ONNX 等平台上使用，适用于实时交互、自动系统和需要低延迟的应用程序。

有很多种方式可以引用 Phi-3。你可以使用不同的编程语言来引用模型。

这里是一个 Python 示例。

```python

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

torch.random.manual_seed(0)

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct", 
    device_map="cuda", 
    torch_dtype="auto", 
    trust_remote_code=True, 
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

messages = [
    {"role": "system", "content": "Your are a python developer."},
    {"role": "user", "content": "Help me generate a bubble algorithm"},
]

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

generation_args = {
    "max_new_tokens": 600,
    "return_full_text": False,
    "temperature": 0.3,
    "do_sample": False,
}

output = pipe(messages, **generation_args)
print(output[0]['generated_text'])


```

> [!NOTE]
> 你可以看看这个结果是否与你想象中的一致

## **4. 使用 C# 进行 Phi-3 推理**

这里是一个 .NET 控制台应用程序的示例。

C# 项目必须添加以下包：

```bash
dotnet add package Microsoft.ML.OnnxRuntime --version 1.18.0
dotnet add package Microsoft.ML.OnnxRuntimeGenAI --version 0.3.0-rc2
dotnet add package Microsoft.ML.OnnxRuntimeGenAI.Cuda --version 0.3.0-rc2
```

这里是 C# 代码。

```csharp
using System;
using Microsoft.ML.OnnxRuntimeGenAI;


// ONNX 模型文件的文件夹位置
var modelPath = @"..\models\Phi-3-mini-4k-instruct-onnx";
var model = new Model(modelPath);
var tokenizer = new Tokenizer(model);

var systemPrompt = "You are an AI assistant that helps people find information. Answer questions using a direct style. Do not share more information that the requested by the users.";

// 聊天开始
Console.WriteLine(@"Ask your question. Type an empty string to Exit.");


// 聊天循环
while (true)
{
    // 获取用户问题
    Console.WriteLine();
    Console.Write(@"Q: ");
    var userQ = Console.ReadLine();    
    if (string.IsNullOrEmpty(userQ))
    {
        break;
    }

    // 显示 phi3 响应
    Console.Write("Phi3: ");
    var fullPrompt = $"<|system|>{systemPrompt}<|end|><|user|>{userQ}<|end|><|assistant|>";
    var tokens = tokenizer.Encode(fullPrompt);

    var generatorParams = new GeneratorParams(model);
    generatorParams.SetSearchOption("max_length", 2048);
    generatorParams.SetSearchOption("past_present_share_buffer", false);
    generatorParams.SetInputSequences(tokens);

    var generator = new Generator(model, generatorParams);
    while (!generator.IsDone())
    {
        generator.ComputeLogits();
        generator.GenerateNextToken();
        var outputTokens = generator.GetSequence(0);
        var newToken = outputTokens.Slice(outputTokens.Length - 1, 1);
        var output = tokenizer.Decode(newToken);
        Console.Write(output);
    }
    Console.WriteLine();
}
```

运行的示例类似于这个：

![Chat running demo](../../../../imgs/02/csharp/20SampleConsole.gif)

***注意：** 第一个问题中有一个拼写错误，Phi-3 足够智能，给出了正确的答案！*

## **5. 在 Hugging Face Chat 中使用 Phi-3**

Hugging Face chat 提供了相关的体验。进入[这里尝试 Phi-3 聊天](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct) 在你的浏览器中体验。

![Hg_Chat](../../../../translated_images/Hg_Chat.6ca1ac61a91bc770f0fb8043586eaf117397de78a5f3c77dac81a6f115c5347c.zh.png)

免责声明：此翻译由AI模型从原文翻译而来，可能并不完美。请审查输出并进行必要的修改。