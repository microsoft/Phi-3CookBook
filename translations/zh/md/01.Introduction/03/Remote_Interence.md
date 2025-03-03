# 使用微调模型进行远程推理

在远程环境中完成适配器训练后，可以使用一个简单的 Gradio 应用程序与模型交互。

![微调完成](../../../../../translated_images/log-finetuning-res.4b3ee593f24d3096742d09375adade22b217738cab93bc1139f224e5888a1cbf.zh.png)

### 配置 Azure 资源
通过从命令面板执行 `AI Toolkit: Provision Azure Container Apps for inference`，设置用于远程推理的 Azure 资源。在此过程中，您需要选择 Azure 订阅和资源组。  
![配置推理资源](../../../../../translated_images/command-provision-inference.b294f3ae5764ab45b83246d464ad5329b0de20cf380f75a699b4cc6b5495ca11.zh.png)

默认情况下，用于推理的订阅和资源组应与用于微调的相同。推理将使用相同的 Azure Container App 环境，并访问存储在 Azure Files 中的模型和模型适配器，这些内容是在微调步骤中生成的。

## 使用 AI Toolkit

### 推理部署  
如果您希望修改推理代码或重新加载推理模型，请执行 `AI Toolkit: Deploy for inference` 命令。这将同步您的最新代码到 ACA 并重新启动副本。

![推理部署](../../../../../translated_images/command-deploy.cb6508c973d6257e649aa4f262d3c170a374da3e9810a4f3d9e03935408a592b.zh.png)

部署成功完成后，模型就可以通过此端点进行评估。

### 访问推理 API

您可以通过 VSCode 通知中显示的 "*Go to Inference Endpoint*" 按钮访问推理 API。或者，可以在 `ACA_APP_ENDPOINT` 中的 `./infra/inference.config.json` 以及输出面板中找到 Web API 端点。

![应用端点](../../../../../translated_images/notification-deploy.00f4267b7aa6a18cfaaec83a7831b5d09311d5d96a70bb4c9d651ea4a41a8af7.zh.png)

> **注意：** 推理端点可能需要几分钟才能完全运行。

## 模板中包含的推理组件

| 文件夹 | 内容 |
| ------ |------|
| `infra` | 包含所有远程操作所需的配置。 |
| `infra/provision/inference.parameters.json` | 保存用于配置 Azure 推理资源的 bicep 模板参数。 |
| `infra/provision/inference.bicep` | 包含用于配置 Azure 推理资源的模板。 |
| `infra/inference.config.json` | 配置文件，由 `AI Toolkit: Provision Azure Container Apps for inference` 命令生成，用作其他远程命令面板的输入。 |

### 使用 AI Toolkit 配置 Azure 资源
配置 [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

为推理配置 Azure Container Apps` command.

You can find configuration parameters in `./infra/provision/inference.parameters.json` file. Here are the details:
| Parameter | Description |
| --------- |------------ |
| `defaultCommands` | This is the commands to initiate a web API. |
| `maximumInstanceCount` | This parameter sets the maximum capacity of GPU instances. |
| `location` | This is the location where Azure resources are provisioned. The default value is the same as the chosen resource group's location. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | These parameters are used to name the Azure resources for provision. By default, they will be same to the fine-tuning resource name. You can input a new, unused resource name to create your own custom-named resources, or you can input the name of an already existing Azure resource if you'd prefer to use that. For details, refer to the section [Using existing Azure Resources](../../../../../md/01.Introduction/03). |

### Using Existing Azure Resources

By default, the inference provision use the same Azure Container App Environment, Storage Account, Azure File Share, and Azure Log Analytics that were used for fine-tuning. A separate Azure Container App is created solely for the inference API. 

If you have customized the Azure resources during the fine-tuning step or want to use your own existing Azure resources for inference, specify their names in the `./infra/inference.parameters.json` 文件。然后，从命令面板运行 `AI Toolkit: Provision Azure Container Apps for inference` 命令。此命令会更新指定的资源并创建缺失的资源。

例如，如果您已有一个现成的 Azure 容器环境，那么您的 `./infra/finetuning.parameters.json` 文件应如下所示：

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

### 手动配置  
如果您更倾向于手动配置 Azure 资源，可以使用 `./infra/provision` folders. If you have already set up and configured all the Azure resources without using the AI Toolkit command palette, you can simply enter the resource names in the `inference.config.json` 文件中提供的 bicep 文件。

例如：

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

**免责声明**：  
本文件使用基于人工智能的机器翻译服务进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文件作为权威来源。对于关键信息，建议寻求专业人工翻译服务。我们对因使用此翻译而引起的任何误解或错误解释不承担责任。