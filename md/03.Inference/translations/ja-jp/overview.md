Phi-3-miniの文脈では、推論とは、モデルを使用して入力データに基づいて予測を行ったり、出力を生成したりするプロセスを指します。Phi-3-miniとその推論機能について詳しく説明します。

Phi-3-miniは、MicrosoftがリリースしたPhi-3シリーズのモデルの一部です。これらのモデルは、小型言語モデル（SLM）の可能性を再定義することを目的としています。

以下は、Phi-3-miniとその推論機能に関するいくつかの重要なポイントです：

## **Phi-3-miniの概要:**
- Phi-3-miniのパラメータサイズは38億です。
- これは、従来のコンピューティングデバイスだけでなく、モバイルデバイスやIoTデバイスなどのエッジデバイスでも動作します。
- Phi-3-miniのリリースにより、個人や企業は、特にリソースが限られた環境で、さまざまなハードウェアデバイスにSLMを展開できるようになりました。
- これには、従来のPyTorch形式、量子化されたgguf形式のバージョン、およびONNXベースの量子化バージョンなど、さまざまなモデル形式が含まれます。

## **Phi-3-miniへのアクセス:**
Phi-3-miniにアクセスするには、Copilotアプリケーションで[Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)を使用できます。Semantic Kernelは、Azure OpenAIサービス、Hugging Faceのオープンソースモデル、およびローカルモデルと一般的に互換性があります。
また、[Ollama](https://ollama.com)や[LlamaEdge](https://llamaedge.com)を使用して量子化モデルを呼び出すこともできます。Ollamaは個々のユーザーが異なる量子化モデルを呼び出すことを可能にし、LlamaEdgeはGGUFモデルのクロスプラットフォームの可用性を提供します。

## **量子化モデル:**
多くのユーザーは、ローカル推論のために量子化モデルを使用することを好みます。たとえば、Ollama run Phi-3を直接実行するか、Modelfileを使用してオフラインで構成できます。Modelfileには、GGUFファイルのパスとプロンプト形式が指定されています。

## **生成AIの可能性:**
Phi-3-miniのようなSLMを組み合わせることで、生成AIの新しい可能性が開かれます。推論は最初のステップに過ぎません。これらのモデルは、リソースが限られた、レイテンシが重要な、コストが制約されたシナリオでさまざまなタスクに使用できます。

## **Phi-3-miniを使用して生成AIを解き放つ：推論とデプロイのガイド**
Semantic Kernel、Ollama/LlamaEdge、およびONNX Runtimeを使用してPhi-3-miniモデルにアクセスし、推論を行い、さまざまなアプリケーションシナリオで生成AIの可能性を探ります。

**特徴**
以下の環境でphi3-miniモデルを推論する：

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

まとめると、Phi-3-miniは、さまざまなモデル形式を探索し、さまざまなアプリケーションシナリオで生成AIを活用するための開発者の可能性を広げます。
