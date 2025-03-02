## نماذج GitHub - إصدار تجريبي عام محدود

مرحبًا بك في [نماذج GitHub](https://github.com/marketplace/models)! نحن جاهزون لتقديم تجربة استكشاف نماذج الذكاء الاصطناعي المستضافة على Azure AI.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.ar.png)

لمزيد من المعلومات حول النماذج المتاحة على نماذج GitHub، قم بزيارة [سوق نماذج GitHub](https://github.com/marketplace/models).

## النماذج المتاحة

كل نموذج يحتوي على واجهة تشغيل خاصة به وعينات من الأكواد.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### نماذج Phi-3 في كتالوج نماذج GitHub

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## البدء

هناك بعض الأمثلة الأساسية الجاهزة للتشغيل. يمكنك العثور عليها في دليل العينات. إذا كنت ترغب في الانتقال مباشرة إلى لغتك المفضلة، يمكنك العثور على الأمثلة باللغات التالية:

- Python  
- JavaScript  
- cURL  

كما يوجد بيئة مخصصة من Codespaces لتشغيل العينات والنماذج.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.ar.png)

## أمثلة على الأكواد

فيما يلي مقتطفات أمثلة للأكواد لبعض حالات الاستخدام. لمزيد من المعلومات حول Azure AI Inference SDK، راجع الوثائق الكاملة والعينات.

## الإعداد

1. إنشاء رمز وصول شخصي  
لا تحتاج إلى إعطاء أي أذونات للرمز. لاحظ أن الرمز سيتم إرساله إلى خدمة Microsoft.

لاستخدام مقتطفات الأكواد أدناه، قم بإنشاء متغير بيئي لتعيين الرمز كمفتاح لكود العميل.

إذا كنت تستخدم bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
إذا كنت تستخدم powershell:  
```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

إذا كنت تستخدم موجه الأوامر في Windows:  
```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## مثال Python

### تثبيت التبعيات  
قم بتثبيت Azure AI Inference SDK باستخدام pip (يتطلب: Python >=3.8):  
```
pip install azure-ai-inference
```  

### تشغيل مثال أساسي  

يُظهر هذا المثال استدعاءً أساسيًا لواجهة API لإكمال المحادثة. يعتمد على نقطة النهاية لاستنتاج نماذج GitHub AI ورمز الوصول الخاص بك. الاتصال متزامن.  

```
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.inference.ai.azure.com"
# Replace Model_Name 
model_name = "Phi-3-small-8k-instruct"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="What is the capital of France?"),
    ],
    model=model_name,
    temperature=1.,
    max_tokens=1000,
    top_p=1.
)

print(response.choices[0].message.content)
```  

### تشغيل محادثة متعددة الجولات  

يوضح هذا المثال محادثة متعددة الجولات باستخدام واجهة API لإكمال المحادثة. عند استخدام النموذج لتطبيق محادثة، ستحتاج إلى إدارة تاريخ المحادثة وإرسال أحدث الرسائل إلى النموذج.  

```
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
# Replace Model_Name
model_name = "Phi-3-small-8k-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    UserMessage(content="What is the capital of France?"),
    AssistantMessage(content="The capital of France is Paris."),
    UserMessage(content="What about Spain?"),
]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```  

### بث المخرجات  

لتحسين تجربة المستخدم، قد ترغب في بث استجابة النموذج بحيث يظهر أول رمز بشكل مبكر وتتجنب الانتظار الطويل للحصول على استجابات طويلة.  

```
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
# Replace Model_Name
model_name = "Phi-3-small-8k-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    stream=True,
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="Give me 5 good reasons why I should exercise every day."),
    ],
    model=model_name,
)

for update in response:
    if update.choices:
        print(update.choices[0].delta.content or "", end="")

client.close()
```  

## JavaScript  

### تثبيت التبعيات  

قم بتثبيت Node.js.  

انسخ النصوص التالية واحفظها كملف package.json داخل المجلد الخاص بك.  

```
{
  "type": "module",
  "dependencies": {
    "@azure-rest/ai-inference": "latest",
    "@azure/core-auth": "latest",
    "@azure/core-sse": "latest"
  }
}
```  

ملاحظة: @azure/core-sse مطلوبة فقط عند بث استجابات إكمال المحادثات.  

افتح نافذة طرفية في هذا المجلد وقم بتشغيل npm install.  

لكل مقتطف من الأكواد أدناه، انسخ المحتوى إلى ملف sample.js وقم بتشغيله باستخدام node sample.js.  

### تشغيل مثال أساسي  

يُظهر هذا المثال استدعاءً أساسيًا لواجهة API لإكمال المحادثة. يعتمد على نقطة النهاية لاستنتاج نماذج GitHub AI ورمز الوصول الخاص بك. الاتصال متزامن.  

```
import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";
// Update your modelname
const modelName = "Phi-3-small-8k-instruct";

export async function main() {

  const client = new ModelClient(endpoint, new AzureKeyCredential(token));

  const response = await client.path("/chat/completions").post({
    body: {
      messages: [
        { role:"system", content: "You are a helpful assistant." },
        { role:"user", content: "What is the capital of France?" }
      ],
      model: modelName,
      temperature: 1.,
      max_tokens: 1000,
      top_p: 1.
    }
  });

  if (response.status !== "200") {
    throw response.body.error;
  }
  console.log(response.body.choices[0].message.content);
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
```  

### تشغيل محادثة متعددة الجولات  

يوضح هذا المثال محادثة متعددة الجولات باستخدام واجهة API لإكمال المحادثة. عند استخدام النموذج لتطبيق محادثة، ستحتاج إلى إدارة تاريخ المحادثة وإرسال أحدث الرسائل إلى النموذج.  

```
import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";
// Update your modelname
const modelName = "Phi-3-small-8k-instruct";

export async function main() {

  const client = new ModelClient(endpoint, new AzureKeyCredential(token));

  const response = await client.path("/chat/completions").post({
    body: {
      messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "What is the capital of France?" },
        { role: "assistant", content: "The capital of France is Paris." },
        { role: "user", content: "What about Spain?" },
      ],
      model: modelName,
    }
  });

  if (response.status !== "200") {
    throw response.body.error;
  }

  for (const choice of response.body.choices) {
    console.log(choice.message.content);
  }
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
```  

### بث المخرجات  
لتحسين تجربة المستخدم، قد ترغب في بث استجابة النموذج بحيث يظهر أول رمز بشكل مبكر وتتجنب الانتظار الطويل للحصول على استجابات طويلة.  

```
import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";
import { createSseStream } from "@azure/core-sse";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";
// Update your modelname
const modelName = "Phi-3-small-8k-instruct";

export async function main() {

  const client = new ModelClient(endpoint, new AzureKeyCredential(token));

  const response = await client.path("/chat/completions").post({
    body: {
      messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "Give me 5 good reasons why I should exercise every day." },
      ],
      model: modelName,
      stream: true
    }
  }).asNodeStream();

  const stream = response.body;
  if (!stream) {
    throw new Error("The response stream is undefined");
  }

  if (response.status !== "200") {
    stream.destroy();
    throw new Error(`Failed to get chat completions, http operation failed with ${response.status} code`);
  }

  const sseStream = createSseStream(stream);

  for await (const event of sseStream) {
    if (event.data === "[DONE]") {
      return;
    }
    for (const choice of (JSON.parse(event.data)).choices) {
        process.stdout.write(choice.delta?.content ?? ``);
    }
  }
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
```  

## REST  

### تشغيل مثال أساسي  

قم بلصق التالي في واجهة shell:  

```
curl -X POST "https://models.inference.ai.azure.com/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -d '{
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What is the capital of France?"
            }
        ],
        "model": "Phi-3-small-8k-instruct"
    }'
```  

### تشغيل محادثة متعددة الجولات  

استدعِ واجهة API لإكمال المحادثة وقم بتمرير سجل المحادثة:  

```
curl -X POST "https://models.inference.ai.azure.com/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -d '{
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What is the capital of France?"
            },
            {
                "role": "assistant",
                "content": "The capital of France is Paris."
            },
            {
                "role": "user",
                "content": "What about Spain?"
            }
        ],
        "model": "Phi-3-small-8k-instruct"
    }'
```  

### بث المخرجات  

هذا مثال لاستدعاء نقطة النهاية وبث الاستجابة.  

```
curl -X POST "https://models.inference.ai.azure.com/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -d '{
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Give me 5 good reasons why I should exercise every day."
            }
        ],
        "stream": true,
        "model": "Phi-3-small-8k-instruct"
    }'
```  

## الاستخدام المجاني وحدود المعدلات لنماذج GitHub  

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.ar.png)  

