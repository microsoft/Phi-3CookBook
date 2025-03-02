Phi-3-mini WebGPU RAG Chatbot

## Demo untuk Menunjukkan WebGPU dan Pola RAG
Pola RAG dengan model Phi-3 Onnx Hosted memanfaatkan pendekatan Retrieval-Augmented Generation, menggabungkan kekuatan model Phi-3 dengan hosting ONNX untuk penerapan AI yang efisien. Pola ini sangat berguna dalam menyempurnakan model untuk tugas-tugas khusus domain, menawarkan perpaduan kualitas, efisiensi biaya, dan pemahaman konteks panjang. Ini adalah bagian dari rangkaian Azure AI, menyediakan berbagai pilihan model yang mudah ditemukan, dicoba, dan digunakan, sesuai dengan kebutuhan kustomisasi berbagai industri. Model Phi-3, termasuk Phi-3-mini, Phi-3-small, dan Phi-3-medium, tersedia di Azure AI Model Catalog dan dapat disesuaikan serta diterapkan secara mandiri atau melalui platform seperti HuggingFace dan ONNX, menunjukkan komitmen Microsoft terhadap solusi AI yang mudah diakses dan efisien.

## Apa itu WebGPU
WebGPU adalah API grafis web modern yang dirancang untuk memberikan akses efisien ke unit pemrosesan grafis (GPU) perangkat secara langsung dari browser web. WebGPU dimaksudkan untuk menjadi penerus WebGL, dengan beberapa peningkatan utama:

1. **Kompatibilitas dengan GPU Modern**: WebGPU dirancang untuk bekerja dengan mulus pada arsitektur GPU masa kini, memanfaatkan API sistem seperti Vulkan, Metal, dan Direct3D 12.
2. **Kinerja yang Ditingkatkan**: Mendukung komputasi GPU umum dan operasi yang lebih cepat, membuatnya cocok untuk rendering grafis dan tugas pembelajaran mesin.
3. **Fitur Lanjutan**: WebGPU memberikan akses ke kemampuan GPU yang lebih canggih, memungkinkan beban kerja grafis dan komputasi yang lebih kompleks dan dinamis.
4. **Beban Kerja JavaScript yang Berkurang**: Dengan mengalihkan lebih banyak tugas ke GPU, WebGPU secara signifikan mengurangi beban kerja pada JavaScript, menghasilkan kinerja yang lebih baik dan pengalaman yang lebih lancar.

Saat ini, WebGPU didukung di browser seperti Google Chrome, dengan pengembangan yang sedang berlangsung untuk memperluas dukungan ke platform lain.

### 03.WebGPU
Lingkungan yang Diperlukan:

**Browser yang Didukung:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Mengaktifkan WebGPU:

- Di Chrome/Microsoft Edge 

Aktifkan flag `chrome://flags/#enable-unsafe-webgpu`.

#### Buka Browser Anda:
Luncurkan Google Chrome atau Microsoft Edge.

#### Akses Halaman Flags:
Di bilah alamat, ketik `chrome://flags` dan tekan Enter.

#### Cari Flag:
Di kotak pencarian di bagian atas halaman, ketik 'enable-unsafe-webgpu'.

#### Aktifkan Flag:
Temukan flag #enable-unsafe-webgpu dalam daftar hasil.

Klik menu dropdown di sebelahnya dan pilih Enabled.

#### Mulai Ulang Browser Anda:

Setelah mengaktifkan flag, Anda perlu memulai ulang browser agar perubahan berlaku. Klik tombol Relaunch yang muncul di bagian bawah halaman.

- Untuk Linux, luncurkan browser dengan `--enable-features=Vulkan`.
- Safari 18 (macOS 15) sudah memiliki WebGPU yang diaktifkan secara default.
- Di Firefox Nightly, masukkan about:config di bilah alamat dan `set dom.webgpu.enabled to true`.

### Menyiapkan GPU untuk Microsoft Edge 

Berikut langkah-langkah untuk menyiapkan GPU berkinerja tinggi untuk Microsoft Edge di Windows:

- **Buka Pengaturan:** Klik menu Start dan pilih Pengaturan.
- **Pengaturan Sistem:** Masuk ke Sistem lalu Tampilan.
- **Pengaturan Grafis:** Gulir ke bawah dan klik Pengaturan grafis.
- **Pilih Aplikasi:** Di bawah "Pilih aplikasi untuk menetapkan preferensi," pilih Aplikasi desktop lalu Telusuri.
- **Pilih Edge:** Arahkan ke folder instalasi Edge (biasanya `C:\Program Files (x86)\Microsoft\Edge\Application`) dan pilih `msedge.exe`.
- **Tetapkan Preferensi:** Klik Opsi, pilih Performa tinggi, lalu klik Simpan.
Ini akan memastikan bahwa Microsoft Edge menggunakan GPU berkinerja tinggi Anda untuk kinerja yang lebih baik. 
- **Restart** komputer Anda agar pengaturan ini berlaku.

### Buka Codespace Anda:
Arahkan ke repositori Anda di GitHub.
Klik tombol Code dan pilih Open with Codespaces.

Jika Anda belum memiliki Codespace, Anda dapat membuatnya dengan mengklik New codespace.

**Catatan** Menginstal Lingkungan Node di Codespace Anda
Menjalankan demo npm dari GitHub Codespace adalah cara yang bagus untuk menguji dan mengembangkan proyek Anda. Berikut adalah panduan langkah demi langkah untuk membantu Anda memulai:

### Siapkan Lingkungan Anda:
Setelah Codespace Anda terbuka, pastikan Anda memiliki Node.js dan npm yang terinstal. Anda dapat memeriksanya dengan menjalankan:
```
node -v
```
```
npm -v
```

Jika belum terinstal, Anda dapat menginstalnya menggunakan:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Arahkan ke Direktori Proyek Anda:
Gunakan terminal untuk menavigasi ke direktori tempat proyek npm Anda berada:
```
cd path/to/your/project
```

### Instal Dependensi:
Jalankan perintah berikut untuk menginstal semua dependensi yang diperlukan yang tercantum dalam file package.json Anda:

```
npm install
```

### Jalankan Demo:
Setelah dependensi terinstal, Anda dapat menjalankan skrip demo Anda. Ini biasanya ditentukan di bagian skrip file package.json Anda. Sebagai contoh, jika skrip demo Anda bernama start, Anda dapat menjalankan:

```
npm run build
```
```
npm run dev
```

### Akses Demo:
Jika demo Anda melibatkan server web, Codespaces akan menyediakan URL untuk mengaksesnya. Cari notifikasi atau periksa tab Ports untuk menemukan URL tersebut.

**Catatan:** Model perlu di-cache di browser, sehingga mungkin membutuhkan waktu untuk memuat. 

### Demo RAG
Unggah file markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Pilih File Anda:
Klik tombol yang bertuliskan “Pilih File” untuk memilih dokumen yang ingin Anda unggah.

### Unggah Dokumen:
Setelah memilih file Anda, klik tombol “Unggah” untuk memuat dokumen Anda untuk RAG (Retrieval-Augmented Generation).

### Mulai Obrolan Anda:
Setelah dokumen diunggah, Anda dapat memulai sesi obrolan menggunakan RAG berdasarkan konten dokumen Anda.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan berbasis AI. Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.