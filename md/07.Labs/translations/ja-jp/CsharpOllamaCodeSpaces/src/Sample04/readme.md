# Phi-3、SemanticKernel、およびTextMemoryを使用した完全なローカルRAGシナリオ

## はじめに

Phi-3、SemanticKernel、およびTextMemoryを使用した完全なローカルRAGシナリオのリポジトリへようこそ。このプロジェクトは、開発者や企業のためにAIの能力を再定義する画期的なSmall Language Model（SLM）であるPhi-3の力を示しています。

## シナリオの概要

このデモシナリオは、「Brunoの好きなスーパーヒーローは誰ですか？」という質問に対して、2つの異なるアプローチを使用して答えることを目的としています：

1. Phi-3モデルに直接質問する。
2. ファンの事実を読み込んだセマンティックメモリオブジェクトを追加し、その後質問する。

## 完全なシナリオの重要性

Phi-3はSmall Language Modelsにおいて大きな飛躍を遂げ、パフォーマンスと効率のユニークな組み合わせを提供します。Phi-3は独立して完全なシナリオを処理することができ、開発プロセスを簡素化し、統合の複雑さを軽減します。

## コードの説明

このコンソールアプリケーションは、Ollamaでホストされているローカルモデルと検索のためのセマンティックメモリの使用を示しています。このプログラムは、依存性注入、構成、およびセマンティックカーネルとメモリ機能のためのいくつかの外部ライブラリを使用しています。

## テスト方法

1. ターミナルを開き、現在のプロジェクトに移動します。

    ```bash
    cd .\src\Sample03\
    ```

1. 次のコマンドを使用してプロジェクトを実行します

    ```bash
    dotnet run
    ```

1. プロジェクト`Sample03`は、次の質問に答えます：

    ```csharp
    var question = "Brunoの好きなスーパーヒーローは誰ですか？"
    ```

1. 最初に質問をPhi-3モデルに直接尋ねます。その後、プログラムは次の情報をテキストメモリに読み込み、再度質問します。

    ```csharp

    // 埋め込み生成サービスを取得
    var embeddingGenerator = kernel.Services.GetRequiredService<ITextEmbeddingGenerationService>();
    var memory = new SemanticTextMemory(new VolatileMemoryStore(), embeddingGenerator);

    // コレクションに事実を追加
    const string MemoryCollectionName = "fanFacts";

    await memory.SaveInformationAsync(MemoryCollectionName, id: "info1",
            text: "Giselaの好きなスーパーヒーローはバットマンです");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info2",
            text: "Giselaが最後に見たスーパーヒーロー映画はガーディアンズ・オブ・ギャラクシー Vol 3です");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info3",
            text: "Brunoの好きなスーパーヒーローはインビンシブルです");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info4",
            text: "Brunoが最後に見たスーパーヒーロー映画はアクアマンIIです");
    await memory.SaveInformationAsync(MemoryCollectionName, id: "info5",
            text: "Brunoはスーパーヒーロー映画「エターナルズ」が好きではありません");
    ```

1. テキストメモリが準備できたら、それをプラグインとしてカーネルに読み込みます。

    ```csharp
    TextMemoryPlugin memoryPlugin = new(memory);

    // テキストメモリプラグインをカーネルにインポート
    kernel.ImportPluginFromObject(memoryPlugin);
    ```

1. これはCodespaceで実行されているデモコンソールアプリケーションです：

    ![Codespaceで実行されているデモコンソールアプリケーション](../Sample03/img/10RAGPhi3.gif)

## 参考文献

- [Phi-3 Microsoft Blog](https://aka.ms/phi3blog-april)
- [Phi-3 Technical Report](https://aka.ms/phi3-tech-report)
- [Phi-3 Cookbook](https://aka.ms/Phi-3CookBook)
- [Generative AI for beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Semantic Kernel main repository](https://github.com/microsoft/semantic-kernel)
- [Smart Components - Local Embeddings](https://github.com/dotnet-smartcomponents/smartcomponents/blob/main/docs/local-embeddings.md)
