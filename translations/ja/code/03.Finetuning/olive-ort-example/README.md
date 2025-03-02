# Oliveを使ってPhi3を微調整する

この例では、Oliveを使用して以下を行います：

1. フレーズを「悲しい」「喜び」「恐れ」「驚き」に分類するためのLoRAアダプターを微調整する。
2. アダプターの重みをベースモデルに統合する。
3. モデルを最適化し、`int4`形式に量子化する。

また、ONNX Runtime (ORT) Generate APIを使用して微調整されたモデルで推論を行う方法も紹介します。

> **⚠️ 微調整には適切なGPUが必要です。例えば、A10、V100、A100などが推奨されます。**

## 💾 インストール

新しいPython仮想環境を作成します（例えば、`conda`を使用）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

次に、Oliveと微調整ワークフロー用の依存関係をインストールします：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Oliveを使ってPhi3を微調整する
[Oliveの設定ファイル](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json)には、以下の*パス*を含む*ワークフロー*が記述されています：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

このワークフローの概要は次のとおりです：

1. [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json)のデータを使用してPhi3を微調整します（150ステップがデフォルトですが、変更可能です）。
2. LoRAアダプターの重みをベースモデルに統合します。これにより、ONNX形式の単一のモデルアーティファクトが生成されます。
3. Model BuilderがモデルをONNX Runtime向けに最適化し、さらにモデルを`int4`形式に量子化します。

ワークフローを実行するには、以下を実行します：

```bash
olive run --config phrase-classification.json
```

Oliveの処理が完了すると、最適化された`int4`形式の微調整されたPhi3モデルが次の場所に保存されます：  
`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`

## 🧑‍💻 微調整されたPhi3をアプリケーションに統合する 

アプリを実行するには：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

この応答は、フレーズの単語分類（悲しい/喜び/恐れ/驚き）のいずれか1つになるはずです。

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを追求していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された原文が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤認に対して、当方は一切の責任を負いません。