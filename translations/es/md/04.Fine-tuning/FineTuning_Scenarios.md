## Escenarios de Ajuste Fino

![FineTuning with MS Services](../../../../translated_images/FinetuningwithMS.921fa8c240611562e7c4a5ceb7eca04f458ad6f3c899d5a0dc120030398d9e08.es.png)

**Plataforma** Esto incluye varias tecnologías como Azure AI Studio, Azure Machine Learning, AI Tools, Kaito y ONNX Runtime.

**Infraestructura** Esto incluye la CPU y FPGA, que son esenciales para el proceso de ajuste fino. Déjame mostrarte los íconos de cada una de estas tecnologías.

**Herramientas y Framework** Esto incluye ONNX Runtime y ONNX Runtime. Déjame mostrarte los íconos de cada una de estas tecnologías.
[Insert icons for ONNX Runtime and ONNX Runtime]

El proceso de ajuste fino con tecnologías de Microsoft involucra varios componentes y herramientas. Al entender y utilizar estas tecnologías, podemos ajustar finamente nuestras aplicaciones y crear mejores soluciones.

## Modelo como Servicio

Ajuste fino del modelo usando ajuste fino alojado, sin necesidad de crear y gestionar el cómputo.

![MaaS Fine Tuning](../../../../translated_images/MaaSfinetune.1678f33544c36b9016d8c018ce9c4c1622fb3bc2d72751291c39813f88bce052.es.png)

El ajuste fino sin servidor está disponible para los modelos Phi-3-mini y Phi-3-medium, permitiendo a los desarrolladores personalizar rápidamente y con facilidad los modelos para escenarios en la nube y en el borde sin tener que organizar el cómputo. También hemos anunciado que, Phi-3-small, ahora está disponible a través de nuestra oferta de Modelos-como-Servicio para que los desarrolladores puedan comenzar rápidamente y con facilidad con el desarrollo de IA sin tener que gestionar la infraestructura subyacente.

[Fine Tuning Sample](https://github.com/microsoft/Phi-3CookBook/blob/main/md/04.Fine-tuning/FineTuning_AIStudio.md)

## Modelo como Plataforma

Los usuarios gestionan su propio cómputo para ajustar finamente sus modelos.

![Maap Fine Tuning](../../../../translated_images/MaaPFinetune.f88828d32d16ced1198525fceed9184ce17516f5c1a404c264d87a4ca816947f.es.png)

[Fine Tuning Sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Escenarios de Ajuste Fino

| | | | | | | |
|-|-|-|-|-|-|-|
|Escenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Adaptación de LLMs preentrenados a tareas o dominios específicos|Sí|Sí|Sí|Sí|Sí|Sí|
|Ajuste fino para tareas de PLN como clasificación de texto, reconocimiento de entidades nombradas y traducción automática|Sí|Sí|Sí|Sí|Sí|Sí|
|Ajuste fino para tareas de QA|Sí|Sí|Sí|Sí|Sí|Sí|
|Ajuste fino para generar respuestas similares a las humanas en chatbots|Sí|Sí|Sí|Sí|Sí|Sí|
|Ajuste fino para generar música, arte u otras formas de creatividad|Sí|Sí|Sí|Sí|Sí|Sí|
|Reducción de costos computacionales y financieros|Sí|Sí|No|Sí|Sí|No|
|Reducción del uso de memoria|No|Sí|No|Sí|Sí|Sí|
|Uso de menos parámetros para un ajuste fino eficiente|No|Sí|Sí|No|No|Sí|
|Forma eficiente en memoria de paralelismo de datos que da acceso a la memoria GPU agregada de todos los dispositivos GPU disponibles|No|No|No|Sí|Sí|Sí|

## Ejemplos de Rendimiento de Ajuste Fino

![Finetuning Performance](../../../../translated_images/Finetuningexamples.88bad3a5350927b08b1f06e4bced95cfd3715caa933d21c9ff658dcf0db94f73.es.png)

Aviso legal: La traducción fue realizada a partir de su original por un modelo de IA y puede no ser perfecta. 
Por favor, revise el resultado y haga las correcciones necesarias.