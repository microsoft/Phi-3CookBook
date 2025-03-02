## PromptFlowとAISearchを使用したRAG

この例では、Phi3をSLM、AI SearchをvectorDB、Prompt Flowをローコードオーケストレーターとして活用し、Retrieval Augmented Generation (RAG) アプリケーションを実装します。

## 特徴

- Dockerを使用した簡単なデプロイ。
- AIワークフローを処理するためのスケーラブルなアーキテクチャ。
- Prompt Flowを使用したローコードアプローチ。

## 前提条件

始める前に、以下の要件を満たしていることを確認してください：

- ローカルマシンにDockerがインストールされていること。
- コンテナリソースを作成・管理する権限を持つAzureアカウント。
- Azure AI StudioとAzure AI Searchのインスタンス。
- インデックスを作成するための埋め込みモデル（Azure OpenAI埋め込みモデルまたはカタログからのOSモデルのいずれか）。
- ローカルマシンにPython 3.8以降がインストールされていること。
- Azure Container Registry（または任意のレジストリ）。

## インストール手順

1. flow.yamlファイルを使用してAzure AI Studioプロジェクトで新しいフローを作成します。
2. Azure AIモデルカタログからPhi3モデルをデプロイし、プロジェクトへの接続を作成します。 [Phi-3をモデルとしてデプロイする](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 任意のドキュメントを使用してAzure AI Searchでベクトルインデックスを作成します。 [Azure AI Searchでベクトルインデックスを作成する](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. マネージドエンドポイントにフローをデプロイし、それをprompt-flow-frontend.pyファイルで使用します。 [オンラインエンドポイントにフローをデプロイする](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
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

2. ブラウザで`http://localhost:8501`にアクセスしてアプリケーションを使用します。

## お問い合わせ

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

全文記事: [Azure Model CatalogのPhi-3-Mediumをモデルとして使用したRAG](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確さが含まれる可能性があります。原文（元の言語の文書）が公式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の利用に起因する誤解や誤認について、当方は一切の責任を負いません。