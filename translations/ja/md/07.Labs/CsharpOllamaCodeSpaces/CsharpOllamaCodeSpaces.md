# Ollama C# プレイグラウンド

このラボは、GitHub Codespaces内でC#のサンプルを使ってPhi-3をテストするために設計されています。ブラウザだけでSLM（小規模言語モデル）を試す簡単な方法を提供します。

## C# + Ollama + Phi-3 Codespace の作成方法

1. リポジトリの上部にある `Code` ボタンを使って新しいCodespaceを作成します。 [+ New with options ...] を選択します。
![Create Codespace with options](../../../../../translated_images/10NewCodespacesWithOptions.b50796422fc7f6d13721a50b72de8b62d83a7951fdace787a0dc12edc22ce807.ja.png)

1. オプションページから `Ollama with Phi-3 for C#` という設定を選択します。

![Select the option Ollama with Phi-3 for C#, to create the CodeSpace](../../../../../translated_images/12NewCSOllamaCodespace.38aab1c942efe444653b4141918ce6d081ce6e9638e0d16117f5b93ce1deee42.ja.png)

1. Codespaceがロードされると、[ollama](https://ollama.com/)が事前にインストールされ、最新のPhi-3モデルがダウンロードされ、[.NET 8](https://dotnet.microsoft.com/download)がインストールされているはずです。

1. （オプション）Codespaceのターミナルを使って、[phi3](https://ollama.com/library/phi3) モデルを実行するようOllamaに指示します:

    ```shell
    ollama run phi3
    ```

4. プロンプトからそのモデルにメッセージを送信できます。

    ```shell
    >>> Write a joke about kittens
    ```

5. 数秒後、モデルからのレスポンスがストリームで表示されるはずです。

    ![run ollama and ask for a joke](../../../../../md/07.Labs/CsharpOllamaCodeSpaces/20ollamarunphi.gif)

1. 言語モデルで使用されるさまざまな技術について学ぶために、`.\src` フォルダーのサンプルプロジェクトをチェックしてください:

| プロジェクト | 説明 |
|---------|-------------|
| Sample01  | OllamaモデルにホストされたPhi-3を使って質問に答えるサンプルプロジェクトです。 |
| Sample02  | Semantic Kernelを使用してコンソールチャットを実装したサンプルプロジェクトです。 |
| [Sample03](./src/Sample03/readme.md)  | ローカルの埋め込みとSemantic Kernelを使用してRAGを実装したサンプルプロジェクトです。ローカルRAGの詳細は[こちら](./src/Sample03/readme.md)をチェックしてください。 |

## サンプルの実行方法

1. ターミナルを開き、実行したいプロジェクトに移動します。例えば、`Sample02`（コンソールチャット）を実行します。

    ```bash
    cd .\src\Sample02\
    ```

1. 次のコマンドでプロジェクトを実行します

    ```bash
    dotnet run
    ```

1. プロジェクト `Sample02` はカスタムシステムメッセージを定義します:

    ```csharp
    var history = new ChatHistory();
    history.AddSystemMessage("You are a useful chatbot. If you don't know an answer, say 'I don't know!'. Always reply in a funny ways. Use emojis if possible.");
    ```

1. したがって、ユーザーが `What is the capital of Italy?` と質問すると、チャットはローカルモードを使って返信します。
   
    出力は以下のようになります：

    ![Chat running demo](../../../../../translated_images/20SampleConsole.22997336ed0fa683bcc3238bb8e953b3a533d28196bc42e7cd1527261dd0689b.ja.png)

## ビデオチュートリアル

GitHubリポジトリでCodespacesをOllamaと一緒に使用する方法についてもっと学びたい場合は、以下の3分間のビデオをチェックしてください：

[![Watch the video](../../../../../translated_images/40ytintro.09cf17cbf9dd4cf8faa91668c42172417f86851025ef325454ce65903606bb9e.ja.jpg)](https://youtu.be/HmKpHErUEHM)

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。 出力を確認し、必要な修正を行ってください。