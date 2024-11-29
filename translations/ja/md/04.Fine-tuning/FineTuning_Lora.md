# **LoRAを使用したPhi-3の微調整**

MicrosoftのPhi-3 Mini言語モデルをカスタムチャット指示データセットで[LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo)を使って微調整します。

LORAは会話の理解と応答生成を改善するのに役立ちます。

## Phi-3 Miniを微調整するためのステップバイステップガイド:

**インポートとセットアップ**

loralibのインストール

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

まず、datasets、transformers、peft、trl、torchなどの必要なライブラリをインポートします。
トレーニングプロセスを追跡するためにログを設定します。

いくつかのレイヤーをloraで実装された対応物に置き換えて適応させることができます。現在、nn.Linear、nn.Embedding、nn.Conv2dのみをサポートしています。また、単一のnn.Linearが複数のレイヤーを表す場合（例：アテンションqkvプロジェクションのいくつかの実装）、MergedLinearもサポートしています（詳細は追加ノートを参照）。

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

loralibをloraとしてインポートします。

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

トレーニングループが始まる前に、LoRAパラメータのみをトレーニング可能としてマークします。

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

チェックポイントを保存する際には、LoRAパラメータのみを含むstate_dictを生成します。

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dictを使用してチェックポイントをロードする際には、strict=Falseに設定することを忘れないでください。

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

これで通常通りトレーニングを進めることができます。

**ハイパーパラメータ**

2つの辞書: training_configとpeft_configを定義します。training_configには学習率、バッチサイズ、ログ設定などのトレーニングのためのハイパーパラメータが含まれます。

peft_configにはランク、ドロップアウト、タスクタイプなどのLoRA関連のパラメータが含まれます。

**モデルとトークナイザーの読み込み**

事前学習済みのPhi-3モデル（例："microsoft/Phi-3-mini-4k-instruct"）へのパスを指定します。キャッシュの使用、データタイプ（混合精度のためのbfloat16）、アテンションの実装などのモデル設定を構成します。

**トレーニング**

カスタムチャット指示データセットを使用してPhi-3モデルを微調整します。効率的な適応のためにpeft_configからのLoRA設定を利用します。指定されたログ戦略を使用してトレーニングの進行状況を監視します。
評価と保存: 微調整されたモデルを評価します。
後で使用するためにトレーニング中にチェックポイントを保存します。

**サンプル**
- [このサンプルノートブックで詳細を学ぶ](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python微調整サンプルの例](../../../../code/04.Finetuning/FineTrainingScript.py)
- [LORAを使用したHugging Face Hubの微調整の例](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Faceモデルカードの例 - LORA微調整サンプル](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [QLORAを使用したHugging Face Hubの微調整の例](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責事項**：
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期すよう努めていますが、自動翻訳には誤りや不正確さが含まれる可能性があります。元の言語の文書を権威ある情報源とみなすべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈については、一切の責任を負いかねます。