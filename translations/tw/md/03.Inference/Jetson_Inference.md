# **在 Nvidia Jetson 上推理 Phi-3**

Nvidia Jetson 是 Nvidia 推出的嵌入式計算板系列。Jetson TK1、TX1 和 TX2 型號都搭載了來自 Nvidia 的 Tegra 處理器（或 SoC），整合了 ARM 架構的中央處理單元（CPU）。Jetson 是一個低功耗系統，設計用於加速機器學習應用。Nvidia Jetson 被專業開發者用於創造各行業的突破性 AI 產品，也被學生和愛好者用於實踐 AI 學習和製作驚人的項目。SLM 被部署在如 Jetson 這樣的邊緣設備中，這將促進工業生成式 AI 應用場景的更好實現。

## 在 NVIDIA Jetson 上部署：
從事自主機器人和嵌入式設備的開發者可以利用 Phi-3 Mini。Phi-3 相對較小的尺寸使其非常適合邊緣部署。參數在訓練過程中經過精心調整，確保高精度的響應。

### TensorRT-LLM 優化：
NVIDIA 的 [TensorRT-LLM 庫](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) 優化了大語言模型推理。它支持 Phi-3 Mini 的長上下文窗口，提高了吞吐量和延遲。優化技術包括 LongRoPE、FP8 和 inflight batching。

### 可用性和部署：
開發者可以在 [NVIDIA 的 AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/) 上探索具有 128K 上下文窗口的 Phi-3 Mini。它打包為 NVIDIA NIM，一種具有標準 API 的微服務，可以部署在任何地方。此外，還有 [GitHub 上的 TensorRT-LLM 實現](https://github.com/NVIDIA/TensorRT-LLM)。

## **1. 準備**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+
   
c. Cuda 11.8
   
d. Python 3.8+

## **2. 在 Jetson 上運行 Phi-3**

我們可以選擇 [Ollama](https://ollama.com) 或 [LlamaEdge](https://llamaedge.com)

如果你想同時在雲端和邊緣設備上使用 gguf，LlamaEdge 可以理解為 WasmEdge（WasmEdge 是一個輕量、高性能、可擴展的 WebAssembly 運行時，適合雲原生、邊緣和去中心化應用。它支持無伺服器應用、嵌入式功能、微服務、智能合約和物聯網設備。你可以通過 LlamaEdge 將 gguf 的定量模型部署到邊緣設備和雲端。

![llamaedge](../../../../translated_images/llamaedge.d1314f30755868575f55e27125fdd9838b6962e3bce66c9bd21eaffebfcf57b9.tw.jpg)

以下是使用步驟

1. 安裝並下載相關庫和文件

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**注意**: llama-api-server.wasm 和 chatbot-ui 需要在同一目錄下

2. 在終端中運行腳本

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

這是運行結果

![llamaedgerun](../../../../translated_images/llamaedgerun.fcb0c81257035c00b2a9ec7d2f541d64f9f357eec4adf45f5c951c4c06cd1df9.tw.png)

***示例代碼*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

總結來說，Phi-3 Mini 代表了語言建模的一次飛躍，結合了效率、上下文感知和 NVIDIA 的優化能力。無論你是在構建機器人還是邊緣應用，Phi-3 Mini 都是一個值得關注的強大工具。

免責聲明：此翻譯由人工智慧模型從原文翻譯而來，可能不完美。
請檢查輸出並進行任何必要的修正。