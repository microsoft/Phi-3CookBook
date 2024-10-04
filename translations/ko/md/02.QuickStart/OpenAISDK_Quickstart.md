# Azure AI 및 Azure ML에서 Phi-3와 함께 OpenAI SDK 사용하기

Azure AI 및 Azure ML에서 Phi-3 배포를 사용하려면 `openai` SDK를 사용하세요. Azure AI 및 Azure ML의 Phi-3 모델군은 OpenAI Chat Completion API와 호환되는 API를 제공합니다. 이를 통해 고객과 사용자는 OpenAI 모델에서 Phi-3 LLM으로 원활하게 전환할 수 있습니다.

이 API는 OpenAI의 클라이언트 라이브러리나 LangChain 또는 LlamaIndex와 같은 타사 도구와 직접 사용할 수 있습니다.

아래 예제는 OpenAI Python 라이브러리를 사용하여 이 전환을 수행하는 방법을 보여줍니다. Phi-3는 채팅 완료 API만 지원한다는 점에 유의하세요.

OpenAI SDK를 사용하여 Phi-3 모델을 사용하려면 환경을 설정하고 API 호출을 수행하는 몇 가지 단계를 따라야 합니다. 시작하는 데 도움이 되는 가이드는 다음과 같습니다:

1. **OpenAI SDK 설치하기**: 먼저, OpenAI Python 패키지를 설치해야 합니다(이미 설치하지 않은 경우).
   ```bash
   pip install openai
   ```

2. **API 키 설정하기**: OpenAI API 키를 준비하세요. 환경 변수에 설정하거나 코드에 직접 입력할 수 있습니다.
   ```python
   import openai

   openai.api_key = "your-api-key"
   ```

3. **API 호출하기**: OpenAI SDK를 사용하여 Phi-3 모델과 상호작용하세요. 다음은 완료 요청을 수행하는 예제입니다:
   ```python
   response = openai.Completion.create(
       model="phi-3",
       prompt="Hello, how are you?",
       max_tokens=50
   )

   print(response.choices[0].text.strip())
   ```

4. **응답 처리하기**: 애플리케이션에 필요한 대로 모델의 응답을 처리하세요.

여기 더 자세한 예제가 있습니다:
```python
import openai

# Set your API key
openai.api_key = "your-api-key"

# Define the prompt
prompt = "Write a short story about a brave knight."

# Make the API call
response = openai.Completion.create(
    model="phi-3",
    prompt=prompt,
    max_tokens=150
)

# Print the response
print(response.choices[0].text.strip())
```

이 코드는 제공된 프롬프트를 기반으로 짧은 이야기를 생성합니다. 출력 길이를 조절하려면 `max_tokens` 매개변수를 조정할 수 있습니다.

[Phi-3 모델용 전체 노트북 샘플 보기](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/openaisdk.ipynb)

Phi-3 모델군에 대한 자세한 내용은 AI Studio 및 ML Studio에서 추론 엔드포인트를 프로비저닝하는 방법, 지역 가용성, 가격 및 추론 스키마 참조에 대한 정보를 확인하려면 [문서](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo)를 검토하세요.

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.