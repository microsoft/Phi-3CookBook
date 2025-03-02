## GitHub modeli - Ograničena javna beta

Dobrodošli na [GitHub modeli](https://github.com/marketplace/models)! Sve je spremno da istražite AI modele hostirane na Azure AI.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.hr.png)

Za više informacija o modelima dostupnim na GitHub Modelima, posjetite [GitHub Model Marketplace](https://github.com/marketplace/models).

## Dostupni modeli

Svaki model ima vlastiti playground i primjerni kod.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3 modeli u GitHub katalogu modela

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Početak rada

Postoji nekoliko osnovnih primjera koji su spremni za pokretanje. Možete ih pronaći u direktoriju primjera. Ako želite odmah prijeći na svoj omiljeni jezik, primjere možete pronaći na sljedećim jezicima:

- Python
- JavaScript
- cURL

Također postoji posebno okruženje za Codespaces za pokretanje primjera i modela.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.hr.png)

## Primjeri koda

U nastavku su prikazani primjeri koda za nekoliko slučajeva korištenja. Za dodatne informacije o Azure AI Inference SDK-u, pogledajte potpunu dokumentaciju i primjere.

## Postavljanje

1. Kreirajte osobni pristupni token  
Nije potrebno dodijeliti nikakve dozvole tokenu. Imajte na umu da će token biti poslan Microsoftovoj usluzi.

Da biste koristili dolje navedene primjere koda, stvorite varijablu okruženja kako biste postavili svoj token kao ključ za klijentski kod.

Ako koristite bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Ako koristite PowerShell:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Ako koristite Windows Command Prompt:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python primjer

### Instalacija ovisnosti  
Instalirajte Azure AI Inference SDK pomoću pip-a (Zahtijeva: Python >=3.8):  

```
pip install azure-ai-inference
```  

### Pokrenite osnovni primjer koda  

Ovaj primjer prikazuje osnovni poziv API-ju za dovršavanje chata. Koristi GitHub AI model inference endpoint i vaš GitHub token. Poziv je sinkroniziran.  

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

### Pokrenite višestruki razgovor  

Ovaj primjer prikazuje višestruki razgovor s API-jem za dovršavanje chata. Kada koristite model za chat aplikaciju, morat ćete upravljati poviješću razgovora i poslati najnovije poruke modelu.  

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

### Streamajte izlaz  

Za bolje korisničko iskustvo, poželjet ćete streamati odgovor modela kako bi se prvi token pojavio što ranije i izbjegli čekanje na duge odgovore.  

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

### Instalacija ovisnosti  

Instalirajte Node.js.  

Kopirajte sljedeće retke teksta i spremite ih kao datoteku package.json unutar svoje mape.  

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

Napomena: @azure/core-sse je potreban samo kada streamate odgovor API-ja za dovršavanje chata.  

Otvorite terminal u ovoj mapi i pokrenite npm install.  

Za svaki od dolje navedenih primjera koda, kopirajte sadržaj u datoteku sample.js i pokrenite s node sample.js.  

### Pokrenite osnovni primjer koda  

Ovaj primjer prikazuje osnovni poziv API-ju za dovršavanje chata. Koristi GitHub AI model inference endpoint i vaš GitHub token. Poziv je sinkroniziran.  

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

### Pokrenite višestruki razgovor  

Ovaj primjer prikazuje višestruki razgovor s API-jem za dovršavanje chata. Kada koristite model za chat aplikaciju, morat ćete upravljati poviješću razgovora i poslati najnovije poruke modelu.  

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

### Streamajte izlaz  
Za bolje korisničko iskustvo, poželjet ćete streamati odgovor modela kako bi se prvi token pojavio što ranije i izbjegli čekanje na duge odgovore.  

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

### Pokrenite osnovni primjer koda  

Zalijepite sljedeće u terminal:  

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

### Pokrenite višestruki razgovor  

Pozovite API za dovršavanje chata i proslijedite povijest razgovora:  

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

### Streamajte izlaz  

Ovo je primjer pozivanja endpointa i streamanja odgovora.  

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

## BESPLATNO korištenje i ograničenja za GitHub modele  

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.hr.png)  

[Ograničenja za playground i besplatno korištenje API-ja](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) namijenjena su za eksperimentiranje s modelima i prototipiranje AI aplikacija. Za korištenje izvan tih ograničenja i za skaliranje vaše aplikacije, morate osigurati resurse putem Azure računa i autentificirati se putem njega umjesto svog GitHub osobnog pristupnog tokena. Ne trebate mijenjati ništa drugo u svom kodu. Koristite ovu poveznicu kako biste saznali kako premašiti ograničenja besplatnog sloja u Azure AI.

### Obavijesti  

Zapamtite da prilikom interakcije s modelom eksperimentirate s AI-jem, pa su moguće greške u sadržaju.  

Ova značajka podliježe raznim ograničenjima (uključujući zahtjeve po minuti, zahtjeve po danu, tokene po zahtjevu i istovremene zahtjeve) i nije namijenjena za proizvodne slučajeve korištenja.  

GitHub modeli koriste Azure AI Content Safety. Ovi filtri se ne mogu isključiti kao dio GitHub Model iskustva. Ako odlučite koristiti modele putem plaćene usluge, konfigurirajte svoje filtre sadržaja prema svojim potrebama.  

Ova usluga podliježe GitHub-ovim Uvjetima za predizdanje.  

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden koristeći usluge strojnog prevođenja pomoću umjetne inteligencije. Iako nastojimo osigurati točnost, molimo vas da budete svjesni da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne snosimo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.