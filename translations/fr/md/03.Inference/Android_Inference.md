# **Inferencia Phi-3 en Android**

Exploremos cómo puedes realizar inferencia con Phi-3-mini en dispositivos Android. Phi-3-mini es una nueva serie de modelos de Microsoft que permite el despliegue de Grandes Modelos de Lenguaje (LLMs) en dispositivos edge y dispositivos IoT.

## Semantic Kernel e Inferencia:
[Semantic Kernel](https://github.com/microsoft/semantic-kernel) es un marco de aplicaciones que te permite crear aplicaciones compatibles con Azure OpenAI Service, modelos de OpenAI e incluso modelos locales. Si eres nuevo en Semantic Kernel, te sugerimos que consultes el [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)

### Para acceder a Phi-3-mini usando Semantic Kernel:
Puedes combinarlo con el Conector de Hugging face en Semantic Kernel. [Código de Ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)

Por defecto, corresponde al ID del modelo en Hugging face. Sin embargo, también puedes conectarte a un servidor de modelos Phi-3-mini construido localmente.

### Llamando a Modelos Cuantificados con Ollama o LlamaEdge:

Muchos usuarios prefieren usar modelos cuantificados para ejecutar modelos localmente.
[Ollama](https://ollama.com/) y [LlamaEdge](https://llamaedge.com) permiten a los usuarios individuales llamar a diferentes modelos cuantificados:

**Ollama**

Puedes ejecutar directamente `ollama run Phi-3` o configurarlo sin conexión creando un Modelfile con la ruta a tu archivo gguf.

```
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> {{.Prompt}}<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096

```

[Código de Ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)



**LlamaEdge** 

Si deseas usar gguf tanto en la nube como en dispositivos edge simultáneamente, LlamaEdge es una excelente opción. [Código de Ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

### Install and Run on Android Phones:
Descarga la aplicación MLC Chat (Gratis) para teléfonos Android. Necesitarás descargar el archivo APK (148MB) e instalarlo. Inicia la aplicación MLC Chat y verás una lista de modelos de IA, incluyendo Phi-3-mini.

En resumen, Phi-3-mini abre posibilidades emocionantes para la IA generativa en dispositivos edge, y puedes comenzar a explorar sus capacidades en Android.

Avertissement : La traduction a été réalisée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. Veuillez examiner le résultat et apporter les corrections nécessaires.