Phi-3-miniの文脈では、推論とはモデルを使用して入力データに基づいて予測や出力を生成するプロセスを指します。ここでは、Phi-3-miniとその推論機能について詳しく説明します。

Phi-3-miniは、MicrosoftがリリースしたPhi-3シリーズのモデルの一部です。これらのモデルは、小型言語モデル（SLM）で可能なことを再定義することを目的としています。

以下はPhi-3-miniとその推論機能に関する主要なポイントです：

## **Phi-3-miniの概要:**
- Phi-3-miniのパラメータサイズは38億です。
- 従来のコンピューティングデバイスだけでなく、モバイルデバイスやIoTデバイスなどのエッジデバイスでも実行可能です。
- Phi-3-miniのリリースにより、個人や企業がリソース制約のある環境でさまざまなハードウェアデバイスにSLMを展開できるようになりました。
- 伝統的なPyTorch形式、gguf形式の量子化バージョン、ONNXベースの量子化バージョンなど、さまざまなモデル形式に対応しています。

## **Phi-3-miniへのアクセス:**
Phi-3-miniにアクセスするには、Copilotアプリケーションで[Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)を使用できます。Semantic Kernelは一般的にAzure OpenAI Service、Hugging Faceのオープンソースモデル、ローカルモデルと互換性があります。
また、量子化されたモデルを呼び出すために[Ollama](https://ollama.com)や[LlamaEdge](https://llamaedge.com)を使用することもできます。Ollamaは個人ユーザーがさまざまな量子化モデルを呼び出すことを可能にし、LlamaEdgeはGGUFモデルのクロスプラットフォーム対応を提供します。

## **量子化モデル:**
多くのユーザーはローカル推論のために量子化モデルを使用することを好みます。例えば、Ollama run Phi-3を直接実行するか、Modelfileを使用してオフラインで設定することができます。ModelfileはGGUFファイルパスとプロンプト形式を指定します。

## **生成AIの可能性:**
Phi-3-miniのようなSLMを組み合わせることで、生成AIの新しい可能性が開かれます。推論はその第一歩に過ぎず、これらのモデルはリソース制約、レイテンシ制約、コスト制約のあるシナリオでさまざまなタスクに使用できます。

## **Phi-3-miniで生成AIを解き放つ: 推論と展開のガイド**
Semantic Kernel、Ollama/LlamaEdge、ONNX Runtimeを使用してPhi-3-miniモデルにアクセスし、推論する方法を学び、さまざまなアプリケーションシナリオで生成AIの可能性を探ります。

**特徴**
Phi-3-miniモデルの推論：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

要約すると、Phi-3-miniは開発者がさまざまなモデル形式を探求し、さまざまなアプリケーションシナリオで生成AIを活用することを可能にします。

