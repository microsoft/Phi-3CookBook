## Phi-3 실험실에 오신 것을 환영합니다 (C# 사용)

.NET 환경에서 강력한 Phi-3 모델의 다양한 버전을 통합하는 방법을 보여주는 여러 실험실이 있습니다.

## 사전 준비 사항
샘플을 실행하기 전에 다음이 설치되어 있는지 확인하세요:

**.NET 8:** [최신 버전의 .NET](https://dotnet.microsoft.com/download/dotnet/8.0?WT.mc_id=aiml-137032-kinfeylo)을 컴퓨터에 설치하세요.

**(선택 사항) Visual Studio 또는 Visual Studio Code:** .NET 프로젝트를 실행할 수 있는 IDE나 코드 편집기가 필요합니다. [Visual Studio](https://visualstudio.microsoft.com/) 또는 [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo)를 추천합니다.

**git 사용하기** [Hugging Face](https://huggingface.co)에서 사용할 수 있는 Phi-3 버전 중 하나를 로컬로 클론하세요.

**phi3-mini-4k-instruct-onnx 모델을** 로컬 컴퓨터에 다운로드하세요:

### 모델을 저장할 폴더로 이동
```bash
cd c:\phi3\models
```
### lfs 지원 추가
```bash
git lfs install 
```
### mini 4K instruct 모델 클론 및 다운로드
```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx
```

### vision 128K 모델 클론 및 다운로드
```
git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```
**중요:** 현재 데모는 모델의 ONNX 버전을 사용하도록 설계되었습니다. 이전 단계에서는 다음 모델들을 클론합니다.

![OnnxDownload](../../../../../translated_images/DownloadOnnx.237f4b37d4d8d66d3f4a4a7219d6004bd6f84bc72cce50251ffc034cb28f6fb8.ko.png)

## 실험실 소개

주요 솔루션에는 C#을 사용하여 Phi-3 모델의 기능을 보여주는 여러 샘플 실험실이 포함되어 있습니다.

| 프로젝트 | 설명 | 위치 |
| ------------ | ----------- | -------- |
| LabsPhi301    | 이 샘플 프로젝트는 로컬 phi3 모델을 사용하여 질문을 합니다. 이 프로젝트는 `Microsoft.ML.OnnxRuntime` libraries. | .\src\LabsPhi301\ |
| LabsPhi302    | This is a sample project that implement a Console chat using Semantic Kernel. | .\src\LabsPhi302\ |
| LabsPhi303 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. | .\src\LabsPhi303\ |
| LabsPhi304 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | .\src\LabsPhi304\ |
| LabsPhi305 | This is a sample project that uses a the Phi-3 hosted in ollama model to answer a question.  |**coming soon**|
| LabsPhi306 | This is a sample project that implement a Console chat using Semantic Kernel. |**coming soon**|
| LabsPhi307  | This is a sample project that implement a RAG using local embeddings and Semantic Kernel. |**coming soon**|


## How to Run the Projects

To run the projects, follow these steps:
1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi301`를 사용하여 로컬 ONNX Phi-3 모델을 로드합니다.
    ```bash
    cd .\src\LabsPhi301\
    ```

1. 다음 명령어로 프로젝트를 실행하세요
    ```bash
    dotnet run
    ```

1. 샘플 프로젝트는 사용자 입력을 요청하고 로컬 모드를 사용하여 응답합니다.

    실행 중인 데모는 다음과 유사합니다:

    ![Chat running demo](../../../../../imgs/07/00/SampleConsole.gif)

    ***참고:** 첫 번째 질문에 오타가 있지만, Phi-3는 정확한 답변을 제공할 만큼 충분히 똑똑합니다!*

1. 프로젝트 `LabsPhi304`는 사용자가 다른 옵션을 선택하도록 요청한 다음 요청을 처리합니다. 예를 들어, 로컬 이미지를 분석하는 것입니다.

    실행 중인 데모는 다음과 유사합니다:

    ![Image Analysis running demo](../../../../../imgs/07/00/SampleVisionConsole.gif)

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 우리는 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원어로 작성된 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문 인간 번역을 권장합니다. 이 번역 사용으로 인한 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.