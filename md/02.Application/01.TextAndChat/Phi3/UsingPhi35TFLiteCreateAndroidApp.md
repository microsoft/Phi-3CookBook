# **Using Microsoft Phi-3.5 tflite to create Android app**

This is an Android sample using Microsoft Phi-3.5 tflite models.

## **📚 Knowledge**

Android LLM Inference API lets you run large language models (LLMs) completely on-device for Android applications, which you can use to perform a wide range of tasks, such as generating text, retrieving information in natural language form, and summarizing documents. The task provides built-in support for multiple text-to-text large language models, so you can apply the latest on-device generative AI models to your Android apps.

Googld AI Edge Torch is a python library that supports converting PyTorch models into a .tflite format, which can then be run with TensorFlow Lite and MediaPipe. This enables applications for Android, iOS and IoT that can run models completely on-device. AI Edge Torch offers broad CPU coverage, with initial GPU and NPU support. AI Edge Torch seeks to closely integrate with PyTorch, building on top of torch.export() and providing good coverage of Core ATen operators.


## **🪬 Guideline**

### **🔥 Convert Microsoft Phi-3.5 to tflite support**

0. This sample is for Android 14+

1. Install Python 3.10.12

***Suggestion:*** using conda to install your Python env

2. Ubuntu 20.04 / 22.04 (please focus on [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Suggestion:*** Using Azure Linux VM or 3rd party cloud vm to create your env

3. Go to your Linux bash , to install Python library 

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Download Microsoft-3.5-Instruct from Hugging face


```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Convert Microsoft Phi-3.5 to tflite


```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```


### **🔥 Convert to Microsoft Phi-3.5 to Android Mediapipe Bundle**

please install mediapipe firstly

```bash

pip install mediapipe

```

run this code in [your notebook](../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)



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


### **🔥 Using adb push task model to your  Android devices path**


```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Running your Android code**

![demo](../../../../imgs/02/android-tf/demo.png)









