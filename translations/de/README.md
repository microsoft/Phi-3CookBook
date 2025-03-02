# Phi Kochbuch: Praxisbeispiele mit Microsofts Phi-Modellen

[![Öffnen und Beispiele in GitHub Codespaces nutzen](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![In Dev Containers öffnen](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub-Mitwirkende](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub-Issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub-Pull-Requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PRs willkommen](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub-Beobachter](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub-Forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub-Sterne](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi ist eine Reihe von Open-Source-KI-Modellen, die von Microsoft entwickelt wurden.

Phi ist derzeit das leistungsstärkste und kosteneffektivste Small Language Model (SLM) mit hervorragenden Benchmarks in den Bereichen Mehrsprachigkeit, logisches Denken, Text-/Chat-Generierung, Programmierung, Bilder, Audio und anderen Szenarien.

Sie können Phi in der Cloud oder auf Edge-Geräten bereitstellen und mit begrenzter Rechenleistung ganz einfach generative KI-Anwendungen entwickeln.

Folgen Sie diesen Schritten, um diese Ressourcen zu nutzen:  
1. **Repository forken**: Klicken Sie hier [![GitHub-Forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **Repository klonen**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Treten Sie der Microsoft AI Discord Community bei und treffen Sie Experten und andere Entwickler**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.de.png)

## Inhaltsverzeichnis

- Einführung  
  - [Willkommen in der Phi-Familie](./md/01.Introduction/01/01.PhiFamily.md)  
  - [Einrichten Ihrer Umgebung](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [Schlüsseltechnologien verstehen](./md/01.Introduction/01/01.Understandingtech.md)  
  - [KI-Sicherheit für Phi-Modelle](./md/01.Introduction/01/01.AISafety.md)  
  - [Hardwareunterstützung für Phi](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Phi-Modelle und Verfügbarkeit auf verschiedenen Plattformen](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Verwendung von Guidance-ai und Phi](./md/01.Introduction/01/01.Guidance.md)  
  - [GitHub Marketplace-Modelle](https://github.com/marketplace/models)  
  - [Azure AI Model Catalog](https://ai.azure.com)

- Phi in verschiedenen Umgebungen ausführen  
    - [Hugging Face](./md/01.Introduction/02/01.HF.md)  
    - [GitHub-Modelle](./md/01.Introduction/02/02.GitHubModel.md)  
    - [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)  
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)  
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Phi-Familie ausführen  
    - [Phi auf iOS ausführen](./md/01.Introduction/03/iOS_Inference.md)  
    - [Phi auf Android ausführen](./md/01.Introduction/03/Android_Inference.md)  
- [Inference Phi in Jetson](./md/01.Introduction/03/Jetson_Inference.md)  
    - [Inference Phi in AI PC](./md/01.Introduction/03/AIPC_Inference.md)  
    - [Inference Phi mit Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)  
    - [Inference Phi auf einem lokalen Server](./md/01.Introduction/03/Local_Server_Inference.md)  
    - [Inference Phi auf einem Remote-Server mit AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)  
    - [Inference Phi mit Rust](./md/01.Introduction/03/Rust_Inference.md)  
    - [Inference Phi--Vision lokal](./md/01.Introduction/03/Vision_Inference.md)  
    - [Inference Phi mit Kaito AKS, Azure Containers (offizieller Support)](./md/01.Introduction/03/Kaito_Inference.md)  

- [Quantifizierung der Phi-Familie](./md/01.Introduction/04/QuantifyingPhi.md)  
    - [Quantisierung von Phi-3.5 / 4 mit llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
    - [Quantisierung von Phi-3.5 / 4 mit Generative AI Extensions für onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
    - [Quantisierung von Phi-3.5 / 4 mit Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
    - [Quantisierung von Phi-3.5 / 4 mit Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)  

- Evaluation von Phi  
    - [Verantwortungsvolle KI](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Azure AI Foundry für Evaluation](./md/01.Introduction/05/AIFoundry.md)  
    - [Evaluation mit Promptflow](./md/01.Introduction/05/Promptflow.md)  

- RAG mit Azure AI Search  
    - [Wie man Phi-4-mini und Phi-4-multimodal (RAG) mit Azure AI Search verwendet](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)  

- Phi-Anwendungsentwicklung - Beispiele  
  - Text- & Chat-Anwendungen  
    - Phi-4 Beispiele 🆕  
      - [📓] [Chat mit Phi-4-mini ONNX-Modell](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Chat mit lokalem Phi-4 ONNX-Modell in .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Chat .NET-Konsolenanwendung mit Phi-4 ONNX und Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 Beispiele  
      - [Lokaler Chatbot im Browser mit Phi3, ONNX Runtime Web und WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [Multi-Modell - Interaktives Phi-3-mini und OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - Wrapper erstellen und Phi-3 mit MLFlow verwenden](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [Modelloptimierung - So optimieren Sie das Phi-3-mini-Modell für ONNX Runtime Web mit Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [WinUI3-App mit Phi-3-mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [WinUI3 Multi-Modell KI-gestützte Notizen-App Beispiel](https://github.com/microsoft/ai-powered-notes-winui3-sample)  
      - [Feinabstimmung und Integration benutzerdefinierter Phi-3-Modelle mit Prompt Flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)  
      - [Feinabstimmung und Integration benutzerdefinierter Phi-3-Modelle mit Prompt Flow in Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)  
      - [Evaluierung des feinabgestimmten Phi-3 / Phi-3.5-Modells in Azure AI Foundry mit Fokus auf Microsofts Prinzipien für verantwortungsvolle KI](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)  
- [📓] [Phi-3.5-mini-instruct Sprachvorhersage-Beispiel (Chinesisch/Englisch)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Verwendung von Windows GPU zur Erstellung einer Prompt-Flow-Lösung mit Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Erstellen einer Android-App mit Microsoft Phi-3.5 tflite](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET Beispiel mit lokalem ONNX Phi-3-Modell unter Verwendung von Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konsolen-Chat .NET-App mit Semantic Kernel und Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Code-basierte Beispiele 
    - Phi-4 Beispiele 🆕
      - [📓] [Projektcode generieren mit Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 Beispiele
      - [Erstellen Sie Ihren eigenen Visual Studio Code GitHub Copilot Chat mit Microsoft Phi-3 Familie](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Erstellen Sie Ihren eigenen Visual Studio Code Chat Copilot Agent mit Phi-3.5 durch GitHub-Modelle](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Beispiele für fortgeschrittenes Denken
    - Phi-4 Beispiele 🆕
      - [📓] [Phi-4-mini Beispiele für fortgeschrittenes Denken](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
  
  - Demos
      - [Phi-4-mini Demos gehostet auf Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal Demos gehostet auf Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vision-Beispiele
    - Phi-4 Beispiele 🆕
      - [📓] [Verwendung von Phi-4-multimodal zum Lesen von Bildern und Generieren von Code](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 Beispiele
      -  [📓][Phi-3-vision-Bild Text zu Text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Visueller Sprachassistent - mit Phi3-Vision und OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision Mehrbild- oder Mehrrahmen-Beispiel](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision Lokales ONNX-Modell unter Verwendung von Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menübasierte Phi-3 Vision Lokales ONNX-Modell unter Verwendung von Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Audio-Beispiele
    - Phi-4 Beispiele 🆕
      - [📓] [Extrahieren von Audio-Transkripten mit Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal Audio-Beispiel](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal Sprachübersetzungsbeispiel](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET Konsolenanwendung mit Phi-4-multimodal Audio zur Analyse einer Audiodatei und Generierung eines Transkripts](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE-Beispiele
    - Phi-3 / 3.5 Beispiele
      - [📓] [Phi-3.5 Mixture of Experts Modelle (MoEs) Social Media Beispiel](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Erstellen einer Retrieval-Augmented Generation (RAG) Pipeline mit NVIDIA NIM Phi-3 MOE, Azure AI Search und LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - Beispiele für Funktionsaufrufe
    - Phi-4 Beispiele 🆕
      -  [📓] [Verwendung von Funktionsaufrufen mit Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
  - Beispiele für multimodales Mixing
    - Phi-4 Beispiele 🆕
-  [📓] [Verwendung von Phi-4-multimodal als Technologiejournalist](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET-Konsolenanwendung, die Phi-4-multimodal zur Bildanalyse verwendet](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Feinabstimmung von Phi-Beispielen
  - [Szenarien für Feinabstimmung](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Feinabstimmung vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Feinabstimmung: Lassen Sie Phi-3 ein Branchenexperte werden](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Feinabstimmung von Phi-3 mit dem AI Toolkit für VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Feinabstimmung von Phi-3 mit Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Feinabstimmung von Phi-3 mit Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Feinabstimmung von Phi-3 mit QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Feinabstimmung von Phi-3 mit Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Feinabstimmung von Phi-3 mit Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Feinabstimmung mit Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Feinabstimmung mit Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Feinabstimmung von Phi-3-vision mit Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Feinabstimmung von Phi-3 mit dem Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Feinabstimmung von Phi-3-vision (offizielle Unterstützung)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Feinabstimmung von Phi-3 mit Kaito AKS, Azure Containers (offizielle Unterstützung)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Feinabstimmung von Phi-3 und 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands-On Lab
  - [Erforschung modernster Modelle: LLMs, SLMs, lokale Entwicklung und mehr](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP-Potenzial freischalten: Feinabstimmung mit Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Akademische Forschungspapiere und Veröffentlichungen
  - [Textbooks Are All You Need II: phi-1.5 technischer Bericht](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Technischer Bericht: Ein hochleistungsfähiges Sprachmodell lokal auf Ihrem Telefon](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Technischer Bericht](https://arxiv.org/abs/2412.08905)
  - [Optimierung kleiner Sprachmodelle für fahrzeuginterne Funktionsaufrufe](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Feinabstimmung von PHI-3 für Multiple-Choice-Fragenbeantwortung: Methodik, Ergebnisse und Herausforderungen](https://arxiv.org/abs/2501.01588)

## Verwendung von Phi-Modellen

### Phi auf Azure AI Foundry

Erfahren Sie, wie Sie Microsoft Phi nutzen und End-to-End-Lösungen auf Ihren verschiedenen Hardwaregeräten erstellen können. Um Phi selbst auszuprobieren, beginnen Sie mit den Modellen und passen Sie Phi an Ihre Szenarien an, indem Sie den [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) verwenden. Weitere Informationen finden Sie unter Erste Schritte mit [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Playground**  
Jedes Modell verfügt über einen eigenen Playground, um das Modell zu testen: [Azure AI Playground](https://aka.ms/try-phi3).

### Phi auf GitHub-Modelle

Erfahren Sie, wie Sie Microsoft Phi nutzen und End-to-End-Lösungen auf Ihren verschiedenen Hardwaregeräten erstellen können. Um Phi selbst auszuprobieren, beginnen Sie mit dem Modell und passen Sie Phi an Ihre Szenarien an, indem Sie den [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) verwenden. Weitere Informationen finden Sie unter Erste Schritte mit [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Playground**  
Jedes Modell hat einen eigenen [Playground, um das Modell zu testen](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi auf Hugging Face

Das Modell ist auch auf [Hugging Face](https://huggingface.co/microsoft) verfügbar.

**Playground**  
[Hugging Chat Playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Verantwortungsbewusste KI

Microsoft engagiert sich dafür, seinen Kunden dabei zu helfen, unsere KI-Produkte verantwortungsvoll zu nutzen, unsere Erkenntnisse zu teilen und vertrauensbasierte Partnerschaften durch Tools wie Transparenzberichte und Wirkungsanalysen aufzubauen. Viele dieser Ressourcen finden Sie unter [https://aka.ms/RAI](https://aka.ms/RAI).  
Microsofts Ansatz für verantwortungsbewusste KI basiert auf unseren KI-Prinzipien: Fairness, Zuverlässigkeit und Sicherheit, Datenschutz und Sicherheit, Inklusivität, Transparenz und Verantwortlichkeit.

Groß angelegte Modelle für natürliche Sprache, Bilder und Sprache – wie die in diesem Beispiel verwendeten – können potenziell auf ungerechte, unzuverlässige oder anstößige Weise agieren und dadurch Schaden verursachen. Bitte lesen Sie die [Transparenzhinweise zum Azure OpenAI-Dienst](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), um sich über Risiken und Einschränkungen zu informieren.

Der empfohlene Ansatz zur Minderung dieser Risiken besteht darin, ein Sicherheitssystem in Ihre Architektur zu integrieren, das schädliches Verhalten erkennen und verhindern kann. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) bietet eine unabhängige Schutzebene, die in der Lage ist, schädliche Inhalte, die von Nutzern oder KI generiert wurden, in Anwendungen und Diensten zu erkennen. Azure AI Content Safety umfasst Text- und Bild-APIs, mit denen Sie schädliches Material erkennen können. Im Azure AI Foundry-Dienst ermöglicht der Content Safety-Dienst Ihnen, Beispielcode für die Erkennung schädlicher Inhalte in verschiedenen Modalitäten anzusehen, zu erkunden und auszuprobieren. Die folgende [Schnellstart-Dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) führt Sie durch die Erstellung von Anfragen an den Dienst.

Ein weiterer zu berücksichtigender Aspekt ist die Gesamtleistung der Anwendung. Bei multimodalen und Multi-Modell-Anwendungen bedeutet Leistung, dass das System so funktioniert, wie Sie und Ihre Nutzer es erwarten, einschließlich der Vermeidung schädlicher Ausgaben. Es ist wichtig, die Leistung Ihrer gesamten Anwendung mit [Evaluatoren für Leistung und Qualität sowie für Risiko und Sicherheit](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) zu bewerten. Sie haben auch die Möglichkeit, [benutzerdefinierte Evaluatoren](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) zu erstellen und zu nutzen.

Sie können Ihre KI-Anwendung in Ihrer Entwicklungsumgebung mit dem [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) bewerten. Mit einem Testdatensatz oder einem Ziel werden die generativen Ausgaben Ihrer KI-Anwendung quantitativ mit integrierten oder benutzerdefinierten Evaluatoren Ihrer Wahl gemessen. Um mit dem Azure AI Evaluation SDK zu beginnen und Ihr System zu bewerten, können Sie der [Schnellstart-Anleitung](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) folgen. Nach der Durchführung eines Bewertungslaufs können Sie die [Ergebnisse in Azure AI Foundry visualisieren](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marken

Dieses Projekt kann Marken oder Logos für Projekte, Produkte oder Dienstleistungen enthalten. Die autorisierte Verwendung von Microsoft-Marken oder -Logos unterliegt den [Microsoft-Markenzeichen- und Markenrichtlinien](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) und muss diesen entsprechen.  
Die Verwendung von Microsoft-Marken oder -Logos in modifizierten Versionen dieses Projekts darf keine Verwirrung stiften oder eine Unterstützung durch Microsoft implizieren. Jede Verwendung von Marken oder Logos Dritter unterliegt den Richtlinien der jeweiligen Dritten.

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-basierten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.