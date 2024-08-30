# AI Toolkit for VScode (Windows)

[AI Toolkit for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) は、Azure AI Studio CatalogやHugging Faceなどのカタログから最新のAI開発ツールとモデルを集約し、生成AIアプリケーションの開発を簡素化します。Azure MLやHugging Faceが提供するAIモデルカタログを閲覧し、ローカルにダウンロードして微調整、テスト、アプリケーションで使用することができます。

AI Toolkit Previewはローカルで実行されます。選択したモデルによっては、WindowsおよびLinuxのみサポートされるタスクがあります。

ローカルでの推論や微調整には、選択したモデルによってはNVIDIA CUDA GPUなどのGPUが必要です。

リモートで実行する場合、クラウドリソースにGPUが必要です。環境を確認してください。Windows + WSLでローカル実行する場合、WSL Ubuntuディストリビューション18.4以上がインストールされ、デフォルトに設定されている必要があります。

## 始めに

[Windows Subsystem for Linuxのインストール方法についてはこちら](https://learn.microsoft.com/windows/wsl/install?WT.mc_id=aiml-137032-kinfeylo)

および[デフォルトのディストリビューションの変更方法](https://learn.microsoft.com/windows/wsl/install#change-the-default-linux-distribution-installed)。

[AI Tooklit GitHubリポジトリ](https://github.com/microsoft/vscode-ai-toolkit/)

- WindowsまたはLinux。
- **MacOSのサポートは近日公開予定**
- WindowsおよびLinuxでの微調整にはNvidia GPUが必要です。さらに、**Windows**ではUbuntuディストリビューション18.4以上のLinuxサブシステムが必要です。[Windows Subsystem for Linuxのインストール方法についてはこちら](https://learn.microsoft.com/windows/wsl/install)および[デフォルトのディストリビューションの変更方法](https://learn.microsoft.com/windows/wsl/install#change-the-default-linux-distribution-installed)。

### AI Toolkitのインストール

AI Toolkitは[Visual Studio Code Extension](https://code.visualstudio.com/docs/setup/additional-components#_vs-code-extensions)として提供されているため、まず[VS Code](https://code.visualstudio.com/docs/setup/windows?WT.mc_id=aiml-137032-kinfeylo)をインストールし、[VS Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)からAI Toolkitをダウンロードする必要があります。
[AI ToolkitはVisual Studio Marketplaceで利用可能です](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)他のVS Code拡張機能と同様にインストールできます。

VS Code拡張機能のインストールに不慣れな場合は、以下の手順に従ってください:

### サインイン

1. VS Codeのアクティビティバーで**拡張機能**を選択します。
1. 拡張機能の検索バーに「AI Toolkit」と入力します。
1. 「AI Toolkit for Visual Studio code」を選択します。
1. **インストール**を選択します。

これで、拡張機能を使用する準備が整いました！

GitHubにサインインするように求められるので、「許可」をクリックして続行してください。GitHubのサインインページにリダイレクトされます。

サインインして手順に従ってください。完了後、VS Codeにリダイレクトされます。

拡張機能がインストールされると、アクティビティバーにAI Toolkitアイコンが表示されます。

利用可能なアクションを探索しましょう！

### 利用可能なアクション

AI Toolkitの主要なサイドバーは次のように整理されています

- **モデル**
- **リソース**
- **プレイグラウンド**
- **微調整**

リソースセクションで利用可能です。開始するには**モデルカタログ**を選択します。

### カタログからモデルをダウンロードする

VS CodeのサイドバーからAI Toolkitを起動すると、次のオプションから選択できます:

![AI toolkit model catalog](../../../../imgs/04/04/AItoolkitmodel_catalog.png)

- **モデルカタログ**からサポートされているモデルを見つけてローカルにダウンロードします。
- **モデルプレイグラウンド**でモデル推論をテストします。
- **モデル微調整**でローカルまたはリモートでモデルを微調整します。
- AI Toolkitのコマンドパレットを介して微調整されたモデルをクラウドにデプロイします。

> [!NOTE]
>
> **GPUとCPU**
>
> モデルカードには、モデルのサイズ、プラットフォーム、およびアクセラレータの種類（CPU、GPU）が表示されます。**少なくとも1つのGPUを持つWindowsデバイス**で最適なパフォーマンスを得るには、Windows専用のモデルバージョンを選択してください。
>
> これにより、DirectMLアクセラレータ用に最適化されたモデルが確保されます。
>
> モデル名の形式は次のとおりです:
>
> - `{model_name}-{accelerator}-{quantization}-{format}`。
>
> WindowsデバイスにGPUがあるかどうかを確認するには、**タスクマネージャー**を開き、**パフォーマンス**タブを選択します。GPUがある場合、「GPU 0」や「GPU 1」などの名前で表示されます。

### プレイグラウンドでモデルを実行する

すべてのパラメータが設定されたら、**プロジェクトを生成**をクリックします。

モデルがダウンロードされたら、カタログのモデルカードで**プレイグラウンドに読み込む**を選択します:

- モデルのダウンロードを開始します。
- すべての前提条件と依存関係をインストールします。
- VS Codeワークスペースを作成します。

![Load model in playground](../../../../imgs/04/04/AItoolkitload_model_into_playground.png)

モデルがダウンロードされたら、AI Toolkitからプロジェクトを起動できます。

> ***注意*** プレビュー機能を試してリモートで推論や微調整を行いたい場合は、[このガイド](https://aka.ms/previewFinetune)に従ってください。

### Windows最適化モデル

モデルの応答がストリーミングで返されるのが見えるはずです:

AI Toolkitは、Windows用に最適化された公開されているAIモデルのコレクションを提供します。これらのモデルはHugging Face、GitHubなどの異なる場所に保存されていますが、すべてのモデルを一箇所で見つけてダウンロードし、Windowsアプリケーションで使用することができます。

![Generation stream](../../../../imgs/04/04/AItoolkitgeneration-gif.gif)

### モデルの選択

*Windows*デバイスに**GPU**がない場合、次のモデルを選択した場合

- Phi-3-mini-4k-**directml**-int4-awq-block-128-onnxモデル

モデルの応答は*非常に遅く*なります。

代わりに、CPU最適化バージョンをダウンロードする必要があります:

- Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx。

また、次のように変更することもできます:

**コンテキストの指示:** モデルがリクエストの全体像を理解するのを助けます。これには、背景情報、例/デモ、またはタスクの目的の説明が含まれます。

**推論パラメータ:**

- *最大応答長:* モデルが返す最大トークン数。
- *温度:* モデルの温度は、言語モデルの出力のランダム性を制御するパラメータです。温度が高いほど、モデルはより多様な単語を生成し、リスクを取ります。一方、温度が低いほど、モデルはより保守的で、集中した予測可能な応答を生成します。
- *Top P:* 核サンプリングとも呼ばれ、言語モデルが次の単語を予測する際に考慮する可能性のある単語やフレーズの数を制御する設定です。
- *頻度ペナルティ:* このパラメータは、モデルが出力で単語やフレーズを繰り返す頻度に影響します。値が高い（1.0に近い）ほど、モデルは単語やフレーズの繰り返しを避けるようになります。
- *存在ペナルティ:* このパラメータは、生成AIモデルで多様性と特異性を促進するために使用されます。値が高い（1.0に近い）ほど、モデルはより新規で多様なトークンを含むようになります。値が低いほど、モデルは一般的なフレーズやクリシェを生成する可能性が高くなります。

### アプリケーションでREST APIを使用する

AI Toolkitには、[OpenAIチャット補完形式](https://platform.openai.com/docs/api-reference/chat/create)を使用する**ポート5272**のローカルREST API Webサーバーが付属しています。

これにより、クラウドAIモデルサービスに依存せずにローカルでアプリケーションをテストできます。たとえば、次のJSONファイルはリクエストの本文を設定する方法を示しています:

```json
{
    "model": "Phi-3-mini-4k-directml-int4-awq-block-128-onnx",
    "messages": [
        {
            "role": "user",
            "content": "黄金比とは何ですか？"
        }
    ],
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 10,
    "max_tokens": 100,
    "stream": true
}
```

[Postman](https://www.postman.com/)やCURL（Client URL）ユーティリティを使用してREST APIをテストできます:

```bash
curl -vX POST http://127.0.0.1:5272/v1/chat/completions -H 'Content-Type: application/json' -d @body.json
```

### OpenAIクライアントライブラリfor Pythonを使用する

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:5272/v1/", 
    api_key="x" # required for the API but not used
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "黄金比とは何ですか？",
        }
    ],
    model="Phi-3-mini-4k-cuda-int4-onnx",
)

print(chat_completion.choices[0].message.content)
```

### Azure OpenAIクライアントライブラリfor .NETを使用する

[Azure OpenAIクライアントライブラリfor .NET](https://www.nuget.org/packages/Azure.AI.OpenAI/)をNuGetを使用してプロジェクトに追加します:

```bash
dotnet add {project_name} package Azure.AI.OpenAI --version 1.0.0-beta.17
```

**OverridePolicy.cs**という名前のC#ファイルをプロジェクトに追加し、次のコードを貼り付けます:

```csharp
// OverridePolicy.cs
using Azure.Core.Pipeline;
using Azure.Core;

internal partial class OverrideRequestUriPolicy(Uri overrideUri)
    : HttpPipelineSynchronousPolicy
{
    private readonly Uri _overrideUri = overrideUri;

    public override void OnSendingRequest(HttpMessage message)
    {
        message.Request.Uri.Reset(_overrideUri);
    }
}
```

次に、**Program.cs**ファイルに次のコードを貼り付けます:

```csharp
// Program.cs
using Azure.AI.OpenAI;

Uri localhostUri = new("http://localhost:5272/v1/chat/completions");

OpenAIClientOptions clientOptions = new();
clientOptions.AddPolicy(
    new OverrideRequestUriPolicy(localhostUri),
    Azure.Core.HttpPipelinePosition.BeforeTransport);
OpenAIClient client = new(openAIApiKey: "unused", clientOptions);

ChatCompletionsOptions options = new()
{
    DeploymentName = "Phi-3-mini-4k-directml-int4-awq-block-128-onnx",
    Messages =
    {
        new ChatRequestSystemMessage("You are a helpful assistant. Be brief and succinct."),
        new ChatRequestUserMessage("黄金比とは何ですか？"),
    }
};

StreamingResponse<StreamingChatCompletionsUpdate> streamingChatResponse
    = await client.GetChatCompletionsStreamingAsync(options);

await foreach (StreamingChatCompletionsUpdate chatChunk in streamingChatResponse)
{
    Console.Write(chatChunk.ContentUpdate);
}
```

## AI Toolkitでの微調整

- モデルの発見とプレイグラウンドから始めます。
- ローカルの計算リソースを使用してモデルの微調整と推論を行います。
- Azureリソースを使用してリモートで微調整と推論を行います。

[AI Toolkitでの微調整](../../../04.Fine-tuning/Finetuning_VSCodeaitoolkit.md)

## AI Toolkit Q&Aリソース

最も一般的な問題と解決策については、[Q&Aページ](https://github.com/microsoft/vscode-ai-toolkit/blob/main/QA.md)を参照してください。
