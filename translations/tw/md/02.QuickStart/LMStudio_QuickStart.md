# **在 LM Studio 中使用 Phi-3**

[LM Studio](https://lmstudio.ai) 是一款在本地桌面應用程式中調用 SLM 和 LLM 的應用程式。它讓使用者能夠輕鬆使用不同的模型，並支援使用 NVIDIA/AMD GPU/Apple Silicon 進行加速運算。透過 LM Studio，使用者可以下載、安裝和運行各種基於 Hugging Face 的開源 LLM 和 SLM，並在本地測試模型性能，無需編碼。

## **1. 安裝**

![LMStudio](../../../../translated_images/LMStudio.87422bdb03d330dc05137ba237dd0cb43f7964245b848a466ab1730de93bc4db.tw.png)

你可以選擇在 Windows、Linux 或 macOS 上通過 LM Studio 的網站 [https://lmstudio.ai/](https://lmstudio.ai/) 進行安裝。

## **2. 在 LM Studio 中下載 Phi-3**

LM Studio 調用的是量化的 gguf 格式的開源模型。你可以直接從 LM Studio 提供的平台搜索界面下載，也可以自行下載並指定在相關目錄中調用。

***我們在 LM Studio 搜索界面搜索 Phi3 並下載 Phi-3 gguf 模型***

![LMStudioSearch](../../../../translated_images/LMStudio_Search.1e577e0f69f336fc26e56653eeec2a20b90c3895cc4aa2ff05b6ec51059f12fd.tw.png)

***通過 LM Studio 管理已下載的模型***

![LMStudioLocal](../../../../translated_images/LMStudio_Local.55f9d6f61eb27f0f37fc4833599aa43fa45a66dfc20444ba1419a922b60b5005.tw.png)

## **3. 在 LM Studio 中與 Phi-3 進行聊天**

我們在 LM Studio 聊天界面中選擇 Phi-3，並設置聊天模板（Preset - Phi3）以開始與 Phi-3 進行本地聊天。

![LMStudioChat](../../../../translated_images/LMStudio_Chat.1bdc3a8f804f12d9548b386448c1642b741c10816576973155a90ef55f8a9c8d.tw.png)

***注意***：

a. 你可以通過 LM Studio 控制面板中的高級配置來設置參數。

b. 因為 Phi-3 有特定的聊天模板要求，必須在 Preset 中選擇 Phi-3。

c. 你還可以設置不同的參數，例如 GPU 使用情況等。

## **4. 從 LM Studio 調用 Phi-3 API**

LM Studio 支持快速部署本地服務，你可以在無需編碼的情況下構建模型服務。

![LMStudioServer](../../../../translated_images/LMStudio_Server.917c115e12599e7698ce323085ce4f8bdb020665656bbe90edca2d45a7de932d.tw.png)

這是在 Postman 中的結果

![LMStudioPostman](../../../../translated_images/LMStudio_Postman.4481aa4873ecaae0e05032f539090897002fc9aca9da5d1336fb28776f4c45a7.tw.png)

免責聲明：此翻譯由人工智慧模型從原文翻譯而來，可能不完美。請審查輸出並進行必要的修正。