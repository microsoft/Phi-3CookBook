# Microsoft 的 Phi-3 系列

Phi-3 模型是目前最强大且性价比最高的小型语言模型（SLM），在各种语言、推理、编码和数学基准测试中表现优于同尺寸及更大尺寸的模型。这次发布扩展了高质量模型的选择，为客户提供了更多构建生成式 AI 应用的实际选择。

Phi-3 系列包括 mini、small、medium 和 vision 版本，基于不同的参数量进行训练，以满足各种应用场景。每个模型都经过指令调优，并根据 Microsoft 的负责任 AI、安全和安全标准开发，以确保即开即用。Phi-3-mini 表现优于两倍大小的模型，Phi-3-small 和 Phi-3-medium 表现优于更大规模的模型，包括 GPT-3.5T。

## Phi-3 任务示例

| | |
|-|-|
|任务|Phi-3|
|语言任务|是|
|数学与推理|是|
|编码|是|
|函数调用|否|
|自我编排（助手）|否|
|专用嵌入模型|否|

## Phi-3-mini

Phi-3-mini 是一个拥有 38 亿参数的语言模型，可以在 [Microsoft Azure AI Studio](https://ai.azure.com/explore/models?selectedCollection=phi)、[Hugging Face](https://huggingface.co/collections/microsoft/phi-3-6626e15e9585a200d2d761e3) 和 [Ollama](https://ollama.com/library/phi3) 上获取。它提供两种上下文长度：[128K](https://ai.azure.com/explore/models/Phi-3-mini-128k-instruct/version/9/registry/azureml) 和 [4K](https://ai.azure.com/explore/models/Phi-3-mini-4k-instruct/version/9/registry/azureml)。

Phi-3-mini 是一个基于 Transformer 的语言模型，拥有 38 亿参数。它使用包含教育性有用信息的高质量数据进行训练，并增加了各种 NLP 合成文本的新数据源，以及内部和外部的聊天数据集，显著提高了聊天能力。此外，Phi-3-mini 在预训练后通过监督微调（SFT）和直接偏好优化（DPO）进行了聊天微调。经过这些后期训练，Phi-3-mini 在多项能力上表现出显著改进，尤其是在对齐性、鲁棒性和安全性方面。该模型是 Phi-3 系列的一部分，提供两种版本，4K 和 128K，代表它可以支持的上下文长度（以 token 计）。

![phi3modelminibenchmark](../../../../translated_images/phi3minibenchmark.c93c3578556239cbaaa43be385def37b27e7f617ba89e3039bfc0ad44ab45ccd.zh.png)

![phi3modelminibenchmark128k](../../../../translated_images/phi3minibenchmark128.7ea027bb3b4f98ea6d11de146498f68eebce7647b7911bdd82945e5ba22feb5a.zh.png)

## Phi-3.5-mini-instruct

[Phi-3.5 mini](https://ai.azure.com/explore/models/Phi-3.5-mini-instruct/version/1/registry/azureml) 是一个轻量级的、最先进的开源模型，基于用于 Phi-3 的数据集构建——合成数据和过滤的公开网站数据——重点是非常高质量的、推理密集的数据。该模型属于 Phi-3 模型系列，支持 128K token 的上下文长度。模型经过严格的增强过程，结合了监督微调、近端策略优化和直接偏好优化，以确保精确的指令遵循和强大的安全措施。

Phi-3.5 Mini 拥有 38 亿参数，是一个仅使用解码器的 Transformer 模型，使用与 Phi-3 Mini 相同的分词器。

![phi3miniinstruct](../../../../translated_images/phi3miniinstructbenchmark.25eee38b4ba0f21f54eed3ec4f2d853d35527c34fa31ef7176354b0cb001108d.zh.png)

总体而言，只有 38 亿参数的模型在多语言理解和推理能力上达到了与更大模型相似的水平。然而，由于其规模有限，在某些任务上仍然存在基本限制。模型没有足够的容量存储太多的事实知识，因此用户可能会遇到事实不准确的情况。不过，我们相信这种弱点可以通过将 Phi-3.5 与搜索引擎结合使用来解决，特别是在 RAG 设置下使用模型时。

### 语言支持

下表突出了 Phi-3 在多语言 MMLU、MEGA 和多语言 MMLU-pro 数据集上的多语言能力。总体而言，我们观察到，即使只有 38 亿活跃参数，模型在多语言任务上也与其他具有更大活跃参数的模型非常具有竞争力。

![phi3minilanguagesupport](../../../../translated_images/phi3miniinstructlanguagesupport.14e2aa67f8245c3a5d045a1cc419514b7e93d0649895d1f47cf4ee055c2eaa8f.zh.png)

## Phi-3-small

Phi-3-small 是一个拥有 70 亿参数的语言模型，提供两种上下文长度 [128K](https://ai.azure.com/explore/models/Phi-3-small-128k-instruct/version/2/registry/azureml) 和 [8K](https://ai.azure.com/explore/models/Phi-3-small-8k-instruct/version/2/registry/azureml)，在各种语言、推理、编码和数学基准测试中表现优于 GPT-3.5T。

Phi-3-small 是一个基于 Transformer 的语言模型，拥有 70 亿参数。它使用包含教育性有用信息的高质量数据进行训练，并增加了各种 NLP 合成文本的新数据源，以及内部和外部的聊天数据集，显著提高了聊天能力。此外，Phi-3-small 在预训练后通过监督微调（SFT）和直接偏好优化（DPO）进行了聊天微调。经过这些后期训练，Phi-3-small 在多项能力上表现出显著改进，尤其是在对齐性、鲁棒性和安全性方面。Phi-3-small 还比 Phi-3-Mini 在多语言数据集上进行了更密集的训练。模型系列提供两种版本，8K 和 128K，代表它可以支持的上下文长度（以 token 计）。

![phi3modelsmall](../../../../translated_images/phi3smallbenchmark.8a18c35945e2dfc770fa7a110b8d39b7538c98d193773256c76f24fd5a8ab0f0.zh.png)

![phi3modelsmall128k](../../../../translated_images/phi3smallbenchmark128.ba75b5bb13f78b2556430c6b27188013a9fc3ca3c0cf80941b4a8e538f817610.zh.png)

## Phi-3-medium

Phi-3-medium 是一个拥有 140 亿参数的语言模型，提供两种上下文长度 [128K](https://ai.azure.com/explore/models/Phi-3-medium-128k-instruct/version/2/registry/azureml) 和 [4K](https://ai.azure.com/explore/models/Phi-3-medium-4k-instruct/version/2/registry/azureml)，继续保持在性能上优于 Gemini 1.0 Pro 的趋势。

Phi-3-medium 是一个基于 Transformer 的语言模型，拥有 140 亿参数。它使用包含教育性有用信息的高质量数据进行训练，并增加了各种 NLP 合成文本的新数据源，以及内部和外部的聊天数据集，显著提高了聊天能力。此外，Phi-3-medium 在预训练后通过监督微调（SFT）和直接偏好优化（DPO）进行了聊天微调。经过这些后期训练，Phi-3-medium 在多项能力上表现出显著改进，尤其是在对齐性、鲁棒性和安全性方面。模型系列提供两种版本，4K 和 128K，代表它可以支持的上下文长度（以 token 计）。

![phi3modelmedium](../../../../translated_images/phi3mediumbenchmark.580c367123541e531634aa8e17d8627b63516c2275833aea89a44d3d57a9886d.zh.png)

![phi3modelmedium128k](../../../../translated_images/phi3mediumbenchmark128.6abc506652e589fc2a8f420302fdfd3e384c563bbd08c7fa767b6200d9452ba4.zh.png)

[!NOTE]
我们推荐切换到 Phi-3.5-MoE 作为 Phi-3-medium 的升级版本，因为 MoE 模型是一个更好且性价比更高的模型。

## Phi-3-vision

[Phi-3-vision](https://ai.azure.com/explore/models/Phi-3-vision-128k-instruct/version/2/registry/azureml) 是一个拥有 42 亿参数的多模态模型，具备语言和视觉能力，在一般视觉推理、OCR 和表格及图表理解任务上表现优于更大的模型如 Claude-3 Haiku 和 Gemini 1.0 Pro V。

Phi-3-vision 是 Phi-3 系列中的第一个多模态模型，将文本和图像结合在一起。Phi-3-vision 可以用于对真实世界图像进行推理，并从图像中提取和推理文本。它还针对图表和图解理解进行了优化，可以用于生成见解和回答问题。Phi-3-vision 基于 Phi-3-mini 的语言能力，继续在小尺寸中保持强大的语言和图像推理质量。

![phi3modelvision](../../../../translated_images/phi3visionbenchmark.6b17cc8d6e937696428859da214d49cdeb86b318ca32ac0d65d12284a3347dfd.zh.png)

## Phi-3.5-vision

[Phi-3.5 Vision](https://ai.azure.com/explore/models/Phi-3.5-vision-instruct/version/1/registry/azureml) 是一个轻量级的、最先进的开源多模态模型，基于包括合成数据和过滤的公开网站在内的数据集构建，重点是非常高质量的、推理密集的数据，涵盖文本和视觉。该模型属于 Phi-3 模型系列，多模态版本支持 128K token 的上下文长度。模型经过严格的增强过程，结合了监督微调和直接偏好优化，以确保精确的指令遵循和强大的安全措施。

Phi-3.5 Vision 拥有 42 亿参数，包含图像编码器、连接器、投影仪和 Phi-3 Mini 语言模型。

该模型旨在广泛的商业和研究用途中使用，主要用于英语。模型提供用于通用 AI 系统和应用的功能，具有视觉和文本输入能力，适用于
1) 内存/计算受限环境。
2) 延迟约束场景。
3) 一般图像理解。
4) OCR。
5) 图表和表格理解。
6) 多图像比较。
7) 多图像或视频剪辑摘要。

