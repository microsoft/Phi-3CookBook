# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo untuk Menunjukkan WebGPU dan Pola RAG

Pola RAG dengan model Phi-3.5 Onnx Hosted memanfaatkan pendekatan Retrieval-Augmented Generation, menggabungkan kekuatan model Phi-3.5 dengan hosting ONNX untuk penerapan AI yang efisien. Pola ini sangat penting dalam menyempurnakan model untuk tugas-tugas khusus domain, menawarkan perpaduan antara kualitas, efisiensi biaya, dan pemahaman konteks panjang. Ini merupakan bagian dari rangkaian Azure AI, menyediakan berbagai pilihan model yang mudah ditemukan, dicoba, dan digunakan, memenuhi kebutuhan kustomisasi berbagai industri.

## Apa itu WebGPU 
WebGPU adalah API grafis web modern yang dirancang untuk memberikan akses yang efisien ke unit pemrosesan grafis (GPU) perangkat langsung dari browser web. WebGPU dimaksudkan sebagai penerus WebGL, dengan menawarkan beberapa peningkatan utama:

1. **Kompatibilitas dengan GPU Modern**: WebGPU dirancang untuk bekerja dengan mulus pada arsitektur GPU terkini, memanfaatkan API sistem seperti Vulkan, Metal, dan Direct3D 12.
2. **Kinerja yang Ditingkatkan**: Mendukung komputasi GPU untuk tujuan umum dan operasi yang lebih cepat, membuatnya cocok untuk rendering grafis maupun tugas pembelajaran mesin.
3. **Fitur Canggih**: WebGPU memberikan akses ke kemampuan GPU yang lebih canggih, memungkinkan beban kerja grafis dan komputasi yang lebih kompleks dan dinamis.
4. **Beban Kerja JavaScript yang Berkurang**: Dengan memindahkan lebih banyak tugas ke GPU, WebGPU secara signifikan mengurangi beban kerja pada JavaScript, menghasilkan kinerja yang lebih baik dan pengalaman yang lebih lancar.

WebGPU saat ini didukung di browser seperti Google Chrome, dengan pengembangan yang sedang berlangsung untuk memperluas dukungan ke platform lain.

### 03.WebGPU
Lingkungan yang Dibutuhkan:

**Browser yang Didukung:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Mengaktifkan WebGPU:

- Di Chrome/Microsoft Edge 

Aktifkan flag `chrome://flags/#enable-unsafe-webgpu`.

#### Buka Browser Anda:
Jalankan Google Chrome atau Microsoft Edge.

#### Akses Halaman Flags:
Di bilah alamat, ketik `chrome://flags` lalu tekan Enter.

#### Cari Flag:
Di kotak pencarian di bagian atas halaman, ketik 'enable-unsafe-webgpu'.

#### Aktifkan Flag:
Temukan flag #enable-unsafe-webgpu dalam daftar hasil.

Klik menu dropdown di sebelahnya dan pilih Enabled.

#### Mulai Ulang Browser Anda:

Setelah mengaktifkan flag, Anda perlu memulai ulang browser agar perubahan berlaku. Klik tombol Relaunch yang muncul di bagian bawah halaman.

- Untuk Linux, jalankan browser dengan `--enable-features=Vulkan`.
- Safari 18 (macOS 15) memiliki WebGPU yang diaktifkan secara default.
- Di Firefox Nightly, masukkan about:config di bilah alamat dan `set dom.webgpu.enabled to true`.

### Mengatur GPU untuk Microsoft Edge 

Berikut langkah-langkah untuk mengatur GPU berkinerja tinggi untuk Microsoft Edge di Windows:

- **Buka Pengaturan:** Klik pada menu Mulai dan pilih Pengaturan.
- **Pengaturan Sistem:** Masuk ke Sistem lalu Tampilan.
- **Pengaturan Grafis:** Gulir ke bawah dan klik pada Pengaturan grafis.
- **Pilih Aplikasi:** Di bawah “Pilih aplikasi untuk mengatur preferensi,” pilih Aplikasi desktop lalu Telusuri.
- **Pilih Edge:** Navigasikan ke folder instalasi Edge (biasanya `C:\Program Files (x86)\Microsoft\Edge\Application`) dan pilih `msedge.exe`.
- **Atur Preferensi:** Klik Opsi, pilih Performa tinggi, lalu klik Simpan.
Ini akan memastikan bahwa Microsoft Edge menggunakan GPU berkinerja tinggi Anda untuk kinerja yang lebih baik.
- **Restart** perangkat Anda agar pengaturan ini berlaku.

### Contoh: Silakan [klik tautan ini](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berupaya untuk mencapai akurasi, harap disadari bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.