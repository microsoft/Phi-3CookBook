Phi-3-miniの文脈において、推論とは、入力データに基づいてモデルを使用して予測や出力を生成するプロセスを指します。ここでは、Phi-3-miniとその推論能力について詳しく説明します。

Phi-3-miniは、MicrosoftがリリースしたPhi-3シリーズの一部です。これらのモデルは、小型言語モデル（SLM）で可能なことを再定義するために設計されています。

以下は、Phi-3-miniとその推論能力に関する主要なポイントです：

## **Phi-3-miniの概要:**
- Phi-3-miniのパラメータサイズは38億です。
- 従来のコンピューティングデバイスだけでなく、モバイルデバイスやIoTデバイスなどのエッジデバイスでも実行できます。
- Phi-3-miniのリリースにより、個人や企業がリソースが限られた環境でもさまざまなハードウェアデバイスにSLMをデプロイできるようになりました。
- 伝統的なPyTorch形式、gguf形式の量子化バージョン、およびONNXベースの量子化バージョンなど、さまざまなモデル形式に対応しています。

## **Phi-3-miniへのアクセス:**
Phi-3-miniにアクセスするには、[Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)を使用してCopilotアプリケーションで使用できます。Semantic Kernelは、Azure OpenAI Service、Hugging Faceのオープンソースモデル、およびローカルモデルと一般的に互換性があります。
また、[Ollama](https://ollama.com)や[LlamaEdge](https://llamaedge.com)を使用して量子化モデルを呼び出すこともできます。Ollamaは個々のユーザーがさまざまな量子化モデルを呼び出すことを可能にし、LlamaEdgeはGGUFモデルのクロスプラットフォーム対応を提供します。

## **量子化モデル:**
多くのユーザーはローカル推論のために量子化モデルを使用することを好みます。例えば、Ollama run Phi-3を直接実行したり、Modelfileを使用してオフラインで設定したりできます。ModelfileはGGUFファイルのパスとプロンプト形式を指定します。

## **生成AIの可能性:**
Phi-3-miniのようなSLMを組み合わせることで、生成AIの新しい可能性が広がります。推論は最初のステップに過ぎず、これらのモデルはリソースが限られた、遅延が重要な、コストが制約されたシナリオでさまざまなタスクに使用できます。

## **Phi-3-miniで生成AIを解き放つ：推論とデプロイメントのガイド**
Semantic Kernel、Ollama/LlamaEdge、およびONNX Runtimeを使用してPhi-3-miniモデルにアクセスし、推論を行う方法を学び、さまざまなアプリケーションシナリオで生成AIの可能性を探りましょう。

**特徴**
phi3-miniモデルの推論：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

まとめると、Phi-3-miniは開発者がさまざまなモデル形式を探求し、さまざまなアプリケーションシナリオで生成AIを活用することを可能にします。

**免責事項**:
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期していますが、自動翻訳には誤りや不正確さが含まれる可能性があることにご注意ください。原文の言語で書かれた元の文書が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。