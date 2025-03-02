# **Microsoft Phi-3.5 tflite-ийг ашиглан Android апп үүсгэх**

Энэ бол Microsoft Phi-3.5 tflite загваруудыг ашигласан Android-ийн жишээ юм.

## **📚 Мэдлэг**

Android LLM Inference API нь Android аппликейшнуудад зориулан том хэмжээний хэлний загваруудыг (LLM) бүрэн төхөөрөмж дээр ажиллуулах боломжийг олгодог. Үүнийг ашиглан текст үүсгэх, байгалийн хэлээр мэдээлэл авах, баримт бичгийг хураангуйлах гэх мэт олон төрлийн даалгавруудыг гүйцэтгэж болно. Энэ даалгавар нь олон төрлийн текстээс текст рүү чиглэсэн том хэлний загваруудыг дэмждэг тул хамгийн сүүлийн үеийн төхөөрөмж дээрх generative AI загваруудыг таны Android апп-д ашиглах боломжтой.

Google AI Edge Torch нь PyTorch загваруудыг .tflite формат руу хөрвүүлэхийг дэмждэг python сан бөгөөд үүнийг TensorFlow Lite болон MediaPipe ашиглан ажиллуулах боломжтой. Энэ нь Android, iOS болон IoT төхөөрөмжүүдэд загваруудыг бүрэн төхөөрөмж дээр ажиллуулах боломжийг олгодог. AI Edge Torch нь CPU-гийн өргөн хүрээг хамардаг бөгөөд GPU болон NPU-ийн эхний шатны дэмжлэгтэй. AI Edge Torch нь PyTorch-тэй нягт уялдаж, torch.export() дээр суурилан Core ATen операторуудыг өргөн хамрахыг зорьдог.

## **🪬 Заавар**

### **🔥 Microsoft Phi-3.5-ийг tflite руу хөрвүүлэх**

0. Энэ жишээ нь зөвхөн Android 14+ хувилбарт зориулагдсан.

1. Python 3.10.12-ийг суулгах.

***Санал болгох:*** Python орчноо conda ашиглан суулгаарай.

2. Ubuntu 20.04 / 22.04 (анхаарлаа [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) дээр төвлөрүүлнэ үү)

***Санал болгох:*** Azure Linux VM эсвэл гуравдагч этгээдийн үүлэн VM ашиглан орчноо үүсгээрэй.

3. Linux bash дээрээ очоод Python сан суулгаарай.

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging Face-ээс Microsoft-3.5-Instruct-ийг татаж ав.

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5-ийг tflite руу хөрвүүлнэ.

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5-ийг Android Mediapipe багц руу хөрвүүлэх**

Эхлээд mediapipe-ийг суулгаарай.

```bash

pip install mediapipe

```

[Тэмдэглэлийн дэвтэртээ](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) дараах кодыг ажиллуулаарай.

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

### **🔥 Загварын файлыг adb push ашиглан Android төхөөрөмжийн замд байршуулах**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Android кодоо ажиллуулах**

![демо](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.mo.png)

It seems like "mo" could refer to a language or abbreviation, but it's not entirely clear which one you mean. Could you clarify whether "mo" refers to a specific language (e.g., Maori, Montenegrin, or something else)? If so, I'd be happy to assist with the translation!