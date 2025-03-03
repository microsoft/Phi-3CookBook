# **Uporaba Microsoft Phi-3.5 tflite za ustvarjanje Android aplikacije**

To je Android primer, ki uporablja Microsoft Phi-3.5 tflite modele.

## **📚 Znanje**

Android LLM Inference API omogoča izvajanje velikih jezikovnih modelov (LLM) neposredno na napravi za Android aplikacije. To lahko uporabite za izvajanje različnih nalog, kot so generiranje besedila, pridobivanje informacij v naravnem jeziku in povzemanje dokumentov. API ponuja vgrajeno podporo za večje jezikovne modele tipa besedilo-v-besedilo, kar omogoča uporabo najnovejših generativnih AI modelov na Android aplikacijah.

Googld AI Edge Torch je Python knjižnica, ki podpira pretvorbo PyTorch modelov v .tflite format, ki ga je nato mogoče izvajati s TensorFlow Lite in MediaPipe. To omogoča aplikacije za Android, iOS in IoT, ki lahko modele izvajajo povsem na napravi. AI Edge Torch ponuja široko podporo za CPU, z začetno podporo za GPU in NPU. AI Edge Torch si prizadeva za tesno integracijo s PyTorch, saj temelji na torch.export() in zagotavlja dobro pokritost Core ATen operaterjev.

## **🪬 Smernice**

### **🔥 Pretvorba Microsoft Phi-3.5 v tflite**

0. Ta primer je za Android 14+

1. Namestite Python 3.10.12

***Predlog:*** uporabite conda za namestitev Python okolja

2. Ubuntu 20.04 / 22.04 (osredotočite se na [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Predlog:*** uporabite Azure Linux VM ali VM tretjih ponudnikov za ustvarjanje okolja

3. V Linux bash-u namestite Python knjižnico 

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Prenesite Microsoft-3.5-Instruct iz Hugging face


```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Pretvorite Microsoft Phi-3.5 v tflite


```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```


### **🔥 Pretvorba Microsoft Phi-3.5 v Android Mediapipe Bundle**

Najprej namestite mediapipe

```bash

pip install mediapipe

```

Zaženite ta koda v [vašem zvezku](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)



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


### **🔥 Uporaba adb push za nalaganje modela na Android napravo**


```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Zagon vaše Android kode**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.sl.png)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, prosimo, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj velja za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.