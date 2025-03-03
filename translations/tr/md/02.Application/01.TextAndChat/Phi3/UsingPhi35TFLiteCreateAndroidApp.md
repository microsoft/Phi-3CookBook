# **Microsoft Phi-3.5 tflite kullanarak Android uygulaması oluşturma**

Bu, Microsoft Phi-3.5 tflite modellerini kullanan bir Android örneğidir.

## **📚 Bilgi**

Android LLM Inference API, Android uygulamaları için büyük dil modellerini (LLM'ler) tamamen cihaz üzerinde çalıştırmanıza olanak tanır. Bu modellerle metin oluşturma, doğal dil formunda bilgi alma ve belgeleri özetleme gibi geniş bir yelpazede görevler gerçekleştirebilirsiniz. Bu görev, birden fazla metin-üzerine-metni büyük dil modeli için yerleşik destek sunar, böylece en yeni cihaz üzerindeki üretken yapay zeka modellerini Android uygulamalarınıza entegre edebilirsiniz.

Google AI Edge Torch, PyTorch modellerini .tflite formatına dönüştürmeyi destekleyen bir Python kütüphanesidir. Bu format, TensorFlow Lite ve MediaPipe ile çalıştırılabilir. Böylece Android, iOS ve IoT uygulamalarında modeller tamamen cihaz üzerinde çalıştırılabilir. AI Edge Torch geniş CPU desteği sunar ve başlangıç seviyesinde GPU ve NPU desteği sağlar. AI Edge Torch, PyTorch ile yakın entegrasyon hedefler ve torch.export() üzerine inşa edilerek Core ATen operatörlerinin geniş kapsamını sunar.

## **🪬 Kılavuz**

### **🔥 Microsoft Phi-3.5'i tflite desteğine dönüştürme**

0. Bu örnek Android 14+ içindir.

1. Python 3.10.12'yi yükleyin.

***Öneri:*** Python ortamınızı kurmak için conda kullanın.

2. Ubuntu 20.04 / 22.04 (lütfen [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) üzerine odaklanın).

***Öneri:*** Ortamınızı oluşturmak için Azure Linux VM veya üçüncü taraf bir bulut VM kullanın.

3. Linux bash'inize gidin ve Python kütüphanesini yükleyin.

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging Face üzerinden Microsoft-3.5-Instruct'u indirin.

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5'i tflite formatına dönüştürün.

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5'i Android Mediapipe Paketi'ne dönüştürme**

Öncelikle mediapipe'i yükleyin.

```bash

pip install mediapipe

```

Bu kodu [not defterinizde](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) çalıştırın.

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

### **🔥 Modeli adb push kullanarak Android cihazınızın yoluna yükleyin**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Android kodunuzu çalıştırma**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.tr.png)

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.