Demo ini menunjukkan cara menggunakan model yang telah dilatih sebelumnya untuk menghasilkan kode Python berdasarkan sebuah gambar dan teks perintah.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Berikut adalah penjelasan langkah demi langkah:

1. **Impor dan Persiapan**:
   - Pustaka dan modul yang diperlukan diimpor, termasuk `requests`, `PIL` untuk pemrosesan gambar, dan `transformers` untuk menangani model dan pemrosesan.

2. **Memuat dan Menampilkan Gambar**:
   - Sebuah file gambar (`demo.png`) dibuka menggunakan pustaka `PIL` dan ditampilkan.

3. **Mendefinisikan Prompt**:
   - Sebuah pesan dibuat yang mencakup gambar dan permintaan untuk menghasilkan kode Python guna memproses gambar dan menyimpannya menggunakan `plt` (matplotlib).

4. **Memuat Processor**:
   - `AutoProcessor` dimuat dari model yang telah dilatih sebelumnya yang ditentukan oleh direktori `out_dir`. Processor ini akan menangani input teks dan gambar.

5. **Membuat Prompt**:
   - Metode `apply_chat_template` digunakan untuk memformat pesan menjadi prompt yang sesuai untuk model.

6. **Memproses Input**:
   - Prompt dan gambar diproses menjadi tensor yang dapat dipahami oleh model.

7. **Menetapkan Argumen Generasi**:
   - Argumen untuk proses generasi model didefinisikan, termasuk jumlah maksimum token baru yang akan dihasilkan dan apakah akan menggunakan sampling pada output.

8. **Menghasilkan Kode**:
   - Model menghasilkan kode Python berdasarkan input dan argumen generasi. `TextStreamer` digunakan untuk menangani output, melewati prompt dan token khusus.

9. **Output**:
   - Kode yang dihasilkan dicetak, yang seharusnya mencakup kode Python untuk memproses gambar dan menyimpannya sesuai dengan permintaan dalam prompt.

Demo ini menunjukkan bagaimana memanfaatkan model yang telah dilatih sebelumnya menggunakan OpenVino untuk menghasilkan kode secara dinamis berdasarkan input pengguna dan gambar.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.