## 使用 PromptFlow 和 AISearch 的 RAG

在这个示例中，我们将实现一个利用 Phi3 作为 SLM，AI Search 作为 vectorDB 和 Prompt Flow 作为低代码编排器的检索增强生成（RAG）应用程序。

## 功能

- 使用 Docker 轻松部署。
- 可扩展的架构以处理 AI 工作流。
- 使用 Prompt Flow 的低代码方法

## 先决条件

在开始之前，请确保您满足以下要求：

- 在本地机器上安装了 Docker。
- 拥有一个 Azure 账户，并具有创建和管理容器资源的权限。
- 拥有 Azure AI Studio 和 Azure AI Search 实例。
- 一个用于创建索引的嵌入模型（可以是 Azure OpenAI 嵌入模型或目录中的 OS 模型）。
- 在本地机器上安装 Python 3.8 或更高版本。
- 一个 Azure 容器注册表（或您选择的任何注册表）。

## 安装

1. 使用 flow.yaml 文件在您的 Azure AI Studio 项目中创建一个新的流程。
2. 从您的 Azure AI 模型目录中部署一个 Phi3 模型，并创建与项目的连接。[将 Phi-3 部署为模型即服务](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 使用您选择的任何文档在 Azure AI Search 上创建向量索引。[在 Azure AI Search 上创建向量索引](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 在托管终端上部署流程，并在 prompt-flow-frontend.py 文件中使用它。[在在线终端上部署流程](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. 克隆仓库：

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

2. 在浏览器中访问应用程序，网址为 `http://localhost:8501`。

## 联系方式

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

完整文章：[使用 Azure 模型目录的 Phi-3-Medium 作为模型即服务的 RAG](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**免责声明**:
本文档使用基于机器的AI翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误读，我们不承担任何责任。