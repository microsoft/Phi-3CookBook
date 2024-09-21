# **AndroidでのPhi-3推論**

AndroidデバイスでPhi-3-miniを使って推論を行う方法を見ていきましょう。Phi-3-miniは、Microsoftが提供する新しいモデルシリーズで、エッジデバイスやIoTデバイスで大規模言語モデル（LLM）を展開することができます。

## Semantic Kernelと推論

[Semantic Kernel](https://github.com/microsoft/semantic-kernel)は、Azure OpenAI Service、OpenAIモデル、さらにはローカルモデルと互換性のあるアプリケーションを作成するためのフレームワークです。Semantic Kernelに初めて触れる方は、[Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)をご覧になることをお勧めします。

### Semantic Kernelを使ってPhi-3-miniにアクセスする

Semantic KernelのHugging Face Connectorと組み合わせて使用することができます。この[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)を参照してください。

デフォルトでは、Hugging FaceのモデルIDに対応していますが、ローカルに構築したPhi-3-miniモデルサーバーにも接続できます。

### OllamaやLlamaEdgeで量子化モデルを呼び出す

多くのユーザーは、ローカルでモデルを実行するために量子化モデルを使用することを好みます。[Ollama](https://ollama.com/)や[LlamaEdge](https://llamaedge.com)を使用すると、個々のユーザーが異なる量子化モデルを呼び出すことができます。

#### Ollama

直接 `ollama run Phi-3` を実行するか、オフラインで `Modelfile` を作成し、`.gguf` ファイルのパスを設定します。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> {{.Prompt}}<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

クラウドとエッジデバイスの両方で `.gguf` ファイルを使用したい場合、LlamaEdgeは素晴らしい選択です。始めるには、この[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)を参照してください。

### Androidスマートフォンにインストールして実行する

1. **MLC Chatアプリ**（無料）をAndroidスマートフォンにダウンロードします。
2. APKファイル（148MB）をダウンロードし、デバイスにインストールします。
3. MLC Chatアプリを起動します。Phi-3-miniを含むAIモデルのリストが表示されます。

まとめると、Phi-3-miniはエッジデバイスでの生成AIに新たな可能性を開き、Androidでその機能を探索し始めることができます。

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。
出力内容を確認し、必要に応じて修正を行ってください。