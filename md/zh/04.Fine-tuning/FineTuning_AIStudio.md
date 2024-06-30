# 使用 Azure AI Studio 微调 Phi-3

接下来我们要探索如何使用 Azure AI Studio 微调微软的 Phi-3 Mini 语言模型。微调可以让 Phi-3 Mini 适应特定任务，使其更加强大并具有上下文感知能力。

## 考虑因素：

- **功能：** 哪些模型可以微调？基础模型可以被微调成什么样子？
- **成本：** 微调的定价是如何计算的？
- **可定制性：** 我可以在多大程度上修改基础模型，并且以及以何种方式修改？
- **便捷性：** 如何进行微调，我需要自己编写代码吗？我需要自带计算资源吗？
- **安全性：** 已知微调模型存在安全风险，是否有任何防护措施来防止产生意外的结果？

![AIStudio Models](../../imgs/05/AIStudio/AIStudioModels.png)

以下是微调的步骤：

## 使用 Azure AI Studio 微调 Phi-3

![Finetune AI Studio](../../imgs/05/AIStudio/AIStudiofinetune.png)

**设置您的环境**

Azure AI Studio：如果您还没有，请登录 [Azure AI Studio](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo)。

**创建一个新项目**

点击“新建”，创建一个新项目。根据您的使用情况选择合适的设置。

![FineTuneSelect](../../imgs/05/AIStudio/AIStudiofinetuneselect.png)
### 数据准备

**数据集选择**

收集或创建与任务相关的数据集。这可以是聊天指令、问答对或任何相关的文本数据。

选择数据集

![FineTuneSelect](../../imgs/05/AIStudio/AIStudiofintunetask.png)

选择您的数据集

![FinetuneDataSelect](../../imgs/05/AIStudio/AIStudiodatafintuneselect.png)

预览数据集

![Finetuneselect](../../imgs/05/AIStudio/AIStudiofinetunepreview.png)

**高级使用**

![FineTuneAdvanced](../../imgs/05/AIStudio/AIStudiofinetuneadvanced.png)

**数据预处理**

清理和预处理您的数据。去除噪音，处理缺失值并对文本进行分词。

## 模型选择

**Phi-3 Mini**

您将微调预训练的 Phi-3 Mini 模型。确保您有模型检查点的访问权限（例如 "microsoft/Phi-3-mini-4k-instruct"）。

**微调配置**

超参数：定义超参数，如学习率、批量大小和训练轮数。

**损失函数**

为您的任务选择合适的损失函数（例如，交叉熵）。

**优化器**

选择一个优化器（例如，Adam）用于训练过程中的梯度更新。

**微调过程**

- 加载预训练模型：加载 Phi-3 Mini 检查点。
- 添加自定义层：添加任务特定的层（例如，聊天指令的分类头）。

**训练模型**

使用您准备好的数据集微调模型。监控训练进度并根据需要调整超参数。

**评估和验证**

验证集：将数据分为训练集和验证集。

**评估性能**

使用准确率、F1 分数或困惑度等指标来评估模型性能。

## 保存微调模型

**检查点**

保存微调后的模型检查点以供将来使用。

## 部署

- 部署为 Web 服务：将微调后的模型部署为 Azure AI Studio 中的 Web 服务。
- 测试端点：向部署的端点发送测试查询以验证其功能。

## 迭代和改进

迭代：如果性能不理想，通过调整超参数、增加数据或进行额外的微调轮次来迭代改进。

## 监控和优化

持续监控模型的行为并根据需要进行优化。

## 定制和扩展

自定义任务：Phi-3 Mini 可以微调用于各种任务，不仅限于聊天指令。探索其他用例！
实验：尝试不同的架构、层组合和技术以增强性能。

***注意***：微调是一个迭代过程。实验、学习并调整您的模型，以实现特定任务的最佳结果！