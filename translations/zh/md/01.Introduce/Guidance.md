### Guidance-AI 和 Phi 模型即服务 (MaaS)
我们将 [Guidance](https://github.com/guidance-ai/guidance) 引入 Azure AI Studio 中的 Phi-3.5-mini 无服务器端点，通过定义应用程序所需的结构，使输出更加可预测。借助 Guidance，你可以避免昂贵的重试，并可以例如约束模型从预定义列表中选择（如医疗代码），限制输出为提供的上下文中的直接引用，或遵循任何正则表达式。Guidance 在推理堆栈中逐字节引导模型，降低 30-50% 的成本和延迟，使其成为 [Phi-3-mini 无服务器端点](https://aka.ms/try-phi3.5mini) 的独特且有价值的附加组件。

## [**Guidance-AI**](https://github.com/guidance-ai/guidance) 是一个帮助开发人员高效创建和部署 AI 模型的框架。它专注于提供构建健壮 AI 应用程序的工具和最佳实践。

当与 **Phi 模型即服务 (MaaS)** 结合时，它为部署既经济高效又高性能的小型语言模型 (SLM) 提供了强大的解决方案。

**Guidance-AI** 是一个编程框架，旨在帮助开发人员更有效地控制和引导大型语言模型 (LLM)。它允许精确地结构化输出，与传统提示或微调方法相比，减少延迟和成本。

### Guidance-AI 的主要特点：
- **高效控制**：使开发人员能够控制语言模型生成文本的方式，确保高质量和相关的输出。
- **成本和延迟减少**：优化生成过程，更加经济高效和快速。
- **灵活集成**：支持多种后端，包括 Transformers、llama.cpp、AzureAI、VertexAI 和 OpenAI。
- **丰富的输出结构**：支持复杂的输出结构，如条件语句、循环和工具使用，使生成清晰且可解析的结果变得更容易。
- **兼容性**：允许单个 Guidance 程序在多个后端上执行，增强了灵活性和易用性。

### 示例用例：
- **约束生成**：使用正则表达式和上下文无关文法来引导模型的输出。
- **工具集成**：自动交替控制和生成，例如在文本生成任务中使用计算器。

有关更多详细信息和示例，你可以查看 [Guidance-AI GitHub 仓库](https://github.com/guidance-ai/guidance)。

[查看 Phi-3.5 示例](../../../../code/01.Introduce/guidance.ipynb)

### Phi 模型的主要特点：
1. **经济高效**：在保持高性能的同时设计为经济实惠。
2. **低延迟**：适用于需要快速响应的实时应用程序。
3. **灵活性**：可以在各种环境中部署，包括云端、边缘和离线场景。
4. **定制化**：可以使用特定领域的数据进行微调，以提升性能。
5. **安全与合规**：基于微软的 AI 原则构建，确保责任、透明、公平、可靠、安全、隐私和包容性。

### Phi 模型即服务 (MaaS)：
Phi 模型通过推理 API 以按需付费的方式提供，使其能够轻松集成到你的应用程序中，而无需大量前期成本。

### 开始使用 Phi-3：
要开始使用 Phi 模型，你可以探索 [Azure AI 模型目录](https://ai.azure.com/explore/models) 或 [GitHub Marketplace Models](https://github.com/marketplace/models)，这些平台提供预构建和可定制的模型。此外，你还可以使用 [Azure AI Studio](https://ai.azure.com) 开发和部署你的 AI 应用程序。

### 资源
[Guidance 入门示例笔记本](../../../../code/01.Introduce/guidance.ipynb)

免责声明：此翻译由AI模型从原文翻译而来，可能不够完美。请审核输出内容并进行必要的修正。