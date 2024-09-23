# Oliveを使ってPhi3をファインチューニングする

この例では、Oliveを使用して以下のことを行います:

1. フレーズをSad, Joy, Fear, Surpriseに分類するためにLoRAアダプタをファインチューニングする。
1. アダプタの重みをベースモデルにマージする。
1. モデルを最適化し、`int4`に量子化する。

また、ONNX Runtime (ORT) Generate APIを使用してファインチューニングされたモデルを推論する方法も紹介します。

> **⚠️ ファインチューニングには、適切なGPUが必要です。例えば、A10, V100, A100などです。**

## 💾 インストール

新しいPython仮想環境を作成します（例えば、`conda`を使用して）:

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

次に、Oliveとファインチューニングワークフローの依存関係をインストールします:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Oliveを使ってPhi3をファインチューニングする
[Olive設定ファイル](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json)には、以下の*パス*を持つ*ワークフロー*が含まれています:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

このワークフローは高レベルでは以下を行います:

1. [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)データを使用して、Phi3を（150ステップで、これは変更可能）ファインチューニングします。
1. LoRAアダプタの重みをベースモデルにマージします。これにより、ONNX形式の単一のモデルアーティファクトが得られます。
1. Model BuilderはモデルをONNXランタイム用に最適化し、`int4`に量子化します。

ワークフローを実行するには、以下を実行します:

```bash
olive run --config phrase-classification.json
```

Oliveが完了すると、最適化された`int4`ファインチューニングされたPhi3モデルが次の場所にあります: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 ファインチューニングされたPhi3をアプリケーションに統合する 

アプリを実行するには:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

この応答は、フレーズの単語分類（Sad/Joy/Fear/Surprise）のいずれかになるはずです。

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。 出力内容を確認し、必要に応じて修正を行ってください。