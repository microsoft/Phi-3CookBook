# Phi-3、SemanticKernel、TextMemoryを使った完全なローカルRAGシナリオ

## はじめに

Phi-3、SemanticKernel、TextMemoryを使った完全なローカルRAGシナリオのリポジトリへようこそ。このプロジェクトは、開発者やビジネス向けにAIの能力を再定義する画期的な小型言語モデル（SLM）であるPhi-3の力を示しています。

## シナリオの概要

デモシナリオは、「Brunoのお気に入りのスーパーヒーローは誰ですか？」という質問に対して、以下の2つのアプローチで回答します。

1. Phi-3モデルに直接質問する。
2. ファンファクトを読み込んだセマンティックメモリオブジェクトを追加して質問する。

## 完全なシナリオの重要性

Phi-3は、小型言語モデルにおける大きな飛躍を表しており、パフォーマンスと効率性のユニークな組み合わせを提供します。独立して完全なシナリオを処理できるため、開発プロセスが簡素化され、統合の複雑さが軽減されます。

## コードの説明

このコンソールアプリケーションは、Ollamaでホストされるローカルモデルと検索のためのセマンティックメモリを使用するデモを示しています。プログラムは、依存性の注入、設定、セマンティックカーネルおよびメモリ機能のためにいくつかの外部ライブラリを使用します。

## テスト方法

1. ターミナルを開き、現在のプロジェクトに移動します。

    ```bash
    cd .\src\Sample03\
    ```

1. 以下のコマンドでプロジェクトを実行します。

    ```bash
    dotnet run
    ```

1. プロジェクト `Sample03` では、以下の質問に回答します。

    ```csharp
    var question = "What is Bruno's favourite super hero?"
    ```

1. 最初にPhi-3モデルに直接質問します。次に、プログラムは以下の情報をテキストメモリに読み込み、再度質問します。

    ```csharp

    // エンベディングジェネレーターサービスを取得
    var embeddingGenerator = kernel.Services.GetRequiredService<ITextEmbeddingGenerationService>();
    var memory = new SemanticTextMemory(new VolatileMemoryStore(), embeddingGenerator);    

    // コレクションにファクトを追加
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

1. テキストメモリが準備できたら、カーネルにプラグインとしてロードします。

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);
    
    // テキストメモリプラグインをカーネルにインポート
    kernel.ImportPluginFromObject(memoryPlugin);    
    ```

1. こちらは、Codespaceで実行中のデモコンソールアプリケーションです。

    ![Demo console application running in a Codespace](../../../../../../../md/07.Labs/CsharpOllamaCodeSpaces/src/Sample03/img/10RAGPhi3.gif)

## 参考文献

- [Phi-3 Microsoft Blog](https://aka.ms/phi3blog-april)
- [Phi-3 Technical Report](https://aka.ms/phi3-tech-report)
- [Phi-3 Cookbook](https://aka.ms/Phi-3CookBook)
- [Generative AI for beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Semantic Kernel main repository](https://github.com/microsoft/semantic-kernel)
- [Smart Components - Local Embeddings](https://github.com/dotnet-smartcomponents/smartcomponents/blob/main/docs/local-embeddings.md)

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。 出力を確認し、必要な修正を加えてください。