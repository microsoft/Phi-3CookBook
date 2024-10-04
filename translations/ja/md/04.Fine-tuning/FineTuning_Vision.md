# Phi-3.5-vision ファインチューニングレシピ

これは huggingface ライブラリを使用した Phi-3.5-vision ファインチューニングの公式サポートです。
以下のコマンドを実行する前に、コードディレクトリ [vision_finetuning](../../../../code/04.Finetuning/vision_finetuning) に `cd` をしてください。

## インストール

```bash
# create a new conda environment
conda create -n phi3v python=3.10
conda activate phi3v

# install pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# other libraries needed to run the example code
pip install -r requirements.txt

# (optional) flash attention -- Ampere+ GPUs (e.g., A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (optional) QLoRA -- Turing+ GPUs (e.g., RTX 8000)
pip install bitsandbytes==0.43.1
```

## クイックスタート

DocVQA とヘイトフルミーム分類のためのファインチューニングスクリプトを2つ提供しています。

最小ハードウェア要件: 4x RTX8000 (GPUごとに48GB RAM)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision は現在、マルチイメージ入力を公式にサポートしています。NLVR2 のファインチューニングの例を以下に示します。

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 使用ガイド

ハードウェアに応じて、ユーザーは異なるファインチューニング戦略を選択できます。全ファインチューニング（Deepspeed Zero-2 を使用）とオプションで視覚パラメータを凍結する方法、そして LoRA（4bit QLoRA を含む）をサポートしています。一般的には、可能な限りフラッシュアテンションと bf16 を使用した全ファインチューニングを推奨します。

### カスタムデータセットを必要な形式に変換するためのガイド

カスタムデータセットを必要な形式に変換し、Phi-3.5-vision をファインチューニングする方法を示すために、最小限のビデオ分類データセット（UCF-101 のサブセット）をエンドツーエンドの例として使用します。

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

変換されたデータは以下のようになります：

```bash
> tree --filelimit=10 /path/to/converted_ucf101
/path/to/converted_ucf101
├── images
│   ├── test
│   │   ├── ApplyEyeMakeup [48 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [32 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [56 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [72 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [32 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [72 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [80 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [88 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [48 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [72 entries exceeds filelimit, not opening dir]
│   ├── train
│   │   ├── ApplyEyeMakeup [240 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [240 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [240 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [240 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [240 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [240 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [240 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [240 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [240 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [240 entries exceeds filelimit, not opening dir]
│   └── val
│       ├── ApplyEyeMakeup [24 entries exceeds filelimit, not opening dir]
│       ├── ApplyLipstick [24 entries exceeds filelimit, not opening dir]
│       ├── Archery [24 entries exceeds filelimit, not opening dir]
│       ├── BabyCrawling [24 entries exceeds filelimit, not opening dir]
│       ├── BalanceBeam [24 entries exceeds filelimit, not opening dir]
│       ├── BandMarching [24 entries exceeds filelimit, not opening dir]
│       ├── BaseballPitch [24 entries exceeds filelimit, not opening dir]
│       ├── Basketball [24 entries exceeds filelimit, not opening dir]
│       ├── BasketballDunk [24 entries exceeds filelimit, not opening dir]
│       └── BenchPress [24 entries exceeds filelimit, not opening dir]
├── ucf101_test.jsonl
├── ucf101_train.jsonl
└── ucf101_val.jsonl

34 directories, 3 files
```

`jsonl` アノテーションでは、各行は以下のような辞書である必要があります：

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

`conversations` はリストであるため、そのようなデータが利用可能であればマルチターン会話をサポートできます。

## Azure GPU クォータのリクエスト

### 前提条件

Contributor ロール（または Contributor アクセスを含む他のロール）を持つ Azure アカウント。

