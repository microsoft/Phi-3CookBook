# Selamat Datang ke Sambungan VS Code Anda

## Apa yang Ada dalam Folder Ini

* Folder ini mengandungi semua fail yang diperlukan untuk sambungan anda.
* `package.json` - ini adalah fail manifest di mana anda mengisytiharkan sambungan dan arahan anda.
  * Plugin contoh mendaftarkan satu arahan dan menentukan tajuk serta nama arahannya. Dengan maklumat ini, VS Code boleh memaparkan arahan tersebut dalam palet arahan. Plugin ini belum perlu dimuatkan lagi.
* `src/extension.ts` - ini adalah fail utama di mana anda akan menyediakan pelaksanaan arahan anda.
  * Fail ini mengeksport satu fungsi, `activate`, yang dipanggil kali pertama sambungan anda diaktifkan (dalam kes ini dengan melaksanakan arahan). Di dalam fungsi `activate`, kami memanggil `registerCommand`.
  * Kami menghantar fungsi yang mengandungi pelaksanaan arahan sebagai parameter kedua kepada `registerCommand`.

## Persediaan

* Pasang sambungan yang disyorkan (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dan dbaeumer.vscode-eslint)

## Mulakan Segera

* Tekan `F5` untuk membuka tetingkap baru dengan sambungan anda dimuatkan.
* Jalankan arahan anda dari palet arahan dengan menekan (`Ctrl+Shift+P` atau `Cmd+Shift+P` pada Mac) dan menaip `Hello World`.
* Tetapkan breakpoint dalam kod anda di dalam `src/extension.ts` untuk menyahpepijat sambungan anda.
* Cari output daripada sambungan anda dalam konsol debug.

## Lakukan Perubahan

* Anda boleh melancarkan semula sambungan daripada bar alat debug selepas membuat perubahan pada kod dalam `src/extension.ts`.
* Anda juga boleh memuat semula (`Ctrl+R` atau `Cmd+R` pada Mac) tetingkap VS Code dengan sambungan anda untuk memuatkan perubahan anda.

## Terokai API

* Anda boleh membuka keseluruhan set API kami apabila anda membuka fail `node_modules/@types/vscode/index.d.ts`.

## Jalankan Ujian

* Pasang [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Jalankan tugas "watch" melalui perintah **Tasks: Run Task**. Pastikan ini sedang berjalan, jika tidak, ujian mungkin tidak ditemui.
* Buka paparan Testing dari bar aktiviti dan klik butang "Run Test", atau gunakan kekunci pintasan `Ctrl/Cmd + ; A`.
* Lihat output hasil ujian dalam paparan Test Results.
* Buat perubahan pada `src/test/extension.test.ts` atau buat fail ujian baru di dalam folder `test`.
  * Test runner yang disediakan hanya akan mempertimbangkan fail yang sepadan dengan corak nama `**.test.ts`.
  * Anda boleh membuat folder di dalam folder `test` untuk menyusun ujian anda mengikut cara yang anda inginkan.

## Pergi Lebih Jauh

* Kurangkan saiz sambungan dan tingkatkan masa permulaan dengan [menggabungkan sambungan anda](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Terbitkan sambungan anda](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) di pasaran sambungan VS Code.
* Automasi binaan dengan menyediakan [Integrasi Berterusan](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berautoriti. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.