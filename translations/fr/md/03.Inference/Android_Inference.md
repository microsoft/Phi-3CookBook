# **Inférence Phi-3 sur Android**

Explorons comment effectuer une inférence avec Phi-3-mini sur des appareils Android. Phi-3-mini est une nouvelle série de modèles de Microsoft qui permet le déploiement de modèles de langage de grande taille (LLMs) sur des appareils de périphérie et des appareils IoT.

## Semantic Kernel et Inférence

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) est un cadre d'application qui vous permet de créer des applications compatibles avec Azure OpenAI Service, les modèles OpenAI, et même les modèles locaux. Si vous êtes nouveau sur Semantic Kernel, nous vous suggérons de consulter le [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Pour Accéder à Phi-3-mini en Utilisant Semantic Kernel

Vous pouvez le combiner avec le Hugging Face Connector dans Semantic Kernel. Référez-vous à ce [Code Exemple](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Par défaut, il correspond à l'ID du modèle sur Hugging Face. Cependant, vous pouvez également vous connecter à un serveur de modèle Phi-3-mini construit localement.

### Appeler des Modèles Quantifiés avec Ollama ou LlamaEdge

De nombreux utilisateurs préfèrent utiliser des modèles quantifiés pour exécuter des modèles localement. [Ollama](https://ollama.com/) et [LlamaEdge](https://llamaedge.com) permettent aux utilisateurs individuels d'appeler différents modèles quantifiés :

#### Ollama

Vous pouvez exécuter directement `ollama run Phi-3` ou le configurer hors ligne en créant un `Modelfile` avec le chemin vers votre fichier `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Code Exemple](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Si vous souhaitez utiliser des fichiers `.gguf` dans le cloud et sur des appareils de périphérie simultanément, LlamaEdge est un excellent choix. Vous pouvez vous référer à ce [code exemple](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) pour commencer.

### Installer et Exécuter sur Téléphones Android

1. **Téléchargez l'application MLC Chat** (gratuite) pour les téléphones Android.
2. Téléchargez le fichier APK (148MB) et installez-le sur votre appareil.
3. Lancez l'application MLC Chat. Vous verrez une liste de modèles d'IA, y compris Phi-3-mini.

En résumé, Phi-3-mini ouvre des possibilités passionnantes pour l'IA générative sur des appareils de périphérie, et vous pouvez commencer à explorer ses capacités sur Android.

**Avertissement**:
Ce document a été traduit en utilisant des services de traduction automatique basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.