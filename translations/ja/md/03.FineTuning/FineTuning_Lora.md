# **Phi-3をLoRAでファインチューニングする方法**

MicrosoftのPhi-3 Mini言語モデルをカスタムチャット指示データセットを使用して[LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo)でファインチューニングします。

LoRAを使用することで、会話の理解と応答生成を向上させることができます。

## Phi-3 Miniをファインチューニングするためのステップバイステップガイド:

**インポートとセットアップ**

loralibのインストール

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

必要なライブラリ（datasets、transformers、peft、trl、torchなど）をインポートするところから始めます。  
トレーニングプロセスを追跡するためにログ設定を行います。

一部のレイヤーをloraライブラリで実装された対応レイヤーに置き換えて適応させることができます。現在、nn.Linear、nn.Embedding、nn.Conv2dのみをサポートしています。また、1つのnn.Linearが複数のレイヤーを表すケース（例えば、アテンションのqkvプロジェクションの一部の実装）では、MergedLinearもサポートしています（詳細は追加の注意事項を参照してください）。

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

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

load_state_dictを使用してチェックポイントをロードする際には、strict=Falseを設定することを忘れないでください。

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

これで通常通りトレーニングを進めることができます。

**ハイパーパラメータ**

training_configとpeft_configという2つの辞書を定義します。  
training_configには学習率、バッチサイズ、ログ設定などのトレーニング用のハイパーパラメータが含まれます。

peft_configでは、ランク、ドロップアウト、タスクタイプなど、LoRA関連のパラメータを指定します。

**モデルとトークナイザの読み込み**

事前学習済みPhi-3モデルのパスを指定します（例: "microsoft/Phi-3-mini-4k-instruct"）。  
キャッシュ使用、データ型（混合精度用のbfloat16）、アテンションの実装方法など、モデル設定を構成します。

**トレーニング**

カスタムチャット指示データセットを使用してPhi-3モデルをファインチューニングします。  
peft_configからのLoRA設定を活用して効率的に適応させます。  
指定されたログ戦略を使用してトレーニングの進行状況を監視します。

**評価と保存**  
ファインチューニングしたモデルを評価します。  
後で使用できるようにトレーニング中にチェックポイントを保存します。

**サンプル**
- [このサンプルノートブックでさらに学ぶ](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Pythonファインチューニングサンプルの例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face HubでLoRAを使ったファインチューニングの例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Faceモデルカードの例 - LoRAファインチューニングサンプル](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face HubでQLORAを使ったファインチューニングの例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で作成された原文が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は一切の責任を負いません。