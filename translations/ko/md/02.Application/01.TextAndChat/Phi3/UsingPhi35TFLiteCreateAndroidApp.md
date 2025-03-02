# **Microsoft Phi-3.5 tflite를 사용하여 Android 앱 만들기**

이 문서는 Microsoft Phi-3.5 tflite 모델을 사용하는 Android 샘플입니다.

## **📚 지식**

Android LLM Inference API를 사용하면 Android 애플리케이션에서 대형 언어 모델(LLMs)을 완전히 온디바이스로 실행할 수 있습니다. 이를 통해 텍스트 생성, 자연어 형식으로 정보 검색, 문서 요약 등 다양한 작업을 수행할 수 있습니다. 이 API는 여러 텍스트-텍스트 대형 언어 모델을 기본적으로 지원하므로, 최신 온디바이스 생성 AI 모델을 Android 앱에 적용할 수 있습니다.

Google AI Edge Torch는 PyTorch 모델을 .tflite 형식으로 변환할 수 있는 Python 라이브러리로, 변환된 모델은 TensorFlow Lite 및 MediaPipe에서 실행할 수 있습니다. 이를 통해 Android, iOS 및 IoT 애플리케이션에서 모델을 온디바이스로 실행할 수 있습니다. AI Edge Torch는 넓은 CPU 지원을 제공하며, 초기 GPU 및 NPU 지원도 포함하고 있습니다. AI Edge Torch는 PyTorch와의 밀접한 통합을 목표로 하며, torch.export()를 기반으로 구축되고 Core ATen 연산자의 높은 커버리지를 제공합니다.

## **🪬 가이드라인**

### **🔥 Microsoft Phi-3.5를 tflite로 변환하기**

0. 이 샘플은 Android 14+를 대상으로 합니다.

1. Python 3.10.12 설치

***제안:*** conda를 사용하여 Python 환경을 설치하는 것을 추천합니다.

2. Ubuntu 20.04 / 22.04 (참고: [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***제안:*** Azure Linux VM 또는 타사 클라우드 VM을 사용하여 환경을 설정하는 것을 추천합니다.

3. Linux bash로 이동하여 Python 라이브러리를 설치하세요.

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging Face에서 Microsoft-3.5-Instruct를 다운로드하세요.

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5를 tflite로 변환하세요.

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5를 Android Mediapipe 번들로 변환하기**

먼저 mediapipe를 설치하세요.

```bash

pip install mediapipe

```

[노트북](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)에서 아래 코드를 실행하세요.

```python

import mediapipe as mp
from mediapipe.tasks.python.genai import bundler

config = bundler.BundleConfig(
    tflite_model='Your Phi-3.5 tflite model path',
    tokenizer_model='Your Phi-3.5 tokenizer model path',
    start_token='start_token',
    stop_tokens=[STOP_TOKENS],
    output_filename='Your Phi-3.5 task model path',
    enable_bytes_to_unicode_mapping=True or Flase,
)
bundler.create_bundle(config)

```

### **🔥 adb를 사용하여 Android 디바이스 경로로 모델 푸시하기**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Android 코드 실행하기**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.ko.png)

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서(모국어로 작성된 문서)가 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.