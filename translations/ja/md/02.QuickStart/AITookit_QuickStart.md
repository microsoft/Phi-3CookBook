# VScode用AIツールキット (Windows)

[AI Toolkit for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) は、Azure AI Foundry CatalogやHugging Faceなどの最新のAI開発ツールとモデルを統合することで、生成的AIアプリ開発を簡素化します。Azure MLやHugging Faceが提供するAIモデルカタログを閲覧し、ローカルにダウンロード、微調整、テスト、アプリケーションでの使用が可能です。

AI Toolkit Previewはローカルで実行されます。選択したモデルに依存しますが、一部のタスクはWindowsとLinuxのみサポートされています。

ローカルでの推論や微調整には、選択したモデルによってはNVIDIA CUDA GPUのようなGPUが必要になる場合があります。

クラウドリソースをリモートで実行する場合、GPUを持つ必要があります。環境を確認してください。Windows + WSLでローカル実行する場合、WSL Ubuntuディストリビューション18.4以上がインストールされ、デフォルトに設定されている必要があります。

## はじめに

[Windows Subsystem for Linuxのインストール方法についてはこちらをご覧ください](https://learn.microsoft.com/windows/wsl/install?WT.mc_id=aiml-137032-kinfeylo)

および[デフォルトディストリビューションの変更](https://learn.microsoft.com/windows/wsl/install#change-the-default-linux-distribution-installed)についてはこちらをご覧ください。

[AI Tooklit GitHub Repo](https://github.com/microsoft/vscode-ai-toolkit/)

- Windows または Linux。
- **MacOSサポートは近日公開予定**
- WindowsおよびLinuxでの微調整にはNvidia GPUが必要です。さらに、**Windows**ではUbuntuディストリビューション18.4以上のLinux用サブシステムが必要です。 [Windows Subsystem for Linuxのインストール方法についてはこちらをご覧ください](https://learn.microsoft.com/windows/wsl/install) および [デフォルトディストリビューションの変更](https://learn.microsoft.com/windows/wsl/install#change-the-default-linux-distribution-installed)についてはこちらをご覧ください。

### AI Toolkitのインストール

AI Toolkitは[Visual Studio Code Extension](https://code.visualstudio.com/docs/setup/additional-components#_vs-code-extensions)として提供されているため、まず[VS Code](https://code.visualstudio.com/docs/setup/windows?WT.mc_id=aiml-137032-kinfeylo)をインストールし、[VS Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)からAI Toolkitをダウンロードする必要があります。
[AI ToolkitはVisual Studio Marketplaceで利用可能です](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) ので、他のVS Code拡張機能と同様にインストールできます。

VS Code拡張機能のインストールに不慣れな場合は、以下の手順に従ってください：

### サインイン

1. VS Codeのアクティビティバーで**拡張機能**を選択します。
2. 拡張機能検索バーに「AI Toolkit」と入力します。
3. 「AI Toolkit for Visual Studio code」を選択します。
4. **インストール**を選択します。

これで、拡張機能を使用する準備が整いました！

GitHubにサインインするように求められるので、「許可」をクリックして続行してください。GitHubのサインインページにリダイレクトされます。

サインインして手順に従ってください。成功すると、VS Codeにリダイレクトされます。

拡張機能がインストールされると、アクティビティバーにAI Toolkitのアイコンが表示されます。

利用可能なアクションを見てみましょう！

### 利用可能なアクション

AI Toolkitの主要なサイドバーは次のように整理されています：

- **Models**
- **Resources**
- **Playground**
- **Fine-tuning**

Resourcesセクションで利用可能です。開始するには**Model Catalog**を選択してください。

### カタログからモデルをダウンロード

VS CodeのサイドバーからAI Toolkitを起動すると、次のオプションから選択できます：

![AI toolkit model catalog](../../../../translated_images/AItoolkitmodel_catalog.49200354ddc7aceecdcab2080769d898b1fd50424ef9f7014aafeb790028c49d.ja.png)

- **Model Catalog**からサポートされているモデルを見つけてローカルにダウンロード
- **Model Playground**でモデル推論をテスト
- **Model Fine-tuning**でローカルまたはリモートでモデルを微調整
- コマンドパレットを介してクラウドに微調整されたモデルをデプロイ

> [!NOTE]
>
> **GPU Vs CPU**
>
> モデルカードには、モデルのサイズ、プラットフォーム、およびアクセラレータタイプ（CPU、GPU）が表示されます。**少なくとも1つのGPUを持つWindowsデバイス**での最適なパフォーマンスのために、Windows専用のモデルバージョンを選択してください。
>
> これにより、DirectMLアクセラレータに最適化されたモデルが確保されます。
>
> モデル名は次の形式です：
>
> - `{model_name}-{accelerator}-{quantization}-{format}`.
>
> WindowsデバイスにGPUがあるかどうかを確認するには、**タスクマネージャー**を開き、**パフォーマンスタブ**を選択します。GPUがある場合は、「GPU 0」や「GPU 1」といった名前で表示されます。

### プレイグラウンドでモデルを実行

すべてのパラメータが設定されたら、**Generate Project**をクリックします。

モデルがダウンロードされたら、カタログのモデルカードで**Load in Playground**を選択します：

- モデルのダウンロードを開始
- すべての前提条件と依存関係をインストール
- VS Codeワークスペースを作成

![Load model in playground](../../../../translated_images/AItoolkitload_model_into_playground.f78799b4838c6521be6a296729279525958dec6cfb9a26c64752e397dfe19ef2.ja.png)

モデルがダウンロードされると、AI Toolkitからプロジェクトを起動できます。

> ***Note*** リモートで推論や微調整を行うプレビュー機能を試したい場合は、[このガイド](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-overall.md)に従ってください。

### Windows最適化モデル

モデルの応答がストリーミングされてくるのが見えるはずです：

AI Toolkitは、Windows用に最適化された公開AIモデルのコレクションを提供します。モデルはHugging Face、GitHubなどのさまざまな場所に保存されていますが、すべてのモデルを1か所で閲覧し、ダウンロードしてWindowsアプリケーションで使用できます。

![Generation stream](../../../../imgs/04/04/AItoolkitgeneration-gif.gif)

### モデルの選択

*Windows*デバイスに**GPU**がないが

- Phi-3-mini-4k-**directml**-int4-awq-block-128-onnxモデル

を選択した場合、モデルの応答は*非常に遅く*なります。

代わりにCPU最適化バージョンをダウンロードする必要があります：

- Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx.

また、次のことも変更できます：

**コンテキスト指示:** モデルにリクエストの大局的な背景を理解させるために役立ちます。これには、背景情報、欲しいものの例やデモ、タスクの目的の説明が含まれます。

**推論パラメータ:**

- *最大応答長*: モデルが返すトークンの最大数。
- *温度*: モデル温度は、言語モデルの出力のランダム性を制御するパラメータです。温度が高いほど、モデルはリスクを取り、多様な単語を生成します。一方、温度が低いほど、モデルは安全策を取り、より集中した予測可能な応答を生成します。
- *Top P*: 核サンプリングとも呼ばれ、言語モデルが次の単語を予測する際に考慮する可能性のある単語やフレーズの数を制御する設定です。
- *頻度ペナルティ*: モデルが出力で単語やフレーズを繰り返す頻度に影響を与えるパラメータです。値が高い（1.0に近い）ほど、モデルが単語やフレーズを繰り返さないように促します。
- *存在ペナルティ*: 生成的AIモデルで使用され、生成されるテキストの多様性と特異性を促進します。値が高い（1.0に近い）ほど、モデルが新しい多様なトークンを含めるように促します。値が低いと、モデルが一般的またはクリシェ的なフレーズを生成する可能性が高くなります。

### アプリケーションでREST APIを使用する

AI Toolkitには、[OpenAI chat completions format](https://platform.openai.com/docs/api-reference/chat/create)を使用するローカルREST APIウェブサーバーが**ポート5272**で付属しています。

これにより、クラウドAIモデルサービスに依存せずにローカルでアプリケーションをテストできます。たとえば、次のJSONファイルはリクエストのボディを構成する方法を示しています：

```json
{
    "model": "Phi-3-mini-4k-directml-int4-awq-block-128-onnx",
    "messages": [
        {
            "role": "user",
            "content": "what is the golden ratio?"
        }
    ],
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 10,
    "max_tokens": 100,
    "stream": true
}
```

[Postman](https://www.postman.com/)やCURL（クライアントURL）ユーティリティを使用してREST APIをテストできます：

```bash
curl -vX POST http://127.0.0.1:5272/v1/chat/completions -H 'Content-Type: application/json' -d @body.json
```

### Python用OpenAIクライアントライブラリの使用

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
            "content": "what is the golden ratio?",
        }
    ],
    model="Phi-3-mini-4k-cuda-int4-onnx",
)

print(chat_completion.choices[0].message.content)
```

### .NET用Azure OpenAIクライアントライブラリの使用

NuGetを使用してプロジェクトに[Azure OpenAIクライアントライブラリfor .NET](https://www.nuget.org/packages/Azure.AI.OpenAI/)を追加します：

```bash
dotnet add {project_name} package Azure.AI.OpenAI --version 1.0.0-beta.17
```

プロジェクトに**OverridePolicy.cs**という名前のC#ファイルを追加し、次のコードを貼り付けます：

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

次に、**Program.cs**ファイルに次のコードを貼り付けます：

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
        new ChatRequestUserMessage("What is the golden ratio?"),
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

- モデルの発見とプレイグラウンドから始めましょう。
- ローカルコンピューティングリソースを使用したモデルの微調整と推論。
- Azureリソースを使用したリモート微調整と推論

[AI Toolkitでの微調整](../04.Fine-tuning/Finetuning_VSCodeaitoolkit.md)

## AI Toolkit Q&Aリソース

最も一般的な問題と解決策については、[Q&Aページ](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/QA.md)をご覧ください。

**免責事項**:
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期すために努力していますが、自動翻訳には誤りや不正確さが含まれる場合があります。元の言語で書かれた原文が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解について、当社は一切の責任を負いません。