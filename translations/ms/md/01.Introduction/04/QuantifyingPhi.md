# **Mengkuantifikasi Keluarga Phi**

Pengkuantifikasian model merujuk kepada proses memetakan parameter (seperti berat dan nilai pengaktifan) dalam model rangkaian neural dari julat nilai yang besar (biasanya julat nilai berterusan) kepada julat nilai terhingga yang lebih kecil. Teknologi ini dapat mengurangkan saiz dan kerumitan pengiraan model serta meningkatkan kecekapan operasi model dalam persekitaran dengan sumber yang terhad seperti peranti mudah alih atau sistem tertanam. Pengkuantifikasian model mencapai pemampatan dengan mengurangkan ketepatan parameter, tetapi ia juga memperkenalkan sedikit kehilangan ketepatan. Oleh itu, dalam proses pengkuantifikasian, adalah perlu untuk mengimbangi saiz model, kerumitan pengiraan, dan ketepatan. Kaedah pengkuantifikasian yang biasa termasuk pengkuantifikasian titik tetap, pengkuantifikasian titik terapung, dan lain-lain. Anda boleh memilih strategi pengkuantifikasian yang sesuai mengikut senario dan keperluan tertentu.

Kami berharap untuk menerapkan model GenAI pada peranti tepi dan membolehkan lebih banyak peranti memasuki senario GenAI, seperti peranti mudah alih, AI PC/Copilot+PC, dan peranti IoT tradisional. Melalui model kuantifikasi, kita boleh menerapkannya pada peranti tepi yang berbeza berdasarkan jenis peranti. Digabungkan dengan rangka kerja pecutan model dan model kuantifikasi yang disediakan oleh pengeluar perkakasan, kita dapat membina senario aplikasi SLM yang lebih baik.

Dalam senario pengkuantifikasian, kita mempunyai pelbagai ketepatan (INT4, INT8, FP16, FP32). Berikut adalah penjelasan mengenai ketepatan pengkuantifikasian yang biasa digunakan:

### **INT4**

Pengkuantifikasian INT4 adalah kaedah pengkuantifikasian yang lebih radikal yang mengkuantifikasikan berat dan nilai pengaktifan model kepada integer 4-bit. Pengkuantifikasian INT4 biasanya mengakibatkan kehilangan ketepatan yang lebih besar disebabkan oleh julat perwakilan yang lebih kecil dan ketepatan yang lebih rendah. Walau bagaimanapun, berbanding dengan pengkuantifikasian INT8, pengkuantifikasian INT4 dapat mengurangkan lagi keperluan storan dan kerumitan pengiraan model. Perlu diingatkan bahawa pengkuantifikasian INT4 agak jarang digunakan dalam aplikasi praktikal, kerana ketepatan yang terlalu rendah boleh menyebabkan penurunan prestasi model yang ketara. Selain itu, tidak semua perkakasan menyokong operasi INT4, jadi keserasian perkakasan perlu dipertimbangkan semasa memilih kaedah pengkuantifikasian.

### **INT8**

Pengkuantifikasian INT8 adalah proses menukar berat dan pengaktifan model daripada nombor titik terapung kepada integer 8-bit. Walaupun julat nilai yang diwakili oleh integer INT8 lebih kecil dan kurang tepat, ia dapat mengurangkan keperluan storan dan pengiraan dengan ketara. Dalam pengkuantifikasian INT8, berat dan nilai pengaktifan model melalui proses pengkuantifikasian, termasuk penskalaan dan offset, untuk mengekalkan maklumat titik terapung asal sebanyak mungkin. Semasa inferens, nilai yang telah dikuantifikasi ini akan dinyahkuantifikasi kembali kepada nombor titik terapung untuk pengiraan, dan kemudian dikuantifikasi kembali kepada INT8 untuk langkah seterusnya. Kaedah ini dapat memberikan ketepatan yang mencukupi dalam kebanyakan aplikasi sambil mengekalkan kecekapan pengiraan yang tinggi.

### **FP16**

Format FP16, iaitu nombor titik terapung 16-bit (float16), mengurangkan jejak memori sebanyak separuh berbanding nombor titik terapung 32-bit (float32), yang mempunyai kelebihan yang ketara dalam aplikasi pembelajaran mendalam berskala besar. Format FP16 membolehkan pemuatan model yang lebih besar atau pemprosesan lebih banyak data dalam had memori GPU yang sama. Memandangkan perkakasan GPU moden terus menyokong operasi FP16, penggunaan format FP16 juga boleh membawa kepada peningkatan kelajuan pengiraan. Walau bagaimanapun, format FP16 juga mempunyai kelemahan tersendiri, iaitu ketepatan yang lebih rendah, yang boleh menyebabkan ketidakstabilan angka atau kehilangan ketepatan dalam beberapa kes.

### **FP32**

Format FP32 menyediakan ketepatan yang lebih tinggi dan dapat mewakili julat nilai yang luas dengan tepat. Dalam senario di mana operasi matematik kompleks dijalankan atau hasil dengan ketepatan tinggi diperlukan, format FP32 lebih disukai. Walau bagaimanapun, ketepatan tinggi juga bermaksud penggunaan memori yang lebih banyak dan masa pengiraan yang lebih lama. Untuk model pembelajaran mendalam berskala besar, terutamanya apabila terdapat banyak parameter model dan jumlah data yang besar, format FP32 boleh menyebabkan kekurangan memori GPU atau penurunan kelajuan inferens.

Pada peranti mudah alih atau peranti IoT, kita boleh menukar model Phi-3.x kepada INT4, manakala AI PC / Copilot PC boleh menggunakan ketepatan yang lebih tinggi seperti INT8, FP16, FP32.

Pada masa ini, pengeluar perkakasan yang berbeza mempunyai rangka kerja yang berbeza untuk menyokong model generatif, seperti OpenVINO daripada Intel, QNN daripada Qualcomm, MLX daripada Apple, dan CUDA daripada Nvidia, yang digabungkan dengan model kuantifikasi untuk melengkapkan pelaksanaan secara tempatan.

Dari segi teknologi, kami mempunyai sokongan format yang berbeza selepas pengkuantifikasian, seperti format PyTorch / Tensorflow, GGUF, dan ONNX. Saya telah melakukan perbandingan format dan senario aplikasi antara GGUF dan ONNX. Di sini saya mengesyorkan format kuantifikasi ONNX, yang mempunyai sokongan yang baik dari rangka kerja model hingga ke perkakasan. Dalam bab ini, kami akan memberi tumpuan kepada ONNX Runtime untuk GenAI, OpenVINO, dan Apple MLX untuk melaksanakan pengkuantifikasian model (jika anda mempunyai cara yang lebih baik, anda juga boleh memberikannya kepada kami dengan menghantar PR).

**Bab ini merangkumi**

1. [Mengkuantifikasi Phi-3.5 / 4 menggunakan llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Mengkuantifikasi Phi-3.5 / 4 menggunakan pelanjutan Generative AI untuk onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Mengkuantifikasi Phi-3.5 / 4 menggunakan Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Mengkuantifikasi Phi-3.5 / 4 menggunakan Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk memastikan ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.