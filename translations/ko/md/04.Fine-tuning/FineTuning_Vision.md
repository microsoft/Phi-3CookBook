# Phi-3.5-vision 파인튜닝 레시피

이 문서는 huggingface 라이브러리를 사용한 Phi-3.5-vision 파인튜닝에 대한 공식 지원 문서입니다.
다음 명령어를 실행하기 전에 코드 디렉토리 [vision_finetuning](../../../../code/04.Finetuning/vision_finetuning)로 이동하세요.

## 설치

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

## 빠른 시작

우리는 DocVQA와 혐오성 밈 분류를 위한 두 가지 예제 파인튜닝 스크립트를 제공합니다.

4x RTX8000 (GPU당 48GB RAM)에서 테스트된 최소 하드웨어

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

이제 Phi-3.5-vision은 공식적으로 다중 이미지 입력을 지원합니다. 여기 NLVR2 파인튜닝 예제가 있습니다.

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 사용 가이드

하드웨어에 따라 사용자는 다양한 파인튜닝 전략을 선택할 수 있습니다. 우리는 선택적으로 비전 매개변수를 고정한 상태에서 Deepspeed Zero-2를 사용한 전체 파인튜닝과 LoRA(4bit QLoRA 포함)를 지원합니다. 일반적으로 가능한 경우 플래시 어텐션과 bf16을 사용한 전체 파인튜닝을 권장합니다.

### 사용자 정의 데이터셋을 필요한 형식으로 변환하는 가이드

최소 비디오 분류 데이터셋(UCF-101의 하위 집합)을 사용하여 사용자 정의 데이터셋을 필요한 형식으로 변환하고 Phi-3.5-vision을 파인튜닝하는 방법을 보여주는 종단 간 예제를 제공합니다.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

변환된 데이터는 다음과 같이 보일 것입니다:

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

`jsonl` 주석의 경우, 각 줄은 다음과 같은 사전(dictionary) 형태여야 합니다:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

`conversations`는 리스트 형태이므로, 다중 턴 대화가 가능한 경우 이를 지원할 수 있습니다.

## Azure GPU 할당량 요청

### 사전 요구 사항

기여자 역할(또는 기여자 액세스를 포함하는 다른 역할)이 있는 Azure 계정.

