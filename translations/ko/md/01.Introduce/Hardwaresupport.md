# Phi-3 하드웨어 지원

Microsoft Phi-3는 ONNX Runtime에 최적화되어 있으며 Windows DirectML을 지원합니다. 다양한 하드웨어 유형, 특히 GPU, CPU, 심지어 모바일 장치에서도 잘 작동합니다.

## 장치 하드웨어
지원되는 하드웨어는 다음과 같습니다:

- GPU SKU: RTX 4090 (DirectML)
- GPU SKU: 1 A100 80GB (CUDA)
- CPU SKU: Standard F64s v2 (64 vCPUs, 128 GiB 메모리)

## 모바일 SKU

- 안드로이드 - 삼성 갤럭시 S21
- 애플 아이폰 14 또는 그 이상의 A16/A17 프로세서

## Phi-3 하드웨어 사양

- 최소 구성 요구 사항.
- Windows: DirectX 12를 지원하는 GPU와 최소 4GB의 통합 RAM

CUDA: 계산 능력 >= 7.02를 가진 NVIDIA GPU

![HardwareSupport](../../../../translated_images/phi3hardware.18078f58e0564ddd43d2acce655b86f50c1b2dd9fe2be2b52d49d835bcf36fbc.ko.png)

## 여러 GPU에서 onnxruntime 실행하기

현재 제공되는 Phi-3 ONNX 모델은 1 GPU용입니다. Phi-3 모델에 대해 다중 GPU를 지원하는 것이 가능하지만, 2개의 GPU를 사용하는 ORT가 2개의 ort 인스턴스보다 더 높은 처리량을 제공한다고 보장하지 않습니다.

[Build 2024의 GenAI ONNX 팀](https://youtu.be/WLW4SE8M9i8?si=EtG04UwDvcjunyfC)은 Phi 모델에 대해 다중 GPU 대신 다중 인스턴스를 활성화했다고 발표했습니다.

현재로서는 CUDA_VISIBLE_DEVICES 환경 변수를 사용하여 하나의 onnxruntime 또는 onnxruntime-genai 인스턴스를 다음과 같이 실행할 수 있습니다.

```Python
CUDA_VISIBLE_DEVICES=0 python infer.py
CUDA_VISIBLE_DEVICES=1 python infer.py
```

[Azure AI Studio](https://ai.azure.com)에서 Phi-3를 더 탐색해 보세요.

면책 조항: 이 번역은 AI 모델에 의해 원문에서 번역되었으며 완벽하지 않을 수 있습니다. 
출력을 검토하고 필요한 수정을 해주시기 바랍니다.