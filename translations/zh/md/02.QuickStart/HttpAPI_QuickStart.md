# 使用 Azure API 与 Phi-3

本笔记本展示了如何使用 Microsoft Azure AI 和 Azure ML 提供的 Phi-3 API 的示例。我们将涵盖以下内容：
* 在 CLI 中使用 HTTP 请求 API 调用 Phi-3 预训练和聊天模型
* 在 Python 中使用 HTTP 请求 API 调用 Phi-3 预训练和聊天模型

当然，以下是 **在 CLI 中使用 HTTP 请求 API 的概述**：

## 在 CLI 中使用 HTTP 请求 API

### 基础知识

要使用 REST API，您需要拥有与该端点关联的端点 URL 和身份验证密钥。这些可以从之前的步骤中获取。

在这个聊天完成示例中，我们使用一个简单的 `curl` 调用来进行说明。主要有三个组件：

1. **`host-url`**：这是您的端点 URL，带有聊天完成模式 `/v1/chat/completions`。
2. **`headers`**：这定义了内容类型以及您的 API 密钥。
3. **`payload` 或 `data`**：这包括您的提示详情和模型超参数。

### 示例

以下是使用 `curl` 进行聊天完成请求的示例：

```bash
curl -X POST https://api.example.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_API_KEY" \
-d '{
  "model": "phi-3",
  "messages": [{"role": "user", "content": "Hello, how are you?"}],
  "max_tokens": 50
}'
```

### 细分

- **`-X POST`**: Specifies the HTTP method to use, which is POST in this case.
- **`https://api.example.com/v1/chat/completions`**: The endpoint URL.
- **`-H "Content-Type: application/json"`**: Sets the content type to JSON.
- **`-H "Authorization: Bearer YOUR_API_KEY"`**: Adds the authorization header with your API key.
- **`-d '{...}'`**: The data payload, which includes the model, messages, and other parameters.

### Tips

- **Endpoint URL**: Ensure you replace `https://api.example.com` with your actual endpoint URL.
- **API Key**: Replace `YOUR_API_KEY` 用您的实际 API 密钥替换 YOUR_API_KEY。
- **有效负载**：根据您的需求自定义有效负载，包括不同的提示、模型和参数。

参见示例 [Http Connections and Streaming](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/webrequests.ipynb)

查看 [文档](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo&tabs=phi-3-mini&pivots=programming-language-rest) 了解 AI Studio 和 ML Studio 中 Phi-3 模型家族的详细信息，包括如何提供推理端点、区域可用性、定价和推理模式参考。

**免责声明**：
本文档是使用基于机器的人工智能翻译服务翻译的。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对使用本翻译引起的任何误解或误释承担责任。