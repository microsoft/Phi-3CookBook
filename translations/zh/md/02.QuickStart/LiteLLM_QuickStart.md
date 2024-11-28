使用 [LiteLLM](https://docs.litellm.ai/) 配合 Phi-3 模型是一个不错的选择，特别是如果你想将其整合到各种应用程序中。LiteLLM 充当中间件，将 API 调用转换为兼容不同模型（包括 Phi-3）的请求。

Phi-3 是微软开发的小型语言模型（SLM），旨在高效运行于资源受限的机器上。它可以在支持 AVX 的 CPU 和仅 4 GB RAM 的情况下运行，非常适合在不需要 GPU 的本地推理。

以下是使用 LiteLLM 配合 Phi-3 的一些步骤：

1. **安装 LiteLLM**：你可以使用 pip 安装 LiteLLM：
   ```bash
   pip install litellm
   ```

2. **设置环境变量**：配置你的 API 密钥和其他必要的环境变量。
   ```python
   import os
   os.environ["OPENAI_API_KEY"] = "your-api-key"
   ```

3. **进行 API 调用**：使用 LiteLLM 对 Phi-3 模型进行 API 调用。
   ```python
   from litellm import completion

   response = completion(
       model="phi-3",
       messages=[{"role": "user", "content": "Hello, how are you?"}]
   )
   print(response)
   ```

4. **集成**：你可以将 LiteLLM 集成到各种平台，如 Nextcloud Assistant，允许你使用 Phi-3 进行文本生成和其他任务。

**LLMLite 完整代码示例**
[LLMLite 示例代码笔记本](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/litellm.ipynb)

**免责声明**：
本文档使用基于机器的人工智能翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误释承担责任。