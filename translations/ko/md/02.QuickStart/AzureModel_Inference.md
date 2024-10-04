# Azure AI 모델 추론

[Azure AI 모델 추론은 API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo)로, 기본 모델을 위한 공통 기능 세트를 제공하며 개발자가 다양한 모델의 예측을 일관되게 소비할 수 있도록 합니다. 개발자는 Azure AI Studio에 배포된 다양한 모델과 상호작용할 수 있으며, 사용하는 기본 코드를 변경할 필요가 없습니다.

마이크로소프트는 이제 [MaaS/MaaP](https://azure.microsoft.com/products/ai-model-catalog?WT.mc_id=aiml-138114-kinfeylo)에 호스팅된 다양한 모델에 대한 AI 모델 추론을 위한 자체 SDK를 제공합니다.

Python과 JS 버전이 출시되었으며, C# 버전은 곧 출시될 예정입니다.

[Python](https://learn.microsoft.com/python/api/overview/azure/ai-inference-readme?view=azure-python-preview?WT.mc_id=aiml-138114-kinfeylo) [샘플](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples?WT.mc_id=aiml-138114-kinfeylo)

[JavaScript](https://learn.microsoft.com/javascript/api/overview/azure/ai-inference-rest-readme?view=azure-node-preview?WT.mc_id=aiml-138114-kinfeylo) [샘플](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples?WT.mc_id=aiml-138114-kinfeylo)

SDK는 [여기에 문서화된 REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo)를 사용합니다.

## 사용 가능 여부

Azure AI 모델 추론 API는 다음 Phi-3 모델에서 사용할 수 있습니다:

- 서버리스 API 엔드포인트에 배포된 모델:
- 관리형 추론에 배포된 모델:

API는 Azure OpenAI 모델 배포와 호환됩니다.

> [!NOTE]
> Azure AI 모델 추론 API는 2024년 6월 24일 이후에 배포된 모델에 대해 관리형 추론(Managed Online Endpoints)에서 사용할 수 있습니다. API를 활용하려면 해당 날짜 이전에 모델이 배포된 경우 엔드포인트를 다시 배포하십시오.

## 기능

다음 섹션에서는 API가 제공하는 일부 기능을 설명합니다. API의 전체 사양은 참조 섹션을 참조하세요.

### 모달리티

API는 개발자가 다음 모달리티에 대한 예측을 소비할 수 있는 방법을 제공합니다:

- 정보 가져오기: 엔드포인트에 배포된 모델에 대한 정보를 반환합니다.
- 텍스트 임베딩: 입력 텍스트를 나타내는 임베딩 벡터를 생성합니다.
- 텍스트 완성: 제공된 프롬프트와 매개변수에 대한 완성을 생성합니다.
- 채팅 완성: 주어진 채팅 대화에 대한 모델 응답을 생성합니다.
- 이미지 임베딩: 입력 텍스트와 이미지를 나타내는 임베딩 벡터를 생성합니다.

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원본 문서를 신뢰할 수 있는 출처로 간주해야 합니다. 중요한 정보에 대해서는 전문 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.