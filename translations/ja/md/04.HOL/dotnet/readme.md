## Phi Labs へようこそ - C# を使った活用

.NET 環境でさまざまなバージョンの Phi モデルを統合する方法を紹介する複数のラボを用意しています。

## 前提条件

サンプルを実行する前に、以下がインストールされていることを確認してください：

**.NET 9:** マシンに [最新バージョンの .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) がインストールされていることを確認してください。

**(オプション) Visual Studio または Visual Studio Code:** .NET プロジェクトを実行可能な IDE またはコードエディタが必要です。[Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) または [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) を推奨します。

**git の使用:** [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) から利用可能な Phi-3、Phi3.5、または Phi-4 バージョンのいずれかをローカルにクローンしてください。

**Phi-4 ONNX モデルをローカルにダウンロードする:**

### モデルを保存するフォルダに移動

```bash
cd c:\phi\models
```

### lfs をサポートに追加

```bash
git lfs install 
```

### Phi-4 mini instruct モデルと Phi-4 multi modal モデルをクローンしてダウンロード

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX モデルをローカルにダウンロードする:**

### Phi-3 mini 4K instruct モデルと Phi-3 vision 128K モデルをクローンしてダウンロード

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**重要:** 現在のデモは ONNX バージョンのモデルを使用するように設計されています。上記の手順では以下のモデルをクローンします。

## ラボについて

メインのソリューションには、Phi モデルを C# で活用する能力を示す複数のサンプルラボが含まれています。

| プロジェクト | モデル | 説明 |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 または Phi-3.5 | ユーザーが質問をすることができるサンプルコンソールチャット。プロジェクトはローカルの ONNX Phi-3 モデルを `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` を使用して読み込みます。

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. 以下のコマンドでプロジェクトを実行します。

    ```bash
    dotnet run
    ```

1. サンプルプロジェクトはユーザー入力を受け取り、ローカルモードで応答します。

   実行中のデモは以下のようになります：

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求していますが、自動翻訳にはエラーや不正確さが含まれる場合がありますのでご注意ください。元の言語で書かれた原文を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用によって生じた誤解や誤認に対して、当方は一切の責任を負いません。