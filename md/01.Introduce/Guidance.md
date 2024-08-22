### Guidance-AI and Phi Models as a Service (MaaS)

[**Guidance-AI**](https://github.com/guidance-ai/guidance) is a framework designed to help developers create and deploy AI models efficiently. It focuses on providing tools and best practices for building robust AI applications. 

When combined with **Phi Models as a Service (MaaS)**, it offers a powerful solution for deploying small language models (SLMs) that are both cost-effective and high-performing.

**Guidance-AI** is a programming framework designed to help developers control and steer large language models (LLMs) more effectively. It allows for precise structuring of outputs, reducing latency and cost compared to traditional prompting or fine-tuning methods¹.

### Key Features of Guidance-AI:
- **Efficient Control**: Enables developers to control how the language model generates text, ensuring high-quality and relevant outputs.
- **Cost and Latency Reduction**: Optimizes the generation process to be more cost-effective and faster.
- **Flexible Integration**: Works with various backends, including Transformers, llama.cpp, AzureAI, VertexAI, and OpenAI.
- **Rich Output Structures**: Supports complex output structures like conditionals, loops, and tool use, making it easier to generate clear and parsable results.
- **Compatibility**: Allows a single Guidance program to be executed on multiple backends, enhancing flexibility and ease of use.

### Example Use Cases:
- **Constrained Generation**: Using regular expressions and context-free grammars to guide the model's output.
- **Tool Integration**: Automatically interleaving control and generation, such as using a calculator within a text generation task.

For more detailed information and examples, you can check out the [Guidance-AI GitHub repository](https://github.com/guidance-ai/guidance).

[Check out the Phi-3.5 Sample](../../code/01.Introduce/guidance.ipynb)

### Key Features of Phi Models:
1. **Cost-Effective**: Designed to be affordable while maintaining high performance.
2. **Low Latency**: Ideal for real-time applications requiring quick responses.
3. **Flexibility**: Can be deployed in various environments, including cloud, edge, and offline scenarios.
4. **Customization**: Models can be fine-tuned with domain-specific data to enhance performance.
5. **Security and Compliance**: Built with Microsoft's AI principles, ensuring accountability, transparency, fairness, reliability, safety, privacy, and inclusiveness.

### Phi Models as a Service (MaaS):
Phi models are available through a pay-as-you-go billing system via inference APIs, making it easy to integrate them into your applications without significant upfront costs.

### Getting Started with Phi-3:
To start using Phi models, you can explore the [Azure AI model catalog](https://ai.azure.com/explore/models) or the GitHub Marketplace Models](https://github.com/marketplace/models) which offers prebuilt and customizable models. Additionally, you can use tools like [Azure AI Studio](https://ai.azure.com) to develop and deploy your AI applications.

### Resources
[Sample Notebook on getting started with Guidance](../../code/01.Introduce/guidance.ipynb)