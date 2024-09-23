# Scénario Complet de RAG Local Utilisant Phi-3, SemanticKernel et TextMemory

## Introduction

Bienvenue dans le dépôt pour le scénario complet de RAG local utilisant Phi-3, SemanticKernel et TextMemory. Ce projet démontre la puissance de Phi-3, un modèle de langage de petite taille révolutionnaire qui redéfinit les capacités de l'IA pour les développeurs et les entreprises.

## Vue d'ensemble du scénario

Le scénario de démonstration est conçu pour répondre à la question "Quel est le super héros préféré de Bruno ?" en utilisant deux approches différentes :

1. Demander directement au modèle Phi-3.
2. Ajouter un objet de mémoire sémantique avec des faits de fans chargés, puis poser la question.

## Importance du scénario complet

Phi-3 représente un saut significatif dans les modèles de langage de petite taille, offrant un mélange unique de performance et d'efficacité. Il est capable de gérer des scénarios complets de manière autonome, ce qui simplifie le processus de développement et réduit les complexités d'intégration.

## Explication du code

L'application console démontre l'utilisation d'un modèle local hébergé dans Ollama et de la mémoire sémantique pour la recherche. Le programme utilise plusieurs bibliothèques externes pour l'injection de dépendances, la configuration, et les fonctionnalités du noyau sémantique et de la mémoire.

## Comment tester

1. Ouvrez un terminal et naviguez jusqu'au projet actuel.

    ```bash
    cd .\src\Sample03\
    ```

1. Exécutez le projet avec la commande

    ```bash
    dotnet run
    ```

1. Le projet `Sample03`, répond à la question suivante :

    ```csharp
    var question = "Quel est le super héros préféré de Bruno ?"
    ```

1. D'abord, la question est posée directement au modèle Phi-3. Ensuite, le programme charge les informations suivantes dans une mémoire texte, et pose à nouveau la question.

    ```csharp

    // obtenir le service générateur d'embeddings
    var embeddingGenerator = kernel.Services.GetRequiredService<ITextEmbeddingGenerationService>();
    var memory = new SemanticTextMemory(new VolatileMemoryStore(), embeddingGenerator);    

    // ajouter des faits à la collection
    const string MemoryCollectionName = "fanFacts";
    
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info1", 
            text: "Le super héros préféré de Gisela est Batman");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info2", 
            text: "Le dernier film de super héros vu par Gisela était Les Gardiens de la Galaxie Vol 3");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info3", 
            text: "Le super héros préféré de Bruno est Invincible");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info4", 
            text: "Le dernier film de super héros vu par Bruno était Aquaman II");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info5", 
            text: "Bruno n'aime pas le film de super héros : Les Éternels");    
    ```

1. Une fois la mémoire texte prête, elle est chargée dans le noyau comme un plugin.

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // Importer le plugin de mémoire texte dans le Kernel.
    kernel.ImportPluginFromObject(memoryPlugin);    
    ```

1. Voici l'application console de démonstration s'exécutant dans un Codespace :

    ![Application console de démonstration s'exécutant dans un Codespace](../../../../../../../md/07.Labs/CsharpOllamaCodeSpaces/src/Sample03/img/10RAGPhi3.gif)

## Références

- [Phi-3 Microsoft Blog](https://aka.ms/phi3blog-april)
- [Phi-3 Technical Report](https://aka.ms/phi3-tech-report)
- [Phi-3 Cookbook](https://aka.ms/Phi-3CookBook)
- [Generative AI for beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Semantic Kernel main repository](https://github.com/microsoft/semantic-kernel)
- [Smart Components - Local Embeddings](https://github.com/dotnet-smartcomponents/smartcomponents/blob/main/docs/local-embeddings.md)

Avertissement : La traduction a été effectuée à partir de son original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.