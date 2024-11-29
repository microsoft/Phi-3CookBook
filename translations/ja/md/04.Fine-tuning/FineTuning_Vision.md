# Phi-3.5-vision ファインチューニングレシピ

これは、huggingfaceライブラリを使用したPhi-3.5-visionファインチューニングの公式サポートです。
以下のコマンドを実行する前に、コードディレクトリ[vision_finetuning](../../../../code/04.Finetuning/vision_finetuning)に移動してください。

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

DocVQAと憎悪メーム分類のための2つのファインチューニングスクリプトを提供しています。

最小ハードウェア：4x RTX8000 (各GPUに48GB RAM)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-visionは現在、複数の画像入力を公式にサポートしています。NLVR2のファインチューニングの例はこちらです。

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 使用ガイド

ハードウェアに応じて、ユーザーは異なるファインチューニング戦略を選択できます。全体ファインチューニング（Deepspeed Zero-2を使用）と、オプションでビジョンパラメータを凍結する方法、およびLoRA（4bit QLoRAを含む）をサポートしています。一般的に、可能であればflash attentionとbf16を使用した全体ファインチューニングを推奨します。

### カスタムデータセットを必要な形式に変換するためのガイド

最小のビデオ分類データセット（UCF-101のサブセット）をエンドツーエンドの例として使用し、カスタムデータセットを必要な形式に変換し、Phi-3.5-visionでファインチューニングする方法を示します。

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

変換されたデータは次のようになります：

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

`jsonl`アノテーションでは、各行は次のような辞書である必要があります：

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

`conversations`はリストであるため、データが利用可能であればマルチターン会話をサポートできます。

## Azure GPUクォータのリクエスト

### 前提条件

Contributorロール（またはContributorアクセスを含む他のロール）を持つAzureアカウント。

Azureアカウントを持っていない場合は、[始める前に無料アカウントを作成](https://azure.microsoft.com)してください。

### クォータ増加のリクエスト

My quotasから直接クォータ増加のリクエストを提出できます。以下の手順に従って、クォータの増加をリクエストしてください。この例では、サブスクリプション内の任意の調整可能なクォータを選択できます。

[Azureポータル](https://portal.azure.com)にサインインします。

検索ボックスに「quotas」と入力し、Quotasを選択します。
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

概要ページで、ComputeやAMLなどのプロバイダーを選択します。

**Note** Compute以外のすべてのプロバイダーには、以下で説明する調整可能な列の代わりにリクエスト増加列が表示されます。そこで、特定のクォータの増加をリクエストするか、増加のサポートリクエストを作成できます。

My quotasページで、クォータ名の下にある増加したいクォータを選択します。このクォータの調整可能な列が「Yes」と表示されていることを確認してください。

ページの上部近くにある新しいクォータリクエストを選択し、新しい制限を入力します。

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

新しいクォータリクエストペインで、新しいクォータ制限の数値を入力し、送信を選択します。

リクエストがレビューされ、リクエストが満たされるかどうかが通知されます。通常、数分以内に完了します。

リクエストが満たされない場合は、サポートリクエストを作成するリンクが表示されます。このリンクを使用すると、サポートエンジニアが増加リクエストを支援します。

## Azure Compute GPUマシンSKUの提案

[ND A100 v4シリーズ](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5シリーズ](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

以下は例です：

### A100またはH100 GPUを持っている場合

フルファインチューニングは通常、最高のパフォーマンスを発揮します。以下のコマンドを使用して、憎悪メーム分類でPhi-3-Vをファインチューニングできます。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Standard_ND40rs_v2 8x V100-32GB GPUを持っている場合

憎悪メーム分類でPhi-3-Vをフルファインチューニングすることは依然として可能です。しかし、flash attentionのサポートがないため、A100やH100 GPUと比較してスループットが大幅に低くなります。bf16のサポートがないため（代わりにfp16混合精度トレーニングが使用されます）、精度にも影響が出る可能性があります。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### データセンターGPUにアクセスできない場合

LoRAが唯一の選択肢かもしれません。以下のコマンドを使用して、憎悪メーム分類でPhi-3-Vをファインチューニングできます。

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPUの場合、QLoRAがサポートされています。

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

トレーニング方法 | 凍結されたビジョンモデル | データタイプ | LoRAランク | LoRAアルファ | バッチサイズ | 学習率 | エポック数 | 精度
--- | --- | --- | --- | --- | --- | --- | --- | --- |
フルファインチューニング |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
フルファインチューニング | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRAの結果は近日公開 |  |  |  |  |  |  |  |  |

### 注意
以下のDocVQAと憎悪メームの結果は以前のバージョン（Phi-3-vision）に基づいています。
Phi-3.5-visionの新しい結果は近日中に更新されます。

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

トレーニング方法 | データタイプ | LoRAランク | LoRAアルファ | バッチサイズ | 学習率 | エポック数 | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
フルファインチューニング | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
フルファインチューニング | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
凍結された画像モデル| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
凍結された画像モデル| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### 憎悪メーム（注意：Phi-3-vision）

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

トレーニング方法 | データタイプ | LoRAランク | LoRAアルファ | バッチサイズ | 学習率 | エポック数 | 精度
--- | --- | --- | --- | --- | --- | --- | --- |
フルファインチューニング | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
フルファインチューニング | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
凍結された画像モデル| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
凍結された画像モデル| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## スピードベンチマーキング（注意：Phi-3-vision）

Phi-3.5-visionの新しいベンチマーキング結果は近日中に更新されます。

スピードベンチマーキングはDocVQAデータセットで実施されます。このデータセットの平均シーケンス長は2443.23トークンです（画像モデルには`num_crops=16`を使用）。

### 8x A100-80GB（Ampere）

トレーニング方法 | ノード数 | GPU数 | flash attention | 有効バッチサイズ | スループット（img/s） | スピードアップ | ピークGPUメモリ（GB）
--- | --- | --- | --- | --- | --- | --- | --- |
フルファインチューニング | 1 | 8 |  | 64 | 5.041 |  1x | ~42
フルファインチューニング | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
フルファインチューニング | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
フルファインチューニング | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
凍結された画像モデル | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
凍結された画像モデル | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB（Volta）

トレーニング方法 | ノード数 | GPU数 | flash attention | 有効バッチサイズ | スループット（img/s） | スピードアップ | ピークGPUメモリ（GB）
--- | --- | --- | --- | --- | --- | --- | --- |
フルファインチューニング | 1 | 8 | | 64 | 2.462 |  1x | ~32
フルファインチューニング | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
フルファインチューニング | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
凍結された画像モデル | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## 既知の問題

- fp16でflash attentionを実行できません（flash attentionをサポートするすべてのGPUはbf16もサポートしているため、常にbf16を推奨します）。
- 中間チェックポイントの保存とトレーニングの再開はまだサポートされていません。

**免責事項**:
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を期しておりますが、自動翻訳にはエラーや不正確な点が含まれる可能性があることにご注意ください。権威ある情報源として、元の言語での原文を参照してください。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用により生じた誤解や誤解について、当社は一切の責任を負いません。