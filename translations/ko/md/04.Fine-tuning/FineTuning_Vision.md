# Phi-3.5-vision 파인튜닝 레시피

이 문서는 huggingface 라이브러리를 사용한 Phi-3.5-vision 파인튜닝에 대한 공식 지원 문서입니다.
다음 명령어를 실행하기 전에 코드 디렉토리 [vision_finetuning](../../../../../../../../code/04.Finetuning/vision_finetuning)로 이동하세요.

## 설치 방법

```bash
# 새로운 conda 환경 생성
conda create -n phi3v python=3.10
conda activate phi3v

# pytorch 설치
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# 예제 코드를 실행하는 데 필요한 기타 라이브러리 설치
pip install -r requirements.txt

# (선택 사항) flash attention -- Ampere+ GPU (예: A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (선택 사항) QLoRA -- Turing+ GPU (예: RTX 8000)
pip install bitsandbytes==0.43.1
```

## 빠른 시작

DocVQA와 혐오성 밈 분류를 위한 두 가지 예제 파인튜닝 스크립트를 제공합니다.

4x RTX8000 (GPU당 48GB RAM)에서 최소 하드웨어 테스트
```bash
# DocVQA의 미니 트레인 스플릿에 대한 최소 스크립트
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision은 이제 공식적으로 다중 이미지 입력을 지원합니다. NLVR2 파인튜닝 예제입니다.
```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 사용 가이드
하드웨어에 따라 사용자는 다양한 파인튜닝 전략을 선택할 수 있습니다. 우리는 전체 파인튜닝 (옵션으로 비전 매개변수 동결)과 LoRA (4bit QLoRA 포함)를 지원합니다. 일반적으로 가능하면 flash attention과 bf16을 사용한 전체 파인튜닝을 권장합니다.

### 커스텀 데이터셋을 필요한 형식으로 변환하는 가이드

최소 비디오 분류 데이터셋(UCF-101의 하위 집합)을 사용하여 커스텀 데이터셋을 필요한 형식으로 변환하고 Phi-3.5-vision을 파인튜닝하는 방법을 단계별로 설명합니다.

```bash
# 데이터 변환
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# 훈련
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

변환된 데이터는 다음과 같습니다:
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

`jsonl` 주석의 각 줄은 다음과 같은 사전이어야 합니다:
```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

`conversations`는 리스트이므로, 다중 회전 대화도 지원 가능합니다.

## Azure GPU 할당량 요청

### 사전 준비
Contributor 역할(또는 Contributor 액세스가 포함된 다른 역할)이 있는 Azure 계정이 필요합니다.

