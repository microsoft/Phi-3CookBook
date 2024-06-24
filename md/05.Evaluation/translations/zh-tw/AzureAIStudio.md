# **使用 Azure AI Studio 進行評估**

![aistudo](../../../../imgs/05/AIStudio/AIStudio.png)

如何使用 [Azure AI Studio](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) 評估您的生成式 AI 應用程式。無論您是在評估單輪還是多輪對話，Azure AI Studio 都提供了評估模型性能和安全性的工具。

![aistudo](../../../../imgs/05/AIStudio/AIPortfolio.png)

以下是開始的步驟:

## 評估生成式 AI 模型在 Azure AI Studio

**先決條件**

- 一個 CSV 或 JSON 格式的測試資料集。
- 一個已部署的生成式 AI 模型（例如 Phi-3、GPT 3.5、GPT 4 或 Davinci 模型）。
- 一個具有計算實例的運行時來執行評估。

## 內建評估指標

Azure AI Studio 允許你評估單輪和複雜的多輪對話。
對於檢索增強生成（RAG）場景，其中模型基於特定數據，你可以使用內建評估指標來評估性能。
此外，你還可以評估一般的單輪問答場景（非 RAG）。

## 建立一個評估執行

從 Azure AI Studio UI，導航到 Evaluate 頁面或 Prompt Flow 頁面。
按照評估建立精靈來設定評估執行。為您的評估提供一個可選的名稱。
選擇與您的應用程式目標一致的情境。
選擇一個或多個評估指標來評估模型的輸出。

## 自訂評估流程 (選擇性)

為了更大的靈活性，您可以建立自訂的評估流程。根據您的具體需求自訂評估過程。

## 檢視結果

執行評估後，在 Azure AI Studio 中記錄、查看和分析詳細的評估指標。深入了解您的應用程式的能力和限制。

**注意** Azure AI Studio 目前處於公開預覽階段，因此請將其用於實驗和開發目的。對於生產工作負載，請考慮其他選項。探索官方 [AI Studio 文件](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) 以獲取更多詳細資訊和逐步指導。

