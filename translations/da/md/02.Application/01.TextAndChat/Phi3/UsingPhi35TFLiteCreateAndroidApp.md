# **Brug af Microsoft Phi-3.5 tflite til at oprette Android-app**

Dette er et Android-eksempel, der bruger Microsoft Phi-3.5 tflite-modeller.

## **📚 Viden**

Android LLM Inference API giver dig mulighed for at køre store sprogmodeller (LLMs) direkte på enheden til Android-applikationer. Du kan bruge det til at udføre en bred vifte af opgaver, såsom at generere tekst, hente information i naturligt sprog og opsummere dokumenter. API'en understøtter flere tekst-til-tekst store sprogmodeller, så du kan anvende de nyeste generative AI-modeller direkte på dine Android-apps.

Google AI Edge Torch er et Python-bibliotek, der understøtter konvertering af PyTorch-modeller til .tflite-format, som derefter kan køres med TensorFlow Lite og MediaPipe. Dette muliggør applikationer til Android, iOS og IoT, der kan køre modeller fuldstændigt på enheden. AI Edge Torch tilbyder bred CPU-understøttelse og indledende GPU- og NPU-support. AI Edge Torch stræber efter tæt integration med PyTorch, bygger oven på torch.export() og tilbyder god dækning af Core ATen-operatører.

## **🪬 Retningslinje**

### **🔥 Konverter Microsoft Phi-3.5 til tflite-understøttelse**

0. Dette eksempel er til Android 14+

1. Installer Python 3.10.12

***Forslag:*** Brug conda til at installere dit Python-miljø

2. Ubuntu 20.04 / 22.04 (fokuser venligst på [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Forslag:*** Brug Azure Linux VM eller en tredjeparts cloud-VM til at oprette dit miljø

3. Gå til din Linux bash for at installere Python-biblioteket

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Download Microsoft-3.5-Instruct fra Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konverter Microsoft Phi-3.5 til tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Konverter Microsoft Phi-3.5 til Android Mediapipe Bundle**

Installer venligst Mediapipe først

```bash

pip install mediapipe

```

Kør denne kode i [din notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Brug adb push til at overføre model til din Android-enheds sti**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Kør din Android-kode**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.da.png)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-baserede maskinoversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.