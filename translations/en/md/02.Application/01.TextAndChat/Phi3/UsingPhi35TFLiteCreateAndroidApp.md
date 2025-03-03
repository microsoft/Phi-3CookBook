# **Using Microsoft Phi-3.5 tflite to create Android app**

This is an Android sample using Microsoft Phi-3.5 tflite models.

## **📚 Knowledge**

The Android LLM Inference API allows you to run large language models (LLMs) entirely on-device for Android applications. These models can be used for a variety of tasks, including text generation, retrieving information in natural language, and document summarization. The API offers built-in support for several text-to-text large language models, enabling you to integrate the latest on-device generative AI models into your Android applications.

Google AI Edge Torch is a Python library that facilitates the conversion of PyTorch models into the .tflite format, which can then be executed using TensorFlow Lite and MediaPipe. This allows for Android, iOS, and IoT applications to run models entirely on-device. AI Edge Torch provides extensive CPU support, with initial support for GPU and NPU as well. It is designed to integrate closely with PyTorch, leveraging torch.export() and ensuring comprehensive coverage of Core ATen operators.

## **🪬 Guideline**

### **🔥 Convert Microsoft Phi-3.5 to tflite support**

0. This sample is compatible with Android 14+.

1. Install Python 3.10.12.

***Suggestion:*** Use conda to set up your Python environment.

2. Use Ubuntu 20.04 / 22.04 (refer to [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch)).

***Suggestion:*** Use an Azure Linux VM or a third-party cloud VM to set up your environment.

3. Open your Linux bash and install the required Python library:

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Download Microsoft-3.5-Instruct from Hugging Face:

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Convert Microsoft Phi-3.5 to tflite:

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Convert Microsoft Phi-3.5 to Android Mediapipe Bundle**

First, install MediaPipe:

```bash

pip install mediapipe

```

Run this code in [your notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb):

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

### **🔥 Use adb to push the task model to your Android device path**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Run your Android code**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.en.png)

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.