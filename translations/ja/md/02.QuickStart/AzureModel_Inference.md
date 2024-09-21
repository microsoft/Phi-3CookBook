# Azure AI モデル推論

[Azure AI モデル推論は API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo)で、基礎モデルの共通機能を提供し、さまざまなモデルから予測を一貫して利用できるようにします。開発者は、Azure AI Studio にデプロイされた異なるモデルと、使用しているコードを変更せずに対話できます。

Microsoft は現在、[MaaS/MaaP](https://azure.microsoft.com/products/ai-model-catalog?WT.mc_id=aiml-138114-kinfeylo)でホストされている異なるモデル向けに独自の AI モデル推論 SDK を提供しています。

Python および JS バージョンがリリースされており、次に C# がリリース予定です。

[Python](https://learn.microsoft.com/python/api/overview/azure/ai-inference-readme?view=azure-python-preview?WT.mc_id=aiml-138114-kinfeylo)の[サンプル](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples?WT.mc_id=aiml-138114-kinfeylo)

[JavaScript](https://learn.microsoft.com/javascript/api/overview/azure/ai-inference-rest-readme?view=azure-node-preview?WT.mc_id=aiml-138114-kinfeylo)の[サンプル](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples?WT.mc_id=aiml-138114-kinfeylo)

この SDK は[こちらに記載された REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo)を使用します。

## 利用可能性

Azure AI モデル推論 API は以下の Phi-3 モデルで利用可能です：

- サーバーレス API エンドポイントにデプロイされたモデル：
- 管理された推論にデプロイされたモデル：

この API は Azure OpenAI モデルのデプロイと互換性があります。

> [!NOTE]
> Azure AI モデル推論 API は、2024年6月24日以降にデプロイされたモデルに対して、管理された推論（Managed Online Endpoints）で利用可能です。この API を利用するには、該当日以前にデプロイされたモデルの場合、エンドポイントを再デプロイしてください。

## 機能

以下のセクションでは、API が提供するいくつかの機能について説明します。API の完全な仕様については、リファレンスセクションを参照してください。

### モダリティ

API は、以下のモダリティに対して予測を利用する方法を示します：

- 情報取得：エンドポイントにデプロイされたモデルに関する情報を返します。
- テキスト埋め込み：入力テキストを表す埋め込みベクターを作成します。
- テキスト補完：提供されたプロンプトとパラメータに対する補完を作成します。
- チャット補完：指定されたチャット会話に対するモデルの応答を作成します。
- 画像埋め込み：入力テキストと画像を表す埋め込みベクターを作成します。

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。
出力内容を確認し、必要に応じて修正を行ってください。