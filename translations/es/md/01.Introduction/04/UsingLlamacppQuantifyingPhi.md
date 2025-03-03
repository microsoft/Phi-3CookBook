# **Cuantización de la Familia Phi usando llama.cpp**

## **¿Qué es llama.cpp?**

llama.cpp es una biblioteca de software de código abierto, escrita principalmente en C++, que realiza inferencia en varios Modelos de Lenguaje de Gran Escala (LLMs), como Llama. Su objetivo principal es ofrecer un rendimiento de última generación para la inferencia de LLM en una amplia gama de hardware con una configuración mínima. Además, esta biblioteca cuenta con enlaces para Python, que proporcionan una API de alto nivel para completar texto y un servidor web compatible con OpenAI.

El objetivo principal de llama.cpp es habilitar la inferencia de LLM con una configuración mínima y un rendimiento de última generación en una gran variedad de hardware, tanto localmente como en la nube.

- Implementación en C/C++ puro sin dependencias
- Apple Silicon es un ciudadano de primera clase: optimizado mediante ARM NEON, Accelerate y los frameworks Metal
- Soporte para AVX, AVX2 y AVX512 en arquitecturas x86
- Cuantización en enteros de 1.5 bits, 2 bits, 3 bits, 4 bits, 5 bits, 6 bits y 8 bits para una inferencia más rápida y menor uso de memoria
- Kernels CUDA personalizados para ejecutar LLMs en GPUs NVIDIA (soporte para GPUs AMD mediante HIP)
- Soporte para backends Vulkan y SYCL
- Inferencia híbrida CPU+GPU para acelerar parcialmente modelos más grandes que la capacidad total de VRAM

## **Cuantizando Phi-3.5 con llama.cpp**

El modelo Phi-3.5-Instruct puede ser cuantizado usando llama.cpp, pero Phi-3.5-Vision y Phi-3.5-MoE aún no son compatibles. El formato convertido por llama.cpp es GGUF, que también es el formato de cuantización más utilizado.

En Hugging Face hay una gran cantidad de modelos en formato GGUF cuantizados. AI Foundry, Ollama y LlamaEdge dependen de llama.cpp, por lo que los modelos GGUF también se utilizan con frecuencia.

### **¿Qué es GGUF?**

GGUF es un formato binario optimizado para la carga y guardado rápido de modelos, lo que lo hace altamente eficiente para propósitos de inferencia. GGUF está diseñado para usarse con GGML y otros ejecutores. GGUF fue desarrollado por @ggerganov, quien también es el creador de llama.cpp, un marco popular de inferencia LLM en C/C++. Los modelos desarrollados inicialmente en frameworks como PyTorch pueden convertirse al formato GGUF para ser usados con esos motores.

### **ONNX vs GGUF**

ONNX es un formato tradicional de aprendizaje automático/aprendizaje profundo, bien soportado en diferentes frameworks de IA y con buenos casos de uso en dispositivos de borde. En cuanto a GGUF, está basado en llama.cpp y puede considerarse un producto de la era GenAI. Ambos tienen usos similares. Si buscas un mejor rendimiento en hardware embebido y capas de aplicación, ONNX podría ser tu elección. Si utilizas el framework derivado y la tecnología de llama.cpp, entonces GGUF podría ser más adecuado.

### **Cuantización de Phi-3.5-Instruct usando llama.cpp**

**1. Configuración del entorno**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Cuantización**

Usando llama.cpp, convierte Phi-3.5-Instruct a FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Cuantizando Phi-3.5 a INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Pruebas**

Instala llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Nota*** 

Si usas Apple Silicon, instala llama-cpp-python de esta forma:


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Pruebas 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Recursos**

1. Aprende más sobre llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Aprende más sobre GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.