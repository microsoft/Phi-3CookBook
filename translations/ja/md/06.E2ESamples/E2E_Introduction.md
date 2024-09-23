# **E2Eサンプルの紹介**

このサンプルでは、[TruthfulQAのデータ](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)をインポートして、Phi-3-miniモデルのファインチューニングを行います。以下がアーキテクチャです。

![arch](../../../../translated_images/arch.9993118a26f2f7367f8fbd75fa2c4ed75c503905d5662dc87818f7752be17716.ja.png)

## **紹介**

私たちは、[TruthfulQAのデータ](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)セットを使用して、Phi-3-miniがより専門的に質問に答えるようにしたいと考えています。これはPhi-3-miniを使った初めてのE2Eプロジェクトです。

### **必要条件**

1. Python 3.10以上
2. CUDA 12.1
3. Linux / WSL
4. Azure ML
5. Azure Compute A100

### **知識**

1. [Phi-3について学ぶ](../01.Introduce/Phi3Family.md)
2. [Microsoft Oliveを使ったファインチューニングについて学ぶ](../04.Fine-tuning/FineTuning_MicrosoftOlive.md)
3. [生成AIのためのONNX Runtimeについて学ぶ](https://github.com/microsoft/onnxruntime-genai)

免責事項: 翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。 出力を確認し、必要な修正を行ってください。