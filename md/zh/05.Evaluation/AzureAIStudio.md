# 使用 Azure AI Studio 进行评估

![aistudo](../../imgs/05/AIStudio/AIStudio.png)

如何使用 [Azure AI Studio](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) 评估您的生成式 AI 应用程序。无论您是在评估单轮对话还是多轮对话，Azure AI Studio 都提供了用于评估模型性能和安全性的工具。

![aistudo](../../imgs/05/AIStudio/AIPortfolio.png)

以下是开始的步骤：

## 在 Azure AI Studio 中评估生成式 AI 模型

**前提条件**

- 一个测试数据集，格式为 CSV 或 JSON。
- 一个已部署的生成式 AI 模型（例如 Phi-3、GPT 3.5、GPT 4 或 Davinci 模型）。
- 一个运行时与计算实例以运行评估。

## 内置评估指标

Azure AI Studio 允许您评估单轮和复杂的多轮对话。在检索增强生成（RAG）场景中，模型基于特定数据，您可以使用内置评估指标来评估性能。此外，您还可以评估一般的单轮问答场景（非 RAG）。

## 创建评估运行

在 Azure AI Studio UI 中，导航到评估页面或提示流页面。按照评估创建向导设置评估运行。为您的评估提供一个可选名称。选择与您的应用程序目标一致的场景。选择一个或多个评估指标来评估模型的输出。

## 自定义评估流程（可选）

为了更大的灵活性，您可以建立一个自定义评估流程。根据您的特定需求自定义评估过程。

## 查看结果

运行评估后，在 Azure AI Studio 中记录、查看和分析详细的评估指标。深入了解您的应用程序的能力和局限性。

**注意** Azure AI Studio 目前处于公开预览阶段，因此请将其用于实验和开发目的。对于生产工作负载，请考虑其他选项。探索官方 [AI Studio 文档](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) 以获取更多详细信息和分步说明。