# **在 Nvidia Jetson 中推論 Phi-3**

Nvidia Jetson 是 Nvidia 的一系列嵌入式計算板。Jetson TK1、TX1 和 TX2 型號都配備了 Nvidia 的 Tegra 處理器（或 SoC），該處理器整合了 ARM 架構中央處理單元（CPU）。Jetson 是一個低功耗系統，旨在加速機器學習應用。Nvidia Jetson 被專業開發者用來創建突破性的 AI 產品，涵蓋所有行業，也被學生和愛好者用於實踐 AI 學習和製作驚人的項目。SLM 部署在 Jetson 等邊緣設備中，這將使工業生成式 AI 應用場景的實施更加完善。

## 部署在 NVIDIA Jetson:

開發人員在自主機器人和嵌入式設備上工作時可以利用 Phi-3 Mini。Phi-3 相對較小的尺寸使其非常適合邊緣部署。在訓練過程中，參數已經過精心調整，確保回應的高準確性。

### TensorRT-LLM 優化:

NVIDIA 的 [TensorRT-LLM 函式庫](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) 優化大型語言模型推論。它支援 Phi-3 Mini 的長上下文窗口，提升吞吐量和延遲。優化包括 LongRoPE、FP8 和飛行批處理等技術。

### 可用性和部署:

開發者可以在 [NVIDIA's AI](https://www.nvidia.com/ai-data-science/generative-ai/) 探索 Phi-3 Mini 及其 128K context window。它被打包為 NVIDIA NIM，一種具有標準 API 的微服務，可以部署在任何地方。此外，還有 [TensorRT-LLM implementations on GitHub](https://github.com/NVIDIA/TensorRT-LLM)。

## **1. 準備**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. 在 Jetson 中執行 Phi-3**

我們可以選擇 [Ollama](https://ollama.com) 或 [LlamaEdge](https://llamaedge.com)

如果你想同時在雲端和邊緣設備上使用 gguf，LlamaEdge 可以理解為 WasmEdge（WasmEdge 是一個輕量、高效能、可延展的 WebAssembly 執行時，適用於雲端原生、邊緣和去中心化應用。它支援無伺服器應用、嵌入式函式、微服務、智慧合約和 IoT 設備。你可以通過 LlamaEdge 將 gguf 的定量模型部署到邊緣設備和雲端。

![llamaedge](../../../../imgs/03/Jetson/llamaedge.jpg)

以下是使用的步驟

1. 安裝和下載相關的函式庫和檔案

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**注意**: llama-api-server.wasm 和 chatbot-ui 需要在相同的目錄中

2. 在終端機中執行腳本

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

這是執行結果

![llamaedgerun](../../../../imgs/03/Jetson/llamaedgerun.png)

***範例程式碼*** [Phi-3 mini WASM Notebook 範例](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

總結來說，Phi-3 Mini 代表了語言模型的一大進步，結合了效率、上下文感知和 NVIDIA 的優化能力。無論你是在建構機器人還是邊緣應用，Phi-3 Mini 都是一個值得注意的強大工具。

