# Oliveを使用してPhi3をファインチューニングする

この例では、Oliveを使用して以下を行います：

1. フレーズをSad, Joy, Fear, Surpriseに分類するためのLoRAアダプターをファインチューニングする。
1. アダプターの重みをベースモデルにマージする。
1. モデルを最適化し、`int4`に量子化する。

また、ONNX Runtime (ORT) Generate APIを使用してファインチューニングされたモデルを推論する方法も紹介します。

> **⚠️ ファインチューニングには、適切なGPU（例：A10、V100、A100）が必要です。**

## 💾 インストール

新しいPython仮想環境を作成します（例えば、`conda`を使用して）：

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

## 🧪 Oliveを使用してPhi3をファインチューニングする
[Olive設定ファイル](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json)には、以下の*パス*を含む*ワークフロー*が含まれています：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

このワークフローは高レベルでは以下を行います：

1. [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)データを使用してPhi3をファインチューニングします（150ステップ、変更可能）。
1. LoRAアダプターの重みをベースモデルにマージします。これにより、ONNX形式の単一モデルアーティファクトが得られます。
1. Model BuilderがモデルをONNXランタイム用に最適化し、`int4`に量子化します。

ワークフローを実行するには、以下を実行します：

```bash
olive run --config phrase-classification.json
```

Oliveが完了すると、最適化された`int4`ファインチューニングされたPhi3モデルは次の場所にあります：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 ファインチューニングされたPhi3をアプリケーションに統合する

アプリを実行するには：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

この応答はフレーズの単語分類（Sad/Joy/Fear/Surprise）であるべきです。

**免責事項**:
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確さが含まれる場合があります。元の言語の原文を権威ある情報源と見なしてください。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用による誤解や誤訳について、当社は一切の責任を負いません。