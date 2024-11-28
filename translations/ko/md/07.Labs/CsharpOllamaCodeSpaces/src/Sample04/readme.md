# Phi-3, SemanticKernel, TextMemory를 사용한 완전한 로컬 RAG 시나리오

## 소개

Phi-3, SemanticKernel, TextMemory를 사용한 완전한 로컬 RAG 시나리오에 오신 것을 환영합니다. 이 프로젝트는 개발자와 비즈니스를 위한 AI 기능을 재정의하는 획기적인 소형 언어 모델(SLM)인 Phi-3의 강력함을 보여줍니다.

## 시나리오 개요

이 데모 시나리오는 "브루노가 가장 좋아하는 슈퍼 히어로는 누구인가?"라는 질문에 두 가지 다른 접근 방식으로 답변하는 것을 목표로 합니다:

1. Phi-3 모델에 직접 질문하기.
2. 팬 사실이 로드된 의미 메모리 객체를 추가하고 질문하기.

## 완전한 시나리오의 중요성

Phi-3는 소형 언어 모델에서 중요한 도약을 나타내며, 성능과 효율성을 독특하게 결합합니다. 독립적으로 전체 시나리오를 처리할 수 있어 개발 과정을 단순화하고 통합 복잡성을 줄입니다.

## 코드 설명

콘솔 애플리케이션은 Ollama에 호스팅된 로컬 모델과 검색을 위한 의미 메모리 사용을 보여줍니다. 이 프로그램은 의존성 주입, 구성, 의미 커널 및 메모리 기능을 위한 여러 외부 라이브러리를 사용합니다.

## 테스트 방법

1. 터미널을 열고 현재 프로젝트로 이동합니다.

    ```bash
    cd .\src\Sample03\
    ```

1. 다음 명령어로 프로젝트를 실행합니다.

    ```bash
    dotnet run
    ```

1. `Sample03` 프로젝트에서 다음 질문에 답하십시오:

    ```csharp
    var question = "What is Bruno's favourite super hero?"
    ```

1. 먼저 Phi-3 모델에 직접 질문합니다. 그런 다음 프로그램은 다음 정보를 텍스트 메모리에 로드하고 다시 질문합니다.

    ```csharp

    // get the embeddings generator service
    var embeddingGenerator = kernel.Services.GetRequiredService<ITextEmbeddingGenerationService>();
    var memory = new SemanticTextMemory(new VolatileMemoryStore(), embeddingGenerator);    

    // add facts to the collection
    const string MemoryCollectionName = "fanFacts";
    
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info1", 
            text: "Gisela's favourite super hero is Batman");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info2", 
            text: "The last super hero movie watched by Gisela was Guardians of the Galaxy Vol 3");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info3", 
            text: "Bruno's favourite super hero is Invincible");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info4", 
            text: "The last super hero movie watched by Bruno was Aquaman II");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info5", 
            text: "Bruno don't like the super hero movie: Eternals");    
    ```

1. 텍스트 메모리가 준비되면, 이를 플러그인으로 커널에 로드합니다.

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // Import the text memory plugin into the Kernel.
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

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하지만 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원어로 작성된 원본 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 오역에 대해서는 책임지지 않습니다.