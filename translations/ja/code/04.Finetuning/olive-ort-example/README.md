# Oliveを使用したPhi3のファインチューニング

この例では、Oliveを使用して以下を行います：

1. フレーズを「悲しい」「喜び」「恐れ」「驚き」に分類するためのLoRAアダプターをファインチューニングします。
2. アダプターの重みをベースモデルに統合します。
3. モデルを最適化し、`int4`形式に量子化します。

さらに、ONNX Runtime (ORT) のGenerate APIを使用して、ファインチューニングされたモデルを推論する方法も説明します。

> **⚠️ ファインチューニングを行うには、適切なGPU（例: A10, V100, A100）が必要です。**

## 💾 インストール

新しいPython仮想環境を作成します（例えば、`conda`を使用）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

次に、Oliveとファインチューニングワークフローの依存関係をインストールします：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Oliveを使用したPhi3のファインチューニング

[Olive設定ファイル](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json)には、以下の*パス*を含む*ワークフロー*が記述されています：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

このワークフローは以下を行います：

1. [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)データを使用してPhi3をファインチューニングします（150ステップ、変更可能）。
2. LoRAアダプターの重みをベースモデルに統合します。これにより、ONNX形式の単一モデルアーティファクトが生成されます。
3. Model BuilderがモデルをONNX Runtime向けに最適化し、さらに`int4`形式に量子化します。

ワークフローを実行するには、以下を実行します：

```bash
olive run --config phrase-classification.json
```

Oliveの処理が完了すると、最適化された`int4`形式のファインチューニング済みPhi3モデルが次の場所に保存されます：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`

## 🧑‍💻 ファインチューニング済みPhi3をアプリケーションに統合する

アプリを実行するには：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

この応答は、フレーズの分類結果（悲しい/喜び/恐れ/驚き）の単語1つで返されます。

**免責事項**:  
この文書は、AI翻訳サービスを使用して機械的に翻訳されたものです。正確性を期すよう努めておりますが、自動翻訳にはエラーや不正確な部分が含まれる可能性があります。原文（元の言語で記載された文書）が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じる誤解や誤訳について、当社は一切の責任を負いません。