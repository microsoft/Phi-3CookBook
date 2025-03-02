# **Menyesuaikan Phi-3 dengan LoRA**

Menyesuaikan model bahasa Phi-3 Mini dari Microsoft menggunakan [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) pada dataset instruksi percakapan kustom.

LoRA akan membantu meningkatkan pemahaman percakapan dan kemampuan menghasilkan respons.

## Panduan langkah demi langkah untuk menyesuaikan Phi-3 Mini:

**Impor dan Pengaturan**

Menginstal loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Mulailah dengan mengimpor pustaka-pustaka yang diperlukan seperti datasets, transformers, peft, trl, dan torch. 
Atur logging untuk melacak proses pelatihan.

Anda dapat memilih untuk menyesuaikan beberapa lapisan dengan menggantinya menggunakan rekanan yang diimplementasikan di loralib. Saat ini, kami hanya mendukung nn.Linear, nn.Embedding, dan nn.Conv2d. Kami juga mendukung MergedLinear untuk kasus di mana satu nn.Linear mewakili lebih dari satu lapisan, seperti dalam beberapa implementasi proyeksi qkv pada mekanisme perhatian (lihat Catatan Tambahan untuk lebih jelasnya).

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

Sebelum memulai loop pelatihan, tandai hanya parameter LoRA yang dapat dilatih.

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

Sekarang pelatihan dapat dilanjutkan seperti biasa.

**Hyperparameter**

Tentukan dua dictionary: training_config dan peft_config. training_config mencakup hyperparameter untuk pelatihan, seperti learning rate, ukuran batch, dan pengaturan logging.

peft_config menentukan parameter terkait LoRA seperti rank, dropout, dan jenis tugas.

**Memuat Model dan Tokenizer**

Tentukan path ke model Phi-3 yang sudah dilatih sebelumnya (misalnya, "microsoft/Phi-3-mini-4k-instruct"). Konfigurasikan pengaturan model, termasuk penggunaan cache, tipe data (bfloat16 untuk presisi campuran), dan implementasi perhatian.

**Pelatihan**

Sesuaikan model Phi-3 menggunakan dataset instruksi percakapan kustom. Gunakan pengaturan LoRA dari peft_config untuk adaptasi yang efisien. Pantau kemajuan pelatihan menggunakan strategi logging yang telah ditentukan.

Evaluasi dan Penyimpanan: Evaluasi model yang telah disesuaikan.
Simpan checkpoint selama pelatihan untuk penggunaan di masa depan.

**Contoh**
- [Pelajari Lebih Lanjut dengan notebook contoh ini](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Contoh Skrip Python untuk FineTuning](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Contoh Fine Tuning di Hugging Face Hub dengan LoRA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Contoh Kartu Model Hugging Face - Contoh Fine Tuning LoRA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Contoh Fine Tuning di Hugging Face Hub dengan QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.