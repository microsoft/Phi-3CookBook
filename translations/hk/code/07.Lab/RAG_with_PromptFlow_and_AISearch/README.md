## 使用 PromptFlow 同 AISearch 做 RAG

呢個例子會示範點樣用 Retrieval Augmented Generation (RAG) 應用，結合 Phi3 作為 SLM、AI Search 作為 vectorDB，同埋用 Prompt Flow 作為低代碼編排工具。

## 功能

- 簡單用 Docker 部署。
- 可擴展架構，適合處理 AI 工作流程。
- 用 Prompt Flow 採用低代碼方式。

## 先決條件

喺開始之前，請確保你已經滿足以下要求：

- 喺你嘅本地機器裝咗 Docker。
- 一個 Azure 帳戶，有權限創建同管理容器資源。
- Azure AI Studio 同 Azure AI Search 實例。
- 一個用嚟建立索引嘅嵌入模型（可以係 Azure OpenAI 嵌入模型或者目錄入面嘅開源模型）。
- 本地機器已安裝 Python 3.8 或更新版本。
- 一個 Azure Container Registry（或者你選擇嘅任何容器註冊表）。

## 安裝

1. 喺 Azure AI Studio 項目中，用 flow.yaml 文件創建一個新嘅 flow。
2. 喺 Azure AI 模型目錄部署一個 Phi3 模型，並創建與你項目嘅連接。[部署 Phi-3 作為服務模型](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 用任意你選擇嘅文檔，喺 Azure AI Search 上創建向量索引。[喺 Azure AI Search 創建向量索引](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 喺一個托管端點部署 flow，並喺 prompt-flow-frontend.py 文件中使用。[喺在線端點部署 flow](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. 克隆倉庫：

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

2. 喺瀏覽器中訪問應用程序，網址係 `http://localhost:8501`。

## 聯絡

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

全文文章：[RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**免責聲明**:  
此文件是使用機器翻譯服務進行翻譯的。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文件作為權威來源。對於關鍵資訊，建議使用專業的人手翻譯。我們對因使用此翻譯而引起的任何誤解或誤譯概不負責。