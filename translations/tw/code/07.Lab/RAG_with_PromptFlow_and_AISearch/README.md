## RAG 使用 PromptFlow 和 AISearch

在這個範例中，我們將實作一個使用 Phi3 作為 SLM、AI Search 作為 vectorDB 以及 Prompt Flow 作為低代碼編排器的檢索增強生成 (RAG) 應用程式。

## 特點

- 使用 Docker 進行簡易部署。
- 可擴展的架構來處理 AI 工作流程。
- 使用 Prompt Flow 的低代碼方法。

## 先決條件

在開始之前，請確保您已經滿足以下要求：

- 在本地機器上安裝 Docker。
- 具有創建和管理容器資源權限的 Azure 帳戶。
- Azure AI Studio 和 Azure AI Search 實例。
- 用於創建索引的嵌入模型（可以是 Azure OpenAI 嵌入模型或目錄中的 OS 模型）。
- 在本地機器上安裝 Python 3.8 或更高版本。
- Azure Container Registry（或您選擇的任何註冊表）。

## 安裝

1. 使用 flow.yaml 文件在您的 Azure AI Studio 專案中創建一個新的流程。
2. 從 Azure AI 模型目錄中部署一個 Phi3 模型並創建與專案的連接。[部署 Phi-3 作為服務模型](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 使用任意文件在 Azure AI Search 上創建向量索引。[在 Azure AI Search 上創建向量索引](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 將流程部署到管理端點並在 prompt-flow-frontend.py 文件中使用它。[在在線端點部署流程](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. 克隆此存儲庫：

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. 建立 Docker 映像：

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. 將 Docker 映像推送到 Azure Container Registry：

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## 使用方法

1. 運行 Docker 容器：

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. 在瀏覽器中訪問應用程式 `http://localhost:8501`。

## 聯絡方式

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

完整文章: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**免責聲明**:
本文件是使用機器翻譯服務翻譯的。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文件為權威來源。對於關鍵信息，建議使用專業的人力翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。