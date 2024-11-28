# **Utiliser Phi-3 dans Ollama**

[Ollama](https://ollama.com) permet à plus de personnes de déployer directement des LLM ou SLM open source via des scripts simples, et peut également créer des API pour aider aux scénarios d'application locaux de Copilot.

## **1. Installation**

Ollama prend en charge l'exécution sur Windows, macOS et Linux. Vous pouvez installer Ollama via ce lien ([https://ollama.com/download](https://ollama.com/download)). Après une installation réussie, vous pouvez utiliser directement le script Ollama pour appeler Phi-3 via une fenêtre de terminal. Vous pouvez voir toutes les [bibliothèques disponibles dans Ollama](https://ollama.com/library). Si vous ouvrez ce dépôt dans un Codespace, Ollama sera déjà installé.

```bash

ollama run phi3

```

> [!NOTE]
> Le modèle sera téléchargé lors de la première exécution. Bien sûr, vous pouvez également spécifier directement le modèle Phi-3 téléchargé. Nous prenons WSL comme exemple pour exécuter la commande. Une fois le modèle téléchargé avec succès, vous pouvez interagir directement sur le terminal.

![run](../../../../translated_images/ollama_run.302aa6484e50a7f8f09b40c787dc22eea10525cac6287c92825c8fc80c012c48.fr.png)

## **2. Appeler l'API phi-3 depuis Ollama**

Si vous souhaitez appeler l'API Phi-3 générée par Ollama, vous pouvez utiliser cette commande dans le terminal pour démarrer le serveur Ollama.

```bash

ollama serve

```

> [!NOTE]
> Si vous utilisez MacOS ou Linux, veuillez noter que vous pouvez rencontrer l'erreur suivante **"Error: listen tcp 127.0.0.1:11434: bind: address already in use"** Vous pouvez obtenir cette erreur lors de l'exécution de la commande. Vous pouvez soit ignorer cette erreur, car elle indique généralement que le serveur est déjà en cours d'exécution, soit arrêter et redémarrer Ollama :

**macOS**

```bash

brew services restart ollama

```

**Linux**

```bash

sudo systemctl stop ollama

```

Ollama prend en charge deux API : generate et chat. Vous pouvez appeler l'API de modèle fournie par Ollama selon vos besoins, en envoyant des requêtes au service local fonctionnant sur le port 11434.

**Chat**

```bash

curl http://127.0.0.1:11434/api/chat -d '{
  "model": "phi3",
  "messages": [
    {
      "role": "system",
      "content": "Your are a python developer."
    },
    {
      "role": "user",
      "content": "Help me generate a bubble algorithm"
    }
  ],
  "stream": false
  
}'


```

Voici le résultat dans Postman

![Capture d'écran des résultats JSON pour la requête chat](../../../../translated_images/ollama_chat.25d29e9741e1daa8efd30ca36e60008b6f2841edb544ca8167645e0ec750c72a.fr.png)

```bash

curl http://127.0.0.1:11434/api/generate -d '{
  "model": "phi3",
  "prompt": "<|system|>Your are my AI assistant.<|end|><|user|>tell me how to learn AI<|end|><|assistant|>",
  "stream": false
}'


```

Voici le résultat dans Postman

![Capture d'écran des résultats JSON pour la requête generate](../../../../translated_images/ollama_gen.523df35c3c34f0ada4770f77c9bb68f55442958adffe73ba5ae03e417ff9a781.fr.png)

## Ressources supplémentaires

Consultez la liste des modèles disponibles dans Ollama dans [leur bibliothèque](https://ollama.com/library).

Récupérez votre modèle depuis le serveur Ollama avec cette commande

```bash
ollama pull phi3
```

Exécutez le modèle avec cette commande

```bash
ollama run phi3
```

***Note :*** Visitez ce lien [https://github.com/ollama/ollama/blob/main/docs/api.md](https://github.com/ollama/ollama/blob/main/docs/api.md) pour en savoir plus

## Appeler Ollama depuis Python

Vous pouvez utiliser `requests` or `urllib3` pour faire des requêtes aux points de terminaison du serveur local utilisés ci-dessus. Cependant, une façon populaire d'utiliser Ollama en Python est via le SDK [openai](https://pypi.org/project/openai/), car Ollama fournit également des points de terminaison de serveur compatibles avec OpenAI.

Voici un exemple pour phi3-mini :

```python
import openai

client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)

response = client.chat.completions.create(
    model="phi3",
    temperature=0.7,
    n=1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about a hungry cat"},
    ],
)

print("Response:")
print(response.choices[0].message.content)
```

## Appeler Ollama depuis JavaScript

```javascript
// Example of Summarize a file with Phi-3
script({
    model: "ollama:phi3",
    title: "Summarize with Phi-3",
    system: ["system"],
})

// Example of summarize
const file = def("FILE", env.files)
$`Summarize ${file} in a single paragraph.`
```

## Appeler Ollama depuis C#

Créez une nouvelle application Console C# et ajoutez le package NuGet suivant :

```bash
dotnet add package Microsoft.SemanticKernel --version 1.13.0
```

Puis remplacez ce code dans le fichier `Program.cs`

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;

// add chat completion service using the local ollama server endpoint
#pragma warning disable SKEXP0001, SKEXP0003, SKEXP0010, SKEXP0011, SKEXP0050, SKEXP0052
builder.AddOpenAIChatCompletion(
    modelId: "phi3.5",
    endpoint: new Uri("http://localhost:11434/"),
    apiKey: "non required");

// invoke a simple prompt to the chat service
string prompt = "Write a joke about kittens";
var response = await kernel.InvokePromptAsync(prompt);
Console.WriteLine(response.GetValue<string>());
```

Exécutez l'application avec la commande :

```bash
dotnet run
```

**Avertissement**:
Ce document a été traduit à l'aide de services de traduction basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.