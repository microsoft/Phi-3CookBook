# **Quantizing Phi Family menggunakan llama.cpp**

## **Apa itu llama.cpp**

llama.cpp adalah perpustakaan perangkat lunak sumber terbuka yang ditulis terutama dalam C++ untuk melakukan inferensi pada berbagai Large Language Models (LLMs), seperti Llama. Tujuan utamanya adalah memberikan performa mutakhir untuk inferensi LLM di berbagai perangkat keras dengan pengaturan yang minimal. Selain itu, terdapat juga binding Python untuk perpustakaan ini, yang menyediakan API tingkat tinggi untuk melengkapi teks dan server web yang kompatibel dengan OpenAI.

Tujuan utama llama.cpp adalah memungkinkan inferensi LLM dengan pengaturan minimal dan performa mutakhir pada berbagai perangkat keras - baik secara lokal maupun di cloud.

- Implementasi murni dalam C/C++ tanpa dependensi
- Apple silicon menjadi prioritas utama - dioptimalkan melalui ARM NEON, Accelerate, dan Metal frameworks
- Dukungan AVX, AVX2, dan AVX512 untuk arsitektur x86
- Kuantisasi bilangan bulat 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, dan 8-bit untuk inferensi yang lebih cepat dan penggunaan memori yang lebih rendah
- Kernel CUDA kustom untuk menjalankan LLM di GPU NVIDIA (dukungan untuk GPU AMD melalui HIP)
- Dukungan backend Vulkan dan SYCL
- Inferensi hibrida CPU+GPU untuk mempercepat model yang lebih besar dari kapasitas total VRAM

## **Kuantisasi Phi-3.5 dengan llama.cpp**

Model Phi-3.5-Instruct dapat dikuantisasi menggunakan llama.cpp, tetapi Phi-3.5-Vision dan Phi-3.5-MoE belum didukung. Format yang dikonversi oleh llama.cpp adalah gguf, yang juga merupakan format kuantisasi yang paling banyak digunakan.

Terdapat banyak model dalam format GGUF yang telah dikuantisasi di Hugging Face. AI Foundry, Ollama, dan LlamaEdge mengandalkan llama.cpp, sehingga model GGUF sering digunakan.

### **Apa itu GGUF**

GGUF adalah format biner yang dioptimalkan untuk pemuatan dan penyimpanan model secara cepat, membuatnya sangat efisien untuk tujuan inferensi. GGUF dirancang untuk digunakan dengan GGML dan eksekutor lainnya. GGUF dikembangkan oleh @ggerganov yang juga merupakan pengembang llama.cpp, sebuah framework inferensi LLM populer berbasis C/C++. Model yang awalnya dikembangkan dalam framework seperti PyTorch dapat dikonversi ke format GGUF untuk digunakan dengan mesin-mesin tersebut.

### **ONNX vs GGUF**

ONNX adalah format tradisional untuk pembelajaran mesin/pembelajaran mendalam, yang didukung dengan baik di berbagai Framework AI dan memiliki skenario penggunaan yang baik pada perangkat edge. Sedangkan GGUF berbasis pada llama.cpp dan bisa dikatakan lahir di era GenAI. Keduanya memiliki kegunaan yang serupa. Jika Anda menginginkan performa yang lebih baik pada perangkat keras tertanam dan lapisan aplikasi, ONNX mungkin menjadi pilihan Anda. Jika Anda menggunakan framework dan teknologi turunan dari llama.cpp, maka GGUF mungkin lebih cocok.

### **Kuantisasi Phi-3.5-Instruct menggunakan llama.cpp**

**1. Konfigurasi Lingkungan**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kuantisasi**

Menggunakan llama.cpp untuk mengonversi Phi-3.5-Instruct ke FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Mengkuantisasi Phi-3.5 ke INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Pengujian**

Pasang llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Catatan*** 

Jika Anda menggunakan Apple Silicon, silakan pasang llama-cpp-python seperti ini


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Pengujian 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Sumber Daya**

1. Pelajari lebih lanjut tentang llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Pelajari lebih lanjut tentang GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.