# Scénario Complet RAG Local Utilisant Phi-3, SemanticKernel et TextMemory

## Introduction

Bienvenue dans le dépôt pour le scénario complet RAG local utilisant Phi-3, SemanticKernel et TextMemory. Ce projet démontre la puissance de Phi-3, un modèle de langage de petite taille révolutionnaire qui redéfinit les capacités de l'IA pour les développeurs et les entreprises.

## Vue d'ensemble du scénario

Le scénario de démonstration est conçu pour répondre à la question, "Quel est le super héros préféré de Bruno ?" en utilisant deux approches différentes :

1. Demander directement au modèle Phi-3.
2. Ajouter un objet de mémoire sémantique avec des faits de fans chargés puis poser la question.

## Importance du Scénario Complet

Phi-3 représente une avancée significative dans les modèles de langage de petite taille, offrant un mélange unique de performance et d'efficacité. Il est capable de gérer des scénarios complets de manière autonome, ce qui simplifie le processus de développement et réduit les complexités d'intégration.

## Explication du Code

L'application console démontre l'utilisation d'un modèle local hébergé dans Ollama et de la mémoire sémantique pour la recherche. Le programme utilise plusieurs bibliothèques externes pour l'injection de dépendances, la configuration et les fonctionnalités du noyau et de la mémoire sémantique.

## Comment Tester

1. Ouvrez un terminal et naviguez vers le projet actuel.

    ```bash
    cd .\src\Sample03\
    ```

1. Exécutez le projet avec la commande

    ```bash
    dotnet run
    ```

1. Le projet `Sample03`, répond à la question suivante :

    ```csharp
    var question = "What is Bruno's favourite super hero?"
    ```

1. D'abord, la question est posée directement au modèle Phi-3. Ensuite, le programme charge les informations suivantes dans une mémoire textuelle, et pose à nouveau la question.

    ```csharp

    // obtenir le service de générateur d'embeddings
    var embeddingGenerator = kernel.Services.GetRequiredService<ITextEmbeddingGenerationService>();
    var memory = new SemanticTextMemory(new VolatileMemoryStore(), embeddingGenerator);    

    // ajouter des faits à la collection
    const string MemoryCollectionName = "fanFacts";
    
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info1", 
            text: "Gisela's favourite super hero is Batman");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info2", 
            text: "The last super hero movie watched by Gisela was Guardians of the Galaxy Vol 3");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info3", 
            text: "Bruno's favourite super hero is Invincible");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info4", 
            text: "The last super hero movie watched by Bruno was Aquaman II");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info5", 
            text: "Bruno don't like the super hero movie: Eternals");    
    ```

1. Une fois la mémoire textuelle prête, elle est chargée dans le noyau en tant que plugin.

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // Importer le plugin de mémoire textuelle dans le noyau.
    kernel.ImportPluginFromObject(memoryPlugin);    
    ```

1. Voici l'application console de démonstration en cours d'exécution dans un Codespace :

    ![Application console de démonstration en cours d'exécution dans un Codespace](./img/10RAGPhi3.gif)

## Références

- [Phi-3 Microsoft Blog](https://aka.ms/phi3blog-april)
- [Phi-3 Technical Report](https://aka.ms/phi3-tech-report)
- [Phi-3 Cookbook](https://aka.ms/Phi-3CookBook)
- [Generative AI for beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Semantic Kernel main repository](https://github.com/microsoft/semantic-kernel)
- [Smart Components - Local Embeddings](https://github.com/dotnet-smartcomponents/smartcomponents/blob/main/docs/local-embeddings.md)

Avertissement : La traduction a été réalisée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.