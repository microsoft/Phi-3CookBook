In the context of Phi-3-mini, inference refers to the process of using the model to make predictions or generate outputs based on input data. Below are more details about Phi-3-mini and its inference capabilities.

Phi-3-mini is part of the Phi-3 series of models released by Microsoft. These models aim to push the boundaries of what can be achieved with Small Language Models (SLMs).

Here are some key points about Phi-3-mini and its inference capabilities:

## **Phi-3-mini Overview:**
- Phi-3-mini has 3.8 billion parameters.
- It is compatible not only with traditional computing devices but also with edge devices like mobile and IoT devices.
- The release of Phi-3-mini allows both individuals and enterprises to deploy SLMs on diverse hardware, especially in environments with limited resources.
- It supports multiple model formats, including the traditional PyTorch format, the quantized gguf format, and the ONNX-based quantized version.

## **Accessing Phi-3-mini:**
To access Phi-3-mini, you can utilize [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) within a Copilot application. Semantic Kernel works seamlessly with Azure OpenAI Service, open-source models on Hugging Face, and local models.
Additionally, you can use [Ollama](https://ollama.com) or [LlamaEdge](https://llamaedge.com) to invoke quantized models. Ollama enables individual users to interact with different quantized models, while LlamaEdge ensures cross-platform support for GGUF models.

## **Quantized Models:**
Many users prefer quantized models for local inference. For instance, you can directly execute the Ollama run Phi-3 command or configure it offline using a Modelfile. The Modelfile defines the GGUF file path and the prompt format.

## **Generative AI Possibilities:**
SLMs like Phi-3-mini open up exciting opportunities in generative AI. Inference is just the beginning; these models can be applied to a wide range of tasks, particularly in scenarios with constraints on resources, latency, or cost.

## **Unlocking Generative AI with Phi-3-mini: A Guide to Inference and Deployment** 
Discover how to use Semantic Kernel, Ollama/LlamaEdge, and ONNX Runtime to access and infer Phi-3-mini models. Explore the potential of generative AI across diverse application areas.

**Features**
Perform inference with the Phi-3-mini model using:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

In conclusion, Phi-3-mini empowers developers to explore various model formats and utilize generative AI in a variety of application scenarios.

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.