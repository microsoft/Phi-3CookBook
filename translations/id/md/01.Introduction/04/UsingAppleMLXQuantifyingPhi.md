# **Mengkuantisasi Phi-3.5 menggunakan Apple MLX Framework**

MLX adalah kerangka array untuk penelitian pembelajaran mesin pada Apple silicon, yang dikembangkan oleh tim penelitian pembelajaran mesin Apple.

MLX dirancang oleh peneliti pembelajaran mesin untuk peneliti pembelajaran mesin. Kerangka ini bertujuan untuk ramah pengguna, namun tetap efisien dalam melatih dan menerapkan model. Desain kerangka ini juga secara konseptual sederhana. Kami bertujuan untuk mempermudah para peneliti dalam memperluas dan meningkatkan MLX dengan tujuan menjelajahi ide-ide baru dengan cepat.

LLM dapat dipercepat pada perangkat Apple Silicon melalui MLX, dan model dapat dijalankan secara lokal dengan sangat nyaman.

Sekarang Apple MLX Framework mendukung konversi kuantisasi untuk Phi-3.5-Instruct(**Dukungan Apple MLX Framework**), Phi-3.5-Vision(**Dukungan MLX-VLM Framework**), dan Phi-3.5-MoE(**Dukungan Apple MLX Framework**). Mari kita coba selanjutnya:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Contoh untuk Phi-3.5 dengan Apple MLX**

| Labs    | Perkenalan | Pergi |
| -------- | ------- |  ------- |
| 🚀 Lab-Perkenalan Phi-3.5 Instruct  | Pelajari cara menggunakan Phi-3.5 Instruct dengan kerangka kerja Apple MLX   |  [Pergi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Perkenalan Phi-3.5 Vision (gambar) | Pelajari cara menggunakan Phi-3.5 Vision untuk menganalisis gambar dengan kerangka kerja Apple MLX     |  [Pergi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Perkenalan Phi-3.5 Vision (moE)   | Pelajari cara menggunakan Phi-3.5 MoE dengan kerangka kerja Apple MLX  |  [Pergi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Sumber Daya**

1. Pelajari tentang Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repositori GitHub Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repositori GitHub MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan berbasis AI. Meskipun kami berupaya untuk memberikan hasil yang akurat, harap disadari bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat krusial, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.