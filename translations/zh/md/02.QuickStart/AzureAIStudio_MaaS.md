# 将 Phi-3 模型部署为无服务器 API

在 [Azure 模型目录](https://learn.microsoft.com/azure/machine-learning/concept-model-catalog?WT.mc_id=aiml-137032-kinfeylo) 中的 Phi-3 模型（Mini、Small 和 Medium）可以按需计费的方式部署为无服务器 API。这种部署方式提供了一种无需在您的订阅中托管模型的 API 消费方式，同时保持企业所需的安全性和合规性。这种部署选项不需要从您的订阅中消耗配额。

[REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo) MaaS 模型现在支持使用 /chat/completions 路由进行聊天完成的通用 REST API。

## 先决条件

1. 一个具有有效支付方式的 Azure 订阅。免费或试用的 Azure 订阅无法使用。如果您没有 Azure 订阅，请创建一个付费的 Azure 账户以开始使用。
1. 一个 [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) 中心。Phi-3 的无服务器 API 模型部署仅适用于在以下地区创建的中心：
    - **美国东部 2**
    - **瑞典中部**

    > [!NOTE]
    > 有关支持无服务器 API 端点部署的模型在每个区域的可用性列表，请参阅无服务器 API 端点中模型的区域可用性。

1. 一个 [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) 项目。
1. Azure 基于角色的访问控制 (Azure RBAC) 用于授予对 Azure AI Foundry 中操作的访问权限。要执行本文中的步骤，您的用户账户必须在资源组上分配有 Azure AI Developer 角色。

## 创建新部署

执行以下任务来创建部署：

1. 登录到 [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。
1. 从左侧边栏选择模型目录。
1. 搜索并选择您要部署的模型，例如 Phi-3-mini-4k-Instruct，以打开其详情页面。
1. 选择部署。
1. 选择无服务器 API 选项以打开模型的无服务器 API 部署窗口。

或者，您可以从 AI Foundry 项目开始启动部署。

1. 从项目的左侧边栏选择组件 > 部署。
1. 选择 + 创建部署。
1. 搜索并选择 Phi-3-mini-4k-Instruct 以打开模型的详情页面。
1. 选择确认，并选择无服务器 API 选项以打开模型的无服务器 API 部署窗口。
1. 选择您希望部署模型的项目。要部署 Phi-3 模型，您的项目必须属于 [先决条件部分](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo)中列出的区域之一。
1. 选择定价和条款标签以了解所选模型的定价。
1. 为部署命名。此名称将成为部署 API URL 的一部分。此 URL 在每个 Azure 区域必须是唯一的。
1. 选择部署。等待部署完成并重定向到部署页面。此步骤要求您的账户在资源组上具有 Azure AI Developer 角色权限，如先决条件中所列。
1. 选择在操场中打开以开始与模型交互。

返回到部署页面，选择部署，并记录端点的目标 URL 和密钥，您可以使用它们来调用部署并生成完成。有关使用 API 的更多信息，请参阅 [参考：聊天完成](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)。

您可以通过导航到项目概览页面随时找到端点的详细信息、URL 和访问密钥。然后，从项目的左侧边栏选择组件 > 部署。

## 作为服务使用 Phi-3 模型

部署为无服务器 API 的模型可以根据您部署的模型类型使用聊天 API 进行消费。

1. 从项目概览页面，转到左侧边栏并选择组件 > 部署。
2. 找到并选择您创建的部署。
3. 复制目标 URL 和密钥值。
4. 使用 <target_url>chat/completions 使用 chat/completions API 进行 API 请求。有关使用 API 的更多信息，请参阅 [参考：聊天完成](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)。

## 成本和配额

部署为无服务器 API 的 Phi-3 模型的成本和配额考虑因素

您可以在部署向导的定价和条款标签中找到定价信息。

配额是按部署管理的。每个部署的速率限制为每分钟 200,000 个令牌和每分钟 1,000 个 API 请求。然而，我们目前限制每个项目每个模型一个部署。如果当前的速率限制不适合您的场景，请联系 Microsoft Azure 支持。

## 其他资源

### 将模型部署为无服务器 API

MaaS 模型作为服务有关 [MaaS 部署](https://learn.microsoft.com//azure/ai-studio/how-to/deploy-models-serverless?tabs=azure-ai-studio?WT.mc_id=aiml-137032-kinfeylo) 的详细信息

### 如何使用 Azure 机器学习工作室或 Azure AI Foundry 部署 Phi-3 系列的小型语言模型

Maap 模型作为平台有关 [MaaP 部署](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini) 的详细信息

**免责声明**：
本文档已使用基于机器的AI翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而引起的任何误解或误读承担责任。