# **在 Azure AI Studio 中使用 Phi-3**

隨著生成式 AI 的發展，我們希望使用統一平台來管理不同的 LLM 和 SLM、企業資料整合、微調/RAG 操作，以及整合 LLM 和 SLM 後對不同企業業務的評估等，使生成式 AI 的智慧應用得以更好地實現。Azure AI Studio 是企業級生成式 AI 應用平台。

![aistudo](../../../../imgs/02/AIStudio/ai-studio-home.png)

使用 Azure AI Studio，你可以評估大型語言模型（LLM）的回應，並通過提示流程協調提示應用程式元件，以提高效能。該平台促進延展性，輕鬆將概念驗證轉化為完整的生產。持續的監控和改進支持長期成功。

我們可以通過簡單的步驟在 Azure AI Studio 上快速部署 Phi-3 模型，然後使用 Azure AI Studio 完成與 Phi-3 相關的 Playground/Chat、微調、評估等相關工作。

## **1. 準備**

建立 Azure AI Studio 在 [Azure Portal](https://portal.azure.com?WT.mc_id=aiml-138114-kinfeylo)

![portal](../../../../imgs/02/AIStudio/ai-studio-portal.png)

完成工作室命名和設定區域後，你可以建立它

![settings](../../../../imgs/02/AIStudio/ai-studio-settings.png)

成功建立後，您可以通過 [ai.azure.com](https://ai.azure.com/) 訪問您建立的工作室。

![page](../../../../imgs/02/AIStudio/ai-studio-page.png)

在一個 AI Studio 上可以有多個專案。在 AI Studio 中建立一個專案以進行準備。

![proj](../../../../imgs/02/AIStudio/ai-studio-proj.png)

## **2. 部署 Phi-3 模型在 Azure AI Studio**

點擊專案的 Explore 選項進入 Model Catalog 並選擇 Phi-3

![model](../../../../imgs/02/AIStudio/ai-studio-model.png)

選擇 Phi-3-mini-4k-instruct

![phi3](../../../../imgs/02/AIStudio/ai-studio-phi3.png)

點擊 'Deploy' 來部署 Phi-3-mini-4k-instruct 模型

***注意***: 你可以在部署時選擇計算能力

## **3. Playground Chat Phi-3 in Azure AI Studio**

前往部署頁面，選擇 Playground，並與 Azure AI Studio 的 Phi-3 聊天

![chat](../../../../imgs/02/AIStudio/ai-studio-chat.png)

## **4. 部署模型從 Azure AI Studio**

要從 Azure 模型目錄部署模型，您可以按照以下步驟進行：

- 登入 Azure AI Studio。
- 從 Azure AI Studio 模型目錄中選擇您要部署的模型。
- 在模型的詳細資訊頁面上，選擇 Deploy，然後選擇 Serverless API with Azure AI Content Safety。
- 選擇您要部署模型的專案。要使用 Serverless API 服務，您的工作區必須屬於 East US 2 或 Sweden Central 區域。您可以自訂部署名稱。
- 在部署精靈上，選擇 Pricing and terms 以了解定價和使用條款。
- 選擇 Deploy。等待部署準備就緒，並且您被重定向到 Deployments 頁面。
- 選擇 Open in playground 以開始與模型互動。
- 您可以返回 Deployments 頁面，選擇部署，並記下端點的 Target URL 和 Secret Key，您可以使用這些來呼叫部署並生成完成。
- 您可以隨時通過導航到 Build 標籤並從 Components 部分選擇 Deployments 來找到端點的詳細資訊、URL 和訪問密鑰。

**請注意，您的帳戶必須在資源群組上具有 Azure AI 開發人員角色權限才能執行這些步驟**

## **5. 在 Azure AI Studio 中使用 Phi-3 API**

您可以通過 Postman GET 訪問 https://{Your project name}.region.inference.ml.azure.com/swagger.json 並結合 Key 來了解提供的介面。

![swagger](../../../../imgs/02/AIStudio/ai-studio-swagger.png)

例如存取分數 api

![score](../../../../imgs/02/AIStudio/ai-studio-score.png)

你可以非常方便地獲取請求參數，以及回應參數。這是 Postman 結果

![result](../../../../imgs/02/AIStudio/ai-studio-result.png)

