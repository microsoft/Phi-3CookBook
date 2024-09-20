# 推理 Azure AI 模型

[Azure AI 模型推理是一种 API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo)，它为基础模型提供了一套通用功能，开发者可以使用该 API 以统一和一致的方式从各种模型中获取预测。开发者可以与部署在 Azure AI Studio 中的不同模型进行交互，而无需更改他们正在使用的底层代码。

微软现在为托管在 [MaaS/MaaP](https://azure.microsoft.com/products/ai-model-catalog?WT.mc_id=aiml-138114-kinfeylo) 上的不同模型提供了自己的 AI 模型推理 SDK。

Python 和 JS 版本已经发布。C# 版本即将发布。

[Python](https://learn.microsoft.com/python/api/overview/azure/ai-inference-readme?view=azure-python-preview?WT.mc_id=aiml-138114-kinfeylo) [示例](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples?WT.mc_id=aiml-138114-kinfeylo)

[JavaScript](https://learn.microsoft.com/javascript/api/overview/azure/ai-inference-rest-readme?view=azure-node-preview?WT.mc_id=aiml-138114-kinfeylo) [示例](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples?WT.mc_id=aiml-138114-kinfeylo)

该 SDK 使用了[此处记录的 REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo)。

## 可用性

Azure AI 模型推理 API 可用于以下 Phi-3 模型：

- 部署到无服务器 API 端点的模型：
- 部署到托管推理的模型：

该 API 与 Azure OpenAI 模型部署兼容。

> [!NOTE]
> Azure AI 模型推理 API 可用于 2024 年 6 月 24 日之后部署的托管推理（托管在线端点）模型。要利用该 API，如果模型是在此日期之前部署的，请重新部署您的端点。

## 功能

以下部分描述了该 API 提供的一些功能。有关 API 的完整规范，请查看参考部分。

### 模态

该 API 指示开发者如何获取以下模态的预测：

- 获取信息：返回部署在端点下的模型信息。
- 文本嵌入：创建表示输入文本的嵌入向量。
- 文本补全：为提供的提示和参数创建补全。
- 聊天补全：为给定的聊天对话创建模型响应。
- 图像嵌入：创建表示输入文本和图像的嵌入向量。

免责声明：该翻译由人工智能模型从原文翻译而来，可能不完全准确。请审阅输出并进行必要的修改。