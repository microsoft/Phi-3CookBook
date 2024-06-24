## Phi-3 硬體支援

Microsoft Phi-3 已針對 ONNX Runtime 進行優化，並支援 Windows DirectML。它在各種硬體類型上運行良好，包括 GPU、CPU，甚至是行動裝置。

### 裝置硬體

具體來說，支援的硬體包括：

- GPU SKU: RTX 4090 (DirectML)
- GPU SKU: 1 A100 80GB (CUDA)
- CPU SKU: Standard F64s v2 (64 vCPUs, 128 GiB 記憶體)

### Mobile SKU

- Android - Samsung Galaxy S21
- Apple iPhone 14 或更高版本 A16/A17 處理器

### Phi-3 硬體規格

- 最低配置要求:
- Windows: 支援 DirectX 12 的 GPU 和至少 4GB 的總 RAM

CUDA: NVIDIA GPU with Compute Capability >= 7.02

![HardwareSupport](../../../../imgs/00/phi3hardware.png)

### 在多個 GPU 上執行 onnxruntime

目前可用的 Phi-3 ONNX 模型僅適用於 1 個 GPU。Phi-3 模型有可能支援多 GPU，但使用 2 個 GPU 的 ORT 並不保證會比 2 個 ORT 實例提供更高的吞吐量。

在 [Build 2024 the GenAI ONNX Team](https://youtu.be/WLW4SE8M9i8?si=EtG04UwDvcjunyfC) 宣布他們已經為 Phi 模型啟用了多實例而不是多 GPU。

目前這允許你使用 CUDA_VISIBLE_DEVICES 環境變數來執行一個 onnnxruntime 或 onnxruntime-genai 實例，如下所示。

```Python
CUDA_VISIBLE_DEVICES=0 python infer.py
CUDA_VISIBLE_DEVICES=1 python infer.py
```

隨時在 [Azure AI Studio](https://ai.azure.com) 進一步探索 Phi-3。

