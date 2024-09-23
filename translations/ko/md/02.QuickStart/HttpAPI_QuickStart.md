# Azure API를 Phi-3와 함께 사용하기

이 노트북은 Microsoft Azure AI와 Azure ML에서 제공하는 Phi-3 API를 사용하는 예제를 보여줍니다. 우리는 다음을 다룰 것입니다:  
* CLI에서 Phi-3 사전 훈련된 모델과 채팅 모델을 위한 HTTP 요청 API 사용법
* Python에서 Phi-3 사전 훈련된 모델과 채팅 모델을 위한 HTTP 요청 API 사용법

자, **CLI에서 HTTP 요청 API 사용법**에 대한 개요를 보겠습니다:

## CLI에서 HTTP 요청 API 사용법

### 기본 사항

REST API를 사용하려면 엔드포인트 URL과 해당 엔드포인트와 연결된 인증 키가 필요합니다. 이는 이전 단계에서 획득할 수 있습니다.

이 채팅 완료 예제에서는 간단한 `curl` 호출을 사용하여 설명합니다. 세 가지 주요 구성 요소가 있습니다:

1. **`host-url`**: 채팅 완료 스키마 `/v1/chat/completions`가 포함된 엔드포인트 URL입니다.
2. **`headers`**: 콘텐츠 유형과 API 키를 정의합니다.
3. **`payload` 또는 `data`**: 프롬프트 세부 정보와 모델 하이퍼파라미터를 포함합니다.

### 예제

다음은 `curl`을 사용하여 채팅 완료 요청을 하는 예제입니다:

```bash
curl -X POST https://api.example.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_API_KEY" \
-d '{
  "model": "phi-3",
  "messages": [{"role": "user", "content": "Hello, how are you?"}],
  "max_tokens": 50
}'
```

### 세부 설명

- **`-X POST`**: 사용할 HTTP 메서드를 지정하며, 이 경우 POST입니다.
- **`https://api.example.com/v1/chat/completions`**: 엔드포인트 URL입니다.
- **`-H "Content-Type: application/json"`**: 콘텐츠 유형을 JSON으로 설정합니다.
- **`-H "Authorization: Bearer YOUR_API_KEY"`**: API 키와 함께 인증 헤더를 추가합니다.
- **`-d '{...}'`**: 데이터 페이로드로, 모델, 메시지 및 기타 매개변수를 포함합니다.

### 팁

- **엔드포인트 URL**: `https://api.example.com`을 실제 엔드포인트 URL로 교체하세요.
- **API 키**: `YOUR_API_KEY`를 실제 API 키로 교체하세요.
- **페이로드**: 다양한 프롬프트, 모델 및 매개변수를 포함하여 페이로드를 필요에 맞게 사용자 정의하세요.

[Http Connections and Streaming](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/webrequests.ipynb) 샘플을 참조하세요.

AI Studio 및 ML Studio에서 Phi-3 모델 패밀리에 대한 세부 사항(추론 엔드포인트 프로비저닝 방법, 지역 가용성, 가격 및 추론 스키마 참조)에 대해서는 [문서](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo&tabs=phi-3-mini&pivots=programming-language-rest)를 검토하세요.

면책 조항: 이 번역은 원본을 AI 모델에 의해 번역된 것이며 완벽하지 않을 수 있습니다. 
출력을 검토하고 필요한 수정 사항을 반영해 주시기 바랍니다.