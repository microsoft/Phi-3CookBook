**Phi-3 모델을 QLoRA로 미세 조정하기**

Microsoft의 Phi-3 Mini 언어 모델을 [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)을 사용하여 미세 조정합니다.

QLoRA는 대화 이해와 응답 생성 능력을 향상시키는 데 도움을 줍니다.

transformers와 bitsandbytes를 사용하여 모델을 4비트로 로드하려면, 소스에서 accelerate와 transformers를 설치하고 bitsandbytes 라이브러리의 최신 버전을 사용해야 합니다.

**샘플들**
- [이 샘플 노트북에서 더 알아보기](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 미세 조정 샘플 예제](../../../../code/04.Finetuning/FineTrainingScript.py)
- [LORA를 사용한 Hugging Face Hub 미세 조정 예제](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [QLORA를 사용한 Hugging Face Hub 미세 조정 예제](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

