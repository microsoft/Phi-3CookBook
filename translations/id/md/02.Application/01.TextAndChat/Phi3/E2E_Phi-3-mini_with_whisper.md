# Chatbot Interaktif Phi 3 Mini 4K Instruct dengan Whisper

## Gambaran Umum

Chatbot Interaktif Phi 3 Mini 4K Instruct adalah alat yang memungkinkan pengguna berinteraksi dengan demo Microsoft Phi 3 Mini 4K Instruct menggunakan input teks atau audio. Chatbot ini dapat digunakan untuk berbagai tugas, seperti terjemahan, pembaruan cuaca, dan pengumpulan informasi umum.

### Memulai

Untuk menggunakan chatbot ini, ikuti langkah-langkah berikut:

1. Buka [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Di jendela utama notebook, Anda akan melihat antarmuka kotak obrolan dengan kotak input teks dan tombol "Kirim".
3. Untuk menggunakan chatbot berbasis teks, cukup ketik pesan Anda di kotak input teks dan klik tombol "Kirim". Chatbot akan merespons dengan file audio yang dapat diputar langsung dari dalam notebook.

**Catatan**: Alat ini memerlukan GPU dan akses ke model Microsoft Phi-3 dan OpenAI Whisper, yang digunakan untuk pengenalan suara dan terjemahan.

### Persyaratan GPU

Untuk menjalankan demo ini, Anda memerlukan memori GPU sebesar 12GB.

Persyaratan memori untuk menjalankan demo **Microsoft-Phi-3-Mini-4K Instruct** pada GPU akan bergantung pada beberapa faktor, seperti ukuran data input (audio atau teks), bahasa yang digunakan untuk terjemahan, kecepatan model, dan memori yang tersedia pada GPU.

Secara umum, model Whisper dirancang untuk dijalankan pada GPU. Jumlah minimum memori GPU yang direkomendasikan untuk menjalankan model Whisper adalah 8 GB, tetapi model ini dapat menangani jumlah memori yang lebih besar jika diperlukan.

Penting untuk dicatat bahwa menjalankan data dalam jumlah besar atau volume permintaan yang tinggi pada model ini mungkin memerlukan lebih banyak memori GPU dan/atau dapat menyebabkan masalah kinerja. Disarankan untuk menguji kasus penggunaan Anda dengan konfigurasi yang berbeda dan memantau penggunaan memori untuk menentukan pengaturan optimal sesuai kebutuhan Anda.

## Contoh E2E untuk Chatbot Interaktif Phi 3 Mini 4K Instruct dengan Whisper

Notebook Jupyter berjudul [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) menunjukkan cara menggunakan Demo Microsoft Phi 3 Mini 4K Instruct untuk menghasilkan teks dari input audio atau teks tertulis. Notebook ini mendefinisikan beberapa fungsi:

1. `tts_file_name(text)`: Fungsi ini menghasilkan nama file berdasarkan teks input untuk menyimpan file audio yang dihasilkan.
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Fungsi ini menggunakan API Edge TTS untuk menghasilkan file audio dari daftar potongan teks input. Parameter inputnya adalah daftar potongan teks, kecepatan bicara, nama suara, dan jalur keluaran untuk menyimpan file audio yang dihasilkan.
3. `talk(input_text)`: Fungsi ini menghasilkan file audio dengan menggunakan API Edge TTS dan menyimpannya dengan nama file acak di direktori /content/audio. Parameter inputnya adalah teks input yang akan diubah menjadi suara.
4. `run_text_prompt(message, chat_history)`: Fungsi ini menggunakan demo Microsoft Phi 3 Mini 4K Instruct untuk menghasilkan file audio dari input pesan dan menambahkannya ke riwayat obrolan.
5. `run_audio_prompt(audio, chat_history)`: Fungsi ini mengonversi file audio menjadi teks menggunakan API model Whisper dan meneruskannya ke fungsi `run_text_prompt()`.
6. Kode ini meluncurkan aplikasi Gradio yang memungkinkan pengguna untuk berinteraksi dengan demo Phi 3 Mini 4K Instruct dengan mengetik pesan atau mengunggah file audio. Output ditampilkan sebagai pesan teks dalam aplikasi.

## Pemecahan Masalah

Menginstal driver GPU Cuda

1. Pastikan aplikasi Linux Anda sudah diperbarui

    ```bash
    sudo apt update
    ```

2. Instal driver Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. Daftarkan lokasi driver Cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. Periksa ukuran memori GPU Nvidia (Memerlukan 12GB Memori GPU)

    ```bash
    nvidia-smi
    ```

5. Kosongkan Cache: Jika Anda menggunakan PyTorch, Anda dapat memanggil torch.cuda.empty_cache() untuk melepaskan semua memori cache yang tidak digunakan sehingga dapat digunakan oleh aplikasi GPU lainnya.

    ```python
    torch.cuda.empty_cache() 
    ```

6. Periksa Nvidia Cuda

    ```bash
    nvcc --version
    ```

7. Lakukan tugas berikut untuk membuat token Hugging Face.

    - Buka halaman [Pengaturan Token Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Pilih **Token Baru**.
    - Masukkan **Nama** proyek yang ingin Anda gunakan.
    - Pilih **Tipe** menjadi **Write**.

> **Catatan**
>
> Jika Anda menemui kesalahan berikut:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Untuk mengatasinya, ketik perintah berikut di dalam terminal Anda.
>
> ```bash
> sudo ldconfig
> ```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan berbasis AI. Meskipun kami berusaha untuk memberikan terjemahan yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.