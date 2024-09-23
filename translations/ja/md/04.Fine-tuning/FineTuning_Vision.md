# Phi-3.5-vision ファインチューニングレシピ

これは、huggingfaceライブラリを使用したPhi-3.5-visionのファインチューニングの公式サポートです。以下のコマンドを実行する前に、コードディレクトリ[vision_finetuning](../../../../code/04.Finetuning/vision_finetuning)に`cd`してください。

## インストール

```bash
# 新しいconda環境を作成
conda create -n phi3v python=3.10
conda activate phi3v

# pytorchをインストール
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# サンプルコードを実行するために必要な他のライブラリ
pip install -r requirements.txt

# (オプション) フラッシュアテンション -- Ampere+ GPUs (例: A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (オプション) QLoRA -- Turing+ GPUs (例: RTX 8000)
pip install bitsandbytes==0.43.1
```

## クイックスタート

DocVQAとヘイトフルミーム分類の2つの例を提供しています。

4x RTX8000 (GPUごとに48GB RAM) でテストされた最小ハードウェア
```bash
# DocVQAのミニトレインスプリットでの最小スクリプト
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-visionは現在、複数画像入力を公式にサポートしています。NLVR2のファインチューニング例はこちらです。
```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 使用ガイド
ハードウェアに応じて、ユーザーは異なるファインチューニング戦略を選択できます。全ファインチューニング（Deepspeed Zero-2を使用）と、オプションで視覚パラメータを凍結する方法、LoRA（4bit QLoRAを含む）をサポートしています。一般的には、可能であればフラッシュアテンションとbf16を使用した全ファインチューニングを推奨します。

### カスタムデータセットを必要な形式に変換するためのガイド

カスタムデータセットを必要な形式に変換し、Phi-3.5-visionでファインチューニングする方法を示すために、最小限のビデオ分類データセット（UCF-101のサブセット）をエンドツーエンドの例として使用します。

```bash
# データ変換
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# トレーニング
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

変換されたデータは次のようになります：
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

`jsonl`アノテーションの各行は次のような辞書形式である必要があります：
```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

`conversations`はリストであるため、そのようなデータが利用可能であればマルチターン会話もサポートできます。

## Azure GPU クォータのリクエスト

### 前提条件
Contributorロール（またはContributorアクセスを含む他のロール）を持つAzureアカウント。

Azureアカウントをお持ちでない場合は、[無料アカウントを作成](https://azure.microsoft.com)してください。

### クォータ増加のリクエスト
クォータ増加のリクエストは、My quotasから直接送信できます。以下の手順に従って、クォータの増加をリクエストします。この例では、サブスクリプション内の任意の調整可能なクォータを選択できます。

[Azureポータル](https://portal.azure.com)にサインインします。

検索ボックスに「quotas」と入力し、Quotasを選択します。
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

概要ページで、ComputeやAMLなどのプロバイダーを選択します。

**Note** Compute以外のすべてのプロバイダーについては、Adjustable列の代わりにRequest increase列が表示されます。ここで、特定のクォータの増加をリクエストするか、増加のサポートリクエストを作成できます。

My quotasページで、クォータ名の下にある増加したいクォータを選択します。このクォータが調整可能な場合、Adjustable列に「Yes」と表示されていることを確認してください。

ページの上部近くにあるNew Quota Requestを選択し、Enter a new limitを選択します。

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Requestペインに新しいクォータ制限の数値を入力し、Submitを選択します。

リクエストが審査され、リクエストが実行可能かどうか通知されます。通常、数分以内に通知されます。

リクエストが実行されない場合は、サポートリクエストを作成するリンクが表示されます。このリンクを使用すると、サポートエンジニアが増加リクエストを支援します。

## Azure Compute GPU マシン SKUの提案

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

以下は一部の例です：

### A100またはH100 GPUを持っている場合
フルファインチューニングが通常最も高いパフォーマンスを発揮します。以下のコマンドを使用して、ヘイトフルミーム分類にPhi-3-Vをファインチューニングできます。

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
ヘイトフルミーム分類にPhi-3-Vを完全にファインチューニングすることは依然として可能ですが、フラッシュアテンションのサポートがないため、A100またはH100 GPUに比べてスループットが大幅に低下します。bf16のサポートがないため（代わりにfp16混合精度トレーニングが使用されます）、精度にも影響が出る可能性があります。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### データセンターGPUにアクセスできない場合
Loraが唯一の選択肢かもしれません。以下のコマンドを使用して、ヘイトフルミーム分類にPhi-3-Vをファインチューニングできます。

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

## 推奨ハイパーパラメータと予想精度
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
LoRA結果近日公開 |  |  |  |  |  |  |  |  |

### NOTE
以下のDocVQAとヘイトフルミームの結果は、以前のバージョン（Phi-3-vision）に基づいています。Phi-3.5-visionの新しい結果は近日中に更新されます。

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
凍結されたイメージモデル| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
凍結されたイメージモデル| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
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
凍結されたイ
| 1x | ~42 full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36 full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29 full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26 frozen image model | 1 | 8 | | 64 | 17.578 | 3.49x | ~29 frozen image model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27 LoRA | 1 | 8 | | 64 | 5.591 | 1.11x | ~50 LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16 QLoRA | 1 | 8 | | 64 | 4.831 | 0.96x | ~32 QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10 ### 8x V100-32GB (Volta) トレーニング方法 | \# ノード | GPU | フラッシュアテンション | 有効バッチサイズ | スループット (img/s) | スピードアップ | ピークGPUメモリ (GB) --- | --- | --- | --- | --- | --- | --- | --- | full-finetuning | 1 | 8 | | 64 | 2.462 | 1x | ~32 full-finetuning | 2 | 16 | | 64 | 4.182 | 1.70x | ~32 full-finetuning | 4 | 32 | | 64 | 5.465 | 2.22x | ~32 frozen image model | 1 | 8 | | 64 | 8.942 | 3.63x | ~27 LoRA | 1 | 8 | | 64 | 2.807 | 1.14x | ~30 ## 既知の問題 - fp16でフラッシュアテンションを実行できません（bf16が利用可能な場合は常に推奨され、フラッシュアテンションをサポートするすべてのGPUはbf16もサポートします）。 - 中間チェックポイントの保存とトレーニングの再開はまだサポートされていません。

免責事項: 翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない場合があります。
出力を確認し、必要に応じて修正を加えてください。