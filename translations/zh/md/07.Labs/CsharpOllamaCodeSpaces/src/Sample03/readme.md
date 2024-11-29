# 使用 Phi-3、SemanticKernel 和 TextMemory 的完整本地 RAG 场景

## 介绍

欢迎来到使用 Phi-3、SemanticKernel 和 TextMemory 的完整本地 RAG 场景的存储库。本项目展示了 Phi-3 的强大功能，这是一种突破性的“小语言模型”（SLM），正在重新定义开发者和企业的 AI 能力。

## 场景概述

这个演示场景旨在通过两种不同的方法回答问题：“Bruno 最喜欢的超级英雄是谁？”：

1. 直接询问 Phi-3 模型。
2. 添加一个加载了粉丝事实的语义记忆对象，然后再问这个问题。

## 完整场景的重要性

Phi-3 代表了“小语言模型”的一个重大飞跃，提供了性能和效率的独特结合。它能够独立处理完整的场景，从而简化开发过程并减少集成复杂性。

## 代码解释

这个控制台应用程序演示了如何使用托管在 Ollama 的本地模型和用于搜索的语义记忆。该程序使用了几个外部库来进行依赖注入、配置以及语义内核和记忆功能。

## 如何测试

1. 打开终端并导航到当前项目。

    ```bash
    cd .\src\Sample03\
    ```

1. 使用以下命令运行项目

    ```bash
    dotnet run
    ```

1. 项目 `Sample03`，回答以下问题：

    ```csharp
    var question = "What is Bruno's favourite super hero?"
    ```

1. 首先，直接向 Phi-3 模型提问。然后，程序将以下信息加载到文本记忆中，并再次提问。

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

1. 一旦文本记忆准备就绪，它将作为插件加载到内核中。

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // Import the text memory plugin into the Kernel.
    kernel.ImportPluginFromObject(memoryPlugin);    
    ```

1. 以下是在 Codespace 中运行的演示控制台应用程序：

    ![在 Codespace 中运行的演示控制台应用程序](../../../../../../../md/07.Labs/CsharpOllamaCodeSpaces/src/Sample03/img/10RAGPhi3.gif)

## 参考资料

- [Phi-3 Microsoft Blog](https://aka.ms/phi3blog-april)
- [Phi-3 Technical Report](https://aka.ms/phi3-tech-report)
- [Phi-3 Cookbook](https://aka.ms/Phi-3CookBook)
- [Generative AI for beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Semantic Kernel main repository](https://github.com/microsoft/semantic-kernel)
- [Smart Components - Local Embeddings](https://github.com/dotnet-smartcomponents/smartcomponents/blob/main/docs/local-embeddings.md)

**免责声明**：
本文件使用基于机器的AI翻译服务进行翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。应将原文档视为权威来源。对于关键信息，建议进行专业的人类翻译。我们不对使用本翻译而产生的任何误解或误读负责。