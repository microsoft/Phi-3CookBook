## PromptFlowとAISearchを用いたRAG

この例では、SLMとしてPhi3、vectorDBとしてAI Search、そして低コードオーケストレーターとしてPrompt Flowを活用したRetrieval Augmented Generation (RAG)アプリケーションを実装します。

## 特徴

- Dockerを使った簡単なデプロイ。
- AIワークフローを処理するためのスケーラブルなアーキテクチャ。
- Prompt Flowを用いた低コードアプローチ。

## 前提条件

始める前に、以下の要件を満たしていることを確認してください：

- ローカルマシンにDockerがインストールされている。
- コンテナリソースを作成および管理する権限を持つAzureアカウント。
- Azure AI StudioとAzure AI Searchのインスタンス。
- インデックスを作成するための埋め込みモデル（Azure OpenAI埋め込みまたはカタログからのOSモデルのいずれか）。
- ローカルマシンにPython 3.8以上がインストールされている。
- Azure Container Registry（または任意のレジストリ）。

## インストール

1. flow.yamlファイルを使用して、Azure AI Studioプロジェクトに新しいフローを作成します。
2. Azure AIモデルカタログからPhi3モデルをデプロイし、プロジェクトに接続します。[Phi-3をModel as a Serviceとしてデプロイ](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 任意のドキュメントを使用して、Azure AI Searchにベクトルインデックスを作成します。[Azure AI Searchでベクトルインデックスを作成](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. マネージドエンドポイントにフローをデプロイし、prompt-flow-frontend.pyファイルで使用します。[オンラインエンドポイントにフローをデプロイ](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. リポジトリをクローンします：

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Dockerイメージをビルドします：

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. DockerイメージをAzure Container Registryにプッシュします：

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## 使用方法

1. Dockerコンテナを実行します：

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. ブラウザでアプリケーションにアクセスします：`http://localhost:8501`.

## 連絡先

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

全文記事: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

