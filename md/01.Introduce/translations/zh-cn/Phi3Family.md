# **Phi-3 Family**

Phi-3 模型是目前最具能力且最具性价比的小型语言模型（SLM），在各种语言、推理、编码和数学基准测试中的表现优于同等大小和较大尺寸的模型。此版本扩展了客户可选择的高质量模型，为构建生成式 AI 应用提供了更多实用选择。

Phi-3 系列包括迷你、小型、中型和视觉版本，根据不同参数数量进行训练，以适应各种应用场景。每个模型均经过针对性调优，并根据微软的负责任 AI、安全性和安全标准进行开发，以确保其可直接使用。

## Phi-3 任务示例
| | |
|-|-|
|任务|Phi-3|
|语言任务|是|
|数学与推理|是|
|代码|是|
|函数调用|否|
|自我编排 (助手)|否|
|专用嵌入模型|否|

## **Phi-3-Mini**

Phi-3-mini 是一个拥有 38 亿参数的语言模型，支持两种上下文长度：[128K](https://ai.azure.com/explore/models/Phi-3-mini-128k-instruct/version/7/registry/azureml) 和 [4K](https://ai.azure.com/explore/models/Phi-3-mini-4k-instruct/version/7/registry/azureml)。

Phi-3-Mini 是一个基于 Transformer 的语言模型，拥有 38 亿参数。它使用包含有益信息的高质量数据进行训练，并辅以各种 NLP 合成文本以及内部和外部聊天数据集，这些新的数据源显著提高了聊天能力。此外，Phi-3-Mini 在预训练后通过监督微调（SFT）和直接偏好优化（DPO）进行了聊天微调。经过这一后期训练，Phi-3-Mini 在多项能力上都取得了显著提升，尤其是在对齐、稳健性和安全性方面。该模型属于 Phi-3 系列，以 Mini 版本推出，有 4K 和 128K 两个版本，分别表示其支持的上下文长度（以 tokens 计）。

## **Phi-3-Small**

Phi-3-small 是一个拥有 70 亿参数的语言模型，支持两种上下文长度：[128K](https://ai.azure.com/explore/models/Phi-3-small-128k-instruct/version/1/registry/azureml) 和 [8K](https://ai.azure.com/explore/models/Phi-3-small-8k-instruct/version/1/registry/azureml)。

Phi-3-Small 是一个基于 Transformer 的语言模型，拥有 70 亿参数。它使用包含有益信息的高质量数据进行训练，并辅以各种 NLP 合成文本以及内部和外部聊天数据集，这些新的数据源显著提高了聊天能力。此外，Phi-3-Small 在预训练后通过监督微调（SFT）和直接偏好优化（DPO）进行了聊天微调。经过这一后期训练，Phi-3-Small 在多项能力上都取得了显著提升，尤其是在对齐、稳健性和安全性方面。与 Phi-3-Mini 相比，Phi-3-Small 还在多语言数据集上进行了更加密集的训练。该模型系列提供两个版本，8K 和 128K，分别表示其支持的上下文长度（以 tokens 计）。

## **Phi-3-Medium**

Phi-3-medium 是一个拥有 140 亿参数的语言模型，支持两种上下文长度：[128K](https://ai.azure.com/explore/models/Phi-3-medium-128k-instruct/version/1/registry/azureml) 和 [4K](https://ai.azure.com/explore/models/Phi-3-medium-4k-instruct/version/1/registry/azureml)。

Phi-3-Medium 是一个基于 Transformer 的语言模型，拥有 140 亿参数。它使用包含有益信息的高质量数据进行训练，并辅以各种 NLP 合成文本以及内部和外部聊天数据集，这些新的数据源显著提高了聊天能力。此外，Phi-3-Medium 在预训练后通过监督微调（SFT）和直接偏好优化（DPO）进行了聊天微调。经过这一后期训练，Phi-3-Medium 在多项能力上都取得了显著提升，尤其是在对齐、稳健性和安全性方面。该模型系列提供两个版本，4K 和 128K，分别表示其支持的上下文长度（以 tokens 计）。

## **Phi-3-vision**

[Phi-3-vision](https://ai.azure.com/explore/models/Phi-3-vision-128k-instruct/version/1/registry/azureml) 是一个拥有 42 亿参数的多模态模型，具备语言和视觉能力。

Phi-3-vision 是 Phi-3 系列中的第一个多模态模型，将文本和图像结合在一起。Phi-3-vision 可用于推理现实世界中的图像，从图像中提取和推理文本。它还针对图表与图形理解进行了优化，可用于生成洞察和回答问题。Phi-3-vision 基于 Phi-3-mini 的语言能力，继续以小尺寸实现强大的语言和图像推理品质。

## **Phi Silica**

我们推出了 Phi Silica，它基于 Phi 系列模型构建，并专门为 Copilot+ PC 中的 NPU 设计。Windows 是第一个为 NPU 定制并内置了一款最先进的小语言模型（SLM）的平台。

Phi Silica API 以及 OCR、Studio Effects、Live Captions、Recall User Activity API 将于 6 月在 Windows Copilot 库中提供。稍后还将推出更多 API，如Vector Embedding、RAG API、Text Summarization等。

## **探索所有 Phi-3 模型**

- [Azure AI](https://ai.azure.com/explore/models?&selectedCollection=phi)
- [Hugging Face.](https://huggingface.co/collections/microsoft/phi-3-6626e15e9585a200d2d761e3)

## ONNX 模型

两个 ONNX 模型，“cpu-int4-rtn-block-32” 和 “cpu-int4-rtn-block-32-acc-level-4” 之间的主要区别在于准确性水平。带有“acc-level-4”的模型旨在平衡延迟与准确性，通过略微牺牲准确性来获得更好的性能，这可能特别适用于移动设备。

## 模型选择示例

| | | | |
|-|-|-|-|
|客户需求|任务|模型选择|更多信息|
|需要一个简单地总结消息的模型|谈话的总结|Phi-3 text model|决定因素在于，客户拥有一个明确且简单的语言任务。|
|一个免费的适用于儿童的数学辅导应用。|数学和推理|Phi-3 text models|由于应用程序是免费的，客户希望找到一个不需要定期支付费用的解决方案。 |
|自主巡逻车载摄像头|视觉分析|Phi-Vision|需要一个可以在无网络环境下工作的边缘计算解决方案
|想要构建一个基于人工智能的旅行预订代理。|需要复杂的规划、函数调用和编排。|GPT models|需要具备规划能力，调用API收集信息并执行的功能。|
|想要为员工创建一个Copilot助手。|RAG, 多域、复杂且开放式的问题。|GPT models|开放式场景，需要更广泛的世界知识，因此更适合使用大型模型。|
