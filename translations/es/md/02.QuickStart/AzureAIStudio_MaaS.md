# Desplegar modelos Phi-3 como APIs sin servidor

Los modelos Phi-3 (Mini, Small y Medium) en el [catálogo de modelos de Azure](https://learn.microsoft.com/azure/machine-learning/concept-model-catalog?WT.mc_id=aiml-137032-kinfeylo) se pueden desplegar como una API sin servidor con facturación de pago por uso. Este tipo de despliegue proporciona una manera de consumir modelos como una API sin alojarlos en tu suscripción, manteniendo la seguridad y el cumplimiento empresarial que las organizaciones necesitan. Esta opción de despliegue no requiere cuota de tu suscripción.

Los modelos MaaS ahora soportan una API REST común para completar chats usando la ruta /chat/completions.

## Prerrequisitos

1. Una suscripción de Azure con un método de pago válido. Las suscripciones gratuitas o de prueba de Azure no funcionarán. Si no tienes una suscripción de Azure, crea una cuenta de pago de Azure para comenzar.
1. Un hub de [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo). La oferta de despliegue de modelos sin servidor para Phi-3 solo está disponible con hubs creados en estas regiones:
    - **East US 2**
    - **Sweden Central**

    > [!NOTE]
    > Para una lista de regiones disponibles para cada uno de los modelos que soportan despliegues de API sin servidor, consulta Disponibilidad regional para modelos en endpoints de API sin servidor.

1. Un proyecto en [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).
1. Los controles de acceso basados en roles de Azure (Azure RBAC) se utilizan para otorgar acceso a operaciones en Azure AI Studio. Para realizar los pasos en este artículo, tu cuenta de usuario debe tener asignado el rol de Desarrollador de Azure AI en el grupo de recursos.

## Crear un nuevo despliegue

Realiza las siguientes tareas para crear un despliegue:

1. Inicia sesión en [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).
1. Selecciona Catálogo de modelos en la barra lateral izquierda.
1. Busca y selecciona el modelo que deseas desplegar, por ejemplo, Phi-3-mini-4k-Instruct, para abrir su página de Detalles.
1. Selecciona Desplegar.
1. Elige la opción API sin servidor para abrir una ventana de despliegue de API sin servidor para el modelo.

Alternativamente, puedes iniciar un despliegue comenzando desde tu proyecto en AI Studio.

1. Desde la barra lateral izquierda de tu proyecto, selecciona Componentes > Despliegues.
1. Selecciona + Crear despliegue.
1. Busca y selecciona Phi-3-mini-4k-Instruct para abrir la página de Detalles del modelo.
1. Selecciona Confirmar, y elige la opción API sin servidor para abrir una ventana de despliegue de API sin servidor para el modelo.
1. Selecciona el proyecto en el que deseas desplegar tu modelo. Para desplegar el modelo Phi-3, tu proyecto debe pertenecer a una de las regiones listadas en la [sección de prerrequisitos](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo).
1. Selecciona la pestaña Precios y términos para conocer los precios del modelo seleccionado.
1. Dale un nombre al despliegue. Este nombre se convierte en parte de la URL de la API de despliegue. Esta URL debe ser única en cada región de Azure.
1. Selecciona Desplegar. Espera hasta que el despliegue esté listo y seas redirigido a la página de Despliegues. Este paso requiere que tu cuenta tenga permisos de rol de Desarrollador de Azure AI en el Grupo de Recursos, como se indica en los prerrequisitos.
1. Selecciona Abrir en el área de pruebas para comenzar a interactuar con el modelo.

Vuelve a la página de Despliegues, selecciona el despliegue y toma nota de la URL de destino y la clave secreta del endpoint, que puedes usar para llamar al despliegue y generar completaciones. Para más información sobre el uso de las APIs, consulta [Referencia: Completaciones de chat](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo).

Siempre puedes encontrar los detalles del endpoint, la URL y las claves de acceso navegando a la página de resumen de tu proyecto. Luego, desde la barra lateral izquierda de tu proyecto, selecciona Componentes > Despliegues.

## Consumir modelos Phi-3 como un servicio

Los modelos desplegados como APIs sin servidor se pueden consumir usando la API de chat, dependiendo del tipo de modelo que hayas desplegado.

1. Desde la página de resumen de tu proyecto, ve a la barra lateral izquierda y selecciona Componentes > Despliegues.
2. Encuentra y selecciona el despliegue que creaste.
3. Copia la URL de destino y el valor de la clave.
4. Realiza una solicitud API usando la API de completaciones de chat con <target_url>chat/completions. Para más información sobre el uso de las APIs, consulta la [Referencia: Completaciones de chat](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo)

## Costos y cuotas

Consideraciones de costos y cuotas para modelos Phi-3 desplegados como APIs sin servidor

Puedes encontrar la información de precios en la pestaña Precios y términos del asistente de despliegue al desplegar el modelo.

La cuota se gestiona por despliegue. Cada despliegue tiene un límite de 200,000 tokens por minuto y 1,000 solicitudes API por minuto. Sin embargo, actualmente limitamos un despliegue por modelo por proyecto. Contacta con el soporte de Microsoft Azure si los límites actuales no son suficientes para tus escenarios.

## Recursos adicionales 

### Desplegar modelos como APIs sin servidor

Modelos MaaS como un Servicio Para detalles sobre el [Despliegue de MaaS](https://learn.microsoft.com//azure/ai-studio/how-to/deploy-models-serverless?tabs=azure-ai-studio?WT.mc_id=aiml-137032-kinfeylo)

### Cómo desplegar la familia de modelos de lenguaje pequeños Phi-3 con Azure Machine Learning studio o Azure AI Studio

Modelos Maap como una Plataforma para detalles sobre el [Despliegue de MaaP](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)

Aviso legal: La traducción fue realizada a partir del original por un modelo de inteligencia artificial y puede no ser perfecta. 
Por favor, revise el resultado y haga las correcciones necesarias.