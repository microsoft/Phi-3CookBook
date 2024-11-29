# **Uso de Phi-3 en Azure AI Foundry**

Con el desarrollo de la IA Generativa, esperamos usar una plataforma unificada para gestionar diferentes LLM y SLM, integración de datos empresariales, operaciones de ajuste fino/RAG, y la evaluación de diferentes negocios empresariales después de integrar LLM y SLM, etc., para que las aplicaciones inteligentes de IA generativa se implementen mejor. [Azure AI Foundry](https://ai.azure.com) es una plataforma de aplicaciones de IA generativa a nivel empresarial.

![aistudo](../../../../translated_images/ai-studio-home.e25e21a22af0a57c0cb02815f4c7554c8816afe8bc3c3008ac74e2eedd9fbaa9.es.png)

Con Azure AI Foundry, puedes evaluar las respuestas de grandes modelos de lenguaje (LLM) y orquestar componentes de aplicación de prompts con prompt flow para un mejor rendimiento. La plataforma facilita la escalabilidad para transformar pruebas de concepto en producción completa con facilidad. El monitoreo y la refinación continuos apoyan el éxito a largo plazo.

Podemos desplegar rápidamente el modelo Phi-3 en Azure AI Foundry a través de pasos simples, y luego usar Azure AI Foundry para completar trabajos relacionados con Phi-3 como Playground/Chat, ajuste fino, evaluación y otros trabajos relacionados.

## **1. Preparación**

## [AZD AI Foundry Starter Template](https://azure.github.io/awesome-azd/?name=AI+Studio)

### Azure AI Foundry Starter

Esta es una plantilla Bicep que despliega todo lo que necesitas para comenzar con Azure AI Foundry. Incluye AI Hub con recursos dependientes, proyecto de IA, servicios de IA y un endpoint en línea.

### Uso Rápido

Si ya tienes instalado el [CLI de Azure Developer](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) en tu máquina, usar esta plantilla es tan simple como ejecutar este comando en un nuevo directorio.

### Comando de Terminal

```bash
azd init -t azd-aistudio-starter
```

O
Si usas la extensión de azd para VS Code, puedes pegar esta URL en el terminal de comandos de VS Code.

### URL de Terminal

```bash
azd-aistudio-starter
```

## Creación Manual

Crea Azure AI Foundry en [Azure Portal](https://portal.azure.com?WT.mc_id=aiml-138114-kinfeylo)

![portal](../../../../translated_images/ai-studio-portal.8ae13fc10a0fe53104d7fe8d1c8c59b53f5ff7f4d74e52d81bcd63b5de6baf13.es.png)

Después de completar el nombramiento del estudio y configurar la región, puedes crearlo.

![settings](../../../../translated_images/ai-studio-settings.ac28832948da45fd844232ae8e743f3e657a4b88e8a02ce80ae6bfad8ba4733a.es.png)

Después de la creación exitosa, puedes acceder al estudio que creaste a través de [ai.azure.com](https://ai.azure.com/)

![page](../../../../translated_images/ai-studio-page.9bfba68b0b3662a5323008dab8d9b24d4fc580be93777203bb64ad78283df469.es.png)

Puede haber múltiples proyectos en un AI Foundry. Crea un proyecto en AI Foundry para prepararte.

![proj](../../../../translated_images/ai-studio-proj.62b5b49ee77bd4e382a82c1c28c247c1204c11ea212a4d95b39e467c6a24998f.es.png)

## **2. Desplegar el modelo Phi-3 en Azure AI Foundry**

Haz clic en la opción Explorar del proyecto para entrar en el Catálogo de Modelos y selecciona Phi-3.

![model](../../../../translated_images/ai-studio-model.d90f85e0b4ce4bbdde6e460304f2e6676502e86ec0aae8f39dd56b7f0538afb9.es.png)

Selecciona Phi-3-mini-4k-instruct.

![phi3](../../../../translated_images/ai-studio-phi3.9320ffe396abdbf9d1026637016462406090df88e0883e411b1984be34ed5710.es.png)

Haz clic en 'Deploy' para desplegar el modelo Phi-3-mini-4k-instruct.

> [!NOTE]
>
> Puedes seleccionar la potencia de cómputo al desplegar.

## **3. Playground Chat Phi-3 en Azure AI Foundry**

Ve a la página de despliegue, selecciona Playground y chatea con Phi-3 de Azure AI Foundry.

![chat](../../../../translated_images/ai-studio-chat.ba2c631ac2279f2deb4e87998895b0688e33d2f79475da6a3851e3fb3a0495c5.es.png)

## **4. Desplegar el Modelo desde Azure AI Foundry**

Para desplegar un modelo desde el Catálogo de Modelos de Azure, puedes seguir estos pasos:

- Inicia sesión en Azure AI Foundry.
- Elige el modelo que deseas desplegar desde el catálogo de modelos de Azure AI Foundry.
- En la página de Detalles del modelo, selecciona Deploy y luego selecciona Serverless API con Azure AI Content Safety.
- Selecciona el proyecto en el que deseas desplegar tus modelos. Para usar la oferta de API sin servidor, tu espacio de trabajo debe pertenecer a la región de East US 2 o Sweden Central. Puedes personalizar el nombre del Despliegue.
- En el asistente de despliegue, selecciona el Precio y términos para conocer el precio y los términos de uso.
- Selecciona Deploy. Espera hasta que el despliegue esté listo y seas redirigido a la página de Despliegues.
- Selecciona Open in playground para comenzar a interactuar con el modelo.
- Puedes regresar a la página de Despliegues, seleccionar el despliegue y anotar la URL del objetivo del endpoint y la Clave Secreta, que puedes usar para llamar al despliegue y generar completions.
- Siempre puedes encontrar los detalles del endpoint, URL y claves de acceso navegando a la pestaña Build y seleccionando Despliegues en la sección de Componentes.

> [!NOTE]
> Ten en cuenta que tu cuenta debe tener permisos de rol de Desarrollador de Azure AI en el Grupo de Recursos para realizar estos pasos.

## **5. Usar la API de Phi-3 en Azure AI Foundry**

Puedes acceder a https://{Your project name}.region.inference.ml.azure.com/swagger.json a través de Postman GET y combinarlo con Key para conocer las interfaces proporcionadas.

![swagger](../../../../translated_images/ai-studio-swagger.ae9e8fff8aba78ec18dc94b0ef251f0efe4ba90e77618ff0df13e1636e196abf.es.png)

como acceder a la API de score.

![score](../../../../translated_images/ai-studio-score.0d5c8ce86241111633e946acf3413d3073957beb81cd37382cfd084ae310678f.es.png)

Puedes obtener los parámetros de solicitud muy convenientemente, así como los parámetros de respuesta. Este es el resultado de Postman.

![result](../../../../translated_images/ai-studio-result.8563455b3a437110aa1d99bfc21cd8c624510b100f20b8907653cba5eef36226.es.png)

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.