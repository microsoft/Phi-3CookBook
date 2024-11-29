# Azure API 사용하기 - Phi-3

이 노트북은 Microsoft Azure AI 및 Azure ML에서 제공하는 Phi-3 API를 사용하는 예제를 보여줍니다. 우리는 다음을 다룰 것입니다:
* CLI에서 Phi-3 사전 학습 및 채팅 모델에 대한 HTTP 요청 API 사용법
* Python에서 Phi-3 사전 학습 및 채팅 모델에 대한 HTTP 요청 API 사용법

자, **CLI에서 HTTP 요청 API 사용법**에 대한 개요입니다:

## CLI에서 HTTP 요청 API 사용법

### 기본 사항

REST API를 사용하려면 엔드포인트 URL과 해당 엔드포인트와 연관된 인증 키가 필요합니다. 이는 이전 단계에서 얻을 수 있습니다.

이 채팅 완료 예제에서는 간단한 `curl` 호출을 사용하여 설명합니다. 주요 구성 요소는 세 가지입니다:

1. **`host-url`**: 이는 채팅 완료 스키마 `/v1/chat/completions`를 포함한 엔드포인트 URL입니다.
2. **`headers`**: 이는 콘텐츠 유형과 API 키를 정의합니다.
3. **`payload` 또는 `data`**: 이는 프롬프트 세부 정보와 모델 하이퍼파라미터를 포함합니다.

### 예제

다음은 `curl`을 사용하여 채팅 완료 요청을 만드는 예제입니다:

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

- **`-X POST`**: Specifies the HTTP method to use, which is POST in this case.
- **`https://api.example.com/v1/chat/completions`**: The endpoint URL.
- **`-H "Content-Type: application/json"`**: Sets the content type to JSON.
- **`-H "Authorization: Bearer YOUR_API_KEY"`**: Adds the authorization header with your API key.
- **`-d '{...}'`**: The data payload, which includes the model, messages, and other parameters.

### Tips

- **Endpoint URL**: Ensure you replace `https://api.example.com` with your actual endpoint URL.
- **API Key**: Replace `YOUR_API_KEY`**: 실제 API 키로 교체하세요.
- **Payload**: 다양한 프롬프트, 모델 및 파라미터를 포함하여 요구 사항에 맞게 페이로드를 맞춤 설정하세요.

샘플을 보려면 [Http Connections and Streaming](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/webrequests.ipynb)을 참조하세요.

AI Studio 및 ML Studio에서 모델 추론 엔드포인트를 프로비저닝하는 방법, 지역 가용성, 가격 및 추론 스키마 참조에 대한 자세한 내용은 [문서](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo&tabs=phi-3-mini&pivots=programming-language-rest)를 검토하세요.

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원어로 작성된 원본 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.