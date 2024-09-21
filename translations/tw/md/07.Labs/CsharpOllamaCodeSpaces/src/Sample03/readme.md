# 使用 Phi-3、SemanticKernel 和 TextMemory 的完整本地 RAG 案例

## 介紹

歡迎來到使用 Phi-3、SemanticKernel 和 TextMemory 的完整本地 RAG 案例庫。這個項目展示了 Phi-3 的強大功能，這是一個突破性的 Small Language Model (SLM)，正在重新定義開發者和企業的 AI 能力。

## 案例概述

這個演示案例旨在通過兩種不同的方法回答 "Bruno 最喜歡的超級英雄是誰？" 這個問題：

1. 直接詢問 Phi-3 模型。
2. 加載一個包含粉絲事實的語義記憶對象，然後再詢問問題。

## 完整案例的重要性

Phi-3 代表了 Small Language Models 的重大飛躍，提供了性能和效率的獨特結合。它能夠獨立處理完整的案例，這簡化了開發過程並減少了集成的複雜性。

## 代碼說明

這個控制台應用程序展示了在 Ollama 中託管的本地模型和語義記憶的使用。該程序使用了多個外部庫來進行依賴注入、配置以及語義內核和記憶功能。

## 測試方法

1. 打開終端並導航到當前項目。

    ```bash
    cd .\src\Sample03\
    ```

1. 使用以下命令運行項目

    ```bash
    dotnet run
    ```

1. 項目 `Sample03`，回答以下問題：

    ```csharp
    var question = "What is Bruno's favourite super hero?"
    ```

1. 首先，問題直接詢問 Phi-3 模型。然後，程序加載以下信息到 Text Memory，並再次詢問問題。

    ```csharp

    // 獲取嵌入生成服務
    var embeddingGenerator = kernel.Services.GetRequiredService<ITextEmbeddingGenerationService>();
    var memory = new SemanticTextMemory(new VolatileMemoryStore(), embeddingGenerator);    

    // 將事實添加到集合中
    const string MemoryCollectionName = "fanFacts";
    
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info1", 
            text: "Gisela 最喜歡的超級英雄是蝙蝠俠");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info2", 
            text: "Gisela 最近看過的超級英雄電影是《銀河護衛隊 3》");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info3", 
            text: "Bruno 最喜歡的超級英雄是 Invincible");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info4", 
            text: "Bruno 最近看過的超級英雄電影是《海王 2》");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info5", 
            text: "Bruno 不喜歡的超級英雄電影是《永恆族》");    
    ```

1. 當文本記憶準備好後，將其作為插件加載到內核中。

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // 將文本記憶插件導入內核。
    kernel.ImportPluginFromObject(memoryPlugin);    
    ```

1. 以下是在 Codespace 中運行的演示控制台應用程序：

    ![在 Codespace 中運行的演示控制台應用程序](../../../../../../../md/07.Labs/CsharpOllamaCodeSpaces/src/Sample03/img/10RAGPhi3.gif)

## 參考資料

- [Phi-3 Microsoft Blog](https://aka.ms/phi3blog-april)
- [Phi-3 Technical Report](https://aka.ms/phi3-tech-report)
- [Phi-3 Cookbook](https://aka.ms/Phi-3CookBook)
- [Generative AI for beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Semantic Kernel main repository](https://github.com/microsoft/semantic-kernel)
- [Smart Components - Local Embeddings](https://github.com/dotnet-smartcomponents/smartcomponents/blob/main/docs/local-embeddings.md)

免責聲明：此翻譯由人工智慧模型從原文翻譯而來，可能並不完美。
請檢查輸出並進行任何必要的修正。