Azure 계정이 없는 경우, [시작하기 전에 무료 계정을 만드세요](https://azure.microsoft.com).

### 할당량 증가 요청

My quotas에서 직접 할당량 증가 요청을 제출할 수 있습니다. 다음 단계를 따라 할당량 증가를 요청하세요. 이 예제에서는 구독에서 조정 가능한 모든 할당량을 선택할 수 있습니다.

[Azure 포털](https://portal.azure.com)에 로그인합니다.

검색 상자에 "quotas"를 입력하고 Quotas를 선택합니다.
![할당량](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

개요 페이지에서 Compute 또는 AML과 같은 공급자를 선택합니다.

**참고** Compute 이외의 모든 공급자에 대해 아래에 설명된 조정 가능한 열 대신 요청 증가 열이 표시됩니다. 여기서 특정 할당량 증가를 요청하거나 증가를 위한 지원 요청을 생성할 수 있습니다.

내 할당량 페이지에서 할당량 이름 아래에서 증가시키려는 할당량을 선택합니다. 이 할당량에 대해 조정 가능한 열이 예라고 표시되는지 확인하세요.

페이지 상단 근처에서 새 할당량 요청을 선택한 다음 새 제한 입력을 선택합니다.

![할당량 증가](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

새 할당량 요청 창에서 새 할당량 한도에 대한 숫자 값을 입력한 다음 제출을 선택합니다.

요청이 검토되며, 요청이 충족 가능한 경우 알림을 받게 됩니다. 일반적으로 몇 분 내에 이루어집니다.

요청이 충족되지 않으면 지원 요청을 생성할 수 있는 링크가 표시됩니다. 이 링크를 사용하면 지원 엔지니어가 증가 요청을 도와줍니다.

## Azure Compute GPU 머신 SKU 제안

[ND A100 v4 시리즈](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5 시리즈](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

다음은 몇 가지 예제입니다:

### A100 또는 H100 GPU가 있는 경우

전체 파인튜닝이 일반적으로 최고의 성능을 제공합니다. 다음 명령어를 사용하여 혐오성 밈 분류에서 Phi-3-V를 파인튜닝할 수 있습니다.

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

여전히 혐오성 밈 분류에서 Phi-3-V를 완전히 파인튜닝할 수 있습니다. 그러나 플래시 어텐션 지원이 없기 때문에 A100 또는 H100 GPU에 비해 처리량이 훨씬 낮을 것으로 예상됩니다.
bf16 지원이 없기 때문에 정확도도 fp16 혼합 정밀도 훈련이 대신 사용되므로 영향을 받을 수 있습니다.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### 데이터 센터 GPU에 접근할 수 없는 경우
Lora가 유일한 선택일 수 있습니다. 다음 명령어를 사용하여 혐오성 밈 분류에서 Phi-3-V를 파인튜닝할 수 있습니다.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU의 경우 QLoRA가 지원됩니다

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## 추천 하이퍼파라미터 및 예상 정확도
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

훈련 방법 | 비전 모델 고정 | 데이터 타입 | LoRA 랭크 | LoRA 알파 | 배치 크기 | 학습률 | 에포크 | 정확도
--- | --- | --- | --- | --- | --- | --- | --- | --- |
전체 파인튜닝 |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
전체 파인튜닝 | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA 결과 곧 업데이트 |  |  |  |  |  |  |  |  |

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

훈련 방법 | 데이터 타입 | LoRA 랭크 | LoRA 알파 | 배치 크기 | 학습률 | 에포크 | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
전체 파인튜닝 | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
전체 파인튜닝 | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
이미지 모델 고정 | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
이미지 모델 고정 | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
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

훈련 방법 | 데이터 타입 | LoRA 랭크 | LoRA 알파 | 배치 크기 | 학습률 | 에포크 | 정확도
--- | --- | --- | --- | --- | --- | --- | --- |
전체 파인튜닝 | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
전체 파인튜닝 | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
이미지 모델 고정 | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
이미지 모델 고정 | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## 속도 벤치마킹 (참고: Phi-3-vision)

Phi-3.5-vision의 새로운 벤치마킹 결과는 곧 업데이트될 예정입니다.

속도 벤치마킹은 DocVQA 데이터셋에서 수행됩니다. 이 데이터셋의 평균 시퀀스 길이는 2443.23 토큰입니다 (`num_crops=16`을 이미지 모델에 사용).

### 8x A100-80GB (Ampere)

훈련 방법 | \# 노드 | GPU | 플래시 어텐션 | 유효 배치 크기 | 처리량 (img/s) | 속도 향상 | 최대 GPU 메모리 (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
전체 파인튜닝 | 1 | 8 |  | 64 | 5.041 |  1x | ~42
전체 파인튜닝 | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
전체 파인튜닝 | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
전체 파인튜닝 | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
이미지 모델 고정 | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
이미지 모델 고정 | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

훈련 방법 | \# 노드 | GPU | 플래시 어텐션 | 유효 배치 크기 | 처리량 (img/s) | 속도 향상 | 최대 GPU 메모리 (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
전체 파인튜닝 | 1 | 8 | | 64 | 2.462 |  1x | ~32
전체 파인튜닝 | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
전체 파인튜닝 | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
이미지 모델 고정 | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## 알려진 문제

- fp16으로 플래시 어텐션을 실행할 수 없습니다 (가능한 경우 항상 bf16을 권장하며, 플래시 어텐션을 지원하는 모든 GPU는 bf16도 지원합니다).
- 중간 체크포인트 저장 및 훈련 재개를 아직 지원하지 않습니다.

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하지만 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원어로 작성된 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우 전문 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.