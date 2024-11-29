# 미세 조정된 모델을 사용한 원격 추론

원격 환경에서 어댑터가 학습된 후, 간단한 Gradio 애플리케이션을 사용하여 모델과 상호 작용할 수 있습니다.

![미세 조정 완료](../../../../translated_images/log-finetuning-res.4b3ee593f24d3096742d09375adade22b217738cab93bc1139f224e5888a1cbf.ko.png)

### Azure 리소스 프로비저닝
명령 팔레트에서 `AI Toolkit: Provision Azure Container Apps for inference`를 실행하여 원격 추론을 위한 Azure 리소스를 설정해야 합니다. 이 설정 과정에서 Azure 구독 및 리소스 그룹을 선택하라는 메시지가 표시됩니다.  
![추론 리소스 프로비저닝](../../../../translated_images/command-provision-inference.b294f3ae5764ab45b83246d464ad5329b0de20cf380f75a699b4cc6b5495ca11.ko.png)

기본적으로, 추론을 위한 구독 및 리소스 그룹은 미세 조정에 사용된 것과 일치해야 합니다. 추론은 동일한 Azure Container App 환경을 사용하고, 미세 조정 단계에서 생성된 모델 및 모델 어댑터를 Azure Files에서 액세스하게 됩니다.

## AI Toolkit 사용

### 추론을 위한 배포  
추론 코드를 수정하거나 추론 모델을 다시 로드하려면 `AI Toolkit: Deploy for inference` 명령을 실행하십시오. 이는 최신 코드를 ACA와 동기화하고 복제본을 다시 시작합니다.

![추론을 위한 배포](../../../../translated_images/command-deploy.a2c9346bd1b7ac9b9fd49fc5e95871a974fbfd647f6c50331f8daa6e45121225.ko.png)

배포가 성공적으로 완료되면 이 엔드포인트를 사용하여 모델을 평가할 준비가 된 것입니다.

### 추론 API 액세스

VSCode 알림에 표시된 "*Go to Inference Endpoint*" 버튼을 클릭하여 추론 API에 액세스할 수 있습니다. 또는 웹 API 엔드포인트는 `ACA_APP_ENDPOINT`에서 `./infra/inference.config.json` 및 출력 패널에서 찾을 수 있습니다.

![앱 엔드포인트](../../../../translated_images/notification-deploy.79f6704239f7d016da3bf72b5c661961c8ddd17147fad195f6282df94d489a86.ko.png)

> **참고:** 추론 엔드포인트가 완전히 작동하기까지 몇 분이 걸릴 수 있습니다.

## 템플릿에 포함된 추론 구성 요소

| 폴더 | 내용 |
| ------ |--------- |
| `infra` | 원격 작업에 필요한 모든 구성을 포함하고 있습니다. |
| `infra/provision/inference.parameters.json` | 추론을 위한 Azure 리소스를 프로비저닝하는 데 사용되는 bicep 템플릿의 매개변수를 보유하고 있습니다. |
| `infra/provision/inference.bicep` | 추론을 위한 Azure 리소스를 프로비저닝하기 위한 템플릿을 포함하고 있습니다. |
| `infra/inference.config.json` | `AI Toolkit: Provision Azure Container Apps for inference` 명령에 의해 생성된 구성 파일입니다. 다른 원격 명령 팔레트의 입력으로 사용됩니다. |

### AI Toolkit을 사용하여 Azure 리소스 프로비저닝 구성
[AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)을 구성합니다.

추론을 위한 Azure Container Apps를 프로비저닝합니다` command.

You can find configuration parameters in `./infra/provision/inference.parameters.json` file. Here are the details:
| Parameter | Description |
| --------- |------------ |
| `defaultCommands` | This is the commands to initiate a web API. |
| `maximumInstanceCount` | This parameter sets the maximum capacity of GPU instances. |
| `location` | This is the location where Azure resources are provisioned. The default value is the same as the chosen resource group's location. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | These parameters are used to name the Azure resources for provision. By default, they will be same to the fine-tuning resource name. You can input a new, unused resource name to create your own custom-named resources, or you can input the name of an already existing Azure resource if you'd prefer to use that. For details, refer to the section [Using existing Azure Resources](../../../../md/03.Inference). |

### Using Existing Azure Resources

By default, the inference provision use the same Azure Container App Environment, Storage Account, Azure File Share, and Azure Log Analytics that were used for fine-tuning. A separate Azure Container App is created solely for the inference API. 

If you have customized the Azure resources during the fine-tuning step or want to use your own existing Azure resources for inference, specify their names in the `./infra/inference.parameters.json` 파일을 사용합니다. 그런 다음, 명령 팔레트에서 `AI Toolkit: Provision Azure Container Apps for inference` 명령을 실행합니다. 이는 지정된 리소스를 업데이트하고 누락된 리소스를 생성합니다.

예를 들어, 기존 Azure 컨테이너 환경이 있는 경우 `./infra/finetuning.parameters.json`은 다음과 같아야 합니다:

```json
{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
      ...
      "acaEnvironmentName": {
        "value": "<your-aca-env-name>"
      },
      "acaEnvironmentStorageName": {
        "value": null
      },
      ...
    }
  }
```

### 수동 프로비저닝  
Azure 리소스를 수동으로 구성하려면 `./infra/provision` folders. If you have already set up and configured all the Azure resources without using the AI Toolkit command palette, you can simply enter the resource names in the `inference.config.json` 파일에 제공된 bicep 파일을 사용할 수 있습니다.

예시:

```json
{
  "SUBSCRIPTION_ID": "<your-subscription-id>",
  "RESOURCE_GROUP_NAME": "<your-resource-group-name>",
  "STORAGE_ACCOUNT_NAME": "<your-storage-account-name>",
  "FILE_SHARE_NAME": "<your-file-share-name>",
  "ACA_APP_NAME": "<your-aca-name>",
  "ACA_APP_ENDPOINT": "<your-aca-endpoint>"
}
```

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원어로 작성된 원본 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.