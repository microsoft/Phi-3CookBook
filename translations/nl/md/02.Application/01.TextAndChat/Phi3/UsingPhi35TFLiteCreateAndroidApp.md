# **Microsoft Phi-3.5 tflite gebruiken om een Android-app te maken**

Dit is een Android-sample waarin Microsoft Phi-3.5 tflite-modellen worden gebruikt.

## **📚 Kennis**

De Android LLM Inference API stelt je in staat om grote taalmodellen (LLMs) volledig on-device uit te voeren voor Android-applicaties. Hiermee kun je een breed scala aan taken uitvoeren, zoals het genereren van tekst, het ophalen van informatie in natuurlijke taal en het samenvatten van documenten. De API biedt ingebouwde ondersteuning voor meerdere tekst-naar-tekst LLMs, zodat je de nieuwste generatieve AI-modellen on-device kunt toepassen in je Android-apps.

Google AI Edge Torch is een Python-bibliotheek die het mogelijk maakt om PyTorch-modellen om te zetten naar een .tflite-formaat, dat vervolgens kan worden uitgevoerd met TensorFlow Lite en MediaPipe. Dit maakt toepassingen mogelijk voor Android, iOS en IoT die modellen volledig on-device kunnen draaien. AI Edge Torch biedt brede CPU-ondersteuning, met initiële GPU- en NPU-ondersteuning. AI Edge Torch streeft naar nauwe integratie met PyTorch, bouwt voort op torch.export() en biedt goede dekking van Core ATen-operatoren.

## **🪬 Richtlijnen**

### **🔥 Microsoft Phi-3.5 converteren naar tflite-ondersteuning**

0. Dit voorbeeld is bedoeld voor Android 14+

1. Installeer Python 3.10.12

***Suggestie:*** gebruik conda om je Python-omgeving te installeren

2. Ubuntu 20.04 / 22.04 (richt je op [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Suggestie:*** Gebruik een Azure Linux VM of een externe cloud-VM om je omgeving te creëren

3. Open je Linux-bash om de Python-bibliotheek te installeren

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Download Microsoft-3.5-Instruct van Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Converteer Microsoft Phi-3.5 naar tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 converteren naar een Android Mediapipe Bundle**

Installeer eerst MediaPipe

```bash

pip install mediapipe

```

Voer deze code uit in [je notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Gebruik adb push om het model naar het Android-apparaat te uploaden**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Je Android-code uitvoeren**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.nl.png)

**Disclaimer**:  
Dit document is vertaald met behulp van AI-vertalingsdiensten. Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet verantwoordelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.