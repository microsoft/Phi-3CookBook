## PromptFlowとAISearchを使用したRAG

この例では、SLMとしてPhi3、vectorDBとしてAI Search、低コードオーケストレーターとしてPrompt Flowを活用したRetrieval Augmented Generation (RAG)アプリケーションを実装します。

## 特徴

- Dockerを使用した簡単なデプロイ。
- AIワークフローを処理するためのスケーラブルなアーキテクチャ。
- Prompt Flowを使用した低コードアプローチ。

## 前提条件

始める前に、以下の要件を満たしていることを確認してください:

- ローカルマシンにDockerがインストールされていること。
- コンテナリソースを作成および管理する権限を持つAzureアカウント。
- Azure AI StudioおよびAzure AI Searchインスタンス。
- インデックスを作成するための埋め込みモデル（Azure OpenAIの埋め込みまたはカタログからのOSモデルのいずれか）。
- ローカルマシンにPython 3.8以降がインストールされていること。
- Azure Container Registry（または任意のレジストリ）。

## インストール

1. flow.yamlファイルを使用して、Azure AI Studioプロジェクトに新しいフローを作成します。
2. Azure AIモデルカタログからPhi3モデルをデプロイし、プロジェクトに接続を作成します。[モデルとしてのPhi-3のデプロイ](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. 任意のドキュメントを使用してAzure AI Searchにベクトルインデックスを作成します。[Azure AI Searchでのベクトルインデックスの作成](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. 管理されたエンドポイントにフローをデプロイし、prompt-flow-frontend.pyファイルで使用します。[オンラインエンドポイントにフローをデプロイ](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. リポジトリをクローンします:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Dockerイメージをビルドします:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. DockerイメージをAzure Container Registryにプッシュします:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## 使用方法

1. Dockerコンテナを実行します:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. ブラウザでアプリケーションにアクセスします: `http://localhost:8501`

## 連絡先

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

全文記事: [Azure Model CatalogからのモデルとしてのPhi-3-Mediumを使用したRAG](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**免責事項**:
この文書は機械翻訳AIサービスを使用して翻訳されています。正確さを期しておりますが、自動翻訳には誤りや不正確な点が含まれる場合があります。権威ある情報源としては、元の言語で書かれた原文を参照してください。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤認について、当社は一切の責任を負いません。