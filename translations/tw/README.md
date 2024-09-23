# Phi-3 食譜：使用 Microsoft 的 Phi-3 模型的實戰範例

[![在 GitHub Codespaces 中打開和使用範例](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)
[![在 Dev Containers 中打開](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

[![GitHub 貢獻者](https://img.shields.io/github/contributors/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 問題](https://img.shields.io/github/issues/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 拉取請求](https://img.shields.io/github/issues-pr/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![歡迎 PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub 觀察者](https://img.shields.io/github/watchers/microsoft/phi-3cookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phi-3cookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 分叉](https://img.shields.io/github/forks/microsoft/phi-3cookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phi-3cookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 星標](https://img.shields.io/github/stars/microsoft/phi-3cookbook?style=social&label=Star)](https://GitHub.com/microsoft/phi-3cookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI 社區 Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi 是 Microsoft 開發的一系列開放式 AI 模型。Phi 模型是目前最具能力和成本效益的小型語言模型 (SLMs)，在各種語言、推理、編碼和數學基準測試中表現優於同尺寸和下一尺寸的模型。Phi-3 系列包括迷你、小型、中型和視覺版本，根據不同參數量進行訓練，以滿足各種應用場景。關於 Microsoft Phi 系列的更多詳細信息，請訪問 [歡迎來到 Phi 家族](/md/01.Introduce/Phi3Family.md) 頁面。

![Phi3Family](/imgs/00/Phi3getstarted.png)

## 目錄

- 介紹
  - [設定您的環境](./md/01.Introduce/EnvironmentSetup.md)(✅)
  - [歡迎來到 Phi 家族](./md/01.Introduce/Phi3Family.md)(✅)
  - [了解關鍵技術](./md/01.Introduce/Understandingtech.md)(✅)
  - [Phi 模型的 AI 安全性](./md/01.Introduce/AISafety.md)(✅)
  - [Phi-3 硬體支援](./md/01.Introduce/Hardwaresupport.md)(✅)
  - [Phi-3 模型與跨平台可用性](./md/01.Introduce/Edgeandcloud.md)(✅)
  - [使用 Guidance-ai 和 Phi](./md/01.Introduce/Guidance.md)(✅)

- 快速入門
  - [在 GitHub Model Catalog 中使用 Phi-3](./md/02.QuickStart/GitHubModel_QuickStart.md)(✅)
  - [在 Hugging face 中使用 Phi-3](./md/02.QuickStart/Huggingface_QuickStart.md)(✅)
  - [使用 OpenAI SDK 使用 Phi-3](./md/02.QuickStart/OpenAISDK_Quickstart.md)(✅)
  - [使用 Http Requests 使用 Phi-3](./md/02.QuickStart/HttpAPI_QuickStart.md)(✅)
  - [在 Azure AI Studio 中使用 Phi-3](./md/02.QuickStart/AzureAIStudio_QuickStart.md)(✅)
  - [使用 Azure MaaS 或 MaaP 進行 Phi-3 模型推理](./md/02.QuickStart/AzureModel_Inference.md)(✅)
  - [在 Azure AI Studio 中將 Phi-3 模型部署為無伺服器 API](./md/02.QuickStart/AzureAIStudio_MaaS.md)(✅)
  - [在 Ollama 中使用 Phi-3](./md/02.QuickStart/Ollama_QuickStart.md)(✅)
  - [在 LM Studio 中使用 Phi-3](./md/02.QuickStart/LMStudio_QuickStart.md)(✅)
  - [在 AI Toolkit VSCode 中使用 Phi-3](./md/02.QuickStart/AITookit_QuickStart.md)(✅)
  - [使用 Phi-3 和 LiteLLM](./md/02.QuickStart/LiteLLM_QuickStart.md)(✅)
- [推論 Phi-3](./md/03.Inference/overview.md)  
  - [在 iOS 上推論 Phi-3](./md/03.Inference/iOS_Inference.md)(✅)
  - [在 Jetson 上推論 Phi-3](./md/03.Inference/Jetson_Inference.md)(✅)
  - [在 AI PC 上推論 Phi-3](./md/03.Inference/AIPC_Inference.md)(✅)
  - [使用 Apple MLX 框架推論 Phi-3](./md/03.Inference/MLX_Inference.md)(✅)
  - [在本地伺服器上推論 Phi-3](./md/03.Inference/Local_Server_Inference.md)(✅)
  - [使用 AI Toolkit 在遠端伺服器上推論 Phi-3](./md/03.Inference/Remote_Interence.md)(✅)
  - [使用 Rust 推論 Phi-3](./md/03.Inference/Rust_Inference.md)(✅)
  - [在本地推論 Phi-3-Vision](./md/03.Inference/Vision_Inference.md)(✅)
  - [使用 Kaito AKS 和 Azure Containers（官方支持）推論 Phi-3](./md/03.Inference/Kaito_Inference.md)(✅)
  - [推論您的 Fine-tuning ONNX Runtime 模型](./md/06.E2ESamples/E2E_Inference_ORT.md)(✅)

- Fine-tuning Phi-3
  - [下載和創建樣本數據集](./md/04.Fine-tuning/CreatingSampleData.md)(✅)
  - [Fine-tuning 場景](./md/04.Fine-tuning/FineTuning_Scenarios.md)(✅)
  - [Fine-tuning vs RAG](./md/04.Fine-tuning/FineTuning_vs_RAG.md)(✅)
  - [Fine-tuning 讓 Phi-3 成為行業專家](./md/04.Fine-tuning/LetPhi3gotoIndustriy.md)(✅)
  - [使用 AI Toolkit for VS Code Fine-tuning Phi-3](./md/04.Fine-tuning/Finetuning_VSCodeaitoolkit.md)(✅)
  - [使用 Azure Machine Learning Service Fine-tuning Phi-3](./md/04.Fine-tuning/Introduce_AzureML.md)(✅)
  - [使用 Lora Fine-tuning Phi-3](./md/04.Fine-tuning/FineTuning_Lora.md)(✅)
  - [使用 QLora Fine-tuning Phi-3](./md/04.Fine-tuning/FineTuning_Qlora.md)(✅)
  - [使用 Azure AI Studio Fine-tuning Phi-3](./md/04.Fine-tuning/FineTuning_AIStudio.md)(✅)
  - [使用 Azure ML CLI/SDK Fine-tuning Phi-3](./md/04.Fine-tuning/FineTuning_MLSDK.md)(✅)
  - [使用 Microsoft Olive Fine-tuning](./md/04.Fine-tuning/FineTuning_MicrosoftOlive.md)(✅)
  - [使用 Weights and Bias Fine-tuning Phi-3-vision](./md/04.Fine-tuning/FineTuning_Phi-3-visionWandB.md)(✅)
  - [使用 Apple MLX 框架 Fine-tuning Phi-3](./md/04.Fine-tuning/FineTuning_MLX.md)(✅)
  - [Fine-tuning Phi-3-vision（官方支持）](./md/04.Fine-tuning/FineTuning_Vision.md)(✅)
  - [使用 Kaito AKS 和 Azure Containers（官方支持）Fine-tuning Phi-3](./md/04.Fine-tuning/FineTuning_Kaito.md)(✅)

- 評估 Phi-3
  - [負責任 AI 介紹](./md/05.Evaluation/ResponsibleAI.md)(✅)
  - [Promptflow 介紹](./md/05.Evaluation/Promptflow.md)(✅)
  - [使用 Azure AI Studio 進行評估介紹](./md/05.Evaluation/AzureAIStudio.md)(✅)

- Phi-3-mini 的 E2E 範例
  - [端到端範例介紹](./md/06.E2ESamples/E2E_Introduction.md)(✅)
- [準備您的行業數據](./md/06.E2ESamples/E2E_Datasets.md)(✅)
  - [使用 Microsoft Olive 設計您的項目](./md/06.E2ESamples/E2E_LoRA&QLoRA_Config_With_Olive.md)(✅)
  - [在 Android 上使用 Phi-3、ONNXRuntime Mobile 和 ONNXRuntime Generate API 的本地聊天機器人](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/mobile/examples/phi-3/android)(✅)
  - [Hugging Face Space WebGPU 和 Phi-3-mini 演示 - Phi-3-mini 提供給用戶一個私密且強大的聊天機器人體驗。您可以試試](https://huggingface.co/spaces/Xenova/experimental-phi3-webgpu)(✅)
  - [在瀏覽器中使用 Phi3、ONNX Runtime Web 和 WebGPU 的本地聊天機器人](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)(✅)
  - [OpenVino 聊天](/md/06.E2ESamples/E2E_OpenVino_Chat.md)(✅)
  - [多模型 - 互動式 Phi-3-mini 和 OpenAI Whisper](./md/06.E2ESamples/E2E_Phi-3-mini_with_whisper.md)(✅)
  - [MLFlow - 構建包裝器並使用 MLFlow 的 Phi-3](./md/06.E2ESamples/E2E_Phi-3-MLflow.md)(✅)
  - [模型優化 - 如何使用 Olive 優化 ONNX Runtime Web 的 Phi-3-min 模型](https://github.com/microsoft/Olive/tree/main/examples/phi3)(✅)
  - [WinUI3 應用程序與 Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)(✅)
  - [WinUI3 多模型 AI 驅動的筆記應用示例](https://github.com/microsoft/ai-powered-notes-winui3-sample)(✅)
  - [微調和集成自定義 Phi-3 模型與 Prompt flow](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)(✅)
  - [在 Azure AI Studio 中微調和集成自定義 Phi-3 模型與 Prompt flow](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIstudio.md)(✅)
  - [Phi-3.5-mini-instruct 語言預測示例（中文/英文）](../../code/09.UpdateSamples/Aug/phi3-instruct-demo.ipynb)(✅)

- Phi-3-vision 的端到端示例
  - [Phi-3-vision-圖像文字轉文字](../../code/06.E2E/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)(✅)
  - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Phi-3-vision CLIP 嵌入](./md/06.E2ESamples/E2E_Phi-3-Embedding_Images_with_CLIPVision.md)(✅)
  - [演示：Phi-3 回收](https://github.com/jennifermarsman/PhiRecycling/)(✅)
  - [Phi-3-vision - 使用 Phi3-Vision 和 OpenVINO 的視覺語言助手](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)(✅)
  - [Phi-3 Vision Nvidia NIM](/md/06.E2ESamples/E2E_Nvidia_NIM_Vision.md)(✅)
  - [Phi-3 Vision OpenVino](/md/06.E2ESamples/E2E_OpenVino_Phi3Vision.md)(✅)
  - [Phi-3.5 Vision 多幀或多圖像示例](../../code/09.UpdateSamples/Aug/phi3-vision-demo.ipynb)(✅)

- Phi-3.5-MoE 的端到端示例
  - [Phi-3.5 專家混合模型（MoEs）社交媒體示例](../../code/09.UpdateSamples/Aug/phi3_moe_demo.ipynb)(✅)
  - [構建一個基於檢索增強生成（RAG）管道，使用 NVIDIA NIM Phi-3 MOE、Azure AI Search 和 LlamaIndex](https://github.com/farzad528/azure-ai-search-python-playground/blob/main/azure-ai-search-nvidia-rag.ipynb)(✅)

- Phi-3 的實驗室和工作坊示例
  - [C# .NET 實驗室](./md/07.Labs/Csharp/csharplabs.md)(✅)
  - [使用 Microsoft Phi-3 家族構建您自己的 Visual Studio Code GitHub Copilot 聊天](./md/07.Labs/VSCode/README.md)(✅)
  - [本地 WebGPU Phi-3 Mini RAG 聊天機器人示例與本地 RAG 文件](./code/08.RAG/rag_webgpu_chat/README.md)(✅)
  - [Phi-3 ONNX 教程](https://onnxruntime.ai/docs/genai/tutorials/phi3-python.html)(✅)
  - [Phi-3-vision ONNX 教程](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [使用 ONNX Runtime generate() API 運行 Phi-3 模型](https://github.com/microsoft/onnxruntime-genai/blob/main/examples/python/phi-3-tutorial.md)(✅)
- [Phi-3 ONNX 多模型 LLM 聊天 UI，這是一個聊天演示](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/chat_app)(✅)
  - [C# Hello Phi-3 ONNX 範例 Phi-3](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi)(✅)
  - [C# API Phi-3 ONNX 範例，支援 Phi3-Vision](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi3V)(✅)
  - [在 CodeSpace 中運行 C# Phi-3 範例](./md/07.Labs/CsharpOllamaCodeSpaces/CsharpOllamaCodeSpaces.md)(✅)
  - [使用 Phi-3 與 Promptflow 和 Azure AI Search](./code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md)(✅)
  - [Windows AI-PC APIs 與 Windows Copilot Library](https://developer.microsoft.com/windows/ai/?WT.mc_id=aiml-137032-kinfeylo)

- 學習 Phi-3.5
  - [Phi-3.5 系列的新功能](./md/08.Update/Phi35/010.WhatsNewInPhi35.md)(✅)
  - [量化 Phi-3.5 系列](./md/08.Update/Phi35/020.QuantifyingPhi35.md)(✅)
    - [使用 llama.cpp 量化 Phi-3.5](./md/08.Update/Phi35/021.UsingLlamacppQuantifyingPhi35.md)(✅)
    - [使用 onnxruntime 的生成式 AI 擴展量化 Phi-3.5](./md/08.Update/Phi35/022.UsingORTGenAIQuantifyingPhi35.md)(✅)
    - [使用 Intel OpenVINO 量化 Phi-3.5](./md/08.Update/Phi35/023.UsingIntelOpenVINOQuantifyingPhi35.md)(✅)
    - [使用 Apple MLX 框架量化 Phi-3.5](./md/08.Update/Phi35/024.UsingAppleMLXQuantifyingPhi35.md)(✅)
  - Phi-3.5 應用範例
    - [Phi-3.5-Instruct WebGPU RAG 聊天機器人](./md/08.Update/Phi35/031.WebGPUWithPhi35Readme.md)(✅)
    - [使用 Phi-3.5 與 GitHub Models 創建您自己的 Visual Studio Code 聊天助手代理](./md/08.Update/Phi35/032.CreateVSCodeChatAgentWithGitHubModels.md)(✅)


## 使用 Phi-3 模型

### Phi-3 在 Azure AI Studio 上

您可以學習如何使用 Microsoft Phi-3 以及如何在不同硬件設備上構建端到端解決方案。要親自體驗 Phi-3，首先可以使用 [Azure AI Studio, Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) 來測試模型並自定義 Phi-3 以適應您的場景。更多資訊請參考 [Azure AI Studio 快速入門](/md/02.QuickStart/AzureAIStudio_QuickStart.md)

**操作台**
每個模型都有專用的操作台來測試模型 [Azure AI Playground](https://aka.ms/try-phi3)。

### Phi-3 在 GitHub Models 上

您可以學習如何使用 Microsoft Phi-3 以及如何在不同硬件設備上構建端到端解決方案。要親自體驗 Phi-3，首先可以使用 [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) 來測試模型並自定義 Phi-3 以適應您的場景。更多資訊請參考 [GitHub Model Catalog 快速入門](/md/02.QuickStart/GitHubModel_QuickStart.md)

**操作台**
每個模型都有專用的 [操作台來測試模型](/md/02.QuickStart/GitHubModel_QuickStart.md)。

### Phi-3 在 Hugging Face 上

您也可以在 [Hugging Face](https://huggingface.co/microsoft) 上找到該模型

**操作台**
 [Hugging Chat 操作台](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🌐 多語言支持

> **Note:**
> 這些翻譯是使用開源的 [co-op-translator](https://github.com/Azure/co-op-translator) 自動生成的，可能包含錯誤或不準確之處。對於重要資訊，建議參考原文或諮詢專業的人工翻譯。如果您希望添加或更新翻譯，請參考 [co-op-translator](https://github.com/Azure/co-op-translator) 儲存庫，您可以通過簡單的命令輕鬆貢獻。

| 語言                  | 代碼 | 連結到翻譯的 README                               | 最後更新日期 |
|----------------------|------|---------------------------------------------------|--------------|
| 中文（簡體）         | zh   | [中文翻譯](../zh/README.md)           | 2024-09-21   |
| 中文（繁體）         | tw   | [中文翻譯](./README.md)           | 2024-09-21   |
| 法語                 | fr   | [法語翻譯](../fr/README.md)           | 2024-09-21   |
| 日語                 | ja   | [日語翻譯](../ja/README.md)           | 2024-09-21   |
| 韓語                 | ko   | [韓語翻譯](../ko/README.md)           | 2024-09-21   |
| 西班牙語             | es   | [西班牙語翻譯](../es/README.md)       | 2024-09-21   |

## 商標

這個專案可能包含專案、產品或服務的商標或標誌。授權使用 Microsoft 商標或標誌必須遵循 [Microsoft 的商標和品牌指南](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)。
在修改版本的這個專案中使用 Microsoft 商標或標誌，不得引起混淆或暗示 Microsoft 的贊助。任何使用第三方商標或標誌都必須遵循第三方的政策。

免責聲明：此翻譯由AI模型從原文翻譯而來，可能不夠完美。請檢查輸出並進行必要的修正。