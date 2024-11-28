# **Azure AI FoundryでPhi-3を使用する**

生成AIの発展に伴い、異なるLLMやSLMの管理、企業データの統合、ファインチューニング/RAG操作、およびLLMやSLMを統合した後の企業業務の評価などを統一プラットフォームで行いたいと考えています。これにより、生成AIのスマートなアプリケーションがより良く実現されます。[Azure AI Foundry](https://ai.azure.com)は、エンタープライズ向けの生成AIアプリケーションプラットフォームです。

![aistudo](../../../../translated_images/ai-studio-home.e25e21a22af0a57c0cb02815f4c7554c8816afe8bc3c3008ac74e2eedd9fbaa9.ja.png)

Azure AI Foundryを使用すると、大規模言語モデル（LLM）の応答を評価し、プロンプトフローでプロンプトアプリケーションコンポーネントを編成してパフォーマンスを向上させることができます。このプラットフォームは、概念実証を完全な本番環境に容易に移行するためのスケーラビリティを提供します。継続的な監視と改良が長期的な成功をサポートします。

簡単な手順でAzure AI FoundryにPhi-3モデルを迅速にデプロイし、その後、Azure AI Foundryを使用してPhi-3関連のPlayground/Chat、ファインチューニング、評価などの関連作業を完了できます。

## **1. 準備**

## [AZD AI Foundry Starter Template](https://azure.github.io/awesome-azd/?name=AI+Studio)

### Azure AI Foundry Starter

これは、Azure AI Foundryの開始に必要なすべてをデプロイするBicepテンプレートです。AI Hubと依存リソース、AIプロジェクト、AIサービス、およびオンラインエンドポイントが含まれています。

### クイック使用

すでに[Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo)がマシンにインストールされている場合、このテンプレートの使用は新しいディレクトリで次のコマンドを実行するだけで簡単です。

### ターミナルコマンド

```bash
azd init -t azd-aistudio-starter
```

または
azd VS Code拡張機能を使用している場合、VS CodeのコマンドターミナルにこのURLを貼り付けることができます。

### ターミナルURL

```bash
azd-aistudio-starter
```

## 手動作成

[Azure Portal](https://portal.azure.com?WT.mc_id=aiml-138114-kinfeylo)でAzure AI Foundryを作成します。

![portal](../../../../translated_images/ai-studio-portal.8ae13fc10a0fe53104d7fe8d1c8c59b53f5ff7f4d74e52d81bcd63b5de6baf13.ja.png)

スタジオの名前を設定し、リージョンを設定した後、作成できます。

![settings](../../../../translated_images/ai-studio-settings.ac28832948da45fd844232ae8e743f3e657a4b88e8a02ce80ae6bfad8ba4733a.ja.png)

作成が成功したら、[ai.azure.com](https://ai.azure.com/)から作成したスタジオにアクセスできます。

![page](../../../../translated_images/ai-studio-page.9bfba68b0b3662a5323008dab8d9b24d4fc580be93777203bb64ad78283df469.ja.png)

1つのAI Foundryに複数のプロジェクトを持つことができます。AI Foundryでプロジェクトを作成して準備をします。

![proj](../../../../translated_images/ai-studio-proj.62b5b49ee77bd4e382a82c1c28c247c1204c11ea212a4d95b39e467c6a24998f.ja.png)

## **2. Azure AI FoundryにPhi-3モデルをデプロイする**

プロジェクトのExploreオプションをクリックしてモデルカタログに入り、Phi-3を選択します。

![model](../../../../translated_images/ai-studio-model.d90f85e0b4ce4bbdde6e460304f2e6676502e86ec0aae8f39dd56b7f0538afb9.ja.png)

Phi-3-mini-4k-instructを選択します。

![phi3](../../../../translated_images/ai-studio-phi3.9320ffe396abdbf9d1026637016462406090df88e0883e411b1984be34ed5710.ja.png)

「Deploy」をクリックしてPhi-3-mini-4k-instructモデルをデプロイします。

> [!NOTE]
>
> デプロイ時に計算能力を選択できます。

## **3. Azure AI FoundryでPhi-3を使ったPlayground Chat**

デプロイページに移動し、Playgroundを選択してAzure AI FoundryのPhi-3とチャットします。

![chat](../../../../translated_images/ai-studio-chat.ba2c631ac2279f2deb4e87998895b0688e33d2f79475da6a3851e3fb3a0495c5.ja.png)

## **4. Azure AI Foundryからモデルをデプロイする**

Azure Model Catalogからモデルをデプロイするには、次の手順を実行します。

- Azure AI Foundryにサインインします。
- Azure AI Foundryのモデルカタログからデプロイしたいモデルを選択します。
- モデルの詳細ページで「Deploy」を選択し、「Serverless API with Azure AI Content Safety」を選択します。
- モデルをデプロイするプロジェクトを選択します。Serverless APIオファリングを使用するには、ワークスペースがEast US 2またはSweden Centralリージョンに属している必要があります。デプロイメント名をカスタマイズできます。
- デプロイメントウィザードで、価格と利用規約を選択して価格と利用規約を確認します。
- 「Deploy」を選択します。デプロイメントが準備完了になるまで待ち、デプロイメントページにリダイレクトされます。
- 「Open in playground」を選択して、モデルと対話を開始します。
- デプロイメントページに戻り、デプロイメントを選択し、エンドポイントのターゲットURLとシークレットキーを確認して、デプロイメントを呼び出して完了を生成します。
- 「Build」タブに移動し、「Components」セクションから「Deployments」を選択することで、エンドポイントの詳細、URL、およびアクセスキーをいつでも確認できます。

> [!NOTE]
> これらの手順を実行するには、アカウントにResource GroupのAzure AI Developerロール権限が必要です。

## **5. Azure AI FoundryでPhi-3 APIを使用する**

Postman GETを使用してhttps://{Your project name}.region.inference.ml.azure.com/swagger.jsonにアクセスし、Keyと組み合わせて提供されるインターフェースについて学びます。

![swagger](../../../../translated_images/ai-studio-swagger.ae9e8fff8aba78ec18dc94b0ef251f0efe4ba90e77618ff0df13e1636e196abf.ja.png)

例えば、スコアAPIにアクセスする場合

![score](../../../../translated_images/ai-studio-score.0d5c8ce86241111633e946acf3413d3073957beb81cd37382cfd084ae310678f.ja.png)

リクエストパラメータやレスポンスパラメータを非常に便利に取得できます。これはPostmanの結果です。

![result](../../../../translated_images/ai-studio-result.8563455b3a437110aa1d99bfc21cd8c624510b100f20b8907653cba5eef36226.ja.png)

**免責事項**:
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期していますが、自動翻訳にはエラーや不正確さが含まれる場合がありますのでご注意ください。元の言語の文書が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解釈について、当社は一切の責任を負いません。