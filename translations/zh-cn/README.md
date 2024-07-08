# 欢迎来到 Microsoft Phi-3 Cookbook

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phi-3cookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phi-3cookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phi-3cookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phi-3cookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phi-3cookbook?style=social&label=Star)](https://GitHub.com/microsoft/phi-3cookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi-3是微软开发的一系列开放AI模型。Phi-3模型是目前性能最优越、性价比最高的小型语言模型（SLM），在各种语言、推理、编程和数学基准测试中表现优于同等和更大规模的模型。这是一本关于如何使用微软Phi-3系列的手册。

![Phi3Family](/imgs/00/Phi3getstarted.png)

## Microsoft 的 Phi-3 家族

Phi-3模型在关键基准测试中明显优于同等和更大规模的语言模型（参见下方基准测试数据，数值越高越好）。Phi-3-mini比规模两倍大的模型表现更好，Phi-3-small和Phi-3-medium在很多方面优于更大的模型，包括GPT-3.5T。

所有报告中的数据都是使用相同的流程生成的，以确保数据具有可比性。因此，这些数据可能会因评估方法的细微差异而与其他已发布数据不同。有关基准测试的更多详细信息，请参阅我们的技术论文。

### Phi-3-mini

Phi-3-mini 是一个拥有 38 亿参数的语言模型，可以通过以下途径获得 [Microsoft Azure AI Studio](https://aka.ms/phi3-azure-ai), [Hugging Face](https://huggingface.co/collections/microsoft/phi-3-6626e15e9585a200d2d761e3), 和 [Ollama](https://ollama.com/library/phi3).

### Phi-3-small

仅有70亿参数的Phi-3-small在各种语言、推理、编程和数学基准测试中击败了GPT-3.5T。

![phimodelsmall](/imgs/00/phi3small.png)

### Phi-3-midium

拥有140亿参数的Phi-3-medium延续了这一趋势，其表现优于Gemini 1.0 Pro。

![phimodelmedium](/imgs/00/phi3medium.png)

### Phi-3-vision

拥有42亿参数的Phi-3-vision继续延续这一趋势，在通用视觉推理任务、光学字符识别、表格和图表理解任务等方面优于Claude-3 Haiku和Gemini 1.0 Pro V等更大的模型。

![phimodelvision](/imgs/00/phi3vision.png)

> **注意**
>
> 在事实知识基准测试（如TriviaQA）中，Phi-3模型的表现不如较小模型，因为较小的模型规模导致其保留事实的能力有限。

### Phi-Silica

我们推出了Phi Silica，它是基于Phi系列模型构建的、专为Copilot + PC中的NPU而设计。Windows是第一个为NPU定制并内置先进小型语言模型（SLM）的平台。Phi Silica API以及OCR、Studio Effects、Live Captions、Recall User Activity API将于6月在Windows Copilot库中提供。更多API，如Vector Embedding、RAG API、Text Summarization 等将在稍后推出。

## Azure AI Studio 中的 Phi-3 模型

您可以学习如何使用Microsoft Phi-3以及如何在不同硬件设备中构建端到端解决方案。要亲自体验Phi-3，您可以在 [Azure AI Studio, Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) 中尝试和自定义Phi-3模型开始，以适应您的应用场景。

**Playground**
每个模型在 Azure AI Playground 上都有一个专门的 Playground 供您测试模型 [Azure AI Playground](https://aka.ms/try-phi3)。

## Hugging Face 中的 Phi-3 模型 

You can also find the model on the [Hugging Face](https://huggingface.co/microsoft)

**Playground**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 内容

本书包含:

## **Microsoft Phi-3 Cookbook**

- [介绍]()
  - [设置您的环境](../../md/01.Introduce/translations/zh-cn/EnvironmentSetup.md)(✅)
  - [欢迎来到 Phi-3 家族](../../md/01.Introduce/translations/zh-cn/Phi3Family.md)(✅)
  - [了解关键技术](../../md/01.Introduce/translations/zh-cn/Understandingtech.md)(✅)
  - [Phi-3 模型的 AI 安全性](../../md/01.Introduce/translations/zh-cn/AISafety.md)(✅)
  - [Phi-3 硬件支持](../../md/01.Introduce/translations/zh-cn/Hardwaresupport.md)(✅)
  - [Phi-3 模型及各平台可用性 ](../../md/01.Introduce/translations/zh-cn/Edgeandcloud.md)(✅)

- [快速开始]()
    - [在 Hugging face 中使用 Phi-3](../../md/02.QuickStart/translations/zh-cn/Huggingface_QuickStart.md)(✅)
    - [在 Azure AI Studio 中使用 Phi-3](../../md/02.QuickStart/translations/zh-cn/AzureAIStudio_QuickStart.md)(✅)
    - [在 Ollama 中使用 Phi-3](../../md/02.QuickStart/translations/zh-cn/Ollama_QuickStart.md)(✅)
    - [在 LM Studio 中使用 Phi-3](../../md/02.QuickStart/translations/zh-cn/LMStudio_QuickStart.md)(✅)
    - [在 AI Toolkit VSCode 中使用 Phi-3](../../md/02.QuickStart/translations/zh-cn/AITookit_QuickStart.md)(✅)

- [Phi-3 推理](../../md/03.Inference/translations/zh-cn/overview.md)  
  - [在 iOS 中使用 Phi-3 进行推理](../../md/03.Inference/translations/zh-cn/iOS_Inference.md)(✅)
  - [在 Jetson 中使用 Phi-3 进行推理](../../md/03.Inference/translations/zh-cn/Jetson_Inference.md)(✅)
  - [在 AI PC 中使用 Phi-3 进行推理](../../md/03.Inference/translations/zh-cn/AIPC_Inference.md)(✅)
  - [使用 Apple MLX 框架进行 Phi-3 推理](../../md/03.Inference/translations/zh-cn/MLX_Inference.md)(✅)
  - [在本地服务器中使用 Phi-3 进行推理](../../md/03.Inference/translations/zh-cn/Local_Server_Inference.md)(✅)
  - [使用 AI Toolkit 在远程服务中进行 Phi-3 推理](../../md/03.Inference/translations/zh-cn/Remote_Interence.md)(✅)
  - [在本地使用 Phi-3-Vision 进行推理](../../md/03.Inference/translations/zh-cn/Vision_Inference.md)(✅)

- [Phi-3 微调]()
  - [下载和创建样本数据集](../../md/04.Fine-tuning/translations/zh-cn/CreatingSampleData.md)(✅)
  - [微调场景](../../md/04.Fine-tuning/translations/zh-cn/FineTuning%20Scenarios.md)(✅)
  - [微调 vs RAG](../../md/04.Fine-tuning/translations/zh-cn/FineTuning%20vs%20RAG.md)(✅)
  - [让Phi-3成为行业专家](../../md/04.Fine-tuning/translations/zh-cn/LetPhi3gotoIndustriy.md)(✅)
  - [使用 VS Code 的 AI 工具包对 Phi-3 进行微调](../../md/04.Fine-tuning/translations/zh-cn/Finetuning_VSCodeaitoolkit.md)(✅)
  - [使用 Azure Machine Learning 服务对 Phi-3 进行微调](../../md/04.Fine-tuning/translations/zh-cn/Introduce_AzureML.md)(✅)
  - [使用 Lora 对 Phi-3 进行微调](../../md/04.Fine-tuning/translations/zh-cn/FineTuning_Lora.md)(✅)
  - [使用 QLora 对 Phi-3 进行微调](../../md/04.Fine-tuning/translations/zh-cn/FineTuning_Qlora.md)(✅)
  - [使用 Azure AI Studio 对 Phi-3 进行微调](../../md/04.Fine-tuning/translations/zh-cn/FineTuning_AIStudio.md)(✅)
  - [使用 Azure ML CLI/SDK 对 Phi-3 进行微调](../../md/04.Fine-tuning/translations/zh-cn/FineTuning_MLSDK.md)(✅)
  - [使用 Microsoft Olive 进行微调](../../md/04.Fine-tuning/translations/zh-cn/FineTuning_MicrosoftOlive.md)(✅)
  - [利用权重和偏差对 Phi-3-vision 进行微调](../../md/04.Fine-tuning/translations/zh-cn/FineTuning_Phi-3-visionWandB.md)(✅)
  - [使用 Apple MLX 框架对 Phi-3 进行微调](../../md/04.Fine-tuning/translations/zh-cn/FineTuning_MLX.md)(✅)
  - [对 Phi-3-vision 进行微调(官方支持)](../../md/04.Fine-tuning/translations/zh-cn/FineTuning_Vision.md)(✅)

- [Evaluation Phi-3]()
  - [负责任的人工智能简介](../../md/05.Evaluation/translations/zh-cn/ResponsibleAI.md)(✅)
  - [Promptflow 简介](../../md/05.Evaluation/translations/zh-cn/Promptflow.md)(✅)
  - [Azure AI Studio 评估简介](../../md/05.Evaluation/translations/zh-cn/AzureAIStudio.md)(✅)

- [Phi-3-mini 的端到端示例]()
  - [端到端示例简介](../../md/06.E2ESamples/translations/zh-cn/E2E_Introduction.md)(✅)
  - [准备您的行业数据](../../md/06.E2ESamples/translations/zh-cn/E2E_Datasets.md)(✅)
  - [使用 Microsoft Olive 构建您的项目架构](../../md/06.E2ESamples/translations/zh-cn/E2E_LoRA&QLoRA_Config_With_Olive.md)(✅)
  - [推理您的微调 ONNX Runtime 模型](../../md/06.E2ESamples/translations/zh-cn/E2E_Inference_ORT.md)(✅)
  - [多模型 - 交互式 Phi-3-mini 和 OpenAI Whisper](../../md/06.E2ESamples/translations/zh-cn/E2E_Phi-3-mini%20with%20whisper.md)(✅)
  - [MLFlow - 构建一个包装器并使用 Phi-3 和 MLFlow](../../md/06.E2ESamples/translations/zh-cn/E2E_Phi-3-MLflow.md)(✅)
  - [基于 Phi-3 mini-4k-instruct-onnx 的 WinUI3 应用](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)(✅)
  - [WinUI3 多模型 AI 支持的笔记应用示例](https://github.com/microsoft/ai-powered-notes-winui3-sample)(✅)
  - [微调和集成自定义 Phi-3 模型与 Prompt flow](../../md/06.E2ESamples/translations/zh-cn/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)(✅)

- [Phi-3-vision 的端到端示例]()
  - [Phi-3-vision-图像文本转文本](../../md/06.E2ESamples/translations/zh-cn/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)(✅)
  - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Phi-3-vision CLIP 嵌入](../../md/06.E2ESamples/translations/zh-cn/E2E_Phi-3-%20Embedding%20Images%20with%20CLIPVision.md)(✅)

- [Phi-3 的实验和工作坊示例]()
  - [C# .NET 实验](../../md/07.Labs/translations/zh-cn/Csharp/csharplabs.md)(✅)
  - [使用 Microsoft Phi-3 系列构建您自己的 Visual Studio Code GitHub Copilot Chat](../../md/07.Labs/translations/zh-cn/VSCode/README.md)(✅)
  - [Phi-3 ONNX 教程](https://onnxruntime.ai/docs/genai/tutorials/phi3-python.html)(✅)
  - [Phi-3-vision ONNX 教程](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [使用 ONNX Runtime generate() API 运行 Phi-3 模型](https://github.com/microsoft/onnxruntime-genai/blob/main/examples/python/phi-3-tutorial.md)(✅)
  - [Phi-3 ONNX 多模型 LLM 聊天 UI，这是一个聊天演示](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/chat_app)(✅)
  - [C# Hello Phi-3 ONNX 示例 Phi-3](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi)(✅)
  - [C# API Phi-3 ONNX 示例以支持 Phi-3-Vision](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi3V)(✅)
  - [在 CodeSpace 中运行 C# Phi-3 示例](../../md/07.Labs/translations/zh-cn/CsharpOllamaCodeSpaces/CsharpOllamaCodeSpaces.md)(✅)
  - [使用 Phi-3 与 Promptflow 和 Azure AI Search](./code/07.Lab/RAG%20with%20PromptFlow%20and%20AISearch/README.md)(✅)

## 贡献

欢迎大家为本项目贡献和建议。大多数贡献需要您同意贡献者许可协议（CLA），声明您有权并确实授权我们使用您的贡献。详情请访问 https://cla.opensource.microsoft.com.

当您提交pull request时，CLA机器人会自动判断您是否需要提供CLA，并相应地装饰拉取请求（例如，状态检查、评论）。只需按照机器人提供的说明操作。在我们所有使用CLA的代码库中，您只需要做一次这个操作。

本项目已采用 [Microsoft 开源代码行为准则](https://opensource.microsoft.com/codeofconduct/).
有关更多信息，请查看 [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 或者
如有其他问题或意见，请联系 [opencode@microsoft.com](mailto:opencode@microsoft.com)。

## 商标

本项目可能包含项目、产品或服务的商标或徽标。使用Microsoft商标或徽标须经授权，并遵循 [Microsoft 商标与品牌指南](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)。
在此项目的修改版本中使用Microsoft商标或徽标不得引起混淆或暗示Microsoft赞助。使用任何第三方商标或徽标须遵循第三方的政策。