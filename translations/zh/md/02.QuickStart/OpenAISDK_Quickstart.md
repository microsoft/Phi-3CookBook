# 在 Azure AI 和 Azure ML 中使用 OpenAI SDK 与 Phi-3

使用 `openai` SDK 来消费 Azure AI 和 Azure ML 中的 Phi-3 部署。Azure AI 和 Azure ML 中的 Phi-3 模型系列提供了与 OpenAI Chat Completion API 兼容的 API。这使得客户和用户可以从 OpenAI 模型无缝过渡到 Phi-3 大型语言模型。

该 API 可以直接与 OpenAI 的客户端库或第三方工具（如 LangChain 或 LlamaIndex）一起使用。

下面的例子展示了如何使用 OpenAI Python 库进行这种过渡。请注意，Phi-3 仅支持聊天完成 API。

要使用 OpenAI SDK 与 Phi-3 模型，您需要按照几个步骤来设置您的环境并进行 API 调用。以下是帮助您入门的指南：

1. **安装 OpenAI SDK**：首先，如果您还没有安装 OpenAI Python 包，则需要安装它。
   ```bash
   pip install openai
   ```

2. **设置您的 API 密钥**：确保您拥有 OpenAI API 密钥。您可以在环境变量中或直接在代码中设置它。
   ```python
   import openai

   openai.api_key = "your-api-key"
   ```

3. **进行 API 调用**：使用 OpenAI SDK 与 Phi-3 模型进行交互。以下是一个进行完成请求的示例：
   ```python
   response = openai.Completion.create(
       model="phi-3",
       prompt="Hello, how are you?",
       max_tokens=50
   )

   print(response.choices[0].text.strip())
   ```

4. **处理响应**：根据您的应用需求处理模型的响应。

这是一个更详细的示例：
```python
import openai

# Set your API key
openai.api_key = "your-api-key"

# Define the prompt
prompt = "Write a short story about a brave knight."

# Make the API call
response = openai.Completion.create(
    model="phi-3",
    prompt=prompt,
    max_tokens=150
)

# Print the response
print(response.choices[0].text.strip())
```

这将根据提供的提示生成一个短篇故事。您可以调整 `max_tokens` 参数来控制输出的长度。

[查看 Phi-3 模型的完整 Notebook 示例](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/openaisdk.ipynb)

查看 [文档](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo)，了解 AI Studio 和 ML Studio 中 Phi-3 模型系列的详细信息，包括如何配置推理端点、区域可用性、定价和推理架构参考。

**免责声明**：
本文档使用基于机器的人工智能翻译服务进行翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。应将原文档的母语版本视为权威来源。对于关键信息，建议进行专业人工翻译。我们对使用此翻译而产生的任何误解或误读不承担责任。