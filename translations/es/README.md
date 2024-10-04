# Phi-3 Cookbook: Ejemplos Prácticos con los Modelos Phi-3 de Microsoft

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

Phi es una familia de modelos de IA abierta desarrollada por Microsoft. Los modelos Phi son los modelos de lenguaje pequeño (SLM) más capaces y rentables disponibles, superando a modelos del mismo tamaño y del siguiente tamaño en una variedad de pruebas de lenguaje, razonamiento, codificación y matemáticas. La Familia Phi-3 incluye versiones mini, pequeñas, medianas y de visión, entrenadas con diferentes cantidades de parámetros para servir diversos escenarios de aplicación. Para información más detallada sobre la familia Phi de Microsoft, por favor visita la página de [Bienvenido a la Familia Phi](/md/01.Introduce/Phi3Family.md).

![Phi3Family](/imgs/00/Phi3getstarted.png)

## Tabla de Contenidos

- Introducción
  - [Configurando tu entorno](./md/01.Introduce/EnvironmentSetup.md)(✅)
  - [Bienvenido a la Familia Phi](./md/01.Introduce/Phi3Family.md)(✅)
  - [Entendiendo Tecnologías Clave](./md/01.Introduce/Understandingtech.md)(✅)
  - [Seguridad de IA para Modelos Phi](./md/01.Introduce/AISafety.md)(✅)
  - [Soporte de Hardware para Phi-3](./md/01.Introduce/Hardwaresupport.md)(✅)
  - [Modelos Phi-3 y Disponibilidad en diversas plataformas](./md/01.Introduce/Edgeandcloud.md)(✅)
  - [Usando Guidance-ai y Phi](./md/01.Introduce/Guidance.md)(✅)

- Inicio Rápido
  - [Usando Phi-3 en el Catálogo de Modelos de GitHub](./md/02.QuickStart/GitHubModel_QuickStart.md)(✅)
  - [Usando Phi-3 en Hugging face](./md/02.QuickStart/Huggingface_QuickStart.md)(✅)
  - [Usando Phi-3 con OpenAI SDK](./md/02.QuickStart/OpenAISDK_Quickstart.md)(✅)
  - [Usando Phi-3 con Solicitudes Http](./md/02.QuickStart/HttpAPI_QuickStart.md)(✅)
  - [Usando Phi-3 en Azure AI Studio](./md/02.QuickStart/AzureAIStudio_QuickStart.md)(✅)
  - [Usando la Inferencia de Modelos Phi-3 con Azure MaaS o MaaP](./md/02.QuickStart/AzureModel_Inference.md)(✅)
  - [Desplegando modelos Phi-3 como APIs serverless en Azure AI Studio](./md/02.QuickStart/AzureAIStudio_MaaS.md)(✅)
  - [Usando Phi-3 en Ollama](./md/02.QuickStart/Ollama_QuickStart.md)(✅)
  - [Usando Phi-3 en LM Studio](./md/02.QuickStart/LMStudio_QuickStart.md)(✅)
  - [Usando Phi-3 en AI Toolkit VSCode](./md/02.QuickStart/AITookit_QuickStart.md)(✅)
  - [Usando Phi-3 y LiteLLM](./md/02.QuickStart/LiteLLM_QuickStart.md)(✅)
- [Inferencia Phi-3](./md/03.Inference/overview.md)  
  - [Inferencia Phi-3 en iOS](./md/03.Inference/iOS_Inference.md)(✅)
  - [Inferencia Phi-3 en Jetson](./md/03.Inference/Jetson_Inference.md)(✅)
  - [Inferencia Phi-3 en PC de IA](./md/03.Inference/AIPC_Inference.md)(✅)
  - [Inferencia Phi-3 con Apple MLX Framework](./md/03.Inference/MLX_Inference.md)(✅)
  - [Inferencia Phi-3 en Servidor Local](./md/03.Inference/Local_Server_Inference.md)(✅)
  - [Inferencia Phi-3 en Servidor Remoto usando AI Toolkit](./md/03.Inference/Remote_Interence.md)(✅)
  - [Inferencia Phi-3 con Rust](./md/03.Inference/Rust_Inference.md)(✅)
  - [Inferencia Phi-3-Vision en Local](./md/03.Inference/Vision_Inference.md)(✅)
  - [Inferencia Phi-3 con Kaito AKS, Contenedores de Azure (soporte oficial)](./md/03.Inference/Kaito_Inference.md)(✅)
  - [Inferencia de Tu Modelo Ajustado con ONNX Runtime](./md/06.E2ESamples/E2E_Inference_ORT.md)(✅)

