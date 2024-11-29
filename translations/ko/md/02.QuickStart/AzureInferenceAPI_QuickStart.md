## Python에서 Phi Family 모델 실행 다른 샘플은 https://github.com/marketplace/models 를 참조하세요

아래는 몇 가지 사용 사례에 대한 예제 코드 조각입니다. Azure AI Inference SDK에 대한 추가 정보는 [전체 문서](https://aka.ms/azsdk/azure-ai-inference/python/reference) 및 [샘플](https://aka.ms/azsdk/azure-ai-inference/python/samples)을 참조하세요.

```
pip install azure-ai-inference
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

# 모델을 인증하려면 GitHub Marketplace 모델을 사용하는 경우 GitHub 설정에서 개인 액세스 토큰(PAT)을 생성해야 합니다 (https://github.com/marketplace/models). 
# 여기에서 PAT 토큰을 생성하는 방법을 따르세요: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
# GitHub 개인 토큰 또는 Azure 키에 대한 GitHub_token으로 .env 파일을 생성하세요

client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
)

response = client.complete(
    messages=[
        SystemMessage(content=""""""),
        UserMessage(content="기계 학습의 기본을 설명해 줄 수 있나요?"),
    ],
    # 적절한 모델 이름 "Phi-3.5-mini-instruct" 또는 "Phi-3.5-vision-instruct"로 모델 이름을 변경하세요
    model="Phi-3.5-MoE-instruct", 
    temperature=0.8,
    max_tokens=2048,
    top_p=0.1
)

print(response.choices[0].message.content)
```

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 우리는 정확성을 위해 노력하지만 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원어로 작성된 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보에 대해서는 전문 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.