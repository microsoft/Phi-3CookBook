# VScode용 AI Toolkit (Windows)

[AI Toolkit for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)는 Azure AI Studio Catalog와 Hugging Face와 같은 다른 카탈로그의 최첨단 AI 개발 도구와 모델을 통합하여 생성 AI 앱 개발을 단순화합니다. Azure ML과 Hugging Face에서 제공하는 AI 모델 카탈로그를 탐색하고, 로컬로 다운로드하고, 미세 조정하고, 테스트하며 애플리케이션에서 사용할 수 있습니다.

AI Toolkit Preview는 로컬에서 실행됩니다. 선택한 모델에 따라 일부 작업은 Windows와 Linux에서만 지원됩니다.

로컬 추론이나 미세 조정은 선택한 모델에 따라 NVIDIA CUDA GPU와 같은 GPU가 필요할 수 있습니다.

원격으로 실행하려면 클라우드 리소스에 GPU가 필요하며, 환경을 확인해 주세요. Windows + WSL에서 로컬로 실행하려면, WSL Ubuntu 배포판 18.4 이상이 설치되어 있고 기본값으로 설정되어 있어야 AI Toolkit을 사용할 수 있습니다.

## 시작하기

[Windows용 Linux 서브시스템 설치 방법](https://learn.microsoft.com/windows/wsl/install?WT.mc_id=aiml-137032-kinfeylo)을 알아보세요.

그리고 [기본 배포판 변경](https://learn.microsoft.com/windows/wsl/install#change-the-default-linux-distribution-installed) 방법도 참고하세요.

[AI Tooklit GitHub Repo](https://github.com/microsoft/vscode-ai-toolkit/)

- Windows 또는 Linux
- **MacOS 지원은 곧 제공 예정**
- Windows와 Linux에서 미세 조정을 하려면 Nvidia GPU가 필요합니다. 또한 **Windows**에서는 Ubuntu 배포판 18.4 이상이 포함된 Linux 서브시스템이 필요합니다. [Windows용 Linux 서브시스템 설치 방법](https://learn.microsoft.com/windows/wsl/install)과 [기본 배포판 변경](https://learn.microsoft.com/windows/wsl/install#change-the-default-linux-distribution-installed) 방법을 알아보세요.

### AI Toolkit 설치

AI Toolkit은 [Visual Studio Code Extension](https://code.visualstudio.com/docs/setup/additional-components#_vs-code-extensions)으로 제공되므로, 먼저 [VS Code](https://code.visualstudio.com/docs/setup/windows?WT.mc_id=aiml-137032-kinfeylo)를 설치하고 [VS Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)에서 AI Toolkit을 다운로드해야 합니다.
[AI Toolkit은 Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)에서 제공되며, 다른 VS Code 확장 프로그램처럼 설치할 수 있습니다.

VS Code 확장 프로그램 설치에 익숙하지 않다면 다음 단계를 따르세요:

### 로그인

1. VS Code의 활동 표시줄에서 **확장**을 선택합니다.
2. 확장 검색 창에 "AI Toolkit"을 입력합니다.
3. "AI Toolkit for Visual Studio code"를 선택합니다.
4. **설치**를 선택합니다.

이제 확장을 사용할 준비가 되었습니다!

GitHub에 로그인하라는 메시지가 표시되므로 "허용"을 클릭하여 계속 진행하세요. GitHub 로그인 페이지로 리디렉션됩니다.

로그인하고 절차를 따르세요. 성공적으로 완료되면 VS Code로 리디렉션됩니다.

확장이 설치되면 활동 표시줄에 AI Toolkit 아이콘이 나타납니다.

이제 사용 가능한 작업을 탐색해 봅시다!

### 사용 가능한 작업

AI Toolkit의 주요 사이드바는 다음과 같이 구성되어 있습니다.

- **모델**
- **리소스**
- **플레이그라운드**
- **미세 조정**

리소스 섹션에서 사용할 수 있습니다. 시작하려면 **모델 카탈로그**를 선택하세요.

### 카탈로그에서 모델 다운로드

VS Code 사이드바에서 AI Toolkit을 실행하면 다음 옵션 중에서 선택할 수 있습니다:

![AI toolkit model catalog](../../../../translated_images/AItoolkitmodel_catalog.49200354ddc7aceecdcab2080769d898b1fd50424ef9f7014aafeb790028c49d.ko.png)

- **모델 카탈로그**에서 지원되는 모델을 찾아 로컬로 다운로드
- **모델 플레이그라운드**에서 모델 추론 테스트
- **모델 미세 조정**에서 로컬 또는 원격으로 모델 미세 조정
- AI Toolkit 명령 팔레트를 통해 클라우드에 미세 조정된 모델 배포

> [!NOTE]
>
> **GPU vs CPU**
>
> 모델 카드에는 모델 크기, 플랫폼 및 가속기 유형(CPU, GPU)이 표시됩니다. **GPU가 있는 Windows 장치**에서 최적의 성능을 얻으려면 Windows만을 대상으로 하는 모델 버전을 선택하세요.
>
> 이는 DirectML 가속기에 최적화된 모델을 보유하게 합니다.
>
> 모델 이름 형식은
>
> - `{model_name}-{accelerator}-{quantization}-{format}`입니다.
>
> Windows 장치에 GPU가 있는지 확인하려면 **작업 관리자**를 열고 **성능** 탭을 선택하세요. GPU가 있는 경우 "GPU 0" 또는 "GPU 1"과 같은 이름으로 나열됩니다.

### 플레이그라운드에서 모델 실행

모든 매개 변수가 설정되면 **프로젝트 생성**을 클릭하세요.

모델이 다운로드되면 카탈로그에서 모델 카드의 **플레이그라운드에서 로드**를 선택하세요:

- 모델 다운로드 시작
- 모든 필수 조건 및 종속성 설치
- VS Code 작업 공간 생성

![Load model in playground](../../../../translated_images/AItoolkitload_model_into_playground.f78799b4838c6521be6a296729279525958dec6cfb9a26c64752e397dfe19ef2.ko.png)

모델이 다운로드되면 AI Toolkit에서 프로젝트를 시작할 수 있습니다.

> ***참고*** 원격으로 추론 또는 미세 조정을 시도하려면 [이 가이드](https://aka.ms/previewFinetune)를 따르세요.

### Windows 최적화 모델

모델 응답이 스트리밍되어 표시됩니다:

AI Toolkit은 Windows에 최적화된 공개적으로 사용 가능한 AI 모델 컬렉션을 제공합니다. 모델은 Hugging Face, GitHub 등 다양한 위치에 저장되어 있지만, 한 곳에서 모델을 탐색하고 Windows 애플리케이션에서 사용할 수 있도록 다운로드할 수 있습니다.

![Generation stream](../../../../imgs/04/04/AItoolkitgeneration-gif.gif)

### 모델 선택

*Windows* 장치에 **GPU**가 없지만

- Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx 모델을 선택한 경우

모델 응답이 *매우 느릴* 것입니다.

대신 CPU 최적화 버전을 다운로드해야 합니다:

- Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx.

또한 다음을 변경할 수 있습니다:

**컨텍스트 지침:** 모델이 요청의 큰 그림을 이해하도록 돕습니다. 배경 정보, 예시/데모 또는 작업의 목적을 설명하는 내용이 될 수 있습니다.

**추론 매개 변수:**

- *최대 응답 길이*: 모델이 반환할 최대 토큰 수.
- *온도*: 모델 온도는 언어 모델의 출력이 얼마나 무작위적인지 제어하는 매개 변수입니다. 높은 온도는 모델이 더 많은 위험을 감수하게 하여 다양한 단어를 제공합니다. 반면 낮은 온도는 모델이 안전하게 플레이하여 더 집중되고 예측 가능한 응답을 제공합니다.
- *Top P*: 누클리어스 샘플링이라고도 하며, 언어 모델이 다음 단어를 예측할 때 고려하는 가능한 단어 또는 구문의 수를 제어하는 설정입니다.
- *빈도 페널티*: 모델이 출력에서 단어나 구문을 반복하는 빈도에 영향을 미치는 매개 변수입니다. 값이 높을수록(1.0에 가까울수록) 모델이 단어나 구문을 반복하지 않도록 유도합니다.
- *존재 페널티*: 생성 AI 모델에서 생성된 텍스트의 다양성과 특이성을 장려하기 위해 사용됩니다. 값이 높을수록(1.0에 가까울수록) 모델이 더 새롭고 다양한 토큰을 포함하도록 유도합니다. 낮은 값은 모델이 일반적이거나 상투적인 구문을 생성할 가능성이 더 큽니다.

### 애플리케이션에서 REST API 사용

AI Toolkit은 [OpenAI chat completions format](https://platform.openai.com/docs/api-reference/chat/create)을 사용하는 로컬 REST API 웹 서버 **포트 5272**를 제공합니다.

이를 통해 클라우드 AI 모델 서비스에 의존하지 않고 로컬에서 애플리케이션을 테스트할 수 있습니다. 예를 들어, 다음 JSON 파일은 요청 본문을 구성하는 방법을 보여줍니다:

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

[Postman](https://www.postman.com/) 또는 CURL (Client URL) 유틸리티를 사용하여 REST API를 테스트할 수 있습니다:

```bash
curl -vX POST http://127.0.0.1:5272/v1/chat/completions -H 'Content-Type: application/json' -d @body.json
```

### Python에서 OpenAI 클라이언트 라이브러리 사용

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:5272/v1/", 
    api_key="x" # API에 필요하지만 사용되지 않음
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

### .NET에서 Azure OpenAI 클라이언트 라이브러리 사용

프로젝트에 [Azure OpenAI 클라이언트 라이브러리 for .NET](https://www.nuget.org/packages/Azure.AI.OpenAI/)을 NuGet을 사용하여 추가합니다:

```bash
dotnet add {project_name} package Azure.AI.OpenAI --version 1.0.0-beta.17
```

프로젝트에 **OverridePolicy.cs**라는 C# 파일을 추가하고 다음 코드를 붙여넣습니다:

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

다음으로, **Program.cs** 파일에 다음 코드를 붙여넣습니다:

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

## AI Toolkit으로 미세 조정

- 모델 탐색 및 플레이그라운드 시작
- 로컬 컴퓨팅 리소스를 사용한 모델 미세 조정 및 추론
- Azure 리소스를 사용한 원격 미세 조정 및 추론

[AI Toolkit으로 미세 조정](../04.Fine-tuning/Finetuning_VSCodeaitoolkit.md)

## AI Toolkit Q&A 리소스

가장 일반적인 문제와 해결책에 대해서는 [Q&A 페이지](https://github.com/microsoft/vscode-ai-toolkit/blob/main/QA.md)를 참조하세요.

면책 조항: 이 번역은 원본을 AI 모델에 의해 번역된 것이며 완벽하지 않을 수 있습니다. 
출력을 검토하시고 필요한 수정 사항을 반영해 주시기 바랍니다.