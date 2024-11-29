# **Nvidia Jetson での Phi-3 推論**

Nvidia Jetson は、Nvidia から提供されている組み込みコンピューティングボードのシリーズです。Jetson TK1、TX1、および TX2 モデルはすべて、ARM アーキテクチャの中央処理装置 (CPU) を統合した Nvidia の Tegra プロセッサ (または SoC) を搭載しています。Jetson は低消費電力システムであり、機械学習アプリケーションの加速を目的としています。Nvidia Jetson は、すべての業界で革新的な AI 製品を作成するためにプロの開発者によって使用されており、学生や愛好者が実践的な AI 学習を行い、素晴らしいプロジェクトを作成するために使用されています。SLM は Jetson などのエッジデバイスに展開され、産業用生成 AI アプリケーションシナリオのより良い実装を可能にします。

## NVIDIA Jetson へのデプロイ:
自律ロボットや組み込みデバイスに取り組んでいる開発者は Phi-3 Mini を活用できます。Phi-3 の比較的小さなサイズはエッジデプロイメントに理想的です。トレーニング中にパラメータが慎重に調整されており、高い応答精度が確保されています。

### TensorRT-LLM 最適化:
NVIDIA の [TensorRT-LLM ライブラリ](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) は、大規模言語モデルの推論を最適化します。Phi-3 Mini の長いコンテキストウィンドウをサポートし、スループットとレイテンシーの両方を向上させます。最適化には LongRoPE、FP8、インフライトバッチングなどの技術が含まれます。

### 利用可能性とデプロイメント:
開発者は [NVIDIA's AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/) で 128K コンテキストウィンドウを持つ Phi-3 Mini を探索できます。これは標準 API を備えたマイクロサービスとしてパッケージ化され、どこにでもデプロイ可能です。また、[GitHub 上の TensorRT-LLM 実装](https://github.com/NVIDIA/TensorRT-LLM) も参照できます。

## **1. 準備**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+
   
c. Cuda 11.8
   
d. Python 3.8+

## **2. Jetson で Phi-3 を実行**

[Ollama](https://ollama.com) または [LlamaEdge](https://llamaedge.com) を選択できます。

クラウドとエッジデバイスで同時に gguf を使用したい場合、LlamaEdge は WasmEdge として理解できます（WasmEdge は軽量で高性能なスケーラブルな WebAssembly ランタイムで、クラウドネイティブ、エッジ、および分散アプリケーションに適しています。サーバーレスアプリケーション、組み込み関数、マイクロサービス、スマートコントラクト、IoT デバイスをサポートします。LlamaEdge を通じて gguf の定量モデルをエッジデバイスおよびクラウドにデプロイできます。

![llamaedge](../../../../translated_images/llamaedge.d1314f30755868575f55e27125fdd9838b6962e3bce66c9bd21eaffebfcf57b9.ja.jpg)

使用手順は以下の通りです

1. 関連ライブラリとファイルをインストールおよびダウンロード

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Note**: llama-api-server.wasm と chatbot-ui は同じディレクトリに配置する必要があります

2. ターミナルでスクリプトを実行

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

実行結果は以下の通りです

![llamaedgerun](../../../../translated_images/llamaedgerun.fcb0c81257035c00b2a9ec7d2f541d64f9f357eec4adf45f5c951c4c06cd1df9.ja.png)

***サンプルコード*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

まとめると、Phi-3 Mini は効率性、コンテキスト認識、および NVIDIA の最適化技術を組み合わせた言語モデリングの飛躍的進歩を表しています。ロボットやエッジアプリケーションを構築する際には、Phi-3 Mini は強力なツールとなるでしょう。

**免責事項**:
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期していますが、自動翻訳には誤りや不正確さが含まれる場合がありますのでご注意ください。元の言語の文書を信頼できる情報源とみなすべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤訳について、当社は一切の責任を負いません。