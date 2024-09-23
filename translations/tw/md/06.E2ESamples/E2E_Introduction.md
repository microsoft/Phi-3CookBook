# **介紹 E2E 範例**

這個範例是導入 [TruthfulQA 的數據](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) 來微調 Phi-3-mini 模型。這是架構圖

![arch](../../../../translated_images/arch.9993118a26f2f7367f8fbd75fa2c4ed75c503905d5662dc87818f7752be17716.tw.png)

## **介紹**

我們希望使用 [TruthfulQA 的數據](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) 集，讓 Phi-3-mini 更專業地回答我們的問題。這是你第一次使用 Phi-3-mini 的 E2E 專案。

### **需求**

1. Python 3.10+
2. CUDA 12.1
3. Linux / WSL
4. Azure ML
5. Azure Compute A100

### **知識**

1. [了解 Phi-3](../01.Introduce/Phi3Family.md)
2. [了解如何使用 Microsoft Olive 進行微調](../04.Fine-tuning/FineTuning_MicrosoftOlive.md)
3. [了解 ONNX Runtime 在生成式 AI 的應用](https://github.com/microsoft/onnxruntime-genai)

