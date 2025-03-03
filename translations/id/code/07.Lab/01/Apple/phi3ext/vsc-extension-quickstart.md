# Selamat Datang di Ekstensi VS Code Anda

## Apa Saja yang Ada di Folder Ini

* Folder ini berisi semua file yang diperlukan untuk ekstensi Anda.
* `package.json` - ini adalah file manifest tempat Anda mendeklarasikan ekstensi dan perintah Anda.
  * Plugin contoh ini mendaftarkan sebuah perintah dan mendefinisikan judul serta nama perintahnya. Dengan informasi ini, VS Code dapat menampilkan perintah di palet perintah. Plugin ini belum perlu dimuat oleh VS Code.
* `src/extension.ts` - ini adalah file utama tempat Anda menyediakan implementasi perintah Anda.
  * File ini mengekspor satu fungsi, `activate`, yang dipanggil saat pertama kali ekstensi Anda diaktifkan (dalam hal ini dengan menjalankan perintah). Di dalam fungsi `activate`, kita memanggil `registerCommand`.
  * Kita meneruskan fungsi yang berisi implementasi perintah sebagai parameter kedua ke `registerCommand`.

## Pengaturan

* Instal ekstensi yang direkomendasikan (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dan dbaeumer.vscode-eslint)

## Langsung Mulai

* Tekan `F5` untuk membuka jendela baru dengan ekstensi Anda yang sudah dimuat.
* Jalankan perintah Anda dari palet perintah dengan menekan (`Ctrl+Shift+P` atau `Cmd+Shift+P` di Mac) dan mengetikkan `Hello World`.
* Tetapkan breakpoint di kode Anda di dalam `src/extension.ts` untuk melakukan debugging ekstensi Anda.
* Temukan output dari ekstensi Anda di konsol debug.

## Lakukan Perubahan

* Anda dapat meluncurkan ulang ekstensi dari toolbar debug setelah mengubah kode di `src/extension.ts`.
* Anda juga dapat memuat ulang (`Ctrl+R` atau `Cmd+R` di Mac) jendela VS Code dengan ekstensi Anda untuk memuat perubahan.

## Jelajahi API

* Anda dapat membuka seluruh set API kami dengan membuka file `node_modules/@types/vscode/index.d.ts`.

## Jalankan Tes

* Instal [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Jalankan tugas "watch" melalui perintah **Tasks: Run Task**. Pastikan ini berjalan, jika tidak, tes mungkin tidak terdeteksi.
* Buka tampilan Testing dari bilah aktivitas dan klik tombol "Run Test", atau gunakan hotkey `Ctrl/Cmd + ; A`
* Lihat output hasil tes di tampilan Test Results.
* Lakukan perubahan pada `src/test/extension.test.ts` atau buat file tes baru di dalam folder `test`.
  * Test runner yang disediakan hanya akan mempertimbangkan file yang sesuai dengan pola nama `**.test.ts`.
  * Anda dapat membuat folder di dalam folder `test` untuk menyusun tes Anda sesuai keinginan.

## Lanjutkan Lebih Jauh

* Kurangi ukuran ekstensi dan tingkatkan waktu startup dengan [membundel ekstensi Anda](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publikasikan ekstensi Anda](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) di marketplace ekstensi VS Code.
* Otomatiskan proses build dengan menyiapkan [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.