# **OllamaでPhi-3を使用する**

[Ollama](https://ollama.com)は、より多くの人々が簡単なスクリプトを使用してオープンソースのLLMまたはSLMを直接デプロイできるようにし、ローカルのCopilotアプリケーションシナリオを支援するためのAPIを構築することもできます。

## **1. インストール**

OllamaはWindows、macOS、およびLinuxで動作します。このリンク([https://ollama.com/download](https://ollama.com/download))からOllamaをインストールできます。インストールが成功すると、ターミナルウィンドウを使用してOllamaスクリプトを直接使用してPhi-3を呼び出すことができます。Ollamaで利用可能なすべてのライブラリを確認できます[available libaries in Ollama](https://ollama.com/library)。このリポジトリをCodespaceで開くと、Ollamaがすでにインストールされていることがわかります。

```bash

ollama run phi3

```

> [!NOTE]
> 初めて実行するときは、モデルが最初にダウンロードされます。もちろん、ダウンロードしたPhi-3モデルを直接指定することもできます。WSLを例にとってコマンドを実行します。モデルが正常にダウンロードされると、ターミナルで直接対話できます。

![run](../../../../imgs/02/Ollama/ollama_run.png)

## **2. Ollamaからphi-3 APIを呼び出す**

Ollamaが生成するPhi-3 APIを呼び出す場合は、ターミナルでこのコマンドを使用してOllamaサーバーを起動できます。

```bash

ollama serve

```

> [!NOTE]
> MacOSまたはLinuxを実行している場合、次のエラーが発生する可能性があります **"Error: listen tcp 127.0.0.1:11434: bind: address already in use"** このコマンドを実行するときにこのエラーが発生する可能性があります。このエラーは通常、サーバーがすでに実行されていることを示しているため、無視するか、Ollamaを停止して再起動することができます。

**macOS**

```bash

brew services restart ollama

```

**Linux**

```bash

sudo systemctl stop ollama

```

Ollamaは2つのAPIをサポートしています：generateとchat。必要に応じて、Ollamaが提供するモデルAPIを呼び出し、ポート11434で実行されているローカルサービスにリクエストを送信できます。

**Chat**

```bash

curl http://127.0.0.1:11434/api/chat -d '{
  "model": "phi3",
  "messages": [
    {
      "role": "system",
      "content": "Your are a python developer."
    },
    {
      "role": "user",
      "content": "Help me generate a bubble algorithm"
    }
  ],
  "stream": false
  
}'


```

これはPostmanの結果です

![Screenshot of JSON results for chat request](../../../../imgs/02/Ollama/ollama_chat.png)

```bash

curl http://127.0.0.1:11434/api/generate -d '{
  "model": "phi3",
  "prompt": "<|system|>Your are my AI assistant.<|end|><|user|>tell me how to learn AI<|end|><|assistant|>",
  "stream": false
}'


```

これはPostmanの結果です

![Screenshot of JSON results for generate request](../../../../imgs/02/Ollama/ollama_gen.png)

## 追加リソース

Ollamaの[ライブラリ](https://ollama.com/library)で利用可能なモデルのリストを確認してください。

このコマンドを使用してOllamaサーバーからモデルを取得します

```bash
ollama pull phi3
```

このコマンドを使用してモデルを実行します

```bash
ollama run phi3
```

***注意:*** 詳細については、このリンク[https://github.com/ollama/ollama/blob/main/docs/api.md](https://github.com/ollama/ollama/blob/main/docs/api.md)を参照してください

## PythonからOllamaを呼び出す

`requests`または`urllib3`を使用して、上記のローカルサーバーエンドポイントにリクエストを送信できます。ただし、PythonでOllamaを使用する一般的な方法は、OllamaがOpenAI互換のサーバーエンドポイントも提供しているため、[openai](https://pypi.org/project/openai/) SDKを介することです。

phi3-miniの例を次に示します：

```python
import openai

client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)

response = client.chat.completions.create(
    model="phi3",
    temperature=0.7,
    n=1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about a hungry cat"},
    ],
)

print("Response:")
print(response.choices[0].message.content)
```

## JavaScriptからOllamaを呼び出す

```javascript
// Example of Summarize a file with Phi-3
script({
    model: "ollama:phi3",
    title: "Summarize with Phi-3",
    system: ["system"],
})

// Example of summarize
const file = def("FILE", env.files)
$`Summarize ${file} in a single paragraph.`
```

## C#からOllamaを呼び出す

新しいC#コンソールアプリケーションを作成し、次のNuGetパッケージを追加します：

```bash
dotnet add package Microsoft.SemanticKernel --version 1.13.0
```

次に、このコードを`Program.cs`ファイルに置き換えます

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;

// add chat completion service using the local ollama server endpoint
#pragma warning disable SKEXP0001, SKEXP0003, SKEXP0010, SKEXP0011, SKEXP0050, SKEXP0052
builder.AddOpenAIChatCompletion(
    modelId: "phi3.5",
    endpoint: new Uri("http://localhost:11434/"),
    apiKey: "non required");

// invoke a simple prompt to the chat service
string prompt = "Write a joke about kittens";
var response = await kernel.InvokePromptAsync(prompt);
Console.WriteLine(response.GetValue<string>());
```

次のコマンドを使用してアプリを実行します：

```bash
dotnet run
```
