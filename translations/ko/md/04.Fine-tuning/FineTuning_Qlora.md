**Phi-3을 QLoRA로 미세 조정하기**

Microsoft의 Phi-3 Mini 언어 모델을 [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)를 사용하여 미세 조정합니다.

QLoRA는 대화 이해와 응답 생성 능력을 향상시키는 데 도움이 됩니다.

transformers와 bitsandbytes를 사용하여 4비트 모델을 로드하려면, 소스에서 accelerate와 transformers를 설치하고 최신 버전의 bitsandbytes 라이브러리를 사용해야 합니다.

**샘플**
- [이 샘플 노트북에서 더 알아보기](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 미세 조정 샘플 예제](../../../../code/04.Finetuning/FineTrainingScript.py)
- [LORA를 사용한 Hugging Face Hub 미세 조정 예제](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [QLORA를 사용한 Hugging Face Hub 미세 조정 예제](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 우리는 정확성을 위해 노력하지만 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인한 오해나 오역에 대해 우리는 책임을 지지 않습니다.