# Phi-3 모델을 서버리스 API로 배포하기

[Azure 모델 카탈로그](https://learn.microsoft.com/azure/machine-learning/concept-model-catalog?WT.mc_id=aiml-137032-kinfeylo)에 있는 Phi-3 모델(Mini, Small, Medium)은 사용한 만큼만 비용을 지불하는 서버리스 API로 배포할 수 있습니다. 이러한 배포 방식은 모델을 구독에 호스팅하지 않고도 API로 소비할 수 있는 방법을 제공하며, 조직이 필요로 하는 엔터프라이즈 보안 및 규정을 유지할 수 있습니다. 이 배포 옵션은 구독에서 할당량을 요구하지 않습니다.

[REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo) MaaS 모델은 이제 /chat/completions 경로를 사용하여 채팅 완료를 위한 공통 REST API를 지원합니다.

## 사전 요구 사항

1. 유효한 결제 수단이 있는 Azure 구독. 무료 또는 체험판 Azure 구독은 작동하지 않습니다. Azure 구독이 없는 경우 유료 Azure 계정을 생성하여 시작하십시오.
1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) 허브. Phi-3의 서버리스 API 모델 배포는 다음 지역에서 생성된 허브에서만 사용할 수 있습니다:
    - **미국 동부 2**
    - **스웨덴 중앙**

    > [!NOTE]
    > 서버리스 API 엔드포인트 배포를 지원하는 각 모델에 대해 사용할 수 있는 지역 목록은 서버리스 API 엔드포인트의 모델 지역 가용성을 참조하십시오.

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) 프로젝트.
1. Azure 역할 기반 액세스 제어(Azure RBAC)는 Azure AI Foundry의 작업에 대한 액세스를 부여하는 데 사용됩니다. 이 문서의 단계를 수행하려면 사용자 계정에 리소스 그룹에 대한 Azure AI 개발자 역할이 할당되어야 합니다.

## 새로운 배포 생성

배포를 생성하려면 다음 작업을 수행하십시오:

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)에 로그인합니다.
1. 왼쪽 사이드바에서 모델 카탈로그를 선택합니다.
1. 배포하려는 모델을 검색하고 선택합니다. 예를 들어 Phi-3-mini-4k-Instruct를 선택하여 세부 정보 페이지를 엽니다.
1. 배포를 선택합니다.
1. 서버리스 API 옵션을 선택하여 모델에 대한 서버리스 API 배포 창을 엽니다.

또는 AI Foundry의 프로젝트에서 시작하여 배포를 시작할 수 있습니다.

1. 프로젝트의 왼쪽 사이드바에서 구성 요소 > 배포를 선택합니다.
1. + 배포 생성 선택합니다.
1. Phi-3-mini-4k-Instruct를 검색하고 선택하여 모델의 세부 정보 페이지를 엽니다.
1. 확인을 선택하고 서버리스 API 옵션을 선택하여 모델에 대한 서버리스 API 배포 창을 엽니다.
1. 모델을 배포할 프로젝트를 선택합니다. Phi-3 모델을 배포하려면 프로젝트가 [사전 요구 사항 섹션](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo)에 나열된 지역 중 하나에 속해야 합니다.
1. 가격 및 조건 탭을 선택하여 선택한 모델의 가격에 대해 알아봅니다.
1. 배포에 이름을 지정합니다. 이 이름은 배포 API URL의 일부가 됩니다. 이 URL은 각 Azure 지역에서 고유해야 합니다.
1. 배포를 선택합니다. 배포가 준비될 때까지 기다렸다가 배포 페이지로 리디렉션됩니다. 이 단계는 사전 요구 사항에 나열된 대로 리소스 그룹에 대한 Azure AI 개발자 역할 권한이 있는 계정이 필요합니다.
1. 플레이그라운드에서 열기를 선택하여 모델과 상호 작용을 시작합니다.

배포 페이지로 돌아가서 배포를 선택하고 배포의 대상 URL과 비밀 키를 확인하여 배포를 호출하고 완료를 생성할 수 있습니다. API 사용에 대한 자세한 내용은 [참조: 채팅 완료](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)를 참조하십시오.

프로젝트 개요 페이지로 이동하여 항상 엔드포인트의 세부 정보, URL 및 액세스 키를 찾을 수 있습니다. 그런 다음 프로젝트의 왼쪽 사이드바에서 구성 요소 > 배포를 선택합니다.

## Phi-3 모델을 서비스로 소비하기

서버리스 API로 배포된 모델은 배포된 모델 유형에 따라 채팅 API를 사용하여 소비할 수 있습니다.

1. 프로젝트 개요 페이지에서 왼쪽 사이드바로 이동하여 구성 요소 > 배포를 선택합니다.
2. 생성한 배포를 찾아 선택합니다.
3. 대상 URL과 키 값을 복사합니다.
4. <target_url>chat/completions를 사용하여 chat/completions API를 사용하여 API 요청을 만듭니다. API 사용에 대한 자세한 내용은 [참조: 채팅 완료](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)를 참조하십시오.

## 비용 및 할당량

서버리스 API로 배포된 Phi-3 모델에 대한 비용 및 할당량 고려 사항

모델을 배포할 때 배포 마법사의 가격 및 조건 탭에서 가격 정보를 찾을 수 있습니다.

할당량은 배포당 관리됩니다. 각 배포는 분당 200,000 토큰 및 분당 1,000 API 요청의 속도 제한이 있습니다. 그러나 현재 프로젝트당 모델당 하나의 배포로 제한됩니다. 현재 속도 제한이 시나리오에 충분하지 않은 경우 Microsoft Azure 지원에 문의하십시오.

## 추가 자료

### 모델을 서버리스 API로 배포

MaaS 모델 서비스에 대한 자세한 내용은 [MaaS 배포](https://learn.microsoft.com//azure/ai-studio/how-to/deploy-models-serverless?tabs=azure-ai-studio?WT.mc_id=aiml-137032-kinfeylo)를 참조하십시오.

### Azure Machine Learning 스튜디오 또는 Azure AI Foundry를 사용하여 Phi-3 소형 언어 모델 배포 방법

Maap 모델 플랫폼에 대한 자세한 내용은 [Maap 배포](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)를 참조하십시오.

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원본 문서는 해당 언어로 작성된 원본 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문 인간 번역을 권장합니다. 이 번역을 사용하여 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.