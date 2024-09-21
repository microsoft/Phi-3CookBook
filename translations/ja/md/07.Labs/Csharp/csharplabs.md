## Phi-3 ラボへようこそ (C# 使用)

ここでは、Phi-3 モデルの強力な異なるバージョンを .NET 環境で統合する方法を示すラボのセレクションを紹介します。

## 前提条件
サンプルを実行する前に、以下がインストールされていることを確認してください：

**.NET 8:** マシンに [最新バージョンの .NET](https://dotnet.microsoft.com/download/dotnet/8.0?WT.mc_id=aiml-137032-kinfeylo) をインストールしてください。

**(オプション) Visual Studio または Visual Studio Code:** .NET プロジェクトを実行できる IDE またはコードエディタが必要です。[Visual Studio](https://visualstudio.microsoft.com/) または [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) が推奨されます。

**git を使用して** [Hugging Face](https://huggingface.co) から利用可能な Phi-3 バージョンの1つをローカルにクローンします。

**phi3-mini-4k-instruct-onnx モデルを** ローカルマシンにダウンロードします：

### モデルを保存するフォルダに移動
```bash
cd c:\phi3\models
```
### lfs のサポートを追加
```bash
git lfs install 
```
### mini 4K instruct モデルをクローンしてダウンロード
```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx
```

### vision 128K モデルをクローンしてダウンロード
```
git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```
**重要:** 現在のデモはモデルの ONNX バージョンを使用するように設計されています。前述の手順で以下のモデルがクローンされます。

![OnnxDownload](../../../../../translated_images/DownloadOnnx.237f4b37d4d8d66d3f4a4a7219d6004bd6f84bc72cce50251ffc034cb28f6fb8.ja.png)

## ラボについて

メインソリューションには、C# を使用して Phi-3 モデルの機能を示すいくつかのサンプルラボがあります。

| プロジェクト | 説明 | 場所 |
| ------------ | ----------- | -------- |
| LabsPhi301    | ローカル phi3 モデルを使用して質問をするサンプルプロジェクトです。`Microsoft.ML.OnnxRuntime` ライブラリを使用してローカル ONNX Phi-3 モデルをロードします。 | .\src\LabsPhi301\ |
| LabsPhi302    | Semantic Kernel を使用してコンソールチャットを実装するサンプルプロジェクトです。 | .\src\LabsPhi302\ |
| LabsPhi303 | ローカル phi3 ビジョンモデルを使用して画像を分析するサンプルプロジェクトです。`Microsoft.ML.OnnxRuntime` ライブラリを使用してローカル ONNX Phi-3 ビジョンモデルをロードします。 | .\src\LabsPhi303\ |
| LabsPhi304 | ローカル phi3 ビジョンモデルを使用して画像を分析するサンプルプロジェクトです。`Microsoft.ML.OnnxRuntime` ライブラリを使用してローカル ONNX Phi-3 ビジョンモデルをロードします。プロジェクトはまた、ユーザーと対話するための異なるオプションを持つメニューを提示します。 | .\src\LabsPhi304\ |
| LabsPhi305 | ollama モデルにホストされた Phi-3 を使用して質問に答えるサンプルプロジェクトです。  |**coming soon**|
| LabsPhi306 | Semantic Kernel を使用してコンソールチャットを実装するサンプルプロジェクトです。 |**coming soon**|
| LabsPhi307  | ローカル埋め込みと Semantic Kernel を使用して RAG を実装するサンプルプロジェクトです。 |**coming soon**|


## プロジェクトの実行方法

プロジェクトを実行するには、以下の手順に従ってください：
1. リポジトリをローカルマシンにクローンします。

1. ターミナルを開き、目的のプロジェクトに移動します。例として、`LabsPhi301` を実行してみましょう。
    ```bash
    cd .\src\LabsPhi301\
    ```

1. プロジェクトを以下のコマンドで実行します
    ```bash
    dotnet run
    ```

1. サンプルプロジェクトはユーザー入力を求め、ローカルモードで応答します。

    実行中のデモは次のようになります：

    ![Chat running demo](../../../../../imgs/07/00/SampleConsole.gif)

    ***注:** 最初の質問に誤字がありますが、Phi-3 は正しい答えを教えてくれます！*

1. プロジェクト `LabsPhi304` はユーザーにさまざまなオプションを選択させ、その後リクエストを処理します。例えば、ローカル画像を分析する場合。

    実行中のデモは次のようになります：

    ![Image Analysis running demo](../../../../../imgs/07/00/SampleVisionConsole.gif)

