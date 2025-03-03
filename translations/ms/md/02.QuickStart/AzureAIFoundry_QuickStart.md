# **Menggunakan Phi-3 di Azure AI Foundry**

Dengan perkembangan Generative AI, kami berharap dapat menggunakan platform terpadu untuk mengelola berbagai LLM dan SLM, integrasi data perusahaan, operasi fine-tuning/RAG, serta evaluasi berbagai bisnis perusahaan setelah integrasi LLM dan SLM, sehingga aplikasi AI generatif dapat diimplementasikan dengan lebih cerdas. [Azure AI Foundry](https://ai.azure.com) adalah platform aplikasi AI generatif tingkat perusahaan.

![aistudo](../../../../translated_images/aifoundry_home.ffa4fe13d11f26171097f8666a1db96ac0979ffa1adde80374c60d1136c7e1de.ms.png)

Dengan Azure AI Foundry, Anda dapat mengevaluasi respons model bahasa besar (LLM) dan mengorkestrasi komponen aplikasi prompt dengan prompt flow untuk kinerja yang lebih baik. Platform ini mempermudah skalabilitas untuk mengubah bukti konsep menjadi produksi penuh dengan mudah. Pemantauan dan penyempurnaan berkelanjutan mendukung keberhasilan jangka panjang.

Kita dapat dengan cepat menerapkan model Phi-3 di Azure AI Foundry melalui langkah-langkah sederhana, lalu menggunakan Azure AI Foundry untuk menyelesaikan pekerjaan terkait Phi-3 seperti Playground/Chat, Fine-tuning, evaluasi, dan lainnya.

## **1. Persiapan**

Jika Anda sudah menginstal [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) di perangkat Anda, menggunakan template ini semudah menjalankan perintah ini di direktori baru.

## Pembuatan Manual

Membuat proyek dan hub Microsoft Azure AI Foundry adalah cara yang baik untuk mengatur dan mengelola pekerjaan AI Anda. Berikut panduan langkah demi langkah untuk memulai:

### Membuat Proyek di Azure AI Foundry

1. **Buka Azure AI Foundry**: Masuk ke portal Azure AI Foundry.
2. **Buat Proyek**:
   - Jika Anda berada di dalam proyek, pilih "Azure AI Foundry" di kiri atas halaman untuk kembali ke halaman utama.
   - Pilih "+ Create project".
   - Masukkan nama untuk proyek Anda.
   - Jika Anda memiliki hub, hub tersebut akan dipilih secara default. Jika Anda memiliki akses ke lebih dari satu hub, Anda dapat memilih hub lain dari dropdown. Jika Anda ingin membuat hub baru, pilih "Create new hub" dan masukkan nama.
   - Pilih "Create".

### Membuat Hub di Azure AI Foundry

1. **Buka Azure AI Foundry**: Masuk dengan akun Azure Anda.
2. **Buat Hub**:
   - Pilih Management center dari menu kiri.
   - Pilih "All resources", lalu panah bawah di samping "+ New project" dan pilih "+ New hub".
   - Di dialog "Create a new hub", masukkan nama untuk hub Anda (contoh: contoso-hub) dan ubah bidang lainnya sesuai kebutuhan.
   - Pilih "Next", tinjau informasi, lalu pilih "Create".

Untuk instruksi lebih rinci, Anda dapat merujuk ke [dokumentasi resmi Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Setelah berhasil dibuat, Anda dapat mengakses studio yang Anda buat melalui [ai.azure.com](https://ai.azure.com/)

Satu AI Foundry dapat memiliki beberapa proyek. Buat proyek di AI Foundry untuk persiapan.

Buat Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Menerapkan Model Phi di Azure AI Foundry**

Klik opsi Explore pada proyek untuk masuk ke Model Catalog dan pilih Phi-3.

Pilih Phi-3-mini-4k-instruct.

Klik 'Deploy' untuk menerapkan model Phi-3-mini-4k-instruct.

> [!NOTE]
>
> Anda dapat memilih daya komputasi saat menerapkan.

## **3. Playground Chat Phi di Azure AI Foundry**

Masuk ke halaman deployment, pilih Playground, dan ajak Phi-3 dari Azure AI Foundry untuk mengobrol.

## **4. Menerapkan Model dari Azure AI Foundry**

Untuk menerapkan model dari Azure Model Catalog, Anda dapat mengikuti langkah-langkah berikut:

- Masuk ke Azure AI Foundry.
- Pilih model yang ingin Anda terapkan dari katalog model Azure AI Foundry.
- Di halaman Details model, pilih Deploy dan kemudian pilih Serverless API with Azure AI Content Safety.
- Pilih proyek tempat Anda ingin menerapkan model Anda. Untuk menggunakan penawaran Serverless API, workspace Anda harus berada di wilayah East US 2 atau Sweden Central. Anda dapat menyesuaikan nama Deployment.
- Di wizard deployment, pilih Pricing and terms untuk mempelajari harga dan syarat penggunaan.
- Pilih Deploy. Tunggu hingga deployment selesai dan Anda diarahkan ke halaman Deployments.
- Pilih Open in playground untuk mulai berinteraksi dengan model.
- Anda dapat kembali ke halaman Deployments, pilih deployment, dan catat Target URL endpoint serta Secret Key, yang dapat Anda gunakan untuk memanggil deployment dan menghasilkan completions.
- Anda selalu dapat menemukan detail endpoint, URL, dan kunci akses dengan menavigasi ke tab Build dan memilih Deployments dari bagian Components.

> [!NOTE]
> Harap diperhatikan bahwa akun Anda harus memiliki izin peran Azure AI Developer pada Resource Group untuk melakukan langkah-langkah ini.

## **5. Menggunakan Phi API di Azure AI Foundry**

Anda dapat mengakses https://{Nama proyek Anda}.region.inference.ml.azure.com/swagger.json melalui Postman GET dan menggabungkannya dengan Key untuk mempelajari antarmuka yang disediakan.

Anda dapat dengan mudah mendapatkan parameter permintaan, serta parameter respons.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.