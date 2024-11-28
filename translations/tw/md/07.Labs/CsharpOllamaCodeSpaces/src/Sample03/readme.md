# 使用 Phi-3、SemanticKernel 和 TextMemory 的完整本地 RAG 案例

## 介紹

歡迎來到使用 Phi-3、SemanticKernel 和 TextMemory 的完整本地 RAG 案例庫。本專案展示了 Phi-3 的強大功能，這是一個突破性的 Small Language Model (SLM)，正在重新定義開發者和企業的 AI 能力。

## 案例概述

此範例旨在回答問題："Bruno 最喜歡的超級英雄是誰？" 使用兩種不同的方法：

1. 直接詢問 Phi-3 模型。
2. 加載帶有粉絲事實的語義記憶對象，然後再次詢問問題。

## 完整案例的重要性

Phi-3 代表了 Small Language Models 的重大飛躍，提供了性能和效率的獨特組合。它能夠獨立處理完整的場景，簡化了開發過程並減少了整合的複雜性。

## 代碼說明

此控制台應用程式展示了如何使用在 Ollama 上託管的本地模型和語義記憶進行搜索。該程式使用了多個外部庫進行依賴注入、配置以及語義內核和記憶功能。

## 測試方法

1. 打開終端並導航到當前項目。

    ```bash
    cd .\src\Sample03\
    ```

1. 使用以下命令運行項目

    ```bash
    dotnet run
    ```

1. 專案 `Sample03`，回答以下問題：

    ```csharp
    var question = "What is Bruno's favourite super hero?"
    ```

1. 首先，問題直接問 Phi-3 模型。然後，程式將以下資訊加載到文本記憶中，並再次詢問問題。

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

1. 一旦文本記憶準備就緒，它將作為插件加載到內核中。

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // Import the text memory plugin into the Kernel.
    kernel.ImportPluginFromObject(memoryPlugin);    
    ```

1. 這是在 Codespace 中運行的演示控制台應用程式：

    ![在 Codespace 中運行的演示控制台應用程式](../../../../../../../md/07.Labs/CsharpOllamaCodeSpaces/src/Sample03/img/10RAGPhi3.gif)

## 參考資料

- [Phi-3 Microsoft Blog](https://aka.ms/phi3blog-april)
- [Phi-3 Technical Report](https://aka.ms/phi3-tech-report)
- [Phi-3 Cookbook](https://aka.ms/Phi-3CookBook)
- [Generative AI for beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Semantic Kernel main repository](https://github.com/microsoft/semantic-kernel)
- [Smart Components - Local Embeddings](https://github.com/dotnet-smartcomponents/smartcomponents/blob/main/docs/local-embeddings.md)

**免責聲明**:
本文檔已使用機器翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始語言的文件視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們不對使用此翻譯所引起的任何誤解或誤讀負責。