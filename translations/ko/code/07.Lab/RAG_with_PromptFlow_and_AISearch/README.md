## PromptFlow와 AISearch를 활용한 RAG

이 예제에서는 Phi3를 SLM으로, AI Search를 vectorDB로, Prompt Flow를 저코드 오케스트레이터로 활용하여 Retrieval Augmented Generation (RAG) 애플리케이션을 구현할 것입니다.

## 특징

- Docker를 이용한 간편한 배포.
- AI 워크플로우를 처리할 수 있는 확장 가능한 아키텍처.
- Prompt Flow를 이용한 저코드 접근 방식.

## 사전 준비 사항

시작하기 전에 다음 요구 사항을 충족했는지 확인하세요:

- 로컬 머신에 Docker가 설치되어 있어야 합니다.
- 컨테이너 리소스를 생성하고 관리할 수 있는 권한이 있는 Azure 계정이 필요합니다.
- Azure AI Studio와 Azure AI Search 인스턴스가 필요합니다.
- 인덱스를 생성할 임베딩 모델이 필요합니다 (Azure OpenAI 임베딩 또는 카탈로그에서 제공하는 OS 모델 중 하나).
- 로컬 머신에 Python 3.8 이상이 설치되어 있어야 합니다.
- Azure Container Registry (또는 선택한 다른 레지스트리).

## 설치

1. flow.yaml 파일을 사용하여 Azure AI Studio 프로젝트에서 새 플로우를 만듭니다.
2. Azure AI 모델 카탈로그에서 Phi3 모델을 배포하고 프로젝트에 연결을 만듭니다. [Phi-3를 모델로 배포하기](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 원하는 문서를 사용하여 Azure AI Search에서 벡터 인덱스를 만듭니다. [Azure AI Search에서 벡터 인덱스 만들기](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 관리형 엔드포인트에 플로우를 배포하고 이를 prompt-flow-frontend.py 파일에서 사용합니다. [온라인 엔드포인트에 플로우 배포하기](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. 저장소를 클론합니다:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker 이미지를 빌드합니다:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker 이미지를 Azure Container Registry에 푸시합니다:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## 사용법

1. Docker 컨테이너를 실행합니다:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. 브라우저에서 `http://localhost:8501`에 접속하여 애플리케이션을 사용합니다.

## 연락처

발렌티나 알토 - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

전체 글: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

면책 조항: 이 번역은 AI 모델에 의해 원본에서 번역되었으며 완벽하지 않을 수 있습니다. 
출력을 검토하고 필요한 수정 사항을 반영해 주시기 바랍니다.