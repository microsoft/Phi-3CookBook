# **Inference Phi-3 dengan Kerangka Kerja Apple MLX**

## **Apa itu Kerangka Kerja MLX**

MLX adalah kerangka kerja array untuk penelitian pembelajaran mesin di perangkat Apple silicon, dikembangkan oleh tim penelitian pembelajaran mesin Apple.

MLX dirancang oleh peneliti pembelajaran mesin untuk peneliti pembelajaran mesin. Kerangka kerja ini dibuat agar mudah digunakan, namun tetap efisien untuk melatih dan menerapkan model. Desain kerangka kerja ini juga secara konseptual sederhana. Kami bertujuan untuk mempermudah peneliti dalam memperluas dan meningkatkan MLX, dengan tujuan mengeksplorasi ide-ide baru dengan cepat.

LLM dapat dipercepat pada perangkat Apple Silicon melalui MLX, dan model dapat dijalankan secara lokal dengan sangat mudah.

## **Menggunakan MLX untuk inferensi Phi-3-mini**

### **1. Siapkan lingkungan MLX Anda**

1. Python 3.11.x  
2. Instal Library MLX  

```bash

pip install mlx-lm

```

### **2. Menjalankan Phi-3-mini di Terminal dengan MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Hasilnya (lingkungan saya adalah Apple M1 Max, 64GB) adalah

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.id.png)

### **3. Mengkuantisasi Phi-3-mini dengan MLX di Terminal**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Catatan:*** Model dapat dikuantisasi melalui mlx_lm.convert, dan kuantisasi default adalah INT4. Contoh ini mengkuantisasi Phi-3-mini ke INT4.

Model dapat dikuantisasi melalui mlx_lm.convert, dan kuantisasi default adalah INT4. Contoh ini adalah untuk mengkuantisasi Phi-3-mini menjadi INT4. Setelah dikuantisasi, model akan disimpan di direktori default ./mlx_model.

Kita dapat menguji model yang telah dikuantisasi dengan MLX melalui terminal.

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Hasilnya adalah

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.id.png)

### **4. Menjalankan Phi-3-mini dengan MLX di Jupyter Notebook**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.id.png)

***Catatan:*** Silakan baca contoh ini [klik tautan ini](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Sumber Daya**

1. Pelajari tentang Kerangka Kerja Apple MLX [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Repositori GitHub Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI berbasis mesin. Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.