# **llama.cppを使ったPhiファミリーの量子化**

## **llama.cppとは**

llama.cppは、主にC++で書かれたオープンソースのソフトウェアライブラリで、Llamaのようなさまざまな大規模言語モデル（LLM）の推論を行います。このライブラリの主な目的は、最小限のセットアップで幅広いハードウェア上で最先端のLLM推論性能を提供することです。また、このライブラリにはPythonバインディングも用意されており、テキスト補完のための高レベルAPIやOpenAI互換のWebサーバーを提供しています。

llama.cppの主な目的は、ローカルおよびクラウド上で、最小限のセットアップでさまざまなハードウェア上での最先端のLLM推論を可能にすることです。

- 依存関係のない純粋なC/C++実装  
- Appleシリコンを第一級市民としてサポート - ARM NEON、Accelerate、Metalフレームワークを活用して最適化  
- x86アーキテクチャ向けにAVX、AVX2、AVX512をサポート  
- 推論速度向上とメモリ使用量削減のための1.5ビット、2ビット、3ビット、4ビット、5ビット、6ビット、8ビット整数量子化  
- NVIDIA GPUでLLMを動作させるためのカスタムCUDAカーネル（AMD GPUはHIPを介してサポート）  
- VulkanおよびSYCLバックエンドのサポート  
- CPU+GPUのハイブリッド推論で、VRAM容量を超える大規模モデルを部分的に高速化  

## **Phi-3.5の量子化（llama.cppを使用）**

Phi-3.5-Instructモデルはllama.cppを使用して量子化できますが、Phi-3.5-VisionやPhi-3.5-MoEはまだサポートされていません。llama.cppで変換されるフォーマットはggufであり、これは現在最も広く使用されている量子化フォーマットでもあります。

Hugging Faceには多数の量子化されたGGUFフォーマットモデルがあります。AI Foundry、Ollama、LlamaEdgeはllama.cppを利用しているため、GGUFモデルも頻繁に使用されています。

### **GGUFとは**

GGUFは、モデルの高速な読み込みと保存を最適化したバイナリフォーマットであり、推論目的において非常に効率的です。GGUFはGGMLやその他の実行エンジンで使用するために設計されています。GGUFは、llama.cppの開発者である@ggerganovによって開発されました。llama.cppは人気のあるC/C++のLLM推論フレームワークです。PyTorchなどのフレームワークで開発されたモデルは、これらのエンジンで使用するためにGGUFフォーマットに変換できます。

### **ONNXとGGUFの比較**

ONNXは従来の機械学習/深層学習フォーマットであり、さまざまなAIフレームワークで広くサポートされており、エッジデバイスでの利用シナリオに適しています。一方、GGUFはllama.cppをベースとしており、生成AI時代に生まれたものと言えます。この2つは似た用途を持ちますが、組み込みハードウェアやアプリケーション層での性能を重視する場合はONNXが適しているかもしれません。一方、llama.cppの派生フレームワークや技術を使用する場合は、GGUFの方が優れている可能性があります。

### **Phi-3.5-Instructの量子化（llama.cppを使用）**

**1. 環境設定**  

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```  

**2. 量子化**  

llama.cppを使用してPhi-3.5-InstructをFP16 GGUFに変換  


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```  

Phi-3.5をINT4に量子化  


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```  

**3. テスト**  

llama-cpp-pythonをインストール  


```bash

pip install llama-cpp-python -U

```  

***注意***  

Apple Siliconを使用している場合は、以下のようにllama-cpp-pythonをインストールしてください  


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```  

テスト  


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```  

## **リソース**

1. llama.cppについてさらに詳しく知る [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  

2. GGUFについてさらに詳しく知る [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)  

**免責事項**:  
本書類は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があることをご承知おきください。原文（元の言語で記載された文書）が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や誤認について、当社は一切の責任を負いません。