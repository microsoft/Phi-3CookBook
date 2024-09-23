# **Inferencia de Phi-3 en Android** 

Exploremos cómo puedes realizar inferencia con Phi-3-mini en dispositivos Android. Phi-3-mini es una nueva serie de modelos de Microsoft que permite el despliegue de Modelos de Lenguaje de Gran Tamaño (LLMs) en dispositivos de borde y dispositivos IoT. 

## Semantic Kernel e Inferencia:
[Semantic Kernel](https://github.com/microsoft/semantic-kernel) es un marco de aplicaciones que te permite crear aplicaciones compatibles con Azure OpenAI Service, modelos de OpenAI e incluso modelos locales. Si eres nuevo en Semantic Kernel, te sugerimos que consultes el [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)

### Para acceder a Phi-3-mini usando Semantic Kernel:
Puedes combinarlo con el Conector de Hugging Face en Semantic Kernel. [Código de ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)

Por defecto, corresponde al ID del modelo en Hugging Face. Sin embargo, también puedes conectarte a un servidor de modelo Phi-3-mini construido localmente.

### Llamando a modelos cuantizados con Ollama o LlamaEdge:

Muchos usuarios prefieren usar modelos cuantizados para ejecutar modelos localmente.
[Ollama](https://ollama.com/) y [LlamaEdge](https://llamaedge.com) permiten a los usuarios individuales llamar a diferentes modelos cuantizados:

**Ollama**

Puedes ejecutar directamente ollama run Phi-3 o configurarlo sin conexión creando un Modelfile con la ruta a tu archivo gguf.

```
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> {{.Prompt}}<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Código de ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

**LlamaEdge** 

Si deseas usar gguf en la nube y en dispositivos de borde simultáneamente, LlamaEdge es una gran opción.
[Código de ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)

### Instalar y ejecutar en teléfonos Android:
Descarga la aplicación MLC Chat (gratuita) para teléfonos Android.
Necesitarás descargar el archivo APK (148 MB) e instalarlo.
Inicia la aplicación MLC Chat, y verás una lista de modelos de IA, incluyendo Phi-3-mini.

En resumen, Phi-3-mini abre emocionantes posibilidades para la IA generativa en dispositivos de borde, y puedes comenzar a explorar sus capacidades en Android.

Aviso legal: La traducción fue realizada a partir del original por un modelo de IA y puede no ser perfecta. Por favor, revise el resultado y haga las correcciones necesarias.