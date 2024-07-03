# **準備推出 E2E 範例**

這個範例是匯入 [TruthfulQA 的資料](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) 來微調 Phi-3-mini 模型。這是架構

![arch](../../../../imgs/06/e2e/arch.png)

## **介紹**

我們希望使用 [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) set 來讓 Phi-3-mini 更專業地回答我們的問題。這是你第一次使用 Phi-3-mini 的 E2E 專案。

### **需求**

1. Python 3.10+
2. CUDA 12.1
3. Linux / WSL
4. Azure ML
5. Azure Compute A100

### **知識**

1. [了解 Phi-3](../../../01.Introduce/Phi3Family.md)
2. [了解如何使用 Microsoft Olive 進行微調](../../../04.Fine-tuning/FineTuning_MicrosoftOlive.md)
3. [了解 ONNX Runtime 用於生成式 AI](https://github.com/microsoft/onnxruntime-genai)

