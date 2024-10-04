## Modèles GitHub - Bêta publique limitée

Bienvenue sur [GitHub Models](https://github.com/marketplace/models) ! Tout est prêt pour que vous puissiez explorer les modèles d'IA hébergés sur Azure AI.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.a652f32407f52c16c528c26d70462aba0e55e3ff90d17ebbc9dffd9533c39363.fr.png)

Pour plus d'informations sur les modèles disponibles sur GitHub Models, consultez le [GitHub Model Marketplace](https://github.com/marketplace/models).

## Modèles disponibles

Chaque modèle dispose d'un espace de test dédié et de code d'exemple.

![Phi-3Model_Github](../../../../translated_images/GitHub_ModelPlay.e87859d6934a9e70830479431732ecc1826348036ebb998882091be8fa5d4fe7.fr.png)

### Modèles Phi-3 dans le catalogue de modèles GitHub

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Pour commencer

Quelques exemples de base sont prêts à être exécutés. Vous pouvez les trouver dans le répertoire des exemples. Si vous souhaitez aller directement à votre langage préféré, vous pouvez trouver les exemples dans les langues suivantes :

- Python
- JavaScript
- cURL

Il y a aussi un environnement Codespaces dédié pour exécuter les exemples et les modèles.

![Pour commencer](../../../../translated_images/GitHub_ModelGetStarted.7eddfc63957b37d8cf9803ec7073b3545f5002d3dae7ab3034ad5fec267e6beb.fr.png)

## Code d'exemple

Voici quelques extraits de code pour quelques cas d'utilisation. Pour plus d'informations sur le SDK d'inférence Azure AI, consultez la documentation complète et les exemples.

## Configuration

1. Créez un jeton d'accès personnel
Vous n'avez pas besoin de donner des permissions au jeton. Notez que le jeton sera envoyé à un service Microsoft.

Pour utiliser les extraits de code ci-dessous, créez une variable d'environnement pour définir votre jeton comme clé pour le code client.

Si vous utilisez bash :
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```
Si vous êtes sous powershell :

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```

Si vous utilisez l'invite de commande Windows :

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```

## Exemple Python

### Installer les dépendances
Installez le SDK d'inférence Azure AI en utilisant pip (Nécessite : Python >=3.8) :

```
pip install azure-ai-inference
```
### Exécuter un exemple de code de base

Cet exemple montre un appel de base à l'API de complétion de chat. Il utilise le point de terminaison d'inférence du modèle AI de GitHub et votre jeton GitHub. L'appel est synchrone.

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

### Exécuter une conversation multi-tours

Cet exemple montre une conversation multi-tours avec l'API de complétion de chat. Lorsque vous utilisez le modèle pour une application de chat, vous devez gérer l'historique de cette conversation et envoyer les derniers messages au modèle.

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

### Diffuser la sortie

Pour une meilleure expérience utilisateur, vous voudrez diffuser la réponse du modèle afin que le premier jeton apparaisse rapidement et que vous évitiez d'attendre des réponses longues.

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

### Installer les dépendances

Installez Node.js.

Copiez les lignes de texte suivantes et enregistrez-les sous le nom de fichier package.json dans votre dossier.

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

Note : @azure/core-sse n'est nécessaire que lorsque vous diffusez la réponse des complétions de chat.

Ouvrez une fenêtre de terminal dans ce dossier et exécutez npm install.

Pour chacun des extraits de code ci-dessous, copiez le contenu dans un fichier sample.js et exécutez-le avec node sample.js.

### Exécuter un exemple de code de base

Cet exemple montre un appel de base à l'API de complétion de chat. Il utilise le point de terminaison d'inférence du modèle AI de GitHub et votre jeton GitHub. L'appel est synchrone.

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

### Exécuter une conversation multi-tours

Cet exemple montre une conversation multi-tours avec l'API de complétion de chat. Lorsque vous utilisez le modèle pour une application de chat, vous devez gérer l'historique de cette conversation et envoyer les derniers messages au modèle.

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

### Diffuser la sortie
Pour une meilleure expérience utilisateur, vous voudrez diffuser la réponse du modèle afin que le premier jeton apparaisse rapidement et que vous évitiez d'attendre des réponses longues.

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

### Exécuter un exemple de code de base

Collez ce qui suit dans un shell :

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
### Exécuter une conversation multi-tours

Appelez l'API de complétion de chat et passez l'historique du chat :

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
### Diffuser la sortie

Voici un exemple d'appel du point de terminaison et de diffusion de la réponse.

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

## Utilisation GRATUITE et limites de taux pour les modèles GitHub

![Catalogue de modèles](../../../../translated_images/GitHub_Model.7cf5115ec8870189517837690a06a18f35716f5b491a315303414a42cf9f9a4e.fr.png)

Les [limites de taux pour l'utilisation du terrain de jeu et de l'API gratuite](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) sont destinées à vous aider à expérimenter avec les modèles et à prototyper votre application d'IA. Pour une utilisation au-delà de ces limites, et pour mettre votre application à l'échelle, vous devez provisionner des ressources à partir d'un compte Azure et vous authentifier depuis là au lieu de votre jeton d'accès personnel GitHub. Vous n'avez pas besoin de changer quoi que ce soit d'autre dans votre code. Utilisez ce lien pour découvrir comment aller au-delà des limites du niveau gratuit dans Azure AI.

### Divulgations

Rappelez-vous qu'en interagissant avec un modèle, vous expérimentez avec l'IA, donc des erreurs de contenu sont possibles.

La fonctionnalité est soumise à diverses limites (y compris les demandes par minute, les demandes par jour, les jetons par demande et les demandes simultanées) et n'est pas conçue pour des cas d'utilisation en production.

Les modèles GitHub utilisent Azure AI Content Safety. Ces filtres ne peuvent pas être désactivés dans le cadre de l'expérience GitHub Models. Si vous décidez d'utiliser des modèles via un service payant, veuillez configurer vos filtres de contenu pour répondre à vos besoins.

Ce service est soumis aux conditions de pré-version de GitHub.

**Avertissement** :
Ce document a été traduit en utilisant des services de traduction automatisée par IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations cruciales, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.