# 推論 Azure AI 模型

[Azure AI 模型推論是一個 API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo)，它為基礎模型提供了一組通用的功能，開發者可以用統一和一致的方式從多種模型中獲取預測結果。開發者可以與部署在 Azure AI Studio 的不同模型進行交互，而無需更改他們正在使用的底層代碼。

Microsoft 現在有自己的 AI 模型推論 SDK，適用於 [MaaS/MaaP](https://azure.microsoft.com/products/ai-model-catalog?WT.mc_id=aiml-138114-kinfeylo) 上托管的不同模型。

Python 和 JS 版本已經推出。C# 版本將在接下來發布。

[Python](https://learn.microsoft.com/python/api/overview/azure/ai-inference-readme?view=azure-python-preview?WT.mc_id=aiml-138114-kinfeylo) [範例](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples?WT.mc_id=aiml-138114-kinfeylo)

[JavaScript](https://learn.microsoft.com/javascript/api/overview/azure/ai-inference-rest-readme?view=azure-node-preview?WT.mc_id=aiml-138114-kinfeylo) [範例](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples?WT.mc_id=aiml-138114-kinfeylo)

這個 SDK 使用 [這裡記錄的 REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo)。

## 可用性

Azure AI 模型推論 API 可用於以下 Phi-3 模型：

- 部署到無伺服器 API 端點的模型：
- 部署到管理推論的模型：

此 API 與 Azure OpenAI 模型部署兼容。

> [!NOTE]
> Azure AI 模型推論 API 可在 2024 年 6 月 24 日之後部署的管理推論（Managed Online Endpoints）中使用。若要利用此 API，如果模型是在此日期之前部署的，請重新部署您的端點。

## 功能

以下部分描述了 API 提供的一些功能。欲了解 API 的完整規範，請查看參考部分。

### 模態

API 說明了開發者如何獲取以下模態的預測結果：

- 獲取信息：返回部署在端點下的模型信息。
- 文本嵌入：創建表示輸入文本的嵌入向量。
- 文本補全：為提供的提示和參數創建補全。
- 聊天補全：為給定的聊天對話創建模型回應。
- 圖像嵌入：創建表示輸入文本和圖像的嵌入向量。

免責聲明：此翻譯由人工智慧模型從原文翻譯而來，可能不完全準確。請檢查輸出並進行必要的修正。