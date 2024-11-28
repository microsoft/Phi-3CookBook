# 推理 Azure AI 模型

[Azure AI 模型推理 API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo) 提供了一组通用的基础模型能力，开发人员可以通过这种方式以统一和一致的方式从各种模型中获取预测。开发人员可以与部署在 Azure AI Foundry 的不同模型进行交互，而无需更改他们所使用的底层代码。

微软现在有自己的 AI 模型推理 SDK，适用于托管在 [MaaS/MaaP](https://azure.microsoft.com/products/ai-model-catalog?WT.mc_id=aiml-138114-kinfeylo) 上的不同模型。

Python 和 JS 版本已经发布。C# 版本即将发布。

对于 [Python](https://learn.microsoft.com/python/api/overview/azure/ai-inference-readme?view=azure-python-preview?WT.mc_id=aiml-138114-kinfeylo) [示例](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples?WT.mc_id=aiml-138114-kinfeylo)

对于 [JavaScript](https://learn.microsoft.com/javascript/api/overview/azure/ai-inference-rest-readme?view=azure-node-preview?WT.mc_id=aiml-138114-kinfeylo) [示例](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples?WT.mc_id=aiml-138114-kinfeylo)

SDK 使用了[这里记录的 REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo)。

## 可用性

Azure AI 模型推理 API 可用于以下 Phi-3 模型：

- 部署到无服务器 API 端点的模型：
- 部署到托管推理的模型：

该 API 与 Azure OpenAI 模型部署兼容。

> [!NOTE]
> Azure AI 模型推理 API 在 2024 年 6 月 24 日之后部署的模型的托管推理（托管在线端点）中可用。要利用该 API，如果模型是在此日期之前部署的，请重新部署您的端点。

## 功能

以下部分描述了 API 提供的一些功能。要查看 API 的完整规范，请查看参考部分。

### 模态

API 指示开发人员如何获取以下模态的预测：

- 获取信息：返回有关在端点下部署的模型的信息。
- 文本嵌入：创建表示输入文本的嵌入向量。
- 文本完成：为提供的提示和参数创建一个完成。
- 聊天完成：为给定的聊天对话创建模型响应。
- 图像嵌入：创建表示输入文本和图像的嵌入向量。

**免责声明**：
本文件使用基于机器的人工智能翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文件视为权威来源。对于关键信息，建议进行专业的人类翻译。对于因使用本翻译而产生的任何误解或误读，我们不承担责任。