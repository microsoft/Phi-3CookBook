## GitHub modeli - Ograničena javna beta verzija

Dobrodošli na [GitHub Models](https://github.com/marketplace/models)! Sve je spremno za vas da istražite AI modele hostovane na Azure AI.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.sr.png)

Za više informacija o modelima dostupnim na GitHub Models, posetite [GitHub Model Marketplace](https://github.com/marketplace/models).

## Dostupni modeli

Svaki model ima svoj posvećeni playground i primer koda.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3 modeli u GitHub katalogu modela

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Početak rada

Postoji nekoliko osnovnih primera koji su spremni za pokretanje. Možete ih pronaći u direktorijumu sa primerima. Ako želite odmah da pređete na svoj omiljeni jezik, primeri su dostupni na sledećim jezicima:

- Python  
- JavaScript  
- cURL  

Takođe postoji posvećeno Codespaces okruženje za pokretanje primera i modela.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.sr.png)

## Primer koda

Ispod su primeri koda za nekoliko slučajeva upotrebe. Za dodatne informacije o Azure AI Inference SDK-u, pogledajte kompletnu dokumentaciju i primere.

## Postavljanje

1. Kreirajte personalni pristupni token  
Ne morate dodeljivati nikakve dozvole tokenu. Imajte na umu da će token biti poslat Microsoft servisu.

Da biste koristili kod ispod, kreirajte promenljivu okruženja i postavite token kao ključ za klijentski kod.

Ako koristite bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Ako ste u PowerShell-u:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Ako koristite Windows Command Prompt:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python primer

### Instalirajte zavisnosti  
Instalirajte Azure AI Inference SDK koristeći pip (zahteva: Python >=3.8):  

```
pip install azure-ai-inference
```  

### Pokrenite osnovni primer koda  

Ovaj primer demonstrira osnovni poziv API-ju za chat completions. Koristi GitHub AI endpoint za inferenciju modela i vaš GitHub token. Poziv je sinhron.  

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

### Pokrenite višekratni razgovor  

Ovaj primer demonstrira višekratni razgovor sa API-jem za chat completions. Kada koristite model za aplikaciju za četovanje, potrebno je da upravljate istorijom razgovora i šaljete najnovije poruke modelu.  

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

### Strimujte izlaz  

Za bolje korisničko iskustvo, preporučuje se strimovanje odgovora modela kako bi se prvi token prikazao ranije i izbeglo dugo čekanje na odgovor.  

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

### Instalirajte zavisnosti  

Instalirajte Node.js.  

Kopirajte sledeće linije teksta i sačuvajte ih kao fajl package.json unutar svog foldera.  

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

Napomena: @azure/core-sse je potreban samo kada strimujete odgovor chat completions API-ja.  

Otvorite terminal u ovom folderu i pokrenite npm install.  

Za svaki od sledećih primera koda, kopirajte sadržaj u fajl sample.js i pokrenite sa node sample.js.  

### Pokrenite osnovni primer koda  

Ovaj primer demonstrira osnovni poziv API-ju za chat completions. Koristi GitHub AI endpoint za inferenciju modela i vaš GitHub token. Poziv je sinhron.  

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

### Pokrenite višekratni razgovor  

Ovaj primer demonstrira višekratni razgovor sa API-jem za chat completions. Kada koristite model za aplikaciju za četovanje, potrebno je da upravljate istorijom razgovora i šaljete najnovije poruke modelu.  

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

### Strimujte izlaz  
Za bolje korisničko iskustvo, preporučuje se strimovanje odgovora modela kako bi se prvi token prikazao ranije i izbeglo dugo čekanje na odgovor.  

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

### Pokrenite osnovni primer koda  

Nalepite sledeće u shell:  

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

### Pokrenite višekratni razgovor  

Pozovite API za chat completions i prosledite istoriju četa:  

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

### Strimujte izlaz  

Ovo je primer pozivanja endpoint-a i strimovanja odgovora.  

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

## BESPLATNO korišćenje i ograničenja za GitHub modele  

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.sr.png)

[Ograničenja za playground i besplatno korišćenje API-ja](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) su dizajnirana da vam pomognu da eksperimentišete sa modelima i prototipirate svoju AI aplikaciju. Za korišćenje izvan ovih ograničenja, i kako biste svoju aplikaciju skalirali, potrebno je da obezbedite resurse putem Azure naloga i da se autentifikujete preko njega umesto GitHub personalnog pristupnog tokena. Ne morate menjati ništa drugo u svom kodu. Koristite ovaj link da saznate kako da pređete granice besplatnog nivoa u Azure AI.

### Obaveštenja  

Imajte na umu da kada radite sa modelom, eksperimentišete sa AI, tako da su greške u sadržaju moguće.  

Funkcionalnost je podložna različitim ograničenjima (uključujući broj zahteva po minutu, zahteva po danu, tokena po zahtevu i paralelnih zahteva) i nije dizajnirana za upotrebu u produkcionim slučajevima.  

GitHub modeli koriste Azure AI Content Safety. Ovi filteri ne mogu biti isključeni kao deo GitHub Models iskustva. Ako odlučite da koristite modele kroz plaćenu uslugu, konfigurišite svoje filtere sadržaja prema vašim zahtevima.  

Ova usluga je pod GitHub-ovim uslovima za pre-release verzije.  

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме који могу проистећи из коришћења овог превода.