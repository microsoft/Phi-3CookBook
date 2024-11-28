# Phi-3 Cookbook : Exemples pratiques avec les modèles Phi-3 de Microsoft

[![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

[![Contributeurs GitHub](https://img.shields.io/github/contributors/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Problèmes GitHub](https://img.shields.io/github/issues/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Pull-requests GitHub](https://img.shields.io/github/issues-pr/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Observateurs GitHub](https://img.shields.io/github/watchers/microsoft/phi-3cookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phi-3cookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Forks GitHub](https://img.shields.io/github/forks/microsoft/phi-3cookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phi-3cookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Étoiles GitHub](https://img.shields.io/github/stars/microsoft/phi-3cookbook?style=social&label=Star)](https://GitHub.com/microsoft/phi-3cookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi est une famille de modèles d'IA ouverts développés par Microsoft. Les modèles Phi sont les plus performants et les plus rentables parmi les petits modèles de langage (SLM) disponibles, surpassant les modèles de même taille et ceux de taille supérieure dans divers benchmarks de langage, de raisonnement, de codage et de mathématiques. La famille Phi-3 comprend des versions mini, petite, moyenne et vision, entraînées sur différentes quantités de paramètres pour répondre à divers scénarios d'application. Pour plus d'informations détaillées sur la famille Phi de Microsoft, veuillez visiter la page [Bienvenue dans la famille Phi](/md/01.Introduce/Phi3Family.md).

Suivez ces étapes :
1. **Forker le dépôt** : Cliquez sur le bouton "Fork" en haut à droite de cette page.
2. **Cloner le dépôt** : `git clone https://github.com/microsoft/Phi-3CookBook.git`

![Phi3Family](/imgs/00/Phi3getstarted.png)

## Table des matières

- Introduction
  - [Configurer votre environnement](./md/01.Introduce/EnvironmentSetup.md)(✅)
  - [Bienvenue dans la famille Phi](./md/01.Introduce/Phi3Family.md)(✅)
  - [Comprendre les technologies clés](./md/01.Introduce/Understandingtech.md)(✅)
  - [Sécurité de l'IA pour les modèles Phi](./md/01.Introduce/AISafety.md)(✅)
  - [Support matériel pour Phi-3](./md/01.Introduce/Hardwaresupport.md)(✅)
  - [Modèles Phi-3 et disponibilité sur les plateformes](./md/01.Introduce/Edgeandcloud.md)(✅)
  - [Utiliser Guidance-ai et Phi](./md/01.Introduce/Guidance.md)(✅)
  - [Modèles du GitHub Marketplace](https://github.com/marketplace/models)(✅)
  - [Catalogue de modèles Azure AI](https://ai.azure.com)(✅)

- Démarrage rapide
  - [Utiliser Phi-3 dans le catalogue de modèles GitHub](./md/02.QuickStart/GitHubModel_QuickStart.md)(✅)
  - [Utiliser Phi-3 dans Hugging Face](./md/02.QuickStart/Huggingface_QuickStart.md)(✅)
  - [Utiliser Phi-3 avec le SDK OpenAI](./md/02.QuickStart/OpenAISDK_Quickstart.md)(✅)
  - [Utiliser Phi-3 avec des requêtes HTTP](./md/02.QuickStart/HttpAPI_QuickStart.md)(✅)
  - [Utiliser Phi-3 dans Azure AI Studio](./md/02.QuickStart/AzureAIStudio_QuickStart.md)(✅)
  - [Utiliser l'inférence de modèle Phi-3 avec Azure MaaS ou MaaP](./md/02.QuickStart/AzureModel_Inference.md)(✅)
  - [Utiliser l'API d'inférence Azure avec GitHub et Azure AI](./md/02.QuickStart/AzureInferenceAPI_QuickStart.md)
  - [Déployer des modèles Phi-3 en tant qu'APIs serverless dans Azure AI Studio](./md/02.QuickStart/AzureAIStudio_MaaS.md)(✅)
  - [Utiliser Phi-3 dans Ollama](./md/02.QuickStart/Ollama_QuickStart.md)(✅)
- [Utiliser Phi-3 dans LM Studio](./md/02.QuickStart/LMStudio_QuickStart.md)(✅)
  - [Utiliser Phi-3 dans AI Toolkit VSCode](./md/02.QuickStart/AITookit_QuickStart.md)(✅)
  - [Utiliser Phi-3 et LiteLLM](./md/02.QuickStart/LiteLLM_QuickStart.md)(✅)
  
- [Inférence Phi-3](./md/03.Inference/overview.md)  
  - [Inférence Phi-3 sur iOS](./md/03.Inference/iOS_Inference.md)(✅)
  - [Inférence Phi-3.5 sur Android](./md/08.Update/Phi35/050.UsingPhi35TFLiteCreateAndroidApp.md)(✅)
  - [Inférence Phi-3 sur Jetson](./md/03.Inference/Jetson_Inference.md)(✅)
  - [Inférence Phi-3 sur PC AI](./md/03.Inference/AIPC_Inference.md)(✅)
  - [Inférence Phi-3 avec Apple MLX Framework](./md/03.Inference/MLX_Inference.md)(✅)
  - [Inférence Phi-3 sur Serveur Local](./md/03.Inference/Local_Server_Inference.md)(✅)
  - [Inférence Phi-3 sur Serveur Distant avec AI Toolkit](./md/03.Inference/Remote_Interence.md)(✅)
  - [Inférence Phi-3 avec Rust](./md/03.Inference/Rust_Inference.md)(✅)
  - [Inférence Phi-3-Vision en Local](./md/03.Inference/Vision_Inference.md)(✅)
  - [Inférence Phi-3 avec Kaito AKS, Azure Containers (support officiel)](./md/03.Inference/Kaito_Inference.md)(✅)
  - [Inférence de Votre Modèle Fine-tuning avec ONNX Runtime](./md/06.E2ESamples/E2E_Inference_ORT.md)(✅)

- Fine-tuning Phi-3
  - [Téléchargement & Création d'un Jeu de Données Exemple](./md/04.Fine-tuning/CreatingSampleData.md)(✅)
  - [Scénarios de Fine-tuning](./md/04.Fine-tuning/FineTuning_Scenarios.md)(✅)
  - [Fine-tuning vs RAG](./md/04.Fine-tuning/FineTuning_vs_RAG.md)(✅)
  - [Fine-tuning : Faire de Phi-3 un expert industriel](./md/04.Fine-tuning/LetPhi3gotoIndustriy.md)(✅)
  - [Fine-tuning Phi-3 avec AI Toolkit pour VS Code](./md/04.Fine-tuning/Finetuning_VSCodeaitoolkit.md)(✅)
  - [Fine-tuning Phi-3 avec Azure Machine Learning Service](./md/04.Fine-tuning/Introduce_AzureML.md)(✅)
  - [Fine-tuning Phi-3 avec Lora](./md/04.Fine-tuning/FineTuning_Lora.md)(✅)
  - [Fine-tuning Phi-3 avec QLora](./md/04.Fine-tuning/FineTuning_Qlora.md)(✅)
  - [Fine-tuning Phi-3 avec Azure AI Studio](./md/04.Fine-tuning/FineTuning_AIStudio.md)(✅)
  - [Fine-tuning Phi-3 avec Azure ML CLI/SDK](./md/04.Fine-tuning/FineTuning_MLSDK.md)(✅)
  - [Fine-tuning avec Microsoft Olive](./md/04.Fine-tuning/FineTuning_MicrosoftOlive.md)(✅)
  - [Fine-tuning avec Microsoft Olive Hands-On Lab](./code/04.Finetuning/olive-lab/readme.md)(✅)
  - [Fine-tuning Phi-3-vision avec Weights and Bias](./md/04.Fine-tuning/FineTuning_Phi-3-visionWandB.md)(✅)
  - [Fine-tuning Phi-3 avec Apple MLX Framework](./md/04.Fine-tuning/FineTuning_MLX.md)(✅)
  - [Fine-tuning Phi-3-vision (support officiel)](./md/04.Fine-tuning/FineTuning_Vision.md)(✅)
- [Fine-Tuning Phi-3 avec Kaito AKS, Azure Containers (support officiel)](./md/04.Fine-tuning/FineTuning_Kaito.md)(✅)
  - [Fine-Tuning Phi-3 et 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)(✅)

- Évaluation Phi-3
  - [Introduction à l'IA Responsable](./md/05.Evaluation/ResponsibleAI.md)(✅)
  - [Introduction à Promptflow](./md/05.Evaluation/Promptflow.md)(✅)
  - [Introduction à Azure AI Studio pour l'évaluation](./md/05.Evaluation/AzureAIStudio.md)(✅)

- Exemples E2E pour Phi-3-mini
  - [Introduction aux exemples de bout en bout](./md/06.E2ESamples/E2E_Introduction.md)(✅)
  - [Préparez vos données industrielles](./md/06.E2ESamples/E2E_Datasets.md)(✅)
  - [Utilisez Microsoft Olive pour architecturer vos projets](./md/06.E2ESamples/E2E_LoRA&QLoRA_Config_With_Olive.md)(✅)
  - [Chatbot local sur Android avec Phi-3, ONNXRuntime Mobile et ONNXRuntime Generate API](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/mobile/examples/phi-3/android)(✅)
  - [Démonstration Hugging Face Space WebGPU et Phi-3-mini - Phi-3-mini offre à l'utilisateur une expérience de chatbot privée (et puissante). Vous pouvez l'essayer](https://huggingface.co/spaces/Xenova/experimental-phi3-webgpu)(✅)
  - [Chatbot local dans le navigateur utilisant Phi3, ONNX Runtime Web et WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)(✅)
  - [Chat OpenVino](/md/06.E2ESamples/E2E_OpenVino_Chat.md)(✅)
  - [Multi Modèle - Phi-3-mini interactif et OpenAI Whisper](./md/06.E2ESamples/E2E_Phi-3-mini_with_whisper.md)(✅)
  - [MLFlow - Construire un wrapper et utiliser Phi-3 avec MLFlow](./md/06.E2ESamples/E2E_Phi-3-MLflow.md)(✅)
  - [Optimisation de modèle - Comment optimiser le modèle Phi-3-min pour ONNX Runtime Web avec Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)(✅)
  - [Application WinUI3 avec Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)(✅)
  - [Exemple d'application de notes alimentée par l'IA WinUI3 Multi Modèle](https://github.com/microsoft/ai-powered-notes-winui3-sample)(✅)
  - [Affiner et intégrer des modèles Phi-3 personnalisés avec Prompt flow](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)(✅)
  - [Affiner et intégrer des modèles Phi-3 personnalisés avec Prompt flow dans Azure AI Studio](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIstudio.md)(✅)
  - [Évaluer le modèle Phi-3 / Phi-3.5 affiné dans Azure AI Studio en se concentrant sur les principes de l'IA Responsable de Microsoft](./md/06.E2ESamples/E2E_Phi-3-Evaluation_AIstudio.md)(✅)
  - [Exemple de prédiction linguistique Phi-3.5-mini-instruct (Chinois/Anglais)](../../code/09.UpdateSamples/Aug/phi3-instruct-demo.ipynb)(✅)

- Exemples E2E pour Phi-3-vision
  - [Phi-3-vision-Image texte en texte](../../code/06.E2E/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)(✅)
  - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Phi-3-vision CLIP Embedding](./md/06.E2ESamples/E2E_Phi-3-Embedding_Images_with_CLIPVision.md)(✅)
  - [DEMO : Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)(✅)
  - [Phi-3-vision - Assistant visuel linguistique avec Phi3-Vision et OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)(✅)
  - [Phi-3 Vision Nvidia NIM](/md/06.E2ESamples/E2E_Nvidia_NIM_Vision.md)(✅)
  - [Phi-3 Vision OpenVino](/md/06.E2ESamples/E2E_OpenVino_Phi3Vision.md)(✅)
  - [Exemple multi-image ou multi-frame Phi-3.5 Vision](../../code/09.UpdateSamples/Aug/phi3-vision-demo.ipynb)(✅)

- Exemples E2E pour Phi-3.5-MoE
  - [Exemple de modèles Mixture of Experts (MoEs) Phi-3.5 pour les réseaux sociaux](../../code/09.UpdateSamples/Aug/phi3_moe_demo.ipynb)(✅)
- [Construire un pipeline de génération augmentée par récupération (RAG) avec NVIDIA NIM Phi-3 MOE, Azure AI Search et LlamaIndex](https://github.com/farzad528/azure-ai-search-python-playground/blob/main/azure-ai-search-nvidia-rag.ipynb)(✅)

- Exemples de laboratoires et d'ateliers Phi-3
  - [Laboratoires C# .NET](./md/07.Labs/Csharp/csharplabs.md)(✅)
  - [Construisez votre propre Visual Studio Code GitHub Copilot Chat avec Microsoft Phi-3 Family](./md/07.Labs/VSCode/README.md)(✅)
  - [Exemples de chatbot Mini RAG WebGPU Phi-3 avec fichier RAG local](./code/08.RAG/rag_webgpu_chat/README.md)(✅)
  - [Tutoriel Phi-3 ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-python.html)(✅)
  - [Tutoriel Phi-3-vision ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Exécuter les modèles Phi-3 avec l'API generate() d'ONNX Runtime](https://github.com/microsoft/onnxruntime-genai/blob/main/examples/python/phi-3-tutorial.md)(✅)
  - [Interface de chat Multi Modèle LLM Phi-3 ONNX, Ceci est une démo de chat](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/chat_app)(✅)
  - [Exemple C# Hello Phi-3 ONNX Phi-3](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi)(✅)
  - [Exemple d'API C# Phi-3 ONNX pour supporter Phi3-Vision](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi3V)(✅)
  - [Exécuter des exemples C# Phi-3 dans un CodeSpace](./md/07.Labs/CsharpOllamaCodeSpaces/CsharpOllamaCodeSpaces.md)(✅)
  - [Utiliser Phi-3 avec Promptflow et Azure AI Search](./code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md)(✅)
  - [API Windows AI-PC avec la bibliothèque Windows Copilot](https://developer.microsoft.com/windows/ai/?WT.mc_id=aiml-137032-kinfeylo)

- Apprentissage de Phi-3.5
  - [Quoi de neuf dans la famille Phi-3.5](./md/08.Update/Phi35/010.WhatsNewInPhi35.md)(✅)
  - [Quantification de la famille Phi-3.5](./md/08.Update/Phi35/020.QuantifyingPhi35.md)(✅)
    - [Quantification de Phi-3.5 avec llama.cpp](./md/08.Update/Phi35/021.UsingLlamacppQuantifyingPhi35.md)(✅)
    - [Quantification de Phi-3.5 avec les extensions d'IA générative pour onnxruntime](./md/08.Update/Phi35/022.UsingORTGenAIQuantifyingPhi35.md)(✅)
    - [Quantification de Phi-3.5 avec Intel OpenVINO](./md/08.Update/Phi35/023.UsingIntelOpenVINOQuantifyingPhi35.md)(✅)
    - [Quantification de Phi-3.5 avec le framework Apple MLX](./md/08.Update/Phi35/024.UsingAppleMLXQuantifyingPhi35.md)(✅)
  - Exemples d'applications Phi-3.5
    - [Chatbot RAG WebGPU Phi-3.5-Instruct](./md/08.Update/Phi35/031.WebGPUWithPhi35Readme.md)(✅)
    - [Créez votre propre agent de chat Copilot Visual Studio Code avec Phi-3.5 via les modèles GitHub](./md/08.Update/Phi35/032.CreateVSCodeChatAgentWithGitHubModels.md)(✅)
    - [Utiliser le GPU Windows pour créer une solution de flux d'invite avec Phi-3.5-Instruct ONNX](./md/08.Update/Phi35/040.UsingPromptFlowWithONNX.md)(✅)
    - [Utiliser Microsoft Phi-3.5 tflite pour créer une application Android](./md/08.Update/Phi35/050.UsingPhi35TFLiteCreateAndroidApp.md)(✅)


## Utiliser les modèles Phi-3

### Phi-3 sur Azure AI Studio

Vous pouvez apprendre à utiliser Microsoft Phi-3 et à créer des solutions E2E sur vos différents appareils matériels. Pour expérimenter Phi-3 par vous-même, commencez par jouer avec le modèle et personnaliser Phi-3 pour vos scénarios en utilisant le [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Vous pouvez en savoir plus en démarrant avec [Azure AI Studio](/md/02.QuickStart/AzureAIStudio_QuickStart.md)

**Playground**
Chaque modèle a un terrain de jeu dédié pour tester le modèle [Azure AI Playground](https://aka.ms/try-phi3).

### Phi-3 sur les modèles GitHub

Vous pouvez apprendre à utiliser Microsoft Phi-3 et à créer des solutions E2E sur vos différents appareils matériels. Pour expérimenter Phi-3 par vous-même, commencez par jouer avec le modèle et personnaliser Phi-3 pour vos scénarios en utilisant le [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Vous pouvez en savoir plus en démarrant avec [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**
Chaque modèle a un [terrain de jeu dédié pour tester le modèle](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi-3 sur Hugging Face

Vous pouvez également trouver le modèle sur [Hugging Face](https://huggingface.co/microsoft)

**Playground**
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🌐 Support Multilingue

> **Note:**
> Ces traductions ont été générées automatiquement à l'aide de l'outil open-source [co-op-translator](https://github.com/Azure/co-op-translator) et peuvent contenir des erreurs ou des inexactitudes. Pour des informations cruciales, il est recommandé de se référer à l'original ou de consulter une traduction humaine professionnelle. Si vous souhaitez ajouter ou mettre à jour une traduction, veuillez vous référer au dépôt [co-op-translator](https://github.com/Azure/co-op-translator), où vous pouvez facilement contribuer en utilisant des commandes simples.

| Langue               | Code | Lien vers le README traduit                             | Dernière mise à jour |
|----------------------|------|---------------------------------------------------------|----------------------|
| Chinois (Simplifié)  | zh   | [Traduction en chinois](../zh/README.md)    | 2024-10-04           |
| Chinois (Traditionnel)| tw  | [Traduction en chinois](../tw/README.md)    | 2024-10-04           |
| Français             | fr   | [Traduction en français](./README.md)   | 2024-10-04           |
| Japonais             | ja   | [Traduction en japonais](../ja/README.md)   | 2024-10-04           |
| Coréen               | ko   | [Traduction en coréen](../ko/README.md)     | 2024-10-04           |
| Espagnol             | es   | [Traduction en espagnol](../es/README.md)   | 2024-10-04           |

## Marques de commerce

Ce projet peut contenir des marques de commerce ou des logos pour des projets, produits ou services. L'utilisation autorisée des marques de commerce ou des logos de Microsoft est soumise aux [Directives d'utilisation des marques et de la marque Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
L'utilisation des marques de commerce ou des logos de Microsoft dans des versions modifiées de ce projet ne doit pas créer de confusion ou impliquer un parrainage de Microsoft. Toute utilisation de marques de commerce ou de logos de tiers est soumise aux politiques de ces tiers.

**Avertissement**:
Ce document a été traduit en utilisant des services de traduction automatique basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.