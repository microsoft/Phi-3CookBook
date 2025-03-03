# Menyumbang

Projek ini mengalu-alukan sumbangan dan cadangan. Kebanyakan sumbangan memerlukan anda untuk bersetuju dengan Perjanjian Lesen Penyumbang (CLA) yang menyatakan bahawa anda mempunyai hak untuk, dan benar-benar memberi kami hak untuk menggunakan sumbangan anda. Untuk butiran lanjut, lawati [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Apabila anda menghantar permintaan tarik (pull request), bot CLA secara automatik akan menentukan sama ada anda perlu menyediakan CLA dan menghiasi PR dengan sewajarnya (contohnya, semakan status, komen). Ikuti sahaja arahan yang diberikan oleh bot tersebut. Anda hanya perlu melakukannya sekali untuk semua repositori yang menggunakan CLA kami.

## Kod Etika

Projek ini telah mengadaptasi [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Untuk maklumat lanjut, baca [Soalan Lazim Kod Etika](https://opensource.microsoft.com/codeofconduct/faq/) atau hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) jika anda mempunyai soalan atau komen tambahan.

## Berhati-hati Ketika Membuat Isu

Sila jangan buka isu GitHub untuk soalan sokongan umum kerana senarai GitHub seharusnya digunakan untuk permintaan ciri dan laporan pepijat. Dengan cara ini, kami dapat menjejaki isu atau pepijat sebenar daripada kod dan memisahkan perbincangan umum daripada kod sebenar.

## Cara Menyumbang

### Garis Panduan Permintaan Tarik

Apabila menghantar permintaan tarik (PR) ke repositori Phi-3 CookBook, sila gunakan garis panduan berikut:

- **Fork Repositori**: Sentiasa fork repositori ke akaun anda sendiri sebelum membuat pengubahsuaian.

- **Pisahkan permintaan tarik (PR)**:
  - Hantar setiap jenis perubahan dalam permintaan tarik yang berasingan. Sebagai contoh, pembaikan pepijat dan kemas kini dokumentasi hendaklah dihantar dalam PR yang berbeza.
  - Pembetulan kesalahan taip dan kemas kini dokumentasi kecil boleh digabungkan ke dalam satu PR jika sesuai.

- **Tangani konflik gabungan**: Jika PR anda menunjukkan konflik gabungan, kemas kini cawangan tempatan `main` anda supaya mencerminkan repositori utama sebelum membuat pengubahsuaian.

- **Penghantaran terjemahan**: Apabila menghantar PR terjemahan, pastikan folder terjemahan termasuk terjemahan untuk semua fail dalam folder asal.

### Garis Panduan Terjemahan

> [!IMPORTANT]
>
> Apabila menterjemah teks dalam repositori ini, jangan gunakan terjemahan mesin. Hanya sukarela untuk terjemahan dalam bahasa yang anda mahir.

Jika anda mahir dalam bahasa selain bahasa Inggeris, anda boleh membantu menterjemah kandungan. Ikuti langkah-langkah ini untuk memastikan sumbangan terjemahan anda diintegrasikan dengan betul, sila gunakan garis panduan berikut:

- **Cipta folder terjemahan**: Navigasi ke folder bahagian yang sesuai dan buat folder terjemahan untuk bahasa yang anda sumbangkan. Sebagai contoh:
  - Untuk bahagian pengenalan: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Untuk bahagian permulaan cepat: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Teruskan corak ini untuk bahagian lain (03.Inference, 04.Finetuning, dsb.)

- **Kemas kini laluan relatif**: Semasa menterjemah, sesuaikan struktur folder dengan menambah `../../` pada permulaan laluan relatif dalam fail markdown untuk memastikan pautan berfungsi dengan betul. Sebagai contoh, ubah seperti berikut:
  - Ubah `(../../imgs/01/phi3aisafety.png)` kepada `(../../../../imgs/01/phi3aisafety.png)`

- **Susun terjemahan anda**: Setiap fail yang diterjemahkan hendaklah diletakkan dalam folder terjemahan bahagian yang sepadan. Sebagai contoh, jika anda menterjemah bahagian pengenalan ke dalam bahasa Sepanyol, anda akan mencipta seperti berikut:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Hantar PR lengkap**: Pastikan semua fail yang diterjemahkan untuk satu bahagian disertakan dalam satu PR. Kami tidak menerima terjemahan separa untuk satu bahagian. Apabila menghantar PR terjemahan, pastikan folder terjemahan termasuk terjemahan untuk semua fail dalam folder asal.

### Garis Panduan Penulisan

Untuk memastikan konsistensi di seluruh dokumen, sila gunakan garis panduan berikut:

- **Pemformatan URL**: Bungkus semua URL dalam kurungan empat segi diikuti dengan kurungan bulat, tanpa ruang tambahan di sekeliling atau di dalamnya. Sebagai contoh: `[example](https://www.microsoft.com)`.

- **Pautan relatif**: Gunakan `./` untuk pautan relatif yang menunjuk kepada fail atau folder dalam direktori semasa, dan `../` untuk pautan dalam direktori induk. Sebagai contoh: `[example](../../path/to/file)` atau `[example](../../../path/to/file)`.

- **Bukan Lokasi Khusus Negara**: Pastikan pautan anda tidak termasuk lokasi khusus negara. Sebagai contoh, elakkan `/en-us/` atau `/en/`.

- **Penyimpanan imej**: Simpan semua imej dalam folder `./imgs`.

- **Nama imej deskriptif**: Namakan imej dengan deskriptif menggunakan aksara Inggeris, nombor, dan tanda sengkang. Sebagai contoh: `example-image.jpg`.

## Alur Kerja GitHub

Apabila anda menghantar permintaan tarik, alur kerja berikut akan dicetuskan untuk mengesahkan perubahan. Ikuti arahan di bawah untuk memastikan permintaan tarik anda lulus semakan alur kerja:

- [Semak Laluan Relatif yang Rosak](../..)
- [Semak URL Tidak Mengandungi Lokasi](../..)

### Semak Laluan Relatif yang Rosak

Alur kerja ini memastikan semua laluan relatif dalam fail anda adalah betul.

1. Untuk memastikan pautan anda berfungsi dengan betul, lakukan tugas berikut menggunakan VS Code:
    - Arahkan kursor pada mana-mana pautan dalam fail anda.
    - Tekan **Ctrl + Klik** untuk navigasi ke pautan.
    - Jika anda klik pada pautan dan ia tidak berfungsi secara tempatan, ia akan mencetuskan alur kerja dan tidak berfungsi di GitHub.

1. Untuk membetulkan isu ini, lakukan tugas berikut menggunakan cadangan laluan yang diberikan oleh VS Code:
    - Taip `./` atau `../`.
    - VS Code akan memberi anda pilihan berdasarkan apa yang anda taip.
    - Ikuti laluan dengan mengklik pada fail atau folder yang dikehendaki untuk memastikan laluan anda betul.

Setelah anda menambah laluan relatif yang betul, simpan dan tolak perubahan anda.

### Semak URL Tidak Mengandungi Lokasi

Alur kerja ini memastikan bahawa mana-mana URL web tidak termasuk lokasi khusus negara. Oleh kerana repositori ini boleh diakses secara global, adalah penting untuk memastikan URL tidak mengandungi lokasi negara anda.

1. Untuk mengesahkan bahawa URL anda tidak mempunyai lokasi negara, lakukan tugas berikut:

    - Periksa teks seperti `/en-us/`, `/en/`, atau mana-mana lokasi bahasa lain dalam URL.
    - Jika ini tidak ada dalam URL anda, maka anda akan lulus semakan ini.

1. Untuk membetulkan isu ini, lakukan tugas berikut:
    - Buka laluan fail yang diserlahkan oleh alur kerja.
    - Alih keluar lokasi negara daripada URL.

Setelah anda menghapuskan lokasi negara, simpan dan tolak perubahan anda.

### Semak URL yang Rosak

Alur kerja ini memastikan bahawa mana-mana URL web dalam fail anda berfungsi dan mengembalikan kod status 200.

1. Untuk mengesahkan bahawa URL anda berfungsi dengan betul, lakukan tugas berikut:
    - Periksa status URL dalam fail anda.

2. Untuk membetulkan mana-mana URL yang rosak, lakukan tugas berikut:
    - Buka fail yang mengandungi URL yang rosak.
    - Kemas kini URL kepada yang betul.

Setelah anda membetulkan URL, simpan dan tolak perubahan anda.

> [!NOTE]
>
> Mungkin ada kes di mana semakan URL gagal walaupun pautan boleh diakses. Ini boleh berlaku atas beberapa sebab, termasuk:
>
> - **Sekatan rangkaian:** Pelayan tindakan GitHub mungkin mempunyai sekatan rangkaian yang menghalang akses kepada URL tertentu.
> - **Isu tamat masa:** URL yang mengambil masa terlalu lama untuk memberi respons mungkin mencetuskan ralat tamat masa dalam alur kerja.
> - **Isu pelayan sementara:** Masa henti pelayan atau penyelenggaraan sementara boleh menyebabkan URL tidak tersedia buat sementara waktu semasa pengesahan.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.