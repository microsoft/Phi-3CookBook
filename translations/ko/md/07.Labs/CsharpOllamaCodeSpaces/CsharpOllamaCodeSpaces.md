# Ollama C# 플레이그라운드

이 실습은 누구나 브라우저에서 SLM(소형 언어 모델)을 쉽게 사용해 볼 수 있도록 GitHub Codespaces에서 직접 C# 샘플로 Phi-3을 테스트할 수 있게 설계되었습니다.

## C# + Ollama + Phi-3 Codespace 생성 방법

1. 저장소 상단의 `Code` 버튼을 사용하여 새 Codespace를 생성하세요. [+ New with options ...]을 선택하세요.
![옵션으로 Codespace 생성](../../../../../translated_images/10NewCodespacesWithOptions.b50796422fc7f6d13721a50b72de8b62d83a7951fdace787a0dc12edc22ce807.ko.png)

1. 옵션 페이지에서 `Ollama with Phi-3 for C#`라는 구성을 선택하세요.

![C#용 Ollama와 Phi-3 옵션 선택하여 Codespace 생성](../../../../../translated_images/12NewCSOllamaCodespace.38aab1c942efe444653b4141918ce6d081ce6e9638e0d16117f5b93ce1deee42.ko.png)

1. Codespace가 로드되면 [ollama](https://ollama.com/)가 사전 설치되어 있고, 최신 Phi-3 모델이 다운로드되며, [.NET 8](https://dotnet.microsoft.com/download)이 설치되어 있어야 합니다.

1. (선택 사항) Codespace 터미널을 사용하여 Ollama에게 [phi3](https://ollama.com/library/phi3) 모델을 실행하도록 요청하세요:

    ```shell
    ollama run phi3
    ```

4. 프롬프트에서 해당 모델에 메시지를 보낼 수 있습니다.

    ```shell
    >>> Write a joke about kittens
    ```

5. 몇 초 후에 모델로부터 응답 스트림을 볼 수 있을 것입니다.

    ![ollama 실행 후 농담 요청](../../../../../md/07.Labs/CsharpOllamaCodeSpaces/20ollamarunphi.gif)

1. 언어 모델에서 사용되는 다양한 기술에 대해 알아보려면 `.\src` folder:

| Project | Description |
|---------|-------------|
| Sample01  | This is a sample project that uses a the Phi-3 hosted in ollama model to answer a question.  |
| Sample02  | This is a sample project that implement a Console chat using Semantic Kernel. |
| [Sample03](./src/Sample03/readme.md)  | This is a sample project that implement a RAG using local embeddings and Semantic Kernel. Check the details of the local RAG [here](./src/Sample03/readme.md) |

## How to run a sample

1. Open a terminal and navigate to the desired project. In example, let's run `Sample02`의 샘플 프로젝트를 확인하세요. 이는 콘솔 채팅입니다.

    ```bash
    cd .\src\Sample02\
    ```

1. 다음 명령어로 프로젝트를 실행하세요.

    ```bash
    dotnet run
    ```

1. `Sample02` 프로젝트는 사용자 정의 시스템 메시지를 정의합니다:

    ```csharp
    var history = new ChatHistory();
    history.AddSystemMessage("You are a useful chatbot. If you don't know an answer, say 'I don't know!'. Always reply in a funny ways. Use emojis if possible.");

    ```

1. 사용자가 `이탈리아의 수도는 무엇인가요?`와 같은 질문을 하면, 채팅은 로컬 모드를 사용하여 응답합니다.
   
    출력은 다음과 유사합니다:

    ![채팅 실행 데모](../../../../../translated_images/20SampleConsole.22997336ed0fa683bcc3238bb8e953b3a533d28196bc42e7cd1527261dd0689b.ko.png)

## 비디오 튜토리얼

GitHub Repository에서 Ollama와 Codespaces를 사용하는 방법에 대해 더 알고 싶다면, 아래의 3분짜리 비디오를 확인하세요:

[![비디오 시청](../../../../../translated_images/40ytintro.09cf17cbf9dd4cf8faa91668c42172417f86851025ef325454ce65903606bb9e.ko.jpg)](https://youtu.be/HmKpHErUEHM)

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문 인간 번역을 권장합니다. 이 번역 사용으로 인한 오해나 오역에 대해 당사는 책임을 지지 않습니다.