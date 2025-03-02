# Berkontribusi

Proyek ini menyambut kontribusi dan saran. Sebagian besar kontribusi mengharuskan Anda menyetujui Contributor License Agreement (CLA) yang menyatakan bahwa Anda memiliki hak, dan benar-benar memberikan kami hak untuk menggunakan kontribusi Anda. Untuk detailnya, kunjungi [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Ketika Anda mengirimkan pull request, bot CLA secara otomatis akan menentukan apakah Anda perlu menyediakan CLA dan menandai PR Anda dengan tepat (misalnya, status cek, komentar). Cukup ikuti instruksi yang diberikan oleh bot tersebut. Anda hanya perlu melakukannya satu kali di semua repositori yang menggunakan CLA kami.

## Kode Etik

Proyek ini telah mengadopsi [Kode Etik Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/).  
Untuk informasi lebih lanjut, baca [FAQ Kode Etik](https://opensource.microsoft.com/codeofconduct/faq/) atau hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) jika ada pertanyaan atau komentar tambahan.

## Peringatan untuk Membuat Isu

Jangan buka isu di GitHub untuk pertanyaan dukungan umum karena daftar GitHub harus digunakan untuk permintaan fitur dan laporan bug. Dengan cara ini, kami dapat lebih mudah melacak masalah atau bug sebenarnya dari kode dan menjaga diskusi umum terpisah dari kode aktual.

## Cara Berkontribusi

### Panduan Pull Request

Saat mengirimkan pull request (PR) ke repositori Phi-3 CookBook, harap ikuti panduan berikut:

- **Fork Repositori**: Selalu fork repositori ke akun Anda sendiri sebelum melakukan modifikasi.

- **Pisahkan pull request (PR)**:
  - Kirim setiap jenis perubahan dalam PR yang terpisah. Misalnya, perbaikan bug dan pembaruan dokumentasi harus dikirimkan dalam PR yang terpisah.
  - Perbaikan typo dan pembaruan dokumentasi kecil dapat digabungkan dalam satu PR jika sesuai.

- **Tangani konflik merge**: Jika pull request Anda menunjukkan konflik merge, perbarui cabang lokal `main` Anda agar mencerminkan repositori utama sebelum melakukan modifikasi.

- **Pengiriman terjemahan**: Saat mengirimkan PR terjemahan, pastikan folder terjemahan mencakup terjemahan untuk semua file di folder asli.

### Panduan Terjemahan

> [!IMPORTANT]
>
> Saat menerjemahkan teks dalam repositori ini, jangan gunakan terjemahan mesin. Hanya sukarelawan yang fasih dalam bahasa yang bersangkutan yang boleh menerjemahkan.

Jika Anda fasih dalam bahasa non-Inggris, Anda dapat membantu menerjemahkan konten. Ikuti langkah-langkah berikut untuk memastikan kontribusi terjemahan Anda terintegrasi dengan benar, gunakan panduan berikut:

- **Buat folder terjemahan**: Arahkan ke folder bagian yang sesuai dan buat folder terjemahan untuk bahasa yang Anda kontribusikan. Contoh:
  - Untuk bagian pengenalan: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - Untuk bagian panduan cepat: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Lanjutkan pola ini untuk bagian lainnya (03.Inference, 04.Finetuning, dll.)

- **Perbarui jalur relatif**: Saat menerjemahkan, sesuaikan struktur folder dengan menambahkan `../../` ke awal jalur relatif dalam file markdown untuk memastikan tautan berfungsi dengan benar. Contoh:
  - Ubah `(../../imgs/01/phi3aisafety.png)` menjadi `(../../../../imgs/01/phi3aisafety.png)`

- **Organisasikan terjemahan Anda**: Setiap file yang diterjemahkan harus ditempatkan di folder terjemahan bagian yang sesuai. Contoh, jika Anda menerjemahkan bagian pengenalan ke dalam bahasa Spanyol, Anda akan membuat sebagai berikut:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Kirimkan PR lengkap**: Pastikan semua file yang diterjemahkan untuk sebuah bagian disertakan dalam satu PR. Kami tidak menerima terjemahan parsial untuk sebuah bagian. Saat mengirimkan PR terjemahan, pastikan folder terjemahan mencakup terjemahan untuk semua file di folder asli.

### Panduan Penulisan

Untuk memastikan konsistensi di semua dokumen, gunakan panduan berikut:

- **Format URL**: Bungkus semua URL dalam tanda kurung siku diikuti dengan tanda kurung, tanpa spasi tambahan di sekitar atau di dalamnya. Contoh: `[example](https://example.com)`.

- **Tautan relatif**: Gunakan `./` untuk tautan relatif yang menunjuk ke file atau folder di direktori saat ini, dan `../` untuk yang ada di direktori induk. Contoh: `[example](../../path/to/file)` atau `[example](../../../path/to/file)`.

- **Tidak ada lokal khusus negara**: Pastikan tautan Anda tidak menyertakan lokal khusus negara. Contoh, hindari `/en-us/` atau `/en/`.

- **Penyimpanan gambar**: Simpan semua gambar di folder `./imgs`.

- **Nama gambar deskriptif**: Beri nama gambar secara deskriptif menggunakan karakter Inggris, angka, dan tanda hubung. Contoh: `example-image.jpg`.

## Alur Kerja GitHub

Saat Anda mengirimkan pull request, alur kerja berikut akan dipicu untuk memvalidasi perubahan. Ikuti instruksi di bawah ini untuk memastikan pull request Anda lulus pemeriksaan alur kerja:

- [Periksa Jalur Relatif yang Rusak](../..)
- [Periksa URL Tidak Memiliki Lokal](../..)

### Periksa Jalur Relatif yang Rusak

Alur kerja ini memastikan bahwa semua jalur relatif dalam file Anda benar.

1. Untuk memastikan tautan Anda berfungsi dengan benar, lakukan tugas berikut menggunakan VS Code:
    - Arahkan kursor ke tautan mana pun di file Anda.
    - Tekan **Ctrl + Klik** untuk menavigasi ke tautan tersebut.
    - Jika Anda mengklik tautan dan itu tidak berfungsi secara lokal, alur kerja akan memicu dan tidak berfungsi di GitHub.

1. Untuk memperbaiki masalah ini, lakukan tugas berikut menggunakan saran jalur yang disediakan oleh VS Code:
    - Ketik `./` atau `../`.
    - VS Code akan meminta Anda memilih dari opsi yang tersedia berdasarkan apa yang Anda ketik.
    - Ikuti jalur dengan mengklik file atau folder yang diinginkan untuk memastikan jalur Anda benar.

Setelah Anda menambahkan jalur relatif yang benar, simpan dan push perubahan Anda.

### Periksa URL Tidak Memiliki Lokal

Alur kerja ini memastikan bahwa URL web apa pun tidak menyertakan lokal khusus negara. Karena repositori ini dapat diakses secara global, penting untuk memastikan bahwa URL tidak mengandung lokal negara Anda.

1. Untuk memverifikasi bahwa URL Anda tidak memiliki lokal negara, lakukan tugas berikut:

    - Periksa teks seperti `/en-us/`, `/en/`, atau lokal bahasa lain dalam URL.
    - Jika ini tidak ada di URL Anda, maka Anda akan lulus pemeriksaan ini.

1. Untuk memperbaiki masalah ini, lakukan tugas berikut:
    - Buka jalur file yang disorot oleh alur kerja.
    - Hapus lokal negara dari URL.

Setelah Anda menghapus lokal negara, simpan dan push perubahan Anda.

### Periksa URL yang Rusak

Alur kerja ini memastikan bahwa URL web apa pun dalam file Anda berfungsi dan mengembalikan kode status 200.

1. Untuk memverifikasi bahwa URL Anda berfungsi dengan benar, lakukan tugas berikut:
    - Periksa status URL dalam file Anda.

2. Untuk memperbaiki URL yang rusak, lakukan tugas berikut:
    - Buka file yang berisi URL yang rusak.
    - Perbarui URL ke yang benar.

Setelah Anda memperbaiki URL, simpan dan push perubahan Anda.

> [!NOTE]
>
> Mungkin ada kasus di mana pemeriksaan URL gagal meskipun tautan dapat diakses. Hal ini dapat terjadi karena beberapa alasan, termasuk:
>
> - **Pembatasan jaringan:** Server GitHub Actions mungkin memiliki pembatasan jaringan yang mencegah akses ke URL tertentu.
> - **Masalah waktu habis:** URL yang membutuhkan waktu terlalu lama untuk merespons dapat memicu kesalahan waktu habis dalam alur kerja.
> - **Masalah server sementara:** Downtime server atau pemeliharaan sesekali dapat membuat URL sementara tidak tersedia selama validasi.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.