- Ajuste fino de Phi-3
  - [Descargando y Creando Conjunto de Datos de Muestra](./md/04.Fine-tuning/CreatingSampleData.md)(✅)
  - [Escenarios de Ajuste Fino](./md/04.Fine-tuning/FineTuning_Scenarios.md)(✅)
  - [Ajuste Fino vs RAG](./md/04.Fine-tuning/FineTuning_vs_RAG.md)(✅)
  - [Ajuste Fino: Convirtiendo a Phi-3 en un experto de la industria](./md/04.Fine-tuning/LetPhi3gotoIndustriy.md)(✅)
  - [Ajuste Fino de Phi-3 con AI Toolkit para VS Code](./md/04.Fine-tuning/Finetuning_VSCodeaitoolkit.md)(✅)
  - [Ajuste Fino de Phi-3 con Azure Machine Learning Service](./md/04.Fine-tuning/Introduce_AzureML.md)(✅)
  - [Ajuste Fino de Phi-3 con Lora](./md/04.Fine-tuning/FineTuning_Lora.md)(✅)
  - [Ajuste Fino de Phi-3 con QLora](./md/04.Fine-tuning/FineTuning_Qlora.md)(✅)
  - [Ajuste Fino de Phi-3 con Azure AI Studio](./md/04.Fine-tuning/FineTuning_AIStudio.md)(✅)
  - [Ajuste Fino de Phi-3 con Azure ML CLI/SDK](./md/04.Fine-tuning/FineTuning_MLSDK.md)(✅)
  - [Ajuste Fino con Microsoft Olive](./md/04.Fine-tuning/FineTuning_MicrosoftOlive.md)(✅)
  - [Ajuste Fino de Phi-3-vision con Weights and Bias](./md/04.Fine-tuning/FineTuning_Phi-3-visionWandB.md)(✅)
  - [Ajuste Fino de Phi-3 con Apple MLX Framework](./md/04.Fine-tuning/FineTuning_MLX.md)(✅)
  - [Ajuste Fino de Phi-3-vision (soporte oficial)](./md/04.Fine-tuning/FineTuning_Vision.md)(✅)
  - [Ajuste Fino de Phi-3 con Kaito AKS, Contenedores de Azure (soporte oficial)](./md/04.Fine-tuning/FineTuning_Kaito.md)(✅)
  - [Ajuste Fino de Phi-3 y 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)(✅)

- Evaluación Phi-3
  - [Introducción a la IA Responsable](./md/05.Evaluation/ResponsibleAI.md)(✅)
  - [Introducción a Promptflow](./md/05.Evaluation/Promptflow.md)(✅)
  - [Introducción a Azure AI Studio para evaluación](./md/05.Evaluation/AzureAIStudio.md)(✅)

