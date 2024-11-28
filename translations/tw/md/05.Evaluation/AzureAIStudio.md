# **使用 Azure AI Foundry 進行評估**

![aistudo](../../../../translated_images/AIStudio.d5171bb73e888005d9ac4020bbbf4ad9bd9a8bc042dfaf90b44c3afa1a8cbeed.tw.png)

如何使用 [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) 評估你的生成式 AI 應用程式。無論你是在評估單輪對話還是多輪對話，Azure AI Foundry 都提供了評估模型性能和安全性的工具。

![aistudo](../../../../translated_images/AIPortfolio.d7a339b6c36a58d3ca1bc2ca3b181618e45b1c87a6c20527a4503cb74e78e5cf.tw.png)

## 如何使用 Azure AI Foundry 評估生成式 AI 應用程式
更多詳細說明請參閱 [Azure AI Foundry 文件](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

以下是開始的步驟：

## 在 Azure AI Foundry 中評估生成式 AI 模型

**先決條件**

- 一個 CSV 或 JSON 格式的測試數據集。
- 一個已部署的生成式 AI 模型（如 Phi-3、GPT 3.5、GPT 4 或 Davinci 模型）。
- 一個運行時環境，包含一個計算實例來運行評估。

## 內建評估指標

Azure AI Foundry 允許你評估單輪對話和複雜的多輪對話。
對於基於檢索增強生成（RAG）的場景，當模型基於特定數據時，你可以使用內建的評估指標來評估性能。
此外，你還可以評估一般的單輪問答場景（非 RAG）。

## 創建評估運行

從 Azure AI Foundry 的 UI，導航到評估頁面或 Prompt Flow 頁面。
按照評估創建向導設置評估運行。為你的評估提供一個可選名稱。
選擇與你的應用程式目標對應的場景。
選擇一個或多個評估指標來評估模型的輸出。

## 自定義評估流程（可選）

為了更大的靈活性，你可以建立自定義的評估流程。根據你的具體需求自定義評估過程。

## 查看結果

在運行評估後，在 Azure AI Foundry 中記錄、查看和分析詳細的評估指標。深入了解你的應用程式的能力和限制。



**Note** Azure AI Foundry 目前處於公開預覽階段，因此用於實驗和開發目的。對於生產工作負載，請考慮其他選項。探索官方 [AI Foundry 文件](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) 以獲取更多詳細信息和逐步說明。

**免責聲明**：
本文件使用機器翻譯服務進行翻譯。我們致力於準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對使用本翻譯所引起的任何誤解或誤讀不承擔責任。