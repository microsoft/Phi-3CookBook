# **Apple MLX 프레임워크를 사용한 Phi-3 추론**

## **MLX 프레임워크란**

MLX는 Apple 실리콘에서 머신러닝 연구를 위한 배열 프레임워크로, Apple 머신러닝 연구팀이 제공합니다.

MLX는 머신러닝 연구자들이 설계한 프레임워크로, 사용자 친화적이면서도 모델을 효율적으로 학습하고 배포할 수 있도록 설계되었습니다. 프레임워크 자체의 설계도 개념적으로 간단합니다. 연구자들이 새로운 아이디어를 신속하게 탐구할 수 있도록 MLX를 쉽게 확장하고 개선할 수 있도록 하는 것이 목표입니다.

Apple Silicon 장치에서 MLX를 통해 LLMs를 가속할 수 있으며, 모델을 로컬에서 매우 편리하게 실행할 수 있습니다.

## **MLX를 사용하여 Phi-3-mini 추론하기**

### **1. MLX 환경 설정**

1. Python 3.11.x
2. MLX 라이브러리 설치


```bash

pip install mlx-lm

```

### **2. 터미널에서 MLX로 Phi-3-mini 실행하기**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

결과 (내 환경은 Apple M1 Max, 64GB)는

![Terminal](../../../../translated_images/01.5cb5f10f82619d0a98bc3584bf81264105a33d9d8559f125418a93b8d7527728.ko.png)

### **3. 터미널에서 MLX로 Phi-3-mini 양자화하기**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** 모델은 mlx_lm.convert를 통해 양자화할 수 있으며, 기본 양자화는 INT4입니다. 이 예제에서는 Phi-3-mini를 INT4로 양자화합니다.

모델은 mlx_lm.convert를 통해 양자화할 수 있으며, 기본 양자화는 INT4입니다. 이 예제는 Phi-3-mini를 INT4로 양자화하는 것입니다. 양자화 후에는 기본 디렉토리 ./mlx_model에 저장됩니다.

터미널에서 MLX로 양자화된 모델을 테스트할 수 있습니다.


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

결과는

![INT4](../../../../translated_images/02.6ca278966b75435a31021b0a6f1f3b377102d7e59e7b90daf8f017c1a9876cb2.ko.png)


### **4. Jupyter Notebook에서 MLX로 Phi-3-mini 실행하기**


![Notebook](../../../../translated_images/03.5b701d4bfe17c5d20c075f7d4c8d1201b8073c8e8196b364a9a19cbe684dd26a.ko.png)

***Note:*** 이 샘플을 읽어보세요 [click this link](../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **리소스**

1. Apple MLX 프레임워크에 대해 알아보기 [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub 저장소 [https://github.com/ml-explore](https://github.com/ml-explore)

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하지만 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태로 신뢰할 수 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인한 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.