## C#を使用したPhi-3ラボへようこそ。

.NET環境で強力なPhi-3モデルの異なるバージョンを統合する方法を紹介するラボの選択があります。

## 前提条件
サンプルを実行する前に、以下がインストールされていることを確認してください：

**.NET 8:** [最新バージョンの.NET](https://dotnet.microsoft.com/download/dotnet/8.0?WT.mc_id=aiml-137032-kinfeylo)がマシンにインストールされていることを確認してください。

**（オプション）Visual StudioまたはVisual Studio Code:** .NETプロジェクトを実行できるIDEまたはコードエディタが必要です。[Visual Studio](https://visualstudio.microsoft.com/)または[Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo)を推奨します。

**gitを使用して**、[Hugging Face](https://huggingface.co)から利用可能なPhi-3バージョンのいずれかをローカルにクローンします。

**phi3-mini-4k-instruct-onnxモデルをダウンロード**してローカルマシンに保存します：

### モデルを保存するフォルダに移動
```bash
cd c:\phi3\models
```
### lfsのサポートを追加
```bash
git lfs install
```
### mini 4K instructモデルをクローンしてダウンロード
```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx
```

### vision 128Kモデルをクローンしてダウンロード
```
git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```
**重要:** 現在のデモはモデルのONNXバージョンを使用するように設計されています。前の手順では以下のモデルをクローンします。

![OnnxDownload](../../../../../imgs/07/00/DownloadOnnx.png)

## ラボについて

メインのソリューションには、C#を使用してPhi-3モデルの機能を示すいくつかのサンプルラボがあります。

| プロジェクト | 説明 | 場所 |
| ------------ | ----------- | -------- |
| LabsPhi301    | これはローカルのphi3モデルを使用して質問をするサンプルプロジェクトです。このプロジェクトは`Microsoft.ML.OnnxRuntime`ライブラリを使用してローカルのONNX Phi-3モデルをロードします。 | .\src\LabsPhi301\ |
| LabsPhi302    | これはSemantic Kernelを使用してコンソールチャットを実装するサンプルプロジェクトです。 | .\src\LabsPhi302\ |
| LabsPhi303 | これはローカルのphi3ビジョンモデルを使用して画像を分析するサンプルプロジェクトです。このプロジェクトは`Microsoft.ML.OnnxRuntime`ライブラリを使用してローカルのONNX Phi-3ビジョンモデルをロードします。 | .\src\LabsPhi303\ |
| LabsPhi304 | これはローカルのphi3ビジョンモデルを使用して画像を分析するサンプルプロジェクトです。このプロジェクトは`Microsoft.ML.OnnxRuntime`ライブラリを使用してローカルのONNX Phi-3ビジョンモデルをロードします。このプロジェクトはユーザーと対話するためのメニューも提供します。 | .\src\LabsPhi304\ |
| LabsPhi305 | これはollamaモデルにホストされたPhi-3を使用して質問に答えるサンプルプロジェクトです。 |**近日公開**|
| LabsPhi306 | これはSemantic Kernelを使用してコンソールチャットを実装するサンプルプロジェクトです。 |**近日公開**|
| LabsPhi307  | これはローカルの埋め込みとSemantic Kernelを使用してRAGを実装するサンプルプロジェクトです。 |**近日公開**|

## プロジェクトの実行方法

プロジェクトを実行するには、以下の手順に従ってください：
1. リポジトリをローカルマシンにクローンします。

1. ターミナルを開き、目的のプロジェクトに移動します。例として、`LabsPhi301`を実行します。
    ```bash
    cd .\src\LabsPhi301\
    ```

1. 次のコマンドを使用してプロジェクトを実行します
    ```bash
    dotnet run
    ```

1. サンプルプロジェクトはユーザー入力を求め、ローカルモードを使用して応答します。

    実行中のデモは次のようになります：

    ![Chat running demo](../../../../../imgs/07/00/SampleConsole.gif)

    ***注意:** 最初の質問にはタイプミスがありますが、Phi-3は正しい答えを共有します！*

1. プロジェクト`LabsPhi304`はユーザーに異なるオプションを選択させ、その後リクエストを処理します。例として、ローカル画像を分析します。

    実行中のデモは次のようになります：

    ![Image Analysis running demo](../../../../../imgs/07/00/SampleVisionConsole.gif)
