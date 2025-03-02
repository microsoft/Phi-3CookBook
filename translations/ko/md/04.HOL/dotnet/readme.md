## Phi Labs에 오신 것을 환영합니다 (C# 사용)

.NET 환경에서 강력한 Phi 모델의 다양한 버전을 통합하는 방법을 보여주는 여러 실습이 준비되어 있습니다.

## 사전 요구사항

샘플을 실행하기 전에 아래 항목들이 설치되어 있는지 확인하세요:

**.NET 9:** [최신 .NET 버전](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo)이 컴퓨터에 설치되어 있는지 확인하세요.

**(선택 사항) Visual Studio 또는 Visual Studio Code:** .NET 프로젝트를 실행할 수 있는 IDE 또는 코드 편집기가 필요합니다. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) 또는 [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo)를 추천합니다.

**git 사용하기** [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c)에서 제공되는 Phi-3, Phi-3.5 또는 Phi-4 버전 중 하나를 로컬로 클론하세요.

**Phi-4 ONNX 모델 다운로드**를 로컬 컴퓨터에 저장하세요:

### 모델을 저장할 폴더로 이동

```bash
cd c:\phi\models
```

### lfs 지원 추가

```bash
git lfs install 
```

### Phi-4 mini instruct 모델과 Phi-4 multi modal 모델 클론 및 다운로드

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX 모델 다운로드**를 로컬 컴퓨터에 저장하세요:

### Phi-3 mini 4K instruct 모델과 Phi-3 vision 128K 모델 클론 및 다운로드

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**중요:** 현재 데모는 ONNX 버전의 모델 사용을 위해 설계되었습니다. 위 단계에서는 다음 모델들을 클론합니다.

## 실습에 대하여

메인 솔루션에는 C#을 사용하여 Phi 모델의 기능을 시연하는 여러 샘플 실습이 포함되어 있습니다.

| 프로젝트 | 모델 | 설명 |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 또는 Phi-3.5 | 사용자가 질문을 할 수 있는 샘플 콘솔 채팅. 프로젝트는 `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`를 사용하여 로컬 ONNX Phi-3 모델을 로드합니다.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. 다음 명령으로 프로젝트를 실행합니다:

    ```bash
    dotnet run
    ```

1. 샘플 프로젝트는 사용자 입력을 요청하고 로컬 모드를 사용하여 응답합니다.

   실행 중인 데모는 아래와 유사합니다:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**면책 조항**:  
이 문서는 AI 기반 기계 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문이 작성된 언어의 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문 번역가에 의한 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.