# **E2Eサンプルの紹介**

このサンプルは、[TruthfulQAのデータ](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)をPhi-3-miniモデルにファインチューニングするものです。これはアーキテクチャです。

![arch](../../../../imgs/06/e2e/arch.png)

## **紹介**

私たちは、[TruthfulQAのデータ](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)セットを使用して、Phi-3-miniが私たちの質問に対してより専門的に回答できるようにしたいと考えています。これはPhi-3-miniを使用した最初のE2Eプロジェクトです。

### **要件**

1. Python 3.10以上
2. CUDA 12.1
3. Linux / WSL
4. Azure ML
5. Azure Compute A100

### **知識**

1. [Phi-3について学ぶ](../../../01.Introduce/translations/ja-jp/Phi3Family.md)
2. [Microsoft Oliveを使用してファインチューニングする方法を学ぶ](../../../04.Fine-tuning/translations/ja-jp/FineTuning_MicrosoftOlive.md)
3. [生成AIのためのONNX Runtimeについて学ぶ](https://github.com/microsoft/onnxruntime-genai)
