## 在 Python 中运行 Phi Family 模型 有关其他示例，请参见 https://github.com/marketplace/models

下面是一些使用示例的代码片段。有关 Azure AI Inference SDK 的更多信息，请参见[完整文档](https://aka.ms/azsdk/azure-ai-inference/python/reference)和[示例](https://aka.ms/azsdk/azure-ai-inference/python/samples)。

```
pip install azure-ai-inference
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

# 要使用模型进行身份验证，如果使用的是 GitHub Marketplace 模型（https://github.com/marketplace/models），则需要在 GitHub 设置中生成个人访问令牌 (PAT)。
# 按照此处的说明创建您的 PAT 令牌：https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
# 使用 GitHub Personal Token 或 Azure Key 创建一个 .env 文件，并设置 GitHub_token

client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
)

response = client.complete(
    messages=[
        SystemMessage(content=""""""),
        UserMessage(content="你能解释一下机器学习的基础知识吗？"),
    ],
    # 只需更改模型名称为适当的模型 "Phi-3.5-mini-instruct" 或 "Phi-3.5-vision-instruct"
    model="Phi-3.5-MoE-instruct", 
    temperature=0.8,
    max_tokens=2048,
    top_p=0.1
)

print(response.choices[0].message.content)
```

**免责声明**：
本文档使用基于机器的AI翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原文档的母语版本视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而产生的任何误解或误读，我们不承担任何责任。