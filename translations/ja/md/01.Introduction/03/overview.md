Phi-3-miniの文脈における推論とは、モデルを使用して入力データに基づいて予測を行ったり、出力を生成したりするプロセスを指します。ここでは、Phi-3-miniとその推論機能について詳しく説明します。

Phi-3-miniは、MicrosoftがリリースしたPhi-3シリーズのモデルの一部です。これらのモデルは、小型言語モデル（SLM）の可能性を再定義することを目的としています。

以下に、Phi-3-miniとその推論機能に関する主なポイントを示します。

## **Phi-3-miniの概要:**
- Phi-3-miniのパラメータサイズは38億です。
- 従来のコンピューティングデバイスだけでなく、モバイルデバイスやIoTデバイスなどのエッジデバイスでも動作します。
- Phi-3-miniのリリースにより、個人や企業がリソースが限られた環境でもSLMをさまざまなハードウェアデバイスに展開できるようになりました。
- モデル形式として、従来のPyTorch形式、gguf形式の量子化バージョン、ONNXベースの量子化バージョンなどをサポートしています。

## **Phi-3-miniへのアクセス方法:**
Phi-3-miniにアクセスするには、[Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)をCopilotアプリケーションで使用できます。Semantic Kernelは、Azure OpenAI Service、Hugging Faceのオープンソースモデル、ローカルモデルと一般的に互換性があります。
また、[Ollama](https://ollama.com)や[LlamaEdge](https://llamaedge.com)を使用して量子化モデルを呼び出すことも可能です。Ollamaは個人ユーザーがさまざまな量子化モデルを呼び出すのに適しており、LlamaEdgeはGGUFモデルのクロスプラットフォーム対応を提供します。

## **量子化モデル:**
多くのユーザーは、ローカルでの推論に量子化モデルを使用することを好みます。例えば、Ollamaで直接Phi-3を実行したり、Modelfileを使用してオフラインで構成したりできます。Modelfileには、GGUFファイルのパスやプロンプト形式が指定されています。

## **生成AIの可能性:**
Phi-3-miniのようなSLMを組み合わせることで、生成AIの新たな可能性が広がります。推論はその第一歩にすぎません。これらのモデルは、リソースが限られた環境や低遅延、コスト制約のあるシナリオでさまざまなタスクに活用できます。

## **Phi-3-miniで生成AIを解き放つ: 推論と展開のガイド**
Semantic Kernel、Ollama/LlamaEdge、ONNX Runtimeを使用してPhi-3-miniモデルにアクセスし、推論を行う方法を学び、さまざまなアプリケーションシナリオにおける生成AIの可能性を探りましょう。

**特徴**
Phi-3-miniモデルの推論を以下で実行可能:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

まとめると、Phi-3-miniは、開発者がさまざまなモデル形式を探求し、さまざまなアプリケーションシナリオで生成AIを活用することを可能にします。

**免責事項**:  
本書類は、機械翻訳AIサービスを使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合があります。元の言語による原文が公式な情報源として優先されるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤認に関して、当方は一切の責任を負いかねます。