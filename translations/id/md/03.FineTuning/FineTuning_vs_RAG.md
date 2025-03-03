## Finetuning vs RAG

## Retrieval Augmented Generation

RAG adalah pengambilan data + pembuatan teks. Data terstruktur dan tidak terstruktur dari perusahaan disimpan dalam basis data vektor. Ketika mencari konten yang relevan, ringkasan dan konten yang relevan ditemukan untuk membentuk konteks, dan kemampuan penyelesaian teks dari LLM/SLM digabungkan untuk menghasilkan konten.

## Proses RAG
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.id.png)

## Fine-tuning
Fine-tuning adalah peningkatan berdasarkan model tertentu. Tidak perlu memulai dari algoritma model, tetapi data perlu terus-menerus dikumpulkan. Jika Anda menginginkan terminologi dan ekspresi bahasa yang lebih tepat dalam aplikasi industri, fine-tuning adalah pilihan yang lebih baik. Namun, jika data Anda sering berubah, fine-tuning bisa menjadi rumit.

## Bagaimana memilih
Jika jawaban kita membutuhkan pengenalan data eksternal, RAG adalah pilihan terbaik.

Jika Anda perlu menghasilkan pengetahuan industri yang stabil dan tepat, fine-tuning akan menjadi pilihan yang baik. RAG mengutamakan penarikan konten yang relevan, tetapi mungkin tidak selalu memahami nuansa spesifik secara mendalam.

Fine-tuning memerlukan kumpulan data berkualitas tinggi, dan jika hanya mencakup data dalam skala kecil, hasilnya tidak akan terlalu berbeda. RAG lebih fleksibel.  
Fine-tuning adalah kotak hitam, semacam metafisika, dan sulit untuk memahami mekanisme internalnya. Tetapi RAG dapat mempermudah menemukan sumber data, sehingga secara efektif mengatasi halusinasi atau kesalahan konten dan memberikan transparansi yang lebih baik.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan berbasis AI. Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan untuk menggunakan penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.