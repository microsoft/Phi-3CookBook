# Melarasikan Phi3 menggunakan Olive

Dalam contoh ini, anda akan menggunakan Olive untuk:

1. Melaras adapter LoRA untuk mengklasifikasikan frasa kepada Sad, Joy, Fear, Surprise.
1. Menggabungkan berat adapter ke dalam model asas.
1. Mengoptimumkan dan Mengkuantumkan model ke dalam `int4`.

Kami juga akan menunjukkan kepada anda cara untuk membuat inferens model yang telah dilaras menggunakan API Generate ONNX Runtime (ORT).

> **⚠️ Untuk Melaras, anda perlu mempunyai GPU yang sesuai - contohnya, A10, V100, A100.**

## 💾 Pemasangan

Cipta persekitaran maya Python baru (contohnya, menggunakan `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Seterusnya, pasang Olive dan kebergantungan untuk aliran kerja melaras:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Melaras Phi3 menggunakan Olive
[Fail konfigurasi Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) mengandungi *aliran kerja* dengan *laluan* berikut:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Secara ringkas, aliran kerja ini akan:

1. Melaras Phi3 (untuk 150 langkah, yang boleh anda ubah) menggunakan data dari [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Menggabungkan berat adapter LoRA ke dalam model asas. Ini akan menghasilkan satu artifak model dalam format ONNX.
1. Model Builder akan mengoptimumkan model untuk runtime ONNX *dan* mengkuantumkan model ke dalam `int4`.

Untuk melaksanakan aliran kerja, jalankan:

```bash
olive run --config phrase-classification.json
```

Apabila Olive selesai, model Phi3 yang telah dilaras dan dioptimumkan `int4` anda tersedia di: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Mengintegrasikan Phi3 yang telah dilaras ke dalam aplikasi anda 

Untuk menjalankan aplikasi:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Respons ini sepatutnya adalah satu klasifikasi perkataan bagi frasa (Sad/Joy/Fear/Surprise).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.