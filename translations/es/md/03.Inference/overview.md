En el contexto de Phi-3-mini, la inferencia se refiere al proceso de usar el modelo para hacer predicciones o generar resultados basados en datos de entrada. Permíteme proporcionarte más detalles sobre Phi-3-mini y sus capacidades de inferencia.

Phi-3-mini es parte de la serie de modelos Phi-3 lanzados por Microsoft. Estos modelos están diseñados para redefinir lo que es posible con los Modelos de Lenguaje Pequeños (SLMs).

Aquí hay algunos puntos clave sobre Phi-3-mini y sus capacidades de inferencia:

## **Visión General de Phi-3-mini:**
- Phi-3-mini tiene un tamaño de parámetro de 3.8 mil millones.
- Puede ejecutarse no solo en dispositivos de computación tradicionales, sino también en dispositivos de borde como dispositivos móviles y dispositivos IoT.
- El lanzamiento de Phi-3-mini permite a individuos y empresas desplegar SLMs en diferentes dispositivos de hardware, especialmente en entornos con recursos limitados.
- Cubre varios formatos de modelo, incluyendo el formato tradicional de PyTorch, la versión cuantizada del formato gguf y la versión cuantizada basada en ONNX.

## **Acceso a Phi-3-mini:**
Para acceder a Phi-3-mini, puedes usar [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) en una aplicación Copilot. Semantic Kernel es generalmente compatible con Azure OpenAI Service, modelos de código abierto en Hugging Face y modelos locales.
También puedes usar [Ollama](https://ollama.com) o [LlamaEdge](https://llamaedge.com) para llamar a modelos cuantizados. Ollama permite a los usuarios individuales llamar a diferentes modelos cuantizados, mientras que LlamaEdge proporciona disponibilidad multiplataforma para modelos GGUF.

## **Modelos Cuantizados:**
Muchos usuarios prefieren usar modelos cuantizados para la inferencia local. Por ejemplo, puedes ejecutar directamente Ollama run Phi-3 o configurarlo sin conexión usando un Modelfile. El Modelfile especifica la ruta del archivo GGUF y el formato del prompt.

## **Posibilidades de IA Generativa:**
Combinar SLMs como Phi-3-mini abre nuevas posibilidades para la IA generativa. La inferencia es solo el primer paso; estos modelos pueden usarse para diversas tareas en escenarios con recursos limitados, latencia reducida y costos restringidos.

## **Desbloqueando la IA Generativa con Phi-3-mini: Una Guía para la Inferencia y el Despliegue**
Aprende cómo usar Semantic Kernel, Ollama/LlamaEdge y ONNX Runtime para acceder e inferir modelos Phi-3-mini, y explora las posibilidades de la IA generativa en varios escenarios de aplicación.

**Características**
Inferencia del modelo phi3-mini en:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

En resumen, Phi-3-mini permite a los desarrolladores explorar diferentes formatos de modelos y aprovechar la IA generativa en varios escenarios de aplicación.

