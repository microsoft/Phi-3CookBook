# Scénario complet de RAG local utilisant Phi-3, SemanticKernel et TextMemory

## Introduction

Bienvenue dans le dépôt pour le scénario complet de RAG local utilisant Phi-3, SemanticKernel et TextMemory. Ce projet démontre la puissance de Phi-3, un modèle de langage petit mais révolutionnaire (SLM) qui redéfinit les capacités de l'IA pour les développeurs et les entreprises.

## Aperçu du scénario

Le scénario de démonstration est conçu pour répondre à la question : "Quel est le super-héros préféré de Bruno ?" en utilisant deux approches différentes :

1. Demander directement au modèle Phi-3.
2. Ajouter un objet de mémoire sémantique avec des faits de fans chargés, puis poser la question.

## Importance du scénario complet

Phi-3 représente un saut significatif dans les modèles de langage petits, offrant un mélange unique de performance et d'efficacité. Il est capable de gérer des scénarios complets de manière autonome, ce qui simplifie le processus de développement et réduit les complexités d'intégration.

## Explication du code

L'application console démontre l'utilisation d'un modèle local hébergé dans Ollama et de la mémoire sémantique pour la recherche. Le programme utilise plusieurs bibliothèques externes pour l'injection de dépendances, la configuration, et les fonctionnalités du kernel et de la mémoire sémantiques.

## Comment tester

1. Ouvrez un terminal et naviguez vers le projet actuel.

    ```bash
    cd .\src\Sample03\
    ```

1. Exécutez le projet avec la commande

    ```bash
    dotnet run
    ```

1. Le projet `Sample03`, répondez à la question suivante :

    ```csharp
    var question = "What is Bruno's favourite super hero?"
    ```

1. D'abord, la question est posée directement au modèle Phi-3. Ensuite, le programme charge les informations suivantes dans une mémoire textuelle, et pose à nouveau la question.

    ```csharp

    // get the embeddings generator service
    var embeddingGenerator = kernel.Services.GetRequiredService<ITextEmbeddingGenerationService>();
    var memory = new SemanticTextMemory(new VolatileMemoryStore(), embeddingGenerator);    

    // add facts to the collection
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

1. Une fois la mémoire textuelle prête, elle est chargée dans le kernel comme un plugin.

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // Import the text memory plugin into the Kernel.
    kernel.ImportPluginFromObject(memoryPlugin);    
    ```

1. Voici l'application console de démonstration fonctionnant dans un Codespace :

    ![Application console de démonstration fonctionnant dans un Codespace](../../../../../../../md/07.Labs/CsharpOllamaCodeSpaces/src/Sample03/img/10RAGPhi3.gif)

## Références

- [Phi-3 Microsoft Blog](https://aka.ms/phi3blog-april)
- [Phi-3 Technical Report](https://aka.ms/phi3-tech-report)
- [Phi-3 Cookbook](https://aka.ms/Phi-3CookBook)
- [Generative AI for beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Semantic Kernel main repository](https://github.com/microsoft/semantic-kernel)
- [Smart Components - Local Embeddings](https://github.com/dotnet-smartcomponents/smartcomponents/blob/main/docs/local-embeddings.md)

**Avertissement** :
Ce document a été traduit en utilisant des services de traduction automatisés basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.