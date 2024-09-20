# **使用 Azure AI Studio 进行评估**

![aistudo](../../../../translated_images/AIStudio.d5171bb73e888005d9ac4020bbbf4ad9bd9a8bc042dfaf90b44c3afa1a8cbeed.zh.png)

如何使用 [Azure AI Studio](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) 评估你的生成式 AI 应用程序。无论你是在评估单轮对话还是多轮对话，Azure AI Studio 都提供了评估模型性能和安全性的工具。

![aistudo](../../../../translated_images/AIPortfolio.d7a339b6c36a58d3ca1bc2ca3b181618e45b1c87a6c20527a4503cb74e78e5cf.zh.png)

## 如何使用 Azure AI Studio 评估生成式 AI 应用程序
更多详细说明请参见 [Azure AI Studio 文档](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

以下是开始的步骤：

## 在 Azure AI Studio 中评估生成式 AI 模型

**前提条件**

- 一个 CSV 或 JSON 格式的测试数据集。
- 一个已部署的生成式 AI 模型（如 Phi-3、GPT 3.5、GPT 4 或 Davinci 模型）。
- 一个运行时实例，用于运行评估。

## 内置评估指标

Azure AI Studio 允许你评估单轮和复杂的多轮对话。
对于模型基于特定数据的检索增强生成 (RAG) 场景，你可以使用内置评估指标来评估性能。
此外，你还可以评估一般的单轮问答场景（非 RAG）。

## 创建评估运行

从 Azure AI Studio 界面，导航到评估页面或提示流页面。
按照评估创建向导设置评估运行。可以为你的评估提供一个可选名称。
选择与你的应用目标一致的场景。
选择一个或多个评估指标来评估模型的输出。

## 自定义评估流程（可选）

为了更大的灵活性，你可以建立一个自定义评估流程。根据你的具体需求定制评估过程。

## 查看结果

运行评估后，在 Azure AI Studio 中记录、查看和分析详细的评估指标。深入了解你的应用能力和局限性。



**Note** Azure AI Studio 目前处于公开预览阶段，因此请将其用于实验和开发目的。对于生产工作负载，请考虑其他选项。更多详细信息和分步说明请参见官方 [AI Studio 文档](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo)。

免责声明：本翻译由人工智能模型从原文翻译而来，可能并不完美。请审核输出内容并进行必要的修改。