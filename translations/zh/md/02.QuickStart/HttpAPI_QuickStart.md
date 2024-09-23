# 使用 Azure API 与 Phi-3

本笔记本展示了如何使用 Microsoft Azure AI 和 Azure ML 提供的 Phi-3 API。我们将涵盖以下内容：
* 在 CLI 中使用 HTTP 请求 API 调用 Phi-3 预训练和聊天模型
* 在 Python 中使用 HTTP 请求 API 调用 Phi-3 预训练和聊天模型

以下是 **在 CLI 中使用 HTTP 请求 API** 的概述：

## 在 CLI 中使用 HTTP 请求 API

### 基础

要使用 REST API，你需要有一个端点 URL 和与该端点关联的认证密钥。这些可以从之前的步骤中获取。

在这个聊天完成示例中，我们使用一个简单的 `curl` 调用进行演示。主要有三个组成部分：

1. **`host-url`**：这是你的端点 URL，包含聊天完成的路径 `/v1/chat/completions`。
2. **`headers`**：这定义了内容类型以及你的 API 密钥。
3. **`payload` 或 `data`**：这包括你的提示详情和模型超参数。

### 示例

以下是如何使用 `curl` 发起一个聊天完成请求的示例：

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

### 解析

- **`-X POST`**：指定要使用的 HTTP 方法，这里是 POST。
- **`https://api.example.com/v1/chat/completions`**：端点 URL。
- **`-H "Content-Type: application/json"`**：设置内容类型为 JSON。
- **`-H "Authorization: Bearer YOUR_API_KEY"`**：添加带有你的 API 密钥的认证头。
- **`-d '{...}'`**：数据负载，包括模型、消息和其他参数。

### 提示

- **端点 URL**：确保将 `https://api.example.com` 替换为你的实际端点 URL。
- **API 密钥**：将 `YOUR_API_KEY` 替换为你的实际 API 密钥。
- **负载**：根据你的需求自定义负载，包括不同的提示、模型和参数。

请参阅示例 [Http Connections and Streaming](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/webrequests.ipynb)

查阅 [文档](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo&tabs=phi-3-mini&pivots=programming-language-rest)，了解 AI Studio 和 ML Studio 中 Phi-3 模型系列的详细信息，包括如何配置推理端点、区域可用性、定价和推理模式参考。

免责声明：此翻译由AI模型从原文翻译而来，可能并不完美。
请审查输出并进行必要的修改。