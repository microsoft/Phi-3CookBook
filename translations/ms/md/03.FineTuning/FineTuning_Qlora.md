**Menyesuaikan Phi-3 dengan QLoRA**

Menyesuaikan model bahasa Phi-3 Mini dari Microsoft menggunakan [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA akan membantu meningkatkan pemahaman percakapan dan penghasilan respons.

Untuk memuat model dalam 4bits menggunakan transformers dan bitsandbytes, Anda harus menginstal accelerate dan transformers dari sumber, serta memastikan Anda memiliki versi terbaru dari pustaka bitsandbytes.

**Contoh**
- [Pelajari Lebih Lanjut dengan notebook contoh ini](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Contoh Python FineTuning](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Contoh Fine Tuning Hugging Face Hub dengan LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Contoh Fine Tuning Hugging Face Hub dengan QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab ke atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.