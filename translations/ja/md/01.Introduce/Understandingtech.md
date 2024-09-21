# 記載されている主要技術

1. [DirectML](https://learn.microsoft.com/windows/ai/directml/dml?WT.mc_id=aiml-138114-kinfeylo) - DirectX 12の上に構築された、ハードウェアアクセラレーション機械学習用の低レベルAPI。
2. [CUDA](https://blogs.nvidia.com/blog/what-is-cuda-2/) - Nvidiaによって開発された並列コンピューティングプラットフォームおよびAPIモデルで、GPU上での汎用処理を可能にする。
3. [ONNX](https://onnx.ai/) (Open Neural Network Exchange) - 機械学習モデルを表現するために設計されたオープンフォーマットで、異なるMLフレームワーク間の相互運用性を提供する。
4. [GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) (Generic Graph Update Format) - 機械学習モデルの表現と更新に使用されるフォーマットで、特に4-8bitの量子化でCPU上で効果的に動作する小規模な言語モデルに有用。

## DirectML

DirectMLは、ハードウェアアクセラレーション機械学習を可能にする低レベルAPIです。これはDirectX 12の上に構築されており、GPUアクセラレーションを利用し、ベンダーに依存しないため、異なるGPUベンダー間でコードの変更を必要としません。主にGPU上でのモデル訓練と推論のワークロードに使用されます。

ハードウェアサポートについては、DirectMLはAMDの統合およびディスクリートGPU、Intelの統合GPU、NVIDIAのディスクリートGPUなど、幅広いGPUで動作するように設計されています。Windows AIプラットフォームの一部であり、Windows 10および11でサポートされているため、任意のWindowsデバイスでモデル訓練と推論が可能です。

DirectMLに関連する更新や機会として、150以上のONNXオペレーターのサポートや、ONNXランタイムおよびWinMLでの使用などがあります。主要な統合ハードウェアベンダー（IHV）によってバックアップされており、各ベンダーがさまざまなメタコマンドを実装しています。

## CUDA

CUDAはCompute Unified Device Architectureの略で、Nvidiaによって作成された並列コンピューティングプラットフォームおよびAPIモデルです。ソフトウェア開発者がCUDA対応のGPUを汎用処理に使用できるようにするもので、このアプローチはGPGPU（Graphics Processing Units上での汎用コンピューティング）と呼ばれます。CUDAはNvidiaのGPUアクセラレーションの主要なエネーブラーであり、機械学習、科学計算、ビデオ処理などのさまざまな分野で広く使用されています。

CUDAのハードウェアサポートはNvidiaのGPUに特化しており、各アーキテクチャはCUDAツールキットの特定のバージョンをサポートします。ツールキットは開発者がCUDAアプリケーションを構築および実行するために必要なライブラリとツールを提供します。

## ONNX

ONNX (Open Neural Network Exchange) は、機械学習モデルを表現するために設計されたオープンフォーマットです。拡張可能な計算グラフモデルの定義、および組み込みオペレーターと標準データ型の定義を提供します。ONNXは開発者が異なるMLフレームワーク間でモデルを移動できるようにし、相互運用性を実現し、AIアプリケーションの作成と展開を容易にします。

Phi3 miniは、サーバープラットフォーム、Windows、LinuxおよびMacデスクトップ、モバイルCPUを含むデバイスで、CPUおよびGPU上でONNXランタイムを使用して実行できます。
追加された最適化構成は以下の通りです：

- int4 DML用ONNXモデル: AWQを使用してint4に量子化
- fp16 CUDA用ONNXモデル
- int4 CUDA用ONNXモデル: RTNを使用してint4に量子化
- int4 CPUおよびモバイル用ONNXモデル: RTNを使用してint4に量子化

## Llama.cpp

Llama.cppはC++で書かれたオープンソースのソフトウェアライブラリで、Llamaを含むさまざまな大規模言語モデル（LLM）の推論を実行します。ggmlライブラリ（汎用テンソルライブラリ）と共に開発され、元のPython実装と比較してより高速な推論と低メモリ使用を提供することを目指しています。ハードウェア最適化、量子化をサポートし、シンプルなAPIと例を提供します。効率的なLLM推論に興味があるなら、Phi3がLlama.cppを実行できるため、Llama.cppを探る価値があります。

## GGUF

GGUF (Generic Graph Update Format) は、機械学習モデルの表現と更新に使用されるフォーマットです。特に、4-8bitの量子化でCPU上で効果的に動作する小規模な言語モデル（SLM）に有用です。GGUFは迅速なプロトタイピングや、エッジデバイス上でのモデル実行、CI/CDパイプラインのバッチジョブなどに役立ちます。

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない場合があります。
出力を確認し、必要に応じて修正を行ってください。