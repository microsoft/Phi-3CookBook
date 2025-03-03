# Selamat Datang di Ekstensi VS Code Anda

## Apa yang ada di folder ini

* Folder ini berisi semua file yang diperlukan untuk ekstensi Anda.
* `package.json` - ini adalah file manifest di mana Anda mendeklarasikan ekstensi dan perintah Anda.
  * Plugin contoh mendaftarkan sebuah perintah dan mendefinisikan judul serta nama perintahnya. Dengan informasi ini, VS Code dapat menampilkan perintah di palet perintah. Plugin ini belum perlu dimuat.
* `src/extension.ts` - ini adalah file utama tempat Anda akan menyediakan implementasi perintah Anda.
  * File ini mengekspor satu fungsi, `activate`, yang dipanggil pertama kali saat ekstensi Anda diaktifkan (dalam hal ini dengan mengeksekusi perintah). Di dalam fungsi `activate`, kita memanggil `registerCommand`.
  * Kita mengoper fungsi yang berisi implementasi perintah sebagai parameter kedua ke `registerCommand`.

## Persiapan

* Instal ekstensi yang direkomendasikan (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dan dbaeumer.vscode-eslint).

## Langsung Mulai

* Tekan `F5` untuk membuka jendela baru dengan ekstensi Anda dimuat.
* Jalankan perintah Anda dari palet perintah dengan menekan (`Ctrl+Shift+P` atau `Cmd+Shift+P` di Mac) dan mengetikkan `Hello World`.
* Tetapkan breakpoint di kode Anda di dalam `src/extension.ts` untuk men-debug ekstensi Anda.
* Temukan output dari ekstensi Anda di konsol debug.

## Lakukan Perubahan

* Anda dapat memuat ulang ekstensi dari toolbar debug setelah mengubah kode di `src/extension.ts`.
* Anda juga dapat memuat ulang (`Ctrl+R` atau `Cmd+R` di Mac) jendela VS Code dengan ekstensi Anda untuk memuat perubahan Anda.

## Jelajahi API

* Anda dapat membuka seluruh set API kami saat Anda membuka file `node_modules/@types/vscode/index.d.ts`.

## Jalankan Tes

* Instal [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Jalankan tugas "watch" melalui perintah **Tasks: Run Task**. Pastikan ini berjalan, atau tes mungkin tidak terdeteksi.
* Buka tampilan Testing dari bilah aktivitas dan klik tombol "Run Test", atau gunakan hotkey `Ctrl/Cmd + ; A`.
* Lihat output hasil tes di tampilan Test Results.
* Lakukan perubahan pada `src/test/extension.test.ts` atau buat file tes baru di dalam folder `test`.
  * Test runner yang disediakan hanya akan mempertimbangkan file yang sesuai dengan pola nama `**.test.ts`.
  * Anda dapat membuat folder di dalam folder `test` untuk mengatur tes Anda sesuai keinginan.

## Langkah Lebih Lanjut

* Kurangi ukuran ekstensi dan tingkatkan waktu startup dengan [membundel ekstensi Anda](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publikasikan ekstensi Anda](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) di marketplace ekstensi VS Code.
* Otomatiskan proses build dengan mengatur [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.