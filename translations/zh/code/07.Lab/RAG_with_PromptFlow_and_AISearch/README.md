## 使用 PromptFlow 和 AISearch 实现 RAG

在这个示例中，我们将实现一个利用 Phi3 作为 SLM、AI Search 作为 vectorDB 和 Prompt Flow 作为低代码编排器的检索增强生成（RAG）应用程序。

## 特性

- 使用 Docker 轻松部署。
- 可扩展的架构来处理 AI 工作流。
- 使用 Prompt Flow 的低代码方法。

## 前提条件

在开始之前，请确保您满足以下要求：

- 在本地机器上安装 Docker。
- 拥有一个 Azure 账户，并具备创建和管理容器资源的权限。
- 拥有 Azure AI Studio 和 Azure AI Search 实例。
- 拥有一个用于创建索引的嵌入模型（可以是 Azure OpenAI 嵌入或目录中的操作系统模型）。
- 在本地机器上安装 Python 3.8 或更高版本。
- 拥有一个 Azure 容器注册表（或您选择的任何注册表）。

## 安装

1. 使用 flow.yaml 文件在您的 Azure AI Studio 项目中创建一个新的流。
2. 从您的 Azure AI 模型目录中部署一个 Phi3 模型，并创建与您项目的连接。[部署 Phi-3 作为服务模型](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 使用任意文档在 Azure AI Search 上创建向量索引。[在 Azure AI Search 上创建向量索引](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 在托管端点上部署流，并在 prompt-flow-frontend.py 文件中使用它。[在在线端点上部署流](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. 克隆代码库：

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. 构建 Docker 镜像：

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. 将 Docker 镜像推送到 Azure 容器注册表：

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## 使用方法

1. 运行 Docker 容器：

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. 在浏览器中访问应用程序 `http://localhost:8501`。

## 联系方式

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

完整文章：[RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

