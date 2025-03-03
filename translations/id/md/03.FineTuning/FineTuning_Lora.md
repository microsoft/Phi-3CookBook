# **Fine-tuning Phi-3 dengan Lora**

Melakukan fine-tuning model bahasa Phi-3 Mini dari Microsoft menggunakan [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) pada dataset instruksi obrolan khusus.

LORA akan membantu meningkatkan pemahaman percakapan dan pembuatan respons.

## Panduan langkah demi langkah untuk melakukan fine-tuning Phi-3 Mini:

**Impor dan Pengaturan**

Menginstal loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Mulailah dengan mengimpor pustaka-pustaka yang diperlukan seperti datasets, transformers, peft, trl, dan torch. Atur logging untuk melacak proses pelatihan.

Anda dapat memilih untuk menyesuaikan beberapa layer dengan menggantinya menggunakan versi yang diimplementasikan dalam loralib. Saat ini kami hanya mendukung nn.Linear, nn.Embedding, dan nn.Conv2d. Kami juga mendukung MergedLinear untuk kasus di mana satu nn.Linear mewakili lebih dari satu layer, seperti dalam beberapa implementasi proyeksi perhatian qkv (lihat Catatan Tambahan untuk lebih lanjut).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Sebelum loop pelatihan dimulai, tandai hanya parameter LoRA sebagai parameter yang dapat dilatih.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Saat menyimpan checkpoint, buat state_dict yang hanya berisi parameter LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Saat memuat checkpoint menggunakan load_state_dict, pastikan untuk mengatur strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Sekarang pelatihan dapat berjalan seperti biasa.

**Hyperparameter**

Tentukan dua dictionary: training_config dan peft_config. training_config mencakup hyperparameter untuk pelatihan, seperti learning rate, ukuran batch, dan pengaturan logging.

peft_config menentukan parameter terkait LoRA seperti rank, dropout, dan jenis tugas.

**Memuat Model dan Tokenizer**

Tentukan path ke model Phi-3 yang telah dilatih sebelumnya (misalnya, "microsoft/Phi-3-mini-4k-instruct"). Konfigurasikan pengaturan model, termasuk penggunaan cache, tipe data (bfloat16 untuk presisi campuran), dan implementasi perhatian.

**Pelatihan**

Lakukan fine-tuning model Phi-3 menggunakan dataset instruksi obrolan khusus. Gunakan pengaturan LoRA dari peft_config untuk adaptasi yang efisien. Pantau kemajuan pelatihan menggunakan strategi logging yang telah ditentukan.
Evaluasi dan Penyimpanan: Evaluasi model yang telah di-fine-tune.
Simpan checkpoint selama pelatihan untuk digunakan nanti.

**Contoh**
- [Pelajari Lebih Lanjut dengan notebook contoh ini](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Contoh Python FineTuning](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Contoh Fine Tuning Hugging Face Hub dengan LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Contoh Model Card Hugging Face - LORA Fine Tuning](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Contoh Fine Tuning Hugging Face Hub dengan QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.