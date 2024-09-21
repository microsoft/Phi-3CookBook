# Phi-3.5-vision ファインチューニングレシピ

これは、huggingfaceライブラリを使用したPhi-3.5-visionファインチューニングの公式サポートです。
以下のコマンドを実行する前に、コードディレクトリ [vision_finetuning](../../../../../../../../code/04.Finetuning/vision_finetuning) に `cd` してください。

## インストール

```bash
# 新しいconda環境を作成
conda create -n phi3v python=3.10
conda activate phi3v

# pytorchをインストール
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# サンプルコードを実行するために必要なその他のライブラリ
pip install -r requirements.txt

# (オプション) flash attention -- Ampere+ GPUs (例: A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (オプション) QLoRA -- Turing+ GPUs (例: RTX 8000)
pip install bitsandbytes==0.43.1
```

## クイックスタート

DocVQA用とヘイトフルミーム分類用の2つのファインチューニングスクリプトの例を提供します。

最小ハードウェア：4x RTX8000 (GPUあたり48GB RAM)
```bash
# DocVQAのミニトレイン分割での最小スクリプト
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-visionは現在、複数の画像入力を公式にサポートしています。NLVR2のファインチューニング例はこちらです。
```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 使用ガイド
ハードウェアに応じて、ユーザーは異なるファインチューニング戦略を選択できます。フルファインチューニング（Deepspeed Zero-2を使用）と、視覚パラメータをオプションで凍結する方法、およびLoRA（4bit QLoRAを含む）をサポートしています。一般的には、可能な限りflash attentionとbf16を使用したフルファインチューニングを推奨します。

### カスタムデータセットを必要な形式に変換するためのガイド

最小のビデオ分類データセット（UCF-101のサブセット）を使用して、カスタムデータセットを必要な形式に変換し、Phi-3.5-visionでファインチューニングする方法をエンドツーエンドで示します。

```bash
# データを変換
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# トレーニング
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

変換されたデータは次のようになります:
```
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

`jsonl` アノテーションでは、各行が次のような辞書である必要があります:
```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

`conversations` はリストであるため、そのようなデータが利用可能であれば、マルチターンの会話もサポートされます。

## Azure GPUクォータのリクエスト

### 前提条件
Contributorロール（またはContributorアクセスを含む他のロール）を持つAzureアカウント。

Azureアカウントをお持ちでない場合は、[こちらで無料アカウントを作成](https://azure.microsoft.com)してください。

### クォータ増加のリクエスト
クォータの増加リクエストは、My quotasから直接提出できます。以下の手順に従って、クォータの増加をリクエストしてください。この例では、サブスクリプション内の任意の調整可能なクォータを選択できます。

[Azureポータル](https://portal.azure.com)にサインインします。

検索ボックスに「quotas」と入力し、Quotasを選択します。
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

概要ページで、ComputeやAMLなどのプロバイダーを選択します。

**Note** Compute以外のすべてのプロバイダーでは、以下で説明する調整可能な列の代わりにRequest increase列が表示されます。ここで、特定のクォータの増加をリクエストするか、増加のためのサポートリクエストを作成できます。

My quotasページで、Quota nameの下にある増加したいクォータを選択します。このクォータが調整可能であることを確認してください。

ページの上部近くにあるNew Quota Requestを選択し、次にEnter a new limitを選択します。

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Requestパネルで、新しいクォータ制限の数値を入力し、Submitを選択します。

リクエストが審査され、リクエストが実行可能かどうか通知されます。通常、これは数分以内に行われます。

リクエストが実行されない場合、サポートリクエストを作成するリンクが表示されます。このリンクを使用すると、サポートエンジニアが増加リクエストの支援を行います。

## Azure Compute GPUマシンSKUの提案

[ND A100 v4シリーズ](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5シリーズ](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

以下にいくつかの例を示します：

### A100またはH100 GPUをお持ちの場合
フルファインチューニングが通常、最良のパフォーマンスを提供します。以下のコマンドを使用して、ヘイトフルミーム分類でPhi-3-Vをファインチューニングできます。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Standard_ND40rs_v2 8x V100-32GB GPUをお持ちの場合
ヘイトフルミーム分類でPhi-3-Vを完全にファインチューニングすることはまだ可能です。ただし、flash attentionサポートの欠如により、A100またはH100 GPUに比べてスループットが大幅に低下することが予想されます。
bf16サポートの欠如（代わりにfp16混合精度トレーニングが使用される）により、精度も影響を受ける可能性があります。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### データセンターGPUにアクセスできない場合
Loraが唯一の選択肢かもしれません。以下のコマンドを使用して、ヘイトフルミーム分類でPhi-3-Vをファインチューニングできます。

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

トレーニング方法 | 凍結視覚モデル | データタイプ | LoRAランク | LoRAアルファ | バッチサイズ | 学習率 | エポック数 | 精度
--- | --- | --- | --- | --- | --- | --- | --- | --- |
フルファインチューニング |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
フルファインチューニング | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRAの結果は近日公開 |  |  |  |  |  |  |  |  |

### NOTE
以下のDocVQAおよびヘイトフルミームの結果は、以前のバージョン（Phi-3-vision）に基づいています。
Phi-3.5-visionの新しい結果は近日中に更新されます。

### DocVQA (NOTE: Phi-3-vision)
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
凍結画像モデル | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
凍結画像モデル | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### ヘイトフルミーム (NOTE: Phi-3-vision)
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

| 1x | ~42 full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36 full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29 full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26 frozen image model | 1 | 8 | | 64 | 17.578 | 3.49x | ~29 frozen image model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27 LoRA | 1 | 8 | | 64 | 5.591 | 1.11x | ~50 LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16 QLoRA | 1 | 8 | | 64 | 4.831 | 0.96x | ~32 QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10 ### 8x V100-32GB (Volta) トレーニング方法 | \# ノード | GPUs | フラッシュアテンション | 有効バッチサイズ | スループット (img/s) | スピードアップ | ピークGPUメモリ (GB) --- | --- | --- | --- | --- | --- | --- | --- | full-finetuning | 1 | 8 | | 64 | 2.462 | 1x | ~32 full-finetuning | 2 | 16 | | 64 | 4.182 | 1.70x | ~32 full-finetuning | 4 | 32 | | 64 | 5.465 | 2.22x | ~32 frozen image model | 1 | 8 | | 64 | 8.942 | 3.63x | ~27 LoRA | 1 | 8 | | 64 | 2.807 | 1.14x | ~30 ## 既知の問題 - fp16でフラッシュアテンションを実行できません（bf16が利用可能な場合は常に推奨され、フラッシュアテンションをサポートするすべてのGPUはbf16もサポートしています）。 - 中間チェックポイントの保存とトレーニングの再開をまだサポートしていません。

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。 出力を確認し、必要な修正を行ってください。