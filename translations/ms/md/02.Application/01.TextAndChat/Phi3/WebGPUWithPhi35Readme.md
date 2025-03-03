# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo untuk Memperkenalkan WebGPU dan Corak RAG

Corak RAG dengan model Phi-3.5 Onnx Hosted menggunakan pendekatan Retrieval-Augmented Generation, menggabungkan kekuatan model Phi-3.5 dengan hosting ONNX untuk penerapan AI yang efisien. Corak ini sangat berguna untuk memperhalusi model bagi tugas-tugas khusus domain, menawarkan gabungan kualiti, keberkesanan kos, dan pemahaman konteks panjang. Ia adalah sebahagian daripada suite Azure AI, menyediakan pelbagai pilihan model yang mudah ditemui, dicuba, dan digunakan, memenuhi keperluan penyesuaian untuk pelbagai industri.

## Apa itu WebGPU 
WebGPU adalah API grafik web moden yang direka untuk memberikan akses efisien kepada unit pemprosesan grafik (GPU) peranti secara langsung dari pelayar web. Ia bertujuan menggantikan WebGL, dengan menawarkan beberapa peningkatan utama:

1. **Keserasian dengan GPU Moden**: WebGPU dibina untuk berfungsi dengan lancar dengan seni bina GPU terkini, menggunakan API sistem seperti Vulkan, Metal, dan Direct3D 12.
2. **Prestasi yang Dipertingkatkan**: Ia menyokong pengiraan GPU tujuan umum dan operasi yang lebih pantas, menjadikannya sesuai untuk rendering grafik dan tugas pembelajaran mesin.
3. **Ciri Lanjutan**: WebGPU menyediakan akses kepada keupayaan GPU yang lebih canggih, membolehkan kerja grafik dan pengiraan yang lebih kompleks dan dinamik.
4. **Beban Kerja JavaScript yang Berkurang**: Dengan memindahkan lebih banyak tugas kepada GPU, WebGPU secara signifikan mengurangkan beban kerja pada JavaScript, menghasilkan prestasi yang lebih baik dan pengalaman yang lebih lancar.

WebGPU kini disokong dalam pelayar seperti Google Chrome, dengan usaha berterusan untuk memperluaskan sokongan ke platform lain.

### 03.WebGPU
Persekitaran Diperlukan:

**Pelayar yang disokong:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Aktifkan WebGPU:

- Dalam Chrome/Microsoft Edge 

Aktifkan bendera `chrome://flags/#enable-unsafe-webgpu`.

#### Buka Pelayar Anda:
Lancarkan Google Chrome atau Microsoft Edge.

#### Akses Halaman Flags:
Di bar alamat, taipkan `chrome://flags` dan tekan Enter.

#### Cari Bendera:
Di kotak carian di bahagian atas halaman, taipkan 'enable-unsafe-webgpu'

#### Aktifkan Bendera:
Cari bendera #enable-unsafe-webgpu dalam senarai hasil.

Klik menu dropdown di sebelahnya dan pilih Enabled.

#### Mulakan Semula Pelayar Anda:

Selepas mengaktifkan bendera, anda perlu mulakan semula pelayar anda untuk perubahan berkuat kuasa. Klik butang Relaunch yang muncul di bahagian bawah halaman.

- Untuk Linux, lancarkan pelayar dengan `--enable-features=Vulkan`.
- Safari 18 (macOS 15) mempunyai WebGPU yang diaktifkan secara lalai.
- Dalam Firefox Nightly, masukkan about:config di bar alamat dan `set dom.webgpu.enabled to true`.

### Menyediakan GPU untuk Microsoft Edge 

Berikut adalah langkah-langkah untuk menyediakan GPU berprestasi tinggi untuk Microsoft Edge pada Windows:

- **Buka Tetapan:** Klik pada menu Mula dan pilih Tetapan.
- **Tetapan Sistem:** Pergi ke Sistem dan kemudian Paparan.
- **Tetapan Grafik:** Tatal ke bawah dan klik pada tetapan Grafik.
- **Pilih Aplikasi:** Di bawah “Pilih aplikasi untuk menetapkan keutamaan,” pilih aplikasi Desktop dan kemudian Semak Imbas.
- **Pilih Edge:** Navigasi ke folder pemasangan Edge (biasanya `C:\Program Files (x86)\Microsoft\Edge\Application`) dan pilih `msedge.exe`.
- **Tetapkan Keutamaan:** Klik Pilihan, pilih Prestasi Tinggi, dan kemudian klik Simpan.
Ini akan memastikan bahawa Microsoft Edge menggunakan GPU berprestasi tinggi anda untuk prestasi yang lebih baik. 
- **Mulakan Semula** mesin anda untuk tetapan ini berkuat kuasa.

### Sampel: Sila [klik pautan ini](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.