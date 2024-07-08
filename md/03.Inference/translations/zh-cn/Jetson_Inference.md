# **在 Nvidia Jetson 上使用 Phi-3 进行推理**

Nvidia Jetson 是一系列来自 Nvidia 的嵌入式计算板。Jetson TK1、TX1 和 TX2 型号都搭载了一款集成了 ARM 架构中央处理器（CPU）的 Nvidia Tegra 处理器（或 SoC）。Jetson 是一个低功耗系统，专为加速机器学习应用而设计。Nvidia Jetson 被专业开发者用于在各个行业创造突破性的人工智能产品，同时也被学生和爱好者用于动手学习人工智能并制作令人惊叹的项目。SLM 被部署在 Jetson 等边缘设备上，将更好地实现工业生成式人工智能应用场景的实施。

## 部署在 NVIDIA Jetson 平台:
从事自主机器人和嵌入式设备开发的开发者可以利用 Phi-3 Mini。Phi-3 的相对较小尺寸使其非常适合边缘部署。在训练过程中，参数经过精细调整，确保响应具有高度准确性。

### TensorRT-LLM 优化:
NVIDIA的[TensorRT-LLM 库](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) 优化了大型语言模型推理。它支持 Phi-3 Mini 的长上下文窗口，提高了吞吐量和延迟性能。优化技术包括 LongRoPE、FP8 和在途批处理等方法。

### 可用性和开发:
开发者可以在[NVIDIA's AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/)上探索具有 128K 上下文窗口的 Phi-3 Mini。它被打包成 NVIDIA NIM，一个具有标准 API 的微服务，可以在任何地方部署。此外，TensorRT-LLM 的实现也可以在 GitHub 上找到 [TensorRT-LLM implementations on GitHub](https://github.com/NVIDIA/TensorRT-LLM)。


 ## **1. 准备**


a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+
   
c. Cuda 11.8
   
d. Python 3.8+

 ## **2. 在 Jetson 中运行Phi-3**

我们可以选择 [Ollama](https://ollama.com) 或者 [LlamaEdge](https://llamaedge.com)。

如果您想同时在云端和边缘设备上使用 gguf，LlamaEdge 可以被理解为 WasmEdge（WasmEdge 是一款轻量级、高性能、可扩展的 WebAssembly 运行时，适用于云原生、边缘和去中心化的应用。它支持无服务器应用、嵌入式函数、微服务、智能合约和物联网设备）。通过 LlamaEdge，您可以将 gguf 的量化模型部署到边缘设备和云端。

![llamaedge](../../../../imgs/03/Jetson/llamaedge.jpg)

下面是使用的步骤：

1. 下载和安装相关的库和文件

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**注意**: llama-api-server.wasm 和 chatbot-ui 需要放置在相同的路径下。

2. 在终端运行以下脚本


```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

以下是运行结果的示意图。


![llamaedgerun](../../../../imgs/03/Jetson/llamaedgerun.png)

***示例代码*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

总之，Phi-3 Mini 在语言建模方面取得了重大突破，它将效率、上下文感知能力和 NVIDIA 的优化技巧相结合。无论您是在构建机器人还是边缘应用，Phi-3 Mini 都是一个值得关注的强大工具。