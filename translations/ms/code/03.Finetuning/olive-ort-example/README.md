# Fine-tune Phi3 menggunakan Olive

Dalam contoh ini, anda akan menggunakan Olive untuk:

1. Melatih semula LoRA adapter untuk mengklasifikasikan frasa kepada Sad, Joy, Fear, Surprise.
1. Menggabungkan berat adapter ke dalam model asas.
1. Mengoptimumkan dan Kuantisasi model menjadi `int4`.

Kami juga akan menunjukkan kepada anda cara untuk melakukan inferens pada model yang telah dilatih semula menggunakan ONNX Runtime (ORT) Generate API.

> **⚠️ Untuk melatih semula, anda perlu mempunyai GPU yang sesuai - sebagai contoh, A10, V100, A100.**

## 💾 Pasang

Cipta persekitaran maya Python baharu (contohnya, menggunakan `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Seterusnya, pasang Olive dan keperluan untuk aliran kerja melatih semula:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Latih semula Phi3 menggunakan Olive
[Fail konfigurasi Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) mengandungi *workflow* dengan *passes* berikut:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Secara ringkas, aliran kerja ini akan:

1. Melatih semula Phi3 (selama 150 langkah, yang boleh anda ubah) menggunakan data [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Menggabungkan berat LoRA adapter ke dalam model asas. Ini akan menghasilkan satu artifak model dalam format ONNX.
1. Model Builder akan mengoptimumkan model untuk ONNX runtime *dan* mengkuantisasi model menjadi `int4`.

Untuk melaksanakan aliran kerja, jalankan:

```bash
olive run --config phrase-classification.json
```

Apabila Olive selesai, model Phi3 yang telah dilatih semula dan dioptimumkan `int4` anda tersedia di: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrasikan Phi3 yang telah dilatih semula ke dalam aplikasi anda 

Untuk menjalankan aplikasi:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Respons ini sepatutnya merupakan satu perkataan klasifikasi bagi frasa tersebut (Sad/Joy/Fear/Surprise).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.