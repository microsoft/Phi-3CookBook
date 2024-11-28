# Azure AIとAzure MLでPhi-3を使用したOpenAI SDKの活用

Azure AIとAzure MLでPhi-3デプロイメントを利用するために`openai` SDKを使用します。Azure AIとAzure MLのPhi-3モデルファミリーは、OpenAIのChat Completion APIと互換性のあるAPIを提供します。これにより、OpenAIモデルからPhi-3 LLMへのシームレスな移行が可能になります。

このAPIは、OpenAIのクライアントライブラリやLangChainやLlamaIndexのようなサードパーティツールと直接使用できます。

以下の例では、OpenAI Python Libraryを使用してこの移行を行う方法を示しています。Phi-3はチャット完了APIのみをサポートしていることに注意してください。

OpenAI SDKを使用してPhi-3モデルを利用するには、環境を設定しAPIコールを行うためのいくつかのステップを踏む必要があります。以下のガイドを参考にしてください：

1. **OpenAI SDKのインストール**: まず、OpenAI Pythonパッケージをまだインストールしていない場合はインストールする必要があります。
   ```bash
   pip install openai
   ```

2. **APIキーの設定**: OpenAI APIキーを持っていることを確認してください。環境変数に設定するか、コード内に直接設定することができます。
   ```python
   import openai

   openai.api_key = "your-api-key"
   ```

3. **APIコールの実行**: OpenAI SDKを使用してPhi-3モデルとやり取りします。以下は完了リクエストを行う例です：
   ```python
   response = openai.Completion.create(
       model="phi-3",
       prompt="Hello, how are you?",
       max_tokens=50
   )

   print(response.choices[0].text.strip())
   ```

4. **レスポンスの処理**: アプリケーションの必要に応じてモデルからのレスポンスを処理します。

以下はより詳細な例です：
```python
import openai

# Set your API key
openai.api_key = "your-api-key"

# Define the prompt
prompt = "Write a short story about a brave knight."

# Make the API call
response = openai.Completion.create(
    model="phi-3",
    prompt=prompt,
    max_tokens=150
)

# Print the response
print(response.choices[0].text.strip())
```

これにより、提供されたプロンプトに基づいて短いストーリーが生成されます。出力の長さを制御するために`max_tokens`パラメータを調整できます。

[Phi-3モデルの完全なノートブックサンプルを見る](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/openaisdk.ipynb)

AI StudioおよびML StudioでPhi-3モデルファミリーの詳細については、推論エンドポイントのプロビジョニング、地域ごとの可用性、価格設定、および推論スキーマのリファレンスについての[ドキュメント](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo)を確認してください。

**免責事項**:
この文書は、機械翻訳AIサービスを使用して翻訳されています。正確性を期すよう努めていますが、自動翻訳には誤りや不正確さが含まれる場合があります。元の言語での文書を権威ある情報源とみなすべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤訳について、当社は一切の責任を負いません。