Phi-3.5-vision 模型旨在加速高效语言和多模态模型的研究，作为生成式 AI 驱动功能的构建模块。

![phi35_vision](../../../../translated_images/phi35visionbenchmark.962c7a0e167a1ba3db02b54e9285cfa974d87353386888f580cb1e4c08061a12.zh.png)

## Phi-3.5-MoE

[Phi-3.5 MoE](https://ai.azure.com/explore/models/Phi-3.5-MoE-instruct/version/1/registry/azureml) 是一个轻量级的、最先进的开源模型，基于用于 Phi-3 的数据集构建——合成数据和过滤的公开文档——重点是非常高质量的、推理密集的数据。该模型支持多语言，并具有 128K token 的上下文长度。模型经过严格的增强过程，结合了监督微调、近端策略优化和直接偏好优化，以确保精确的指令遵循和强大的安全措施。

Phi-3 MoE 具有 16x3.8B 参数，在使用 2 个专家时具有 6.6B 活跃参数。该模型是一个仅使用解码器的混合专家 Transformer 模型，使用词汇量为 32,064 的分词器。

该模型旨在广泛的商业和研究用途中使用，主要用于英语。模型提供用于通用 AI 系统和应用的功能，适用于

1) 内存/计算受限环境。
2) 延迟约束场景。
3) 强推理（特别是数学和逻辑）。

