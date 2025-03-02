# **Korištenje Microsoft Phi-3.5 tflite za kreiranje Android aplikacije**

Ovo je Android primjer koji koristi Microsoft Phi-3.5 tflite modele.

## **📚 Znanje**

Android LLM Inference API omogućuje pokretanje velikih jezičnih modela (LLM-ova) potpuno na uređaju za Android aplikacije. Možete ih koristiti za obavljanje širokog raspona zadataka, poput generiranja teksta, dohvaćanja informacija u obliku prirodnog jezika i sažimanja dokumenata. Ova funkcionalnost nudi ugrađenu podršku za više tekst-u-tekst velikih jezičnih modela, tako da možete primijeniti najnovije generativne AI modele na uređaju u svojim Android aplikacijama.

Google AI Edge Torch je Python biblioteka koja podržava pretvaranje PyTorch modela u .tflite format, koji se zatim može pokretati pomoću TensorFlow Lite i MediaPipe-a. Ovo omogućuje aplikacijama za Android, iOS i IoT da pokreću modele potpuno na uređaju. AI Edge Torch nudi široku pokrivenost CPU-a, uz početnu podršku za GPU i NPU. AI Edge Torch teži bliskoj integraciji s PyTorchom, nadograđujući se na torch.export() i pružajući dobru pokrivenost Core ATen operatora.

## **🪬 Upute**

### **🔥 Pretvorba Microsoft Phi-3.5 u tflite podršku**

0. Ovaj primjer je za Android 14+

1. Instalirajte Python 3.10.12

***Prijedlog:*** koristite conda za instalaciju Python okruženja

2. Ubuntu 20.04 / 22.04 (fokusirajte se na [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Prijedlog:*** Koristite Azure Linux VM ili VM treće strane za kreiranje svog okruženja

3. Otvorite Linux bash kako biste instalirali Python biblioteku

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Preuzmite Microsoft-3.5-Instruct s Hugging face-a

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Pretvorite Microsoft Phi-3.5 u tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Pretvorba Microsoft Phi-3.5 u Android Mediapipe Bundle**

Prvo instalirajte mediapipe

```bash

pip install mediapipe

```

Pokrenite ovaj kod u [vašoj bilježnici](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Korištenje adb push za premještanje modela zadatka na putanju vašeg Android uređaja**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Pokretanje vašeg Android koda**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.hr.png)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga strojno baziranog AI prijevoda. Iako nastojimo postići točnost, molimo vas da budete svjesni da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.