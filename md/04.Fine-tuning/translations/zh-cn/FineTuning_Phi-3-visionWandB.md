# Phi-3-Vision-128K-Instruct 项目概述

## 模型

本项目的核心是轻量级、先进的多模态模型 Phi-3-Vision-128K-Instruct。它属于 Phi-3 模型家族，支持最多 128,000 个令牌的上下文长度。该模型在包括合成数据和精心筛选的公开网站在内的多样化数据集上进行了训练，强调高质量、推理密集型内容。训练过程包括监督微调和直接优先级优化，以确保精确遵循指令，同时具有强大的安全措施。

## 创建样本数据的关键因素:

1. **测试**: 样本数据允许您在各种场景下测试应用程序，而不影响实际数据。这在开发和暂存阶段尤为重要。

2. **性能调优**: 通过模拟实际数据的规模和复杂性的样本数据，您可以发现性能瓶颈并相应地优化应用程序。

3. **原型制作**: 样本数据可用于创建原型和模型，有助于了解用户需求并获得反馈。

4. **数据分析**: 在数据科学中，样本数据通常用于探索性数据分析、模型训练和算法测试。

5. **安全性**: 在开发和测试环境中使用样本数据可以帮助防止敏感实际数据的意外泄露。

6. **学习**: 如果您正在学习新技术或工具，使用样本数据提供了一种实际的方法来应用所学内容。

请记住，样本数据的质量对这些活动的影响可能非常显著。在结构和可变性方面，它应尽可能接近实际数据。

### 样本数据创建
[Generate DataSet Script](./CreatingSampleData.md)

## 数据集

一个很好的样本数据集示例是 [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (可在 Huggingface 上找到). 
这个样本数据集包含了 Burberry 产品及其元数据，如产品类别、价格和标题，共有 3,040 行，每行代表一个独特的产品。这个数据集让我们测试模型理解和解释视觉数据的能力，生成描述性文本，捕捉复杂的视觉细节和品牌特定特征。

**注意:** 您可以使用任何包含图像的数据集。

## 综合推理

模型需要根据图像对价格和命名进行推理。这要求模型不仅要识别视觉特征，还要理解它们在产品价值和品牌方面的含义。通过从图像中合成准确的文本描述，该项目突显了整合视觉数据以提高模型在实际应用中的性能和通用性的潜力。

## Phi-3 Vision 架构

模型架构是 Phi-3 的多模态版本。它处理文本和图像数据，将这些输入整合到一个统一的序列中，以实现全面的理解和生成任务。模型为文本和图像使用单独的嵌入层。文本令牌被转换为密集向量，而图像通过 CLIP 视觉模型进行处理以提取特征嵌入。然后投影这些图像嵌入以匹配文本嵌入的维度，确保它们可以无缝集成。

## 文本和图像嵌入集成

文本序列中的特殊令牌表示应插入图像嵌入的位置。在处理过程中，这些特殊令牌被替换为相应的图像嵌入，使模型能够将文本和图像作为单个序列处理。针对我们的数据集，使用特殊的 <|image|> 令牌按如下方式来格式化提示词:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## 示例代码
- [Phi-3-Vision Training Script](../../code/04.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)
