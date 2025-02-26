# **Inference Phi-3 in Nvidia Jetson**

Nvidia Jetson is a series of embedded computing boards from Nvidia. The Jetson TK1, TX1 and TX2 models all carry a Tegra processor (or SoC) from Nvidia that integrates an ARM architecture central processing unit (CPU). Jetson is a low-power system and is designed for accelerating machine learning applications.Nvidia Jetson is used by professional developers to create breakthrough AI products across all industries, and by students and enthusiasts for hands-on AI learning and making amazing projects.SLM is deployed in edge devices such as Jetson, which will enable better implementation of industrial generative AI application scenarios.

## Deployment on NVIDIA Jetson:
Developers working on autonomous robotics and embedded devices can leverage Phi-3 Mini. Phi-3 relatively small size makes it ideal for edge deployment. Parameters have been meticulously tuned during training, ensuring high accuracy in responses.

### TensorRT-LLM Optimization:
NVIDIA's [TensorRT-LLM library](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) optimizes large language model inference. It supports Phi-3 Mini's long context window, enhancing both throughput and latency. Optimizations include techniques like LongRoPE, FP8, and inflight batching.

### Availability and Deployment:
Developers can explore Phi-3 Mini with the 128K context window at [NVIDIA's AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). It's packaged as an NVIDIA NIM, a microservice with a standard API that can be deployed anywhere. Additionally, the [TensorRT-LLM implementations on GitHub](https://github.com/NVIDIA/TensorRT-LLM).


 ## **1. Preparation**


a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+
   
c. Cuda 11.8
   
d. Python 3.8+

 ## **2. Running Phi-3 in Jetson**

 We can choose [Ollama](https://ollama.com) or [LlamaEdge](https://llamaedge.com)

 If you want to use gguf in the cloud and edge devices at the same time, LlamaEdge can be understood as WasmEdge (WasmEdge is a lightweight, high-performance, scalable WebAssembly runtime suitable for cloud native, edge and decentralized applications. It supports serverless applications, embedded functions, microservices, smart contracts and IoT devices. You can deploy gguf's quantitative model to edge devices and the cloud through LlamaEdge.

![llamaedge](../../../imgs/01/03/Jetson/llamaedge.jpg)

Here are the steps to use 

1. Install and download related libraries and files

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Note**: llama-api-server.wasm and chatbot-ui need to be in the same directory

2. Run scripts in terminal


```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Here is the running result


![llamaedgerun](../../../imgs/01/03/Jetson/llamaedgerun.png)

***Sample code*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

In summary, Phi-3 Mini represents a leap forward in language modeling, combining efficiency, context awareness, and NVIDIA's optimization prowess. Whether you're building robots or edge applications, Phi-3 Mini is a powerful tool to be aware of. 
