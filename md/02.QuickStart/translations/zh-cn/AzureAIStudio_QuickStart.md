# **在 Azure AI Studio 中使用 Phi-3 **

随着生成式 AI 的发展，我们希望使用统一平台来管理不同的 LLM 和 SLM，企业数据集成，微调/RAG 操作，以及在整合 LLM 和 SLM 后对不同企业业务的评估等，从而使生成式 AI 能更好地实现智能应用。 [Azure AI Studio](https://ai.azure.com) 是一个面向企业级的生成式 AI 应用平台。

![aistudo](../../../../imgs/02/AIStudio/ai-studio-home.png)

使用 Azure AI Studio，您可以评估大型语言模型（LLM）的响应，并通过提示流程（prompt flow）协调提示应用组件以获得更好的性能。该平台有助于轻松地将概念验证转化为完整的生产应用，实现可扩展性。持续的监控和优化支持长期的成功。

我们可以通过简单的步骤在 Azure AI Studio 上快速部署 Phi-3 模型，然后使用 Azure AI Studio 完成与 Phi-3 相关的 Playground/Chat、微调（Fine-tuning）、评估和其他相关工作。

## **1. 准备工作**
## [AZD AI Studio Starter Template](https://azure.github.io/awesome-azd/?name=AI+Studio)
 
### Azure AI Studio Starter
这是一个Bicep模板，部署了您开始使用Azure AI Studio所需的一切。包括具有依赖资源的AI Hub、AI项目、AI服务和一个在线端点。

### 快速开始使用
如果您已经在电脑上安装了 [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) , 那么，使用此模板就非常简单，只需在新目录中运行此命令即可。

### 终端命令
```bash
azd init -t azd-aistudio-starter
```
或者
如果您安装了 azd 的 VS Code 扩展，就可以在 VS Code 的命令终端中粘贴该URL。

### 终端 URL
```
azd-aistudio-starter
```
## 手动创建
在 [Azure Portal](https://portal.azure.com?WT.mc_id=aiml-138114-kinfeylo) 中手动创建 Azure AI Studio

![portal](../../../../imgs/02/AIStudio/ai-studio-portal.png)

在完成资源的命名并设置区域后，您可以创建它。

![settings](../../../../imgs/02/AIStudio/ai-studio-settings.png)

创建成功后，您可以通过 [ai.azure.com](https://ai.azure.com/)  访问您创建的Azure AI Studio

![page](../../../../imgs/02/AIStudio/ai-studio-page.png)

一个 AI Studio 上可以有多个项目。在 AI Studio 中创建一个项目以做准备。

![proj](../../../../imgs/02/AIStudio/ai-studio-proj.png)


## **2.在 Azure AI Studio 中部署 Phi-3 模型**

点击项目的“Explore”选项，进入模型目录并选择 Phi-3。

![model](../../../../imgs/02/AIStudio/ai-studio-model.png)

选择 Phi-3-mini-4k-instruct

![phi3](../../../../imgs/02/AIStudio/ai-studio-phi3.png)

点击“Deploy”来部署 Phi-3-mini-4k-instruct 模型。

***注意***: 您可以在部署时选择算力。


## **3.在 Azure AI Studio 中通过 Playground 与 Phi-3模型对话**

导航到部署页面，选择Playground，就可以和Azure AI Studio中的Phi-3模型对话了。

![chat](../../../../imgs/02/AIStudio/ai-studio-chat.png)


## **4. 从 Azure AI Studio 部署模型**
要从 AzureModel Catalog 部署一个模型，您可以按照以下步骤操作:

- 登录 Azure AI Studio.
- 从 Azure AI Studio 模型目录中选择要部署的模型.
- 在模型的详情页面上，选择“部署”，然后选择使用Azure AI内容安全的Serverless API。
- 选择要将模型部署到的项目。要使用无服务器API产品，您的工作空间必须属于East US 2地区或Sweden Central地区。您可以自定义部署名称。
- 在部署向导上，选择“Pricing and terms”以了解定价和使用条款。
- 选择“部署”，等待部署准备就绪，然后您将被重定向到部署页面。
- 选择“在Playground中打开”就可以开始与模型互动。
- 您可以返回到部署页面，选择部署，查看endpoint的目标URL和Secret Key，以调用部署并生成完成项。
- 您可以随时通过导航到“Build”标签并从组件部分选择“Deployments”来查找端点的详细信息、URL和访问密钥。

**请注意，您的帐户必须在资源组上具有Azure AI开发人员角色权限才能执行这些操作。**

## **5.在 Azure AI Studio 中使用 Phi-3 模型**

您可以通过Postman的GET方法访问 https://{Your project name}.region.inference.ml.azure.com/swagger.json 并将其与密钥结合使用，以了解提供的接口。

![swagger](../../../../imgs/02/AIStudio/ai-studio-swagger.png)

例如，获取 score api 

![score](../../../../imgs/02/AIStudio/ai-studio-score.png)

您可以非常方便地获取请求参数和响应参数。这是Postman的结果。

![result](../../../../imgs/02/AIStudio/ai-studio-result.png)






















