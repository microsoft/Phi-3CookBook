# Desplegar modelos Phi-3 como APIs sin servidor

Los modelos Phi-3 (Mini, Small y Medium) en el [catálogo de modelos de Azure](https://learn.microsoft.com/azure/machine-learning/concept-model-catalog?WT.mc_id=aiml-137032-kinfeylo) se pueden desplegar como una API sin servidor con facturación de pago por uso. Este tipo de despliegue proporciona una forma de consumir modelos como una API sin alojarlos en tu suscripción, manteniendo la seguridad y el cumplimiento empresarial que las organizaciones necesitan. Esta opción de despliegue no requiere cuota de tu suscripción.

Los modelos MaaS [REST API](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo) ahora soportan una API REST común para completaciones de chat usando la ruta /chat/completions.

## Requisitos previos

1. Una suscripción de Azure con un método de pago válido. Las suscripciones gratuitas o de prueba de Azure no funcionarán. Si no tienes una suscripción de Azure, crea una cuenta de Azure de pago para comenzar.
1. Un hub de [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo). La oferta de despliegue de modelos sin servidor para Phi-3 solo está disponible con hubs creados en estas regiones:
    - **East US 2**
    - **Sweden Central**

    > [!NOTE]
    > Para una lista de las regiones disponibles para cada uno de los modelos que soportan despliegues de API sin servidor, consulta la disponibilidad regional para modelos en endpoints de API sin servidor.

1. Un proyecto de [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).
1. Los controles de acceso basados en roles de Azure (Azure RBAC) se usan para otorgar acceso a operaciones en Azure AI Foundry. Para realizar los pasos en este artículo, tu cuenta de usuario debe tener asignado el rol de Desarrollador de Azure AI en el grupo de recursos.

## Crear un nuevo despliegue

Realiza las siguientes tareas para crear un despliegue:

1. Inicia sesión en [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).
1. Selecciona Catálogo de modelos desde la barra lateral izquierda.
1. Busca y selecciona el modelo que deseas desplegar, por ejemplo Phi-3-mini-4k-Instruct, para abrir su página de Detalles.
1. Selecciona Desplegar.
1. Elige la opción API sin servidor para abrir una ventana de despliegue de API sin servidor para el modelo.

Alternativamente, puedes iniciar un despliegue comenzando desde tu proyecto en AI Foundry.

1. Desde la barra lateral izquierda de tu proyecto, selecciona Componentes > Despliegues.
1. Selecciona + Crear despliegue.
1. Busca y selecciona Phi-3-mini-4k-Instruct para abrir la página de Detalles del modelo.
1. Selecciona Confirmar, y elige la opción API sin servidor para abrir una ventana de despliegue de API sin servidor para el modelo.
1. Selecciona el proyecto en el que deseas desplegar tu modelo. Para desplegar el modelo Phi-3, tu proyecto debe pertenecer a una de las regiones listadas en la [sección de requisitos previos](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo).
1. Selecciona la pestaña Precios y términos para conocer los precios del modelo seleccionado.
1. Da un nombre al despliegue. Este nombre se convierte en parte de la URL de la API de despliegue. Esta URL debe ser única en cada región de Azure.
1. Selecciona Desplegar. Espera hasta que el despliegue esté listo y seas redirigido a la página de Despliegues. Este paso requiere que tu cuenta tenga permisos de rol de Desarrollador de Azure AI en el Grupo de Recursos, como se menciona en los requisitos previos.
1. Selecciona Abrir en el playground para comenzar a interactuar con el modelo.

Regresa a la página de Despliegues, selecciona el despliegue, y anota la URL de destino del endpoint y la Clave secreta, que puedes usar para llamar al despliegue y generar completaciones. Para más información sobre el uso de las APIs, consulta [Referencia: Completaciones de chat](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo).

Siempre puedes encontrar los detalles del endpoint, la URL y las claves de acceso navegando a la página de vista general de tu Proyecto. Luego, desde la barra lateral izquierda de tu proyecto, selecciona Componentes > Despliegues.

## Consumir modelos Phi-3 como un servicio

Los modelos desplegados como APIs sin servidor se pueden consumir utilizando la API de chat, dependiendo del tipo de modelo que hayas desplegado.

1. Desde la página de vista general de tu Proyecto, ve a la barra lateral izquierda y selecciona Componentes > Despliegues.
2. Encuentra y selecciona el despliegue que creaste.
3. Copia la URL de destino y el valor de la Clave.
4. Realiza una solicitud API utilizando la API de chat/completions usando <target_url>chat/completions. Para más información sobre el uso de las APIs, consulta la [Referencia: Completaciones de chat](https://learn.microsoft.com/azure/ai-studio/reference/reference-model-inference-chat-completions?WT.mc_id=aiml-137032-kinfeylo).

## Costos y cuotas

Consideraciones de costos y cuotas para modelos Phi-3 desplegados como APIs sin servidor

Puedes encontrar la información de precios en la pestaña Precios y términos del asistente de despliegue al desplegar el modelo.

La cuota se gestiona por despliegue. Cada despliegue tiene un límite de tasa de 200,000 tokens por minuto y 1,000 solicitudes API por minuto. Sin embargo, actualmente limitamos un despliegue por modelo por proyecto. Contacta al Soporte de Microsoft Azure si los límites de tasa actuales no son suficientes para tus escenarios.

## Recursos adicionales 

### Desplegar modelos como APIs sin servidor

Modelos MaaS como un Servicio Para más detalles sobre el [Despliegue MaaS](https://learn.microsoft.com//azure/ai-studio/how-to/deploy-models-serverless?tabs=azure-ai-studio?WT.mc_id=aiml-137032-kinfeylo)

### Cómo desplegar la familia de pequeños modelos de lenguaje Phi-3 con Azure Machine Learning studio o Azure AI Foundry

Modelos Maap como una Plataforma para más detalles sobre el [Despliegue Maap](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando servicios de traducción automatizada por inteligencia artificial. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.