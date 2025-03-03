# 使用 Azure AI Foundry 微调 Phi-3

让我们探索如何使用 Azure AI Foundry 微调 Microsoft 的 Phi-3 Mini 语言模型。通过微调，您可以将 Phi-3 Mini 适配到特定任务，使其更加强大和具有上下文感知能力。

## 注意事项

- **能力：** 哪些模型可以进行微调？基础模型可以被微调成什么样？
- **成本：** 微调的定价模式是什么？
- **定制化：** 我可以在多大程度上修改基础模型？可以以什么方式修改？
- **便利性：** 微调过程是如何进行的？我需要编写自定义代码吗？需要自己提供计算资源吗？
- **安全性：** 微调后的模型可能存在安全风险——是否有任何防护措施来防止意外的伤害？

![AIFoundry Models](../../../../translated_images/AIFoundryModels.4440430c9f07dbd6c625971422e7b9a5b9cb91fa046e447ba9ea41457860532f.zh.png)

## 微调准备工作

### 先决条件

> [!NOTE]  
> 对于 Phi-3 系列模型，按需付费的微调服务仅适用于在 **East US 2** 区域创建的 Hub。

- 一个 Azure 订阅。如果您还没有 Azure 订阅，可以创建一个 [付费 Azure 帐户](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) 开始使用。

- 一个 [AI Foundry 项目](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo)。  
- Azure 基于角色的访问控制 (Azure RBAC) 用于授予 Azure AI Foundry 操作的访问权限。要执行本文中的步骤，您的用户帐户必须被分配为资源组上的 __Azure AI Developer 角色__。

### 订阅提供程序注册

验证订阅是否已注册到 `Microsoft.Network` 资源提供程序。

