## 使用 PromptFlow 和 AISearch 的 RAG

在這個範例中，我們將實作一個檢索增強生成（RAG）應用，利用 Phi3 作為 SLM，AI Search 作為向量資料庫，以及 Prompt Flow 作為低程式碼的協作工具。

## 功能

- 使用 Docker 輕鬆部署。
- 可擴展的架構以處理 AI 工作流程。
- 使用 Prompt Flow 的低程式碼方法。

## 先決條件

在開始之前，請確保您已滿足以下要求：

- 本地機器上已安裝 Docker。
- 一個具有建立和管理容器資源權限的 Azure 帳戶。
- Azure AI Studio 和 Azure AI Search 實例。
- 用於建立索引的嵌入模型（可以是 Azure OpenAI 的嵌入模型或目錄中的開源模型）。
- 本地機器上已安裝 Python 3.8 或更新版本。
- 一個 Azure 容器登錄（或任何您選擇的登錄）。

## 安裝

1. 使用 flow.yaml 文件在您的 Azure AI Studio 專案中創建一個新的 flow。
2. 從 Azure AI 模型目錄部署一個 Phi3 模型，並建立與專案的連接。[部署 Phi-3 作為服務模型](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 使用任意文件在 Azure AI Search 上創建向量索引。[在 Azure AI Search 上創建向量索引](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 將 flow 部署到受管端點，並在 prompt-flow-frontend.py 文件中使用它。[在線端點上部署 flow](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. 克隆此存儲庫：

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. 建立 Docker 映像檔：

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. 將 Docker 映像檔推送到 Azure 容器登錄：

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## 使用方式

1. 運行 Docker 容器：

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. 在瀏覽器中訪問應用程式，網址為 `http://localhost:8501`。

## 聯繫方式

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

完整文章：[RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**免責聲明**：  
本文檔是使用基於機器的人工智能翻譯服務進行翻譯的。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文檔的母語版本作為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。