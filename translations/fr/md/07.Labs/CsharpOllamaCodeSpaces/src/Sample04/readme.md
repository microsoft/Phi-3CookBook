# Scénario complet RAG local utilisant Phi-3, SemanticKernel et TextMemory

## Introduction

Bienvenue dans le dépôt pour le scénario complet RAG local utilisant Phi-3, SemanticKernel et TextMemory. Ce projet démontre la puissance de Phi-3, un modèle de langue de petite taille révolutionnaire qui redéfinit les capacités de l'IA pour les développeurs et les entreprises.

## Aperçu du scénario

Le scénario de démonstration est conçu pour répondre à la question : "Quel est le super-héros préféré de Bruno ?" en utilisant deux approches différentes :

1. Demander directement au modèle Phi-3.
2. Ajouter un objet de mémoire sémantique avec des faits de fans chargés, puis poser la question.

## Importance du scénario complet

Phi-3 représente un saut significatif dans les modèles de langue de petite taille, offrant un mélange unique de performance et d'efficacité. Il est capable de gérer des scénarios complets de manière indépendante, ce qui simplifie le processus de développement et réduit les complexités d'intégration.

## Explication du code

L'application console démontre l'utilisation d'un modèle local hébergé dans Ollama et de la mémoire sémantique pour la recherche. Le programme utilise plusieurs bibliothèques externes pour l'injection de dépendances, la configuration, et les fonctionnalités du kernel sémantique et de la mémoire.

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
    var question = "Quel est le super-héros préféré de Bruno ?"
    ```

1. D'abord, la question est posée directement au modèle Phi-3. Ensuite, le programme charge les informations suivantes dans une mémoire textuelle, et pose à nouveau la question.

    ```csharp

    // obtenir le service générateur d'embeddings
    var embeddingGenerator = kernel.Services.GetRequiredService<ITextEmbeddingGenerationService>();
    var memory = new SemanticTextMemory(new VolatileMemoryStore(), embeddingGenerator);    

    // ajouter des faits à la collection
    const string MemoryCollectionName = "fanFacts";
    
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info1", 
            text: "Le super-héros préféré de Gisela est Batman");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info2", 
            text: "Le dernier film de super-héros regardé par Gisela était Les Gardiens de la Galaxie Vol 3");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info3", 
            text: "Le super-héros préféré de Bruno est Invincible");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info4", 
            text: "Le dernier film de super-héros regardé par Bruno était Aquaman II");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info5", 
            text: "Bruno n'aime pas le film de super-héros : Les Éternels");    
    ```

1. Une fois la mémoire textuelle prête, elle est chargée dans le kernel comme un plugin.

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // Importer le plugin de mémoire textuelle dans le Kernel.
    kernel.ImportPluginFromObject(memoryPlugin);    
    ```

1. Voici l'application console de démonstration en cours d'exécution dans un Codespace :

    ![Application console de démonstration en cours d'exécution dans un Codespace](../../../../../../../md/07.Labs/CsharpOllamaCodeSpaces/src/Sample03/img/10RAGPhi3.gif)

## Références

- [Phi-3 Microsoft Blog](https://aka.ms/phi3blog-april)
- [Rapport technique de Phi-3](https://aka.ms/phi3-tech-report)
- [Cookbook de Phi-3](https://aka.ms/Phi-3CookBook)
- [IA générative pour débutants](https://github.com/microsoft/generative-ai-for-beginners)
- [Dépôt principal de Semantic Kernel](https://github.com/microsoft/semantic-kernel)
- [Composants intelligents - Embeddings locaux](https://github.com/dotnet-smartcomponents/smartcomponents/blob/main/docs/local-embeddings.md)

Avertissement : La traduction a été réalisée à partir de son original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.