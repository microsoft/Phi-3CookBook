# **Inference Phi-3 in Android**

Let's explore how to perform inference with Phi-3-mini on Android devices. Phi-3-mini is a new series of models from Microsoft that enables deploying Large Language Models (LLMs) on edge and IoT devices.

## Semantic Kernel and Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) is an application framework that lets you create applications compatible with Azure OpenAI Service, OpenAI models, and even local models. If you're new to Semantic Kernel, we recommend checking out the [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Accessing Phi-3-mini Using Semantic Kernel

You can integrate it with the Hugging Face Connector in Semantic Kernel. See this [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

By default, it corresponds to the model ID on Hugging Face. However, you can also connect to a locally hosted Phi-3-mini model server.

### Running Quantized Models with Ollama or LlamaEdge

Many users prefer working with quantized models to run them locally. [Ollama](https://ollama.com/) and [LlamaEdge](https://llamaedge.com) allow individuals to use various quantized models:

#### Ollama

You can run `ollama run Phi-3` directly or configure it for offline use by creating a `Modelfile` with the path to your `.gguf` file.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

If you want to use `.gguf` files both in the cloud and on edge devices, LlamaEdge is a great option. Check out this [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) to get started.

### Installing and Running on Android Phones

1. **Download the MLC Chat app** (Free) for Android phones.
2. Download the APK file (148MB) and install it on your device.
3. Open the MLC Chat app. You'll find a list of AI models, including Phi-3-mini.

In summary, Phi-3-mini offers exciting opportunities for generative AI on edge devices, and you can start exploring its potential on Android.

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.