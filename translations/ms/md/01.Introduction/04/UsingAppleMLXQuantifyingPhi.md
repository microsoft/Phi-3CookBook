# **Mengkuantisasi Phi-3.5 menggunakan Kerangka Apple MLX**

MLX adalah kerangka array untuk penelitian pembelajaran mesin di Apple silicon, yang dikembangkan oleh tim penelitian pembelajaran mesin Apple.

MLX dirancang oleh peneliti pembelajaran mesin untuk peneliti pembelajaran mesin. Kerangka ini dimaksudkan untuk ramah pengguna, namun tetap efisien untuk melatih dan menjalankan model. Desain kerangka ini juga secara konseptual sederhana. Kami bertujuan untuk mempermudah peneliti dalam memperluas dan meningkatkan MLX dengan tujuan menjelajahi ide-ide baru dengan cepat.

LLM dapat dipercepat di perangkat Apple Silicon melalui MLX, dan model dapat dijalankan secara lokal dengan sangat nyaman.

Kini Kerangka Apple MLX mendukung konversi kuantisasi untuk Phi-3.5-Instruct(**Dukungan Kerangka Apple MLX**), Phi-3.5-Vision(**Dukungan Kerangka MLX-VLM**), dan Phi-3.5-MoE(**Dukungan Kerangka Apple MLX**). Mari kita coba berikut ini:

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

| Labs    | Pengenalan | Pergi |
| -------- | ------- |  ------- |
| 🚀 Lab-Pengenalan Phi-3.5 Instruct  | Pelajari cara menggunakan Phi-3.5 Instruct dengan kerangka Apple MLX   |  [Pergi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Pengenalan Phi-3.5 Vision (gambar) | Pelajari cara menggunakan Phi-3.5 Vision untuk menganalisis gambar dengan kerangka Apple MLX     |  [Pergi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Pengenalan Phi-3.5 Vision (moE)   | Pelajari cara menggunakan Phi-3.5 MoE dengan kerangka Apple MLX  |  [Pergi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Sumber Daya**

1. Pelajari tentang Kerangka Apple MLX [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repositori GitHub Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repositori GitHub MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.