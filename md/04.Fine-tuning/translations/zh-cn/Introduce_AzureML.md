# **介绍 Azure Machine Learning 服务**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) 是一个加速和管理机器学习（ML）项目生命周期的云服务。

ML 专业人士、数据科学家和工程师可以在日常工作流程中使用它来： 

- 训练和部署模型。管理机器学习操作（MLOps）。
- 您可以在Azure Machine Learning中创建一个模型，或者使用来自开源平台（如 PyTorch、TensorFlow 或 scikit-learn）的模型。 
- MLOps 工具可以帮助您监控、重新训练和重新部署模型。

## Azure Machine Learning服务于谁？

**数据科学家和 ML 工程师**
他们可以使用工具来加速和自动化日常工作流程。Azure ML 为公平性、可解释性、跟踪和审计性提供了功能。

**Application Developers**
他们可以无缝地将模型集成到应用程序或服务中。

**平台开发人员**
他们可以使用一套由稳定的 Azure 资源管理器 API 支持的强大工具。这些工具允许构建高级 ML 工具。

**企业**
在 Microsoft Azure 云中工作的企业可以从熟悉的安全性和基于角色的访问控制中受益。设置项目以控制对受保护数据和特定操作的访问。

## 团队中每个人的生产力
机器学习项目通常需要具有不同技能组合的团队来构建和维护。

Azure ML 提供了使您能够完成以下任务的工具：
- 通过共享笔记本、计算资源、无服务器计算、数据和环境与团队协作。
- 以公平、可解释性、跟踪和审计性来开发模型，以满足溯源和审计合规的要求。
- 使用 MLOps 快速轻松地大规模部署机器学习模型，并高效地管理和监管它们。
- 在任何地方运行具有内置治理、安全性和合规性的机器学习工作负载。


## 跨兼容平台工具

机器学习团队中的任何人都可以使用他们喜欢的工具来完成工作。
无论您是进行快速实验、超参数调优、构建管道还是管理推理，您都可以使用熟悉的界面，包括：
- Azure Machine Learning Studio
- Python SDK (v2)
- Azure CLI (v2)
- Azure Resource Manager REST APIs

在整个开发周期中，您可以在 Azure Machine Learning studio UI 中优化模型、协作、共享和查找资产、资源和指标。

## **Azure ML 中的 LLM/SLM**

Azure ML 已经添加了许多与 LLM/SLM 相关的功能，将 LLMOps 和 SLMOps 结合起来，创建了一个企业级生成式人工智能技术平台。

### **模型目录**

企业用户可以通过模型目录根据不同的业务场景部署不同的模型，并为企业开发人员或用户提供 Model as Service 的服务以供访问。

![models](../../../../imgs/04/03/models.png)

Azure Machine Learning studio中的模型目录是发现和使用各种模型的中心，这些模型使您能够构建生成式 AI 应用程序。模型目录包含了数百种来自不同模型提供商的模型，如 Azure OpenAI 服务、Mistral、Meta、Cohere、Nvidia 和 Hugging Face，包括 Microsoft 训练的模型。除 Microsoft 之外的其他提供商的模型属于非 Microsoft 产品，按照 Microsoft 产品条款中的定义，受模型所附带的条款约束。


### **任务管道**

机器学习管道的核心是将一个完整的机器学习任务拆分为多步骤工作流程。每个步骤都是一个可管理的组件，可以单独进行开发、优化、配置和自动化。步骤通过明确的接口相互连接。Azure Machine Learning 管道服务自动协调管道步骤之间的所有依赖关系。

在微调 SLM / LLM 时，我们可以通过管道管理我们的数据、训练和生成过程。

![finetuning](../../../../imgs/04/03/finetuning.png)


### **提示流**

使用 Azure Machine Learning 提示流的好处：Azure Machine Learning 提示流提供了一系列好处，帮助用户从构思过渡到实验，最终实现基于 LLM 的用于生产的应用程序:

**提示工程敏捷性**

交互式创作体验：Azure Machine Learning 提示流提供了流程结构的可视化表示，使用户能够轻松理解和浏览他们的项目。它还提供了类似于Jupyter notebook的编码体验，以实现高效的流程开发和调试。

提示调整的变体：用户可以创建并比较多个提示变体，促进迭代优化过程。

评估：内置评估流程使用户能够评估他们的提示和流程的质量和有效性。

综合资源：Azure Machine Learning 提示流包括一套内置的工具、样本和模板库，作为开发的起点，激发创意并加速过程。

**基于 LLM 的应用程序的企业准备情况**

协作：Azure Machine Learning 提示流支持团队协作，允许多个用户共同参与提示工程项目，共享知识并保持版本控制。

一站式平台：Azure Machine Learning 提示流简化了整个提示工程过程，从开发和评估到部署和监控。用户可以轻松地将流程部署为 Azure Machine Learning 端点，并实时监控其性能，确保最佳运行和持续改进。

Azure Machine Learning 企业就绪解决方案：提示流利用 Azure Machine Learning 强大的企业就绪解决方案，为流程的开发、实验和部署提供安全、可扩展和可靠的基础。

借助 Azure Machine Learning 提示流，用户可以释放他们的提示工程敏捷性，有效协作，并利用企业级解决方案实现成功的基于 LLM 的应用程序开发和部署。

通过整合 Azure ML 的计算能力、数据和不同组件，企业开发者可以轻松构建自己的人工智能应用程序。
