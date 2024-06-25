# Full Local RAG Scenario Using Phi-3, SemanticKernel, and TextMemory

## Introduction

Welcome to the repository for the full local RAG scenario using Phi-3, SemanticKernel, and TextMemory. This project demonstrates the power of Phi-3, a groundbreaking Small Language Model (SLM) that is redefining AI capabilities for developers and businesses.

## Scenario Overview

The demo scenario is designed to answer the question, "What is Bruno's favourite super hero?" using two different approaches:

1. Directly asking the Phi-3 model.
2. Adding a semantic memory object with fan facts loaded and then asking the question.

## Importance of Full Scenario

Phi-3 represents a significant leap in Small Language Models, offering a unique blend of performance and efficiency. It is capable of handling full scenarios independently, which simplifies the development process and reduces integration complexities.

## Code Explanation

The console application demonstrates the use of a local model hosted in Ollama and semantic memory for search. The program uses several external libraries for dependency injection, configuration, and semantic kernel and memory functionalities.

## How to Test

1. Open a terminal and navigate to the current project.

    ```bash
    cd .\src\Sample03\
    ```

1. Run the project with the command

    ```bash
    dotnet run
    ```

1. The project `Sample03`, answer the following question:

    ```csharp
    var question = "What is Bruno's favourite super hero?"
    ```

1. First the question is asked directly to the Phi-3 Model. Then, the program load the following information in a Text Memory, and ask the question again.

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

1. Once the text memory is ready, it's loaded into the kernel as a plugin.

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // Import the text memory plugin into the Kernel.
    kernel.ImportPluginFromObject(memoryPlugin);    
    ```

1. Here is the demo console application running in a Codespace:

    ![Demo console application running in a Codespace](./img/10RAGPhi3.gif)

## References

- [Phi-3 Microsoft Blog](https://aka.ms/phi3blog-april)
- [Phi-3 Technical Report](https://aka.ms/phi3-tech-report)
- [Phi-3 Cookbook](https://aka.ms/Phi-3CookBook)
- [Generative AI for beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Semantic Kernel main repository](https://github.com/microsoft/semantic-kernel)
- [Smart Components - Local Embeddings](https://github.com/dotnet-smartcomponents/smartcomponents/blob/main/docs/local-embeddings.md)