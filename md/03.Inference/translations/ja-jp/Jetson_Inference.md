# **Nvidia JetsonでPhi-3を推論する**

Nvidia Jetsonは、Nvidiaの一連の組み込みコンピューティングボードです。Jetson TK1、TX1、およびTX2モデルはすべて、ARMアーキテクチャの中央処理装置（CPU）を統合したNvidiaのTegraプロセッサ（またはSoC）を搭載しています。Jetsonは低消費電力システムであり、機械学習アプリケーションの加速を目的としています。Nvidia Jetsonは、プロの開発者がすべての業界で画期的なAI製品を作成するために使用し、学生や愛好者が実践的なAI学習と驚くべきプロジェクトを作成するために使用します。SLMはJetsonなどのエッジデバイスに展開され、産業生成AIアプリケーションシナリオのより良い実装を可能にします。

## NVIDIA Jetsonでのデプロイ:
自律ロボティクスや組み込みデバイスで作業する開発者は、Phi-3 Miniを活用できます。Phi-3の比較的小さなサイズは、エッジデプロイに理想的です。トレーニング中にパラメータが綿密に調整され、応答の高い精度が保証されています。

### TensorRT-LLM最適化:
NVIDIAの[TensorRT-LLMライブラリ](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo)は、大規模言語モデルの推論を最適化します。Phi-3 Miniの長いコンテキストウィンドウをサポートし、スループットとレイテンシの両方を向上させます。最適化には、LongRoPE、FP8、およびインフライトバッチ処理などの技術が含まれます。

### 可用性とデプロイ:
開発者は、[NVIDIAのAI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/)で128Kコンテキストウィンドウを持つPhi-3 Miniを探索できます。これは、標準APIを備えたマイクロサービスとしてパッケージ化されており、どこにでもデプロイできます。さらに、[GitHubのTensorRT-LLM実装](https://github.com/NVIDIA/TensorRT-LLM)も利用できます。

## **1. 準備**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. JetsonでPhi-3を実行する**

[Ollama](https://ollama.com)または[LlamaEdge](https://llamaedge.com)を選択できます。

クラウドとエッジデバイスで同時にggufを使用したい場合、LlamaEdgeはWasmEdgeとして理解できます（WasmEdgeは、クラウドネイティブ、エッジ、および分散アプリケーションに適した軽量、高性能、スケーラブルなWebAssemblyランタイムです。サーバーレスアプリケーション、埋め込み関数、マイクロサービス、スマートコントラクト、およびIoTデバイスをサポートします。LlamaEdgeを通じて、ggufの量子化モデルをエッジデバイスとクラウドにデプロイできます。

![llamaedge](../../imgs/03/Jetson/llamaedge.jpg)

使用手順は次のとおりです。

1. 関連ライブラリとファイルをインストールしてダウンロードします。

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**注意**: llama-api-server.wasmとchatbot-uiは同じディレクトリに配置する必要があります。

2. ターミナルでスクリプトを実行します。

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

実行結果は次のとおりです。

![llamaedgerun](../../imgs/03/Jetson/llamaedgerun.png)

***サンプルコード*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

まとめると、Phi-3 Miniは、効率、コンテキスト認識、およびNVIDIAの最適化能力を組み合わせた言語モデリングの進歩を表しています。ロボットやエッジアプリケーションを構築する場合でも、Phi-3 Miniは注目すべき強力なツールです。
