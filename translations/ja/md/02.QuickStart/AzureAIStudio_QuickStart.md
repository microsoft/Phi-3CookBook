# **Azure AI StudioでのPhi-3の使用方法**

生成AIの発展に伴い、異なるLLMやSLMの管理、企業データの統合、ファインチューニング/RAG操作、およびLLMとSLMを統合した後の企業ビジネスの評価などを統一プラットフォームで行い、生成AIのスマートアプリケーションをより良く実現したいと考えています。[Azure AI Studio](https://ai.azure.com)は、エンタープライズ向けの生成AIアプリケーションプラットフォームです。

![aistudo](../../../../translated_images/ai-studio-home.e25e21a22af0a57c0cb02815f4c7554c8816afe8bc3c3008ac74e2eedd9fbaa9.ja.png)

Azure AI Studioを使用すると、大規模言語モデル（LLM）の応答を評価し、プロンプトフローを使ってプロンプトアプリケーションコンポーネントを調整し、パフォーマンスを向上させることができます。このプラットフォームは、概念実証から本格的な生産への移行を容易にし、スケーラビリティを提供します。継続的な監視と改良が長期的な成功をサポートします。

簡単な手順でAzure AI Studio上にPhi-3モデルを迅速にデプロイし、Azure AI Studioを使用してPhi-3関連のPlayground/Chat、ファインチューニング、評価などの関連作業を完了できます。

## **1. 準備**

## [AZD AI Studio スターターテンプレート](https://azure.github.io/awesome-azd/?name=AI+Studio)

### Azure AI Studio スターター

これは、Azure AI Studioを開始するために必要なすべてをデプロイするBicepテンプレートです。依存リソースを含むAI Hub、AIプロジェクト、AIサービス、およびオンラインエンドポイントが含まれます。

### クイック使用

既にマシンに[Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo)がインストールされている場合、新しいディレクトリでこのコマンドを実行するだけでこのテンプレートを使用できます。

### ターミナルコマンド

```bash
azd init -t azd-aistudio-starter
```

または
azd VS Code拡張機能を使用している場合は、このURLをVS Codeコマンドターミナルに貼り付けることができます。

### ターミナルURL

```bash
azd-aistudio-starter
```

## 手動作成

[Azure Portal](https://portal.azure.com?WT.mc_id=aiml-138114-kinfeylo)でAzure AI Studioを作成します。

![portal](../../../../translated_images/ai-studio-portal.8ae13fc10a0fe53104d7fe8d1c8c59b53f5ff7f4d74e52d81bcd63b5de6baf13.ja.png)

スタジオの命名とリージョンの設定を完了した後、作成できます。

![settings](../../../../translated_images/ai-studio-settings.ac28832948da45fd844232ae8e743f3e657a4b88e8a02ce80ae6bfad8ba4733a.ja.png)

作成が成功すると、[ai.azure.com](https://ai.azure.com/)を通じて作成したスタジオにアクセスできます。

![page](../../../../translated_images/ai-studio-page.9bfba68b0b3662a5323008dab8d9b24d4fc580be93777203bb64ad78283df469.ja.png)

1つのAI Studioには複数のプロジェクトが存在できます。AI Studioでプロジェクトを作成して準備を整えます。

![proj](../../../../translated_images/ai-studio-proj.62b5b49ee77bd4e382a82c1c28c247c1204c11ea212a4d95b39e467c6a24998f.ja.png)

## **2. Azure AI StudioでPhi-3モデルをデプロイ**

プロジェクトのExploreオプションをクリックしてモデルカタログに入り、Phi-3を選択します。

![model](../../../../translated_images/ai-studio-model.d90f85e0b4ce4bbdde6e460304f2e6676502e86ec0aae8f39dd56b7f0538afb9.ja.png)

Phi-3-mini-4k-instructを選択します。

![phi3](../../../../translated_images/ai-studio-phi3.9320ffe396abdbf9d1026637016462406090df88e0883e411b1984be34ed5710.ja.png)

「Deploy」をクリックしてPhi-3-mini-4k-instructモデルをデプロイします。

> [!NOTE]
>
> デプロイ時にコンピューティングパワーを選択できます。

## **3. Azure AI StudioでPlayground Chat Phi-3**

デプロイメントページに移動し、Playgroundを選択してAzure AI StudioのPhi-3とチャットします。

![chat](../../../../translated_images/ai-studio-chat.ba2c631ac2279f2deb4e87998895b0688e33d2f79475da6a3851e3fb3a0495c5.ja.png)

## **4. Azure AI Studioからモデルをデプロイ**

Azure Model Catalogからモデルをデプロイするには、次の手順に従います。

- Azure AI Studioにサインインします。
- Azure AI Studioのモデルカタログからデプロイしたいモデルを選択します。
- モデルの詳細ページで「Deploy」を選択し、次に「Serverless API with Azure AI Content Safety」を選択します。
- モデルをデプロイしたいプロジェクトを選択します。Serverless APIオファリングを使用するには、ワークスペースがEast US 2またはSweden Centralリージョンに属している必要があります。デプロイメント名をカスタマイズできます。
- デプロイメントウィザードで、価格と利用規約を確認します。
- 「Deploy」を選択します。デプロイメントが完了するまで待ち、デプロイメントページにリダイレクトされます。
- 「Open in playground」を選択してモデルと対話を開始します。
- デプロイメントページに戻り、デプロイメントを選択し、エンドポイントのターゲットURLとシークレットキーを確認します。これを使用してデプロイメントを呼び出し、完了を生成できます。
- Buildタブに移動し、ComponentsセクションからDeploymentsを選択して、エンドポイントの詳細、URL、およびアクセスキーをいつでも確認できます。

> [!NOTE]
> これらの手順を実行するには、アカウントにResource GroupのAzure AI Developerロールの権限が必要です。

## **5. Azure AI StudioでPhi-3 APIを使用**

Postman GETを通じてhttps://{Your project name}.region.inference.ml.azure.com/swagger.jsonにアクセスし、Keyと組み合わせて提供されるインターフェースについて学ぶことができます。

![swagger](../../../../translated_images/ai-studio-swagger.ae9e8fff8aba78ec18dc94b0ef251f0efe4ba90e77618ff0df13e1636e196abf.ja.png)

例えば、スコアAPIにアクセスする場合

![score](../../../../translated_images/ai-studio-score.0d5c8ce86241111633e946acf3413d3073957beb81cd37382cfd084ae310678f.ja.png)

リクエストパラメータやレスポンスパラメータを非常に簡単に取得できます。これはPostmanの結果です。

![result](../../../../translated_images/ai-studio-result.8563455b3a437110aa1d99bfc21cd8c624510b100f20b8907653cba5eef36226.ja.png)

免責事項: 翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。
出力を確認し、必要な修正を行ってください。