MoE 模型旨在加速语言和多模态模型的研究，作为生成式 AI 驱动功能的构建模块，并需要额外的计算资源。

![phi35moe_model](../../../../translated_images/phi35moebenchmark.9d66006ffabab800536d6e3feb1874dc52c360f1e5b25efa856dfb08c6290c7a.zh.png)

> [!NOTE]
>
> Phi-3 模型在事实知识基准测试（如 TriviaQA）中的表现不如预期，因为较小的模型尺寸导致其保留事实的能力较低。

## Phi silica

我们推出了 Phi Silica，该模型基于 Phi 系列模型构建，专为 Copilot+ PC 中的 NPU 设计。Windows 是第一个拥有为 NPU 定制的小型语言模型（SLM）并随系统内置的平台。Phi Silica API 以及 OCR、Studio Effects、Live Captions 和 Recall User Activity API 将于六月在 Windows Copilot Library 中提供。更多 API，如 Vector Embedding、RAG API 和 Text Summarization 将在后续推出。

## **查找所有 Phi-3 模型**

- [Azure AI](https://ai.azure.com/explore/models?selectedCollection=phi)
- [Hugging Face](https://huggingface.co/collections/microsoft/phi-3-6626e15e9585a200d2d761e3)

## ONNX 模型

两个 ONNX 模型 “cpu-int4-rtn-block-32” 和 “cpu-int4-rtn-block-32-acc-level-4” 之间的主要区别在于准确性水平。带有 “acc-level-4” 的模型旨在平衡延迟与准确性，在准确性上略有妥协以获得更好的性能，这可能特别适合移动设备。

## 模型选择示例

| | | | |
|-|-|-|-|
|客户需求|任务|起始模型|更多详情|
|需要一个简单总结消息线程的模型|对话总结|Phi-3 文本模型|决定因素是客户有一个定义明确且直接的语言任务|
|一个免费的儿童数学辅导应用|数学和推理|Phi-3 文本模型|因为应用是免费的，客户希望解决方案不会产生持续费用|
|自巡逻车摄像头|视觉分析|Phi-Vision|需要一个可以在无互联网情况下工作的解决方案|
|想要构建一个基于 AI 的旅行预订代理|需要复杂的计划、函数调用和编排|GPT 模型|需要具备计划、调用 API 收集信息和执行的能力|
|想为员工构建一个助手|RAG、多领域、复杂且开放|GPT 模型|开放场景，需要更广泛的世界知识，因此更大模型更合适|

**免责声明**:
本文件是使用机器翻译服务翻译的。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文件视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误读，我们不承担任何责任。