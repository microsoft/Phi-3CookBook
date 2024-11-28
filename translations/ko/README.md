# Phi-3 요리책: Microsoft의 Phi-3 모델과 함께하는 실습 예제

[![GitHub Codespaces에서 샘플 열기 및 사용하기](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)
[![Dev Containers에서 열기](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

[![GitHub 기여자](https://img.shields.io/github/contributors/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 이슈](https://img.shields.io/github/issues/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 풀 리퀘스트](https://img.shields.io/github/issues-pr/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR 환영](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub 구독자](https://img.shields.io/github/watchers/microsoft/phi-3cookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phi-3cookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 포크](https://img.shields.io/github/forks/microsoft/phi-3cookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phi-3cookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 별점](https://img.shields.io/github/stars/microsoft/phi-3cookbook?style=social&label=Star)](https://GitHub.com/microsoft/phi-3cookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi는 Microsoft가 개발한 오픈 AI 모델 패밀리입니다. Phi 모델은 다양한 언어, 추론, 코딩 및 수학 벤치마크에서 동일한 크기와 그 다음 크기의 모델을 능가하는 가장 능력 있고 비용 효율적인 소형 언어 모델(SLM)입니다. Phi-3 패밀리에는 미니, 소형, 중형 및 비전 버전이 포함되어 있으며, 다양한 애플리케이션 시나리오에 맞게 다른 매개변수를 기반으로 훈련되었습니다. Microsoft의 Phi 패밀리에 대한 자세한 정보는 [Phi 패밀리에 오신 것을 환영합니다](/md/01.Introduce/Phi3Family.md) 페이지를 방문하세요.

다음 단계를 따르세요:
1. **저장소 포크하기**: 이 페이지의 오른쪽 상단에 있는 "Fork" 버튼을 클릭하세요.
2. **저장소 클론하기**: `git clone https://github.com/microsoft/Phi-3CookBook.git`

![Phi3Family](/imgs/00/Phi3getstarted.png)

## 목차

- 소개
  - [환경 설정](./md/01.Introduce/EnvironmentSetup.md)(✅)
  - [Phi 패밀리에 오신 것을 환영합니다](./md/01.Introduce/Phi3Family.md)(✅)
  - [핵심 기술 이해하기](./md/01.Introduce/Understandingtech.md)(✅)
  - [Phi 모델의 AI 안전성](./md/01.Introduce/AISafety.md)(✅)
  - [Phi-3 하드웨어 지원](./md/01.Introduce/Hardwaresupport.md)(✅)
  - [플랫폼별 Phi-3 모델 및 가용성](./md/01.Introduce/Edgeandcloud.md)(✅)
  - [Guidance-ai와 Phi 사용하기](./md/01.Introduce/Guidance.md)(✅)
  - [GitHub Marketplace 모델](https://github.com/marketplace/models)(✅)
  - [Azure AI 모델 카탈로그](https://ai.azure.com)(✅)

- 빠른 시작
  - [GitHub 모델 카탈로그에서 Phi-3 사용하기](./md/02.QuickStart/GitHubModel_QuickStart.md)(✅)
  - [Hugging face에서 Phi-3 사용하기](./md/02.QuickStart/Huggingface_QuickStart.md)(✅)
  - [OpenAI SDK와 함께 Phi-3 사용하기](./md/02.QuickStart/OpenAISDK_Quickstart.md)(✅)
  - [Http 요청으로 Phi-3 사용하기](./md/02.QuickStart/HttpAPI_QuickStart.md)(✅)
  - [Azure AI Studio에서 Phi-3 사용하기](./md/02.QuickStart/AzureAIStudio_QuickStart.md)(✅)
  - [Azure MaaS 또는 MaaP와 함께 Phi-3 모델 추론 사용하기](./md/02.QuickStart/AzureModel_Inference.md)(✅)
  - [GitHub 및 Azure AI와 함께 Azure Inference API로 Phi-3 사용하기](./md/02.QuickStart/AzureInferenceAPI_QuickStart.md)
  - [Azure AI Studio에서 서버리스 API로 Phi-3 모델 배포하기](./md/02.QuickStart/AzureAIStudio_MaaS.md)(✅)
  - [Ollama에서 Phi-3 사용하기](./md/02.QuickStart/Ollama_QuickStart.md)(✅)
- [LM Studio에서 Phi-3 사용하기](./md/02.QuickStart/LMStudio_QuickStart.md)(✅)
  - [AI Toolkit VSCode에서 Phi-3 사용하기](./md/02.QuickStart/AITookit_QuickStart.md)(✅)
  - [Phi-3와 LiteLLM 사용하기](./md/02.QuickStart/LiteLLM_QuickStart.md)(✅)

- [Phi-3 추론하기](./md/03.Inference/overview.md)  
  - [iOS에서 Phi-3 추론하기](./md/03.Inference/iOS_Inference.md)(✅)
  - [Android에서 Phi-3.5 추론하기](./md/08.Update/Phi35/050.UsingPhi35TFLiteCreateAndroidApp.md)(✅)
  - [Jetson에서 Phi-3 추론하기](./md/03.Inference/Jetson_Inference.md)(✅)
  - [AI PC에서 Phi-3 추론하기](./md/03.Inference/AIPC_Inference.md)(✅)
  - [Apple MLX Framework와 함께 Phi-3 추론하기](./md/03.Inference/MLX_Inference.md)(✅)
  - [로컬 서버에서 Phi-3 추론하기](./md/03.Inference/Local_Server_Inference.md)(✅)
  - [AI Toolkit을 사용해 원격 서버에서 Phi-3 추론하기](./md/03.Inference/Remote_Interence.md)(✅)
  - [Rust와 함께 Phi-3 추론하기](./md/03.Inference/Rust_Inference.md)(✅)
  - [로컬에서 Phi-3-Vision 추론하기](./md/03.Inference/Vision_Inference.md)(✅)
  - [Kaito AKS, Azure Containers(공식 지원)와 함께 Phi-3 추론하기](./md/03.Inference/Kaito_Inference.md)(✅)
  - [Fine-tuning ONNX Runtime 모델 추론하기](./md/06.E2ESamples/E2E_Inference_ORT.md)(✅)

- Phi-3 파인튜닝
  - [샘플 데이터 세트 다운로드 및 생성](./md/04.Fine-tuning/CreatingSampleData.md)(✅)
  - [파인튜닝 시나리오](./md/04.Fine-tuning/FineTuning_Scenarios.md)(✅)
  - [파인튜닝 vs RAG](./md/04.Fine-tuning/FineTuning_vs_RAG.md)(✅)
  - [Phi-3을 산업 전문가로 만들기](./md/04.Fine-tuning/LetPhi3gotoIndustriy.md)(✅)
  - [AI Toolkit for VS Code로 Phi-3 파인튜닝하기](./md/04.Fine-tuning/Finetuning_VSCodeaitoolkit.md)(✅)
  - [Azure Machine Learning Service로 Phi-3 파인튜닝하기](./md/04.Fine-tuning/Introduce_AzureML.md)(✅)
  - [Lora로 Phi-3 파인튜닝하기](./md/04.Fine-tuning/FineTuning_Lora.md)(✅)
  - [QLora로 Phi-3 파인튜닝하기](./md/04.Fine-tuning/FineTuning_Qlora.md)(✅)
  - [Azure AI Studio로 Phi-3 파인튜닝하기](./md/04.Fine-tuning/FineTuning_AIStudio.md)(✅)
  - [Azure ML CLI/SDK로 Phi-3 파인튜닝하기](./md/04.Fine-tuning/FineTuning_MLSDK.md)(✅)
  - [Microsoft Olive로 파인튜닝하기](./md/04.Fine-tuning/FineTuning_MicrosoftOlive.md)(✅)
  - [Microsoft Olive 실습 랩으로 파인튜닝하기](./code/04.Finetuning/olive-lab/readme.md)(✅)
  - [Weights and Bias로 Phi-3-vision 파인튜닝하기](./md/04.Fine-tuning/FineTuning_Phi-3-visionWandB.md)(✅)
  - [Apple MLX Framework로 Phi-3 파인튜닝하기](./md/04.Fine-tuning/FineTuning_MLX.md)(✅)
  - [Phi-3-vision 파인튜닝 (공식 지원)](./md/04.Fine-tuning/FineTuning_Vision.md)(✅)
- [Kaito AKS 및 Azure Containers(공식 지원)으로 Phi-3 미세 조정](./md/04.Fine-tuning/FineTuning_Kaito.md)(✅)
  - [Phi-3 및 3.5 Vision 미세 조정](https://github.com/2U1/Phi3-Vision-Finetune)(✅)

- Phi-3 평가
  - [책임 있는 AI 소개](./md/05.Evaluation/ResponsibleAI.md)(✅)
  - [Promptflow 소개](./md/05.Evaluation/Promptflow.md)(✅)
  - [평가를 위한 Azure AI Studio 소개](./md/05.Evaluation/AzureAIStudio.md)(✅)

- Phi-3-mini를 위한 E2E 샘플
  - [엔드 투 엔드 샘플 소개](./md/06.E2ESamples/E2E_Introduction.md)(✅)
  - [산업 데이터를 준비하세요](./md/06.E2ESamples/E2E_Datasets.md)(✅)
  - [Microsoft Olive를 사용하여 프로젝트를 설계하세요](./md/06.E2ESamples/E2E_LoRA&QLoRA_Config_With_Olive.md)(✅)
  - [Phi-3, ONNXRuntime Mobile 및 ONNXRuntime Generate API를 사용한 Android에서의 로컬 챗봇](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/mobile/examples/phi-3/android)(✅)
  - [Hugging Face Space WebGPU 및 Phi-3-mini 데모 - Phi-3-mini는 사용자에게 개인적이고 강력한 챗봇 경험을 제공합니다. 시도해보세요](https://huggingface.co/spaces/Xenova/experimental-phi3-webgpu)(✅)
  - [Phi3, ONNX Runtime Web 및 WebGPU를 사용한 브라우저에서의 로컬 챗봇](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)(✅)
  - [OpenVino Chat](/md/06.E2ESamples/E2E_OpenVino_Chat.md)(✅)
  - [다중 모델 - 인터랙티브 Phi-3-mini 및 OpenAI Whisper](./md/06.E2ESamples/E2E_Phi-3-mini_with_whisper.md)(✅)
  - [MLFlow - 래퍼를 구축하고 MLFlow와 함께 Phi-3 사용](./md/06.E2ESamples/E2E_Phi-3-MLflow.md)(✅)
  - [모델 최적화 - Olive를 사용하여 ONNX Runtime Web에 대한 Phi-3-min 모델 최적화 방법](https://github.com/microsoft/Olive/tree/main/examples/phi3)(✅)
  - [Phi-3 mini-4k-instruct-onnx를 사용한 WinUI3 앱](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)(✅)
  - [WinUI3 다중 모델 AI 지원 노트 앱 샘플](https://github.com/microsoft/ai-powered-notes-winui3-sample)(✅)
  - [Prompt flow와 함께 맞춤형 Phi-3 모델 미세 조정 및 통합](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)(✅)
  - [Azure AI Studio에서 Prompt flow와 함께 맞춤형 Phi-3 모델 미세 조정 및 통합](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIstudio.md)(✅)
  - [Microsoft의 책임 있는 AI 원칙에 중점을 두고 Azure AI Studio에서 미세 조정된 Phi-3 / Phi-3.5 모델 평가](./md/06.E2ESamples/E2E_Phi-3-Evaluation_AIstudio.md)(✅)
  - [Phi-3.5-mini-instruct 언어 예측 샘플 (중국어/영어)](../../code/09.UpdateSamples/Aug/phi3-instruct-demo.ipynb)(✅)

- Phi-3-vision을 위한 E2E 샘플
  - [Phi-3-vision-이미지 텍스트에서 텍스트로](../../code/06.E2E/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)(✅)
  - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Phi-3-vision CLIP 임베딩](./md/06.E2ESamples/E2E_Phi-3-Embedding_Images_with_CLIPVision.md)(✅)
  - [데모: Phi-3 재활용](https://github.com/jennifermarsman/PhiRecycling/)(✅)
  - [Phi-3-vision - Phi3-Vision 및 OpenVINO를 사용한 시각적 언어 어시스턴트](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)(✅)
  - [Phi-3 Vision Nvidia NIM](/md/06.E2ESamples/E2E_Nvidia_NIM_Vision.md)(✅)
  - [Phi-3 Vision OpenVino](/md/06.E2ESamples/E2E_OpenVino_Phi3Vision.md)(✅)
  - [Phi-3.5 Vision 다중 프레임 또는 다중 이미지 샘플](../../code/09.UpdateSamples/Aug/phi3-vision-demo.ipynb)(✅)

- Phi-3.5-MoE를 위한 E2E 샘플
  - [Phi-3.5 전문가 모델(MoEs) 소셜 미디어 샘플](../../code/09.UpdateSamples/Aug/phi3_moe_demo.ipynb)(✅)
- [NVIDIA NIM Phi-3 MOE, Azure AI Search, 및 LlamaIndex와 함께 Retrieval-Augmented Generation (RAG) 파이프라인 구축](https://github.com/farzad528/azure-ai-search-python-playground/blob/main/azure-ai-search-nvidia-rag.ipynb)(✅)

- 실습 및 워크샵 샘플 Phi-3
  - [C# .NET 실습](./md/07.Labs/Csharp/csharplabs.md)(✅)
  - [Microsoft Phi-3 Family와 함께 Visual Studio Code GitHub Copilot Chat 구축](./md/07.Labs/VSCode/README.md)(✅)
  - [로컬 RAG 파일을 사용한 Local WebGPU Phi-3 Mini RAG 챗봇 샘플](./code/08.RAG/rag_webgpu_chat/README.md)(✅)
  - [Phi-3 ONNX 튜토리얼](https://onnxruntime.ai/docs/genai/tutorials/phi3-python.html)(✅)
  - [Phi-3-vision ONNX 튜토리얼](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [ONNX Runtime generate() API를 사용하여 Phi-3 모델 실행](https://github.com/microsoft/onnxruntime-genai/blob/main/examples/python/phi-3-tutorial.md)(✅)
  - [Phi-3 ONNX 멀티 모델 LLM 채팅 UI, 이것은 채팅 데모입니다](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/chat_app)(✅)
  - [C# Hello Phi-3 ONNX 예제 Phi-3](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi)(✅)
  - [C# API Phi-3 ONNX 예제 Phi3-Vision 지원](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi3V)(✅)
  - [CodeSpace에서 C# Phi-3 샘플 실행](./md/07.Labs/CsharpOllamaCodeSpaces/CsharpOllamaCodeSpaces.md)(✅)
  - [Promptflow와 Azure AI Search를 사용하여 Phi-3 사용](./code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md)(✅)
  - [Windows Copilot 라이브러리를 사용한 Windows AI-PC API](https://developer.microsoft.com/windows/ai/?WT.mc_id=aiml-137032-kinfeylo)

- Phi-3.5 학습
  - [Phi-3.5 Family의 새로운 기능](./md/08.Update/Phi35/010.WhatsNewInPhi35.md)(✅)
  - [Phi-3.5 Family 정량화](./md/08.Update/Phi35/020.QuantifyingPhi35.md)(✅)
    - [llama.cpp를 사용하여 Phi-3.5 정량화](./md/08.Update/Phi35/021.UsingLlamacppQuantifyingPhi35.md)(✅)
    - [onnxruntime의 생성 AI 확장을 사용하여 Phi-3.5 정량화](./md/08.Update/Phi35/022.UsingORTGenAIQuantifyingPhi35.md)(✅)
    - [Intel OpenVINO를 사용하여 Phi-3.5 정량화](./md/08.Update/Phi35/023.UsingIntelOpenVINOQuantifyingPhi35.md)(✅)
    - [Apple MLX Framework를 사용하여 Phi-3.5 정량화](./md/08.Update/Phi35/024.UsingAppleMLXQuantifyingPhi35.md)(✅)
  - Phi-3.5 애플리케이션 샘플
    - [Phi-3.5-Instruct WebGPU RAG 챗봇](./md/08.Update/Phi35/031.WebGPUWithPhi35Readme.md)(✅)
    - [GitHub 모델을 사용하여 Phi-3.5로 Visual Studio Code Chat Copilot 에이전트 생성](./md/08.Update/Phi35/032.CreateVSCodeChatAgentWithGitHubModels.md)(✅)
    - [Windows GPU를 사용하여 Phi-3.5-Instruct ONNX와 함께 프롬프트 흐름 솔루션 생성](./md/08.Update/Phi35/040.UsingPromptFlowWithONNX.md)(✅)
    - [Microsoft Phi-3.5 tflite를 사용하여 Android 앱 생성](./md/08.Update/Phi35/050.UsingPhi35TFLiteCreateAndroidApp.md)(✅)


## Phi-3 모델 사용하기

### Azure AI Studio에서 Phi-3

Microsoft Phi-3를 사용하고 다양한 하드웨어 장치에서 E2E 솔루션을 구축하는 방법을 배울 수 있습니다. 직접 Phi-3를 경험하려면 모델을 사용해보고 시나리오에 맞게 Phi-3를 커스터마이징하는 것으로 시작하십시오. [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai)에서 자세히 알아볼 수 있으며, [Azure AI Studio 시작하기](/md/02.QuickStart/AzureAIStudio_QuickStart.md)에서 더 많은 정보를 얻을 수 있습니다.

**Playground**
각 모델에는 모델을 테스트할 수 있는 전용 플레이그라운드가 있습니다 [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub Models에서 Phi-3

Microsoft Phi-3를 사용하고 다양한 하드웨어 장치에서 E2E 솔루션을 구축하는 방법을 배울 수 있습니다. 직접 Phi-3를 경험하려면 모델을 사용해보고 시나리오에 맞게 Phi-3를 커스터마이징하는 것으로 시작하십시오. [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)에서 자세히 알아볼 수 있으며, [GitHub Model Catalog 시작하기](/md/02.QuickStart/GitHubModel_QuickStart.md)에서 더 많은 정보를 얻을 수 있습니다.

**Playground**
각 모델에는 모델을 테스트할 수 있는 전용 [플레이그라운드](/md/02.QuickStart/GitHubModel_QuickStart.md)가 있습니다.

### Hugging Face에서 Phi-3

[Hugging Face](https://huggingface.co/microsoft)에서도 모델을 찾을 수 있습니다.

**Playground**
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🌐 다국어 지원

> **Note:**
> 이 번역들은 오픈 소스 [co-op-translator](https://github.com/Azure/co-op-translator)를 사용해 자동으로 생성되었으며, 오류나 부정확한 내용이 포함될 수 있습니다. 중요한 정보는 원본을 참조하거나 전문 번역가와 상담하는 것이 좋습니다. 번역을 추가하거나 업데이트하고 싶다면, [co-op-translator](https://github.com/Azure/co-op-translator) 리포지토리를 참조하십시오. 간단한 명령어를 사용하여 쉽게 기여할 수 있습니다.

| 언어                  | 코드 | 번역된 README 링크                                      | 마지막 업데이트 |
|----------------------|------|---------------------------------------------------------|-----------------|
| 중국어 (간체)        | zh   | [Chinese Translation](../zh/README.md)      | 2024-11-29      |
| 중국어 (번체)        | tw   | [Chinese Translation](../tw/README.md)      | 2024-11-29      |
| 프랑스어             | fr   | [French Translation](../fr/README.md)       | 2024-11-29      |
| 일본어               | ja   | [Japanese Translation](../ja/README.md)     | 2024-11-29      |
| 한국어               | ko   | [Korean Translation](./README.md)       | 2024-11-29      |
| 스페인어             | es   | [Spanish Translation](../es/README.md)      | 2024-11-29      |

## 상표

이 프로젝트에는 프로젝트, 제품 또는 서비스에 대한 상표나 로고가 포함될 수 있습니다. Microsoft 상표나 로고의 승인된 사용은 [Microsoft의 상표 및 브랜드 가이드라인](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)을 따라야 합니다.
이 프로젝트의 수정된 버전에서 Microsoft 상표나 로고를 사용하는 경우 혼란을 초래하거나 Microsoft의 후원을 암시해서는 안 됩니다. 제3자 상표나 로고의 사용은 해당 제3자의 정책을 따라야 합니다.

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원본 문서는 해당 언어로 작성된 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인한 오해나 오역에 대해 당사는 책임을 지지 않습니다.