## Phi-3 硬件支持

微软 Phi-3 已针对 ONNX Runtime 进行了优化，并支持 Windows DirectML。它在各种硬件类型上表现良好，包括 GPU、CPU 甚至移动设备。 

### 硬件设备 
具体来说，支持的硬件包括：

- GPU SKU: RTX 4090 (DirectML)
- GPU SKU: 1 A100 80GB (CUDA)
- CPU SKU: Standard F64s v2 (64 vCPUs, 128 GiB memory)

### Mobile SKU

- Android - Samsung Galaxy S21
- Apple iPhone 14 或更高版本 A16/A17 处理器

### Phi-3 硬件规范
- 最低配置需求:
- Windows: 支持DirectX 12的GPU，最少4GB的总RAM

CUDA: NVIDIA GPU with Compute Capability >= 7.02

![HardwareSupport](../../../../imgs/00/phi3hardware.png)

### 在多GPU上运行onnxruntime 
目前可用的 Phi-3 ONNX 模型仅适用于单个 GPU。虽然可以支持多 GPU 的 Phi-3 模型，但是与 2 个 ORT 实例相比，2 个 GPU 的 ORT 并不能保证会带来更高的吞吐量。 

在 2024 年 Build 大会上，[GenAI ONNX 团队](https://youtu.be/WLW4SE8M9i8?si=EtG04UwDvcjunyfC) 宣布已为 Phi 模型启用多实例而非多 GPU 支持。 

目前，这允许您使用CUDA_VISIBLE_DEVICES 环境变量运行一个 onnxruntime 或 onnxruntime-genai 实例：

```Python
CUDA_VISIBLE_DEVICES=0 python infer.py
CUDA_VISIBLE_DEVICES=1 python infer.py
```
请在 [Azure AI Studio](https://ai.azure.com) 中进一步探索 Phi-3。


