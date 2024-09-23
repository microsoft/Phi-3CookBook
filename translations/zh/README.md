# Phi-3 烹饪手册：微软Phi-3模型的实战示例

[![在GitHub Codespaces中打开并使用示例](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)
[![在Dev Containers中打开](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

[![GitHub贡献者](https://img.shields.io/github/contributors/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub问题](https://img.shields.io/github/issues/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub拉取请求](https://img.shields.io/github/issues-pr/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![欢迎PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub关注者](https://img.shields.io/github/watchers/microsoft/phi-3cookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phi-3cookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub分叉](https://img.shields.io/github/forks/microsoft/phi-3cookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phi-3cookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub星标](https://img.shields.io/github/stars/microsoft/phi-3cookbook?style=social&label=Star)](https://GitHub.com/microsoft/phi-3cookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi是微软开发的一系列开源AI模型。Phi模型是目前最强大且成本效益最高的小型语言模型（SLMs），在多种语言、推理、编码和数学基准测试中表现优于同等大小和更大尺寸的模型。Phi-3系列包括迷你、小型、中型和视觉版本，基于不同的参数量进行训练，以满足各种应用场景。有关微软Phi系列的更多详细信息，请访问[欢迎来到Phi家族](/md/01.Introduce/Phi3Family.md)页面。

![Phi3Family](/imgs/00/Phi3getstarted.png)

## 目录

- 介绍
  - [设置你的环境](./md/01.Introduce/EnvironmentSetup.md)(✅)
  - [欢迎来到Phi家族](./md/01.Introduce/Phi3Family.md)(✅)
  - [了解关键技术](./md/01.Introduce/Understandingtech.md)(✅)
  - [Phi模型的AI安全](./md/01.Introduce/AISafety.md)(✅)
  - [Phi-3硬件支持](./md/01.Introduce/Hardwaresupport.md)(✅)
  - [Phi-3模型及其在各平台的可用性](./md/01.Introduce/Edgeandcloud.md)(✅)
  - [使用Guidance-ai和Phi](./md/01.Introduce/Guidance.md)(✅)

- 快速开始
  - [在GitHub模型目录中使用Phi-3](./md/02.QuickStart/GitHubModel_QuickStart.md)(✅)
  - [在Hugging face中使用Phi-3](./md/02.QuickStart/Huggingface_QuickStart.md)(✅)
  - [使用OpenAI SDK与Phi-3](./md/02.QuickStart/OpenAISDK_Quickstart.md)(✅)
  - [使用Http请求与Phi-3](./md/02.QuickStart/HttpAPI_QuickStart.md)(✅)
  - [在Azure AI Studio中使用Phi-3](./md/02.QuickStart/AzureAIStudio_QuickStart.md)(✅)
  - [使用Azure MaaS或MaaP进行Phi-3模型推理](./md/02.QuickStart/AzureModel_Inference.md)(✅)
  - [在Azure AI Studio中将Phi-3模型部署为无服务器API](./md/02.QuickStart/AzureAIStudio_MaaS.md)(✅)
  - [在Ollama中使用Phi-3](./md/02.QuickStart/Ollama_QuickStart.md)(✅)
  - [在LM Studio中使用Phi-3](./md/02.QuickStart/LMStudio_QuickStart.md)(✅)
  - [在AI Toolkit VSCode中使用Phi-3](./md/02.QuickStart/AITookit_QuickStart.md)(✅)
  - [使用Phi-3和LiteLLM](./md/02.QuickStart/LiteLLM_QuickStart.md)(✅)
- [Phi-3推理](./md/03.Inference/overview.md)  
  - [在iOS上进行Phi-3推理](./md/03.Inference/iOS_Inference.md)(✅)
  - [在Jetson上进行Phi-3推理](./md/03.Inference/Jetson_Inference.md)(✅)
  - [在AI PC上进行Phi-3推理](./md/03.Inference/AIPC_Inference.md)(✅)
  - [使用Apple MLX Framework进行Phi-3推理](./md/03.Inference/MLX_Inference.md)(✅)
  - [在本地服务器上进行Phi-3推理](./md/03.Inference/Local_Server_Inference.md)(✅)
  - [使用AI Toolkit在远程服务器上进行Phi-3推理](./md/03.Inference/Remote_Interence.md)(✅)
  - [使用Rust进行Phi-3推理](./md/03.Inference/Rust_Inference.md)(✅)
  - [在本地进行Phi-3-Vision推理](./md/03.Inference/Vision_Inference.md)(✅)
  - [使用Kaito AKS、Azure Containers（官方支持）进行Phi-3推理](./md/03.Inference/Kaito_Inference.md)(✅)
  - [推理您微调的ONNX Runtime模型](./md/06.E2ESamples/E2E_Inference_ORT.md)(✅)

- Phi-3微调
  - [下载并创建示例数据集](./md/04.Fine-tuning/CreatingSampleData.md)(✅)
  - [微调场景](./md/04.Fine-tuning/FineTuning_Scenarios.md)(✅)
  - [微调与RAG](./md/04.Fine-tuning/FineTuning_vs_RAG.md)(✅)
  - [微调使Phi-3成为行业专家](./md/04.Fine-tuning/LetPhi3gotoIndustriy.md)(✅)
  - [使用VS Code的AI Toolkit微调Phi-3](./md/04.Fine-tuning/Finetuning_VSCodeaitoolkit.md)(✅)
  - [使用Azure Machine Learning Service微调Phi-3](./md/04.Fine-tuning/Introduce_AzureML.md)(✅)
  - [使用Lora微调Phi-3](./md/04.Fine-tuning/FineTuning_Lora.md)(✅)
  - [使用QLora微调Phi-3](./md/04.Fine-tuning/FineTuning_Qlora.md)(✅)
  - [使用Azure AI Studio微调Phi-3](./md/04.Fine-tuning/FineTuning_AIStudio.md)(✅)
  - [使用Azure ML CLI/SDK微调Phi-3](./md/04.Fine-tuning/FineTuning_MLSDK.md)(✅)
  - [使用Microsoft Olive微调](./md/04.Fine-tuning/FineTuning_MicrosoftOlive.md)(✅)
  - [使用Weights and Bias微调Phi-3-vision](./md/04.Fine-tuning/FineTuning_Phi-3-visionWandB.md)(✅)
  - [使用Apple MLX Framework微调Phi-3](./md/04.Fine-tuning/FineTuning_MLX.md)(✅)
  - [微调Phi-3-vision（官方支持）](./md/04.Fine-tuning/FineTuning_Vision.md)(✅)
  - [使用Kaito AKS、Azure Containers（官方支持）微调Phi-3](./md/04.Fine-tuning/FineTuning_Kaito.md)(✅)

- Phi-3评估
  - [负责任的AI简介](./md/05.Evaluation/ResponsibleAI.md)(✅)
  - [Promptflow简介](./md/05.Evaluation/Promptflow.md)(✅)
  - [Azure AI Studio评估简介](./md/05.Evaluation/AzureAIStudio.md)(✅)

- Phi-3-mini的端到端示例
  - [端到端示例简介](./md/06.E2ESamples/E2E_Introduction.md)(✅)
- [准备您的行业数据](./md/06.E2ESamples/E2E_Datasets.md)(✅)
  - [使用 Microsoft Olive 构建您的项目架构](./md/06.E2ESamples/E2E_LoRA&QLoRA_Config_With_Olive.md)(✅)
  - [在 Android 上使用 Phi-3、ONNXRuntime Mobile 和 ONNXRuntime Generate API 本地聊天机器人](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/mobile/examples/phi-3/android)(✅)
  - [Hugging Face Space WebGPU 和 Phi-3-mini 演示 - Phi-3-mini 为用户提供私人（且强大的）聊天机器人体验。您可以试试](https://huggingface.co/spaces/Xenova/experimental-phi3-webgpu)(✅)
  - [在浏览器中使用 Phi3、ONNX Runtime Web 和 WebGPU 本地聊天机器人](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)(✅)
  - [OpenVino 聊天](/md/06.E2ESamples/E2E_OpenVino_Chat.md)(✅)
  - [多模型 - 交互式 Phi-3-mini 和 OpenAI Whisper](./md/06.E2ESamples/E2E_Phi-3-mini_with_whisper.md)(✅)
  - [MLFlow - 构建包装器并使用 MLFlow 的 Phi-3](./md/06.E2ESamples/E2E_Phi-3-MLflow.md)(✅)
  - [模型优化 - 如何使用 Olive 优化 ONNX Runtime Web 的 Phi-3-min 模型](https://github.com/microsoft/Olive/tree/main/examples/phi3)(✅)
  - [带有 Phi-3 mini-4k-instruct-onnx 的 WinUI3 应用](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)(✅)
  - [WinUI3 多模型 AI 驱动的笔记应用示例](https://github.com/microsoft/ai-powered-notes-winui3-sample)(✅)
  - [使用 Prompt flow 微调和集成自定义 Phi-3 模型](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)(✅)
  - [在 Azure AI Studio 中使用 Prompt flow 微调和集成自定义 Phi-3 模型](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIstudio.md)(✅)
  - [Phi-3.5-mini-instruct 语言预测示例（中文/英文）](../../code/09.UpdateSamples/Aug/phi3-instruct-demo.ipynb)(✅)

- Phi-3-vision 的端到端示例
  - [Phi-3-vision-图像文本到文本](../../code/06.E2E/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)(✅)
  - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Phi-3-vision CLIP 嵌入](./md/06.E2ESamples/E2E_Phi-3-Embedding_Images_with_CLIPVision.md)(✅)
  - [演示：Phi-3 回收](https://github.com/jennifermarsman/PhiRecycling/)(✅)
  - [Phi-3-vision - 使用 Phi3-Vision 和 OpenVINO 的视觉语言助手](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)(✅)
  - [Phi-3 Vision Nvidia NIM](/md/06.E2ESamples/E2E_Nvidia_NIM_Vision.md)(✅)
  - [Phi-3 Vision OpenVino](/md/06.E2ESamples/E2E_OpenVino_Phi3Vision.md)(✅)
  - [Phi-3.5 Vision 多帧或多图像示例](../../code/09.UpdateSamples/Aug/phi3-vision-demo.ipynb)(✅)

- Phi-3.5-MoE 的端到端示例
  - [Phi-3.5 专家模型混合 (MoEs) 社交媒体示例](../../code/09.UpdateSamples/Aug/phi3_moe_demo.ipynb)(✅)
  - [使用 NVIDIA NIM Phi-3 MOE、Azure AI 搜索和 LlamaIndex 构建检索增强生成 (RAG) 管道](https://github.com/farzad528/azure-ai-search-python-playground/blob/main/azure-ai-search-nvidia-rag.ipynb)(✅)

- Phi-3 的实验室和工作坊示例
  - [C# .NET 实验室](./md/07.Labs/Csharp/csharplabs.md)(✅)
  - [使用 Microsoft Phi-3 系列构建您自己的 Visual Studio Code GitHub Copilot Chat](./md/07.Labs/VSCode/README.md)(✅)
  - [带有本地 RAG 文件的本地 WebGPU Phi-3 Mini RAG 聊天机器人示例](./code/08.RAG/rag_webgpu_chat/README.md)(✅)
  - [Phi-3 ONNX 教程](https://onnxruntime.ai/docs/genai/tutorials/phi3-python.html)(✅)
  - [Phi-3-vision ONNX 教程](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [使用 ONNX Runtime generate() API 运行 Phi-3 模型](https://github.com/microsoft/onnxruntime-genai/blob/main/examples/python/phi-3-tutorial.md)(✅)
- [Phi-3 ONNX 多模型 LLM 聊天 UI，这是一个聊天演示](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/chat_app)(✅)
  - [C# Hello Phi-3 ONNX 示例 Phi-3](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi)(✅)
  - [C# API Phi-3 ONNX 示例，支持 Phi3-Vision](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi3V)(✅)
  - [在 CodeSpace 中运行 C# Phi-3 示例](./md/07.Labs/CsharpOllamaCodeSpaces/CsharpOllamaCodeSpaces.md)(✅)
  - [使用 Phi-3 与 Promptflow 和 Azure AI 搜索](./code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md)(✅)
  - [使用 Windows AI-PC API 和 Windows Copilot 库](https://developer.microsoft.com/windows/ai/?WT.mc_id=aiml-137032-kinfeylo)

- 学习 Phi-3.5
  - [Phi-3.5 家族的新功能](./md/08.Update/Phi35/010.WhatsNewInPhi35.md)(✅)
  - [量化 Phi-3.5 家族](./md/08.Update/Phi35/020.QuantifyingPhi35.md)(✅)
    - [使用 llama.cpp 量化 Phi-3.5](./md/08.Update/Phi35/021.UsingLlamacppQuantifyingPhi35.md)(✅)
    - [使用 ONNXRuntime 的生成 AI 扩展量化 Phi-3.5](./md/08.Update/Phi35/022.UsingORTGenAIQuantifyingPhi35.md)(✅)
    - [使用 Intel OpenVINO 量化 Phi-3.5](./md/08.Update/Phi35/023.UsingIntelOpenVINOQuantifyingPhi35.md)(✅)
    - [使用 Apple MLX 框架量化 Phi-3.5](./md/08.Update/Phi35/024.UsingAppleMLXQuantifyingPhi35.md)(✅)
  - Phi-3.5 应用示例
    - [Phi-3.5-Instruct WebGPU RAG 聊天机器人](./md/08.Update/Phi35/031.WebGPUWithPhi35Readme.md)(✅)
    - [使用 GitHub 模型创建你自己的 Visual Studio Code 聊天 Copilot 代理](./md/08.Update/Phi35/032.CreateVSCodeChatAgentWithGitHubModels.md)(✅)

## 使用 Phi-3 模型

### 在 Azure AI Studio 上使用 Phi-3

你可以学习如何使用 Microsoft Phi-3 并在不同硬件设备上构建 E2E 解决方案。要亲自体验 Phi-3，可以从使用 [Azure AI Studio, Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) 自定义 Phi-3 的场景开始。更多信息请参见 [Azure AI Studio 快速入门](/md/02.QuickStart/AzureAIStudio_QuickStart.md)。

**Playground**
每个模型都有一个专用的测试区 [Azure AI Playground](https://aka.ms/try-phi3)。

### 在 GitHub 模型上使用 Phi-3

你可以学习如何使用 Microsoft Phi-3 并在不同硬件设备上构建 E2E 解决方案。要亲自体验 Phi-3，可以从使用 [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) 自定义 Phi-3 的场景开始。更多信息请参见 [GitHub Model Catalog 快速入门](/md/02.QuickStart/GitHubModel_QuickStart.md)。

**Playground**
每个模型都有一个专用的 [测试区](/md/02.QuickStart/GitHubModel_QuickStart.md)。

### 在 Hugging Face 上使用 Phi-3

你也可以在 [Hugging Face](https://huggingface.co/microsoft) 上找到模型。

**Playground**
 [Hugging Chat 测试区](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)。

## 🌐 多语言支持

> **Note:**
> 这些翻译是使用开源的 [co-op-translator](https://github.com/Azure/co-op-translator) 自动生成的，可能包含错误或不准确之处。对于重要信息，建议参考原文或咨询专业人类翻译。如果你想添加或更新翻译，请参阅 [co-op-translator](https://github.com/Azure/co-op-translator) 仓库，你可以通过简单的命令轻松贡献。

| 语言                 | 代码 | 链接到翻译后的 README                                   | 最后更新      |
|----------------------|------|---------------------------------------------------------|--------------|
| 中文（简体）         | zh   | [中文翻译](./README.md)                 | 2024-09-21   |
| 中文（繁体）         | tw   | [中文翻译](../tw/README.md)              | 2024-09-21   |
| 法语                 | fr   | [法语翻译](../fr/README.md)                 | 2024-09-21   |
| 日语                 | ja   | [日语翻译](../ja/README.md)                 | 2024-09-21   |
| 韩语                 | ko   | [韩语翻译](../ko/README.md)                 | 2024-09-21   |
| 西班牙语             | es   | [西班牙语翻译](../es/README.md)             | 2024-09-21   |

## 商标

本项目可能包含项目、产品或服务的商标或标志。使用 Microsoft 商标或标志必须遵循 [Microsoft 的商标和品牌指南](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)。在修改版本的项目中使用 Microsoft 商标或标志不得引起混淆或暗示 Microsoft 的赞助。任何第三方商标或标志的使用均需遵循相应第三方的政策。

免责声明：此翻译由AI模型从原文翻译而来，可能不完全准确。请审阅输出内容并进行必要的修改。