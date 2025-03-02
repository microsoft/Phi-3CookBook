# **Kuantifikasi Keluarga Phi**

Kuantifikasi model mengacu pada proses memetakan parameter (seperti bobot dan nilai aktivasi) dalam model jaringan neural dari rentang nilai yang besar (biasanya rentang nilai kontinu) ke rentang nilai yang lebih kecil dan terbatas. Teknologi ini dapat mengurangi ukuran dan kompleksitas komputasi model serta meningkatkan efisiensi operasional model di lingkungan dengan sumber daya terbatas seperti perangkat seluler atau sistem tertanam. Kuantifikasi model mencapai kompresi dengan mengurangi presisi parameter, tetapi ini juga dapat menyebabkan kehilangan presisi tertentu. Oleh karena itu, dalam proses kuantifikasi, perlu untuk menyeimbangkan antara ukuran model, kompleksitas komputasi, dan presisi. Metode kuantifikasi yang umum mencakup kuantisasi titik tetap, kuantisasi titik mengambang, dan lainnya. Anda dapat memilih strategi kuantifikasi yang sesuai berdasarkan skenario dan kebutuhan spesifik.

Kami berharap dapat menerapkan model GenAI ke perangkat edge dan memungkinkan lebih banyak perangkat masuk ke skenario GenAI, seperti perangkat seluler, AI PC/Copilot+PC, dan perangkat IoT tradisional. Melalui model kuantifikasi, kami dapat menerapkannya pada berbagai perangkat edge berdasarkan perangkat yang berbeda. Dikombinasikan dengan kerangka akselerasi model dan model kuantifikasi yang disediakan oleh produsen perangkat keras, kami dapat membangun skenario aplikasi SLM yang lebih baik.

Dalam skenario kuantifikasi, kami memiliki berbagai tingkat presisi (INT4, INT8, FP16, FP32). Berikut adalah penjelasan tentang tingkat presisi kuantifikasi yang umum digunakan:

### **INT4**

Kuantifikasi INT4 adalah metode kuantifikasi yang cukup radikal yang mengkuantisasi bobot dan nilai aktivasi model menjadi bilangan bulat 4-bit. Kuantifikasi INT4 biasanya menghasilkan kehilangan presisi yang lebih besar karena rentang representasi yang lebih kecil dan presisi yang lebih rendah. Namun, dibandingkan dengan kuantifikasi INT8, kuantifikasi INT4 dapat lebih jauh mengurangi kebutuhan penyimpanan dan kompleksitas komputasi model. Perlu dicatat bahwa kuantifikasi INT4 relatif jarang digunakan dalam aplikasi praktis, karena presisi yang terlalu rendah dapat menyebabkan penurunan kinerja model yang signifikan. Selain itu, tidak semua perangkat keras mendukung operasi INT4, sehingga kompatibilitas perangkat keras perlu dipertimbangkan saat memilih metode kuantifikasi.

### **INT8**

Kuantifikasi INT8 adalah proses mengubah bobot dan aktivasi model dari angka titik mengambang menjadi bilangan bulat 8-bit. Meskipun rentang nilai yang direpresentasikan oleh bilangan bulat INT8 lebih kecil dan kurang presisi, ini dapat secara signifikan mengurangi kebutuhan penyimpanan dan perhitungan. Dalam kuantifikasi INT8, bobot dan nilai aktivasi model melalui proses kuantifikasi, termasuk penskalaan dan offset, untuk mempertahankan informasi titik mengambang asli sebanyak mungkin. Selama inferensi, nilai-nilai yang telah dikuantisasi ini akan didekuantisasi kembali menjadi angka titik mengambang untuk perhitungan, dan kemudian dikuantisasi kembali ke INT8 untuk langkah berikutnya. Metode ini dapat memberikan presisi yang cukup dalam sebagian besar aplikasi sambil tetap menjaga efisiensi komputasi yang tinggi.

### **FP16**

Format FP16, yaitu bilangan titik mengambang 16-bit (float16), mengurangi jejak memori hingga setengah dibandingkan dengan bilangan titik mengambang 32-bit (float32), yang memiliki keuntungan signifikan dalam aplikasi pembelajaran mendalam skala besar. Format FP16 memungkinkan pemuatan model yang lebih besar atau pemrosesan lebih banyak data dalam batasan memori GPU yang sama. Karena perangkat keras GPU modern terus mendukung operasi FP16, menggunakan format FP16 juga dapat membawa peningkatan kecepatan komputasi. Namun, format FP16 juga memiliki kelemahan bawaan, yaitu presisi yang lebih rendah, yang dapat menyebabkan ketidakstabilan numerik atau kehilangan presisi dalam beberapa kasus.

### **FP32**

Format FP32 memberikan presisi yang lebih tinggi dan dapat merepresentasikan rentang nilai yang luas dengan akurat. Dalam skenario di mana operasi matematis kompleks dilakukan atau hasil presisi tinggi diperlukan, format FP32 lebih disukai. Namun, presisi tinggi juga berarti penggunaan memori yang lebih besar dan waktu perhitungan yang lebih lama. Untuk model pembelajaran mendalam skala besar, terutama ketika terdapat banyak parameter model dan jumlah data yang sangat besar, format FP32 dapat menyebabkan kekurangan memori GPU atau penurunan kecepatan inferensi.

Pada perangkat seluler atau perangkat IoT, kita dapat mengonversi model Phi-3.x ke INT4, sementara AI PC / Copilot PC dapat menggunakan presisi yang lebih tinggi seperti INT8, FP16, FP32.

Saat ini, produsen perangkat keras yang berbeda memiliki kerangka kerja yang berbeda untuk mendukung model generatif, seperti OpenVINO dari Intel, QNN dari Qualcomm, MLX dari Apple, dan CUDA dari Nvidia, yang dikombinasikan dengan model kuantifikasi untuk menyelesaikan penerapan lokal.

Dalam hal teknologi, kami memiliki dukungan format yang berbeda setelah kuantifikasi, seperti format PyTorch / Tensorflow, GGUF, dan ONNX. Saya telah melakukan perbandingan format dan skenario aplikasi antara GGUF dan ONNX. Di sini saya merekomendasikan format kuantifikasi ONNX, yang memiliki dukungan baik dari kerangka model hingga perangkat keras. Dalam bab ini, kami akan berfokus pada ONNX Runtime untuk GenAI, OpenVINO, dan Apple MLX untuk melakukan kuantifikasi model (jika Anda memiliki cara yang lebih baik, Anda juga dapat memberikannya kepada kami dengan mengirimkan PR).

**Bab ini mencakup**

1. [Mengkuantisasi Phi-3.5 / 4 menggunakan llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Mengkuantisasi Phi-3.5 / 4 menggunakan ekstensi Generative AI untuk onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Mengkuantisasi Phi-3.5 / 4 menggunakan Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Mengkuantisasi Phi-3.5 / 4 menggunakan Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan berbasis AI. Meskipun kami berupaya untuk memberikan hasil yang akurat, harap disadari bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.