# **Paggamit ng Microsoft Phi-3.5 tflite para gumawa ng Android app**

Ito ay isang Android sample na gumagamit ng Microsoft Phi-3.5 tflite models.

## **📚 Kaalaman**

Ang Android LLM Inference API ay nagbibigay-daan sa iyo na patakbuhin ang malalaking language models (LLMs) nang buo sa iyong Android device para sa mga aplikasyon, na magagamit mo upang magsagawa ng iba't ibang gawain tulad ng pagbuo ng teksto, pagkuha ng impormasyon sa natural na anyo ng wika, at pagbubuod ng mga dokumento. Ang task na ito ay may built-in na suporta para sa maraming text-to-text large language models, kaya maaari mong gamitin ang pinakabagong on-device generative AI models para sa iyong Android apps.

Ang Google AI Edge Torch ay isang python library na sumusuporta sa pag-convert ng mga PyTorch models sa .tflite na format, na maaaring patakbuhin gamit ang TensorFlow Lite at MediaPipe. Pinapayagan nito ang mga aplikasyon para sa Android, iOS, at IoT na maaaring magpatakbo ng mga modelo nang buo sa device. Ang AI Edge Torch ay nag-aalok ng malawak na coverage para sa CPU, at may paunang suporta para sa GPU at NPU. Ang AI Edge Torch ay naglalayong maging malapit na naka-integrate sa PyTorch, gamit ang torch.export() at nagbibigay ng magandang coverage ng Core ATen operators.

## **🪬 Gabay**

### **🔥 I-convert ang Microsoft Phi-3.5 sa tflite support**

0. Ang sample na ito ay para sa Android 14+

1. Mag-install ng Python 3.10.12

***Mungkahi:*** Gumamit ng conda para i-install ang iyong Python environment

2. Ubuntu 20.04 / 22.04 (mangyaring magtuon sa [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Mungkahi:*** Gumamit ng Azure Linux VM o 3rd party cloud VM para gawin ang iyong environment

3. Pumunta sa iyong Linux bash, at mag-install ng Python library

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. I-download ang Microsoft-3.5-Instruct mula sa Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. I-convert ang Microsoft Phi-3.5 sa tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 I-convert ang Microsoft Phi-3.5 sa Android Mediapipe Bundle**

Mangyaring i-install muna ang MediaPipe

```bash

pip install mediapipe

```

Patakbuhin ang code na ito sa [iyong notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Gamitin ang adb push task model sa path ng iyong Android device**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Patakbuhin ang iyong Android code**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.tl.png)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyong AI na batay sa makina. Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagiging wasto. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling ginawa ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.