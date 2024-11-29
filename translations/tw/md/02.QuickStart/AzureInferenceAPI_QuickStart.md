## 在 Python 中运行 Phi Family 模型 更多示例请参见 https://github.com/marketplace/models

以下是一些用例的示例代码片段。有关 Azure AI Inference SDK 的更多信息，请参见[完整文档](https://aka.ms/azsdk/azure-ai-inference/python/reference)和[示例](https://aka.ms/azsdk/azure-ai-inference/python/samples)。

```
pip install azure-ai-inference
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

# 要验证模型，您需要在 GitHub 设置中生成个人访问令牌 (PAT)，如果您使用的是 GitHub Marketplace 模型 (https://github.com/marketplace/models)。
# 按照此处的说明创建您的 PAT 令牌：https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
# 创建一个 .env 文件，并为您的 GitHub 个人令牌或 Azure 密钥添加 GitHub_token

client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
)

response = client.complete(
    messages=[
        SystemMessage(content=""""""),
        UserMessage(content="你能解释一下机器学习的基本原理吗？"),
    ],
    # 只需更改模型名称为适当的模型 "Phi-3.5-mini-instruct" 或 "Phi-3.5-vision-instruct"
    model="Phi-3.5-MoE-instruct", 
    temperature=0.8,
    max_tokens=2048,
    top_p=0.1
)

print(response.choices[0].message.content)
```

**免責聲明**：
本文檔使用機器翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文檔為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀不承擔責任。