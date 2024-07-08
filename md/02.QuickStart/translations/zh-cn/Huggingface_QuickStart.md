# **在 Hugging Face 中使用 Phi-3**

[Hugging Face](https://huggingface.co/) 是一个非常受欢迎的AI社区，拥有丰富的数据和开源模型资源。不同的制造商会通过Hugging Face发布开源的LLM（大型语言模型）和SLM（小型语言模型），例如微软、Meta、Mistral、苹果、谷歌等。

![Phi3](../../../../imgs/02/Huggingface/Hg_Phi3.png)

微软已在Hugging Face上发布了Phi-3模型。开发者可以根据场景和业务需求下载相应的Phi-3模型。除了在Hugging Face上部署Phi-3的Pytorch模型外，我们还发布了量化模型，使用GGUF和ONNX格式，以便为最终用户提供选择。


## **1.从 Hugging Face 下载 Phi-3**

```bash

git lfs install 

git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

```

## **2.了解 Phi-3 提示模板**

在训练Phi-3时有一个特定的数据模板，因此在使用Phi-3时，需要通过模板设置发送的提示词。在微调过程中，数据也需要根据模板进行扩展。

模板具有三个角色，包括系统、用户和助手。


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


## **3.利用 Python 来进行 Phi-3 推理**

使用Phi-3进行推理是指：利用Phi-3模型根据输入数据生成预测或输出的过程。Phi-3模型是一系列小型语言模型（SLM），包括Phi-3-Mini、Phi-3-Small和Phi-3-Medium等变体，每种变体都针对不同的应用场景和参数大小进行设计。这些模型经过高质量数据的训练，并针对聊天能力、对齐、稳健性和安全性进行了微调。它们可以使用ONNX和TensorFlow Lite在边缘和云平台上部署，并根据微软的负责任AI原则进行开发。

例如，Phi-3-Mini是一款轻量级的先进开放模型，拥有38亿个参数，适用于使用聊天格式的提示，并支持最多128K个令牌的上下文长度。它是第一个支持如此长上下文的同类重量级模型。

Phi-3模型可在Azure AI MaaS、HuggingFace、NVIDIA、Ollama、ONNX等平台上使用，可用于实时互动、自主系统和需要低延迟的应用程序等多种应用。

有许多方法可以引用Phi-3。您可以使用不同的编程语言来引用模型。

以下是一个Python示例。


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

*请您查看此结果是否与您心中的预期结果一致。*

## **4.利用 C# 进行 Phi-3 推理**

在一个.NET控制台应用程序中，您可以使用以下示例。

C#项目必须添加以下程序包：

```
dotnet add package Microsoft.ML.OnnxRuntime --version 1.18.0
dotnet add package Microsoft.ML.OnnxRuntimeGenAI --version 0.3.0-rc2
dotnet add package Microsoft.ML.OnnxRuntimeGenAI.Cuda --version 0.3.0-rc2
```

C#代码如下：

```csharp
using System;
using Microsoft.ML.OnnxRuntimeGenAI;


// folder location of the ONNX model file
var modelPath = @"..\models\Phi-3-mini-4k-instruct-onnx";
var model = new Model(modelPath);
var tokenizer = new Tokenizer(model);

var systemPrompt = "You are an AI assistant that helps people find information. Answer questions using a direct style. Do not share more information that the requested by the users.";

// chat start
Console.WriteLine(@"Ask your question. Type an empty string to Exit.");


// chat loop
while (true)
{
    // Get user question
    Console.WriteLine();
    Console.Write(@"Q: ");
    var userQ = Console.ReadLine();    
    if (string.IsNullOrEmpty(userQ))
    {
        break;
    }

    // show phi3 response
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

运行的演示与此类似:

![Chat running demo](../../../../imgs/02/csharp/20SampleConsole.gif)

***注意:** 第一个问题中有一个拼写错误，但Phi-3足够优秀，仍然给出了正确答案！*



## **5.在 Hugging Face Chat 中使用 Phi-3**

Hugging Face聊天提供了相关体验。在浏览器中输入https://aka.ms/try-phi3-hf-chat以体验。

![Hg_Chat](../../../../imgs/02/Huggingface/Hg_Chat.png)
