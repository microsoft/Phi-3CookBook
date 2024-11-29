# **Hugging Face에서 Phi-3 사용하기**

[Hugging Face](https://huggingface.co/)는 풍부한 데이터와 오픈 소스 모델 리소스를 갖춘 매우 인기 있는 AI 커뮤니티입니다. 다양한 제조업체들이 Microsoft, Meta, Mistral, Apple, Google 등과 같은 LLM 및 SLM을 Hugging Face를 통해 공개합니다.

![Phi3](../../../../translated_images/Hg_Phi3.dc94956455e775c886b69f7430a05b7a42aab729a81fa4083c906812edb475f8.ko.png)

Microsoft Phi-3가 Hugging Face에 출시되었습니다. 개발자들은 시나리오와 비즈니스에 따라 해당 Phi-3 모델을 다운로드할 수 있습니다. Hugging Face에서 Phi-3 Pytorch 모델을 배포하는 것 외에도, 최종 사용자에게 선택의 폭을 넓혀주기 위해 GGUF 및 ONNX 형식의 양자화된 모델도 출시했습니다.


## **1. Hugging Face에서 Phi-3 다운로드하기**

```bash

git lfs install 

git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

```

## **2. Phi-3 프롬프트 템플릿 알아보기**

Phi-3를 훈련할 때 특정 데이터 템플릿이 있습니다. 따라서 Phi-3를 사용할 때 프롬프트를 보낼 때 템플릿을 통해 설정해야 합니다. 파인튜닝 시에도 데이터는 템플릿에 따라 확장되어야 합니다.

템플릿에는 시스템, 사용자, 그리고 어시스턴트 세 가지 역할이 있습니다.

```txt

<|system|>
Your Role<|end|>
<|user|>
Your Question?<|end|>
<|assistant|>

```

예를 들어

```txt

<|system|>
Your are a python developer.<|end|>
<|user|>
Help me generate a bubble algorithm<|end|>
<|assistant|>

```

## **3. Python으로 Phi-3 추론하기**

Phi-3 추론은 입력 데이터에 기반하여 Phi-3 모델을 사용해 예측이나 출력을 생성하는 과정을 말합니다. Phi-3 모델은 Phi-3-Mini, Phi-3-Small, Phi-3-Medium과 같은 변형을 포함하는 소형 언어 모델(SLM) 계열로, 각각 다른 응용 시나리오와 다양한 매개변수 크기에 맞게 설계되었습니다. 이 모델들은 고품질 데이터로 훈련되었으며, 채팅 기능, 정렬, 견고성 및 안전성을 위해 파인튜닝되었습니다. 이들은 ONNX와 TensorFlow Lite를 사용하여 엣지 및 클라우드 플랫폼에 배포될 수 있으며, Microsoft의 책임 있는 AI 원칙에 따라 개발되었습니다.

예를 들어, Phi-3-Mini는 38억 개의 매개변수를 가진 경량의 최신 오픈 모델로, 채팅 형식의 프롬프트에 적합하며 최대 128K 토큰의 컨텍스트 길이를 지원합니다. 이 무게 클래스에서 처음으로 이렇게 긴 컨텍스트를 지원하는 모델입니다.

Phi-3 모델은 Azure AI MaaS, HuggingFace, NVIDIA, Ollama, ONNX 등의 플랫폼에서 제공되며, 실시간 상호작용, 자율 시스템 및 저지연 응용 프로그램을 포함한 다양한 응용 프로그램에 사용할 수 있습니다.

Phi-3를 참조하는 방법은 여러 가지가 있습니다. 다양한 프로그래밍 언어를 사용하여 모델을 참조할 수 있습니다.

여기 Python 예제가 있습니다.

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
> 이 결과가 여러분의 생각과 일치하는지 확인해보세요

## **4. C#으로 Phi-3 추론하기**

여기 .NET 콘솔 애플리케이션 예제가 있습니다.

C# 프로젝트에는 다음 패키지를 추가해야 합니다:

```bash
dotnet add package Microsoft.ML.OnnxRuntime --version 1.18.0
dotnet add package Microsoft.ML.OnnxRuntimeGenAI --version 0.3.0-rc2
dotnet add package Microsoft.ML.OnnxRuntimeGenAI.Cuda --version 0.3.0-rc2
```

여기 C# 코드입니다.

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

실행 데모는 다음과 비슷합니다:

![Chat running demo](../../../../imgs/02/csharp/20SampleConsole.gif)

***Note:** 첫 번째 질문에 오타가 있지만, Phi-3는 올바른 답을 공유할 만큼 충분히 멋집니다!*

## **5. Hugging Face Chat에서 Phi-3 사용하기**

Hugging Face 채팅은 관련 경험을 제공합니다. 브라우저에서 [여기에서 Phi-3 채팅 시도](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)를 통해 경험해보세요.

![Hg_Chat](../../../../translated_images/Hg_Chat.6ca1ac61a91bc770f0fb8043586eaf117397de78a5f3c77dac81a6f115c5347c.ko.png)

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하지만 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.