# **Lora를 사용한 Phi-3 미니 모델 미세 조정**

[LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo)을 사용하여 Microsoft의 Phi-3 Mini 언어 모델을 사용자 지정 채팅 지침 데이터셋으로 미세 조정합니다.

LORA는 대화 이해와 응답 생성 능력을 향상시키는 데 도움이 됩니다.

## Phi-3 Mini를 미세 조정하는 단계별 가이드:

**임포트 및 설정**

loralib 설치

```
pip install loralib
# 또는
# pip install git+https://github.com/microsoft/LoRA

```

필요한 라이브러리(datasets, transformers, peft, trl, torch 등)를 임포트하는 것으로 시작합니다.
훈련 과정을 추적하기 위해 로깅을 설정합니다.

일부 레이어를 loralib로 구현된 대응 레이어로 교체하여 조정할 수 있습니다. 현재 nn.Linear, nn.Embedding, nn.Conv2d만 지원합니다. 또한, 단일 nn.Linear가 여러 레이어를 나타내는 경우를 위해 MergedLinear도 지원합니다. (추가 정보는 추가 노트를 참조하세요.)

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# 랭크 r=16인 저랭크 적응 행렬 쌍 추가
layer = lora.Linear(in_features, out_features, r=16)
```

훈련 루프가 시작되기 전에 LoRA 파라미터만 훈련 가능하도록 설정합니다.

```
import loralib as lora
model = BigModel()
# 이름에 "lora_"가 포함되지 않은 모든 파라미터에 대해 requires_grad를 False로 설정합니다.
lora.mark_only_lora_as_trainable(model)
# 훈련 루프
for batch in dataloader:
```

체크포인트를 저장할 때는 LoRA 파라미터만 포함된 state_dict를 생성합니다.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict를 사용하여 체크포인트를 로드할 때 strict=False로 설정하는 것을 잊지 마세요.

```
# 먼저 사전 훈련된 체크포인트를 로드합니다.
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# 그런 다음 LoRA 체크포인트를 로드합니다.
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

이제 평소와 같이 훈련을 진행할 수 있습니다.

**하이퍼파라미터**

training_config와 peft_config 두 개의 딕셔너리를 정의합니다. training_config에는 학습률, 배치 크기, 로깅 설정 등 훈련을 위한 하이퍼파라미터가 포함됩니다.

peft_config는 랭크, 드롭아웃, 작업 유형 등 LoRA 관련 파라미터를 지정합니다.

**모델 및 토크나이저 로딩**

사전 훈련된 Phi-3 모델의 경로를 지정합니다(예: "microsoft/Phi-3-mini-4k-instruct"). 캐시 사용, 데이터 타입(bfloat16 혼합 정밀도), 주의 구현 등 모델 설정을 구성합니다.

**훈련**

사용자 지정 채팅 지침 데이터셋을 사용하여 Phi-3 모델을 미세 조정합니다. peft_config의 LoRA 설정을 활용하여 효율적으로 적응합니다. 지정된 로깅 전략을 사용하여 훈련 진행 상황을 모니터링합니다.
평가 및 저장: 미세 조정된 모델을 평가합니다.
나중에 사용할 수 있도록 훈련 중에 체크포인트를 저장합니다.

**샘플**
- [이 샘플 노트북으로 더 알아보기](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning 샘플 예제](../../../../code/04.Finetuning/FineTrainingScript.py)
- [LORA를 사용한 Hugging Face Hub 미세 조정 예제](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face 모델 카드 예제 - LORA 미세 조정 샘플](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [QLORA를 사용한 Hugging Face Hub 미세 조정 예제](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

면책 조항: 이 번역은 AI 모델에 의해 원본에서 번역되었으며 완벽하지 않을 수 있습니다. 출력물을 검토하고 필요한 수정 사항을 반영해 주세요.