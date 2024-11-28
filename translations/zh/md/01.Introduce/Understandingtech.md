# 关键技术包括

1. [DirectML](https://learn.microsoft.com/windows/ai/directml/dml?WT.mc_id=aiml-138114-kinfeylo) - 基于DirectX 12构建的硬件加速机器学习的低级API。
2. [CUDA](https://blogs.nvidia.com/blog/what-is-cuda-2/) - 由Nvidia开发的并行计算平台和应用程序接口（API）模型，允许在图形处理单元（GPU）上进行通用处理。
3. [ONNX](https://onnx.ai/) (开放神经网络交换格式) - 一种用于表示机器学习模型的开放格式，提供不同机器学习框架之间的互操作性。
4. [GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) (通用图更新格式) - 一种用于表示和更新机器学习模型的格式，特别适用于在4-8位量化的CPU上有效运行的小型语言模型。

## DirectML

DirectML 是一个低级API，能够实现硬件加速的机器学习。它基于DirectX 12构建，利用GPU加速，并且与供应商无关，这意味着无需更改代码即可在不同的GPU供应商之间工作。它主要用于GPU上的模型训练和推理工作负载。

关于硬件支持，DirectML 设计用于与广泛的GPU配合工作，包括AMD集成和独立GPU，Intel集成GPU，以及NVIDIA独立GPU。它是Windows AI平台的一部分，并在Windows 10和11上受支持，允许在任何Windows设备上进行模型训练和推理。

与DirectML相关的更新和机会包括支持多达150个ONNX操作符，并被ONNX运行时和WinML使用。它得到了主要集成硬件供应商（IHVs）的支持，每个供应商实现了各种元命令。

## CUDA

CUDA，代表统一计算设备架构，是由Nvidia创建的并行计算平台和应用程序接口（API）模型。它允许软件开发人员使用支持CUDA的图形处理单元（GPU）进行通用处理——这种方法称为GPGPU（图形处理单元上的通用计算）。CUDA是Nvidia GPU加速的关键使能技术，广泛应用于机器学习、科学计算和视频处理等各个领域。

CUDA的硬件支持特定于Nvidia的GPU，因为它是Nvidia开发的专有技术。每种架构支持特定版本的CUDA工具包，提供必要的库和工具，供开发人员构建和运行CUDA应用程序。

## ONNX

ONNX（开放神经网络交换格式）是一种用于表示机器学习模型的开放格式。它提供了一个可扩展计算图模型的定义，以及内置操作符和标准数据类型的定义。ONNX允许开发人员在不同的机器学习框架之间移动模型，实现互操作性，并简化AI应用程序的创建和部署。

Phi3 mini 可以在包括服务器平台、Windows、Linux和Mac桌面以及移动CPU在内的设备上，使用ONNX运行时在CPU和GPU上运行。
我们添加的优化配置包括：

- 针对int4 DML的ONNX模型：通过AWQ量化为int4
- 针对fp16 CUDA的ONNX模型
- 针对int4 CUDA的ONNX模型：通过RTN量化为int4
- 针对int4 CPU和移动设备的ONNX模型：通过RTN量化为int4

## Llama.cpp

Llama.cpp 是一个用C++编写的开源软件库。它在各种大型语言模型（LLM）上执行推理，包括Llama。与ggml库（一个通用张量库）一起开发，llama.cpp旨在提供比原始Python实现更快的推理速度和更低的内存使用。它支持硬件优化、量化，并提供了简单的API和示例。如果你对高效的LLM推理感兴趣，llama.cpp值得探索，因为Phi3可以运行Llama.cpp。

## GGUF

GGUF（通用图更新格式）是一种用于表示和更新机器学习模型的格式。它特别适用于可以在4-8位量化的CPU上有效运行的小型语言模型（SLM）。GGUF对快速原型设计和在边缘设备或CI/CD管道等批处理任务中运行模型非常有用。

**免责声明**：
本文档使用基于机器的人工智能翻译服务进行翻译。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于关键信息，建议使用专业的人类翻译。我们不对因使用此翻译而引起的任何误解或误读负责。