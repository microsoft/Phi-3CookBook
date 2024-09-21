# 將 Phi-3 模型部署為無伺服器 API

[Azure 模型目錄](https://learn.microsoft.com/azure/machine-learning/concept-model-catalog?WT.mc_id=aiml-137032-kinfeylo)中的 Phi-3 模型（Mini、Small 和 Medium）可以部署為按需付費的無伺服器 API。這種部署方式提供了一種消費模型的方式，無需在您的訂閱中託管它們，同時保留企業所需的安全性和合規性。這種部署選項不需要使用您訂閱中的配額。

[REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo) MaaS 模型現在支援一個通用的 REST API，用於使用 /chat/completions 路徑進行聊天完成。

## 先決條件

1. 一個有效付款方式的 Azure 訂閱。免費或試用 Azure 訂閱無法使用。如果您沒有 Azure 訂閱，請創建一個付費的 Azure 帳戶開始。
1. 一個 [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) 中心。Phi-3 的無伺服器 API 模型部署僅在以下地區創建的中心中可用：
    - **美國東部 2**
    - **瑞典中部**

    > [!NOTE]
    > 有關支持無伺服器 API 端點部署的模型在各地區的可用性列表，請參見無伺服器 API 端點中模型的地區可用性。

1. 一個 [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) 項目。
1. Azure 基於角色的訪問控制 (Azure RBAC) 用於授予 Azure AI Studio 中操作的訪問權限。要執行本文中的步驟，您的用戶帳戶必須被分配 Azure AI 開發人員角色在資源組上。

## 創建新部署

執行以下任務以創建部署：

1. 登錄 [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。
1. 從左側邊欄中選擇模型目錄。
1. 搜索並選擇您想要部署的模型，例如 Phi-3-mini-4k-Instruct，打開其詳情頁。
1. 選擇部署。
1. 選擇無伺服器 API 選項，為模型打開無伺服器 API 部署窗口。

或者，您可以從 AI Studio 的項目開始啟動部署。

1. 從您的項目的左側邊欄中，選擇組件 > 部署。
1. 選擇 + 創建部署。
1. 搜索並選擇 Phi-3-mini-4k-Instruct 打開模型的詳情頁。
1. 選擇確認，並選擇無伺服器 API 選項，為模型打開無伺服器 API 部署窗口。
1. 選擇您想要部署模型的項目。要部署 Phi-3 模型，您的項目必須屬於[先決條件部分](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo)中列出的地區之一。
1. 選擇定價和條款選項卡，了解所選模型的定價。
1. 給部署起個名字。這個名字將成為部署 API URL 的一部分。這個 URL 在每個 Azure 地區必須是唯一的。
1. 選擇部署。等待部署完成，並將您重定向到部署頁面。這一步需要您的帳戶在資源組上具有 Azure AI 開發人員角色權限，如先決條件中所列。
1. 選擇在操場中打開以開始與模型互動。

返回部署頁面，選擇部署，並記下端點的目標 URL 和密鑰，您可以用它們來調用部署並生成完成。 有關使用 API 的更多信息，請參見 [參考：聊天完成](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)。

您可以隨時通過導航到您的項目概述頁面找到端點的詳細信息、URL 和訪問密鑰。然後，從您的項目的左側邊欄中，選擇組件 > 部署。

## 作為服務消費 Phi-3 模型

部署為無伺服器 API 的模型可以根據您部署的模型類型使用聊天 API 進行消費。

1. 從您的項目概述頁面，轉到左側邊欄並選擇組件 > 部署。
2. 查找並選擇您創建的部署。
3. 複製目標 URL 和密鑰值。
4. 使用 chat/completions API 進行 API 請求，使用 <target_url>chat/completions。 有關使用 API 的更多信息，請參見 [參考：聊天完成](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)。

## 成本和配額

部署為無伺服器 API 的 Phi-3 模型的成本和配額考慮

您可以在部署向導的定價和條款選項卡中找到定價信息。

配額是按部署管理的。每個部署每分鐘有 200,000 個令牌的速率限制和每分鐘 1,000 個 API 請求。然而，我們目前限制每個項目每個模型一個部署。如果當前的速率限制不足以滿足您的場景，請聯繫 Microsoft Azure 支持。

## 其他資源

### 將模型部署為無伺服器 API

MaaS 作為服務的模型 有關 [MaaS 部署](https://learn.microsoft.com//azure/ai-studio/how-to/deploy-models-serverless?tabs=azure-ai-studio?WT.mc_id=aiml-137032-kinfeylo) 的詳細信息

### 如何使用 Azure 機器學習工作室或 Azure AI Studio 部署 Phi-3 系列的小型語言模型

Maap 作為平台的模型 有關 [MaaP 部署](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini) 的詳細信息

免责声明：此翻译由AI模型从原文翻译而来，可能不够完美。请审阅输出内容并进行必要的修改。