Azure 계정이 없는 경우, 시작하기 전에 [무료 계정 생성](https://azure.microsoft.com)하세요.

### 할당량 증가 요청
할당량 증가는 My quotas에서 직접 요청할 수 있습니다. 아래 단계를 따라 할당량 증대를 요청하세요. 이 예제에서는 구독 내에서 조정 가능한 모든 할당량을 선택할 수 있습니다.

[Azure 포털](https://portal.azure.com)에 로그인하세요.

검색 상자에 "quotas"를 입력하고, Quotas를 선택합니다.
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

개요 페이지에서 Compute 또는 AML과 같은 공급자를 선택합니다.

**참고** Compute 이외의 모든 공급자에 대해서는 아래 설명된 조정 가능한 열 대신 요청 증가 열을 볼 수 있습니다. 여기에서 특정 할당량에 대한 증대를 요청하거나, 증대를 위한 지원 요청을 생성할 수 있습니다.

My quotas 페이지에서, Quota name 아래에 있는 증가하고 싶은 할당량을 선택합니다. 이 할당량에 대해 조정 가능 열이 "Yes"인지 확인하세요.

페이지 상단 근처에서 New Quota Request를 선택한 다음, Enter a new limit를 선택합니다.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request 창에서 새로운 할당량 한도를 입력한 다음, Submit을 선택합니다.

요청이 검토되며, 요청이 승인될 수 있는 경우 알림을 받게 됩니다. 일반적으로 몇 분 이내에 발생합니다.

요청이 승인되지 않는 경우, 지원 요청을 생성할 수 있는 링크가 표시됩니다. 이 링크를 사용하면 지원 엔지니어가 증가 요청을 도와줄 것입니다.

## Azure Compute GPU 머신 SKU 제안

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

다음은 몇 가지 예제입니다:

### A100 또는 H100 GPU가 있는 경우
전체 파인튜닝이 일반적으로 최고의 성능을 제공합니다. 다음 명령어를 사용하여 혐오성 밈 분류에 Phi-3-V를 파인튜닝할 수 있습니다.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Standard_ND40rs_v2 8x V100-32GB GPU가 있는 경우
여전히 혐오성 밈 분류에 Phi-3-V를 완전히 파인튜닝할 수 있습니다. 그러나 flash attention 지원 부족으로 인해 A100 또는 H100 GPU에 비해 훨씬 낮은 처리량을 기대해야 합니다. 또한 bf16 지원 부족으로 인해 정확도도 영향을 받을 수 있습니다(fp16 혼합 정밀도 훈련이 대신 사용됨).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### 데이터 센터 GPU에 접근할 수 없는 경우
Lora가 유일한 선택일 수 있습니다. 다음 명령어를 사용하여 혐오성 밈 분류에 Phi-3-V를 파인튜닝할 수 있습니다.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU의 경우, QLoRA를 지원합니다.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## 제안된 하이퍼파라미터 및 예상 정확도
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

훈련 방법 | 비전 모델 동결 | 데이터 타입 | LoRA 랭크 | LoRA 알파 | 배치 사이즈 | 학습률 | 에포크 | 정확도
--- | --- | --- | --- | --- | --- | --- | --- | --- |
전체 파인튜닝 |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
전체 파인튜닝 | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA 결과 곧 공개 |  |  |  |  |  |  |  |  |

### 참고
아래 DocVQA와 혐오성 밈 결과는 이전 버전(Phi-3-vision)을 기반으로 합니다.
Phi-3.5-vision의 새로운 결과는 곧 업데이트될 예정입니다.

### DocVQA (참고: Phi-3-vision)
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

훈련 방법 | 데이터 타입 | LoRA 랭크 | LoRA 알파 | 배치 사이즈 | 학습률 | 에포크 | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
전체 파인튜닝 | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
전체 파인튜닝 | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
비전 모델 동결 | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
비전 모델 동결 | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### 혐오성 밈 (참고: Phi-3-vision)
```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>
```

훈련 방법 | 데이터 타입 | LoRA 랭크 | LoRA 알파 | 배치 사이즈 | 학습률 | 에포크 | 정확도
--- | --- | --- | --- | --- | --- | --- | --- |
전체 파인튜닝 | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
전체 파인튜닝 | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
비전 모델 동결 | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
비전 모델 동결 | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## 속도 벤치마킹 (참고: Phi-3-vision)
Phi-3.5-vision의 새로운 벤치마킹 결과는 곧 업데이트될 예정입니다.
속도 벤치마킹은 DocVQA 데이터셋에서 수행되었습니다. 이 데이터셋의 평균 시퀀스 길이는 2443.23 토큰입니다 (`num_crops=16`을 이미지 모델에 사용).

### 8x A100-80GB (Ampere)
훈련 방법 | \# 노드 | GPU | flash attention | 유효 배치 사이즈 | 처리량 (img/s) |
| 1x | ~42 full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36 full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29 full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26 frozen image model | 1 | 8 | | 64 | 17.578 | 3.49x | ~29 frozen image model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27 LoRA | 1 | 8 | | 64 | 5.591 | 1.11x | ~50 LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16 QLoRA | 1 | 8 | | 64 | 4.831 | 0.96x | ~32 QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10 ### 8x V100-32GB (Volta) Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB) --- | --- | --- | --- | --- | --- | --- | --- | full-finetuning | 1 | 8 | | 64 | 2.462 | 1x | ~32 full-finetuning | 2 | 16 | | 64 | 4.182 | 1.70x | ~32 full-finetuning | 4 | 32 | | 64 | 5.465 | 2.22x | ~32 frozen image model | 1 | 8 | | 64 | 8.942 | 3.63x | ~27 LoRA | 1 | 8 | | 64 | 2.807 | 1.14x | ~30 ## Known issues - Cannot run flash attention with fp16 (bf16 is always recommended when available, and all GPUs supporting flash attention also support bf16). - Do not support saving intermediate checkpoints and resuming training yet.

면책 조항: 이 번역은 AI 모델에 의해 원본에서 번역된 것이며 완벽하지 않을 수 있습니다. 
출력을 검토하고 필요한 수정 사항을 반영해 주시기 바랍니다.