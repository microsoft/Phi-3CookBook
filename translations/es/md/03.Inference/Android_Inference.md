# **Inferencia de Phi-3 en Android**

Vamos a explorar cómo puedes realizar inferencias con Phi-3-mini en dispositivos Android. Phi-3-mini es una nueva serie de modelos de Microsoft que permite el despliegue de Modelos de Lenguaje Grande (LLMs) en dispositivos de borde y dispositivos IoT.

## Semantic Kernel e Inferencia

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) es un marco de aplicación que te permite crear aplicaciones compatibles con Azure OpenAI Service, modelos de OpenAI e incluso modelos locales. Si eres nuevo en Semantic Kernel, te sugerimos que revises el [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Para Acceder a Phi-3-mini Usando Semantic Kernel

Puedes combinarlo con el Hugging Face Connector en Semantic Kernel. Consulta este [Código de Ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Por defecto, corresponde al ID del modelo en Hugging Face. Sin embargo, también puedes conectarte a un servidor de modelos Phi-3-mini construido localmente.

### Llamando a Modelos Cuantificados con Ollama o LlamaEdge

Muchos usuarios prefieren usar modelos cuantificados para ejecutar modelos localmente. [Ollama](https://ollama.com/) y [LlamaEdge](https://llamaedge.com) permiten a los usuarios individuales llamar a diferentes modelos cuantificados:

#### Ollama

Puedes ejecutar directamente `ollama run Phi-3` o configurarlo sin conexión creando un `Modelfile` con la ruta a tu archivo `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Código de Ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Si deseas usar archivos `.gguf` en la nube y en dispositivos de borde simultáneamente, LlamaEdge es una excelente opción. Puedes consultar este [código de ejemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) para comenzar.

### Instalar y Ejecutar en Teléfonos Android

1. **Descarga la app MLC Chat** (Gratis) para teléfonos Android.
2. Descarga el archivo APK (148MB) e instálalo en tu dispositivo.
3. Inicia la app MLC Chat. Verás una lista de modelos de IA, incluyendo Phi-3-mini.

En resumen, Phi-3-mini abre emocionantes posibilidades para la IA generativa en dispositivos de borde, y puedes comenzar a explorar sus capacidades en Android.

**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción humana profesional. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.