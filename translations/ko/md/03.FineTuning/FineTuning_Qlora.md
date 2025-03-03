**Phi-3를 QLoRA로 미세 조정하기**

Microsoft의 Phi-3 Mini 언어 모델을 [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)을 사용해 미세 조정합니다.

QLoRA는 대화 이해와 응답 생성 능력을 향상시키는 데 도움을 줍니다.

Transformers와 bitsandbytes를 사용하여 모델을 4비트로 로드하려면, accelerate와 transformers를 소스에서 설치하고 bitsandbytes 라이브러리의 최신 버전을 사용해야 합니다.

**샘플**
- [이 샘플 노트북에서 더 알아보기](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 미세 조정 샘플 예제](../../../../code/03.Finetuning/FineTrainingScript.py)
- [LORA를 사용한 Hugging Face Hub 미세 조정 예제](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [QLORA를 사용한 Hugging Face Hub 미세 조정 예제](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원어로 작성된 문서)가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문 번역가에 의한 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.