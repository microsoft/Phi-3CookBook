# 使用 Phi-3、SemanticKernel 和 TextMemory 的完整本地 RAG 情境

## 介紹

歡迎來到使用 Phi-3、SemanticKernel 和 TextMemory 的完整本地 RAG 情境的倉庫。這個專案展示了 Phi-3 的強大功能，這是一個突破性的 Small Language Model (SLM)，正在重新定義開發者和企業的 AI 能力。

## 情境概述

這個示範情境旨在回答這個問題：「Bruno 最喜歡的超級英雄是誰？」使用兩種不同的方法：

1. 直接詢問 Phi-3 模型。
2. 添加一個載入粉絲事實的語義記憶體物件，然後再詢問問題。

## 完整情境的重要性

Phi-3 代表了 Small Language Models 的重大飛躍，提供了性能和效率的獨特結合。它能夠獨立處理完整的情境，這簡化了開發過程並減少了整合的複雜性。

## 代碼解釋

這個控制台應用程式展示了如何使用在 Ollama 中託管的本地模型和語義記憶體進行搜尋。該程式使用了多個外部庫來進行依賴注入、配置以及語義內核和記憶體功能。

## 如何測試

1. 打開終端並導航到當前專案。

    ```bash
    cd .\src\Sample03\
    ```

1. 使用以下命令運行專案

    ```bash
    dotnet run
    ```

1. 專案 `Sample03`，回答以下問題：

    ```csharp
    var question = "What is Bruno's favourite super hero?"
    ```

1. 首先直接向 Phi-3 模型詢問問題。然後，程式將以下信息載入 Text Memory，並再次詢問問題。

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

1. 一旦文本記憶體準備好，它會作為插件載入內核。

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // Import the text memory plugin into the Kernel.
    kernel.ImportPluginFromObject(memoryPlugin);    
    ```

1. 以下是運行於 Codespace 的示範控制台應用程式：

    ![運行於 Codespace 的示範控制台應用程式](../../../../../../../md/07.Labs/CsharpOllamaCodeSpaces/src/Sample03/img/10RAGPhi3.gif)

## 參考資料

- [Phi-3 Microsoft Blog](https://aka.ms/phi3blog-april)
- [Phi-3 Technical Report](https://aka.ms/phi3-tech-report)
- [Phi-3 Cookbook](https://aka.ms/Phi-3CookBook)
- [Generative AI for beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Semantic Kernel main repository](https://github.com/microsoft/semantic-kernel)
- [Smart Components - Local Embeddings](https://github.com/dotnet-smartcomponents/smartcomponents/blob/main/docs/local-embeddings.md)

**免責聲明**:
此文件是使用機器翻譯服務翻譯的。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文件為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們不對因使用此翻譯而產生的任何誤解或誤讀承擔責任。