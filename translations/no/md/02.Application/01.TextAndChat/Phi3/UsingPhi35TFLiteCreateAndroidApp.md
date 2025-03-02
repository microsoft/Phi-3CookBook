# **Bruke Microsoft Phi-3.5 tflite for å lage Android-app**

Dette er et Android-eksempel som bruker Microsoft Phi-3.5 tflite-modeller.

## **📚 Kunnskap**

Android LLM Inference API lar deg kjøre store språkmodeller (LLMs) helt på enheten for Android-applikasjoner. Disse kan brukes til å utføre en rekke oppgaver, som å generere tekst, hente informasjon i naturlig språkform og oppsummere dokumenter. API-en har innebygd støtte for flere tekst-til-tekst-stor språkmodeller, slik at du kan bruke de nyeste generative AI-modellene på enheten i Android-appene dine.

Google AI Edge Torch er et Python-bibliotek som støtter konvertering av PyTorch-modeller til .tflite-format, som deretter kan kjøres med TensorFlow Lite og MediaPipe. Dette muliggjør applikasjoner for Android, iOS og IoT som kan kjøre modeller helt på enheten. AI Edge Torch tilbyr bred CPU-dekning, med innledende støtte for GPU og NPU. AI Edge Torch søker å integrere tett med PyTorch, bygger videre på torch.export() og gir god dekning av Core ATen-operatører.

## **🪬 Veiledning**

### **🔥 Konverter Microsoft Phi-3.5 til tflite-støtte**

0. Dette eksempelet er for Android 14+

1. Installer Python 3.10.12

***Forslag:*** bruk conda til å installere ditt Python-miljø

2. Ubuntu 20.04 / 22.04 (vennligst fokuser på [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Forslag:*** Bruk Azure Linux VM eller tredjeparts skybasert VM for å opprette miljøet ditt

3. Gå til Linux-bash, og installer Python-biblioteket

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Last ned Microsoft-3.5-Instruct fra Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konverter Microsoft Phi-3.5 til tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Konverter Microsoft Phi-3.5 til Android Mediapipe Bundle**

Installer Mediapipe først

```bash

pip install mediapipe

```

Kjør denne koden i [din notatbok](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Bruk adb push for å laste opp modell til Android-enhetens sti**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Kjøre Android-koden din**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.no.png)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.