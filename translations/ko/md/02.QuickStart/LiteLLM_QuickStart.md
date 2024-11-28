[LiteLLM](https://docs.litellm.ai/)을 Phi-3 모델에 사용하면 다양한 애플리케이션에 통합하기에 아주 좋습니다. LiteLLM은 API 호출을 다양한 모델, 특히 Phi-3와 호환되는 요청으로 변환하는 미들웨어 역할을 합니다.

Phi-3는 Microsoft에서 개발한 소형 언어 모델(SLM)로, 자원이 제한된 기기에서도 효율적으로 실행될 수 있도록 설계되었습니다. AVX 지원이 있는 CPU와 최소 4GB의 RAM만으로도 작동할 수 있어, GPU 없이도 로컬 추론을 수행할 수 있는 좋은 옵션입니다.

LiteLLM을 사용하여 Phi-3를 시작하는 몇 가지 단계는 다음과 같습니다:

1. **LiteLLM 설치**: pip을 사용하여 LiteLLM을 설치할 수 있습니다:
   ```bash
   pip install litellm
   ```

2. **환경 변수 설정**: API 키 및 기타 필요한 환경 변수를 설정합니다.
   ```python
   import os
   os.environ["OPENAI_API_KEY"] = "your-api-key"
   ```

3. **API 호출**: LiteLLM을 사용하여 Phi-3 모델에 API 호출을 합니다.
   ```python
   from litellm import completion

   response = completion(
       model="phi-3",
       messages=[{"role": "user", "content": "Hello, how are you?"}]
   )
   print(response)
   ```

4. **통합**: LiteLLM을 Nextcloud Assistant와 같은 다양한 플랫폼과 통합하여 텍스트 생성 및 기타 작업에 Phi-3를 사용할 수 있습니다.

**LLMLite 전체 코드 샘플**
[LLMLite 샘플 코드 노트북](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/litellm.ipynb)

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 모국어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.