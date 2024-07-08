## 提到的关键技术包括:
 
1. [DirectML](https://learn.microsoft.com/windows/ai/directml/dml?WT.mc_id=aiml-138114-kinfeylo) - 基于DirectX 12构建的用于硬件加速机器学习的低阶API。
2. [CUDA](https://blogs.nvidia.com/blog/what-is-cuda-2/) - 由Nvidia开发的并行计算平台和应用程序编程接口（API）模型，可实现图形处理单元（GPU）上的通用处理。
3. [ONNX](https://onnx.ai/) (Open Neural Network Exchange) - 一个旨在表示机器学习模型的开放格式，可在不同的ML框架之间提供互操作性。
4. [GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) (Generic Graph Update Format) - 用于表示和更新机器学习模型的格式，特别适用于可以在4-8位量化的CPU上高效运行的较小语言模型。

 
### DirectML 
DirectML 是一个底层级别的 API，可以实现硬件加速的机器学习。它基于 DirectX 12 构建，以利用 GPU 加速，并且是厂商无关的，这意味着在不同的 GPU 厂商之间无需更改代码即可工作。它主要用于在 GPU 上进行模型训练和推理负载。
 
在硬件支持方面，DirectML 旨在与各种 GPU（包括 AMD 集成和独立 GPU、Intel 集成 GPU 和 NVIDIA 独立 GPU）一起工作。它是 Windows AI 平台的一部分，在 Windows 10 和 11 上受支持，允许在任何 Windows 设备上进行模型训练和推理。
 
与 DirectML 相关的更新和特性，包括支持多达 150 个 ONNX 操作符，以及由 ONNX 运行时和 WinML 同时使用。它得到了主要集成硬件供应商（IHV）的支持，每个供应商都实现了各种元命令（metacommands）。
 
### CUDA 
CUDA（Compute Unified Device Architecture 的缩写）是由Nvidia创建的一个并行计算平台和应用程序编程接口（API）模型。它允许软件开发人员使用支持CUDA的图形处理单元（GPU）进行通用处理，这种方法被称为GPGPU（图形处理单元上的通用计算）。CUDA是Nvidia GPU加速的关键技术，已经在机器学习、科学计算和视频处理等多个领域得到广泛应用。
 
对于CUDA的硬件支持，由于它是Nvidia开发的专有技术，因此只适用于Nvidia的GPU。每种架构都支持特定版本的CUDA工具包，为开发人员提供构建和运行CUDA应用程序所需的库和工具。
 
### ONNX 
ONNX（Open Neural Network Exchange）是一个旨在表示机器学习模型的开放格式。它提供了一个可扩展计算图模型的定义，以及内置操作符和标准数据类型的定义。ONNX允许开发人员在不同的ML框架之间移动模型，实现互操作性，使创建和部署AI应用程序变得更容易。

Phi3 mini 可以在 CPU 和 GPU 上运行 ONNX Runtime，支持跨设备，包括服务器平台、Windows、Linux 和 Mac 桌面以及移动 CPU。
我们添加的优化配置包括：
- 用于 int4 DML 的 ONNX 模型: 通过 AWQ 量化为 int4
- 用于 fp16 CUDA 的 ONNX 模型
- 用于 int4 CUDA 的 ONNX 模型: 通过 RTN 量化为 int4
- 用于 int4 CPU 和移动设备的 ONNX 模型: 通过 RTN 量化为 int4

### Llama.cpp
Llama.cpp 是一个用 C++ 编写的开源软件库。它对各种大型语言模型（LLM）进行推理，包括 Llama。在 ggml 库（一个通用张量库）的协同开发下，llama.cpp 旨在提供比原始 Python 实现更快的推理速度和更低的内存使用。它支持硬件优化、量化，并提供简单的 API 和示例。如果您对高效的 LLM 推理感兴趣，可以探索一下 llama.cpp，因为 Phi3 可以运行 Llama.cpp。

### GGUF 
GGUF（Generic Graph Update Format）是一种用于表示和更新机器学习模型的格式。它特别适用于可以在具有4-8位量化的CPU上高效运行的较小语言模型（SLM）。GGUF 对于在边缘设备上进行快速原型设计和运行模型以及在批处理任务（如 CI/CD 流水线）中运行模型具有很大的优势。
