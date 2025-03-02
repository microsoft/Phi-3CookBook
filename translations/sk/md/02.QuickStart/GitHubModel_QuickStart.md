## GitHub Modely - Obmedzená verejná beta verzia

Vitajte v [GitHub Modely](https://github.com/marketplace/models)! Máme všetko pripravené, aby ste mohli preskúmať AI modely hostované na Azure AI.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.sk.png)

Viac informácií o modeloch dostupných na GitHub Modely nájdete na [GitHub Model Marketplace](https://github.com/marketplace/models)

## Dostupné modely

Každý model má vyhradené prostredie na testovanie a ukážkový kód.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3 modely v GitHub Model Katalógu

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Začíname

Máme pripravených niekoľko základných príkladov, ktoré môžete ihneď spustiť. Nájdete ich v adresári s ukážkami. Ak chcete prejsť priamo na svoj obľúbený jazyk, ukážky nájdete v nasledujúcich jazykoch:

- Python
- JavaScript
- cURL

K dispozícii je tiež vyhradené prostredie Codespaces na spúšťanie ukážok a modelov.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.sk.png)

## Ukážkový kód 

Nižšie sú uvedené ukážky kódu pre niekoľko prípadov použitia. Pre ďalšie informácie o Azure AI Inference SDK si pozrite kompletnú dokumentáciu a ukážky.

## Nastavenie 

1. Vytvorte si osobný prístupový token  
Nemusíte tokenu priradiť žiadne oprávnenia. Upozorňujeme, že token bude odoslaný do služby Microsoft.

Na použitie nižšie uvedených ukážok kódu vytvorte premennú prostredia, aby ste nastavili svoj token ako kľúč pre klientský kód.

Ak používate bash:
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```
Ak používate PowerShell:

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```

Ak používate príkazový riadok Windows:

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```

## Ukážka v Pythone

### Inštalácia závislostí  
Nainštalujte Azure AI Inference SDK pomocou pip (Požiadavka: Python >=3.8):

```
pip install azure-ai-inference
```
### Spustenie základnej ukážky kódu

Táto ukážka demonštruje základné volanie API na dokončenie chatu. Využíva GitHub AI model inferenčný endpoint a váš GitHub token. Volanie je synchronné.

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

### Viackolová konverzácia

Táto ukážka demonštruje viackolovú konverzáciu s API na dokončenie chatu. Pri použití modelu na chatovú aplikáciu budete musieť spravovať históriu tejto konverzácie a posielať modelu najnovšie správy.

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

### Streamovanie výstupu

Pre lepší používateľský zážitok budete chcieť streamovať odpoveď modelu, aby sa prvý token zobrazil okamžite a nečakali ste na dlhé odpovede.

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

### Inštalácia závislostí

Nainštalujte Node.js.

Skopírujte nasledujúce riadky textu a uložte ich ako súbor package.json vo vašom priečinku.

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

Poznámka: @azure/core-sse je potrebný iba v prípade, že streamujete odpoveď na dokončenie chatu.

Otvorte terminál v tomto priečinku a spustite npm install.

Pre každý z nižšie uvedených úryvkov kódu skopírujte obsah do súboru sample.js a spustite ho pomocou node sample.js.

### Spustenie základnej ukážky kódu

Táto ukážka demonštruje základné volanie API na dokončenie chatu. Využíva GitHub AI model inferenčný endpoint a váš GitHub token. Volanie je synchronné.

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

### Viackolová konverzácia

Táto ukážka demonštruje viackolovú konverzáciu s API na dokončenie chatu. Pri použití modelu na chatovú aplikáciu budete musieť spravovať históriu tejto konverzácie a posielať modelu najnovšie správy.

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

### Streamovanie výstupu
Pre lepší používateľský zážitok budete chcieť streamovať odpoveď modelu, aby sa prvý token zobrazil okamžite a nečakali ste na dlhé odpovede.

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

### Spustenie základnej ukážky kódu

Vložte nasledujúce do shellu:

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
### Viackolová konverzácia

Zavolajte API na dokončenie chatu a odovzdajte históriu chatu:

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
### Streamovanie výstupu

Toto je príklad volania endpointu a streamovania odpovede.

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

## BEZPLATNÉ používanie a obmedzenia rýchlosti pre GitHub Modely

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.sk.png)

[Obmedzenia rýchlosti pre testovacie prostredie a bezplatné používanie API](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) sú navrhnuté tak, aby vám pomohli experimentovať s modelmi a vytvárať prototypy vašej AI aplikácie. Pre použitie nad tieto limity a pre škálovanie vašej aplikácie musíte zabezpečiť zdroje z Azure účtu a autentifikovať sa odtiaľ namiesto vášho osobného GitHub tokenu. Nemusíte meniť nič iné vo vašom kóde. Použite tento odkaz na objavenie, ako prekročiť bezplatné limity v Azure AI.

### Upozornenia

Pamätajte, že pri interakcii s modelom experimentujete s AI, takže môžu nastať chyby v obsahu.

Funkcia podlieha rôznym obmedzeniam (vrátane požiadaviek za minútu, požiadaviek za deň, tokenov na požiadavku a súbežných požiadaviek) a nie je navrhnutá na produkčné použitie.

GitHub Modely používajú Azure AI Content Safety. Tieto filtre nie je možné vypnúť v rámci skúsenosti s GitHub Modely. Ak sa rozhodnete používať modely prostredníctvom platenej služby, nakonfigurujte si filtre obsahu podľa svojich požiadaviek.

Táto služba podlieha predbežným podmienkam GitHub.

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových prekladateľských služieb založených na umelej inteligencii. Hoci sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za záväzný zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.