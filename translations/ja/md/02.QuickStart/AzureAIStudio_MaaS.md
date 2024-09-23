# Phi-3モデルをサーバーレスAPIとしてデプロイ

[Azureモデルカタログ](https://learn.microsoft.com/azure/machine-learning/concept-model-catalog?WT.mc_id=aiml-137032-kinfeylo)にあるPhi-3モデル（Mini、Small、Medium）は、従量課金制でサーバーレスAPIとしてデプロイできます。このデプロイ方法は、サブスクリプション上でホスティングせずにAPIとしてモデルを利用できる方法を提供し、企業が必要とするセキュリティとコンプライアンスを維持します。このデプロイオプションは、サブスクリプションのクォータを必要としません。

[REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo) MaaSモデルは、/chat/completionsルートを使用してチャット完了のための共通のREST APIをサポートしています。

## 前提条件

1. 有効な支払い方法を持つAzureサブスクリプション。無料または試用のAzureサブスクリプションは利用できません。Azureサブスクリプションをお持ちでない場合、有料のAzureアカウントを作成してください。
1. [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)ハブ。Phi-3のサーバーレスAPIモデルデプロイは、以下のリージョンで作成されたハブでのみ利用可能です：
    - **East US 2**
    - **Sweden Central**

    > [!NOTE]
    > サーバーレスAPIエンドポイントデプロイメントをサポートする各モデルが利用可能なリージョンの一覧については、サーバーレスAPIエンドポイントのモデルのリージョン可用性を参照してください。

1. [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)プロジェクト。
1. Azureロールベースアクセス制御（Azure RBAC）は、Azure AI Studioでの操作にアクセス権を付与するために使用されます。この記事の手順を実行するには、ユーザーアカウントがリソースグループのAzure AI Developerロールに割り当てられている必要があります。

## 新しいデプロイを作成する

デプロイを作成するために以下のタスクを実行します：

1. [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)にサインインします。
1. 左のサイドバーからモデルカタログを選択します。
1. デプロイしたいモデル（例：Phi-3-mini-4k-Instruct）を検索して選択し、詳細ページを開きます。
1. デプロイを選択します。
1. サーバーレスAPIオプションを選択して、モデルのサーバーレスAPIデプロイウィンドウを開きます。

または、AI Studioのプロジェクトからデプロイを開始することもできます。

1. プロジェクトの左サイドバーからコンポーネント > デプロイを選択します。
1. + デプロイの作成を選択します。
1. Phi-3-mini-4k-Instructを検索して選択し、モデルの詳細ページを開きます。
1. 確認を選択し、サーバーレスAPIオプションを選択して、モデルのサーバーレスAPIデプロイウィンドウを開きます。
1. モデルをデプロイしたいプロジェクトを選択します。Phi-3モデルをデプロイするには、プロジェクトが[前提条件セクション](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo)に記載されているリージョンのいずれかに属している必要があります。
1. 価格と利用規約タブを選択して、選択したモデルの価格について学びます。
1. デプロイに名前を付けます。この名前はデプロイAPIのURLの一部になります。このURLは各Azureリージョンで一意である必要があります。
1. デプロイを選択します。デプロイが完了し、デプロイページにリダイレクトされるまで待ちます。このステップには、アカウントがリソースグループのAzure AI Developerロール権限を持っている必要があります（前提条件に記載）。
1. プレイグラウンドで開くを選択して、モデルとの対話を開始します。

デプロイページに戻り、デプロイを選択し、エンドポイントのターゲットURLとシークレットキーを確認してください。これらを使用してデプロイを呼び出し、完了を生成できます。APIの使用方法については、[Reference: Chat Completions](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)を参照してください。

プロジェクトの概要ページに移動し、左のサイドバーからコンポーネント > デプロイを選択することで、エンドポイントの詳細、URL、およびアクセスキーをいつでも確認できます。

## Phi-3モデルをサービスとして利用する

サーバーレスAPIとしてデプロイされたモデルは、デプロイしたモデルの種類に応じてチャットAPIを使用して利用できます。

1. プロジェクトの概要ページから、左サイドバーに移動し、コンポーネント > デプロイを選択します。
2. 作成したデプロイを見つけて選択します。
3. ターゲットURLとキーの値をコピーします。
4. <target_url>chat/completionsを使用してチャット/完了APIを使用してAPIリクエストを行います。APIの使用方法については、[Reference: Chat Completions](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)を参照してください。

## コストとクォータ

サーバーレスAPIとしてデプロイされたPhi-3モデルのコストとクォータの考慮事項

モデルをデプロイする際のデプロイウィザードの価格と利用規約タブで価格情報を確認できます。

クォータはデプロイごとに管理されます。各デプロイは1分あたり200,000トークンと1分あたり1,000 APIリクエストのレート制限があります。ただし、現在はプロジェクトごとにモデルごとに1つのデプロイのみを制限しています。現在のレート制限がシナリオに対して十分でない場合は、Microsoft Azureサポートに連絡してください。

## 追加リソース

### モデルをサーバーレスAPIとしてデプロイ

MaaSモデルをサービスとしての詳細については、[MaaS Deployment](https://learn.microsoft.com//azure/ai-studio/how-to/deploy-models-serverless?tabs=azure-ai-studio?WT.mc_id=aiml-137032-kinfeylo)を参照してください。

### Azure Machine Learning StudioまたはAzure AI Studioを使用してPhi-3ファミリーの小型言語モデルをデプロイする方法

Maap Models as a Platformの詳細については、[MaaP Deployment](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)を参照してください。

