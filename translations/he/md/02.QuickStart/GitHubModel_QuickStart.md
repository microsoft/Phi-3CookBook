## GitHub Models - בטא ציבורית מוגבלת

ברוכים הבאים ל-[GitHub Models](https://github.com/marketplace/models)! אנחנו מוכנים ומזומנים שתחקור את מודלי ה-AI המופעלים על Azure AI.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.he.png)

למידע נוסף על המודלים הזמינים ב-GitHub Models, עיין ב-[GitHub Model Marketplace](https://github.com/marketplace/models).

## מודלים זמינים

לכל מודל יש סביבת ניסוי ייעודית ודוגמאות קוד.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### מודלים של Phi-3 ב-GitHub Model Catalog

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## תחילת העבודה

יש מספר דוגמאות בסיסיות שמוכנות להרצה. ניתן למצוא אותן בתיקיית הדוגמאות. אם תרצה לגשת ישירות לשפה המועדפת עליך, תוכל למצוא דוגמאות בשפות הבאות:

- Python  
- JavaScript  
- cURL  

בנוסף, קיימת סביבת Codespaces ייעודית להרצת הדוגמאות והמודלים.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.he.png)

## דוגמאות קוד

להלן קטעי קוד לדוגמא למספר מקרי שימוש. למידע נוסף על Azure AI Inference SDK, עיין בתיעוד המלא ובדוגמאות.

## הגדרות ראשוניות

1. צור אסימון גישה אישי  
אין צורך להעניק הרשאות לאסימון. שים לב שהאסימון יישלח לשירות של Microsoft.

כדי להשתמש בקטעי הקוד שלמטה, צור משתנה סביבה והגדר את האסימון כמפתח לקוד הלקוח.

אם אתה משתמש ב-bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
אם אתה משתמש ב-powershell:  
```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

אם אתה משתמש ב-Windows command prompt:  
```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## דוגמת Python

### התקנת תלותים  
התקן את Azure AI Inference SDK באמצעות pip (דרישות: Python >=3.8):  

```
pip install azure-ai-inference
```  

### הרצת דוגמה בסיסית

דוגמה זו מדגימה קריאה בסיסית ל-API להשלמת צ'אט. היא משתמשת בנקודת הקצה של GitHub AI Model Inference ובאסימון GitHub שלך. הקריאה היא סינכרונית.

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

### הרצת שיחה רב-שלבית

דוגמה זו מדגימה שיחה רב-שלבית עם ה-API להשלמת צ'אט. כשמשתמשים במודל ליישום צ'אט, יש לנהל את היסטוריית השיחה ולשלוח את ההודעות האחרונות למודל.

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

### סטרימינג של הפלט

כדי לשפר את חוויית המשתמש, מומלץ להזרים את תגובת המודל כך שהטוקן הראשון יופיע במהירות, ותימנע המתנה ממושכת לתגובות ארוכות.

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

### התקנת תלותים  

התקן Node.js.  

העתק את השורות הבאות ושמור אותן כקובץ בשם package.json בתוך התיקייה שלך.  

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

הערה: @azure/core-sse נדרש רק כאשר מזרים את תגובת השלמת הצ'אט.  

פתח חלון טרמינל בתיקייה זו והרץ npm install.  

עבור כל אחד מקטעי הקוד למטה, העתק את התוכן לקובץ בשם sample.js והרץ באמצעות node sample.js.  

### הרצת דוגמה בסיסית

דוגמה זו מדגימה קריאה בסיסית ל-API להשלמת צ'אט. היא משתמשת בנקודת הקצה של GitHub AI Model Inference ובאסימון GitHub שלך. הקריאה היא סינכרונית.

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

### הרצת שיחה רב-שלבית

דוגמה זו מדגימה שיחה רב-שלבית עם ה-API להשלמת צ'אט. כשמשתמשים במודל ליישום צ'אט, יש לנהל את היסטוריית השיחה ולשלוח את ההודעות האחרונות למודל.

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

### סטרימינג של הפלט  
כדי לשפר את חוויית המשתמש, מומלץ להזרים את תגובת המודל כך שהטוקן הראשון יופיע במהירות, ותימנע המתנה ממושכת לתגובות ארוכות.

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

### הרצת דוגמה בסיסית  

הדבק את הפקודות הבאות ב-shell:  

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

### הרצת שיחה רב-שלבית  

קרא ל-API להשלמת צ'אט והעבר את היסטוריית השיחה:  

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

### סטרימינג של הפלט  

זהו דוגמה לקריאה לנקודת הקצה ולהזרמת התגובה.  

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

## שימוש חינמי ומגבלות קצב עבור GitHub Models  

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.he.png)  

המגבלות לשימוש החינמי ב-API ובסביבת הניסוי ([rate limits for the playground and free API usage](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits)) נועדו לעזור לך להתנסות במודלים ולבנות אבטיפוס לאפליקציית ה-AI שלך. לשימוש מעבר למגבלות אלו, וכדי להרחיב את האפליקציה שלך, עליך להקצות משאבים מחשבון Azure ולאמת משם במקום להשתמש באסימון הגישה האישי של GitHub. אין צורך לשנות דבר בקוד שלך. השתמש בקישור זה כדי לגלות כיצד לעבור את מגבלות השימוש החינמיות ב-Azure AI.

### גילויים  

זכור, בעת אינטראקציה עם מודל, אתה מתנסה ב-AI ולכן ייתכנו טעויות בתוכן.

התכונה כפופה למגבלות שונות (כולל בקשות לדקה, בקשות ליום, טוקנים לכל בקשה ובקשות בו-זמניות) ואינה מיועדת לשימוש במקרי ייצור.

GitHub Models משתמש ב-Azure AI Content Safety. מסננים אלו לא ניתנים לביטול כחלק מהשימוש ב-GitHub Models. אם תבחר להפעיל מודלים דרך שירות בתשלום, תוכל להגדיר את מסנני התוכן שלך בהתאם לדרישותיך.

שירות זה פועל תחת תנאי השחרור המוקדם של GitHub.  

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. בעוד שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ להיעזר בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעות משימוש בתרגום זה.