- Ejemplos E2E para Phi-3-mini
- [Introducción a las muestras de extremo a extremo](./md/06.E2ESamples/E2E_Introduction.md)(✅)
  - [Prepara tus datos industriales](./md/06.E2ESamples/E2E_Datasets.md)(✅)
  - [Usa Microsoft Olive para diseñar tus proyectos](./md/06.E2ESamples/E2E_LoRA&QLoRA_Config_With_Olive.md)(✅)
  - [Chatbot local en Android con Phi-3, ONNXRuntime Mobile y ONNXRuntime Generate API](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/mobile/examples/phi-3/android)(✅)
  - [Demostración de Hugging Face Space WebGPU y Phi-3-mini - Phi-3-mini ofrece al usuario una experiencia de chatbot privada (y poderosa). Puedes probarlo](https://huggingface.co/spaces/Xenova/experimental-phi3-webgpu)(✅)
  - [Chatbot local en el navegador usando Phi3, ONNX Runtime Web y WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)(✅)
  - [Chat OpenVino](/md/06.E2ESamples/E2E_OpenVino_Chat.md)(✅)
  - [Modelo múltiple - Phi-3-mini interactivo y OpenAI Whisper](./md/06.E2ESamples/E2E_Phi-3-mini_with_whisper.md)(✅)
  - [MLFlow - Construyendo un envoltorio y usando Phi-3 con MLFlow](./md/06.E2ESamples/E2E_Phi-3-MLflow.md)(✅)
  - [Optimización del modelo - Cómo optimizar el modelo Phi-3-min para ONNX Runtime Web con Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)(✅)
  - [Aplicación WinUI3 con Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)(✅)
  - [Ejemplo de aplicación de notas con IA multimodelo en WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)(✅)
  - [Ajusta e integra modelos personalizados de Phi-3 con Prompt flow](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)(✅)
  - [Ajusta e integra modelos personalizados de Phi-3 con Prompt flow en Azure AI Studio](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIstudio.md)(✅)
  - [Evalúa el modelo ajustado Phi-3 / Phi-3.5 en Azure AI Studio enfocándose en los principios de IA Responsable de Microsoft](./md/06.E2ESamples/E2E_Phi-3-Evaluation_AIstudio.md)(✅)
  - [Ejemplo de predicción de lenguaje con Phi-3.5-mini-instruct (Chino/Inglés)](../../code/09.UpdateSamples/Aug/phi3-instruct-demo.ipynb)(✅)

- Muestras de extremo a extremo para Phi-3-vision
  - [Phi-3-vision - Imagen texto a texto](../../code/06.E2E/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)(✅)
  - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Phi-3-vision CLIP Embedding](./md/06.E2ESamples/E2E_Phi-3-Embedding_Images_with_CLIPVision.md)(✅)
  - [DEMO: Phi-3 Reciclaje](https://github.com/jennifermarsman/PhiRecycling/)(✅)
  - [Phi-3-vision - Asistente visual de lenguaje con Phi3-Vision y OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)(✅)
  - [Phi-3 Vision Nvidia NIM](/md/06.E2ESamples/E2E_Nvidia_NIM_Vision.md)(✅)
  - [Phi-3 Vision OpenVino](/md/06.E2ESamples/E2E_OpenVino_Phi3Vision.md)(✅)
  - [Ejemplo de múltiples fotogramas o imágenes con Phi-3.5 Vision](../../code/09.UpdateSamples/Aug/phi3-vision-demo.ipynb)(✅)

- Muestras de extremo a extremo para Phi-3.5-MoE
  - [Modelos de mezcla de expertos Phi-3.5 (MoEs) Ejemplo de redes sociales](../../code/09.UpdateSamples/Aug/phi3_moe_demo.ipynb)(✅)
  - [Construyendo una tubería de generación aumentada por recuperación (RAG) con NVIDIA NIM Phi-3 MOE, Azure AI Search y LlamaIndex](https://github.com/farzad528/azure-ai-search-python-playground/blob/main/azure-ai-search-nvidia-rag.ipynb)(✅)

- Ejemplos de laboratorios y talleres Phi-3
  - [Laboratorios C# .NET](./md/07.Labs/Csharp/csharplabs.md)(✅)
  - [Construye tu propio chat de GitHub Copilot en Visual Studio Code con la familia Microsoft Phi-3](./md/07.Labs/VSCode/README.md)(✅)
  - [Ejemplos de chatbot RAG local con WebGPU Phi-3 Mini y archivo RAG local](./code/08.RAG/rag_webgpu_chat/README.md)(✅)
  - [Tutorial de Phi-3 ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-python.html)(✅)
- [Tutorial de Phi-3-vision ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Ejecutar los modelos Phi-3 con la API generate() de ONNX Runtime](https://github.com/microsoft/onnxruntime-genai/blob/main/examples/python/phi-3-tutorial.md)(✅)
  - [Interfaz de Chat Multi Modelo LLM Phi-3 ONNX, Esta es una demo de chat](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/chat_app)(✅)
  - [Ejemplo en C# Hello Phi-3 ONNX Phi-3](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi)(✅)
  - [Ejemplo de API en C# Phi-3 ONNX para soportar Phi3-Vision](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi3V)(✅)
  - [Ejecutar ejemplos de C# Phi-3 en un CodeSpace](./md/07.Labs/CsharpOllamaCodeSpaces/CsharpOllamaCodeSpaces.md)(✅)
  - [Usando Phi-3 con Promptflow y Azure AI Search](./code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md)(✅)
  - [APIs de Windows AI-PC con Windows Copilot Library](https://developer.microsoft.com/windows/ai/?WT.mc_id=aiml-137032-kinfeylo)

- Aprendiendo Phi-3.5
  - [Novedades de la Familia Phi-3.5](./md/08.Update/Phi35/010.WhatsNewInPhi35.md)(✅)
  - [Cuantificación de la Familia Phi-3.5](./md/08.Update/Phi35/020.QuantifyingPhi35.md)(✅)
    - [Cuantificación de Phi-3.5 usando llama.cpp](./md/08.Update/Phi35/021.UsingLlamacppQuantifyingPhi35.md)(✅)
    - [Cuantificación de Phi-3.5 usando extensiones de IA Generativa para onnxruntime](./md/08.Update/Phi35/022.UsingORTGenAIQuantifyingPhi35.md)(✅)
    - [Cuantificación de Phi-3.5 usando Intel OpenVINO](./md/08.Update/Phi35/023.UsingIntelOpenVINOQuantifyingPhi35.md)(✅)
    - [Cuantificación de Phi-3.5 usando Apple MLX Framework](./md/08.Update/Phi35/024.UsingAppleMLXQuantifyingPhi35.md)(✅)
  - Ejemplos de Aplicación Phi-3.5
    - [Chatbot RAG WebGPU Phi-3.5-Instruct](./md/08.Update/Phi35/031.WebGPUWithPhi35Readme.md)(✅)
    - [Crea tu propio Agente de Chat Copilot en Visual Studio Code con Phi-3.5 usando Modelos de GitHub](./md/08.Update/Phi35/032.CreateVSCodeChatAgentWithGitHubModels.md)(✅)

## Usando Modelos Phi-3

### Phi-3 en Azure AI Studio

Puedes aprender a usar Microsoft Phi-3 y cómo construir soluciones E2E en tus diferentes dispositivos de hardware. Para experimentar Phi-3 por ti mismo, comienza jugando con el modelo y personalizando Phi-3 para tus escenarios usando el [Azure AI Studio, Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) puedes aprender más en la Guía de Inicio Rápido con [Azure AI Studio](/md/02.QuickStart/AzureAIStudio_QuickStart.md)

**Playground**
Cada modelo tiene un playground dedicado para probar el modelo [Azure AI Playground](https://aka.ms/try-phi3).

### Phi-3 en Modelos de GitHub

Puedes aprender a usar Microsoft Phi-3 y cómo construir soluciones E2E en tus diferentes dispositivos de hardware. Para experimentar Phi-3 por ti mismo, comienza jugando con el modelo y personalizando Phi-3 para tus escenarios usando el [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) puedes aprender más en la Guía de Inicio Rápido con [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**
Cada modelo tiene un [playground dedicado para probar el modelo](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi-3 en Hugging Face

También puedes encontrar el modelo en [Hugging Face](https://huggingface.co/microsoft)

**Playground**
[playground de Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🌐 Soporte Multilenguaje

> **Note:**
> Estas traducciones fueron generadas automáticamente usando el traductor de código abierto [co-op-translator](https://github.com/Azure/co-op-translator) y pueden contener errores o inexactitudes. Para información crítica, se recomienda referirse al original o consultar una traducción profesional humana. Si deseas agregar o actualizar una traducción, por favor consulta el repositorio de [co-op-translator](https://github.com/Azure/co-op-translator), donde puedes contribuir fácilmente usando comandos simples.

| Idioma               | Código | Enlace al README Traducido                             | Última Actualización |
|----------------------|--------|-------------------------------------------------------|----------------------|
| Chino (Simplificado) | zh     | [Traducción al Chino](../zh/README.md)    | 2024-10-04           |
| Chino (Tradicional)  | tw     | [Traducción al Chino](../tw/README.md)    | 2024-10-04           |
| Francés              | fr     | [Traducción al Francés](../fr/README.md)  | 2024-10-04           |
| Japonés              | ja     | [Traducción al Japonés](../ja/README.md)  | 2024-10-04           |
| Korean               | ko   | [Traducción al Coreana](../ko/README.md)       | 2024-10-04   |
| Spanish              | es   | [Traducción al Española](./README.md)      | 2024-10-04   |

## Marcas Registradas

Este proyecto puede contener marcas registradas o logotipos de proyectos, productos o servicios. El uso autorizado de las marcas registradas o logotipos de Microsoft está sujeto a y debe seguir las [Directrices de Marca y Uso de Marcas Registradas de Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
El uso de marcas registradas o logotipos de Microsoft en versiones modificadas de este proyecto no debe causar confusión ni implicar patrocinio de Microsoft. Cualquier uso de marcas registradas o logotipos de terceros está sujeto a las políticas de esos terceros.

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por lograr la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción humana profesional. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.