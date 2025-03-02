# **Microsoft Phi-3.5 tflite -mallin käyttäminen Android-sovelluksen luomiseen**

Tämä on Android-esimerkki, jossa käytetään Microsoft Phi-3.5 tflite -malleja.

## **📚 Tietoa**

Android LLM Inference API:n avulla voit suorittaa suuria kielimalleja (LLM) täysin laitteessa Android-sovelluksille. Näitä malleja voidaan käyttää monenlaisiin tehtäviin, kuten tekstin generointiin, tiedon hakemiseen luonnollisella kielellä ja dokumenttien tiivistämiseen. API tarjoaa sisäänrakennetun tuen useille tekstistä-tekstiin suurille kielimalleille, joten voit hyödyntää uusimpia laitteessa toimivia generatiivisia AI-malleja Android-sovelluksissasi.

Googlen AI Edge Torch on Python-kirjasto, joka tukee PyTorch-mallien muuntamista .tflite-muotoon, jota voidaan ajaa TensorFlow Lite- ja MediaPipe-ympäristöissä. Tämä mahdollistaa täysin laitteessa toimivat sovellukset Androidille, iOS:lle ja IoT-laitteille. AI Edge Torch tarjoaa laajan CPU-tuen sekä alkuvaiheen GPU- ja NPU-tuen. AI Edge Torch pyrkii tiiviiseen integraatioon PyTorchin kanssa hyödyntäen torch.export()-toimintoa ja tarjoamalla kattavan tuen Core ATen -operaattoreille.

## **🪬 Ohjeet**

### **🔥 Microsoft Phi-3.5:n muuntaminen tflite-muotoon**

0. Tämä esimerkki on tarkoitettu Android 14+:lle

1. Asenna Python 3.10.12

***Suositus:*** käytä Condaa Python-ympäristösi asentamiseen

2. Ubuntu 20.04 / 22.04 (keskity [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Suositus:*** käytä Azure Linux VM:ää tai kolmannen osapuolen pilvipalvelimen VM:ää ympäristösi luomiseen

3. Siirry Linux-bashiin ja asenna Python-kirjasto

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Lataa Microsoft-3.5-Instruct Hugging Facesta

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Muunna Microsoft Phi-3.5 tflite-muotoon

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5:n muuntaminen Android Mediapipe Bundleksi**

Asenna ensin mediapipe

```bash

pip install mediapipe

```

aja tämä koodi [notebookissasi](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Tehtävämallin siirtäminen adb push -komennolla Android-laitteesi hakemistoon**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Android-koodin suorittaminen**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.fi.png)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisia tekoälykäännöspalveluja käyttäen. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittistä tietoa varten suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.