## GitHub-modeller - Begränsad offentlig beta

Välkommen till [GitHub Models](https://github.com/marketplace/models)! Vi har allt redo för dig att utforska AI-modeller som är värdade på Azure AI.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.sv.png)

För mer information om modellerna som finns tillgängliga på GitHub Models, kolla in [GitHub Model Marketplace](https://github.com/marketplace/models)

## Tillgängliga modeller

Varje modell har en dedikerad lekplats och exempel på kod 

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3-modeller i GitHub Model Catalog

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Kom igång

Det finns några grundläggande exempel som är redo att köras. Du hittar dem i samples-katalogen. Om du vill hoppa direkt till ditt favoritprogrammeringsspråk hittar du exemplen i följande språk:

- Python
- JavaScript
- cURL

Det finns också en dedikerad Codespaces-miljö för att köra exemplen och modellerna. 

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.sv.png)

## Exempel på kod 

Nedan finns exempel på kodsnuttar för några användningsområden. För ytterligare information om Azure AI Inference SDK, se fullständig dokumentation och exempel.

## Installation 

1. Skapa en personlig åtkomsttoken  
Du behöver inte ge några behörigheter till token. Observera att token kommer att skickas till en Microsoft-tjänst.

För att använda kodsnuttarna nedan, skapa en miljövariabel för att ställa in din token som nyckel för klientkoden.

Om du använder bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Om du använder powershell:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Om du använder Windows-kommandotolken:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python-exempel

### Installera beroenden  
Installera Azure AI Inference SDK med pip (Kräver: Python >=3.8):  

```
pip install azure-ai-inference
```  

### Kör ett grundläggande kodexempel  

Detta exempel visar ett grundläggande anrop till chat completion API. Det använder GitHub AI-modellens inferensendpoint och din GitHub-token. Anropet är synkront.  

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

### Kör en konversation med flera turer  

Detta exempel visar en konversation med flera turer med chat completion API. När du använder modellen för en chattapplikation behöver du hantera historiken för den konversationen och skicka de senaste meddelandena till modellen.  

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

### Strömma utdata  

För en bättre användarupplevelse vill du strömma modellens svar så att den första token visas tidigt och du undviker att vänta på långa svar.  

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

### Installera beroenden  

Installera Node.js.  

Kopiera följande rader text och spara dem som en fil package.json i din mapp.  

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

Obs: @azure/core-sse behövs endast när du strömmar svar från chat completions.  

Öppna ett terminalfönster i denna mapp och kör npm install.  

För varje kodsnutt nedan, kopiera innehållet till en fil sample.js och kör med node sample.js.  

### Kör ett grundläggande kodexempel  

Detta exempel visar ett grundläggande anrop till chat completion API. Det använder GitHub AI-modellens inferensendpoint och din GitHub-token. Anropet är synkront.  

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

### Kör en konversation med flera turer  

Detta exempel visar en konversation med flera turer med chat completion API. När du använder modellen för en chattapplikation behöver du hantera historiken för den konversationen och skicka de senaste meddelandena till modellen.  

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

### Strömma utdata  
För en bättre användarupplevelse vill du strömma modellens svar så att den första token visas tidigt och du undviker att vänta på långa svar.  

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

### Kör ett grundläggande kodexempel  

Klistra in följande i ett shell:  

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

### Kör en konversation med flera turer  

Anropa chat completion API och skicka med chattens historik:  

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

### Strömma utdata  

Detta är ett exempel på hur man anropar endpointen och strömmar svaret.  

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

## GRATIS användning och gränser för GitHub-modeller  

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.sv.png)

[Gränserna för lekplatsen och gratis API-användning](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) är avsedda för att hjälpa dig att experimentera med modeller och prototypa din AI-applikation. För användning utöver dessa gränser, och för att skala upp din applikation, måste du tillhandahålla resurser från ett Azure-konto och autentisera därifrån istället för med din GitHub personliga åtkomsttoken. Du behöver inte ändra något annat i din kod. Använd denna länk för att upptäcka hur du går bortom gratisnivåns gränser i Azure AI.  

### Utlåtanden  

Kom ihåg att när du interagerar med en modell experimenterar du med AI, så innehållsfel kan förekomma.  

Funktionen är föremål för olika gränser (inklusive förfrågningar per minut, förfrågningar per dag, tokens per förfrågan och samtidiga förfrågningar) och är inte utformad för produktionsanvändning.  

GitHub Models använder Azure AI Content Safety. Dessa filter kan inte stängas av som en del av GitHub Models-upplevelsen. Om du väljer att använda modeller genom en betald tjänst, vänligen konfigurera dina innehållsfilter för att möta dina krav.  

Denna tjänst omfattas av GitHubs förhandsutgåvetermer.  

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-baserade maskinöversättningstjänster. Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för missförstånd eller feltolkningar som uppstår vid användning av denna översättning.