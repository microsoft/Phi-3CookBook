# Usar GPU de Windows para crear una solución Prompt flow con Phi-3.5-Instruct ONNX 

El siguiente documento es un ejemplo de cómo usar PromptFlow con ONNX (Open Neural Network Exchange) para desarrollar aplicaciones de IA basadas en modelos Phi-3.

PromptFlow es un conjunto de herramientas de desarrollo diseñado para simplificar el ciclo completo de desarrollo de aplicaciones de IA basadas en LLM (Modelos de Lenguaje a Gran Escala), desde la ideación y el prototipado hasta las pruebas y la evaluación.

Al integrar PromptFlow con ONNX, los desarrolladores pueden:

- Optimizar el Rendimiento del Modelo: Aprovechar ONNX para una inferencia y despliegue de modelos más eficientes.
- Simplificar el Desarrollo: Utilizar PromptFlow para gestionar el flujo de trabajo y automatizar tareas repetitivas.
- Mejorar la Colaboración: Facilitar una mejor colaboración entre los miembros del equipo proporcionando un entorno de desarrollo unificado.

**Prompt flow** es un conjunto de herramientas de desarrollo diseñado para simplificar el ciclo completo de desarrollo de aplicaciones de IA basadas en LLM, desde la ideación, el prototipado, las pruebas, la evaluación, hasta el despliegue en producción y el monitoreo. Facilita enormemente la ingeniería de prompts y te permite construir aplicaciones LLM con calidad de producción.

Prompt flow puede conectarse a OpenAI, Azure OpenAI Service y modelos personalizables (Huggingface, LLM/SLM locales). Esperamos desplegar el modelo ONNX cuantizado de Phi-3.5 en aplicaciones locales. Prompt flow puede ayudarnos a planificar mejor nuestro negocio y completar soluciones locales basadas en Phi-3.5. En este ejemplo, combinaremos la biblioteca ONNX Runtime GenAI para completar la solución Prompt flow basada en GPU de Windows.

## **Instalación**

### **ONNX Runtime GenAI para GPU de Windows**

Lee esta guía para configurar ONNX Runtime GenAI para GPU de Windows [haz clic aquí](./ORTWindowGPUGuideline.md)

### **Configurar Prompt flow en VSCode**

1. Instala la extensión Prompt flow para VS Code

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.es.png)

2. Después de instalar la extensión Prompt flow para VS Code, haz clic en la extensión y selecciona **Installation dependencies**. Sigue esta guía para instalar el SDK de Prompt flow en tu entorno.

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.es.png)

3. Descarga [Código de Ejemplo](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) y usa VS Code para abrir este ejemplo.

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.es.png)

4. Abre **flow.dag.yaml** para elegir tu entorno de Python.

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.es.png)

   Abre **chat_phi3_ort.py** para cambiar la ubicación de tu modelo Phi-3.5-Instruct ONNX.

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.es.png)

5. Ejecuta tu flujo de prompts para realizar pruebas.

Abre **flow.dag.yaml** y haz clic en el editor visual.

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.es.png)

Después de hacer clic aquí, ejecútalo para realizar pruebas.

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.es.png)

1. Puedes ejecutar un lote en la terminal para verificar más resultados.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Puedes verificar los resultados en tu navegador predeterminado.

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.es.png)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.