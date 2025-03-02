# **Mengkuantisasi Keluarga Phi Menggunakan Generative AI extensions untuk onnxruntime**

## **Apa itu Generative AI extensions untuk onnxruntime**

Ekstensi ini membantu Anda menjalankan AI generatif dengan ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Ekstensi ini menyediakan loop AI generatif untuk model ONNX, termasuk inferensi dengan ONNX Runtime, pemrosesan logits, pencarian dan sampling, serta manajemen cache KV. Pengembang dapat memanggil metode tingkat tinggi generate(), atau menjalankan setiap iterasi model dalam sebuah loop, menghasilkan satu token pada satu waktu, dan secara opsional memperbarui parameter generasi di dalam loop. Ekstensi ini mendukung pencarian greedy/beam dan sampling TopP, TopK untuk menghasilkan urutan token serta pemrosesan logits bawaan seperti penalti pengulangan. Anda juga dapat dengan mudah menambahkan penilaian khusus.

Pada tingkat aplikasi, Anda dapat menggunakan Generative AI extensions untuk onnxruntime untuk membangun aplikasi menggunakan C++/C#/Python. Pada tingkat model, Anda dapat menggunakannya untuk menggabungkan model yang telah di-fine-tune dan melakukan pekerjaan implementasi kuantitatif terkait.

## **Mengkuantisasi Phi-3.5 dengan Generative AI extensions untuk onnxruntime**

### **Model yang Didukung**

Generative AI extensions untuk onnxruntime mendukung konversi kuantisasi untuk Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Model Builder dalam Generative AI extensions untuk onnxruntime**

Model builder mempercepat pembuatan model ONNX yang dioptimalkan dan dikuantisasi untuk dijalankan dengan API generate() ONNX Runtime.

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

1. **model_name** Ini adalah model di Hugging Face, seperti microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, dll. Ini juga bisa berupa path tempat Anda menyimpan model.

2. **path_to_output_folder** Jalur penyimpanan hasil konversi kuantisasi.

3. **execution_provider** Dukungan akselerasi perangkat keras yang berbeda, seperti cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Kami mengunduh model dari Hugging Face dan menyimpannya secara lokal.

***Catatan：***

## **Cara Menggunakan Model Builder untuk Mengkuantisasi Phi-3.5**

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

3. Silakan unduh file-file berikut ke folder Phi-3.5-vision-instruct Anda:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Unduh file berikut ke folder models:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Buka terminal

   Konversi ONNX dengan dukungan FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Catatan：**

1. Model Builder saat ini mendukung konversi Phi-3.5-Instruct dan Phi-3.5-Vision, tetapi tidak untuk Phi-3.5-MoE.

2. Untuk menggunakan model ONNX yang telah dikuantisasi, Anda dapat menggunakannya melalui Generative AI extensions untuk onnxruntime SDK.

3. Kita perlu mempertimbangkan AI yang lebih bertanggung jawab, jadi setelah konversi kuantisasi model, disarankan untuk melakukan pengujian hasil yang lebih efektif.

4. Dengan mengkuantisasi model CPU INT4, kita dapat menerapkannya pada Perangkat Edge, yang memiliki skenario aplikasi yang lebih baik. Oleh karena itu, kami telah menyelesaikan Phi-3.5-Instruct untuk INT 4.

## **Sumber Daya**

1. Pelajari lebih lanjut tentang Generative AI extensions untuk onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions untuk onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.