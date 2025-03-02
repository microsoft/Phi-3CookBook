# **Folosirea Microsoft Phi-3.5 tflite pentru a crea o aplicație Android**

Acesta este un exemplu Android care utilizează modele Microsoft Phi-3.5 tflite.

## **📚 Cunoștințe**

API-ul Android LLM Inference vă permite să rulați modele mari de limbaj (LLMs) complet pe dispozitiv pentru aplicațiile Android. Aceste modele pot fi utilizate pentru o gamă largă de sarcini, cum ar fi generarea de text, obținerea de informații în limbaj natural și rezumarea documentelor. Sarcina oferă suport încorporat pentru mai multe modele mari de limbaj text-la-text, permițându-vă să aplicați cele mai recente modele AI generative pe dispozitive direct în aplicațiile Android.

Googld AI Edge Torch este o bibliotecă Python care sprijină conversia modelelor PyTorch în format .tflite, care ulterior pot fi rulate cu TensorFlow Lite și MediaPipe. Aceasta permite aplicații pentru Android, iOS și IoT care pot rula modele complet pe dispozitiv. AI Edge Torch oferă o acoperire largă pentru CPU, cu suport inițial pentru GPU și NPU. AI Edge Torch urmărește să se integreze strâns cu PyTorch, bazându-se pe torch.export() și oferind o acoperire bună a operatorilor Core ATen.

## **🪬 Ghid**

### **🔥 Conversia Microsoft Phi-3.5 pentru suport tflite**

0. Acest exemplu este pentru Android 14+

1. Instalați Python 3.10.12

***Sugestie:*** utilizați conda pentru a instala mediul Python

2. Ubuntu 20.04 / 22.04 (vă rugăm să vă concentrați pe [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Sugestie:*** Utilizați Azure Linux VM sau o mașină virtuală de la un furnizor terț pentru a crea mediul dvs.

3. Accesați bash-ul Linux și instalați biblioteca Python 

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Descărcați Microsoft-3.5-Instruct de pe Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Convertiți Microsoft Phi-3.5 în tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Conversia Microsoft Phi-3.5 într-un pachet Android Mediapipe**

Vă rugăm să instalați mai întâi mediapipe

```bash

pip install mediapipe

```

Rulați acest cod în [notebook-ul dvs.](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Folosirea adb push pentru a transfera modelul pe dispozitivul Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Rularea codului Android**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.ro.png)

**Declinări de responsabilitate**:  
Acest document a fost tradus folosind servicii de traducere automată bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa maternă, ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.