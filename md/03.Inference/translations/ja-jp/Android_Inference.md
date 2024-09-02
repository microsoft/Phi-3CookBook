# **AndroidでPhi-3を推論する**

AndroidデバイスでPhi-3-miniを使用して推論を行う方法を探ってみましょう。Phi-3-miniは、Microsoftが提供する新しいモデルシリーズで、エッジデバイスやIoTデバイスに大型言語モデル（LLM）をデプロイすることができます。

## セマンティックカーネルと推論:
[セマンティックカーネル](https://github.com/microsoft/semantic-kernel)は、Azure OpenAIサービス、OpenAIモデル、さらにはローカルモデルと互換性のあるアプリケーションを作成できるアプリケーションフレームワークです。セマンティックカーネルに不慣れな方は、[セマンティックカーネルクックブック](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)を参照することをお勧めします。

### セマンティックカーネルを使用してPhi-3-miniにアクセスするには:
セマンティックカーネルのHugging Faceコネクタと組み合わせて使用することができます。[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)

デフォルトでは、Hugging Face上のモデルIDに対応しています。ただし、ローカルで構築したPhi-3-miniモデルサーバーに接続することもできます。

### OllamaまたはLlamaEdgeを使用して量子化モデルを呼び出す:

多くのユーザーは、量子化モデルを使用してローカルでモデルを実行することを好みます。
[Ollama](https://ollama.com/)および[LlamaEdge](https://llamaedge.com)は、個々のユーザーが異なる量子化モデルを呼び出すことを可能にします:

**Ollama**

直接「ollama run Phi-3」を実行するか、ggufファイルのパスを含むModelfileを作成してオフラインで設定することができます。

```
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> {{.Prompt}}<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096

```
[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

**LlamaEdge**

クラウドとエッジデバイスの両方でggufを同時に使用したい場合、LlamaEdgeは優れた選択肢です。
[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)

### Androidスマートフォンにインストールして実行する:
Androidスマートフォン用の無料のMLC Chatアプリをダウンロードします。
APKファイル（148MB）をダウンロードしてインストールする必要があります。
MLC Chatアプリを起動すると、Phi-3-miniを含むAIモデルのリストが表示されます。

まとめると、Phi-3-miniはエッジデバイス上での生成AIにエキサイティングな可能性をもたらし、Androidでその機能を探索し始めることができます。
