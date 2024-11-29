## PythonでPhi Familyモデルを実行する 他のサンプルについては https://github.com/marketplace/models を参照してください

以下は、いくつかのユースケースのサンプルコードスニペットです。Azure AI Inference SDKの詳細については、[完全なドキュメント](https://aka.ms/azsdk/azure-ai-inference/python/reference)および[サンプル](https://aka.ms/azsdk/azure-ai-inference/python/samples)を参照してください。

```
pip install azure-ai-inference
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

# モデルを認証するには、GitHub Marketplaceのモデルを使用している場合、GitHub設定でパーソナルアクセストークン（PAT）を生成する必要があります（https://github.com/marketplace/models）。 
# PATトークンの作成方法については、こちらの手順に従ってください：https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
# GitHubのパーソナルトークンまたはAzure Key用にGitHub_tokenを含む.envファイルを作成します

client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
)

response = client.complete(
    messages=[
        SystemMessage(content=""""""),
        UserMessage(content="機械学習の基本を説明してもらえますか？"),
    ],
    # 適切なモデル名 "Phi-3.5-mini-instruct" または "Phi-3.5-vision-instruct" に変更するだけです
    model="Phi-3.5-MoE-instruct", 
    temperature=0.8,
    max_tokens=2048,
    top_p=0.1
)

print(response.choices[0].message.content)
```

**免責事項**:
この文書は機械翻訳サービスを使用して翻訳されています。正確さを期していますが、自動翻訳には誤りや不正確さが含まれる可能性があることにご注意ください。原文の母国語の文書が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤訳について、当社は一切の責任を負いません。