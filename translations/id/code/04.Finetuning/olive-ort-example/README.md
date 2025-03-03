# Fine-tune Phi3 menggunakan Olive

Dalam contoh ini, Anda akan menggunakan Olive untuk:

1. Melakukan fine-tuning adapter LoRA untuk mengklasifikasikan frasa menjadi Sad, Joy, Fear, Surprise.
1. Menggabungkan bobot adapter ke dalam model dasar.
1. Mengoptimalkan dan Mengkuantisasi model menjadi `int4`.

Kami juga akan menunjukkan kepada Anda cara melakukan inferensi pada model yang telah di-fine-tune menggunakan ONNX Runtime (ORT) Generate API.

> **⚠️ Untuk Fine-tuning, Anda perlu memiliki GPU yang sesuai - misalnya, A10, V100, A100.**

## 💾 Instalasi

Buat lingkungan virtual Python baru (misalnya, menggunakan `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Selanjutnya, instal Olive dan dependensi untuk alur kerja fine-tuning:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 menggunakan Olive
[File konfigurasi Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) berisi sebuah *workflow* dengan *passes* berikut:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Secara garis besar, alur kerja ini akan:

1. Melakukan fine-tuning Phi3 (selama 150 langkah, yang dapat Anda ubah) menggunakan data [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Menggabungkan bobot adapter LoRA ke dalam model dasar. Ini akan menghasilkan satu artefak model dalam format ONNX.
1. Model Builder akan mengoptimalkan model untuk runtime ONNX *dan* mengkuantisasi model menjadi `int4`.

Untuk menjalankan alur kerja ini, eksekusi:

```bash
olive run --config phrase-classification.json
```

Setelah Olive selesai, model Phi3 yang telah di-fine-tune dan dioptimalkan menjadi `int4` tersedia di: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrasikan Phi3 yang telah di-fine-tune ke dalam aplikasi Anda 

Untuk menjalankan aplikasi:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Respon ini seharusnya berupa satu kata yang mengklasifikasikan frasa (Sad/Joy/Fear/Surprise).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berusaha untuk memberikan terjemahan yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.