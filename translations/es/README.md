# Phi-3 Cookbook: Ejemplos Prácticos con los Modelos Phi-3 de Microsoft

[![Abrir y usar los ejemplos en GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)
[![Abrir en Contenedores de Desarrollo](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

[![Contribuidores de GitHub](https://img.shields.io/github/contributors/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Problemas de GitHub](https://img.shields.io/github/issues/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Pull-requests de GitHub](https://img.shields.io/github/issues-pr/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Bienvenidos](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Observadores de GitHub](https://img.shields.io/github/watchers/microsoft/phi-3cookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phi-3cookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Bifurcaciones de GitHub](https://img.shields.io/github/forks/microsoft/phi-3cookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phi-3cookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Estrellas de GitHub](https://img.shields.io/github/stars/microsoft/phi-3cookbook?style=social&label=Star)](https://GitHub.com/microsoft/phi-3cookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Discord de la Comunidad de Azure AI](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi es una familia de modelos de IA abiertos desarrollados por Microsoft. Los modelos Phi son los modelos de lenguaje pequeño (SLMs) más capaces y rentables disponibles, superando a modelos del mismo tamaño y de tamaño superior en una variedad de pruebas de lenguaje, razonamiento, codificación y matemáticas. La Familia Phi-3 incluye versiones mini, pequeñas, medianas y de visión, entrenadas con diferentes cantidades de parámetros para servir a varios escenarios de aplicación. Para obtener información más detallada sobre la familia Phi de Microsoft, por favor visita la página [Bienvenido a la Familia Phi](/md/01.Introduce/Phi3Family.md).

![Phi3Family](/imgs/00/Phi3getstarted.png)

## Tabla de Contenidos

- Introducción
  - [Configurando tu entorno](./md/01.Introduce/EnvironmentSetup.md)(✅)
  - [Bienvenido a la Familia Phi](./md/01.Introduce/Phi3Family.md)(✅)
  - [Entendiendo Tecnologías Clave](./md/01.Introduce/Understandingtech.md)(✅)
  - [Seguridad de IA para Modelos Phi](./md/01.Introduce/AISafety.md)(✅)
  - [Soporte de Hardware para Phi-3](./md/01.Introduce/Hardwaresupport.md)(✅)
  - [Modelos Phi-3 y Disponibilidad en Plataformas](./md/01.Introduce/Edgeandcloud.md)(✅)
  - [Usando Guidance-ai y Phi](./md/01.Introduce/Guidance.md)(✅)

- Inicio Rápido
  - [Usando Phi-3 en el Catálogo de Modelos de GitHub](./md/02.QuickStart/GitHubModel_QuickStart.md)(✅)
  - [Usando Phi-3 en Hugging Face](./md/02.QuickStart/Huggingface_QuickStart.md)(✅)
  - [Usando Phi-3 con OpenAI SDK](./md/02.QuickStart/OpenAISDK_Quickstart.md)(✅)
  - [Usando Phi-3 con Solicitudes Http](./md/02.QuickStart/HttpAPI_QuickStart.md)(✅)
  - [Usando Phi-3 en Azure AI Studio](./md/02.QuickStart/AzureAIStudio_QuickStart.md)(✅)
  - [Usando Inferencia de Modelos Phi-3 con Azure MaaS o MaaP](./md/02.QuickStart/AzureModel_Inference.md)(✅)
  - [Desplegando modelos Phi-3 como APIs sin servidor en Azure AI Studio](./md/02.QuickStart/AzureAIStudio_MaaS.md)(✅)
  - [Usando Phi-3 en Ollama](./md/02.QuickStart/Ollama_QuickStart.md)(✅)
  - [Usando Phi-3 en LM Studio](./md/02.QuickStart/LMStudio_QuickStart.md)(✅)
  - [Usando Phi-3 en AI Toolkit VSCode](./md/02.QuickStart/AITookit_QuickStart.md)(✅)
  - [Usando Phi-3 y LiteLLM](./md/02.QuickStart/LiteLLM_QuickStart.md)(✅)

- [Prepara tus datos de la industria](./md/06.E2ESamples/E2E_Datasets.md)(✅)
  - [Usa Microsoft Olive para diseñar tus proyectos](./md/06.E2ESamples/E2E_LoRA&QLoRA_Config_With_Olive.md)(✅)
  - [Chatbot local en Android con Phi-3, ONNXRuntime Mobile y ONNXRuntime Generate API](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/mobile/examples/phi-3/android)(✅)
  - [Hugging Face Space WebGPU y Demo de Phi-3-mini - Phi-3-mini ofrece al usuario una experiencia de chatbot privada (y poderosa). Puedes probarlo](https://huggingface.co/spaces/Xenova/experimental-phi3-webgpu)(✅)
  - [Chatbot local en el navegador usando Phi3, ONNX Runtime Web y WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)(✅)
  - [Chat OpenVino](/md/06.E2ESamples/E2E_OpenVino_Chat.md)(✅)
  - [Multi Modelo - Phi-3-mini interactivo y OpenAI Whisper](./md/06.E2ESamples/E2E_Phi-3-mini_with_whisper.md)(✅)
  - [MLFlow - Construyendo un wrapper y usando Phi-3 con MLFlow](./md/06.E2ESamples/E2E_Phi-3-MLflow.md)(✅)
  - [Optimización de Modelos - Cómo optimizar el modelo Phi-3-min para ONNX Runtime Web con Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)(✅)
  - [App WinUI3 con Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)(✅)
  - [Ejemplo de App de Notas AI Potenciada Multi Modelo en WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)(✅)
  - [Ajuste fino e integración de modelos Phi-3 personalizados con Prompt flow](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)(✅)
  - [Ajuste fino e integración de modelos Phi-3 personalizados con Prompt flow en Azure AI Studio](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIstudio.md)(✅)
  - [Ejemplo de predicción de lenguaje Phi-3.5-mini-instruct (Chino/Inglés)](../../code/09.UpdateSamples/Aug/phi3-instruct-demo.ipynb)(✅)

- Ejemplos E2E para Phi-3-vision
  - [Phi-3-vision-Texto de imagen a texto](../../code/06.E2E/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)(✅)
  - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Phi-3-vision Embedding CLIP](./md/06.E2ESamples/E2E_Phi-3-Embedding_Images_with_CLIPVision.md)(✅)
  - [DEMO: Phi-3 Reciclaje](https://github.com/jennifermarsman/PhiRecycling/)(✅)
  - [Phi-3-vision - Asistente visual de lenguaje con Phi3-Vision y OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)(✅)
  - [Phi-3 Vision Nvidia NIM](/md/06.E2ESamples/E2E_Nvidia_NIM_Vision.md)(✅)
  - [Phi-3 Vision OpenVino](/md/06.E2ESamples/E2E_OpenVino_Phi3Vision.md)(✅)
  - [Ejemplo multi-frame o multi-imagen Phi-3.5 Vision](../../code/09.UpdateSamples/Aug/phi3-vision-demo.ipynb)(✅)

- Ejemplos E2E para Phi-3.5-MoE
  - [Phi-3.5 Modelos Mixture of Experts (MoEs) Ejemplo de Redes Sociales](../../code/09.UpdateSamples/Aug/phi3_moe_demo.ipynb)(✅)
  - [Construyendo una pipeline de Generación Aumentada por Recuperación (RAG) con NVIDIA NIM Phi-3 MOE, Azure AI Search, y LlamaIndex](https://github.com/farzad528/azure-ai-search-python-playground/blob/main/azure-ai-search-nvidia-rag.ipynb)(✅)

- Ejemplos de laboratorios y talleres Phi-3
  - [Laboratorios C# .NET](./md/07.Labs/Csharp/csharplabs.md)(✅)
  - [Construye tu propio Chat de Visual Studio Code GitHub Copilot con Microsoft Phi-3 Family](./md/07.Labs/VSCode/README.md)(✅)
  - [Ejemplos de Chatbot RAG local con WebGPU Phi-3 Mini con archivo RAG local](./code/08.RAG/rag_webgpu_chat/README.md)(✅)
  - [Tutorial de Phi-3 ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-python.html)(✅)
  - [Tutorial de Phi-3-vision ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Ejecuta los modelos Phi-3 con la API generate() de ONNX Runtime](https://github.com/microsoft/onnxruntime-genai/blob/main/examples/python/phi-3-tutorial.md)(✅)
- [Phi-3 ONNX Multi Model LLM Chat UI, Este es un demo de chat](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/chat_app)(✅)
  - [Ejemplo de C# Hello Phi-3 ONNX Phi-3](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi)(✅)
  - [Ejemplo de API C# Phi-3 ONNX para soportar Phi3-Vision](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi3V)(✅)
  - [Ejecutar ejemplos de C# Phi-3 en un CodeSpace](./md/07.Labs/CsharpOllamaCodeSpaces/CsharpOllamaCodeSpaces.md)(✅)
  - [Usando Phi-3 con Promptflow y Azure AI Search](./code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md)(✅)
  - [APIs de Windows AI-PC con Windows Copilot Library](https://developer.microsoft.com/windows/ai/?WT.mc_id=aiml-137032-kinfeylo)

- Aprendiendo Phi-3.5
  - [Novedades de la familia Phi-3.5](./md/08.Update/Phi35/010.WhatsNewInPhi35.md)(✅)
  - [Cuantificación de la familia Phi-3.5](./md/08.Update/Phi35/020.QuantifyingPhi35.md)(✅)
    - [Cuantificación de Phi-3.5 usando llama.cpp](./md/08.Update/Phi35/021.UsingLlamacppQuantifyingPhi35.md)(✅)
    - [Cuantificación de Phi-3.5 usando extensiones de IA generativa para onnxruntime](./md/08.Update/Phi35/022.UsingORTGenAIQuantifyingPhi35.md)(✅)
    - [Cuantificación de Phi-3.5 usando Intel OpenVINO](./md/08.Update/Phi35/023.UsingIntelOpenVINOQuantifyingPhi35.md)(✅)
    - [Cuantificación de Phi-3.5 usando Apple MLX Framework](./md/08.Update/Phi35/024.UsingAppleMLXQuantifyingPhi35.md)(✅)
  - Ejemplos de Aplicaciones de Phi-3.5
    - [Chatbot Phi-3.5-Instruct WebGPU RAG](./md/08.Update/Phi35/031.WebGPUWithPhi35Readme.md)(✅)
    - [Crea tu propio agente de chat Copilot en Visual Studio Code con Phi-3.5 usando modelos de GitHub](./md/08.Update/Phi35/032.CreateVSCodeChatAgentWithGitHubModels.md)(✅)

## Usando Modelos Phi-3

### Phi-3 en Azure AI Studio

Puedes aprender cómo usar Microsoft Phi-3 y cómo construir soluciones E2E en tus diferentes dispositivos de hardware. Para experimentar Phi-3 por ti mismo, comienza jugando con el modelo y personalizando Phi-3 para tus escenarios usando el [Azure AI Studio, Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) puedes aprender más en Comenzando con [Azure AI Studio](/md/02.QuickStart/AzureAIStudio_QuickStart.md)

**Playground**
Cada modelo tiene un playground dedicado para probar el modelo [Azure AI Playground](https://aka.ms/try-phi3).

### Phi-3 en Modelos de GitHub

Puedes aprender cómo usar Microsoft Phi-3 y cómo construir soluciones E2E en tus diferentes dispositivos de hardware. Para experimentar Phi-3 por ti mismo, comienza jugando con el modelo y personalizando Phi-3 para tus escenarios usando el [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) puedes aprender más en Comenzando con [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**
Cada modelo tiene un [playground dedicado para probar el modelo](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi-3 en Hugging Face

También puedes encontrar el modelo en [Hugging Face](https://huggingface.co/microsoft)

**Playground**
 [Playground de Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🌐 Soporte Multilenguaje

> **Note:**
> Estas traducciones fueron generadas automáticamente usando el [co-op-translator](https://github.com/Azure/co-op-translator) de código abierto y pueden contener errores o imprecisiones. Para información crítica, se recomienda referirse al original o consultar una traducción profesional humana. Si deseas agregar o actualizar una traducción, por favor consulta el repositorio [co-op-translator](https://github.com/Azure/co-op-translator), donde puedes contribuir fácilmente usando comandos simples.

| Idioma               | Código | Enlace al README Traducido                             | Última Actualización |
|----------------------|--------|-------------------------------------------------------|----------------------|
| Chino (Simplificado) | zh     | [Traducción al Chino](../zh/README.md)    | 2024-09-21           |
| Chino (Tradicional)  | tw     | [Traducción al chino](../tw/README.md)    | 2024-09-21           |
| Francés              | fr     | [Traducción al Francés](../fr/README.md)  | 2024-09-21           |
| Japonés              | ja     | [Traducción al Japonés](../ja/README.md)  | 2024-09-21           |
| Coreano              | ko     | [Traducción al Coreano](../ko/README.md)  | 2024-09-21           |
| Español              | es     | [Traducción al Español](./README.md)      | 2024-09-21           |

## Marcas Registradas

Este proyecto puede contener marcas registradas o logotipos para proyectos, productos o servicios. El uso autorizado de las marcas registradas o logotipos de Microsoft está sujeto y debe seguir las [Pautas de Marca y Logotipo de Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
El uso de marcas registradas o logotipos de Microsoft en versiones modificadas de este proyecto no debe causar confusión o implicar patrocinio de Microsoft. Cualquier uso de marcas registradas o logotipos de terceros está sujeto a las políticas de esos terceros.

Aviso legal: La traducción fue realizada a partir de su original por un modelo de IA y puede no ser perfecta. Por favor, revise el resultado y haga las correcciones necesarias.