1. 登录 [Azure 门户](https://portal.azure.com)。  
1. 从左侧菜单中选择 **订阅**。  
1. 选择您想使用的订阅。  
1. 从左侧菜单中选择 **AI 项目设置** > **资源提供程序**。  
1. 确认 **Microsoft.Network** 是否在资源提供程序列表中。如果没有，请添加它。

### 数据准备

准备您的训练和验证数据来微调模型。您的训练数据和验证数据集应包括输入和输出示例，以展示您希望模型如何表现。

确保所有训练示例符合推理的预期格式。为了有效地微调模型，请确保数据集平衡且多样化。

这涉及维护数据平衡、涵盖各种场景，并定期优化训练数据以符合现实世界的期望，从而最终实现更准确和平衡的模型响应。

不同的模型类型需要不同格式的训练数据。

### 聊天补全

您使用的训练和验证数据**必须**格式化为 JSON Lines (JSONL) 文档。对于 `Phi-3-mini-128k-instruct`，微调数据集必须采用聊天补全 API 使用的对话格式。

### 示例文件格式

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

支持的文件类型为 JSON Lines。文件将上传到默认数据存储并在您的项目中可用。

## 使用 Azure AI Foundry 微调 Phi-3

Azure AI Foundry 通过微调过程让您能够根据个人数据集定制大型语言模型。微调通过实现特定任务和应用的定制化和优化，带来了显著的价值。这可以提高性能、降低成本、减少延迟，并提供定制化的输出。

![Finetune AI Foundry](../../../../translated_images/AIFoundryfinetune.69ddc22d1ab08167a7e53a911cd33c749d99fea4047801a836ceb6eec66c5719.zh.png)

### 创建新项目

1. 登录 [Azure AI Foundry](https://ai.azure.com)。

1. 选择 **+新建项目** 来在 Azure AI Foundry 中创建一个新项目。

    ![FineTuneSelect](../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.zh.png)

1. 执行以下任务：

    - 项目 **Hub 名称**。必须是唯一值。  
    - 选择要使用的 **Hub**（如有需要可创建一个新的）。

    ![FineTuneSelect](../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.zh.png)

1. 执行以下任务以创建新的 Hub：

    - 输入 **Hub 名称**。必须是唯一值。  
    - 选择您的 Azure **订阅**。  
    - 选择要使用的 **资源组**（如有需要可创建一个新的）。  
    - 选择您希望使用的 **位置**。  
    - 选择要使用的 **连接 Azure AI 服务**（如有需要可创建一个新的）。  
    - 选择 **连接 Azure AI 搜索** 并选择 **跳过连接**。

    ![FineTuneSelect](../../../../translated_images/create-hub.b93d390a6d3eebd4c33eb7e4ea6ef41fd69c4d39f21339d4bda51af9ed70505f.zh.png)

1. 选择 **下一步**。  
1. 选择 **创建项目**。

### 数据准备

在微调之前，收集或创建与您的任务相关的数据集，例如聊天指令、问答对或其他相关文本数据。通过清理和预处理这些数据来去除噪音、处理缺失值并对文本进行分词。

### 在 Azure AI Foundry 中微调 Phi-3 模型

> [!NOTE]  
> Phi-3 模型的微调目前仅支持在 East US 2 区域的项目中。

1. 从左侧标签中选择 **模型目录**。

1. 在 **搜索栏** 中输入 *phi-3* 并选择您想使用的 phi-3 模型。

    ![FineTuneSelect](../../../../translated_images/select-model.02eef2cbb5b7e61a86526b05bd5ec9822fd6b2abae4e38fd5d9bdef541dfb967.zh.png)

1. 选择 **微调**。

    ![FineTuneSelect](../../../../translated_images/select-finetune.88cf562034f78baf0b7f41511fd4c45e1f068104238f1397661b9402ff9e2e09.zh.png)

1. 输入 **微调后的模型名称**。

    ![FineTuneSelect](../../../../translated_images/finetune1.8a20c66f797cc7ede7feb789a45c42713b7aeadfeb01dbc34446019db5c189d4.zh.png)

1. 选择 **下一步**。

1. 执行以下任务：

    - 选择 **任务类型** 为 **聊天补全**。  
    - 选择您想使用的 **训练数据**。您可以通过 Azure AI Foundry 的数据或从本地环境上传。

    ![FineTuneSelect](../../../../translated_images/finetune2.47df1aa177096dbaa01e4d64a06eb3f46a29718817fa706167af3ea01419a32f.zh.png)

1. 选择 **下一步**。

1. 上传您想使用的 **验证数据**，或者选择 **自动拆分训练数据**。

    ![FineTuneSelect](../../../../translated_images/finetune3.e887e47240626c31f969532610c965594635c91cf3f94639fa60fb5d2bbd8f93.zh.png)

1. 选择 **下一步**。

1. 执行以下任务：

    - 选择您想使用的 **批量大小倍数**。  
    - 选择您想使用的 **学习率**。  
    - 选择您想使用的 **训练轮数**。

    ![FineTuneSelect](../../../../translated_images/finetune4.9f47c2fad66fddd0f091b62a2fa6ac23260226ab841287805d843ebc83761801.zh.png)

1. 选择 **提交** 开始微调过程。

    ![FineTuneSelect](../../../../translated_images/select-submit.b5344fd77e49bfb6d4efe72e713f6a46f04323d871c118bbf59bf0217698dfee.zh.png)

1. 一旦您的模型完成微调，状态将显示为 **已完成**，如下图所示。现在，您可以部署模型并在自己的应用程序中、在 playground 或在 prompt flow 中使用它。有关更多信息，请参阅 [如何使用 Azure AI Foundry 部署 Phi-3 系列的小型语言模型](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python)。

    ![FineTuneSelect](../../../../translated_images/completed.f4be2c6e660d8ba908d1d23e2102925cc31e57cbcd60fb10e7ad3b7925f585c4.zh.png)

> [!NOTE]  
> 有关微调 Phi-3 的更多详细信息，请访问 [在 Azure AI Foundry 中微调 Phi-3 模型](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini)。

## 清理微调后的模型

您可以从 [Azure AI Foundry](https://ai.azure.com) 的微调模型列表或从模型详细信息页面删除微调后的模型。在微调页面选择要删除的微调模型，然后点击删除按钮以删除该模型。

> [!NOTE]  
> 如果自定义模型有现有部署，则无法删除该模型。您必须先删除模型部署，才能删除自定义模型。

## 成本和配额

### Phi-3 模型微调服务的成本和配额注意事项

作为服务提供的 Phi 模型由 Microsoft 提供，并与 Azure AI Foundry 集成使用。您可以在[部署](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python)或微调模型时，在部署向导的“定价和条款”选项卡下找到定价信息。

## 内容过滤

以按需付费方式部署为服务的模型受到 Azure AI 内容安全的保护。当部署到实时终端时，您可以选择退出此功能。启用 Azure AI 内容安全后，提示和生成结果都将通过一组分类模型，用于检测和防止输出有害内容。内容过滤系统会检测并对输入提示和输出结果中的潜在有害内容类别采取行动。了解更多关于 [Azure AI 内容安全](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering)。

**微调配置**

超参数：定义超参数，例如学习率、批量大小和训练轮数。

**损失函数**

为您的任务选择适当的损失函数（例如交叉熵）。

**优化器**

选择优化器（例如 Adam）以在训练期间更新梯度。

**微调过程**

- 加载预训练模型：加载 Phi-3 Mini 检查点。  
- 添加自定义层：添加任务特定的层（例如用于聊天指令的分类头）。

**训练模型**  
使用准备好的数据集微调模型。监控训练进度并根据需要调整超参数。

**评估与验证**

验证集：将数据分为训练集和验证集。

**评估性能**

使用准确率、F1 分数或困惑度等指标评估模型性能。

## 保存微调后的模型

**检查点**  
保存微调后的模型检查点以供未来使用。

## 部署

- 部署为 Web 服务：将微调后的模型部署为 Azure AI Foundry 中的 Web 服务。  
- 测试终端：向部署的终端发送测试查询以验证其功能。

## 迭代与改进

迭代：如果性能不令人满意，通过调整超参数、添加更多数据或进行额外轮数的微调来进行迭代。

## 监控与优化

持续监控模型的行为并根据需要进行优化。

## 定制与扩展

自定义任务：Phi-3 Mini 可以微调用于聊天指令以外的各种任务。探索其他用例！  
实验：尝试不同的架构、层组合和技术来增强性能。

> [!NOTE]  
> 微调是一个迭代的过程。实验、学习并调整您的模型，以实现针对特定任务的最佳结果！

**免责声明**：  
本文件通过基于机器的人工智能翻译服务进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文的母语版本作为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而导致的任何误解或误读，我们概不负责。