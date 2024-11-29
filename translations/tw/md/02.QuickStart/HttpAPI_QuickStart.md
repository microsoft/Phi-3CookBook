# 使用 Azure API 與 Phi-3

這份筆記本展示了如何使用 Microsoft Azure AI 和 Azure ML 提供的 Phi-3 API。我們將涵蓋以下內容：
* 在 CLI 中使用 HTTP 請求 API 來操作 Phi-3 預訓練模型和聊天模型
* 在 Python 中使用 HTTP 請求 API 來操作 Phi-3 預訓練模型和聊天模型

這裡是 **在 CLI 中使用 HTTP 請求 API** 的概述：

## 在 CLI 中使用 HTTP 請求 API

### 基本概念

使用 REST API 時，你需要有一個端點 URL 和與該端點關聯的身份驗證密鑰。這些可以從之前的步驟中獲取。

在這個聊天完成範例中，我們使用一個簡單的 `curl` 調用來進行說明。有三個主要組成部分：

1. **`host-url`**：這是你的端點 URL，包含聊天完成的架構 `/v1/chat/completions`。
2. **`headers`**：這定義了內容類型以及你的 API 密鑰。
3. **`payload` 或 `data`**：這包括你的提示詳情和模型超參數。

### 範例

這裡是一個使用 `curl` 進行聊天完成請求的範例：

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

- **`-X POST`**: Specifies the HTTP method to use, which is POST in this case.
- **`https://api.example.com/v1/chat/completions`**: The endpoint URL.
- **`-H "Content-Type: application/json"`**: Sets the content type to JSON.
- **`-H "Authorization: Bearer YOUR_API_KEY"`**: Adds the authorization header with your API key.
- **`-d '{...}'`**: The data payload, which includes the model, messages, and other parameters.

### Tips

- **Endpoint URL**: Ensure you replace `https://api.example.com` with your actual endpoint URL.
- **API Key**: Replace `YOUR_API_KEY` 替換成你的實際 API 密鑰。
- **有效載荷**：根據你的需求自定義有效載荷，包括不同的提示、模型和參數。

參考範例 [Http Connections and Streaming](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/webrequests.ipynb)

查看 [文件](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo&tabs=phi-3-mini&pivots=programming-language-rest) 了解 AI Studio 和 ML Studio 中 Phi-3 模型系列的詳細資訊，包括如何配置推理端點、區域可用性、定價和推理架構參考。

**免責聲明**：
本文件是使用基於機器的AI翻譯服務進行翻譯的。儘管我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以其原始語言的文件為權威來源。對於關鍵信息，建議進行專業的人類翻譯。我們對因使用本翻譯而引起的任何誤解或誤讀不承擔責任。