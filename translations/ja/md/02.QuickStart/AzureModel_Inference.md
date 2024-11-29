# Azure AI モデル推論

[Azure AI モデル推論は API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo)であり、基盤モデルの共通機能を公開し、開発者が多様なモデルから予測を一貫して利用できるようにします。開発者は、Azure AI Foundry にデプロイされた異なるモデルと対話する際に、使用している基礎コードを変更することなく利用できます。

Microsoft は、[MaaS/MaaP](https://azure.microsoft.com/products/ai-model-catalog?WT.mc_id=aiml-138114-kinfeylo)にホストされている異なるモデルのための AI モデル推論用の独自の SDK を提供しています。

Python と JS のバージョンがリリースされており、次に C# がリリースされる予定です。

[Python](https://learn.microsoft.com/python/api/overview/azure/ai-inference-readme?view=azure-python-preview?WT.mc_id=aiml-138114-kinfeylo)の[サンプル](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples?WT.mc_id=aiml-138114-kinfeylo)

[JavaScript](https://learn.microsoft.com/javascript/api/overview/azure/ai-inference-rest-readme?view=azure-node-preview?WT.mc_id=aiml-138114-kinfeylo)の[サンプル](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples?WT.mc_id=aiml-138114-kinfeylo)

この SDK は[ここで文書化された REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo)を使用します。

## 利用可能性

Azure AI モデル推論 API は以下の Phi-3 モデルで利用可能です：

- サーバーレス API エンドポイントにデプロイされたモデル：
- 管理された推論にデプロイされたモデル：

この API は Azure OpenAI モデルのデプロイメントと互換性があります。

> [!NOTE]
> Azure AI モデル推論 API は、2024年6月24日以降にデプロイされたモデルに対して管理された推論 (Managed Online Endpoints) で利用可能です。この API を利用するには、その日以前にデプロイされたモデルの場合、エンドポイントを再デプロイしてください。

## 機能

以下のセクションでは、API が提供するいくつかの機能について説明します。API の完全な仕様については、リファレンスセクションを参照してください。

### モダリティ

この API は、開発者が以下のモダリティの予測をどのように利用できるかを示します：

- 情報取得: エンドポイントにデプロイされたモデルに関する情報を返します。
- テキスト埋め込み: 入力テキストを表す埋め込みベクトルを作成します。
- テキスト補完: 提供されたプロンプトとパラメータに基づいて補完を作成します。
- チャット補完: 指定されたチャット会話に対するモデルの応答を作成します。
- 画像埋め込み: 入力テキストと画像を表す埋め込みベクトルを作成します。

**免責事項**：
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を期していますが、自動翻訳にはエラーや不正確さが含まれる可能性があることをご理解ください。原文の言語で書かれた元の文書が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用によって生じた誤解や誤訳について、当社は責任を負いません。