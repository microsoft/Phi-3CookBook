# **Introducción al Servicio de Azure Machine Learning**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) es un servicio en la nube para acelerar y gestionar el ciclo de vida de los proyectos de machine learning (ML).

Profesionales de ML, científicos de datos e ingenieros pueden usarlo en sus flujos de trabajo diarios para:

- Entrenar y desplegar modelos.
- Gestionar operaciones de machine learning (MLOps).
- Puedes crear un modelo en Azure Machine Learning o usar un modelo construido en una plataforma de código abierto, como PyTorch, TensorFlow o scikit-learn.
- Las herramientas de MLOps te ayudan a monitorear, reentrenar y redeployar modelos.

## ¿Para quién es Azure Machine Learning?

**Científicos de Datos e Ingenieros de ML**

Pueden usar herramientas para acelerar y automatizar sus flujos de trabajo diarios.
Azure ML ofrece características para equidad, explicabilidad, seguimiento y auditabilidad.
**Desarrolladores de Aplicaciones**

Pueden integrar modelos en aplicaciones o servicios sin problemas.

**Desarrolladores de Plataforma**

Tienen acceso a un conjunto robusto de herramientas respaldadas por APIs duraderas de Azure Resource Manager.
Estas herramientas permiten construir herramientas avanzadas de ML.

**Empresas**

Trabajando en la nube de Microsoft Azure, las empresas se benefician de la seguridad familiar y el control de acceso basado en roles.
Configura proyectos para controlar el acceso a datos protegidos y operaciones específicas.

## Productividad para Todos en el Equipo
Los proyectos de ML a menudo requieren un equipo con habilidades variadas para construir y mantener.

Azure ML proporciona herramientas que te permiten:
- Colaborar con tu equipo a través de notebooks compartidos, recursos de cómputo, cómputo sin servidor, datos y entornos.
- Desarrollar modelos con equidad, explicabilidad, seguimiento y auditabilidad para cumplir con los requisitos de linaje y auditoría.
- Desplegar modelos de ML rápida y fácilmente a gran escala, y gestionarlos y gobernarlos eficientemente con MLOps.
- Ejecutar cargas de trabajo de machine learning en cualquier lugar con gobernanza, seguridad y cumplimiento integrados.

## Herramientas de Plataforma Compatibles

Cualquiera en un equipo de ML puede usar sus herramientas preferidas para hacer el trabajo.
Ya sea que estés realizando experimentos rápidos, ajuste de hiperparámetros, construyendo pipelines o gestionando inferencias, puedes usar interfaces familiares incluyendo:
- Azure Machine Learning Studio
- Python SDK (v2)
- Azure CLI (v2)
- Azure Resource Manager REST APIs

A medida que refinan modelos y colaboran a lo largo del ciclo de desarrollo, pueden compartir y encontrar activos, recursos y métricas dentro de la interfaz de usuario de Azure Machine Learning studio.

## **LLM/SLM en Azure ML**

Azure ML ha añadido muchas funciones relacionadas con LLM/SLM, combinando LLMOps y SLMOps para crear una plataforma tecnológica de inteligencia artificial generativa a nivel empresarial.

### **Catálogo de Modelos**

Los usuarios empresariales pueden desplegar diferentes modelos según diferentes escenarios de negocio a través del Catálogo de Modelos, y proporcionar servicios como Model as Service para que los desarrolladores o usuarios empresariales accedan.

![models](../../../../translated_images/models.cb8d085cb832f2d0d8b24e4c091e223d3aa6a585f5ab53747e8d3db7ed3d2446.es.png)

El Catálogo de Modelos en Azure Machine Learning studio es el centro para descubrir y usar una amplia gama de modelos que te permiten construir aplicaciones de AI Generativa. El catálogo de modelos cuenta con cientos de modelos de proveedores de modelos como Azure OpenAI service, Mistral, Meta, Cohere, Nvidia, Hugging Face, incluyendo modelos entrenados por Microsoft. Los modelos de proveedores distintos a Microsoft son Productos No-Microsoft, según lo definido en los Términos del Producto de Microsoft, y están sujetos a los términos proporcionados con el modelo.

### **Pipeline de Tareas**

El núcleo de un pipeline de machine learning es dividir una tarea completa de machine learning en un flujo de trabajo de múltiples pasos. Cada paso es un componente manejable que se puede desarrollar, optimizar, configurar y automatizar individualmente. Los pasos están conectados a través de interfaces bien definidas. El servicio de pipeline de Azure Machine Learning orquesta automáticamente todas las dependencias entre los pasos del pipeline.

En el ajuste fino de SLM / LLM, podemos gestionar nuestros datos, procesos de entrenamiento y generación a través de Pipeline.

![finetuning](../../../../translated_images/finetuning.45db682d7f536aeb2a5f38d7bd8a42e61d02b6729f6d39df7a97ff4fad4c42b6.es.png)

### **Flujo de Prompts**

Beneficios de usar el flujo de prompts de Azure Machine Learning
El flujo de prompts de Azure Machine Learning ofrece una gama de beneficios que ayudan a los usuarios a pasar de la ideación a la experimentación y, finalmente, a aplicaciones listas para producción basadas en LLM:

**Agilidad en la ingeniería de prompts**

Experiencia de autoría interactiva: el flujo de prompts de Azure Machine Learning proporciona una representación visual de la estructura del flujo, permitiendo a los usuarios entender y navegar fácilmente por sus proyectos. También ofrece una experiencia de codificación similar a un notebook para un desarrollo y depuración eficientes del flujo.
Variantes para el ajuste de prompts: los usuarios pueden crear y comparar múltiples variantes de prompts, facilitando un proceso de refinamiento iterativo.

Evaluación: los flujos de evaluación integrados permiten a los usuarios evaluar la calidad y efectividad de sus prompts y flujos.

Recursos completos: el flujo de prompts de Azure Machine Learning incluye una biblioteca de herramientas integradas, muestras y plantillas que sirven como punto de partida para el desarrollo, inspirando creatividad y acelerando el proceso.

**Preparación empresarial para aplicaciones basadas en LLM**

Colaboración: el flujo de prompts de Azure Machine Learning admite la colaboración en equipo, permitiendo a múltiples usuarios trabajar juntos en proyectos de ingeniería de prompts, compartir conocimientos y mantener el control de versiones.

Plataforma todo en uno: el flujo de prompts de Azure Machine Learning simplifica todo el proceso de ingeniería de prompts, desde el desarrollo y evaluación hasta el despliegue y monitoreo. Los usuarios pueden desplegar fácilmente sus flujos como endpoints de Azure Machine Learning y monitorear su rendimiento en tiempo real, asegurando una operación óptima y mejora continua.

Soluciones de Preparación Empresarial de Azure Machine Learning: el flujo de prompts aprovecha las robustas soluciones de preparación empresarial de Azure Machine Learning, proporcionando una base segura, escalable y confiable para el desarrollo, experimentación y despliegue de flujos.

Con el flujo de prompts de Azure Machine Learning, los usuarios pueden desatar su agilidad en la ingeniería de prompts, colaborar efectivamente y aprovechar soluciones de grado empresarial para el desarrollo y despliegue exitoso de aplicaciones basadas en LLM.

Combinando la potencia de cómputo, datos y diferentes componentes de Azure ML, los desarrolladores empresariales pueden construir fácilmente sus propias aplicaciones de inteligencia artificial.

Aviso legal: La traducción fue realizada a partir del original por un modelo de IA y puede no ser perfecta. 
Por favor, revise el resultado y haga las correcciones necesarias.