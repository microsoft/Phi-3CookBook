# Fine-tune Phi3 menggunakan Olive

Dalam contoh ini, Anda akan menggunakan Olive untuk:

1. Melakukan fine-tune adapter LoRA untuk mengklasifikasikan frasa menjadi Sad, Joy, Fear, Surprise.
2. Menggabungkan bobot adapter ke dalam model dasar.
3. Mengoptimalkan dan mengkuantisasi model menjadi `int4`.

Kami juga akan menunjukkan cara melakukan inferensi pada model yang telah di-fine-tune menggunakan API Generate dari ONNX Runtime (ORT).

> **⚠️ Untuk Fine-tuning, Anda perlu memiliki GPU yang sesuai - misalnya, A10, V100, A100.**

## 💾 Instalasi

Buat lingkungan virtual Python baru (misalnya, menggunakan `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Selanjutnya, instal Olive dan dependensi untuk workflow fine-tuning:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 menggunakan Olive
[File konfigurasi Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) berisi sebuah *workflow* dengan *passes* berikut:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Secara garis besar, workflow ini akan:

1. Melakukan fine-tune pada Phi3 (selama 150 langkah, yang dapat Anda ubah) menggunakan data dari [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
2. Menggabungkan bobot adapter LoRA ke dalam model dasar. Ini akan menghasilkan satu artefak model dalam format ONNX.
3. Model Builder akan mengoptimalkan model untuk runtime ONNX *dan* mengkuantisasi model menjadi `int4`.

Untuk menjalankan workflow, jalankan:

```bash
olive run --config phrase-classification.json
```

Setelah Olive selesai, model Phi3 yang telah di-fine-tune dan dioptimalkan dalam format `int4` tersedia di: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrasikan Phi3 yang telah di-fine-tune ke dalam aplikasi Anda 

Untuk menjalankan aplikasi:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Respons ini seharusnya berupa klasifikasi satu kata dari frasa (Sad/Joy/Fear/Surprise).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan untuk menggunakan layanan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.