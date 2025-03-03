## GitHub modeli - Omejena javna beta

Dobrodošli v [GitHub modeli](https://github.com/marketplace/models)! Vse je pripravljeno, da raziščete AI modele, gostovane na Azure AI.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.sl.png)

Za več informacij o modelih, ki so na voljo na GitHub Modelih, obiščite [GitHub Model Marketplace](https://github.com/marketplace/models).

## Razpoložljivi modeli

Vsak model ima svoj namenski preizkusni prostor in vzorčno kodo.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3 modeli v katalogu GitHub Model

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Začetek

Na voljo je nekaj osnovnih primerov, ki jih lahko takoj zaženete. Najdete jih v imeniku z vzorci. Če želite začeti neposredno v vašem priljubljenem jeziku, lahko primere najdete v naslednjih jezikih:

- Python
- JavaScript
- cURL

Na voljo je tudi namensko okolje Codespaces za izvajanje vzorcev in modelov.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.sl.png)

## Vzorčna koda

Spodaj so primeri kod za nekaj primerov uporabe. Za dodatne informacije o Azure AI Inference SDK si oglejte celotno dokumentacijo in primere.

## Nastavitev

1. Ustvarite osebni dostopni žeton  
Žetonu vam ni treba dodeliti nobenih dovoljenj. Upoštevajte, da bo žeton poslan Microsoftovi storitvi.

Za uporabo spodnjih primerov kode ustvarite okoljsko spremenljivko, da nastavite svoj žeton kot ključ za odjemalsko kodo.

Če uporabljate bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Če uporabljate PowerShell:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Če uporabljate Windows Command Prompt:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python primer

### Namestitev odvisnosti  
Namestite Azure AI Inference SDK z uporabo pip (zahteva: Python >=3.8):  

```
pip install azure-ai-inference
```  

### Zaženite osnovni primer kode  

Ta primer prikazuje osnovni klic API-ja za dokončanje klepeta. Uporablja se GitHub AI model in vaš GitHub žeton. Klic je sinhron.  

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

### Zaženite večkratni pogovor  

Ta primer prikazuje večkratni pogovor z API-jem za dokončanje klepeta. Pri uporabi modela za aplikacijo za klepet boste morali upravljati zgodovino pogovora in poslati najnovejša sporočila modelu.  

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

### Pretok izhoda  

Za boljšo uporabniško izkušnjo boste želeli pretakati odziv modela, da se prvi token prikaže takoj in se izognete čakanju na dolge odgovore.  

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

### Namestitev odvisnosti  

Namestite Node.js.  

Kopirajte naslednje vrstice besedila in jih shranite kot datoteko package.json v svojo mapo.  

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

Opomba: @azure/core-sse je potreben samo, če pretakate odziv dokončanja klepeta.  

Odprite terminal v tej mapi in zaženite npm install.  

Za vsak spodnji primer kode kopirajte vsebino v datoteko sample.js in jo zaženite z node sample.js.  

### Zaženite osnovni primer kode  

Ta primer prikazuje osnovni klic API-ja za dokončanje klepeta. Uporablja se GitHub AI model in vaš GitHub žeton. Klic je sinhron.  

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

### Zaženite večkratni pogovor  

Ta primer prikazuje večkratni pogovor z API-jem za dokončanje klepeta. Pri uporabi modela za aplikacijo za klepet boste morali upravljati zgodovino pogovora in poslati najnovejša sporočila modelu.  

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

### Pretok izhoda  

Za boljšo uporabniško izkušnjo boste želeli pretakati odziv modela, da se prvi token prikaže takoj in se izognete čakanju na dolge odgovore.  

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

### Zaženite osnovni primer kode  

Prilepite naslednje v ukazno lupino:  

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

### Zaženite večkratni pogovor  

Pokličite API za dokončanje klepeta in posredujte zgodovino klepeta:  

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

### Pretok izhoda  

To je primer klica končne točke in pretakanja odziva.  

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

## BREZPLAČNA uporaba in omejitve hitrosti za GitHub modele  

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.sl.png)  

[Omejitve hitrosti za preizkusni prostor in brezplačno uporabo API-ja](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) so namenjene pomoči pri eksperimentiranju z modeli in prototipiranju vaše AI aplikacije. Za uporabo, ki presega te omejitve, in za povečanje vaše aplikacije morate zagotoviti vire iz Azure računa in se od tam avtenticirati namesto z vašim GitHub osebnim dostopnim žetonom. V kodi ni potrebno ničesar drugega spremeniti. Uporabite to povezavo, da odkrijete, kako preseči omejitve brezplačne stopnje v Azure AI.  

### Razkritja  

Zapomnite si, da pri interakciji z modelom eksperimentirate z AI, zato so možne napake v vsebini.  

Funkcija je podvržena različnim omejitvam (vključno z zahtevami na minuto, zahtevami na dan, tokeni na zahtevo in sočasnimi zahtevami) in ni zasnovana za uporabo v produkcijskih primerih.  

GitHub modeli uporabljajo Azure AI Content Safety. Te filtre ni mogoče izklopiti kot del izkušnje GitHub modelov. Če se odločite za uporabo modelov prek plačljive storitve, prosimo, konfigurirajte filtre vsebine tako, da ustrezajo vašim zahtevam.  

Ta storitev je pod GitHub-ovimi pogoji za predhodno izdajo.  

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo strojnih AI prevajalskih storitev. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.