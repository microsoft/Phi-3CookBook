Dalam konteks Phi-3-mini, inferensi mengacu pada proses menggunakan model untuk membuat prediksi atau menghasilkan output berdasarkan data masukan. Berikut adalah detail lebih lanjut tentang Phi-3-mini dan kemampuan inferensinya.

Phi-3-mini adalah bagian dari seri model Phi-3 yang dirilis oleh Microsoft. Model-model ini dirancang untuk mendefinisikan ulang apa yang mungkin dilakukan dengan Small Language Models (SLMs).

Berikut adalah beberapa poin penting tentang Phi-3-mini dan kemampuan inferensinya:

## **Gambaran Umum Phi-3-mini:**
- Phi-3-mini memiliki ukuran parameter sebesar 3,8 miliar.
- Model ini dapat berjalan tidak hanya pada perangkat komputasi tradisional, tetapi juga pada perangkat edge seperti perangkat seluler dan perangkat IoT.
- Peluncuran Phi-3-mini memungkinkan individu dan perusahaan untuk menerapkan SLM pada berbagai perangkat keras, terutama di lingkungan dengan sumber daya terbatas.
- Model ini mendukung berbagai format, termasuk format tradisional PyTorch, versi terkuantisasi dari format gguf, dan versi terkuantisasi berbasis ONNX.

## **Mengakses Phi-3-mini:**
Untuk mengakses Phi-3-mini, Anda dapat menggunakan [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) dalam aplikasi Copilot. Semantic Kernel umumnya kompatibel dengan Azure OpenAI Service, model open-source di Hugging Face, dan model lokal.  
Anda juga dapat menggunakan [Ollama](https://ollama.com) atau [LlamaEdge](https://llamaedge.com) untuk memanggil model terkuantisasi. Ollama memungkinkan pengguna individu memanggil berbagai model terkuantisasi, sementara LlamaEdge menyediakan ketersediaan lintas platform untuk model GGUF.

## **Model Terkuantisasi:**
Banyak pengguna lebih memilih menggunakan model terkuantisasi untuk inferensi lokal. Sebagai contoh, Anda dapat langsung menjalankan Ollama run Phi-3 atau mengonfigurasinya secara offline menggunakan Modelfile. Modelfile menentukan jalur file GGUF dan format prompt.

## **Kemungkinan AI Generatif:**
Menggabungkan SLM seperti Phi-3-mini membuka peluang baru untuk AI generatif. Inferensi hanyalah langkah pertama; model-model ini dapat digunakan untuk berbagai tugas dalam skenario yang terbatas sumber daya, terikat latensi, dan terbatas biaya.

## **Membuka Potensi AI Generatif dengan Phi-3-mini: Panduan Inferensi dan Penerapan**  
Pelajari cara menggunakan Semantic Kernel, Ollama/LlamaEdge, dan ONNX Runtime untuk mengakses dan melakukan inferensi dengan model Phi-3-mini, serta eksplorasi kemungkinan AI generatif dalam berbagai skenario aplikasi.

**Fitur**  
Inferensi model phi3-mini di:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Sebagai kesimpulan, Phi-3-mini memungkinkan pengembang untuk mengeksplorasi berbagai format model dan memanfaatkan AI generatif dalam berbagai skenario aplikasi.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.