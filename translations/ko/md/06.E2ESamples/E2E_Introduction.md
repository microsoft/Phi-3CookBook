# **E2E 샘플 소개**

이 샘플은 [TruthfulQA의 데이터](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)를 가져와서 Phi-3-mini 모델을 파인 튜닝하는 예제입니다. 다음은 아키텍처입니다.

![arch](../../../../translated_images/arch.9993118a26f2f7367f8fbd75fa2c4ed75c503905d5662dc87818f7752be17716.ko.png)

## **소개**

우리는 [TruthfulQA의 데이터](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) 세트를 사용하여 Phi-3-mini가 우리의 질문에 더 전문적으로 답변할 수 있도록 하고자 합니다. 이것이 Phi-3-mini를 사용한 첫 번째 E2E 프로젝트입니다.

### **요구사항**

1. Python 3.10+
2. CUDA 12.1
3. Linux / WSL
4. Azure ML
5. Azure Compute A100

### **지식**

1. [Phi-3에 대해 배우기](../01.Introduce/Phi3Family.md)
2. [Microsoft Olive를 사용한 파인 튜닝 방법 배우기](../04.Fine-tuning/FineTuning_MicrosoftOlive.md)
3. [생성 AI를 위한 ONNX Runtime 배우기](https://github.com/microsoft/onnxruntime-genai)

