## GitHub Modellek - Korlátozott Nyilvános Béta

Üdvözlünk a [GitHub Modellek](https://github.com/marketplace/models) oldalán! Minden készen áll arra, hogy felfedezd az Azure AI által hosztolt AI modelleket.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.hu.png)

További információért a GitHub Modelleken elérhető modellekről nézd meg a [GitHub Model Marketplace](https://github.com/marketplace/models) oldalt.

## Elérhető Modellek

Minden modellhez tartozik egy dedikált playground és példa kód.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3 Modellek a GitHub Modell Katalógusban

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Első Lépések

Néhány alapvető példa már készen áll arra, hogy lefuttasd őket. Ezeket a samples mappában találod. Ha egyből a kedvenc programozási nyelvedhez ugranál, az alábbi nyelveken találhatsz példákat:

- Python
- JavaScript
- cURL

Ezen kívül elérhető egy dedikált Codespaces környezet is a példák és modellek futtatásához.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.hu.png)

## Példa Kód

Az alábbiakban néhány használati esethez található példa kód. Az Azure AI Inference SDK-val kapcsolatos további információkért nézd meg a teljes dokumentációt és példákat.

## Beállítás

1. Hozz létre egy személyes hozzáférési tokent  
Nem kell engedélyeket adnod a tokennek. Jegyezd meg, hogy a tokent egy Microsoft szolgáltatásnak fogod elküldeni.

Ahhoz, hogy az alábbi kódrészleteket használd, hozz létre egy környezeti változót, hogy a tokent kulcsként állítsd be a klienskódhoz.

Ha bash-t használsz:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Ha PowerShell-t használsz:  
```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Ha Windows parancssort használsz:  
```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python Példa

### Függőségek telepítése  
Telepítsd az Azure AI Inference SDK-t pip segítségével (Követelmény: Python >=3.8):  

```
pip install azure-ai-inference
```  

### Futtass egy alapvető kódrészletet  

Ez a példa bemutat egy alapvető hívást a chat completion API-hoz. Az GitHub AI modell inference végpontját és a GitHub tokenedet használja. A hívás szinkron módon történik.  

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

### Többmenetes beszélgetés futtatása  

Ez a példa bemutat egy többmenetes beszélgetést a chat completion API-val. Ha a modellt egy chat alkalmazáshoz használod, kezelni kell a beszélgetés előzményeit, és az aktuális üzeneteket kell elküldened a modellnek.  

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

### Kimenet streamelése  

A jobb felhasználói élmény érdekében érdemes a modell válaszát streamelni, hogy az első token korán megjelenjen, és ne kelljen hosszú válaszokra várni.  

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

### Függőségek telepítése  

Telepítsd a Node.js-t.  

Másold ki az alábbi szöveget, és mentsd el package.json fájlként a mappádba.  

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

Megjegyzés: Az @azure/core-sse csak akkor szükséges, ha a chat completion válaszát streamelni szeretnéd.  

Nyiss egy terminál ablakot ebben a mappában, és futtasd az npm install parancsot.  

Az alábbi kódrészletek mindegyikéhez másold be a tartalmat egy sample.js nevű fájlba, és futtasd a node sample.js paranccsal.  

### Futtass egy alapvető kódrészletet  

Ez a példa bemutat egy alapvető hívást a chat completion API-hoz. Az GitHub AI modell inference végpontját és a GitHub tokenedet használja. A hívás szinkron módon történik.  

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

### Többmenetes beszélgetés futtatása  

Ez a példa bemutat egy többmenetes beszélgetést a chat completion API-val. Ha a modellt egy chat alkalmazáshoz használod, kezelni kell a beszélgetés előzményeit, és az aktuális üzeneteket kell elküldened a modellnek.  

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

### Kimenet streamelése  

A jobb felhasználói élmény érdekében érdemes a modell válaszát streamelni, hogy az első token korán megjelenjen, és ne kelljen hosszú válaszokra várni.  

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

### Futtass egy alapvető kódrészletet  

Illeszd be az alábbiakat egy shell-be:  

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

### Többmenetes beszélgetés futtatása  

Hívd meg a chat completion API-t, és add át a beszélgetés előzményeit:  

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

### Kimenet streamelése  

Ez egy példa az endpoint hívására és a válasz streamelésére.  

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

## INGYENES Használat és Korlátozások a GitHub Modellekhez  

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.hu.png)  

A [playground és az ingyenes API használatának korlátai](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) segítenek a modellekkel való kísérletezésben és az AI alkalmazásod prototípusának elkészítésében. Ha ezen korlátokon túl szeretnéd használni a szolgáltatást, és skálázni szeretnéd az alkalmazásodat, Azure fiókból kell erőforrásokat biztosítanod, és onnan kell hitelesítened ahelyett, hogy a GitHub személyes hozzáférési tokenedet használnád. A kódban más változtatást nem kell végezned. Használd ezt a linket, hogy megtudd, hogyan léphetsz túl az ingyenes szint korlátain az Azure AI-ban.  

### Nyilatkozatok  

Ne feledd, amikor egy modellel lépsz interakcióba, AI-t tesztelsz, így tartalmi hibák előfordulhatnak.  

A funkció különböző korlátoknak van alávetve (beleértve a kérések számát percenként, naponta, tokenek számát kéréseként, és egyidejű kérések számát), és nem alkalmas éles használati esetekre.  

A GitHub Modellek az Azure AI Tartalombiztonságot használják. Ezek a szűrők nem kapcsolhatók ki a GitHub Modellek élmény részeként. Ha úgy döntesz, hogy fizetős szolgáltatáson keresztül használod a modelleket, konfiguráld a tartalomszűrőidet az igényeid szerint.  

Ez a szolgáltatás a GitHub előzetes kiadási feltételei alá tartozik.  

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítószolgáltatásokkal lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.