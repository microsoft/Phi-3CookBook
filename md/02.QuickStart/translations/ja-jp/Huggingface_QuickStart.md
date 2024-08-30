# **Hugging FaceでPhi-3を使用する**

[Hugging Face](https://huggingface.co/)は、豊富なデータとオープンソースモデルリソースを持つ非常に人気のあるAIコミュニティです。Microsoft、Meta、Mistral、Apple、Googleなどのさまざまなメーカーが、Hugging Faceを通じてオープンソースのLLMおよびSLMをリリースしています。

![Phi3](../../../../imgs/02/Huggingface/Hg_Phi3.png)

Microsoft Phi-3はHugging Faceでリリースされています。開発者は、シナリオやビジネスに基づいて対応するPhi-3モデルをダウンロードできます。Hugging FaceでPhi-3 Pytorchモデルをデプロイするだけでなく、GGUFおよびONNX形式を使用して量子化モデルもリリースし、エンドユーザーに選択肢を提供しています。

## **1. Hugging FaceからPhi-3をダウンロードする**

```bash

git lfs install 

git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

```

## **2. Phi-3プロンプトテンプレートを理解する**

Phi-3をトレーニングする際には特定のデータテンプレートがあります。そのため、Phi-3を使用する際には、テンプレートを通じてプロンプトを設定する必要があります。ファインチューニング中には、データもテンプレートに基づいて拡張する必要があります。

テンプレートには、システム、ユーザー、アシスタントの3つの役割があります。

```txt

<|system|>
Your Role<|end|>
<|user|>
Your Question?<|end|>
<|assistant|>

```

例えば

```txt

<|system|>
Your are a python developer.<|end|>
<|user|>
Help me generate a bubble algorithm<|end|>
<|assistant|>

```

## **3. PythonでPhi-3を推論する**

Phi-3を使用した推論とは、Phi-3モデルを使用して入力データに基づいて予測や出力を生成するプロセスを指します。Phi-3モデルは、小型言語モデル（SLM）のファミリーであり、Phi-3-Mini、Phi-3-Small、Phi-3-Mediumなどのバリアントが含まれています。これらのモデルは、さまざまなアプリケーションシナリオに対応するために異なるパラメータサイズで設計されています。これらのモデルは高品質なデータでトレーニングされており、チャット機能、整合性、堅牢性、安全性のためにファインチューニングされています。これらのモデルは、ONNXおよびTensorFlow Liteを使用してエッジおよびクラウドプラットフォームにデプロイできます。

例えば、Phi-3-Miniは3.8Bパラメータの軽量で最先端のオープンモデルであり、チャット形式を使用したプロンプトに適しており、最大128Kトークンのコンテキスト長をサポートします。これは、その重量クラスで最初にそのような長いコンテキストをサポートするモデルです。

Phi-3モデルは、Azure AI MaaS、HuggingFace、NVIDIA、Ollama、ONNXなどのプラットフォームで利用可能であり、リアルタイムの対話、自律システム、低遅延を必要とするアプリケーションなど、さまざまなアプリケーションに使用できます。

Phi-3を参照する方法は多数あります。さまざまなプログラミング言語を使用してモデルを参照できます。

以下はPythonの例です。

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
> この結果があなたの考えと一致するかどうかを確認してください

## **4. C#でPhi-3を推論する**

以下は.NETコンソールアプリケーションの例です。

C#プロジェクトには、次のパッケージを追加する必要があります。

```bash
dotnet add package Microsoft.ML.OnnxRuntime --version 1.18.0
dotnet add package Microsoft.ML.OnnxRuntimeGenAI --version 0.3.0-rc2
dotnet add package Microsoft.ML.OnnxRuntimeGenAI.Cuda --version 0.3.0-rc2
```

以下はC#コードです。

```csharp
using System;
using Microsoft.ML.OnnxRuntimeGenAI;


// ONNXモデルファイルのフォルダ位置
var modelPath = @"..\models\Phi-3-mini-4k-instruct-onnx";
var model = new Model(modelPath);
var tokenizer = new Tokenizer(model);

var systemPrompt = "You are an AI assistant that helps people find information. Answer questions using a direct style. Do not share more information that the requested by the users.";

// チャット開始
Console.WriteLine(@"Ask your question. Type an empty string to Exit.");


// チャットループ
while (true)
{
    // ユーザーの質問を取得
    Console.WriteLine();
    Console.Write(@"Q: ");
    var userQ = Console.ReadLine();
    if (string.IsNullOrEmpty(userQ))
    {
        break;
    }

    // phi3の応答を表示
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

実行デモは次のようになります。

![Chat running demo](../../../../imgs/02/csharp/20SampleConsole.gif)

***注意:** 最初の質問に誤字がありますが、Phi-3は十分に優れており、正しい答えを共有しています！*

## **5. Hugging Face ChatでPhi-3を使用する**

Hugging Faceチャットは関連する体験を提供します。Phi-3チャットを体験するには、[こちら](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)をクリックしてください。

![Hg_Chat](../../../../imgs/02/Huggingface/Hg_Chat.png)
