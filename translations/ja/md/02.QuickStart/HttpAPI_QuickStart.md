# Azure API を Phi-3 で使う

このノートブックでは、Microsoft Azure AI と Azure ML が提供する Phi-3 API の使用例を紹介します。以下の内容をカバーします:  
* CLIでのPhi-3事前学習およびチャットモデルのHTTPリクエストAPIの使用方法
* PythonでのPhi-3事前学習およびチャットモデルのHTTPリクエストAPIの使用方法

では、**CLIでのHTTPリクエストAPIの使用方法**の概要を見ていきましょう。

## CLIでのHTTPリクエストAPIの使用方法

### 基本

REST APIを使用するには、エンドポイントURLとそのエンドポイントに関連付けられた認証キーが必要です。これらは前のステップで取得できます。

このチャットコンプリートの例では、シンプルな`curl`コールを使用して説明します。主に3つのコンポーネントがあります:

1. **`host-url`**: これはチャットコンプリートのスキーマ `/v1/chat/completions` を含むエンドポイントURLです。
2. **`headers`**: これはコンテンツタイプおよびAPIキーを定義します。
3. **`payload`または`data`**: これはプロンプトの詳細およびモデルのハイパーパラメータを含みます。

### 例

`curl`を使用してチャットコンプリートリクエストを行う例は以下の通りです:

```bash
curl -X POST https://api.example.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer YOUR_API_KEY" \
-d '{
  "model": "phi-3",
  "messages": [{"role": "user", "content": "Hello, how are you?"}],
  "max_tokens": 50
}'
```

### 内訳

- **`-X POST`**: 使用するHTTPメソッドを指定します。この場合はPOSTです。
- **`https://api.example.com/v1/chat/completions`**: エンドポイントURLです。
- **`-H "Content-Type: application/json"`**: コンテンツタイプをJSONに設定します。
- **`-H "Authorization: Bearer YOUR_API_KEY"`**: 認証ヘッダーにAPIキーを追加します。
- **`-d '{...}'`**: データペイロードで、モデル、メッセージ、およびその他のパラメータが含まれています。

### ヒント

- **エンドポイントURL**: `https://api.example.com` を実際のエンドポイントURLに置き換えてください。
- **APIキー**: `YOUR_API_KEY` を実際のAPIキーに置き換えてください。
- **ペイロード**: さまざまなプロンプト、モデル、およびパラメータに応じてペイロードをカスタマイズしてください。

サンプルを参照してください [Http Connections and Streaming](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/webrequests.ipynb)

詳細は [documentation](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo&tabs=phi-3-mini&pivots=programming-language-rest) を参照してください。AI StudioおよびML StudioのPhi-3ファミリーモデルの詳細、推論エンドポイントのプロビジョニング、地域の可用性、価格設定、および推論スキーマのリファレンスについて説明しています。

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完全ではない可能性があります。出力内容を確認し、必要な修正を行ってください。