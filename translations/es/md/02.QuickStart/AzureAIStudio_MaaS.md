# Implementar modelos Phi-3 como APIs sin servidor

Los modelos Phi-3 (Mini, Small y Medium) en el [catálogo de modelos de Azure](https://learn.microsoft.com/azure/machine-learning/concept-model-catalog?WT.mc_id=aiml-137032-kinfeylo) se pueden implementar como una API sin servidor con facturación de pago por uso. Este tipo de implementación proporciona una manera de consumir modelos como una API sin alojarlos en tu suscripción, manteniendo la seguridad y el cumplimiento empresarial que las organizaciones necesitan. Esta opción de implementación no requiere cuota de tu suscripción.

[REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo) Los modelos MaaS ahora soportan una API REST común para completaciones de chat usando la ruta /chat/completions.

## Prerrequisitos

1. Una suscripción de Azure con un método de pago válido. Las suscripciones gratuitas o de prueba de Azure no funcionarán. Si no tienes una suscripción de Azure, crea una cuenta de Azure paga para comenzar.
1. Un hub de [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo). La oferta de implementación de modelos sin servidor para Phi-3 solo está disponible con hubs creados en estas regiones:
    - **East US 2**
    - **Sweden Central**

    > [!NOTE]
    > Para una lista de regiones disponibles para cada uno de los modelos que soportan implementaciones de endpoints API sin servidor, consulta la Disponibilidad de regiones para modelos en endpoints API sin servidor.

1. Un proyecto de [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).
1. Los controles de acceso basados en roles de Azure (Azure RBAC) se utilizan para otorgar acceso a operaciones en Azure AI Studio. Para realizar los pasos en este artículo, tu cuenta de usuario debe tener asignado el rol de Desarrollador de Azure AI en el grupo de recursos.

## Crear una nueva implementación

Realiza las siguientes tareas para crear una implementación:

1. Inicia sesión en [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).
1. Selecciona Catálogo de modelos en la barra lateral izquierda.
1. Busca y selecciona el modelo que deseas implementar, por ejemplo, Phi-3-mini-4k-Instruct, para abrir su página de Detalles.
1. Selecciona Implementar.
1. Elige la opción API sin servidor para abrir una ventana de implementación de API sin servidor para el modelo.

Alternativamente, puedes iniciar una implementación comenzando desde tu proyecto en AI Studio.

1. Desde la barra lateral izquierda de tu proyecto, selecciona Componentes > Implementaciones.
1. Selecciona + Crear implementación.
1. Busca y selecciona Phi-3-mini-4k-Instruct para abrir la página de Detalles del modelo.
1. Selecciona Confirmar y elige la opción API sin servidor para abrir una ventana de implementación de API sin servidor para el modelo.
1. Selecciona el proyecto en el que deseas implementar tu modelo. Para implementar el modelo Phi-3, tu proyecto debe pertenecer a una de las regiones enumeradas en la [sección de prerrequisitos](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo).
1. Selecciona la pestaña de Precios y términos para conocer los precios del modelo seleccionado.
1. Dale un nombre a la implementación. Este nombre se convierte en parte de la URL de la API de implementación. Esta URL debe ser única en cada región de Azure.
1. Selecciona Implementar. Espera hasta que la implementación esté lista y seas redirigido a la página de Implementaciones. Este paso requiere que tu cuenta tenga permisos de rol de Desarrollador de Azure AI en el Grupo de Recursos, como se indica en los prerrequisitos.
1. Selecciona Abrir en el playground para comenzar a interactuar con el modelo.

Regresa a la página de Implementaciones, selecciona la implementación y anota la URL del objetivo del endpoint y la Clave secreta, que puedes usar para llamar a la implementación y generar completaciones. Para más información sobre el uso de las APIs, consulta [Referencia: Completaciones de Chat](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo).

Siempre puedes encontrar los detalles del endpoint, la URL y las claves de acceso navegando a la página de vista general de tu Proyecto. Luego, desde la barra lateral izquierda de tu proyecto, selecciona Componentes > Implementaciones.

## Consumir modelos Phi-3 como un servicio

Los modelos implementados como APIs sin servidor pueden ser consumidos usando la API de chat, dependiendo del tipo de modelo que hayas implementado.

1. Desde la página de vista general de tu Proyecto, ve a la barra lateral izquierda y selecciona Componentes > Implementaciones.
2. Encuentra y selecciona la implementación que creaste.
3. Copia la URL del objetivo y el valor de la Clave.
4. Realiza una solicitud API usando la API de chat/completions usando <target_url>chat/completions. Para más información sobre el uso de las APIs, consulta la [Referencia: Completaciones de Chat](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)

## Costos y cuotas

Consideraciones de costos y cuotas para los modelos Phi-3 implementados como APIs sin servidor

Puedes encontrar la información de precios en la pestaña de Precios y términos del asistente de implementación al implementar el modelo.

La cuota se gestiona por implementación. Cada implementación tiene un límite de tasa de 200,000 tokens por minuto y 1,000 solicitudes API por minuto. Sin embargo, actualmente limitamos una implementación por modelo por proyecto. Contacta con el soporte de Microsoft Azure si los límites de tasa actuales no son suficientes para tus escenarios.

## Recursos adicionales

### Implementar modelos como APIs sin servidor

Modelos MaaS como un Servicio Para más detalles sobre [Implementación MaaS](https://learn.microsoft.com//azure/ai-studio/how-to/deploy-models-serverless?tabs=azure-ai-studio?WT.mc_id=aiml-137032-kinfeylo)

### Cómo implementar la familia de pequeños modelos de lenguaje Phi-3 con Azure Machine Learning studio o Azure AI Studio

Modelos Maap como una Plataforma para más detalles sobre [Implementación MaaP](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)

Aviso legal: La traducción fue realizada a partir de su original por un modelo de IA y puede no ser perfecta. 
Por favor, revise el resultado y haga las correcciones necesarias.