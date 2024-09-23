# 使用 Phi-3、SemanticKernel 和 TextMemory 的完整本地 RAG 场景

## 介绍

欢迎来到使用 Phi-3、SemanticKernel 和 TextMemory 的完整本地 RAG 场景的仓库。这个项目展示了 Phi-3 的强大功能，这是一种突破性的“小语言模型”（SLM），正在重新定义开发人员和企业的 AI 能力。

## 场景概述

这个演示场景旨在通过两种不同的方法回答“Bruno 最喜欢的超级英雄是谁？”这个问题：

1. 直接询问 Phi-3 模型。
2. 添加一个加载了粉丝事实的语义记忆对象，然后再问问题。

## 完整场景的重要性

Phi-3 代表了小语言模型的重大飞跃，提供了性能和效率的独特结合。它能够独立处理完整的场景，这简化了开发过程并减少了集成的复杂性。

## 代码说明

这个控制台应用程序展示了如何使用托管在 Ollama 中的本地模型和用于搜索的语义记忆。程序使用了几个外部库来进行依赖注入、配置以及语义内核和记忆功能。

## 如何测试

1. 打开终端并导航到当前项目。

    ```bash
    cd .\src\Sample03\
    ```

1. 使用以下命令运行项目

    ```bash
    dotnet run
    ```

1. 在项目 `Sample03` 中，回答以下问题：

    ```csharp
    var question = "What is Bruno's favourite super hero?"
    ```

1. 首先直接向 Phi-3 模型提问。然后，程序在文本记忆中加载以下信息，再次提问。

    ```csharp

    // 获取嵌入生成服务
    var embeddingGenerator = kernel.Services.GetRequiredService<ITextEmbeddingGenerationService>();
    var memory = new SemanticTextMemory(new VolatileMemoryStore(), embeddingGenerator);    

    // 向集合中添加事实
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

1. 一旦文本记忆准备好，就将其作为插件加载到内核中。

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // 将文本记忆插件导入内核。
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

免责声明：本翻译由AI模型从原文翻译而来，可能并不完美。请审查输出并进行任何必要的修改。