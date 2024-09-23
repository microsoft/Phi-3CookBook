# Tecnologías clave mencionadas incluyen

1. [DirectML](https://learn.microsoft.com/windows/ai/directml/dml?WT.mc_id=aiml-138114-kinfeylo) - una API de bajo nivel para el aprendizaje automático acelerado por hardware construida sobre DirectX 12.
2. [CUDA](https://blogs.nvidia.com/blog/what-is-cuda-2/) - una plataforma de computación paralela y modelo de interfaz de programación de aplicaciones (API) desarrollada por Nvidia, que permite el procesamiento de propósito general en unidades de procesamiento gráfico (GPUs).
3. [ONNX](https://onnx.ai/) (Open Neural Network Exchange) - un formato abierto diseñado para representar modelos de aprendizaje automático que proporciona interoperabilidad entre diferentes marcos de ML.
4. [GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) (Generic Graph Update Format) - un formato utilizado para representar y actualizar modelos de aprendizaje automático, particularmente útil para modelos de lenguaje más pequeños que pueden funcionar eficazmente en CPUs con cuantización de 4-8 bits.

## DirectML

DirectML es una API de bajo nivel que permite el aprendizaje automático acelerado por hardware. Está construida sobre DirectX 12 para utilizar la aceleración de GPU y es independiente del proveedor, lo que significa que no requiere cambios en el código para funcionar con diferentes proveedores de GPU. Se utiliza principalmente para cargas de trabajo de entrenamiento e inferencia de modelos en GPUs.

En cuanto al soporte de hardware, DirectML está diseñado para trabajar con una amplia gama de GPUs, incluidas las GPUs integradas y discretas de AMD, las GPUs integradas de Intel y las GPUs discretas de NVIDIA. Es parte de la Plataforma de IA de Windows y es compatible con Windows 10 y 11, lo que permite el entrenamiento e inferencia de modelos en cualquier dispositivo con Windows.

Ha habido actualizaciones y oportunidades relacionadas con DirectML, como el soporte de hasta 150 operadores ONNX y su uso tanto por el runtime de ONNX como por WinML. Está respaldado por importantes Proveedores de Hardware Integrado (IHVs), cada uno implementando varios metacomandos.

## CUDA

CUDA, que significa Compute Unified Device Architecture, es una plataforma de computación paralela y un modelo de interfaz de programación de aplicaciones (API) creado por Nvidia. Permite a los desarrolladores de software utilizar una unidad de procesamiento gráfico (GPU) habilitada para CUDA para el procesamiento de propósito general, un enfoque denominado GPGPU (General-Purpose computing on Graphics Processing Units). CUDA es un habilitador clave de la aceleración de GPU de Nvidia y se utiliza ampliamente en diversos campos, incluidos el aprendizaje automático, la computación científica y el procesamiento de video.

El soporte de hardware para CUDA es específico de las GPUs de Nvidia, ya que es una tecnología propietaria desarrollada por Nvidia. Cada arquitectura admite versiones específicas del kit de herramientas CUDA, que proporciona las bibliotecas y herramientas necesarias para que los desarrolladores construyan y ejecuten aplicaciones CUDA.

## ONNX

ONNX (Open Neural Network Exchange) es un formato abierto diseñado para representar modelos de aprendizaje automático. Proporciona una definición de un modelo de gráfico de computación extensible, así como definiciones de operadores integrados y tipos de datos estándar. ONNX permite a los desarrolladores mover modelos entre diferentes marcos de ML, habilitando la interoperabilidad y facilitando la creación y el despliegue de aplicaciones de IA.

Phi3 mini puede funcionar con ONNX Runtime en CPU y GPU en diferentes dispositivos, incluidos plataformas de servidor, escritorios con Windows, Linux y Mac, y CPUs móviles.
Las configuraciones optimizadas que hemos añadido son

- Modelos ONNX para int4 DML: Cuantizados a int4 a través de AWQ
- Modelo ONNX para fp16 CUDA
- Modelo ONNX para int4 CUDA: Cuantizados a int4 a través de RTN
- Modelo ONNX para int4 CPU y Móvil: Cuantizados a int4 a través de RTN

## Llama.cpp

Llama.cpp es una biblioteca de software de código abierto escrita en C++. Realiza inferencia en varios Modelos de Lenguaje Grande (LLMs), incluyendo Llama. Desarrollada junto con la biblioteca ggml (una biblioteca de tensores de propósito general), llama.cpp tiene como objetivo proporcionar una inferencia más rápida y un menor uso de memoria en comparación con la implementación original en Python. Soporta optimización de hardware, cuantización y ofrece una API simple y ejemplos. Si estás interesado en una inferencia eficiente de LLM, llama.cpp vale la pena explorar ya que Phi3 puede ejecutar Llama.cpp.

## GGUF

GGUF (Generic Graph Update Format) es un formato utilizado para representar y actualizar modelos de aprendizaje automático. Es particularmente útil para modelos de lenguaje más pequeños (SLMs) que pueden funcionar eficazmente en CPUs con cuantización de 4-8 bits. GGUF es beneficioso para la creación rápida de prototipos y la ejecución de modelos en dispositivos de borde o en trabajos por lotes como las canalizaciones de CI/CD.

        Descargo de responsabilidad: La traducción fue realizada a partir del original por un modelo de IA y puede no ser perfecta. 
        Por favor, revise el resultado y haga las correcciones necesarias.