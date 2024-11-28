# **介绍 E2E 示例**

此示例将导入 [TruthfulQA 的数据](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) 以微调 Phi-3-mini 模型。这是架构图

![arch](../../../../translated_images/arch.9993118a26f2f7367f8fbd75fa2c4ed75c503905d5662dc87818f7752be17716.zh.png)

## **介绍**

我们希望使用 [TruthfulQA 的数据](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) 集让 Phi-3-mini 更专业地回答我们的问题。这是你使用 Phi-3-mini 的第一个 E2E 项目

### **要求**

1. Python 3.10+
2. CUDA 12.1
3. Linux / WSL
4. Azure ML
5. Azure Compute A100

### **知识**

1. [了解 Phi-3](../01.Introduce/Phi3Family.md)
2. [了解如何使用 Microsoft Olive 进行微调](../04.Fine-tuning/FineTuning_MicrosoftOlive.md)
3. [了解 ONNX Runtime 用于生成式 AI](https://github.com/microsoft/onnxruntime-genai)

**免责声明**:
本文档使用基于机器的AI翻译服务进行翻译。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原文档的母语版本视为权威来源。对于关键信息，建议进行专业的人类翻译。我们对因使用本翻译而引起的任何误解或误读不承担责任。