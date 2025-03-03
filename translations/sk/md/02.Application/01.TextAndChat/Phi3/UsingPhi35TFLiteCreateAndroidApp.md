# **Použitie Microsoft Phi-3.5 tflite na vytvorenie Android aplikácie**

Toto je ukážka Android aplikácie využívajúcej modely Microsoft Phi-3.5 tflite.

## **📚 Znalosti**

Android LLM Inference API umožňuje spúšťať veľké jazykové modely (LLMs) priamo na zariadení pre Android aplikácie. Tieto modely môžete využiť na rôzne úlohy, ako je generovanie textu, získavanie informácií v prirodzenej jazykovej forme a sumarizácia dokumentov. Táto funkcionalita poskytuje zabudovanú podporu pre viacero text-to-text veľkých jazykových modelov, takže môžete do svojich Android aplikácií integrovať najnovšie generatívne AI modely na zariadení.

Googld AI Edge Torch je knižnica v jazyku Python, ktorá umožňuje konvertovať PyTorch modely do formátu .tflite. Tieto modely je možné následne spúšťať pomocou TensorFlow Lite a MediaPipe. Táto technológia umožňuje vytvárať aplikácie pre Android, iOS a IoT zariadenia, ktoré môžu modely spúšťať úplne na zariadení. AI Edge Torch poskytuje širokú podporu pre CPU, pričom zahŕňa aj počiatočnú podporu GPU a NPU. AI Edge Torch je úzko integrovaný s PyTorch, pričom stavia na funkcii torch.export() a ponúka dobré pokrytie základných ATen operátorov.

## **🪬 Pokyny**

### **🔥 Konverzia Microsoft Phi-3.5 na tflite podporu**

0. Táto ukážka je určená pre Android 14+

1. Nainštalujte Python 3.10.12

***Odporúčanie:*** Použite conda na inštaláciu vášho Python prostredia.

2. Ubuntu 20.04 / 22.04 (zamerajte sa na [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Odporúčanie:*** Použite Azure Linux VM alebo cloudové VM od tretích strán na vytvorenie vášho prostredia.

3. Otvorte Linux bash a nainštalujte Python knižnicu 

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Stiahnite si Microsoft-3.5-Instruct z Hugging Face


```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konvertujte Microsoft Phi-3.5 na tflite


```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```


### **🔥 Konverzia Microsoft Phi-3.5 na Android Mediapipe balík**

Najskôr nainštalujte mediapipe

```bash

pip install mediapipe

```

Spustite tento kód vo [vašom notebooku](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)



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


### **🔥 Použitie adb push na presun modelu do zariadenia Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Spustenie vášho Android kódu**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.sk.png)

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových prekladových služieb založených na umelej inteligencii. Hoci sa snažíme o presnosť, prosím, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny preklad vykonaný človekom. Nezodpovedáme za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.