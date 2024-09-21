# 使用 Azure API 和 Phi-3

這個筆記本展示了如何使用 Microsoft Azure AI 和 Azure ML 提供的 Phi-3 API。我們將涵蓋以下內容：
* 在 CLI 中使用 HTTP 請求 API 來操作 Phi-3 預訓練和聊天模型
* 在 Python 中使用 HTTP 請求 API 來操作 Phi-3 預訓練和聊天模型

以下是 **在 CLI 中使用 HTTP 請求 API** 的概述：

## 在 CLI 中使用 HTTP 請求 API

### 基本概念

要使用 REST API，你需要一個 Endpoint URL 和與該端點相關的驗證金鑰。這些可以從之前的步驟中獲取。

在這個聊天完成範例中，我們使用一個簡單的 `curl` 呼叫來說明。有三個主要組成部分：

1. **`host-url`**：這是你的端點 URL，帶有聊天完成的路徑 `/v1/chat/completions`。
2. **`headers`**：這定義了內容類型以及你的 API 金鑰。
3. **`payload` 或 `data`**：這包括你的提示詳細信息和模型超參數。

### 範例

以下是一個使用 `curl` 進行聊天完成請求的範例：

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

- **`-X POST`**：指定要使用的 HTTP 方法，在這個例子中是 POST。
- **`https://api.example.com/v1/chat/completions`**：端點 URL。
- **`-H "Content-Type: application/json"`**：將內容類型設置為 JSON。
- **`-H "Authorization: Bearer YOUR_API_KEY"`**：添加帶有你的 API 金鑰的授權標頭。
- **`-d '{...}'`**：數據負載，包括模型、消息和其他參數。

### 提示

- **端點 URL**：確保將 `https://api.example.com` 替換為你的實際端點 URL。
- **API 金鑰**：將 `YOUR_API_KEY` 替換為你的實際 API 金鑰。
- **數據負載**：根據你的需求自定義數據負載，包括不同的提示、模型和參數。

參見範例 [Http Connections and Streaming](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/webrequests.ipynb)

查看 [documentation](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo&tabs=phi-3-mini&pivots=programming-language-rest) 以了解 AI Studio 和 ML Studio 中 Phi-3 系列模型的詳細信息，包括如何配置推理端點、區域可用性、定價和推理模式參考。

免責聲明：本翻譯由 AI 模型從原文翻譯而來，可能不夠完美。請審閱並進行必要的修正。