[حدود المعدلات لواجهة التشغيل والاستخدام المجاني لواجهة API](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) تهدف إلى مساعدتك على تجربة النماذج وبناء نماذج أولية لتطبيق الذكاء الاصطناعي الخاص بك. لاستخدام يتجاوز هذه الحدود، ولتوسيع نطاق تطبيقك، يجب عليك توفير الموارد من حساب Azure، والمصادقة من هناك بدلاً من استخدام رمز الوصول الشخصي الخاص بـ GitHub. لا تحتاج إلى تغيير أي شيء آخر في الكود الخاص بك. استخدم هذا الرابط لمعرفة كيفية تجاوز حدود المستوى المجاني في Azure AI.  

### الإفصاحات  

تذكر عند التفاعل مع نموذج أنك تقوم بتجربة الذكاء الاصطناعي، لذا قد تحدث أخطاء في المحتوى.  

الميزة تخضع لقيود متنوعة (بما في ذلك الطلبات لكل دقيقة، والطلبات لكل يوم، والرموز لكل طلب، والطلبات المتزامنة) وليست مصممة للاستخدام في حالات الإنتاج.  

نماذج GitHub تستخدم Azure AI Content Safety. لا يمكن إيقاف تشغيل هذه الفلاتر كجزء من تجربة نماذج GitHub. إذا قررت استخدام النماذج عبر خدمة مدفوعة، يرجى تكوين فلاتر المحتوى لتلبية متطلباتك.  

هذه الخدمة تخضع لشروط ما قبل الإصدار الخاصة بـ GitHub.  

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمات الترجمة الآلية المعتمدة على الذكاء الاصطناعي. بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حساسة أو مهمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ نتيجة استخدام هذه الترجمة.