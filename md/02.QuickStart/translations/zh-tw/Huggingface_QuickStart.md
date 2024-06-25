# **在 Hugging Face 中使用 Phi-3**

[Hugging Face](https://huggingface.co/) 是一個非常受歡迎的 AI 社群，擁有豐富的資料和開源模型資源。不同的廠商會通過 Hugging Face 發佈開源的 LLM 和 SLM，例如 Microsoft、Meta、Mistral、Apple、Google 等等。

![Phi3](../../../../imgs/02/Huggingface/Hg_Phi3.png)

Microsoft Phi-3 已經在 Hugging Face 上發布。開發人員可以根據場景和業務下載相應的 Phi-3 模型。在 Hugging Face 部署 Phi-3 Pytorch 模型的同時，我們還發布了量化模型，使用 GGUF 和 ONNX 格式給最終用戶選擇。

## **1. 從 Hugging Face 下載 Phi-3**

```bash

git lfs install

git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

```

## **2. 了解 Phi-3 Prompt Template**

在訓練 Phi-3 時有一個特定的資料範本，因此在使用 Phi-3 時，發送 Prompt 需要通過範本來設定。在微調過程中，資料也需要根據範本進行擴展。

範本有三個角色，包括系統、使用者和助手。

```txt

<|system|>
你的角色<|end|>
<|user|>
你的問題？<|end|>
<|assistant|>

```

例如

```txt

<|system|>
你是一名 Python 開發者。<|end|>
<|user|>
幫我生成一個冒泡排序算法<|end|>
<|assistant|>

```
```

## **3. 使用 Python 進行 Phi-3 推論**

使用 Phi-3 進行推論是指使用 Phi-3 模型根據輸入數據生成預測或輸出。Phi-3 模型是一系列小型語言模型（SLMs），包括 Phi-3-Mini、Phi-3-Small 和 Phi-3-Medium 等變體，每個變體針對不同的應用場景並具有不同的參數大小。這些模型已經在高品質數據上進行訓練，並針對聊天功能、對齊、穩健性和安全性進行了微調。它們可以使用 ONNX 和 TensorFlow Lite 部署在邊緣和雲端平台上，並根據微軟的負責任 AI 原則進行開發。

例如，Phi-3-Mini 是一個輕量級、先進的開放模型，擁有 38 億個參數，適用於使用聊天格式的提示，並支持長達 128K 個 tokens 的上下文長度。這是其重量級別中首個支持如此長上下文的模型。

Phi-3 模型可在 Azure AI MaaS、HuggingFace、NVIDIA、Ollama、ONNX 等平台上使用，並可用於各種應用，包括即時互動、自主系統和需要低延遲的應用程式。

有很多方法可以參考 Phi-3。你可以使用不同的程式語言來參考該模型。

這是一個 Python 的範例。

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
    {"role": "user", "content": "幫我生成一個氣泡排序演算法"},
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

*你可以查看這個結果是否與你心中的結果一致*

## **4. 使用 C# 推論 Phi-3**

這是一個 .NET Console 應用程式中的範例。

C# 專案必須新增以下套件:

```
dotnet add package Microsoft.ML.OnnxRuntime --version 1.18.0
dotnet add package Microsoft.ML.OnnxRuntimeGenAI --version 0.3.0-rc2
dotnet add package Microsoft.ML.OnnxRuntimeGenAI.Cuda --version 0.3.0-rc2
```

以下是 C# 程式碼。

```csharp
using System;
using Microsoft.ML.OnnxRuntimeGenAI;


// ONNX 模型檔案的資料夾位置
var modelPath = @"..\models\Phi-3-mini-4k-instruct-onnx";
var model = new Model(modelPath);
var tokenizer = new Tokenizer(model);

var systemPrompt = "You are an AI assistant that helps people find information. Answer questions using a direct style. Do not share more information that the requested by the users.";

// 聊天開始
Console.WriteLine(@"Ask your question. Type an empty string to Exit.");


// 聊天迴圈
while (true)
{
    // 獲取使用者問題
    Console.WriteLine();
    Console.Write(@"Q: ");
    var userQ = Console.ReadLine();
    if (string.IsNullOrEmpty(userQ))
    {
        break;
    }

    // 顯示 phi3 回應
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

執行展示與此類似:

![Chat running demo](../../../../imgs/02/csharp/20SampleConsole.gif)

***注意:** 第一個問題有一個錯字，Phi-3 很酷，願意分享正確答案！*

## **5. 在 Hugging Face Chat 中使用 Phi-3**

Hugging Face 聊天提供相關體驗。輸入 https://aka.ms/try-phi3-hf-chat 在您的瀏覽器中體驗它。

![Hg_Chat](../../../../imgs/02/Huggingface/Hg_Chat.png)

