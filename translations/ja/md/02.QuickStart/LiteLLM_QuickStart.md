[LiteLLM](https://docs.litellm.ai/) を使って Phi-3 モデルを利用することは、多くのアプリケーションに統合したい場合に特に良い選択となります。LiteLLM は、API 呼び出しを異なるモデル（Phi-3 を含む）に対応するリクエストに変換するミドルウェアとして機能します。

Phi-3 は Microsoft によって開発された小型言語モデル (SLM) で、リソースが限られたマシンでも効率的に動作するよう設計されています。AVX サポートを持つ CPU と 4 GB の RAM さえあれば動作可能で、GPU を必要とせずにローカルで推論を行うのに適しています。

以下は、Phi-3 を利用するための LiteLLM の導入手順です：

1. **LiteLLM のインストール**: pip を使用して LiteLLM をインストールします：
   ```bash
   pip install litellm
   ```

2. **環境変数の設定**: API キーやその他必要な環境変数を設定します。
   ```python
   import os
   os.environ["OPENAI_API_KEY"] = "your-api-key"
   ```

3. **API 呼び出しの実行**: LiteLLM を使用して Phi-3 モデルに API 呼び出しを行います。
   ```python
   from litellm import completion

   response = completion(
       model="phi-3",
       messages=[{"role": "user", "content": "Hello, how are you?"}]
   )
   print(response)
   ```

4. **統合**: LiteLLM を Nextcloud Assistant などのさまざまなプラットフォームと統合することで、テキスト生成やその他のタスクに Phi-3 を利用することができます。

**LLMLite の完全なコードサンプル**
[Sample Code Notebook for LLMLite](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/litellm.ipynb)

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。
出力を確認し、必要な修正を行ってください。