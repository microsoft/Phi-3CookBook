# **Quantifying Phi Family**

Model quantization refers to the process of mapping the parameters (such as weights and activation values) in a neural network model from a large value range (usually a continuous range) to a smaller, finite value range. This technique can reduce the model's size and computational complexity, improving its operational efficiency in resource-constrained environments such as mobile devices or embedded systems. Model quantization achieves compression by reducing parameter precision, but it also introduces some precision loss. Therefore, during the quantization process, it's essential to balance model size, computational complexity, and precision. Common quantization methods include fixed-point quantization, floating-point quantization, and more. You can choose the appropriate quantization strategy based on specific scenarios and requirements.

We aim to deploy the GenAI model to edge devices, enabling more devices to participate in GenAI scenarios, such as mobile devices, AI PCs/Copilot PCs, and traditional IoT devices. By leveraging quantized models, we can deploy to various edge devices according to their specific hardware. Combined with the model acceleration frameworks and quantization tools provided by hardware manufacturers, we can create better SLM application scenarios.

In the quantization context, we have different precision levels (INT4, INT8, FP16, FP32). Below is an explanation of the commonly used quantization precisions:

### **INT4**

INT4 quantization is an aggressive method that quantizes the model's weights and activation values into 4-bit integers. Due to its smaller representation range and lower precision, INT4 quantization often results in greater precision loss. However, compared to INT8 quantization, INT4 further reduces the model's storage requirements and computational complexity. It’s worth noting that INT4 quantization is relatively rare in practical applications because the very low precision can significantly degrade model performance. Additionally, not all hardware supports INT4 operations, so hardware compatibility should be considered when selecting a quantization method.

### **INT8**

INT8 quantization involves converting a model’s weights and activations from floating-point numbers to 8-bit integers. While INT8 integers represent a smaller and less precise numerical range, this method significantly reduces storage and computation requirements. In INT8 quantization, the model's weights and activation values are quantized using scaling and offset processes to retain as much of the original floating-point information as possible. During inference, these quantized values are dequantized back to floating-point numbers for computation and then re-quantized to INT8 for the next step. This approach can deliver sufficient accuracy in most applications while maintaining high computational efficiency.

### **FP16**

The FP16 format, which uses 16-bit floating-point numbers (float16), reduces memory usage by half compared to 32-bit floating-point numbers (float32). This provides significant advantages in large-scale deep learning applications. The FP16 format allows larger models to be loaded or more data to be processed within the same GPU memory constraints. As modern GPU hardware increasingly supports FP16 operations, using the FP16 format may also improve computational speed. However, FP16 has inherent drawbacks, including lower precision, which may lead to numerical instability or precision loss in certain cases.

### **FP32**

The FP32 format offers higher precision and can accurately represent a wide range of values. It is preferred in scenarios involving complex mathematical operations or where high-precision results are required. However, higher precision also entails greater memory usage and longer computation times. For large-scale deep learning models, especially those with numerous parameters and massive datasets, the FP32 format may result in GPU memory limitations or slower inference speeds.

On mobile or IoT devices, Phi-3.x models can be converted to INT4, while AI PCs/Copilot PCs can utilize higher precision levels like INT8, FP16, or FP32.

Currently, different hardware manufacturers provide various frameworks to support generative models, such as Intel's OpenVINO, Qualcomm's QNN, Apple's MLX, and Nvidia's CUDA. These frameworks, combined with model quantization, enable local deployment.

From a technical perspective, quantization supports various formats, such as PyTorch/TensorFlow formats, GGUF, and ONNX. I’ve compared the GGUF and ONNX formats and their application scenarios. Here, I recommend the ONNX quantization format, which offers excellent support from model frameworks to hardware. In this chapter, we will focus on using ONNX Runtime for GenAI, OpenVINO, and Apple MLX to perform model quantization (if you have a better method, feel free to share it with us by submitting a PR).

**This chapter includes**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.