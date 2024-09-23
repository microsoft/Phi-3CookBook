# **在本地伺服器上進行 Phi-3 推理**

我們可以在本地伺服器上部署 Phi-3。用戶可以選擇 [Ollama](https://ollama.com) 或 [LM Studio](https://llamaedge.com) 的解決方案，也可以編寫自己的代碼。您可以通過 [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) 或 [Langchain](https://www.langchain.com/) 來連接 Phi-3 的本地服務，從而構建 Copilot 應用程式。

## **使用 Semantic Kernel 訪問 Phi-3-mini**

在 Copilot 應用程式中，我們通過 Semantic Kernel / LangChain 來創建應用程式。這種類型的應用程式框架通常與 Azure OpenAI Service / OpenAI 模型兼容，也可以支持 Hugging Face 上的開源模型和本地模型。如果我們想使用 Semantic Kernel 訪問 Phi-3-mini 該怎麼辦？以 .NET 為例，我們可以將其與 Semantic Kernel 中的 Hugging Face Connector 結合使用。預設情況下，它可以對應 Hugging Face 上的模型 id（第一次使用時，模型將從 Hugging Face 下載，這需要較長時間）。您也可以連接到自建的本地服務。相比之下，我們建議使用後者，因為它具有更高的自主性，特別是在企業應用中。

![sk](../../../../translated_images/sk.fc8f38bb6ac491315099aa29a2704de109fc0b052448c9bc3d7c02586c196ca4.tw.png)

從圖中可以看出，通過 Semantic Kernel 訪問本地服務，可以輕鬆連接到自建的 Phi-3-mini 模型伺服器。以下是運行結果

![skrun](../../../../translated_images/skrun.f579fcb28592ba4644af8b578e66fb01923bf032b670cef44874c6550e85876d.tw.png)

***範例代碼*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

