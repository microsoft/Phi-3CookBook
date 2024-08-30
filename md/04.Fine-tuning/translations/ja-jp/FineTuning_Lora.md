# **LoRAを使用してPhi-3を微調整する**

LoRA（低ランク適応）を使用して、MicrosoftのPhi-3 Mini言語モデルをカスタムチャット指示データセットで微調整します。[LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo)。

LoRAは、会話の理解と応答生成を向上させるのに役立ちます。

## Phi-3 Miniを微調整するためのステップバイステップガイド：

**インポートとセットアップ**

loralibのインストール

```
pip install loralib
# あるいは
# pip install git+https://github.com/microsoft/LoRA
```

まず、datasets、transformers、peft、trl、およびtorchなどの必要なライブラリをインポートします。
トレーニングプロセスを追跡するためにログを設定します。

いくつかのレイヤーをloralibで実装された対応するレイヤーに置き換えることで適応させることができます。現在、nn.Linear、nn.Embedding、およびnn.Conv2dをサポートしています。また、単一のnn.Linearが複数のレイヤーを表す場合に使用されるMergedLinearもサポートしています（詳細については追加の注記を参照してください）。

```
# ===== 以前 =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== 以降 =====
```

loralibをloraとしてインポート

```
# ランクr=16の低ランク適応行列のペアを追加
layer = lora.Linear(in_features, out_features, r=16)
```

トレーニングループが始まる前に、LoRAパラメータのみをトレーニング可能としてマークします。

```
import loralib as lora
model = BigModel()
# これにより、名前に "lora_" が含まれていないすべてのパラメータのrequires_gradがFalseに設定されます
lora.mark_only_lora_as_trainable(model)
# トレーニングループ
for batch in dataloader:
```

チェックポイントを保存する際に、LoRAパラメータのみを含むstate_dictを生成します。

```
# ===== 以前 =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== 以降 =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dictを使用してチェックポイントを読み込む際には、strict=Falseを設定してください。

```
# まず、事前トレーニングされたチェックポイントを読み込みます
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# 次に、LoRAチェックポイントを読み込みます
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

これで、通常通りトレーニングを進めることができます。

**ハイパーパラメータ**

training_configとpeft_configの2つの辞書を定義します。training_configには、学習率、バッチサイズ、ログ設定などのトレーニング用のハイパーパラメータが含まれます。

peft_configには、ランク、ドロップアウト、タスクタイプなどのLoRA関連のパラメータが指定されています。

**モデルとトークナイザーの読み込み**

事前トレーニングされたPhi-3モデルのパスを指定します（例："microsoft/Phi-3-mini-4k-instruct"）。キャッシュの使用、データ型（混合精度用のbfloat16）、および注意実装を含むモデル設定を構成します。

**トレーニング**

カスタムチャット指示データセットを使用してPhi-3モデルを微調整します。効率的な適応のためにpeft_configのLoRA設定を使用します。指定されたログ戦略を使用してトレーニングの進行状況を監視します。
評価と保存：微調整されたモデルを評価します。
後で使用するためにトレーニング中にチェックポイントを保存します。

**サンプル**
- [このサンプルノートブックで詳細を学ぶ](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python微調整サンプルの例](../../../../code/04.Finetuning/FineTrainingScript.py)
- [Hugging Face HubでのLoRAを使用した微調整の例](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Faceモデルカードの例 - LoRA微調整サンプル](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face HubでのQLoRAを使用した微調整の例](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)
