# Selamat Datang ke Sambungan VS Code Anda

## Apa yang terdapat dalam folder ini

* Folder ini mengandungi semua fail yang diperlukan untuk sambungan anda.
* `package.json` - ini adalah fail manifest di mana anda mengisytiharkan sambungan dan arahan anda.
  * Plugin contoh mendaftarkan satu arahan dan menetapkan tajuk serta nama arahannya. Dengan maklumat ini, VS Code boleh memaparkan arahan dalam palet arahan. Ia belum lagi perlu memuatkan plugin tersebut.
* `src/extension.ts` - ini adalah fail utama di mana anda akan menyediakan pelaksanaan untuk arahan anda.
  * Fail ini mengeksport satu fungsi, `activate`, yang akan dipanggil kali pertama sambungan anda diaktifkan (dalam kes ini dengan melaksanakan arahan). Di dalam fungsi `activate`, kita memanggil `registerCommand`.
  * Kita menghantar fungsi yang mengandungi pelaksanaan arahan sebagai parameter kedua kepada `registerCommand`.

## Persediaan

* Pasang sambungan yang disyorkan (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dan dbaeumer.vscode-eslint)

## Mulakan dengan segera

* Tekan `F5` untuk membuka tetingkap baru dengan sambungan anda dimuatkan.
* Jalankan arahan anda dari palet arahan dengan menekan (`Ctrl+Shift+P` atau `Cmd+Shift+P` pada Mac) dan taipkan `Hello World`.
* Tetapkan breakpoint dalam kod anda di dalam `src/extension.ts` untuk menyahpepijat sambungan anda.
* Cari output daripada sambungan anda di konsol debug.

## Lakukan perubahan

* Anda boleh melancarkan semula sambungan dari toolbar debug selepas mengubah kod dalam `src/extension.ts`.
* Anda juga boleh memuat semula (`Ctrl+R` atau `Cmd+R` pada Mac) tetingkap VS Code dengan sambungan anda untuk memuatkan perubahan anda.

## Teroka API

* Anda boleh membuka keseluruhan set API kami apabila anda membuka fail `node_modules/@types/vscode/index.d.ts`.

## Jalankan ujian

* Pasang [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Jalankan tugas "watch" melalui arahan **Tasks: Run Task**. Pastikan ia sedang berjalan, jika tidak ujian mungkin tidak dapat dikesan.
* Buka paparan Testing dari bar aktiviti dan klik butang "Run Test", atau gunakan kekunci pintasan `Ctrl/Cmd + ; A`.
* Lihat output hasil ujian dalam paparan Test Results.
* Lakukan perubahan pada `src/test/extension.test.ts` atau cipta fail ujian baru di dalam folder `test`.
  * Pelari ujian yang disediakan hanya akan mempertimbangkan fail yang sepadan dengan corak nama `**.test.ts`.
  * Anda boleh mencipta folder di dalam folder `test` untuk menyusun ujian anda mengikut cara yang anda mahu.

## Melangkah lebih jauh

* Kurangkan saiz sambungan dan tingkatkan masa permulaan dengan [membundel sambungan anda](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Terbitkan sambungan anda](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) di pasaran sambungan VS Code.
* Automasi binaan dengan menyediakan [Integrasi Berterusan](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.