# **Mengkuantisasi Keluarga Phi menggunakan ekstensi Generative AI untuk onnxruntime**

## **Apa itu ekstensi Generative AI untuk onnxruntime**

Ekstensi ini membantu Anda menjalankan Generative AI dengan ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Ekstensi ini menyediakan loop Generative AI untuk model ONNX, termasuk inferensi dengan ONNX Runtime, pemrosesan logits, pencarian dan sampling, serta manajemen cache KV. Pengembang dapat memanggil metode tingkat tinggi generate(), atau menjalankan setiap iterasi model dalam loop, menghasilkan satu token pada satu waktu, dan secara opsional memperbarui parameter generasi di dalam loop. Ekstensi ini mendukung pencarian greedy/beam dan sampling TopP, TopK untuk menghasilkan urutan token, serta pemrosesan logits bawaan seperti penalti pengulangan. Anda juga dapat dengan mudah menambahkan penilaian khusus.

Pada level aplikasi, Anda dapat menggunakan ekstensi Generative AI untuk onnxruntime untuk membangun aplikasi menggunakan C++/C#/Python. Pada level model, Anda dapat menggunakannya untuk menggabungkan model yang telah di-fine-tune dan melakukan pekerjaan deployment kuantitatif terkait.

## **Mengkuantisasi Phi-3.5 dengan ekstensi Generative AI untuk onnxruntime**

### **Model yang Didukung**

Ekstensi Generative AI untuk onnxruntime mendukung konversi kuantisasi untuk Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Model Builder dalam ekstensi Generative AI untuk onnxruntime**

Model Builder secara signifikan mempercepat pembuatan model ONNX yang dioptimalkan dan dikuantisasi yang dapat berjalan dengan API generate() ONNX Runtime.

Melalui Model Builder, Anda dapat mengkuantisasi model ke INT4, INT8, FP16, FP32, dan menggabungkan berbagai metode akselerasi perangkat keras seperti CPU, CUDA, DirectML, Mobile, dll.

Untuk menggunakan Model Builder, Anda perlu menginstal

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Setelah instalasi, Anda dapat menjalankan skrip Model Builder dari terminal untuk melakukan konversi format model dan kuantisasi.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Pahami parameter yang relevan:

1. **model_name** Ini adalah model di Hugging Face, seperti microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, dll. Bisa juga merupakan jalur tempat Anda menyimpan model.

2. **path_to_output_folder** Jalur penyimpanan hasil konversi kuantisasi.

3. **execution_provider** Dukungan akselerasi perangkat keras yang berbeda, seperti CPU, CUDA, DirectML.

4. **cache_dir_to_save_hf_files** Kami mengunduh model dari Hugging Face dan menyimpannya secara lokal.

***Catatan:***

## **Cara menggunakan Model Builder untuk mengkuantisasi Phi-3.5**

Model Builder kini mendukung kuantisasi model ONNX untuk Phi-3.5 Instruct dan Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Konversi INT 4 yang dipercepat CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Konversi INT 4 yang dipercepat CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Atur lingkungan di terminal

```bash

mkdir models

cd models 

```

2. Unduh microsoft/Phi-3.5-vision-instruct ke folder models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Silakan unduh file berikut ke folder Phi-3.5-vision-instruct Anda

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Unduh file ini ke folder models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Buka terminal

   Konversi ONNX dengan dukungan FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Catatan:**

1. Model Builder saat ini mendukung konversi Phi-3.5-Instruct dan Phi-3.5-Vision, tetapi belum mendukung Phi-3.5-MoE.

2. Untuk menggunakan model ONNX yang dikuantisasi, Anda dapat menggunakannya melalui SDK ekstensi Generative AI untuk onnxruntime.

3. Kita perlu mempertimbangkan AI yang lebih bertanggung jawab, jadi setelah konversi kuantisasi model, disarankan untuk melakukan pengujian hasil yang lebih efektif.

4. Dengan mengkuantisasi model CPU INT4, kita dapat mendistribusikannya ke Edge Device, yang memiliki skenario aplikasi yang lebih baik. Oleh karena itu, kami telah menyelesaikan Phi-3.5-Instruct dalam format INT4.

## **Sumber Daya**

1. Pelajari lebih lanjut tentang ekstensi Generative AI untuk onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repositori GitHub ekstensi Generative AI untuk onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan berbasis AI. Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat krusial, disarankan untuk menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.