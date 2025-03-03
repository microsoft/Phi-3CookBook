# **Introducción al Servicio de Azure Machine Learning**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) es un servicio en la nube diseñado para acelerar y gestionar el ciclo de vida de los proyectos de aprendizaje automático (ML).

Los profesionales de ML, científicos de datos e ingenieros pueden usarlo en sus flujos de trabajo diarios para:

- Entrenar y desplegar modelos.
- Gestionar operaciones de aprendizaje automático (MLOps).
- Puedes crear un modelo en Azure Machine Learning o utilizar un modelo desarrollado en una plataforma de código abierto, como PyTorch, TensorFlow o scikit-learn.
- Las herramientas de MLOps te ayudan a monitorear, reentrenar y volver a desplegar modelos.

## ¿Para quién es Azure Machine Learning?

**Científicos de Datos e Ingenieros de ML**

Pueden utilizar herramientas para acelerar y automatizar sus flujos de trabajo diarios.  
Azure ML ofrece características para garantizar equidad, explicabilidad, seguimiento y auditabilidad.

**Desarrolladores de Aplicaciones**

Pueden integrar modelos en aplicaciones o servicios de manera fluida.

**Desarrolladores de Plataformas**

Tienen acceso a un conjunto robusto de herramientas respaldadas por las API de Azure Resource Manager.  
Estas herramientas permiten construir herramientas avanzadas de ML.

**Empresas**

Al trabajar en la nube de Microsoft Azure, las empresas se benefician de una seguridad familiar y controles de acceso basados en roles.  
Configura proyectos para controlar el acceso a datos protegidos y operaciones específicas.

## Productividad para Todos en el Equipo

Los proyectos de ML a menudo requieren un equipo con un conjunto de habilidades variadas para construir y mantenerlos.

Azure ML ofrece herramientas que te permiten:
- Colaborar con tu equipo mediante notebooks compartidos, recursos de cómputo, cómputo sin servidor, datos y entornos.
- Desarrollar modelos con equidad, explicabilidad, seguimiento y auditabilidad para cumplir con los requisitos de trazabilidad y auditoría.
- Desplegar modelos de ML de manera rápida y sencilla a gran escala, y gestionarlos y gobernarlos eficientemente con MLOps.
- Ejecutar cargas de trabajo de aprendizaje automático en cualquier lugar con gobernanza, seguridad y cumplimiento integrados.

## Herramientas de Plataforma Compatibles

Cualquier miembro de un equipo de ML puede usar sus herramientas preferidas para realizar su trabajo.  
Ya sea que estés ejecutando experimentos rápidos, ajustando hiperparámetros, construyendo pipelines o gestionando inferencias, puedes usar interfaces conocidas como:
- Azure Machine Learning Studio
- Python SDK (v2)
- Azure CLI (v2)
- APIs REST de Azure Resource Manager

A medida que refinas modelos y colaboras durante el ciclo de desarrollo, puedes compartir y encontrar activos, recursos y métricas dentro de la interfaz de usuario de Azure Machine Learning Studio.

## **LLM/SLM en Azure ML**

Azure ML ha incorporado numerosas funciones relacionadas con LLM/SLM, combinando LLMOps y SLMOps para crear una plataforma tecnológica de inteligencia artificial generativa a nivel empresarial.

### **Catálogo de Modelos**

Los usuarios empresariales pueden desplegar diferentes modelos según distintos escenarios de negocio a través del Catálogo de Modelos, y ofrecer servicios como Modelo como Servicio para que los desarrolladores o usuarios empresariales accedan.

![models](../../../../translated_images/models.2450411eac222e539ffb55785a8f550d01be1030bd8eb67c9c4f9ae4ca5d64be.es.png)

El Catálogo de Modelos en Azure Machine Learning Studio es el centro para descubrir y utilizar una amplia gama de modelos que te permiten construir aplicaciones de inteligencia artificial generativa.  
El catálogo de modelos cuenta con cientos de modelos de proveedores como Azure OpenAI Service, Mistral, Meta, Cohere, Nvidia, Hugging Face, incluidos modelos entrenados por Microsoft. Los modelos de proveedores distintos a Microsoft son Productos No Microsoft, tal como se definen en los Términos de Producto de Microsoft, y están sujetos a los términos proporcionados con el modelo.

### **Pipeline de Tareas**

El núcleo de un pipeline de aprendizaje automático es dividir una tarea completa de ML en un flujo de trabajo de múltiples pasos. Cada paso es un componente manejable que puede desarrollarse, optimizarse, configurarse y automatizarse de manera individual. Los pasos están conectados a través de interfaces bien definidas. El servicio de pipelines de Azure Machine Learning orquesta automáticamente todas las dependencias entre los pasos del pipeline.

En el ajuste fino de SLM / LLM, podemos gestionar nuestros procesos de datos, entrenamiento y generación a través de Pipeline.

![finetuning](../../../../translated_images/finetuning.b52e4aa971dfd8d3c668db913a2b419380533bd3a920d227ec19c078b7b3f309.es.png)

### **Flujo de Prompts**

**Beneficios de usar el flujo de prompts de Azure Machine Learning**  
El flujo de prompts de Azure Machine Learning ofrece una serie de beneficios que ayudan a los usuarios a pasar de la ideación a la experimentación y, finalmente, a aplicaciones basadas en LLM listas para producción:

**Agilidad en la ingeniería de prompts**

- Experiencia interactiva de creación: El flujo de prompts de Azure Machine Learning proporciona una representación visual de la estructura del flujo, lo que permite a los usuarios entender y navegar fácilmente por sus proyectos. También ofrece una experiencia de codificación similar a un notebook para un desarrollo y depuración eficientes del flujo.
- Variantes para ajuste de prompts: Los usuarios pueden crear y comparar múltiples variantes de prompts, facilitando un proceso iterativo de refinamiento.
- Evaluación: Los flujos de evaluación integrados permiten a los usuarios evaluar la calidad y efectividad de sus prompts y flujos.
- Recursos completos: El flujo de prompts de Azure Machine Learning incluye una biblioteca de herramientas integradas, muestras y plantillas que sirven como punto de partida para el desarrollo, inspirando creatividad y acelerando el proceso.

**Preparación empresarial para aplicaciones basadas en LLM**

- Colaboración: El flujo de prompts de Azure Machine Learning admite la colaboración en equipo, permitiendo que varios usuarios trabajen juntos en proyectos de ingeniería de prompts, compartan conocimientos y mantengan el control de versiones.
- Plataforma todo en uno: El flujo de prompts de Azure Machine Learning simplifica todo el proceso de ingeniería de prompts, desde el desarrollo y la evaluación hasta el despliegue y monitoreo. Los usuarios pueden desplegar fácilmente sus flujos como endpoints de Azure Machine Learning y monitorear su desempeño en tiempo real, asegurando una operación óptima y mejora continua.
- Soluciones de preparación empresarial de Azure Machine Learning: El flujo de prompts aprovecha las sólidas soluciones de preparación empresarial de Azure Machine Learning, proporcionando una base segura, escalable y confiable para el desarrollo, experimentación y despliegue de flujos.

Con el flujo de prompts de Azure Machine Learning, los usuarios pueden liberar su agilidad en la ingeniería de prompts, colaborar de manera efectiva y aprovechar soluciones de nivel empresarial para el desarrollo y despliegue exitoso de aplicaciones basadas en LLM.

Combinando el poder de cómputo, los datos y los diferentes componentes de Azure ML, los desarrolladores empresariales pueden construir fácilmente sus propias aplicaciones de inteligencia artificial.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automatizada por inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.