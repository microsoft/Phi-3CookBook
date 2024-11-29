# 推理 Azure AI 模型

[Azure AI 模型推理是一個 API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo)，它為基礎模型提供了一組通用功能，開發者可以用它以一致的方式從各種模型中獲取預測結果。開發者可以與部署在 Azure AI Foundry 的不同模型進行交互，而不需要更改所使用的底層代碼。

Microsoft 現在有自己的 AI 模型推理 SDK，適用於 [MaaS/MaaP](https://azure.microsoft.com/products/ai-model-catalog?WT.mc_id=aiml-138114-kinfeylo) 上托管的不同模型。

Python 和 JS 版本已經發布。C# 版本將在接下來發布。

[Python](https://learn.microsoft.com/python/api/overview/azure/ai-inference-readme?view=azure-python-preview?WT.mc_id=aiml-138114-kinfeylo) 的 [範例](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples?WT.mc_id=aiml-138114-kinfeylo)

[JavaScript](https://learn.microsoft.com/javascript/api/overview/azure/ai-inference-rest-readme?view=azure-node-preview?WT.mc_id=aiml-138114-kinfeylo) 的 [範例](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples?WT.mc_id=aiml-138114-kinfeylo)

該 SDK 使用 [這裡記錄的 REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo)。

## 可用性

Azure AI 模型推理 API 可用於以下 Phi-3 模型：

- 部署到無伺服器 API 端點的模型：
- 部署到託管推理的模型：

該 API 與 Azure OpenAI 模型部署兼容。

> [!NOTE]
> Azure AI 模型推理 API 可用於 2024 年 6 月 24 日之後部署的託管推理（Managed Online Endpoints）。如果模型是在此日期之前部署的，請重新部署端點以利用該 API。

## 功能

以下部分描述了該 API 所提供的一些功能。完整的 API 規範請查看參考部分。

### 模態

該 API 指示開發者如何消費以下模態的預測：

- 獲取信息：返回部署在端點下的模型信息。
- 文本嵌入：創建表示輸入文本的嵌入向量。
- 文本完成：根據提供的提示和參數創建完成。
- 聊天完成：為給定的聊天對話創建模型回應。
- 圖像嵌入：創建表示輸入文本和圖像的嵌入向量。

**免責聲明**:
本文件使用基於機器的人工智能翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始語言的文件視為權威來源。對於關鍵信息，建議進行專業人工翻譯。對於因使用此翻譯而引起的任何誤解或誤釋，我們不承擔責任。