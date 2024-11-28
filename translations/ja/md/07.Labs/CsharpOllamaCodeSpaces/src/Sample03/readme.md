# Phi-3、SemanticKernel、TextMemoryを使用した完全ローカルRAGシナリオ

## はじめに

Phi-3、SemanticKernel、TextMemoryを使用した完全ローカルRAGシナリオのリポジトリへようこそ。このプロジェクトは、開発者や企業向けにAIの能力を再定義する画期的な小型言語モデル（SLM）であるPhi-3の力を示しています。

## シナリオ概要

このデモシナリオは、「ブルーノの好きなスーパーヒーローは誰？」という質問に対して、以下の2つの異なるアプローチで回答するように設計されています。

1. Phi-3モデルに直接質問する。
2. ファンファクトが読み込まれたセマンティックメモリオブジェクトを追加してから質問する。

## 完全シナリオの重要性

Phi-3は、小型言語モデルにおける大きな飛躍を示しており、性能と効率のユニークな組み合わせを提供します。Phi-3は、完全なシナリオを独立して処理する能力があり、開発プロセスを簡素化し、統合の複雑さを軽減します。

## コードの説明

このコンソールアプリケーションは、Ollamaにホストされたローカルモデルと検索用のセマンティックメモリを使用する方法を示しています。プログラムは、依存性注入、設定、セマンティックカーネルおよびメモリ機能のためにいくつかの外部ライブラリを使用しています。

## テスト方法

1. ターミナルを開き、現在のプロジェクトに移動します。

    ```bash
    cd .\src\Sample03\
    ```

1. 以下のコマンドでプロジェクトを実行します。

    ```bash
    dotnet run
    ```

1. プロジェクト `Sample03` で、次の質問に答えます：

    ```csharp
    var question = "What is Bruno's favourite super hero?"
    ```

1. まず、Phi-3モデルに直接質問します。次に、プログラムは以下の情報をText Memoryに読み込み、再度質問します。

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

1. テキストメモリが準備できたら、それをプラグインとしてカーネルにロードします。

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // Import the text memory plugin into the Kernel.
    kernel.ImportPluginFromObject(memoryPlugin);    
    ```

1. こちらはCodespaceで実行中のデモコンソールアプリケーションです：

    ![Codespaceで実行中のデモコンソールアプリケーション](../../../../../../../md/07.Labs/CsharpOllamaCodeSpaces/src/Sample03/img/10RAGPhi3.gif)

## 参考文献

- [Phi-3 Microsoft Blog](https://aka.ms/phi3blog-april)
- [Phi-3 Technical Report](https://aka.ms/phi3-tech-report)
- [Phi-3 Cookbook](https://aka.ms/Phi-3CookBook)
- [Generative AI for beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Semantic Kernel main repository](https://github.com/microsoft/semantic-kernel)
- [Smart Components - Local Embeddings](https://github.com/dotnet-smartcomponents/smartcomponents/blob/main/docs/local-embeddings.md)

**免責事項**:
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期すよう努めておりますが、自動翻訳には誤りや不正確さが含まれる場合があります。権威ある情報源としては、原文の言語の文書を参照してください。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤認については、一切の責任を負いかねます。