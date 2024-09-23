## RAG 與 PromptFlow 和 AISearch

在這個範例中，我們將實現一個檢索增強生成 (RAG) 應用，利用 Phi3 作為 SLM、AI Search 作為 vectorDB，並使用 Prompt Flow 作為低代碼編排器。

## 功能

- 使用 Docker 進行簡單部署。
- 可擴展的架構以處理 AI 工作流程。
- 使用 Prompt Flow 的低代碼方法

## 先決條件

在開始之前，請確保您已滿足以下要求：

- 本地機器上已安裝 Docker。
- 具有創建和管理容器資源權限的 Azure 帳戶。
- Azure AI Studio 和 Azure AI Search 實例
- 一個用於創建索引的嵌入模型（可以是 Azure OpenAI 嵌入或目錄中的 OS 模型）
- 本地機器上已安裝 Python 3.8 或更高版本。
- 一個 Azure 容器註冊表（或您選擇的任何註冊表）

## 安裝

1. 使用 flow.yaml 文件在您的 Azure AI Studio 項目中創建一個新流程。
2. 從您的 Azure AI 模型目錄部署一個 Phi3 模型，並創建與項目的連接。[部署 Phi-3 作為服務模型](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 使用您選擇的任何文檔在 Azure AI Search 上創建向量索引 [在 Azure AI Search 上創建向量索引](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 在管理端點上部署該流程，並在 prompt-flow-frontend.py 文件中使用它。[在在線端點上部署流程](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. 克隆此存儲庫：

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. 構建 Docker 映像：

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. 將 Docker 映像推送到 Azure 容器註冊表：

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

2. 在瀏覽器中訪問應用程序 `http://localhost:8501`。

## 聯繫方式

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

完整文章: [RAG 與 Phi-3-Medium 作為 Azure 模型目錄中的服務模型](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

