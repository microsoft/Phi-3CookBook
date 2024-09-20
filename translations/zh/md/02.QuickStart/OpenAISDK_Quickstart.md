# 使用 OpenAI SDK 在 Azure AI 和 Azure ML 中调用 Phi-3

使用 `openai` SDK 来调用 Azure AI 和 Azure ML 中的 Phi-3 部署。Azure AI 和 Azure ML 中的 Phi-3 模型系列提供了与 OpenAI Chat Completion API 兼容的 API，使客户和用户能够从 OpenAI 模型无缝过渡到 Phi-3 LLMs。

该 API 可以直接与 OpenAI 的客户端库或第三方工具（如 LangChain 或 LlamaIndex）一起使用。

下面的示例展示了如何使用 OpenAI Python 库进行这种过渡。注意，Phi-3 仅支持聊天完成 API。

要使用 OpenAI SDK 调用 Phi-3 模型，您需要按照以下步骤设置环境并进行 API 调用。以下是帮助您入门的指南：

1. **安装 OpenAI SDK**：首先，如果尚未安装 OpenAI Python 包，需要进行安装。
   ```bash
   pip install openai
   ```

2. **设置 API 密钥**：确保您拥有 OpenAI API 密钥。可以在环境变量中或直接在代码中进行设置。
   ```python
   import openai

   openai.api_key = "your-api-key"
   ```

3. **进行 API 调用**：使用 OpenAI SDK 与 Phi-3 模型交互。以下是一个完成请求的示例：
   ```python
   response = openai.Completion.create(
       model="phi-3",
       prompt="Hello, how are you?",
       max_tokens=50
   )

   print(response.choices[0].text.strip())
   ```

4. **处理响应**：根据您的应用需求处理模型的响应。

以下是一个更详细的示例：
```python
import openai

# 设置您的 API 密钥
openai.api_key = "your-api-key"

# 定义提示
prompt = "Write a short story about a brave knight."

# 进行 API 调用
response = openai.Completion.create(
    model="phi-3",
    prompt=prompt,
    max_tokens=150
)

# 打印响应
print(response.choices[0].text.strip())
```

这将根据提供的提示生成一个简短的故事。您可以调整 `max_tokens` 参数来控制输出的长度。

[查看 Phi-3 模型的完整 Notebook 示例](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/openaisdk.ipynb)

查阅 [Phi-3 模型系列文档](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo)，了解 AI Studio 和 ML Studio 中如何配置推理端点、区域可用性、定价和推理模式参考的详细信息。

免责声明：本翻译由AI模型从原文翻译而来，可能并不完美。请审阅输出并进行必要的修改。