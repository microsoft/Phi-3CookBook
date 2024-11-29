# **Phi-3를 Lora로 미세 조정하기**

Microsoft의 Phi-3 Mini 언어 모델을 사용자 지정 채팅 지시 데이터 세트를 사용하여 [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo)로 미세 조정하기.

LORA는 대화 이해와 응답 생성 능력을 향상시키는 데 도움을 줄 것입니다.

## Phi-3 Mini를 미세 조정하는 단계별 가이드:

**Imports 및 설정**

loralib 설치

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

필요한 라이브러리 (datasets, transformers, peft, trl, torch 등) 가져오기.
훈련 과정을 추적하기 위해 로깅 설정.

일부 레이어를 loralib로 구현된 대응물로 교체하여 적응할 수 있습니다. 현재 nn.Linear, nn.Embedding, nn.Conv2d만 지원합니다. 또한, 단일 nn.Linear가 여러 레이어를 나타내는 경우(예: 일부 attention qkv projection 구현)에는 MergedLinear도 지원합니다 (추가 노트 참조).

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

훈련 루프가 시작되기 전에 LoRA 매개변수만 훈련 가능하도록 표시합니다.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

체크포인트를 저장할 때, LoRA 매개변수만 포함된 state_dict를 생성합니다.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict를 사용하여 체크포인트를 로드할 때는 strict=False로 설정해야 합니다.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

이제 훈련을 평소처럼 진행할 수 있습니다.

**하이퍼파라미터**

두 개의 딕셔너리: training_config와 peft_config를 정의합니다. training_config는 학습률, 배치 크기, 로깅 설정 등 훈련을 위한 하이퍼파라미터를 포함합니다.

peft_config는 rank, dropout, task type 등 LoRA 관련 매개변수를 지정합니다.

**모델 및 토크나이저 로딩**

사전 훈련된 Phi-3 모델의 경로를 지정합니다 (예: "microsoft/Phi-3-mini-4k-instruct"). 캐시 사용, 데이터 타입 (혼합 정밀도를 위한 bfloat16), attention 구현 등 모델 설정을 구성합니다.

**훈련**

사용자 지정 채팅 지시 데이터 세트를 사용하여 Phi-3 모델을 미세 조정합니다. 효율적인 적응을 위해 peft_config의 LoRA 설정을 활용합니다. 지정된 로깅 전략을 사용하여 훈련 진행 상황을 모니터링합니다.
평가 및 저장: 미세 조정된 모델을 평가합니다.
나중에 사용할 수 있도록 훈련 중에 체크포인트를 저장합니다.

**샘플**
- [이 샘플 노트북으로 더 알아보기](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning 샘플 예제](../../../../code/04.Finetuning/FineTrainingScript.py)
- [LORA를 사용한 Hugging Face Hub 미세 조정 예제](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face 모델 카드 예제 - LORA 미세 조정 샘플](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [QLORA를 사용한 Hugging Face Hub 미세 조정 예제](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 우리는 정확성을 위해 노력하지만 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 오역에 대해 우리는 책임을 지지 않습니다.