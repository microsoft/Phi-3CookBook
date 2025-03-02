# **Phi Family Quantization**

Model quantization refers to the process of mapping a neural network model's parameters (such as weights and activation values) from a large value range (often continuous) to a smaller, finite range. This technique reduces the model's size and computational complexity, enhancing its efficiency in resource-constrained environments like mobile devices or embedded systems. Quantization achieves compression by lowering parameter precision, but it also introduces some loss of accuracy. Therefore, it's crucial to strike a balance between model size, computational complexity, and precision during quantization. Common quantization methods include fixed-point quantization, floating-point quantization, and others. The choice of quantization strategy depends on specific scenarios and requirements.

Our goal is to deploy GenAI models on edge devices, enabling broader adoption of GenAI use cases across mobile devices, AI PCs/Copilot+PCs, and traditional IoT devices. By utilizing quantized models, we can adapt deployment to different edge devices. Coupled with hardware manufacturers' acceleration frameworks and quantization models, we can create improved SLM application scenarios.

In quantization, we have different precision levels (INT4, INT8, FP16, FP32). Below is an explanation of the commonly used quantization precisions.

### **INT4**

INT4 quantization is an aggressive method that maps model weights and activation values to 4-bit integers. Due to its smaller representation range and reduced precision, INT4 quantization often results in greater accuracy loss. However, compared to INT8, INT4 further reduces storage requirements and computational complexity. It's worth noting that INT4 quantization is relatively uncommon in practice, as its low precision may lead to significant degradation in model performance. Additionally, not all hardware supports INT4 operations, so hardware compatibility must be considered when selecting this method.

### **INT8**

INT8 quantization involves converting a model's weights and activations from floating-point numbers to 8-bit integers. Although INT8 has a smaller range and lower precision, it significantly reduces storage and computation demands. In INT8 quantization, weights and activations undergo a process involving scaling and offset to retain as much of the original floating-point information as possible. During inference, these quantized values are dequantized back to floating-point for computation and then re-quantized to INT8 for the next step. This approach maintains sufficient accuracy for most applications while delivering high computational efficiency.

### **FP16**

FP16, or 16-bit floating-point format, reduces memory usage by half compared to FP32 (32-bit floating-point format), offering significant benefits in large-scale deep learning applications. FP16 enables loading larger models or processing more data within the same GPU memory constraints. As modern GPUs increasingly support FP16 operations, this format may also improve computational speed. However, FP16 has inherent limitations, such as lower precision, which can lead to numerical instability or accuracy loss in some cases.

### **FP32**

FP32 provides higher precision and can represent a wide range of values accurately. It is preferred in scenarios requiring complex mathematical operations or high-precision results. However, its higher precision comes at the cost of increased memory usage and longer computation times. For large-scale deep learning models with numerous parameters and massive datasets, FP32 may lead to GPU memory shortages or slower inference speeds.

For mobile or IoT devices, Phi-3.x models can be converted to INT4, while AI PCs/Copilot PCs can use higher precisions such as INT8, FP16, or FP32.

Currently, different hardware manufacturers provide various frameworks to support generative models, such as Intel's OpenVINO, Qualcomm's QNN, Apple's MLX, and Nvidia's CUDA. These frameworks, combined with model quantization, enable local deployment.

From a technical perspective, quantized models can be stored in various formats, such as PyTorch/TensorFlow formats, GGUF, and ONNX. I have compared GGUF and ONNX formats and their application scenarios. I recommend the ONNX quantization format due to its robust support from model frameworks to hardware. In this chapter, we will focus on using ONNX Runtime for GenAI, OpenVINO, and Apple MLX for model quantization (if you have a better approach, feel free to submit a PR).

**This chapter includes:**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

It seems like "mo" could refer to a specific language, but it's not clear which one you mean. Could you clarify which language you'd like this text translated into? For example, are you referring to Maori, Mongolian, or another language? Let me know so I can assist you better!