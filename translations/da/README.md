# Phi Cookbook: Praktiske Eksempler med Microsofts Phi Modeller

[![Åbn og brug eksemplerne i GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Åbn i Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub bidragsydere](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Velkommen](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub følgere](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stjerner](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi er en serie af open source AI-modeller udviklet af Microsoft.

Phi er i øjeblikket den mest kraftfulde og omkostningseffektive lille sprogmodel (SLM) med fremragende resultater inden for flersprogede opgaver, ræsonnement, tekst-/chatgenerering, kodning, billeder, lyd og andre scenarier.

Du kan implementere Phi i skyen eller på edge-enheder, og du kan nemt bygge generative AI-applikationer med begrænset computerkraft.

Følg disse trin for at komme i gang med at bruge disse ressourcer:
1. **Fork repository**: Klik [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klon repository**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Deltag i Microsoft AI Discord Community og mød eksperter og andre udviklere**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.da.png)

## Indholdsfortegnelse

- Introduktion
  - [Velkommen til Phi-familien](./md/01.Introduction/01/01.PhiFamily.md)
  - [Opsætning af dit miljø](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Forståelse af nøgleteknologier](./md/01.Introduction/01/01.Understandingtech.md)
  - [AI-sikkerhed for Phi-modeller](./md/01.Introduction/01/01.AISafety.md)
  - [Phi hardware-support](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi-modeller og tilgængelighed på tværs af platforme](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Brug af Guidance-ai og Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace-modeller](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- Inferens af Phi i forskellige miljøer
    - [Hugging Face](./md/01.Introduction/02/01.HF.md)
    - [GitHub-modeller](./md/01.Introduction/02/02.GitHubModel.md)
    - [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Inferens af Phi-familien
    - [Inferens af Phi på iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inferens af Phi på Android](./md/01.Introduction/03/Android_Inference.md)
- [Inference Phi i Jetson](./md/01.Introduction/03/Jetson_Inference.md)  
    - [Inference Phi på AI PC](./md/01.Introduction/03/AIPC_Inference.md)  
    - [Inference Phi med Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)  
    - [Inference Phi på Lokal Server](./md/01.Introduction/03/Local_Server_Inference.md)  
    - [Inference Phi på Fjernserver med AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)  
    - [Inference Phi med Rust](./md/01.Introduction/03/Rust_Inference.md)  
    - [Inference Phi--Vision lokalt](./md/01.Introduction/03/Vision_Inference.md)  
    - [Inference Phi med Kaito AKS, Azure Containers (officiel support)](./md/01.Introduction/03/Kaito_Inference.md)  

- [Kvantisering af Phi-familien](./md/01.Introduction/04/QuantifyingPhi.md)  
    - [Kvantisering af Phi-3.5 / 4 med llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
    - [Kvantisering af Phi-3.5 / 4 med Generative AI-udvidelser til onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
    - [Kvantisering af Phi-3.5 / 4 med Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
    - [Kvantisering af Phi-3.5 / 4 med Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)  

- Evaluering af Phi  
    - [Ansvarlig AI](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Azure AI Foundry til Evaluering](./md/01.Introduction/05/AIFoundry.md)  
    - [Brug af Promptflow til Evaluering](./md/01.Introduction/05/Promptflow.md)  

- RAG med Azure AI Search  
    - [Sådan bruges Phi-4-mini og Phi-4-multimodal (RAG) med Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)  

- Phi applikationsudviklings-eksempler  
  - Tekst- og chatapplikationer  
    - Phi-4 Eksempler 🆕  
      - [📓] [Chat med Phi-4-mini ONNX Model](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Chat med Phi-4 lokal ONNX Model .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Chat .NET Konsolapp med Phi-4 ONNX ved brug af Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 Eksempler  
      - [Lokal chatbot i browseren ved brug af Phi3, ONNX Runtime Web og WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [Multi Model - Interaktiv Phi-3-mini og OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - Bygning af en wrapper og brug af Phi-3 med MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [Modeloptimering - Sådan optimeres Phi-3-mini model til ONNX Runtime Web med Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [WinUI3 App med Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [WinUI3 Multi Model AI-drevet Notes App Eksempel](https://github.com/microsoft/ai-powered-notes-winui3-sample)  
      - [Finjuster og integrer brugerdefinerede Phi-3 modeller med Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)  
      - [Finjuster og integrer brugerdefinerede Phi-3 modeller med Prompt flow i Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)  
      - [Evaluer den finjusterede Phi-3 / Phi-3.5 Model i Azure AI Foundry med fokus på Microsofts principper for Ansvarlig AI](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)  
- [📓] [Phi-3.5-mini-instruct sprogforudsigelseseksempel (Kinesisk/Engelsk)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Brug af Windows GPU til at skabe Prompt flow-løsning med Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Brug af Microsoft Phi-3.5 tflite til at lave en Android-app](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET Eksempel med lokal ONNX Phi-3 model ved brug af Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konsol-chat .NET-app med Semantic Kernel og Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Kodebaserede Eksempler 
    - Phi-4 Eksempler 🆕
      - [📓] [Generer projektkode med Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 Eksempler
      - [Byg din egen Visual Studio Code GitHub Copilot Chat med Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Skab din egen Visual Studio Code Chat Copilot Agent med Phi-3.5 ved hjælp af GitHub-modeller](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Avancerede Reasoning Eksempler
    - Phi-4 Eksempler 🆕
      - [📓] [Phi-4-mini Reasoning Eksempler](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
  
  - Demoer
      - [Phi-4-mini demoer hostet på Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demoer hostet på Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vision Eksempler
    - Phi-4 Eksempler 🆕
      - [📓] [Brug Phi-4-multimodal til at læse billeder og generere kode](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 Eksempler
      - [📓][Phi-3-vision-Billedtekst til tekst](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Genbrug](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Visuel sprogassistent - med Phi3-Vision og OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision multi-frame eller multi-image eksempel](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision Lokal ONNX Model ved brug af Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menu-baseret Phi-3 Vision Lokal ONNX Model ved brug af Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Audio Eksempler
    - Phi-4 Eksempler 🆕
      - [📓] [Ekstrahering af lydtransskriptioner ved hjælp af Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal Audio Eksempel](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal Taleoversættelseseksempel](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET konsolapplikation ved brug af Phi-4-multimodal Audio til at analysere en lydfil og generere transskription](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE Eksempler
    - Phi-3 / 3.5 Eksempler
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) Social Media Eksempel](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Opbygning af en Retrieval-Augmented Generation (RAG) Pipeline med NVIDIA NIM Phi-3 MOE, Azure AI Search og LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - Funktionkald Eksempler
    - Phi-4 Eksempler 🆕
      - [📓] [Brug af Funktionkald med Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
  - Multimodal Mixing Eksempler
    - Phi-4 Eksempler 🆕
- [📓] [Brug af Phi-4-multimodal som teknologijournalist](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
  - [.NET-konsolapplikation, der bruger Phi-4-multimodal til at analysere billeder](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Finjustering af Phi-eksempler  
  - [Scenarier for finjustering](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Finjustering vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Finjustering: Lad Phi-3 blive en brancheekspert](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Finjustering af Phi-3 med AI Toolkit til VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Finjustering af Phi-3 med Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Finjustering af Phi-3 med Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [Finjustering af Phi-3 med QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Finjustering af Phi-3 med Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Finjustering af Phi-3 med Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Finjustering med Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Finjustering med Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)  
  - [Finjustering af Phi-3-vision med Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Finjustering af Phi-3 med Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Finjustering af Phi-3-vision (officiel support)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Finjustering af Phi-3 med Kaito AKS, Azure Containers (officiel support)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Finjustering af Phi-3 og 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands-On Lab  
  - [Udforskning af avancerede modeller: LLM'er, SLM'er, lokal udvikling og mere](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [Udnyt NLP's potentiale: Finjustering med Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Akademiske forskningsartikler og publikationer  
  - [Textbooks Are All You Need II: phi-1.5 teknisk rapport](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 teknisk rapport: En yderst kompetent sprogmodel lokalt på din telefon](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 teknisk rapport](https://arxiv.org/abs/2412.08905)  
  - [Optimering af små sprogmodeller til funktionelle opkald i køretøjer](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Finjustering af PHI-3 til multiple-choice spørgsmål: Metodologi, resultater og udfordringer](https://arxiv.org/abs/2501.01588)

## Brug af Phi-modeller

### Phi på Azure AI Foundry  

Du kan lære, hvordan du bruger Microsoft Phi, og hvordan du bygger end-to-end-løsninger på dine forskellige hardwareenheder. For at prøve Phi selv kan du starte med at eksperimentere med modellerne og tilpasse Phi til dine scenarier ved hjælp af [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Du kan lære mere ved at begynde med [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Playground**  
Hver model har en dedikeret playground til at teste modellen [Azure AI Playground](https://aka.ms/try-phi3).

### Phi på GitHub-modeller  

Du kan lære, hvordan du bruger Microsoft Phi, og hvordan du bygger end-to-end-løsninger på dine forskellige hardwareenheder. For at prøve Phi selv kan du starte med at eksperimentere med modellen og tilpasse Phi til dine scenarier ved hjælp af [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Du kan lære mere ved at begynde med [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Playground**
Hver model har en dedikeret [legeplads til at teste modellen](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi på Hugging Face

Du kan også finde modellen på [Hugging Face](https://huggingface.co/microsoft)

**Legeplads**  
[Hugging Chat legeplads](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Ansvarlig AI

Microsoft er forpligtet til at hjælpe vores kunder med at bruge vores AI-produkter ansvarligt, dele vores erfaringer og opbygge tillidsbaserede partnerskaber gennem værktøjer som Transparency Notes og Impact Assessments. Mange af disse ressourcer kan findes på [https://aka.ms/RAI](https://aka.ms/RAI).  
Microsofts tilgang til ansvarlig AI er baseret på vores AI-principper om retfærdighed, pålidelighed og sikkerhed, privatliv og sikkerhed, inklusion, gennemsigtighed og ansvarlighed.

Store sprog-, billed- og tale-modeller – som dem, der bruges i dette eksempel – kan potentielt opføre sig på måder, der er uretfærdige, upålidelige eller stødende, hvilket kan forårsage skader. Konsulter venligst [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) for at blive informeret om risici og begrænsninger.

Den anbefalede tilgang til at mindske disse risici er at inkludere et sikkerhedssystem i din arkitektur, der kan opdage og forhindre skadelig adfærd. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) tilbyder et uafhængigt lag af beskyttelse, der kan opdage skadeligt bruger- og AI-genereret indhold i applikationer og tjenester. Azure AI Content Safety inkluderer tekst- og billed-API'er, der gør det muligt at opdage skadeligt materiale. Inden for Azure AI Foundry giver Content Safety-tjenesten dig mulighed for at se, udforske og afprøve eksempler på kode til at opdage skadeligt indhold på tværs af forskellige modaliteter. Følgende [quickstart-dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) guider dig igennem, hvordan du laver forespørgsler til tjenesten.

En anden faktor, der skal tages i betragtning, er den overordnede applikationsydelse. For multimodale og multi-model applikationer betyder ydeevne, at systemet fungerer som forventet af dig og dine brugere, herunder ikke at generere skadelige output. Det er vigtigt at vurdere ydeevnen af din samlede applikation ved hjælp af [Performance and Quality og Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Du har også mulighed for at oprette og evaluere med [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Du kan evaluere din AI-applikation i dit udviklingsmiljø ved hjælp af [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Ved enten at bruge et testdatasæt eller et mål bliver dine generative AI-applikationers output kvantitativt målt med indbyggede eller brugerdefinerede evaluators efter eget valg. For at komme i gang med Azure AI Evaluation SDK til at evaluere dit system kan du følge [quickstart-guiden](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Når du har udført en evalueringskørsel, kan du [visualisere resultaterne i Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Varemærker

Dette projekt kan indeholde varemærker eller logoer for projekter, produkter eller tjenester. Autoriseret brug af Microsofts varemærker eller logoer er underlagt og skal følge [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Brug af Microsofts varemærker eller logoer i modificerede versioner af dette projekt må ikke skabe forvirring eller antyde Microsoft-sponsorering. Enhver brug af tredjeparts varemærker eller logoer er underlagt de pågældende tredjeparts politikker.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-baserede maskinoversættelsestjenester. Selvom vi bestræber os på at opnå nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.