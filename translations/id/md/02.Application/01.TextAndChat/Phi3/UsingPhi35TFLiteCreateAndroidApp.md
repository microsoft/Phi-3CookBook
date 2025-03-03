# **Menggunakan Microsoft Phi-3.5 tflite untuk Membuat Aplikasi Android**

Ini adalah contoh aplikasi Android yang menggunakan model Microsoft Phi-3.5 tflite.

## **📚 Pengetahuan**

Android LLM Inference API memungkinkan Anda menjalankan model bahasa besar (LLM) sepenuhnya di perangkat untuk aplikasi Android. Anda dapat menggunakannya untuk melakukan berbagai tugas, seperti menghasilkan teks, mengambil informasi dalam bentuk bahasa alami, dan merangkum dokumen. API ini menyediakan dukungan bawaan untuk beberapa model bahasa besar teks-ke-teks, sehingga Anda dapat menerapkan model AI generatif terbaru di perangkat ke dalam aplikasi Android Anda.

Google AI Edge Torch adalah pustaka Python yang mendukung konversi model PyTorch menjadi format .tflite, yang kemudian dapat dijalankan dengan TensorFlow Lite dan MediaPipe. Ini memungkinkan aplikasi untuk Android, iOS, dan IoT menjalankan model sepenuhnya di perangkat. AI Edge Torch menawarkan cakupan CPU yang luas, dengan dukungan awal untuk GPU dan NPU. AI Edge Torch berupaya untuk terintegrasi erat dengan PyTorch, membangun di atas torch.export(), dan menyediakan cakupan yang baik untuk operator Core ATen.

## **🪬 Panduan**

### **🔥 Mengonversi Microsoft Phi-3.5 ke format tflite**

0. Contoh ini hanya untuk Android 14+

1. Instal Python 3.10.12

***Saran:*** gunakan conda untuk menginstal lingkungan Python Anda

2. Ubuntu 20.04 / 22.04 (fokus pada [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Saran:*** Gunakan Azure Linux VM atau VM cloud pihak ketiga untuk membuat lingkungan Anda

3. Masuk ke bash Linux Anda, lalu instal pustaka Python 

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Unduh Microsoft-3.5-Instruct dari Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konversi Microsoft Phi-3.5 ke format tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Mengonversi Microsoft Phi-3.5 ke Android Mediapipe Bundle**

Instal terlebih dahulu mediapipe

```bash

pip install mediapipe

```

Jalankan kode ini di [notebook Anda](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Menggunakan adb push untuk memindahkan model ke path perangkat Android Anda**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Menjalankan kode Android Anda**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.id.png)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berusaha untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.