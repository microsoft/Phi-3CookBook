# **Inference Phi-3 di Android**

Mari kita lihat bagaimana anda dapat melakukan inferensi dengan Phi-3-mini di perangkat Android. Phi-3-mini adalah seri model baru dari Microsoft yang memungkinkan penerapan Large Language Models (LLMs) di perangkat edge dan IoT.

## Semantic Kernel dan Inferensi

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) adalah kerangka aplikasi yang memungkinkan anda membuat aplikasi yang kompatibel dengan Azure OpenAI Service, model OpenAI, dan bahkan model lokal. Jika anda baru mengenal Semantic Kernel, kami sarankan untuk melihat [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Mengakses Phi-3-mini Menggunakan Semantic Kernel

Anda dapat menggabungkannya dengan Hugging Face Connector di Semantic Kernel. Lihat [Kode Contoh](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Secara default, ini sesuai dengan ID model di Hugging Face. Namun, anda juga dapat terhubung ke server model Phi-3-mini yang dibangun secara lokal.

### Memanggil Model Kuantisasi dengan Ollama atau LlamaEdge

Banyak pengguna lebih memilih menggunakan model kuantisasi untuk menjalankan model secara lokal. [Ollama](https://ollama.com/) dan [LlamaEdge](https://llamaedge.com) memungkinkan pengguna individu memanggil berbagai model kuantisasi:

#### Ollama

Anda dapat langsung menjalankan `ollama run Phi-3` atau mengonfigurasinya secara offline dengan membuat `Modelfile` dengan jalur ke file `.gguf` anda.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Kode Contoh](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Jika anda ingin menggunakan file `.gguf` di cloud dan perangkat edge secara bersamaan, LlamaEdge adalah pilihan yang bagus. Anda dapat merujuk ke [kode contoh](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) untuk memulai.

### Instal dan Jalankan di Ponsel Android

1. **Unduh aplikasi MLC Chat** (Gratis) untuk ponsel Android.
2. Unduh file APK (148MB) dan instal di perangkat anda.
3. Buka aplikasi MLC Chat. Anda akan melihat daftar model AI, termasuk Phi-3-mini.

Sebagai kesimpulan, Phi-3-mini membuka peluang menarik untuk AI generatif di perangkat edge, dan anda dapat mulai menjelajahi kemampuannya di Android.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berautoriti. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.