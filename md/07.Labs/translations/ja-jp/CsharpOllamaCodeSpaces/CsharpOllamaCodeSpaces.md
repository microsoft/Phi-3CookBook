# Ollama C# Playground

![Select the option Ollama with Phi-3 for C#, to create the CodeSpace](./12NewCSOllamaCodespace.png)

1. Codespaceの読み込みが完了すると、[ollama](https://ollama.com/)が事前にインストールされ、最新のPhi-3モデルがダウンロードされ、[.NET 8](https://dotnet.microsoft.com/download)がインストールされているはずです。

1. （オプション）Codespaceターミナルを使用して、Ollamaが[phi3](https://ollama.com/library/phi3)モデルを実行するようにします：

    ```shell
    ollama run phi3
    ```

4. プロンプトからそのモデルにメッセージを送信できます。

    ```shell
    >>> Write a joke about kittens
    ```

5. 数秒後、モデルからの応答がストリーミングされるのを確認できます。

    ![run ollama and ask for a joke](./20ollamarunphi.gif)

1. 言語モデルの使用に関するさまざまな技術については、`.\src`フォルダー内のサンプルプロジェクトを参照してください：

| プロジェクト | 説明 |
|---------|-------------|
| Sample01  | Ollamaモデル内のPhi-3を使用して質問に回答します。 |
| Sample02  | Semantic Kernelを使用してターミナルでチャットを実現します。 |
| [Sample03](./src/Sample03/readme.md)  | ローカル埋め込みモデルとSemantic Kernelを使用してRAGを実現します。ローカルRAGの詳細については[こちら](./src/Sample03/readme.md)を参照してください。 |

## サンプルを実行する方法

1. ターミナルを開き、必要なプロジェクトに移動します。たとえば、`Sample02`を実行する場合、コンソールチャットを実行します。

    ```bash
    cd .\src\Sample02\
    ```

1. 次のコマンドを使用してプロジェクトを実行します

    ```bash
    dotnet run
    ```

1. プロジェクト`Sample02`はカスタムシステムメッセージを定義しています：

    ```csharp
    var history = new ChatHistory();
    history.AddSystemMessage("You are a useful chatbot. If you don't know an answer, say 'I don't know!'. Always reply in a funny ways. Use emojis if possible.");
    ```

1. したがって、ユーザーが`What is the capital of Italy?`のような質問をすると、チャットはローカルモデルを使用して応答します。

    出力は次のようになります：

    ![Chat running demo](./20SampleConsole.png)

## ビデオガイド

GitHubリポジトリでCodespacesとOllamaを使用する方法について詳しく知りたい場合は、以下の3分間のビデオをご覧ください：

[![ビデオを見る](./40ytintro.jpg)](https://youtu.be/HmKpHErUEHM)
# Ollama C# Playground

このラボは、Phi-3を直接GitHub CodespacesでC#のサンプルを使用してテストすることを目的としています。これにより、誰でもブラウザ内でSLM（小型言語モデル）を完全に試すことができます。

## C# + Ollama + Phi-3のCodespaceを作成する方法

1. リポジトリの上部にある`Code`ボタンを使用して、新しいCodespaceを作成します。 [+ New with options ...]を選択します。
![Create Codespace with options](./10NewCodespacesWithOptions.png)

1. オプションページで、`Ollama with Phi-3 for C#`という名前の構成を選択します。
