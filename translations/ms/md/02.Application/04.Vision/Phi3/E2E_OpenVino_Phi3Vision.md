Demo ini menunjukkan cara menggunakan model pra-latih untuk menghasilkan kod Python berdasarkan imej dan teks arahan.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Berikut adalah penjelasan langkah demi langkah:

1. **Imports dan Persediaan**:
   - Pustaka dan modul yang diperlukan diimport, termasuk `requests`, `PIL` untuk pemprosesan imej, dan `transformers` untuk mengendalikan model dan pemprosesan.

2. **Memuat dan Memaparkan Imej**:
   - Fail imej (`demo.png`) dibuka menggunakan pustaka `PIL` dan dipaparkan.

3. **Mendefinisikan Arahan**:
   - Mesej dicipta yang merangkumi imej dan permintaan untuk menghasilkan kod Python bagi memproses imej tersebut dan menyimpannya menggunakan `plt` (matplotlib).

4. **Memuat Pemproses**:
   - `AutoProcessor` dimuatkan daripada model pra-latih yang ditentukan oleh direktori `out_dir`. Pemproses ini akan mengendalikan input teks dan imej.

5. **Mencipta Arahan**:
   - Kaedah `apply_chat_template` digunakan untuk memformat mesej ke dalam arahan yang sesuai untuk model.

6. **Memproses Input**:
   - Arahan dan imej diproses menjadi tensor yang boleh difahami oleh model.

7. **Menetapkan Argumen Penjanaan**:
   - Argumen untuk proses penjanaan model ditentukan, termasuk bilangan maksimum token baru yang akan dihasilkan dan sama ada untuk mengambil sampel output.

8. **Menjana Kod**:
   - Model menghasilkan kod Python berdasarkan input dan argumen penjanaan. `TextStreamer` digunakan untuk mengendalikan output, dengan mengabaikan arahan dan token khas.

9. **Output**:
   - Kod yang dihasilkan dicetak, yang sepatutnya merangkumi kod Python untuk memproses imej dan menyimpannya seperti yang dinyatakan dalam arahan.

Demo ini menunjukkan bagaimana memanfaatkan model pra-latih menggunakan OpenVino untuk menjana kod secara dinamik berdasarkan input pengguna dan imej.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.