# Phi-3, SemanticKernel, TextMemory를 활용한 완전한 로컬 RAG 시나리오

## 소개

Phi-3, SemanticKernel, TextMemory를 활용한 완전한 로컬 RAG 시나리오에 오신 것을 환영합니다. 이 프로젝트는 개발자와 비즈니스를 위해 AI 기능을 재정의하는 혁신적인 소형 언어 모델(SLM)인 Phi-3의 강력함을 보여줍니다.

## 시나리오 개요

이 데모 시나리오는 "브루노가 가장 좋아하는 슈퍼 히어로는 누구인가요?"라는 질문에 두 가지 방법으로 답변하는 것을 목표로 합니다:

1. Phi-3 모델에 직접 질문하기.
2. 팬 사실이 로드된 시맨틱 메모리 객체를 추가한 후 질문하기.

## 전체 시나리오의 중요성

Phi-3는 소형 언어 모델에서 중요한 도약을 나타내며, 성능과 효율성을 독특하게 결합합니다. Phi-3는 독립적으로 전체 시나리오를 처리할 수 있어 개발 과정을 단순화하고 통합 복잡성을 줄여줍니다.

## 코드 설명

이 콘솔 애플리케이션은 Ollama에 호스팅된 로컬 모델과 검색을 위한 시맨틱 메모리의 사용을 보여줍니다. 이 프로그램은 의존성 주입, 구성, 시맨틱 커널 및 메모리 기능을 위해 여러 외부 라이브러리를 사용합니다.

## 테스트 방법

1. 터미널을 열고 현재 프로젝트로 이동합니다.

    ```bash
    cd .\src\Sample03\
    ```

1. 다음 명령어로 프로젝트를 실행합니다.

    ```bash
    dotnet run
    ```

1. 프로젝트 `Sample03`에서 다음 질문에 답하세요:

    ```csharp
    var question = "What is Bruno's favourite super hero?"
    ```

1. 먼저 질문을 Phi-3 모델에 직접 묻습니다. 그런 다음 프로그램은 텍스트 메모리에 다음 정보를 로드하고 다시 질문합니다.

    ```csharp

    // 임베딩 생성 서비스 가져오기
    var embeddingGenerator = kernel.Services.GetRequiredService<ITextEmbeddingGenerationService>();
    var memory = new SemanticTextMemory(new VolatileMemoryStore(), embeddingGenerator);    

    // 컬렉션에 사실 추가
    const string MemoryCollectionName = "fanFacts";
    
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info1", 
            text: "Gisela의 가장 좋아하는 슈퍼 히어로는 배트맨입니다");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info2", 
            text: "Gisela가 마지막으로 본 슈퍼 히어로 영화는 가디언즈 오브 갤럭시 Vol 3입니다");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info3", 
            text: "Bruno의 가장 좋아하는 슈퍼 히어로는 인빈서블입니다");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info4", 
            text: "Bruno가 마지막으로 본 슈퍼 히어로 영화는 아쿠아맨 II입니다");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info5", 
            text: "Bruno는 이터널스라는 슈퍼 히어로 영화를 좋아하지 않습니다");    
    ```

1. 텍스트 메모리가 준비되면 커널에 플러그인으로 로드됩니다.

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // 텍스트 메모리 플러그인을 커널에 가져오기.
    kernel.ImportPluginFromObject(memoryPlugin);    
    ```

1. 다음은 Codespace에서 실행 중인 데모 콘솔 애플리케이션입니다:

    ![Codespace에서 실행 중인 데모 콘솔 애플리케이션](../../../../../../../md/07.Labs/CsharpOllamaCodeSpaces/src/Sample03/img/10RAGPhi3.gif)

## 참고 자료

- [Phi-3 Microsoft Blog](https://aka.ms/phi3blog-april)
- [Phi-3 Technical Report](https://aka.ms/phi3-tech-report)
- [Phi-3 Cookbook](https://aka.ms/Phi-3CookBook)
- [Generative AI for beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Semantic Kernel main repository](https://github.com/microsoft/semantic-kernel)
- [Smart Components - Local Embeddings](https://github.com/dotnet-smartcomponents/smartcomponents/blob/main/docs/local-embeddings.md)

