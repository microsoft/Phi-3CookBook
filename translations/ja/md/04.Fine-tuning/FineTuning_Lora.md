# **Phi-3 を Lora でファインチューニングする方法**

Microsoft の Phi-3 Mini 言語モデルをカスタムチャット指示データセットで [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) を使ってファインチューニングします。

LORA は会話の理解と応答生成を改善するのに役立ちます。

## Phi-3 Mini をファインチューニングするステップバイステップガイド：

**インポートとセットアップ**

loralib のインストール

```
pip install loralib
# または
# pip install git+https://github.com/microsoft/LoRA

```

まず、datasets、transformers、peft、trl、torch などの必要なライブラリをインポートします。
トレーニングプロセスを追跡するためのロギングをセットアップします。

いくつかのレイヤーを loralib で実装された対応部分に置き換えて適応させることができます。現在のところ、nn.Linear、nn.Embedding、および nn.Conv2d のみをサポートしています。また、単一の nn.Linear が複数のレイヤーを表す場合（例：attention qkv projection の一部の実装）に対応する MergedLinear もサポートしています（詳細は Additional Notes を参照）。

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# ランク r=16 の低ランク適応行列のペアを追加
layer = lora.Linear(in_features, out_features, r=16)
```

トレーニングループが始まる前に、LoRA パラメータのみをトレーニング可能としてマークします。

```
import loralib as lora
model = BigModel()
# 名前に "lora_" が含まれていないすべてのパラメータに対して requires_grad を False に設定
lora.mark_only_lora_as_trainable(model)
# トレーニングループ
for batch in dataloader:
```

チェックポイントを保存する際には、LoRA パラメータのみを含む state_dict を生成します。

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict を使用してチェックポイントをロードする際には、strict=False を設定してください。

```
# まず事前学習済みのチェックポイントをロード
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# 次に LoRA チェックポイントをロード
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

これで通常通りにトレーニングを進めることができます。

**ハイパーパラメータ**

training_config と peft_config の 2 つの辞書を定義します。training_config には、学習率、バッチサイズ、ロギング設定などのトレーニング用ハイパーパラメータが含まれます。

peft_config には、ランク、ドロップアウト、タスクタイプなどの LoRA 関連パラメータが指定されます。

**モデルとトークナイザの読み込み**

事前学習済み Phi-3 モデルのパスを指定します（例："microsoft/Phi-3-mini-4k-instruct"）。キャッシュ使用、データタイプ（混合精度用の bfloat16）、およびアテンション実装などのモデル設定を構成します。

**トレーニング**

カスタムチャット指示データセットを使用して Phi-3 モデルをファインチューニングします。効率的な適応のために peft_config の LoRA 設定を利用します。指定されたロギング戦略を使用してトレーニングの進捗を監視します。
評価と保存：ファインチューニングされたモデルを評価します。
後で使用するためにトレーニング中にチェックポイントを保存します。

**サンプル**
- [このサンプルノートブックで詳細を学ぶ](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python ファインチューニングサンプルの例](../../../../code/04.Finetuning/FineTrainingScript.py)
- [LORA を使用した Hugging Face Hub ファインチューニングの例](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face モデルカードの例 - LORA ファインチューニングサンプル](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [QLORA を使用した Hugging Face Hub ファインチューニングの例](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。
出力を確認し、必要な修正を行ってください。