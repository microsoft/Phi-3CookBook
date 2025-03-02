# **AndroidでのPhi-3の推論**

AndroidデバイスでPhi-3-miniを使った推論を行う方法を見ていきましょう。Phi-3-miniはMicrosoftが提供する新しいモデルシリーズで、大規模言語モデル（LLM）をエッジデバイスやIoTデバイスに展開することを可能にします。

## Semantic Kernelと推論

[Semantic Kernel](https://github.com/microsoft/semantic-kernel)は、Azure OpenAI Service、OpenAIモデル、さらにはローカルモデルと互換性のあるアプリケーションを作成するためのフレームワークです。Semantic Kernelを初めて使用する方は、[Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)をご覧になることをお勧めします。

### Semantic Kernelを使ってPhi-3-miniにアクセスするには

Semantic KernelのHugging Face Connectorを組み合わせて利用できます。この[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)を参考にしてください。

デフォルトでは、Hugging Face上のモデルIDに対応しています。ただし、ローカルで構築したPhi-3-miniモデルサーバーに接続することも可能です。

### OllamaやLlamaEdgeを使った量子化モデルの呼び出し

多くのユーザーは、ローカルでモデルを実行するために量子化モデルを使用することを好みます。[Ollama](https://ollama.com/)や[LlamaEdge](https://llamaedge.com)を使えば、さまざまな量子化モデルを個別に呼び出すことができます。

#### Ollama

`ollama run Phi-3`を直接実行するか、`Modelfile`を作成して`.gguf`ファイルへのパスを指定することでオフライン設定が可能です。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

クラウドとエッジデバイスの両方で`.gguf`ファイルを使用したい場合、LlamaEdgeは優れた選択肢です。この[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)を参考にして始めてみてください。

### Androidスマートフォンへのインストールと実行

1. **MLC Chatアプリをダウンロード**（無料）します。
2. APKファイル（148MB）をダウンロードし、デバイスにインストールします。
3. MLC Chatアプリを起動すると、Phi-3-miniを含むAIモデルのリストが表示されます。

まとめると、Phi-3-miniはエッジデバイス上で生成AIを活用するためのエキサイティングな可能性を提供し、Androidでその機能をすぐに探求することができます。

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の母国語で書かれた文書が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や解釈の誤りについて、当社は一切の責任を負いません。