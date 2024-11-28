## 微调场景

![使用微软服务进行微调](../../../../translated_images/FinetuningwithMS.921fa8c240611562e7c4a5ceb7eca04f458ad6f3c899d5a0dc120030398d9e08.zh.png)

**平台** 这包括各种技术，如Azure AI Foundry、Azure Machine Learning、AI Tools、Kaito和ONNX Runtime。

**基础设施** 这包括CPU和FPGA，它们是微调过程中的关键部分。让我向你展示每种技术的图标。

**工具和框架** 这包括ONNX Runtime和ONNX Runtime。让我向你展示每种技术的图标。
[插入ONNX Runtime和ONNX Runtime的图标]

使用微软技术进行微调过程涉及各种组件和工具。通过理解和利用这些技术，我们可以有效地微调我们的应用程序并创建更好的解决方案。

## 模型即服务

使用托管微调来微调模型，无需创建和管理计算资源。

![MaaS微调](../../../../translated_images/MaaSfinetune.1678f33544c36b9016d8c018ce9c4c1622fb3bc2d72751291c39813f88bce052.zh.png)

无服务器微调适用于Phi-3-mini和Phi-3-medium模型，使开发人员能够快速轻松地为云和边缘场景定制模型，而无需安排计算资源。我们还宣布，Phi-3-small现在通过我们的模型即服务产品提供，使开发人员可以快速轻松地开始AI开发，而无需管理底层基础设施。

[微调示例](https://github.com/microsoft/Phi-3CookBook/blob/main/md/04.Fine-tuning/FineTuning_AIStudio.md)
## 模型即平台

用户管理自己的计算资源以微调他们的模型。

![Maap微调](../../../../translated_images/MaaPFinetune.f88828d32d16ced1198525fceed9184ce17516f5c1a404c264d87a4ca816947f.zh.png)

[微调示例](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## 微调场景

| | | | | | | |
|-|-|-|-|-|-|-|
|场景|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|将预训练的LLM适应特定任务或领域|是|是|是|是|是|是|
|为NLP任务（如文本分类、命名实体识别和机器翻译）进行微调|是|是|是|是|是|是|
|为QA任务进行微调|是|是|是|是|是|是|
|为聊天机器人生成类似人类的响应进行微调|是|是|是|是|是|是|
|为生成音乐、艺术或其他形式的创意进行微调|是|是|是|是|是|是|
|减少计算和财务成本|是|是|否|是|是|否|
|减少内存使用|否|是|否|是|是|是|
|使用更少的参数进行高效微调|否|是|是|否|否|是|
|内存高效的数据并行形式，可访问所有可用GPU设备的总GPU内存|否|否|否|是|是|是|

## 微调性能示例

![微调性能](../../../../translated_images/Finetuningexamples.88bad3a5350927b08b1f06e4bced95cfd3715caa933d21c9ff658dcf0db94f73.zh.png)

**免责声明**：
本文档是使用基于机器的人工智能翻译服务进行翻译的。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于关键信息，建议进行专业的人类翻译。我们对使用此翻译所产生的任何误解或误读不承担责任。