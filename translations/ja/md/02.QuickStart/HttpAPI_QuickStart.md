# Azure APIをPhi-3で使用する

このノートブックでは、Microsoft Azure AIおよびAzure MLが提供するPhi-3 APIの使用例を紹介します。以下をカバーします：  
* CLIでのPhi-3事前学習済みモデルおよびチャットモデルのHTTPリクエストAPIの使用方法
* PythonでのPhi-3事前学習済みモデルおよびチャットモデルのHTTPリクエストAPIの使用方法

まずは、**CLIでのHTTPリクエストAPIの使用方法**についての概要です：

## CLIでのHTTPリクエストAPIの使用方法

### 基本

REST APIを使用するには、エンドポイントURLとそのエンドポイントに関連付けられた認証キーが必要です。これらは前のステップで取得できます。

このチャット完了の例では、簡単な`curl`コールを使用して説明します。主に3つのコンポーネントがあります：

1. **`host-url`**: これは、チャット完了スキーマ`/v1/chat/completions`を持つエンドポイントURLです。
2. **`headers`**: これは、コンテンツタイプとAPIキーを定義します。
3. **`payload`または`data`**: これは、プロンプトの詳細とモデルのハイパーパラメータを含みます。

### 例

以下は、`curl`を使用してチャット完了リクエストを行う例です：

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

### 詳細

- **`-X POST`**: Specifies the HTTP method to use, which is POST in this case.
- **`https://api.example.com/v1/chat/completions`**: The endpoint URL.
- **`-H "Content-Type: application/json"`**: Sets the content type to JSON.
- **`-H "Authorization: Bearer YOUR_API_KEY"`**: Adds the authorization header with your API key.
- **`-d '{...}'`**: The data payload, which includes the model, messages, and other parameters.

### Tips

- **Endpoint URL**: Ensure you replace `https://api.example.com` with your actual endpoint URL.
- **API Key**: Replace `YOUR_API_KEY`**：実際のAPIキーに置き換えます。
- **ペイロード**：異なるプロンプト、モデル、およびパラメータを含めて、要件に応じてペイロードをカスタマイズします。

サンプルを参照：[Http Connections and Streaming](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/webrequests.ipynb)

Phi-3ファミリーモデルの詳細については、AI StudioおよびML Studioの[ドキュメント](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo&tabs=phi-3-mini&pivots=programming-language-rest)を参照してください。推論エンドポイントのプロビジョニング、地域の可用性、価格、および推論スキーマのリファレンスについて詳しく説明しています。

**免責事項**:
この文書は機械翻訳AIサービスを使用して翻訳されています。正確さを期すために努めていますが、自動翻訳には誤りや不正確さが含まれる場合があります。原文の言語で書かれた元の文書を信頼できる情報源とみなしてください。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤訳について、当社は一切の責任を負いません。