# **AndroidでのPhi-3推論**

AndroidデバイスでPhi-3-miniを使って推論を行う方法を見てみましょう。Phi-3-miniはMicrosoftの新しいモデルシリーズで、大規模言語モデル（LLM）のエッジデバイスやIoTデバイスへの展開を可能にします。

## Semantic Kernelと推論

[Semantic Kernel](https://github.com/microsoft/semantic-kernel)は、Azure OpenAI Service、OpenAIモデル、さらにはローカルモデルと互換性のあるアプリケーションを作成するためのフレームワークです。Semantic Kernelに不慣れな方は、[Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)をご覧になることをお勧めします。

### Semantic Kernelを使ってPhi-3-miniにアクセスする方法

Semantic KernelでHugging Face Connectorと組み合わせて使用できます。この[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)を参照してください。

デフォルトでは、Hugging FaceのモデルIDに対応していますが、ローカルに構築したPhi-3-miniモデルサーバーにも接続できます。

### OllamaやLlamaEdgeで量子化モデルを呼び出す

多くのユーザーは、ローカルでモデルを実行するために量子化モデルを使用することを好みます。[Ollama](https://ollama.com/)や[LlamaEdge](https://llamaedge.com)を使用すると、個々のユーザーが異なる量子化モデルを呼び出すことができます：

#### Ollama

`ollama run Phi-3`を直接実行するか、`.gguf`ファイルへのパスを指定して`Modelfile`を作成することで、オフラインで構成できます。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

クラウドとエッジデバイスで同時に`.gguf`ファイルを使用したい場合、LlamaEdgeは素晴らしい選択です。この[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)を参照して始めてください。

### Androidスマホにインストールして実行する

1. **MLC Chatアプリ**（無料）をAndroidスマホにダウンロードします。
2. APKファイル（148MB）をダウンロードしてデバイスにインストールします。
3. MLC Chatアプリを起動します。Phi-3-miniを含むAIモデルのリストが表示されます。

まとめると、Phi-3-miniはエッジデバイスでの生成AIに新しい可能性を開き、Androidでその機能を探索し始めることができます。

**免責事項**:
この文書は機械翻訳AIサービスを使用して翻訳されています。正確さを期すため努力していますが、自動翻訳には誤りや不正確さが含まれる可能性があります。元の言語での文書が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は一切の責任を負いません。