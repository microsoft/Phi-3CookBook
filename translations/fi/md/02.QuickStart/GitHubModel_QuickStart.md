## GitHub-mallit - Rajoitettu julkinen beta

Tervetuloa [GitHub-mallit](https://github.com/marketplace/models) -sivustolle! Olemme valmiina tarjoamaan sinulle mahdollisuuden tutustua Azure AI:n isännöimiin tekoälymalleihin.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.fi.png)

Lisätietoja GitHub-malleista löydät [GitHub Model Marketplace](https://github.com/marketplace/models) -sivustolta.

## Saatavilla olevat mallit

Jokaisella mallilla on oma käyttöympäristönsä ja esimerkkikoodinsa.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3-mallit GitHub-mallikatalogissa

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Aloitusopas

Meillä on valmiita esimerkkejä, jotka voit suorittaa heti. Löydät ne samples-hakemistosta. Jos haluat aloittaa suoraan suosikkikielelläsi, löydät esimerkit seuraavilla kielillä:

- Python
- JavaScript
- cURL

Lisäksi on olemassa oma Codespaces-ympäristö mallien ja esimerkkien suorittamiseen.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.fi.png)

## Esimerkkikoodi

Alla on esimerkkikoodeja muutamista käyttötapauksista. Lisätietoja Azure AI Inference SDK:sta löydät täydellisestä dokumentaatiosta ja esimerkeistä.

## Asennus

1. Luo henkilökohtainen käyttöoikeustunnus  
Sinun ei tarvitse antaa tunnukselle erityisiä oikeuksia. Huomaa, että tunnus lähetetään Microsoftin palveluun.

Käyttääksesi alla olevia koodiesimerkkejä, luo ympäristömuuttuja, jossa asetat tunnuksesi avaimena asiakaskoodille.

Jos käytät bashia:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Jos käytät powershelliä:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Jos käytät Windowsin komentokehotetta:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python-esimerkki

### Riippuvuuksien asennus  
Asenna Azure AI Inference SDK pipillä (vaatii: Python >=3.8):  

```
pip install azure-ai-inference
```  

### Perusesimerkin suorittaminen  

Tämä esimerkki näyttää, kuinka tehdä peruskutsu chat completion -rajapintaan. Se käyttää GitHub AI -mallin inferenssipistettä ja GitHub-tunnustasi. Kutsu on synkroninen.  

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

### Monivaiheisen keskustelun suorittaminen  

Tämä esimerkki näyttää, kuinka käydä monivaiheista keskustelua chat completion -rajapinnan kanssa. Kun käytät mallia chat-sovelluksessa, sinun täytyy hallita keskustelun historiaa ja lähettää viimeisimmät viestit mallille.  

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

### Tulosten suoratoisto  

Parempaa käyttökokemusta varten kannattaa suoratoistaa mallin vastaus niin, että ensimmäinen sana näkyy nopeasti eikä pitkiä viiveitä tule.  

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

### Riippuvuuksien asennus  

Asenna Node.js.  

Kopioi seuraavat rivit tekstitiedostoon nimeltä package.json ja tallenna kansioosi.  

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

Huomio: @azure/core-sse tarvitaan vain, jos suoratoistat chat completion -vastauksia.  

Avaa terminaali tässä kansiossa ja suorita npm install.  

Kopioi alla olevien koodiesimerkkien sisältö tiedostoon sample.js ja suorita node sample.js.  

### Perusesimerkin suorittaminen  

Tämä esimerkki näyttää, kuinka tehdä peruskutsu chat completion -rajapintaan. Se käyttää GitHub AI -mallin inferenssipistettä ja GitHub-tunnustasi. Kutsu on synkroninen.  

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

### Monivaiheisen keskustelun suorittaminen  

Tämä esimerkki näyttää, kuinka käydä monivaiheista keskustelua chat completion -rajapinnan kanssa. Kun käytät mallia chat-sovelluksessa, sinun täytyy hallita keskustelun historiaa ja lähettää viimeisimmät viestit mallille.  

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

### Tulosten suoratoisto  
Parempaa käyttökokemusta varten kannattaa suoratoistaa mallin vastaus niin, että ensimmäinen sana näkyy nopeasti eikä pitkiä viiveitä tule.  

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

### Perusesimerkin suorittaminen  

Liitä seuraava shelliin:  

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

### Monivaiheisen keskustelun suorittaminen  

Kutsu chat completion -rajapintaa ja lähetä keskusteluhistoria:  

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

### Tulosten suoratoisto  

Tämä on esimerkki siitä, kuinka kutsutaan rajapintaa ja suoratoistetaan vastaus.  

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

## ILMAINEN käyttö ja GitHub-mallien rajoitukset  

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.fi.png)

[Playgroundin ja ilmaisen API-käytön rajoitukset](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) on suunniteltu auttamaan sinua kokeilemaan malleja ja prototyyppien kehittämisessä tekoälysovelluksillesi. Jos tarvitset käyttöä näiden rajoitusten yli ja haluat laajentaa sovellustasi, sinun on hankittava resurssit Azure-tililtä ja todennettava sieltä GitHubin henkilökohtaisen käyttöoikeustunnuksen sijaan. Sinun ei tarvitse muuttaa mitään muuta koodissasi. Käytä tätä linkkiä saadaksesi lisätietoja siitä, miten voit ylittää ilmaisen tason rajoitukset Azure AI:ssa.  

### Huomautukset  

Muista, että mallin kanssa toimiessasi kokeilet tekoälyä, joten sisällössä voi olla virheitä.  

Tämä ominaisuus on alisteinen erilaisille rajoituksille (kuten pyyntöjä minuutissa, pyyntöjä päivässä, tokeneita per pyyntö ja samanaikaisia pyyntöjä) eikä sitä ole suunniteltu tuotantokäyttöön.  

GitHub-mallit käyttävät Azure AI Content Safety -suodatusta. Näitä suodattimia ei voi poistaa käytöstä osana GitHub-mallien käyttöä. Jos päätät käyttää malleja maksullisen palvelun kautta, määritä sisältösuodattimesi vastaamaan vaatimuksiasi.  

Tämä palvelu on GitHubin ennakkoversioehtojen alainen.  

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisia tekoälyyn perustuvia käännöspalveluja käyttäen. Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon kohdalla suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.