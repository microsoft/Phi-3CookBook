Dalam konteks Phi-3-mini, inferens merujuk kepada proses menggunakan model untuk membuat ramalan atau menghasilkan output berdasarkan data input. Berikut adalah maklumat lanjut mengenai Phi-3-mini dan keupayaan inferensnya.

Phi-3-mini adalah sebahagian daripada siri model Phi-3 yang dikeluarkan oleh Microsoft. Model-model ini direka untuk mentakrifkan semula apa yang mungkin dicapai dengan Small Language Models (SLMs).

Berikut adalah beberapa perkara utama mengenai Phi-3-mini dan keupayaan inferensnya:

## **Gambaran Keseluruhan Phi-3-mini:**
- Phi-3-mini mempunyai saiz parameter sebanyak 3.8 bilion.
- Ia boleh dijalankan bukan sahaja pada peranti pengkomputeran tradisional tetapi juga pada peranti edge seperti peranti mudah alih dan peranti IoT.
- Pelepasan Phi-3-mini membolehkan individu dan syarikat menggunakan SLM pada pelbagai peranti perkakasan, terutamanya dalam persekitaran yang terhad sumber.
- Ia menyokong pelbagai format model, termasuk format PyTorch tradisional, versi kuantized dalam format gguf, dan versi kuantized berasaskan ONNX.

## **Mengakses Phi-3-mini:**
Untuk mengakses Phi-3-mini, anda boleh menggunakan [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) dalam aplikasi Copilot. Semantic Kernel umumnya serasi dengan Azure OpenAI Service, model sumber terbuka di Hugging Face, dan model tempatan.  
Anda juga boleh menggunakan [Ollama](https://ollama.com) atau [LlamaEdge](https://llamaedge.com) untuk memanggil model kuantized. Ollama membolehkan pengguna individu memanggil pelbagai model kuantized, manakala LlamaEdge menyediakan ketersediaan silang platform untuk model GGUF.

## **Model Kuantized:**
Ramai pengguna lebih suka menggunakan model kuantized untuk inferens tempatan. Sebagai contoh, anda boleh terus menjalankan Ollama run Phi-3 atau mengkonfigurasinya secara luar talian menggunakan Modelfile. Modelfile menentukan laluan fail GGUF dan format prompt.

## **Kemungkinan AI Generatif:**
Menggabungkan SLM seperti Phi-3-mini membuka peluang baru untuk AI generatif. Inferens hanyalah langkah pertama; model-model ini boleh digunakan untuk pelbagai tugas dalam persekitaran yang terhad sumber, terikat kependaman, dan terhad kos.

## **Meneroka AI Generatif dengan Phi-3-mini: Panduan untuk Inferens dan Penerapan**
Pelajari cara menggunakan Semantic Kernel, Ollama/LlamaEdge, dan ONNX Runtime untuk mengakses dan melakukan inferens model Phi-3-mini, serta meneroka kemungkinan AI generatif dalam pelbagai senario aplikasi.

**Ciri-Ciri**
Inferens model phi3-mini dalam:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Secara ringkasnya, Phi-3-mini membolehkan pembangun meneroka pelbagai format model dan memanfaatkan AI generatif dalam pelbagai senario aplikasi.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.