# 部署 Phi-3 模型為無伺服器 API

[Azure 模型目錄](https://learn.microsoft.com/azure/machine-learning/concept-model-catalog?WT.mc_id=aiml-137032-kinfeylo)中的 Phi-3 模型（Mini、Small 和 Medium）可以部署為無伺服器 API，並採用隨用隨付的計費方式。這種部署方式提供了一種通過 API 使用模型的方法，而無需在您的訂閱中託管它們，同時保持企業所需的安全性和合規性。這種部署選項不需要使用您訂閱中的配額。

[REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo) MaaS 模型現在支援使用 /chat/completions 路徑的通用 REST API 進行聊天完成。

## 先決條件

1. 具有有效付款方式的 Azure 訂閱。免費或試用的 Azure 訂閱無法使用。如果您沒有 Azure 訂閱，請創建一個付費的 Azure 帳戶開始使用。
1. 一個 [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) 中心。Phi-3 的無伺服器 API 模型部署僅在以下區域創建的中心可用：
    - **美國東部 2**
    - **瑞典中部**

    > [!NOTE]
    > 有關支持無伺服器 API 端點部署的模型在各區域的可用性列表，請參見無伺服器 API 端點中的模型區域可用性。

1. 一個 [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) 項目。
1. Azure 基於角色的存取控制（Azure RBAC）用於授予對 Azure AI Foundry 中操作的訪問權限。要執行本文中的步驟，您的用戶帳戶必須在資源組上被分配為 Azure AI 開發者角色。

## 創建新部署

執行以下任務來創建部署：

1. 登錄到 [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。
1. 從左側邊欄選擇模型目錄。
1. 搜索並選擇您要部署的模型，例如 Phi-3-mini-4k-Instruct，打開其詳細信息頁面。
1. 選擇部署。
1. 選擇無伺服器 API 選項以打開模型的無伺服器 API 部署窗口。

或者，您可以從 AI Foundry 中的項目開始啟動部署。

1. 從項目的左側邊欄選擇組件 > 部署。
1. 選擇 + 創建部署。
1. 搜索並選擇 Phi-3-mini-4k-Instruct 以打開模型的詳細信息頁面。
1. 選擇確認，並選擇無伺服器 API 選項以打開模型的無伺服器 API 部署窗口。
1. 選擇您要部署模型的項目。要部署 Phi-3 模型，您的項目必須屬於 [先決條件部分](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo)中列出的區域之一。
1. 選擇定價和條款選項卡以了解所選模型的定價。
1. 為部署命名。此名稱將成為部署 API URL 的一部分。此 URL 在每個 Azure 區域中必須是唯一的。
1. 選擇部署。等待部署準備就緒並將您重定向到部署頁面。此步驟需要您的帳戶在資源組上具有 Azure AI 開發者角色權限，如先決條件中所列。
1. 選擇在 Playground 中打開以開始與模型互動。

返回部署頁面，選擇部署，記下端點的目標 URL 和密鑰，您可以使用它們來調用部署並生成完成。關於如何使用 API 的更多信息，請參見 [參考：聊天完成](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)。

您可以隨時通過導航到您的項目概覽頁面找到端點的詳細信息、URL 和訪問密鑰。然後，從項目的左側邊欄選擇組件 > 部署。

## 作為服務消費 Phi-3 模型

根據您部署的模型類型，部署為無伺服器 API 的模型可以使用聊天 API 進行消費。

1. 從您的項目概覽頁面，轉到左側邊欄並選擇組件 > 部署。
2. 找到並選擇您創建的部署。
3. 複製目標 URL 和密鑰值。
4. 使用 <target_url>chat/completions 使用聊天/完成 API 發出 API 請求。關於如何使用 API 的更多信息，請參見 [參考：聊天完成](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)。

## 成本和配額

部署為無伺服器 API 的 Phi-3 模型的成本和配額考量

您可以在部署向導的定價和條款選項卡上找到定價信息。

配額是按部署管理的。每個部署的速率限制為每分鐘 200,000 個標記和每分鐘 1,000 個 API 請求。然而，我們目前限制每個項目每個模型一個部署。如果當前的速率限制不夠您的場景，請聯繫 Microsoft Azure 支援。

## 其他資源

### 部署模型為無伺服器 API

MaaS 模型作為服務 有關 [MaaS 部署](https://learn.microsoft.com//azure/ai-studio/how-to/deploy-models-serverless?tabs=azure-ai-studio?WT.mc_id=aiml-137032-kinfeylo) 的詳細信息

### 如何使用 Azure Machine Learning Studio 或 Azure AI Foundry 部署 Phi-3 系列的小型語言模型

Maap 模型作為平台 有關 [MaaP 部署](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini) 的詳細信息

**免責聲明**:
本文檔已使用機器翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文檔為權威來源。對於關鍵信息，建議使用專業的人類翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。