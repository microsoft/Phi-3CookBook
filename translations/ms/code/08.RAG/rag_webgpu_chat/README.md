Phi-3-mini WebGPU RAG Chatbot

## Demo untuk Memperkenalkan WebGPU dan Corak RAG
Corak RAG dengan model Phi-3 Onnx Hosted menggunakan pendekatan Retrieval-Augmented Generation, menggabungkan kekuatan model Phi-3 dengan hosting ONNX untuk penyebaran AI yang efisien. Corak ini sangat penting dalam menyempurnakan model untuk tugas-tugas khusus domain, menawarkan gabungan antara kualiti, kos efektif, dan pemahaman konteks panjang. Ia merupakan sebahagian daripada rangkaian Azure AI, menyediakan pelbagai model yang mudah dicari, dicuba, dan digunakan, memenuhi keperluan penyesuaian pelbagai industri. Model Phi-3, termasuk Phi-3-mini, Phi-3-small, dan Phi-3-medium, tersedia di Azure AI Model Catalog dan boleh disesuaikan serta digunakan secara kendiri atau melalui platform seperti HuggingFace dan ONNX, menunjukkan komitmen Microsoft terhadap penyelesaian AI yang mudah diakses dan efisien.

## Apa itu WebGPU 
WebGPU ialah API grafik web moden yang direka untuk memberikan akses yang efisien kepada unit pemprosesan grafik (GPU) sesebuah peranti secara langsung dari pelayar web. Ia bertujuan menjadi pengganti kepada WebGL, menawarkan beberapa penambahbaikan utama:

1. **Keserasian dengan GPU Moden**: WebGPU dibina untuk berfungsi lancar dengan seni bina GPU terkini, memanfaatkan API sistem seperti Vulkan, Metal, dan Direct3D 12.
2. **Prestasi Ditingkatkan**: Ia menyokong pengiraan GPU untuk pelbagai tujuan dan operasi yang lebih pantas, menjadikannya sesuai untuk rendering grafik dan tugas pembelajaran mesin.
3. **Ciri-ciri Lanjutan**: WebGPU memberikan akses kepada keupayaan GPU yang lebih maju, membolehkan beban kerja grafik dan pengiraan yang lebih kompleks dan dinamik.
4. **Mengurangkan Beban Kerja JavaScript**: Dengan memindahkan lebih banyak tugas kepada GPU, WebGPU secara signifikan mengurangkan beban kerja pada JavaScript, menghasilkan prestasi yang lebih baik dan pengalaman yang lebih lancar.

WebGPU kini disokong dalam pelayar seperti Google Chrome, dengan usaha berterusan untuk memperluaskan sokongan ke platform lain.

### 03.WebGPU
Keperluan Persekitaran:

**Pelayar yang Disokong:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Mengaktifkan WebGPU:

- Dalam Chrome/Microsoft Edge 

Aktifkan bendera `chrome://flags/#enable-unsafe-webgpu`.

#### Buka Pelayar Anda:
Lancarkan Google Chrome atau Microsoft Edge.

#### Akses Halaman Flags:
Dalam bar alamat, taipkan `chrome://flags` dan tekan Enter.

#### Cari Bendera:
Dalam kotak carian di bahagian atas halaman, taip 'enable-unsafe-webgpu'

#### Aktifkan Bendera:
Cari bendera #enable-unsafe-webgpu dalam senarai hasil.

Klik menu dropdown di sebelahnya dan pilih Enabled.

#### Mulakan Semula Pelayar Anda:

Selepas mengaktifkan bendera, anda perlu memulakan semula pelayar anda untuk perubahan berkuat kuasa. Klik butang Relaunch yang muncul di bahagian bawah halaman.

- Untuk Linux, lancarkan pelayar dengan `--enable-features=Vulkan`.
- Safari 18 (macOS 15) mempunyai WebGPU yang diaktifkan secara lalai.
- Dalam Firefox Nightly, masukkan about:config dalam bar alamat dan `set dom.webgpu.enabled to true`.

### Menyediakan GPU untuk Microsoft Edge 

Berikut adalah langkah-langkah untuk menyediakan GPU berprestasi tinggi untuk Microsoft Edge pada Windows:

- **Buka Tetapan:** Klik pada menu Mula dan pilih Tetapan.
- **Tetapan Sistem:** Pergi ke Sistem dan kemudian Paparan.
- **Tetapan Grafik:** Tatal ke bawah dan klik pada tetapan Grafik.
- **Pilih Aplikasi:** Di bawah "Pilih aplikasi untuk menetapkan keutamaan," pilih Aplikasi Desktop dan kemudian Browse.
- **Pilih Edge:** Navigasi ke folder pemasangan Edge (biasanya `C:\Program Files (x86)\Microsoft\Edge\Application`) dan pilih `msedge.exe`.
- **Tetapkan Keutamaan:** Klik Pilihan, pilih Prestasi Tinggi, dan kemudian klik Simpan.
Ini akan memastikan bahawa Microsoft Edge menggunakan GPU berprestasi tinggi anda untuk prestasi yang lebih baik.
- **Mulakan Semula** komputer anda untuk perubahan ini berkuat kuasa.

### Buka Codespace Anda:
Navigasi ke repositori anda di GitHub.
Klik pada butang Code dan pilih Open with Codespaces.

Jika anda belum mempunyai Codespace, anda boleh menciptanya dengan klik New codespace.

**Nota** Memasang Persekitaran Node dalam Codespace anda
Menjalankan demo npm dari GitHub Codespace adalah cara yang hebat untuk menguji dan membangunkan projek anda. Berikut adalah panduan langkah demi langkah untuk membantu anda bermula:

### Sediakan Persekitaran Anda:
Setelah Codespace anda dibuka, pastikan anda mempunyai Node.js dan npm dipasang. Anda boleh memeriksanya dengan menjalankan:
```
node -v
```
```
npm -v
```

Jika ia tidak dipasang, anda boleh memasangnya menggunakan:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navigasi ke Direktori Projek Anda:
Gunakan terminal untuk menavigasi ke direktori di mana projek npm anda terletak:
```
cd path/to/your/project
```

### Pasang Kebergantungan:
Jalankan perintah berikut untuk memasang semua kebergantungan yang diperlukan yang disenaraikan dalam fail package.json anda:

```
npm install
```

### Jalankan Demo:
Setelah kebergantungan dipasang, anda boleh menjalankan skrip demo anda. Ini biasanya ditentukan dalam bahagian skrip dalam package.json anda. Sebagai contoh, jika skrip demo anda dinamakan start, anda boleh menjalankan:

```
npm run build
```
```
npm run dev
```

### Akses Demo:
Jika demo anda melibatkan pelayan web, Codespaces akan memberikan URL untuk mengaksesnya. Cari notifikasi atau periksa tab Ports untuk mencari URL tersebut.

**Nota:** Model perlu di-cache dalam pelayar, jadi ia mungkin mengambil sedikit masa untuk dimuatkan.

### Demo RAG
Muat naik fail markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Pilih Fail Anda:
Klik pada butang yang tertulis “Choose File” untuk memilih dokumen yang anda ingin muat naik.

### Muat Naik Dokumen:
Setelah memilih fail anda, klik butang “Upload” untuk memuat naik dokumen anda untuk RAG (Retrieval-Augmented Generation).

### Mulakan Sesi Chat Anda:
Setelah dokumen dimuat naik, anda boleh memulakan sesi chat menggunakan RAG berdasarkan kandungan dokumen anda.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.