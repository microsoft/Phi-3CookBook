# **在 Android 中推論 Phi-3**

讓我們來探索如何在 Android 裝置上進行 Phi-3-mini 的推論。Phi-3-mini 是 Microsoft 推出的一系列新模型，能夠在邊緣裝置和 IoT 裝置上部署大型語言模型（LLMs）。

## 語義核心和推論:

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) 是一個應用程式框架，允許你建立與 Azure OpenAI Service、OpenAI 模型，甚至是本地模型相容的應用程式。如果你是 Semantic Kernel 的新手，我們建議你查看 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。

### 要使用 Semantic Kernel 存取 Phi-3-mini:

你可以將它與 Semantic Kernel 中的 Hugging face Connector 結合使用。[範例程式碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)。

預設情況下，它對應於 Hugging face 上的模型 ID。不過，你也可以連接到本地建構的 Phi-3-mini 模型伺服器。

### 呼叫量化模型與 Ollama 或 LlamaEdge:

許多使用者偏好使用量化模型在本地執行模型。
[Ollama](https://ollama.com/) 和 [LlamaEdge](https://llamaedge.com) 允許個別使用者呼叫不同的量化模型：

**Ollama**

你可以直接執行 ollama run Phi-3 或通過建立一個 Modelfile 並設置 gguf 檔案的路徑來離線配置。

```
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> {{.Prompt}}<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096

```

[範例程式碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

**LlamaEdge**

如果你想在雲端和邊緣設備上同時使用 gguf，LlamaEdge 是一個很好的選擇。
[範例程式碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)

### 安裝並在 Android 手機上執行:

下載 MLC Chat 應用程式 (免費) 適用於 Android 手機。
您需要下載 APK 檔案 (148MB) 並安裝它。
啟動 MLC Chat 應用程式，您將看到 AI 模型列表，包括 Phi-3-mini。

總之，Phi-3-mini 為邊緣設備上的生成式 AI 開啟了令人興奮的可能性，您可以開始在 Android 上探索其功能。

