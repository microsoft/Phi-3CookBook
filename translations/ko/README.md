# Phi-3 요리책: Microsoft의 Phi-3 모델을 활용한 실습 예제

[![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phi-3cookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phi-3cookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phi-3cookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phi-3cookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phi-3cookbook?style=social&label=Star)](https://GitHub.com/microsoft/phi-3cookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi는 Microsoft가 개발한 오픈 AI 모델의 가족입니다. Phi 모델은 동일한 크기와 그보다 큰 모델들보다 다양한 언어, 추론, 코딩, 수학 벤치마크에서 더 뛰어난 성능을 보이며, 가장 유능하고 비용 효율적인 소형 언어 모델(SLM)입니다. Phi-3 가족에는 미니, 소형, 중형, 비전 버전이 포함되어 있으며, 다양한 응용 시나리오를 위해 다양한 매개변수 양을 기반으로 훈련되었습니다. Microsoft의 Phi 가족에 대한 더 자세한 정보는 [Welcome to the Phi Family](/md/01.Introduce/Phi3Family.md) 페이지를 방문하세요.

![Phi3Family](/imgs/00/Phi3getstarted.png)

## 목차

- 소개
  - [환경 설정하기](./md/01.Introduce/EnvironmentSetup.md)(✅)
  - [Phi 가족 소개](./md/01.Introduce/Phi3Family.md)(✅)
  - [핵심 기술 이해하기](./md/01.Introduce/Understandingtech.md)(✅)
  - [Phi 모델의 AI 안전성](./md/01.Introduce/AISafety.md)(✅)
  - [Phi-3 하드웨어 지원](./md/01.Introduce/Hardwaresupport.md)(✅)
  - [Phi-3 모델 및 플랫폼별 가용성](./md/01.Introduce/Edgeandcloud.md)(✅)
  - [Guidance-ai와 Phi 사용하기](./md/01.Introduce/Guidance.md)(✅)

- 빠른 시작
  - [GitHub 모델 카탈로그에서 Phi-3 사용하기](./md/02.QuickStart/GitHubModel_QuickStart.md)(✅)
  - [Hugging face에서 Phi-3 사용하기](./md/02.QuickStart/Huggingface_QuickStart.md)(✅)
  - [OpenAI SDK로 Phi-3 사용하기](./md/02.QuickStart/OpenAISDK_Quickstart.md)(✅)
  - [Http 요청으로 Phi-3 사용하기](./md/02.QuickStart/HttpAPI_QuickStart.md)(✅)
  - [Azure AI Studio에서 Phi-3 사용하기](./md/02.QuickStart/AzureAIStudio_QuickStart.md)(✅)
  - [Azure MaaS 또는 MaaP로 Phi-3 모델 추론 사용하기](./md/02.QuickStart/AzureModel_Inference.md)(✅)
  - [Azure AI Studio에서 서버리스 API로 Phi-3 모델 배포하기](./md/02.QuickStart/AzureAIStudio_MaaS.md)(✅)
  - [Ollama에서 Phi-3 사용하기](./md/02.QuickStart/Ollama_QuickStart.md)(✅)
  - [LM Studio에서 Phi-3 사용하기](./md/02.QuickStart/LMStudio_QuickStart.md)(✅)
  - [AI Toolkit VSCode에서 Phi-3 사용하기](./md/02.QuickStart/AITookit_QuickStart.md)(✅)
  - [Phi-3와 LiteLLM 사용하기](./md/02.QuickStart/LiteLLM_QuickStart.md)(✅)
- [Inference Phi-3](./md/03.Inference/overview.md)  
  - [Inference Phi-3 in iOS](./md/03.Inference/iOS_Inference.md)(✅)
  - [Inference Phi-3 in Jetson](./md/03.Inference/Jetson_Inference.md)(✅)
  - [Inference Phi-3 in AI PC](./md/03.Inference/AIPC_Inference.md)(✅)
  - [Inference Phi-3 with Apple MLX Framework](./md/03.Inference/MLX_Inference.md)(✅)
  - [Inference Phi-3 in Local Server](./md/03.Inference/Local_Server_Inference.md)(✅)
  - [Inference Phi-3 in Remote Server using AI Toolkit](./md/03.Inference/Remote_Interence.md)(✅)
  - [Inference Phi-3 with Rust](./md/03.Inference/Rust_Inference.md)(✅)
  - [Inference Phi-3-Vision in Local](./md/03.Inference/Vision_Inference.md)(✅)
  - [Inference Phi-3 with Kaito AKS, Azure Containers(official support)](./md/03.Inference/Kaito_Inference.md)(✅)
  - [Inference Your Fine-tuning ONNX Runtime Model](./md/06.E2ESamples/E2E_Inference_ORT.md)(✅)

- Phi-3 미세 조정
  - [샘플 데이터 세트 다운로드 및 생성](./md/04.Fine-tuning/CreatingSampleData.md)(✅)
  - [미세 조정 시나리오](./md/04.Fine-tuning/FineTuning_Scenarios.md)(✅)
  - [미세 조정 vs RAG](./md/04.Fine-tuning/FineTuning_vs_RAG.md)(✅)
  - [Phi-3를 산업 전문가로 만들기](./md/04.Fine-tuning/LetPhi3gotoIndustriy.md)(✅)
  - [VS Code의 AI Toolkit을 사용한 Phi-3 미세 조정](./md/04.Fine-tuning/Finetuning_VSCodeaitoolkit.md)(✅)
  - [Azure Machine Learning Service를 사용한 Phi-3 미세 조정](./md/04.Fine-tuning/Introduce_AzureML.md)(✅)
  - [Lora를 사용한 Phi-3 미세 조정](./md/04.Fine-tuning/FineTuning_Lora.md)(✅)
  - [QLora를 사용한 Phi-3 미세 조정](./md/04.Fine-tuning/FineTuning_Qlora.md)(✅)
  - [Azure AI Studio를 사용한 Phi-3 미세 조정](./md/04.Fine-tuning/FineTuning_AIStudio.md)(✅)
  - [Azure ML CLI/SDK를 사용한 Phi-3 미세 조정](./md/04.Fine-tuning/FineTuning_MLSDK.md)(✅)
  - [Microsoft Olive를 사용한 미세 조정](./md/04.Fine-tuning/FineTuning_MicrosoftOlive.md)(✅)
  - [Weights and Bias를 사용한 Phi-3-vision 미세 조정](./md/04.Fine-tuning/FineTuning_Phi-3-visionWandB.md)(✅)
  - [Apple MLX Framework를 사용한 Phi-3 미세 조정](./md/04.Fine-tuning/FineTuning_MLX.md)(✅)
  - [Phi-3-vision 미세 조정 (공식 지원)](./md/04.Fine-tuning/FineTuning_Vision.md)(✅)
  - [Kaito AKS, Azure Containers를 사용한 Phi-3 미세 조정 (공식 지원)](./md/04.Fine-tuning/FineTuning_Kaito.md)(✅)

- Phi-3 평가
  - [책임 있는 AI 소개](./md/05.Evaluation/ResponsibleAI.md)(✅)
  - [Promptflow 소개](./md/05.Evaluation/Promptflow.md)(✅)
  - [평가를 위한 Azure AI Studio 소개](./md/05.Evaluation/AzureAIStudio.md)(✅)

- Phi-3-mini의 E2E 샘플
  - [엔드 투 엔드 샘플 소개](./md/06.E2ESamples/E2E_Introduction.md)(✅)
- [산업 데이터를 준비하세요](./md/06.E2ESamples/E2E_Datasets.md)(✅)
  - [Microsoft Olive를 사용하여 프로젝트 설계하기](./md/06.E2ESamples/E2E_LoRA&QLoRA_Config_With_Olive.md)(✅)
  - [Phi-3, ONNXRuntime Mobile 및 ONNXRuntime Generate API를 사용한 Android 로컬 챗봇](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/mobile/examples/phi-3/android)(✅)
  - [Hugging Face Space WebGPU와 Phi-3-mini 데모 - Phi-3-mini는 사용자에게 강력한 개인 챗봇 경험을 제공합니다. 시도해 보세요](https://huggingface.co/spaces/Xenova/experimental-phi3-webgpu)(✅)
  - [Phi3, ONNX Runtime Web 및 WebGPU를 사용한 브라우저 내 로컬 챗봇](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)(✅)
  - [OpenVino Chat](/md/06.E2ESamples/E2E_OpenVino_Chat.md)(✅)
  - [멀티 모델 - 인터랙티브 Phi-3-mini와 OpenAI Whisper](./md/06.E2ESamples/E2E_Phi-3-mini_with_whisper.md)(✅)
  - [MLFlow - 래퍼 빌드 및 MLFlow와 함께 Phi-3 사용하기](./md/06.E2ESamples/E2E_Phi-3-MLflow.md)(✅)
  - [모델 최적화 - Olive를 사용하여 ONNX Runtime Web용 Phi-3-min 모델 최적화 방법](https://github.com/microsoft/Olive/tree/main/examples/phi3)(✅)
  - [Phi-3 mini-4k-instruct-onnx를 사용한 WinUI3 앱](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)(✅)
  - [WinUI3 멀티 모델 AI 노트 앱 샘플](https://github.com/microsoft/ai-powered-notes-winui3-sample)(✅)
  - [사용자 정의 Phi-3 모델을 Prompt flow와 함께 미세 조정 및 통합하기](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)(✅)
  - [Azure AI Studio에서 사용자 정의 Phi-3 모델을 Prompt flow와 함께 미세 조정 및 통합하기](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIstudio.md)(✅)
  - [Phi-3.5-mini-instruct 언어 예측 샘플 (중국어/영어)](../../code/09.UpdateSamples/Aug/phi3-instruct-demo.ipynb)(✅)

- Phi-3-vision을 위한 E2E 샘플
  - [Phi-3-vision-이미지 텍스트에서 텍스트로](../../code/06.E2E/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)(✅)
  - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Phi-3-vision CLIP 임베딩](./md/06.E2ESamples/E2E_Phi-3-Embedding_Images_with_CLIPVision.md)(✅)
  - [데모: Phi-3 재활용](https://github.com/jennifermarsman/PhiRecycling/)(✅)
  - [Phi-3-vision - Phi3-Vision 및 OpenVINO를 사용한 시각적 언어 보조](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)(✅)
  - [Phi-3 Vision Nvidia NIM](/md/06.E2ESamples/E2E_Nvidia_NIM_Vision.md)(✅)
  - [Phi-3 Vision OpenVino](/md/06.E2ESamples/E2E_OpenVino_Phi3Vision.md)(✅)
  - [Phi-3.5 Vision 다중 프레임 또는 다중 이미지 샘플](../../code/09.UpdateSamples/Aug/phi3-vision-demo.ipynb)(✅)

- Phi-3.5-MoE를 위한 E2E 샘플
  - [Phi-3.5 전문가 혼합 모델(MoEs) 소셜 미디어 샘플](../../code/09.UpdateSamples/Aug/phi3_moe_demo.ipynb)(✅)
  - [NVIDIA NIM Phi-3 MOE, Azure AI Search 및 LlamaIndex를 사용한 검색-증강 생성(RAG) 파이프라인 구축](https://github.com/farzad528/azure-ai-search-python-playground/blob/main/azure-ai-search-nvidia-rag.ipynb)(✅)

- Phi-3를 위한 실습 및 워크숍 샘플
  - [C# .NET 실습](./md/07.Labs/Csharp/csharplabs.md)(✅)
  - [Microsoft Phi-3 패밀리와 함께 Visual Studio Code GitHub Copilot Chat 구축하기](./md/07.Labs/VSCode/README.md)(✅)
  - [로컬 RAG 파일과 함께하는 로컬 WebGPU Phi-3 Mini RAG 챗봇 샘플](./code/08.RAG/rag_webgpu_chat/README.md)(✅)
  - [Phi-3 ONNX 튜토리얼](https://onnxruntime.ai/docs/genai/tutorials/phi3-python.html)(✅)
  - [Phi-3-vision ONNX 튜토리얼](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [ONNX Runtime generate() API를 사용하여 Phi-3 모델 실행하기](https://github.com/microsoft/onnxruntime-genai/blob/main/examples/python/phi-3-tutorial.md)(✅)
- [Phi-3 ONNX 다중 모델 LLM 채팅 UI, 채팅 데모입니다](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/chat_app)(✅)
  - [C# Hello Phi-3 ONNX 예제 Phi-3](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi)(✅)
  - [Phi3-Vision을 지원하는 C# API Phi-3 ONNX 예제](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi3V)(✅)
  - [CodeSpace에서 C# Phi-3 샘플 실행하기](./md/07.Labs/CsharpOllamaCodeSpaces/CsharpOllamaCodeSpaces.md)(✅)
  - [Promptflow와 Azure AI Search를 사용한 Phi-3](./code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md)(✅)
  - [Windows Copilot Library를 사용하는 Windows AI-PC API](https://developer.microsoft.com/windows/ai/?WT.mc_id=aiml-137032-kinfeylo)

- Phi-3.5 학습하기
  - [Phi-3.5 패밀리의 새로운 기능](./md/08.Update/Phi35/010.WhatsNewInPhi35.md)(✅)
  - [Phi-3.5 패밀리의 정량화](./md/08.Update/Phi35/020.QuantifyingPhi35.md)(✅)
    - [llama.cpp를 사용한 Phi-3.5 정량화](./md/08.Update/Phi35/021.UsingLlamacppQuantifyingPhi35.md)(✅)
    - [onnxruntime의 생성 AI 확장을 사용한 Phi-3.5 정량화](./md/08.Update/Phi35/022.UsingORTGenAIQuantifyingPhi35.md)(✅)
    - [Intel OpenVINO를 사용한 Phi-3.5 정량화](./md/08.Update/Phi35/023.UsingIntelOpenVINOQuantifyingPhi35.md)(✅)
    - [Apple MLX Framework를 사용한 Phi-3.5 정량화](./md/08.Update/Phi35/024.UsingAppleMLXQuantifyingPhi35.md)(✅)
  - Phi-3.5 애플리케이션 샘플
    - [Phi-3.5-Instruct WebGPU RAG 챗봇](./md/08.Update/Phi35/031.WebGPUWithPhi35Readme.md)(✅)
    - [GitHub 모델을 사용하여 Visual Studio Code 채팅 코파일럿 에이전트 만들기](./md/08.Update/Phi35/032.CreateVSCodeChatAgentWithGitHubModels.md)(✅)


## Phi-3 모델 사용하기

### Azure AI Studio에서 Phi-3 사용하기

Microsoft Phi-3를 사용하는 방법과 다양한 하드웨어 장치에서 E2E 솔루션을 구축하는 방법을 배울 수 있습니다. Phi-3를 직접 체험하려면, [Azure AI Studio, Azure AI Model Catalog](https://aka.ms/phi3-azure-ai)를 사용하여 모델을 시도하고 시나리오에 맞게 Phi-3를 커스터마이징하는 것부터 시작하세요. 자세한 내용은 [Azure AI Studio 시작하기](/md/02.QuickStart/AzureAIStudio_QuickStart.md)에서 확인할 수 있습니다.

**Playground**
각 모델에는 모델을 테스트할 수 있는 전용 플레이그라운드가 있습니다 [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub 모델에서 Phi-3 사용하기

Microsoft Phi-3를 사용하는 방법과 다양한 하드웨어 장치에서 E2E 솔루션을 구축하는 방법을 배울 수 있습니다. Phi-3를 직접 체험하려면, [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)를 사용하여 모델을 시도하고 시나리오에 맞게 Phi-3를 커스터마이징하는 것부터 시작하세요. 자세한 내용은 [GitHub Model Catalog 시작하기](/md/02.QuickStart/GitHubModel_QuickStart.md)에서 확인할 수 있습니다.

**Playground**
각 모델에는 모델을 테스트할 수 있는 전용 [플레이그라운드](/md/02.QuickStart/GitHubModel_QuickStart.md)가 있습니다.

### Hugging Face에서 Phi-3 사용하기

모델을 [Hugging Face](https://huggingface.co/microsoft)에서도 찾을 수 있습니다.

**Playground**
 [Hugging Chat 플레이그라운드](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🌐 다국어 지원

> **Note:**
> 이 번역들은 오픈 소스 [co-op-translator](https://github.com/Azure/co-op-translator)를 사용하여 자동으로 생성되었으며 오류나 부정확성을 포함할 수 있습니다. 중요한 정보의 경우 원본을 참조하거나 전문 번역가의 도움을 받는 것이 좋습니다. 번역을 추가하거나 업데이트하려면 [co-op-translator](https://github.com/Azure/co-op-translator) 리포지토리를 참조하여 간단한 명령어로 기여할 수 있습니다.

| 언어                | 코드 | 번역된 README 링크                                      | 마지막 업데이트 |
|---------------------|------|---------------------------------------------------------|-----------------|
| 중국어 (간체)       | zh   | [중국어 번역](../zh/README.md)              | 2024-09-21      |
| 프랑스어            | fr   | [프랑스어 번역](../fr/README.md)            | 2024-09-21      |
| 일본어              | ja   | [일본어 번역](../ja/README.md)              | 2024-09-21      |
| 한국어              | ko   | [한국어 번역](./README.md)              | 2024-09-21      |
| 스페인어            | es   | [스페인어 번역](../es/README.md)            | 2024-09-21      |

## 상표

이 프로젝트에는 프로젝트, 제품 또는 서비스의 상표나 로고가 포함될 수 있습니다. Microsoft 상표나 로고의 허가된 사용은 [Microsoft의 상표 및 브랜드 지침](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)을 따라야 합니다.
이 프로젝트의 수정된 버전에서 Microsoft 상표나 로고를 사용하는 경우 혼동을 일으키거나 Microsoft의 후원을 암시해서는 안 됩니다. 제3자 상표나 로고의 사용은 해당 제3자의 정책을 따릅니다.

면책 조항: 이 번역은 원본을 AI 모델에 의해 번역된 것이며 완벽하지 않을 수 있습니다.
출력을 검토하고 필요한 수정 사항을 반영해 주시기 바랍니다.