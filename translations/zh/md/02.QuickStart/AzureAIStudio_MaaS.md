# 部署 Phi-3 模型为无服务器 API

[Azure 模型目录](https://learn.microsoft.com/azure/machine-learning/concept-model-catalog?WT.mc_id=aiml-137032-kinfeylo)中的 Phi-3 模型（Mini、Small 和 Medium）可以部署为按需付费的无服务器 API。这种部署方式提供了一种通过 API 消费模型的方法，而无需在你的订阅中托管它们，同时保持企业所需的安全性和合规性。这种部署选项不需要从你的订阅中获取配额。

[REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo) MaaS 模型现在支持使用 /chat/completions 路由进行聊天完成的通用 REST API。

## 先决条件

1. 一个具有有效支付方式的 Azure 订阅。免费或试用的 Azure 订阅无法使用。如果你没有 Azure 订阅，请创建一个付费的 Azure 账户开始使用。
1. 一个 [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) 中心。Phi-3 的无服务器 API 模型部署仅在以下区域创建的中心中可用：
    - **美国东部 2**
    - **瑞典中部**

    > [!NOTE]
    > 有关支持无服务器 API 端点部署的每个模型可用区域的列表，请参见无服务器 API 端点中的模型区域可用性。

1. 一个 [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) 项目。
1. Azure 基于角色的访问控制 (Azure RBAC) 用于授予对 Azure AI Studio 中操作的访问权限。要执行本文中的步骤，你的用户帐户必须在资源组上分配 Azure AI 开发者角色。

## 创建新的部署

执行以下任务以创建部署：

1. 登录到 [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。
1. 从左侧边栏选择模型目录。
1. 搜索并选择你想要部署的模型，例如 Phi-3-mini-4k-Instruct，打开其详细信息页面。
1. 选择部署。
1. 选择无服务器 API 选项以打开模型的无服务器 API 部署窗口。

或者，你可以从 AI Studio 中的项目开始启动部署。

1. 从项目的左侧边栏选择组件 > 部署。
1. 选择 + 创建部署。
1. 搜索并选择 Phi-3-mini-4k-Instruct 以打开模型的详细信息页面。
1. 选择确认，并选择无服务器 API 选项以打开模型的无服务器 API 部署窗口。
1. 选择你要部署模型的项目。要部署 Phi-3 模型，你的项目必须属于[先决条件部分](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo)中列出的区域之一。
1. 选择定价和条款标签以了解所选模型的定价。
1. 给部署起一个名字。这个名字将成为部署 API URL 的一部分。这个 URL 在每个 Azure 区域中必须是唯一的。
1. 选择部署。等待部署准备就绪，并将你重定向到部署页面。此步骤要求你的帐户在资源组上具有 Azure AI 开发者角色权限，如先决条件中所列。
1. 选择在操场中打开以开始与模型交互。

返回到部署页面，选择部署，并记下端点的目标 URL 和密钥，你可以用它们来调用部署并生成完成。有关使用 API 的更多信息，请参见[参考：聊天完成](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)。

你始终可以通过导航到项目概览页面找到端点的详细信息、URL 和访问密钥。然后，从项目的左侧边栏选择组件 > 部署。

## 将 Phi-3 模型作为服务消费

根据你部署的模型类型，部署为无服务器 API 的模型可以使用聊天 API 进行消费。

1. 从项目概览页面，转到左侧边栏并选择组件 > 部署。
2. 找到并选择你创建的部署。
3. 复制目标 URL 和密钥值。
4. 使用 chat/completions API 发出 API 请求，使用 <target_url>chat/completions。有关使用 API 的更多信息，请参见[参考：聊天完成](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)。

## 成本和配额

部署为无服务器 API 的 Phi-3 模型的成本和配额考虑

你可以在部署向导的定价和条款标签中找到定价信息。

配额是按部署管理的。每个部署每分钟有 200,000 个令牌的速率限制和每分钟 1,000 个 API 请求。然而，目前我们限制每个项目每个模型一个部署。如果当前的速率限制不足以满足你的场景，请联系 Microsoft Azure 支持。

## 其他资源

### 部署模型为无服务器 API

MaaS 模型即服务 详细信息请参见 [MaaS 部署](https://learn.microsoft.com//azure/ai-studio/how-to/deploy-models-serverless?tabs=azure-ai-studio?WT.mc_id=aiml-137032-kinfeylo)

### 如何使用 Azure Machine Learning Studio 或 Azure AI Studio 部署 Phi-3 系列的小型语言模型

Maap 模型即平台 详细信息请参见 [MaaP 部署](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)

