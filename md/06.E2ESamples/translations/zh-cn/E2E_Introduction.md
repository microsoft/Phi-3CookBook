# E2E 示例

这个示例将导入[TruthfulQA 数据](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)来微调 Phi-3-mini 模型。这是其架构图

![架构图](../../imgs/06/e2e/arch.png)

## 简介

我们希望使用[TruthfulQA 数据](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)集，使 Phi-3-mini 更专业地回答我们的问题。这是你第一次使用 Phi-3-mini 进行的 E2E 项目。

### 要求

1. Python 3.10+
2. CUDA 12.1
3. Linux / WSL
4. Azure ML
5. Azure Compute A100

### 参考

1. [了解 Phi-3](../01.Introduce/Phi3Family.md)
2. [了解如何使用 Microsoft Olive 进行微调](../04.Fine-tuning/FineTuning_MicrosotOlive.md)
3. [了解用于生成型AI的 ONNX Runtime](https://github.com/microsoft/onnxruntime-genai)