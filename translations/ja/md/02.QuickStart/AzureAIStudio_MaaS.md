# Phi-3 モデルをサーバーレスAPIとしてデプロイする

[Azure モデルカタログ](https://learn.microsoft.com/azure/machine-learning/concept-model-catalog?WT.mc_id=aiml-137032-kinfeylo)のPhi-3モデル（Mini、Small、Medium）は、従量課金制のサーバーレスAPIとしてデプロイできます。このデプロイメント方法は、モデルをサブスクリプションにホスティングせずにAPIとして消費する方法を提供し、企業が必要とするセキュリティとコンプライアンスを維持します。このデプロイメントオプションは、サブスクリプションのクォータを必要としません。

[REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo) MaaS モデルは、/chat/completions ルートを使用してチャット完了のための共通のREST APIをサポートするようになりました。

## 前提条件

1. 有効な支払い方法を持つAzureサブスクリプション。無料または試用版のAzureサブスクリプションは使用できません。Azureサブスクリプションをお持ちでない場合は、有料のAzureアカウントを作成してください。
1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) ハブ。Phi-3のサーバーレスAPIモデルデプロイメントは、以下のリージョンで作成されたハブでのみ利用可能です：
    - **East US 2**
    - **Sweden Central**

    > [!NOTE]
    > サーバーレスAPIエンドポイントデプロイメントをサポートする各モデルの利用可能なリージョンの一覧については、サーバーレスAPIエンドポイントのモデルのリージョン可用性を参照してください。

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) プロジェクト。
1. Azureロールベースのアクセス制御（Azure RBAC）は、Azure AI Foundryの操作にアクセスを付与するために使用されます。この記事の手順を実行するには、ユーザーアカウントにリソースグループのAzure AI Developerロールが割り当てられている必要があります。

## 新しいデプロイメントを作成する

デプロイメントを作成するには、次の手順を実行します：

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) にサインインします。
1. 左のサイドバーからモデルカタログを選択します。
1. デプロイしたいモデルを検索して選択します。例えば、Phi-3-mini-4k-Instructを選択して、詳細ページを開きます。
1. デプロイを選択します。
1. サーバーレスAPIオプションを選択して、モデルのサーバーレスAPIデプロイメントウィンドウを開きます。

または、AI Foundryのプロジェクトからデプロイメントを開始することもできます。

1. プロジェクトの左サイドバーから、コンポーネント > デプロイメントを選択します。
1. + Create deploymentを選択します。
1. Phi-3-mini-4k-Instructを検索して選択し、モデルの詳細ページを開きます。
1. 確認を選択し、サーバーレスAPIオプションを選択して、モデルのサーバーレスAPIデプロイメントウィンドウを開きます。
1. モデルをデプロイしたいプロジェクトを選択します。Phi-3モデルをデプロイするには、プロジェクトが[前提条件セクション](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo)に記載されているリージョンのいずれかに属している必要があります。
1. 価格と条件タブを選択して、選択したモデルの価格について確認します。
1. デプロイメントに名前を付けます。この名前はデプロイメントAPIのURLの一部になります。このURLは各Azureリージョンで一意である必要があります。
1. デプロイを選択します。デプロイメントが準備完了になるまで待ち、デプロイメントページにリダイレクトされるのを待ちます。このステップには、アカウントにリソースグループのAzure AI Developerロールの権限が必要です（前提条件に記載されています）。
1. プレイグラウンドで開くを選択して、モデルとの対話を開始します。

デプロイメントページに戻り、デプロイメントを選択して、エンドポイントのターゲットURLとシークレットキーを確認します。これを使用してデプロイメントを呼び出し、完了を生成できます。APIの使用方法について詳しくは、[参考資料：チャット完了](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)を参照してください。

プロジェクトの概要ページに移動すると、エンドポイントの詳細、URL、およびアクセスキーを常に確認できます。その後、プロジェクトの左サイドバーから、コンポーネント > デプロイメントを選択します。

## Phi-3 モデルをサービスとして消費する

サーバーレスAPIとしてデプロイされたモデルは、デプロイされたモデルの種類に応じてチャットAPIを使用して消費できます。

1. プロジェクトの概要ページから、左サイドバーのコンポーネント > デプロイメントを選択します。
2. 作成したデプロイメントを見つけて選択します。
3. ターゲットURLとキーの値をコピーします。
4. <target_url>chat/completions を使用してチャット/完了APIを使用してAPIリクエストを行います。APIの使用方法について詳しくは、[参考資料：チャット完了](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)を参照してください。

## コストとクォータ

サーバーレスAPIとしてデプロイされたPhi-3モデルのコストとクォータの考慮事項

モデルをデプロイする際のデプロイメントウィザードの価格と条件タブで価格情報を確認できます。

クォータはデプロイメントごとに管理されます。各デプロイメントには、1分あたり200,000トークンおよび1分あたり1,000 APIリクエストのレート制限があります。ただし、現在、プロジェクトごとにモデルごとに1つのデプロイメントに制限しています。現在のレート制限がシナリオに十分でない場合は、Microsoft Azureサポートに連絡してください。

## 追加リソース

### モデルをサーバーレスAPIとしてデプロイする

MaaS Models as a Service 詳細については、[MaaS Deployment](https://learn.microsoft.com//azure/ai-studio/how-to/deploy-models-serverless?tabs=azure-ai-studio?WT.mc_id=aiml-137032-kinfeylo)を参照してください。

### Azure Machine Learning studio または Azure AI Foundry を使用して Phi-3 小型言語モデルファミリーをデプロイする方法

Maap Models as a Platform 詳細については、[MaaP Deployment](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)を参照してください。

**免責事項**:
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期すよう努めていますが、自動翻訳には誤りや不正確さが含まれる場合があります。権威ある情報源としては、原文の言語の文書を参照してください。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤訳について、当社は一切の責任を負いかねます。