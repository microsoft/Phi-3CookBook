# Chatbot Interaktif Phi 3 Mini 4K dengan Whisper

## Gambaran Umum

Chatbot Interaktif Phi 3 Mini 4K adalah alat yang membolehkan pengguna berinteraksi dengan demo Microsoft Phi 3 Mini 4K menggunakan input teks atau audio. Chatbot ini boleh digunakan untuk pelbagai tugas seperti terjemahan, kemas kini cuaca, dan pengumpulan maklumat umum.

### Cara Bermula

Untuk menggunakan chatbot ini, ikuti langkah-langkah berikut:

1. Buka [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb).
2. Dalam tetingkap utama notebook, anda akan melihat antara muka kotak sembang dengan kotak input teks dan butang "Send".
3. Untuk menggunakan chatbot berasaskan teks, taip mesej anda ke dalam kotak input teks dan klik butang "Send". Chatbot akan memberikan respons dalam bentuk fail audio yang boleh dimainkan terus dari dalam notebook.

**Nota**: Alat ini memerlukan GPU dan akses kepada model Microsoft Phi-3 dan OpenAI Whisper, yang digunakan untuk pengecaman dan terjemahan suara.

### Keperluan GPU

Untuk menjalankan demo ini, anda memerlukan memori GPU sebanyak 12GB.

Keperluan memori untuk menjalankan demo **Microsoft-Phi-3-Mini-4K instruct** pada GPU bergantung kepada beberapa faktor seperti saiz data input (audio atau teks), bahasa yang digunakan untuk terjemahan, kelajuan model, dan memori yang tersedia pada GPU.

Secara umum, model Whisper direka untuk dijalankan pada GPU. Jumlah minimum memori GPU yang disyorkan untuk menjalankan model Whisper adalah 8GB, tetapi ia boleh mengendalikan jumlah memori yang lebih besar jika diperlukan.

Penting untuk diingat bahawa menjalankan data dalam jumlah besar atau permintaan dalam volume tinggi pada model mungkin memerlukan lebih banyak memori GPU dan/atau boleh menyebabkan masalah prestasi. Adalah disyorkan untuk menguji kes penggunaan anda dengan konfigurasi berbeza dan memantau penggunaan memori untuk menentukan tetapan optimum bagi keperluan spesifik anda.

## Contoh E2E untuk Chatbot Interaktif Phi 3 Mini 4K dengan Whisper

Notebook Jupyter bertajuk [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) menunjukkan cara menggunakan demo Microsoft Phi 3 Mini 4K untuk menghasilkan teks daripada input audio atau teks bertulis. Notebook ini mentakrifkan beberapa fungsi:

1. `tts_file_name(text)`: Fungsi ini menghasilkan nama fail berdasarkan teks input untuk menyimpan fail audio yang dihasilkan.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Fungsi ini menggunakan Edge TTS API untuk menghasilkan fail audio daripada senarai pecahan teks input. Parameter input termasuk senarai pecahan, kadar ucapan, nama suara, dan laluan output untuk menyimpan fail audio yang dihasilkan.
1. `talk(input_text)`: Fungsi ini menghasilkan fail audio dengan menggunakan Edge TTS API dan menyimpannya dengan nama fail rawak dalam direktori /content/audio. Parameter input adalah teks yang akan ditukar kepada suara.
1. `run_text_prompt(message, chat_history)`: Fungsi ini menggunakan demo Microsoft Phi 3 Mini 4K untuk menghasilkan fail audio daripada input mesej dan menambahkannya ke dalam sejarah sembang.
1. `run_audio_prompt(audio, chat_history)`: Fungsi ini menukar fail audio kepada teks menggunakan Whisper model API dan menghantarnya ke fungsi `run_text_prompt()`.
1. Kod ini melancarkan aplikasi Gradio yang membolehkan pengguna berinteraksi dengan demo Phi 3 Mini 4K dengan menaip mesej atau memuat naik fail audio. Output dipaparkan sebagai mesej teks dalam aplikasi.

## Penyelesaian Masalah

Memasang pemacu GPU Cuda

1. Pastikan aplikasi Linux anda adalah terkini

    ```bash
    sudo apt update
    ```

1. Pasang Pemacu Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Daftarkan lokasi pemacu cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Semak saiz memori Nvidia GPU (Memerlukan 12GB Memori GPU)

    ```bash
    nvidia-smi
    ```

1. Kosongkan Cache: Jika anda menggunakan PyTorch, anda boleh memanggil torch.cuda.empty_cache() untuk melepaskan semua memori cache yang tidak digunakan supaya ia boleh digunakan oleh aplikasi GPU lain

    ```python
    torch.cuda.empty_cache() 
    ```

1. Semak Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Lakukan langkah berikut untuk mencipta token Hugging Face.

    - Navigasi ke [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Pilih **New token**.
    - Masukkan **Name** projek yang ingin anda gunakan.
    - Pilih **Type** kepada **Write**.

> **Nota**
>
> Jika anda menghadapi ralat berikut:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Untuk menyelesaikan ini, taip arahan berikut di dalam terminal anda.
>
> ```bash
> sudo ldconfig
> ```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.