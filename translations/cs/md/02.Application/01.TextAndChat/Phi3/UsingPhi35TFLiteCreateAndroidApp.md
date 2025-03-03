# **Použití Microsoft Phi-3.5 tflite k vytvoření Android aplikace**

Toto je ukázka Android aplikace využívající modely Microsoft Phi-3.5 tflite.

## **📚 Znalosti**

Android LLM Inference API umožňuje spouštět velké jazykové modely (LLMs) přímo na zařízení pro Android aplikace. Tyto modely lze využít k široké škále úloh, jako je generování textu, získávání informací v přirozeném jazyce nebo shrnutí dokumentů. API nabízí vestavěnou podporu pro více text-to-text velkých jazykových modelů, což umožňuje využít nejnovější generativní AI modely přímo na Android aplikacích.

Google AI Edge Torch je python knihovna, která podporuje převod PyTorch modelů do formátu .tflite, který lze následně spustit pomocí TensorFlow Lite a MediaPipe. Tím se otevírají možnosti pro aplikace na Android, iOS a IoT, které mohou modely spouštět kompletně na zařízení. AI Edge Torch poskytuje širokou podporu pro CPU, s počáteční podporou GPU a NPU. AI Edge Torch se snaží úzce integrovat s PyTorch, staví na funkci torch.export() a nabízí dobrou podporu pro Core ATen operátory.

## **🪬 Návod**

### **🔥 Převod Microsoft Phi-3.5 na tflite**

0. Tento příklad je určen pro Android 14+

1. Nainstalujte Python 3.10.12

***Doporučení:*** Použijte conda k instalaci Python prostředí.

2. Ubuntu 20.04 / 22.04 (zaměřte se na [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Doporučení:*** Použijte Azure Linux VM nebo cloudové VM od třetích stran k vytvoření vašeho prostředí.

3. Otevřete Linux bash a nainstalujte Python knihovny.

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Stáhněte Microsoft-3.5-Instruct z Hugging Face.

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Převeďte Microsoft Phi-3.5 na tflite.

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Převod Microsoft Phi-3.5 na Android Mediapipe Bundle**

Nejprve nainstalujte mediapipe.

```bash

pip install mediapipe

```

Spusťte tento kód ve [vašem notebooku](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb).

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

### **🔥 Použití adb push pro nahrání modelu na Android zařízení**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Spuštění vašeho Android kódu**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.cs.png)

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových překladových služeb založených na umělé inteligenci. Ačkoli se snažíme o přesnost, vezměte prosím na vědomí, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.