# Phi-3 硬體支援

Microsoft Phi-3 已經針對 ONNX Runtime 進行了優化，並支援 Windows DirectML。它能在各種硬體上良好運行，包括 GPU、CPU，甚至是移動設備。

## 設備硬體
具體支持的硬體包括：

- GPU SKU: RTX 4090 (DirectML)
- GPU SKU: 1 A100 80GB (CUDA)
- CPU SKU: Standard F64s v2 (64 vCPUs, 128 GiB 記憶體)

## 移動設備 SKU

- Android - Samsung Galaxy S21
- Apple iPhone 14 或更高版本 A16/A17 處理器

## Phi-3 硬體規格

- 最低配置要求。
- Windows: 支援 DirectX 12 的 GPU 和至少 4GB 的總 RAM

CUDA: NVIDIA GPU，計算能力 >= 7.02

![HardwareSupport](../../../../translated_images/phi3hardware.18078f58e0564ddd43d2acce655b86f50c1b2dd9fe2be2b52d49d835bcf36fbc.tw.png)

## 在多個 GPU 上運行 onnxruntime

目前可用的 Phi-3 ONNX 模型僅支援 1 個 GPU。支持 Phi-3 模型的多 GPU 是可能的，但使用 2 個 GPU 的 ORT 不保證比使用 2 個 ORT 實例有更高的吞吐量。

在 [Build 2024 the GenAI ONNX Team](https://youtu.be/WLW4SE8M9i8?si=EtG04UwDvcjunyfC) 宣布，他們已經為 Phi 模型啟用了多實例而不是多 GPU。

目前，這允許你使用 CUDA_VISIBLE_DEVICES 環境變量運行一個 onnnxruntime 或 onnxruntime-genai 實例，如下所示。

```Python
CUDA_VISIBLE_DEVICES=0 python infer.py
CUDA_VISIBLE_DEVICES=1 python infer.py
```

歡迎在 [Azure AI Studio](https://ai.azure.com) 進一步探索 Phi-3。

免責聲明：此翻譯由AI模型從原文翻譯而來，可能不完全準確。請檢查翻譯結果並進行必要的修正。