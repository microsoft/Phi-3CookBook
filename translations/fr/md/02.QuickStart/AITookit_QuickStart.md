# AI Toolkit pour VScode (Windows)

[AI Toolkit pour VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) simplifie le développement d'applications d'IA générative en rassemblant des outils et modèles de développement d'IA de pointe du catalogue Azure AI Foundry et d'autres catalogues comme Hugging Face. Vous pourrez parcourir le catalogue de modèles d'IA alimenté par Azure ML et Hugging Face, les télécharger localement, les ajuster, les tester et les utiliser dans votre application.

AI Toolkit Preview fonctionnera localement. Selon le modèle que vous avez sélectionné, certaines tâches sont uniquement prises en charge sur Windows et Linux,

L'inférence ou l'ajustement local, selon le modèle que vous avez sélectionné, peut nécessiter un GPU tel qu'un GPU NVIDIA CUDA.

Si vous exécutez à distance, la ressource cloud doit avoir un GPU, assurez-vous de vérifier votre environnement. Pour une exécution locale sur Windows + WSL, la distribution WSL Ubuntu 18.4 ou supérieure doit être installée et définie par défaut avant d'utiliser AI Toolkit.

## Pour commencer

[En savoir plus sur l'installation du sous-système Windows pour Linux](https://learn.microsoft.com/windows/wsl/install?WT.mc_id=aiml-137032-kinfeylo)

et [changer la distribution par défaut](https://learn.microsoft.com/windows/wsl/install#change-the-default-linux-distribution-installed).

[AI Tooklit GitHub Repo](https://github.com/microsoft/vscode-ai-toolkit/)

- Windows ou Linux.
- **Le support MacOS arrive bientôt**
- Pour l'ajustement sur Windows et Linux, vous aurez besoin d'un GPU Nvidia. De plus, **Windows** nécessite un sous-système pour Linux avec une distribution Ubuntu 18.4 ou supérieure. [En savoir plus sur l'installation du sous-système Windows pour Linux](https://learn.microsoft.com/windows/wsl/install) et [changer la distribution par défaut](https://learn.microsoft.com/windows/wsl/install#change-the-default-linux-distribution-installed).

### Installer AI Toolkit

AI Toolkit est fourni sous forme d'[extension Visual Studio Code](https://code.visualstudio.com/docs/setup/additional-components#_vs-code-extensions), donc vous devez d'abord installer [VS Code](https://code.visualstudio.com/docs/setup/windows?WT.mc_id=aiml-137032-kinfeylo) et télécharger AI Toolkit depuis le [VS Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio).
[AI Toolkit est disponible sur le Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) et peut être installé comme toute autre extension VS Code.

Si vous n'êtes pas familier avec l'installation des extensions VS Code, suivez ces étapes :

### Se connecter

1. Dans la barre d'activités de VS Code, sélectionnez **Extensions**
2. Dans la barre de recherche des extensions, tapez "AI Toolkit"
3. Sélectionnez "AI Toolkit pour Visual Studio Code"
4. Sélectionnez **Installer**

Vous êtes maintenant prêt à utiliser l'extension !

Vous serez invité à vous connecter à GitHub, cliquez sur "Autoriser" pour continuer. Vous serez redirigé vers la page de connexion GitHub.

Veuillez vous connecter et suivre les étapes du processus. Après avoir terminé avec succès, vous serez redirigé vers VS Code.

Une fois l'extension installée, vous verrez l'icône AI Toolkit apparaître dans votre barre d'activités.

Explorons les actions disponibles !

### Actions disponibles

La barre latérale principale de l'AI Toolkit est organisée en  

- **Modèles**
- **Ressources**
- **Playground**
- **Ajustement**

sont disponibles dans la section Ressources. Pour commencer, sélectionnez **Catalogue de modèles**.

### Télécharger un modèle depuis le catalogue

En lançant AI Toolkit depuis la barre latérale de VS Code, vous pouvez choisir parmi les options suivantes :

![Catalogue de modèles AI Toolkit](../../../../translated_images/AItoolkitmodel_catalog.49200354ddc7aceecdcab2080769d898b1fd50424ef9f7014aafeb790028c49d.fr.png)

- Trouver un modèle pris en charge dans le **Catalogue de modèles** et le télécharger localement
- Tester l'inférence du modèle dans le **Model Playground**
- Ajuster le modèle localement ou à distance dans **Model Fine-tuning**
- Déployer des modèles ajustés sur le cloud via la palette de commandes pour AI Toolkit

> [!NOTE]
>
> **GPU Vs CPU**
>
> Vous remarquerez que les cartes des modèles indiquent la taille du modèle, la plateforme et le type d'accélérateur (CPU, GPU). Pour des performances optimisées sur **les appareils Windows ayant au moins un GPU**, sélectionnez les versions de modèles qui ciblent uniquement Windows.
>
> Cela garantit que vous disposez d'un modèle optimisé pour l'accélérateur DirectML.
>
> Les noms des modèles sont au format
>
> - `{model_name}-{accelerator}-{quantization}-{format}`.
>
>Pour vérifier si vous avez un GPU sur votre appareil Windows, ouvrez **Gestionnaire des tâches** puis sélectionnez l'onglet **Performance**. Si vous avez des GPU, ils seront listés sous des noms comme "GPU 0" ou "GPU 1".

### Exécuter le modèle dans le playground

Après avoir défini tous les paramètres, cliquez sur **Générer le projet**.

Une fois votre modèle téléchargé, sélectionnez **Charger dans le Playground** sur la carte du modèle dans le catalogue :

- Initier le téléchargement du modèle
- Installer toutes les conditions préalables et dépendances
- Créer un espace de travail VS Code

![Charger le modèle dans le playground](../../../../translated_images/AItoolkitload_model_into_playground.f78799b4838c6521be6a296729279525958dec6cfb9a26c64752e397dfe19ef2.fr.png)

Lorsque le modèle est téléchargé, vous pouvez lancer le projet depuis AI Toolkit.

> ***Note*** Si vous souhaitez essayer la fonction d'aperçu pour faire de l'inférence ou de l'ajustement à distance, veuillez suivre [ce guide](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-overall.md)

### Modèles optimisés pour Windows

Vous devriez voir la réponse du modèle vous être renvoyée en continu :

AI Toolkit propose une collection de modèles d'IA disponibles publiquement déjà optimisés pour Windows. Les modèles sont stockés à différents endroits, y compris Hugging Face, GitHub et d'autres, mais vous pouvez parcourir les modèles et les trouver tous au même endroit, prêts à être téléchargés et utilisés dans votre application Windows.

![Flux de génération](../../../../imgs/04/04/AItoolkitgeneration-gif.gif)

### Sélections de modèles

Si vous **n'avez pas** de **GPU** disponible sur votre appareil *Windows* mais que vous avez sélectionné le

- modèle Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx

la réponse du modèle sera *très lente*.

Vous devriez plutôt télécharger la version optimisée pour CPU :

- Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx.

Il est également possible de changer :

**Instructions de contexte :** Aidez le modèle à comprendre le contexte plus large de votre demande. Cela peut inclure des informations de base, des exemples/démonstrations de ce que vous voulez ou expliquer l'objectif de votre tâche.

**Paramètres d'inférence :**

- *Longueur maximale de la réponse* : Le nombre maximum de tokens que le modèle renverra.
- *Température* : La température du modèle est un paramètre qui contrôle à quel point la sortie d'un modèle de langage est aléatoire. Une température plus élevée signifie que le modèle prend plus de risques, vous donnant un mélange diversifié de mots. En revanche, une température plus basse fait que le modèle joue la sécurité, s'en tenant à des réponses plus concentrées et prévisibles.
- *Top P* : Également connu sous le nom d'échantillonnage par noyau, est un paramètre qui contrôle combien de mots ou de phrases possibles le modèle de langage considère lors de la prédiction du mot suivant.
- *Pénalité de fréquence* : Ce paramètre influence la fréquence à laquelle le modèle répète des mots ou des phrases dans sa sortie. Une valeur plus élevée (proche de 1.0) encourage le modèle à *éviter* de répéter des mots ou des phrases.
- *Pénalité de présence* : Ce paramètre est utilisé dans les modèles d'IA générative pour encourager la diversité et la spécificité dans le texte généré. Une valeur plus élevée (proche de 1.0) encourage le modèle à inclure plus de tokens nouveaux et diversifiés. Une valeur plus basse est plus susceptible de faire générer au modèle des phrases courantes ou clichées.

### Utiliser l'API REST dans votre application

AI Toolkit est livré avec un serveur web API REST local **sur le port 5272** qui utilise le [format de complétion de chat OpenAI](https://platform.openai.com/docs/api-reference/chat/create).

Cela vous permet de tester votre application localement sans avoir à dépendre d'un service de modèle d'IA cloud. Par exemple, le fichier JSON suivant montre comment configurer le corps de la requête :

```json
{
    "model": "Phi-3-mini-4k-directml-int4-awq-block-128-onnx",
    "messages": [
        {
            "role": "user",
            "content": "what is the golden ratio?"
        }
    ],
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 10,
    "max_tokens": 100,
    "stream": true
}
```

Vous pouvez tester l'API REST en utilisant (par exemple) [Postman](https://www.postman.com/) ou l'utilitaire CURL (Client URL) :

```bash
curl -vX POST http://127.0.0.1:5272/v1/chat/completions -H 'Content-Type: application/json' -d @body.json
```

### Utilisation de la bibliothèque cliente OpenAI pour Python

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:5272/v1/", 
    api_key="x" # required for the API but not used
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "what is the golden ratio?",
        }
    ],
    model="Phi-3-mini-4k-cuda-int4-onnx",
)

print(chat_completion.choices[0].message.content)
```

### Utilisation de la bibliothèque cliente Azure OpenAI pour .NET

Ajoutez la [bibliothèque cliente Azure OpenAI pour .NET](https://www.nuget.org/packages/Azure.AI.OpenAI/) à votre projet en utilisant NuGet :

```bash
dotnet add {project_name} package Azure.AI.OpenAI --version 1.0.0-beta.17
```

Ajoutez un fichier C# appelé **OverridePolicy.cs** à votre projet et collez le code suivant :

```csharp
// OverridePolicy.cs
using Azure.Core.Pipeline;
using Azure.Core;

internal partial class OverrideRequestUriPolicy(Uri overrideUri)
    : HttpPipelineSynchronousPolicy
{
    private readonly Uri _overrideUri = overrideUri;

    public override void OnSendingRequest(HttpMessage message)
    {
        message.Request.Uri.Reset(_overrideUri);
    }
}
```

Ensuite, collez le code suivant dans votre fichier **Program.cs** :

```csharp
// Program.cs
using Azure.AI.OpenAI;

Uri localhostUri = new("http://localhost:5272/v1/chat/completions");

OpenAIClientOptions clientOptions = new();
clientOptions.AddPolicy(
    new OverrideRequestUriPolicy(localhostUri),
    Azure.Core.HttpPipelinePosition.BeforeTransport);
OpenAIClient client = new(openAIApiKey: "unused", clientOptions);

ChatCompletionsOptions options = new()
{
    DeploymentName = "Phi-3-mini-4k-directml-int4-awq-block-128-onnx",
    Messages =
    {
        new ChatRequestSystemMessage("You are a helpful assistant. Be brief and succinct."),
        new ChatRequestUserMessage("What is the golden ratio?"),
    }
};

StreamingResponse<StreamingChatCompletionsUpdate> streamingChatResponse
    = await client.GetChatCompletionsStreamingAsync(options);

await foreach (StreamingChatCompletionsUpdate chatChunk in streamingChatResponse)
{
    Console.Write(chatChunk.ContentUpdate);
}
```

## Ajustement avec AI Toolkit

- Commencez par la découverte des modèles et le playground.
- Ajustement et inférence des modèles en utilisant des ressources informatiques locales.
- Ajustement et inférence à distance en utilisant les ressources Azure

[Ajustement avec AI Toolkit](../04.Fine-tuning/Finetuning_VSCodeaitoolkit.md)

## Ressources Q&A AI Toolkit

Veuillez consulter notre [page Q&A](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/QA.md) pour les problèmes les plus courants et leurs résolutions.

**Avertissement** :
Ce document a été traduit en utilisant des services de traduction automatisés par IA. Bien que nous nous efforcions d'atteindre une précision optimale, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.