Azure アカウントを持っていない場合は、[開始する前に無料アカウントを作成](https://azure.microsoft.com)してください。

### クォータ増加のリクエスト

My quotas から直接クォータ増加のリクエストを提出できます。以下の手順に従って、クォータの増加をリクエストしてください。この例では、サブスクリプション内の任意の調整可能なクォータを選択できます。

[Azure ポータル](https://portal.azure.com)にサインインします。

検索ボックスに「quotas」と入力し、Quotas を選択します。
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

概要ページで、Compute や AML などのプロバイダーを選択します。

**Note** Compute 以外のすべてのプロバイダーでは、以下で説明する Adjustable 列の代わりに Request increase 列が表示されます。そこでは、特定のクォータの増加をリクエストするか、増加のサポートリクエストを作成できます。

My quotas ページで、クォータ名の下にある増加したいクォータを選択します。このクォータの Adjustable 列が Yes であることを確認してください。

ページの上部近くで New Quota Request を選択し、Enter a new limit を選択します。

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request パネルで、新しいクォータ制限の数値を入力し、Submit を選択します。

リクエストがレビューされ、リクエストが満たされるかどうかが通知されます。通常、数分以内に行われます。

リクエストが満たされない場合は、サポートリクエストを作成するリンクが表示されます。このリンクを使用すると、サポートエンジニアが増加リクエストを支援します。

## Azure Compute GPU マシン SKU の提案

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

以下は例です：

### A100 または H100 GPU をお持ちの場合

完全なファインチューニングが通常最高のパフォーマンスを発揮します。以下のコマンドを使用して、ヘイトフルミーム分類に Phi-3-V をファインチューニングできます。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Standard_ND40rs_v2 8x V100-32GB GPU をお持ちの場合

ヘイトフルミーム分類に Phi-3-V を完全にファインチューニングすることも可能です。ただし、フラッシュアテンションサポートの欠如により、A100 や H100 GPU と比べてスループットが大幅に低下することが予想されます。bf16 サポートがないため、精度にも影響が出る可能性があります（代わりに fp16 混合精度トレーニングが使用されます）。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### データセンター GPU へのアクセスがない場合

Lora が唯一の選択肢かもしれません。以下のコマンドを使用して、ヘイトフルミーム分類に Phi-3-V をファインチューニングできます。

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU では QLoRA がサポートされています

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## 推奨ハイパーパラメータと期待される精度
### NLVR2

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_nlvr2.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

トレーニング方法 | 凍結ビジョンモデル | データタイプ | LoRA ランク | LoRA アルファ | バッチサイズ | 学習率 | エポック | 精度
--- | --- | --- | --- | --- | --- | --- | --- | --- |
全ファインチューニング |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
全ファインチューニング | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA 結果は近日公開 |  |  |  |  |  |  |  |  |

### 注意
以下の DocVQA とヘイトフルミームの結果は、以前のバージョン（Phi-3-vision）に基づいています。
Phi-3.5-vision での新しい結果は近日中に更新されます。

### DocVQA（注意：Phi-3-vision）

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_docvqa.py \
  --full_train \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

トレーニング方法 | データタイプ | LoRA ランク | LoRA アルファ | バッチサイズ | 学習率 | エポック | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
全ファインチューニング | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
全ファインチューニング | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
凍結画像モデル | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
凍結画像モデル | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### ヘイトフルミーム（注意：Phi-3-vision）

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

トレーニング方法 | データタイプ | LoRA ランク | LoRA アルファ | バッチサイズ | 学習率 | エポック | 精度
--- | --- | --- | --- | --- | --- | --- | --- |
全ファインチューニング | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
全ファインチューニング | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
凍結画像モデル | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
凍結画像モデル | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## スピードベンチマーキング（注意：Phi-3-vision）

Phi-3.5-vision の新しいベンチマーキング結果は近日中に更新されます。

スピードベンチマーキングは DocVQA データセットで実施されます。このデータセットの平均シーケンス長は 2443.23 トークンです（画像モデルに `num_crops=16` を使用）。

### 8x A100-80GB (Ampere)

トレーニング方法 | ノード数 | GPU | フラッシュアテンション | 有効バッチサイズ | スループット (img/s) | スピードアップ | ピーク GPU メモリ (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
全ファインチューニング | 1 | 8 |  | 64 | 5.041 |  1x | ~42
全ファインチューニング | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
全ファインチューニング | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
全ファインチューニング | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
凍結画像モデル | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
凍結画像モデル | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

トレーニング方法 | ノード数 | GPU | フラッシュアテンション | 有効バッチサイズ | スループット (img/s) | スピードアップ | ピーク GPU メモリ (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
全ファインチューニング | 1 | 8 | | 64 | 2.462 |  1x | ~32
全ファインチューニング | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
全ファインチューニング | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
凍結画像モデル | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## 既知の問題

- fp16 ではフラッシュアテンションを実行できません（bf16 が利用可能な場合は常に推奨され、フラッシュアテンションをサポートするすべての GPU も bf16 をサポートしています）。
- 中間チェックポイントの保存とトレーニングの再開をまだサポートしていません。

**免責事項**:
この文書は機械翻訳AIサービスを使用して翻訳されています。正確さを期しておりますが、自動翻訳には誤りや不正確さが含まれる場合があります。原文の言語で書かれた元の文書を信頼できる情報源としてください。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や誤認については責任を負いかねます。