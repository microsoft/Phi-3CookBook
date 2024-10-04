# Azure AI と Azure ML で Phi-3 を使用するための OpenAI SDK

Azure AI と Azure ML で Phi-3 デプロイメントを利用するために `openai` SDK を使用します。Azure AI と Azure ML の Phi-3 モデルファミリーは、OpenAI Chat Completion API と互換性のある API を提供しており、OpenAI モデルから Phi-3 LLM へのシームレスな移行を可能にします。

この API は、OpenAI のクライアントライブラリや LangChain や LlamaIndex などのサードパーティツールで直接使用できます。

以下の例では、OpenAI Python ライブラリを使用してこの移行を行う方法を示しています。Phi-3 はチャット完了 API のみをサポートしていることに注意してください。

OpenAI SDK を使用して Phi-3 モデルを利用するには、環境を設定し、API コールを行うためにいくつかの手順を踏む必要があります。以下は、その手順を示したガイドです：

1. **OpenAI SDK のインストール**: まず、OpenAI Python パッケージをまだインストールしていない場合はインストールします。
   ```bash
   pip install openai
   ```

2. **API キーの設定**: OpenAI API キーを用意してください。環境変数に設定するか、コード内で直接設定することができます。
   ```python
   import openai

   openai.api_key = "your-api-key"
   ```

3. **API コールの実行**: OpenAI SDK を使用して Phi-3 モデルと対話します。以下は、完了リクエストを行う例です：
   ```python
   response = openai.Completion.create(
       model="phi-3",
       prompt="Hello, how are you?",
       max_tokens=50
   )

   print(response.choices[0].text.strip())
   ```

4. **レスポンスの処理**: アプリケーションに必要な形でモデルからのレスポンスを処理します。

以下は、より詳細な例です：
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

これにより、提供されたプロンプトに基づいて短いストーリーが生成されます。出力の長さを制御するために `max_tokens` パラメータを調整できます。

[Phi-3 モデルの完全なノートブックサンプルを見る](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/openaisdk.ipynb)

AI Studio と ML Studio の Phi-3 モデルファミリーに関する詳細な情報は、推論エンドポイントのプロビジョニング、地域の可用性、価格設定、および推論スキーマのリファレンスについて、[ドキュメント](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo) を確認してください。

**免責事項**:
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期すよう努めておりますが、自動翻訳には誤りや不正確さが含まれる場合があります。原文が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤訳について、当社は一切の責任を負いません。