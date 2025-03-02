**Fine-tuning Phi-3 dengan QLoRA**

Fine-tuning model bahasa Phi-3 Mini dari Microsoft menggunakan [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA akan membantu meningkatkan pemahaman percakapan dan pembuatan respons.

Untuk memuat model dalam 4bits menggunakan transformers dan bitsandbytes, Anda perlu menginstal accelerate dan transformers dari sumber, serta memastikan Anda memiliki versi terbaru dari pustaka bitsandbytes.

**Contoh**
- [Pelajari Lebih Lanjut dengan notebook contoh ini](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Contoh FineTuning Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Contoh Fine Tuning di Hugging Face Hub dengan LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Contoh Fine Tuning di Hugging Face Hub dengan QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan berbasis AI. Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat krusial, disarankan menggunakan jasa penerjemah manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang salah yang timbul dari penggunaan terjemahan ini.