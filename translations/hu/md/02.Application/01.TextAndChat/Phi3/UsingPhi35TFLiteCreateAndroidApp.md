# **Microsoft Phi-3.5 tflite használata Android alkalmazás létrehozásához**

Ez egy Android példa, amely Microsoft Phi-3.5 tflite modelleket használ.

## **📚 Tudnivalók**

Az Android LLM Inference API lehetővé teszi, hogy nagy nyelvi modelleket (LLM-eket) futtassunk teljes mértékben eszközön belül Android alkalmazásokhoz. Ezáltal számos feladatot végezhetünk el, például szöveg generálását, információk természetes nyelvi formában történő lekérdezését és dokumentumok összegzését. Az API beépített támogatást nyújt több szöveg-szöveg típusú nagy nyelvi modellhez, így a legújabb generatív mesterséges intelligencia modelleket alkalmazhatjuk Android alkalmazásainkban.

A Google AI Edge Torch egy Python könyvtár, amely támogatja a PyTorch modellek .tflite formátumba való konvertálását, amelyeket ezután TensorFlow Lite-tal és MediaPipe-pal futtathatunk. Ez lehetővé teszi, hogy Android, iOS és IoT alkalmazások teljesen eszközön belül futtathassák a modelleket. Az AI Edge Torch széles körű CPU támogatást kínál, kezdeti GPU és NPU támogatással. Az AI Edge Torch szorosan integrálódik a PyTorch-sal, a torch.export() funkcióra építve, és jó lefedettséget biztosít a Core ATen operátorok számára.

## **🪬 Útmutató**

### **🔥 Microsoft Phi-3.5 tflite támogatássá alakítása**

0. Ez a minta Android 14+ verzióhoz készült.

1. Telepítsd a Python 3.10.12 verziót.

***Javaslat:*** Használj conda-t a Python környezeted telepítéséhez.

2. Ubuntu 20.04 / 22.04 (kérlek, koncentrálj a [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) projektre).

***Javaslat:*** Használj Azure Linux VM-et vagy harmadik fél által biztosított felhő VM-et a környezeted létrehozásához.

3. Lépj be a Linux bash-be, és telepítsd a Python könyvtárakat:

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Töltsd le a Microsoft-3.5-Instruct modellt a Hugging Face-ről:

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Alakítsd át a Microsoft Phi-3.5 modellt tflite formátumba:

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 átalakítása Android Mediapipe csomaggá**

Először telepítsd a MediaPipe-ot:

```bash

pip install mediapipe

```

Futtasd ezt a kódot a [jegyzetfüzetedben](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb):

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

### **🔥 A modell átmásolása adb push segítségével az Android eszközöd elérési útjára**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Az Android kód futtatása**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.hu.png)

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítási szolgáltatások segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekinthető hiteles forrásnak. Fontos információk esetén javasoljuk a professzionális, emberi fordítást. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.