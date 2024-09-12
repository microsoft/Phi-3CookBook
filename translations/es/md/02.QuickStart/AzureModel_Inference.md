# Inferencia del Modelo de Azure AI

La [Inferencia del Modelo de Azure AI es una API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo) que expone un conjunto común de capacidades para modelos fundamentales y que puede ser utilizada por desarrolladores para consumir predicciones de un conjunto diverso de modelos de manera uniforme y consistente. Los desarrolladores pueden interactuar con diferentes modelos desplegados en Azure AI Studio sin cambiar el código subyacente que están utilizando.

Microsoft ahora tiene su propio SDK para la inferencia de modelos de IA, para diferentes modelos alojados en [MaaS/MaaP](https://azure.microsoft.com/products/ai-model-catalog?WT.mc_id=aiml-138114-kinfeylo). 

Las versiones de Python y JS ya están disponibles. C# será lanzado próximamente.

Para [Python](https://learn.microsoft.com/python/api/overview/azure/ai-inference-readme?view=azure-python-preview?WT.mc_id=aiml-138114-kinfeylo) [Ejemplos](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-inference/samples?WT.mc_id=aiml-138114-kinfeylo)

Para [JavaScript](https://learn.microsoft.com/javascript/api/overview/azure/ai-inference-rest-readme?view=azure-node-preview?WT.mc_id=aiml-138114-kinfeylo) [Ejemplos](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples?WT.mc_id=aiml-138114-kinfeylo)

El SDK utiliza la [API REST documentada aquí](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-api?tabs=python?WT.mc_id=aiml-138114-kinfeylo).

## Disponibilidad

La API de Inferencia del Modelo de Azure AI está disponible en los siguientes modelos Phi-3:

- Modelos desplegados en endpoints de API sin servidor:
- Modelos desplegados en inferencia gestionada:

La API es compatible con los despliegues de modelos de Azure OpenAI.

> [!NOTE]
> La API de inferencia de modelos de Azure AI está disponible en inferencia gestionada (Managed Online Endpoints) para modelos desplegados después del 24 de junio de 2024. Para aprovechar la API, vuelva a desplegar su endpoint si el modelo ha sido desplegado antes de dicha fecha.

## Capacidades

La siguiente sección describe algunas de las capacidades que expone la API. Para una especificación completa de la API, consulte la sección de referencia.

### Modalidades

La API indica cómo los desarrolladores pueden consumir predicciones para las siguientes modalidades:

- Obtener información: Devuelve la información sobre el modelo desplegado bajo el endpoint.
- Embeddings de texto: Crea un vector de embedding que representa el texto de entrada.
- Completaciones de texto: Crea una completación para el prompt y parámetros proporcionados.
- Completaciones de chat: Crea una respuesta del modelo para la conversación de chat dada.
- Embeddings de imagen: Crea un vector de embedding que representa el texto y la imagen de entrada.

