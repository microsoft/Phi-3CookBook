# **Apple MLX 프레임워크를 사용한 Phi-3.5 양자화**

MLX는 Apple 실리콘에서 머신 러닝 연구를 위한 배열 프레임워크로, Apple 머신 러닝 연구팀에서 제공합니다.

MLX는 머신 러닝 연구자들을 위해 설계된 프레임워크로, 모델을 효율적으로 학습하고 배포할 수 있으면서도 사용이 간편하도록 만들어졌습니다. 프레임워크 자체의 설계도 개념적으로 단순하여, 연구자들이 MLX를 쉽게 확장하고 개선할 수 있도록 함으로써 새로운 아이디어를 빠르게 탐구할 수 있도록 돕는 것이 목표입니다.

Apple 실리콘 디바이스에서는 MLX를 통해 LLM을 가속화할 수 있으며, 모델을 로컬에서 매우 편리하게 실행할 수 있습니다.

이제 Apple MLX 프레임워크는 Phi-3.5-Instruct(**Apple MLX 프레임워크 지원**), Phi-3.5-Vision(**MLX-VLM 프레임워크 지원**), 그리고 Phi-3.5-MoE(**Apple MLX 프레임워크 지원**)의 양자화 변환을 지원합니다. 다음을 통해 시도해 봅시다:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Apple MLX를 사용한 Phi-3.5 샘플**

| 연구소    | 소개      | 이동   |
| -------- | ------- | ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLX 프레임워크를 사용하여 Phi-3.5 Instruct를 사용하는 방법을 배워보세요   | [이동](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb) |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Apple MLX 프레임워크를 사용하여 이미지를 분석하기 위한 Phi-3.5 Vision 사용법을 배워보세요 | [이동](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb) |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLX 프레임워크를 사용하여 Phi-3.5 MoE를 사용하는 방법을 배워보세요 | [이동](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb) |

## **리소스**

1. Apple MLX 프레임워크에 대해 알아보기 [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub 저장소 [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub 저장소 [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서의 원어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.