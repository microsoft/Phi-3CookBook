# Evaluasi Model Phi-3 / Phi-3.5 yang Disesuaikan di Azure AI Foundry dengan Fokus pada Prinsip AI yang Bertanggung Jawab dari Microsoft

Contoh end-to-end (E2E) ini didasarkan pada panduan "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" dari Microsoft Tech Community.

## Ikhtisar

### Bagaimana cara mengevaluasi keamanan dan kinerja model Phi-3 / Phi-3.5 yang telah disesuaikan di Azure AI Foundry?

Menyesuaikan model dapat menyebabkan respons yang tidak diinginkan atau tidak diharapkan. Untuk memastikan model tetap aman dan efektif, penting untuk mengevaluasi potensi model dalam menghasilkan konten berbahaya serta kemampuannya menghasilkan respons yang akurat, relevan, dan koheren. Dalam tutorial ini, Anda akan belajar cara mengevaluasi keamanan dan kinerja model Phi-3 / Phi-3.5 yang telah disesuaikan dan diintegrasikan dengan Prompt flow di Azure AI Foundry.

Berikut adalah proses evaluasi di Azure AI Foundry.

![Arsitektur tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.id.png)

*Sumber Gambar: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Untuk informasi lebih rinci dan sumber daya tambahan tentang Phi-3 / Phi-3.5, kunjungi [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Prasyarat

- [Python](https://www.python.org/downloads)
- [Langganan Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Model Phi-3 / Phi-3.5 yang telah disesuaikan

### Daftar Isi

1. [**Skenario 1: Pengenalan evaluasi Prompt flow di Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Pengenalan evaluasi keamanan](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pengenalan evaluasi kinerja](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Skenario 2: Mengevaluasi model Phi-3 / Phi-3.5 di Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Sebelum memulai](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Menerapkan Azure OpenAI untuk mengevaluasi model Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Evaluasi model Phi-3 / Phi-3.5 yang telah disesuaikan menggunakan evaluasi Prompt flow di Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Selamat!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Skenario 1: Pengenalan evaluasi Prompt flow di Azure AI Foundry**

### Pengenalan evaluasi keamanan

Untuk memastikan model AI Anda etis dan aman, penting untuk mengevaluasinya berdasarkan Prinsip AI yang Bertanggung Jawab dari Microsoft. Di Azure AI Foundry, evaluasi keamanan memungkinkan Anda menilai kerentanan model terhadap serangan jailbreak dan potensinya untuk menghasilkan konten berbahaya, yang sejalan dengan prinsip-prinsip tersebut.

![Evaluasi keamanan.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.id.png)

*Sumber Gambar: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Prinsip AI yang Bertanggung Jawab dari Microsoft

Sebelum memulai langkah-langkah teknis, penting untuk memahami Prinsip AI yang Bertanggung Jawab dari Microsoft, kerangka kerja etis yang dirancang untuk membimbing pengembangan, penerapan, dan pengoperasian sistem AI secara bertanggung jawab. Prinsip-prinsip ini memastikan teknologi AI dibangun secara adil, transparan, dan inklusif. Prinsip-prinsip ini menjadi dasar untuk mengevaluasi keamanan model AI.

Prinsip AI yang Bertanggung Jawab dari Microsoft meliputi:

- **Keadilan dan Inklusivitas**: Sistem AI harus memperlakukan semua orang dengan adil dan menghindari memengaruhi kelompok dengan situasi serupa secara berbeda. Misalnya, ketika sistem AI memberikan panduan tentang pengobatan medis, aplikasi pinjaman, atau pekerjaan, rekomendasi yang diberikan harus sama untuk semua orang dengan kondisi serupa.

- **Keandalan dan Keamanan**: Untuk membangun kepercayaan, penting bahwa sistem AI beroperasi secara andal, aman, dan konsisten. Sistem ini harus dapat beroperasi sesuai dengan desain awalnya, merespons kondisi yang tidak terduga dengan aman, dan tahan terhadap manipulasi berbahaya.

- **Transparansi**: Ketika sistem AI membantu membuat keputusan yang berdampak besar pada kehidupan manusia, penting bagi orang untuk memahami bagaimana keputusan tersebut dibuat. Misalnya, bank mungkin menggunakan sistem AI untuk menentukan kelayakan kredit seseorang.

- **Privasi dan Keamanan**: Seiring dengan meningkatnya penggunaan AI, melindungi privasi dan mengamankan informasi pribadi serta bisnis menjadi semakin penting. Privasi dan keamanan data memerlukan perhatian khusus karena akses ke data sangat penting bagi sistem AI untuk membuat prediksi dan keputusan yang akurat.

- **Akuntabilitas**: Orang-orang yang merancang dan menerapkan sistem AI harus bertanggung jawab atas cara sistem mereka beroperasi. Organisasi harus mengacu pada standar industri untuk mengembangkan norma akuntabilitas, memastikan bahwa sistem AI tidak menjadi otoritas akhir dalam keputusan yang memengaruhi kehidupan manusia.

![Hub tanggung jawab.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.id.png)

*Sumber Gambar: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Untuk mempelajari lebih lanjut tentang Prinsip AI yang Bertanggung Jawab dari Microsoft, kunjungi [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metrik keamanan

Dalam tutorial ini, Anda akan mengevaluasi keamanan model Phi-3 yang telah disesuaikan menggunakan metrik keamanan Azure AI Foundry. Metrik ini membantu Anda menilai potensi model dalam menghasilkan konten berbahaya dan kerentanannya terhadap serangan jailbreak. Metrik keamanan meliputi:

- **Konten Terkait Cedera Diri**: Mengevaluasi apakah model cenderung menghasilkan konten yang terkait dengan cedera diri.
- **Konten Kebencian dan Ketidakadilan**: Mengevaluasi apakah model cenderung menghasilkan konten yang penuh kebencian atau tidak adil.
- **Konten Kekerasan**: Mengevaluasi apakah model cenderung menghasilkan konten kekerasan.
- **Konten Seksual**: Mengevaluasi apakah model cenderung menghasilkan konten seksual yang tidak pantas.

Evaluasi ini memastikan model AI tidak menghasilkan konten berbahaya atau ofensif, sehingga sejalan dengan nilai-nilai masyarakat dan standar regulasi.

![Evaluasi berdasarkan keamanan.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.id.png)

### Pengenalan evaluasi kinerja

Untuk memastikan model AI Anda berfungsi seperti yang diharapkan, penting untuk mengevaluasi kinerjanya berdasarkan metrik kinerja. Di Azure AI Foundry, evaluasi kinerja memungkinkan Anda menilai efektivitas model dalam menghasilkan respons yang akurat, relevan, dan koheren.

![Evaluasi kinerja.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.id.png)

*Sumber Gambar: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Metrik kinerja

Dalam tutorial ini, Anda akan mengevaluasi kinerja model Phi-3 / Phi-3.5 yang telah disesuaikan menggunakan metrik kinerja Azure AI Foundry. Metrik ini membantu Anda menilai efektivitas model dalam menghasilkan respons yang akurat, relevan, dan koheren. Metrik kinerja meliputi:

- **Groundedness**: Mengevaluasi sejauh mana jawaban yang dihasilkan sesuai dengan informasi dari sumber input.
- **Relevansi**: Mengevaluasi relevansi respons yang dihasilkan terhadap pertanyaan yang diberikan.
- **Koherensi**: Mengevaluasi sejauh mana teks yang dihasilkan mengalir dengan lancar, terbaca alami, dan menyerupai bahasa manusia.
- **Kefasihan**: Mengevaluasi kemampuan bahasa dari teks yang dihasilkan.
- **Kemiripan GPT**: Membandingkan respons yang dihasilkan dengan kebenaran dasar untuk kesamaan.
- **Skor F1**: Menghitung rasio kata yang sama antara respons yang dihasilkan dan data sumber.

Metrik ini membantu Anda mengevaluasi efektivitas model dalam menghasilkan respons yang akurat, relevan, dan koheren.

![Evaluasi berdasarkan kinerja.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.id.png)

## **Skenario 2: Mengevaluasi model Phi-3 / Phi-3.5 di Azure AI Foundry**

### Sebelum memulai

Tutorial ini merupakan kelanjutan dari postingan blog sebelumnya, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" dan "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Dalam postingan tersebut, kami membahas proses penyetelan model Phi-3 / Phi-3.5 di Azure AI Foundry dan mengintegrasikannya dengan Prompt flow.

Dalam tutorial ini, Anda akan menerapkan model Azure OpenAI sebagai evaluator di Azure AI Foundry dan menggunakannya untuk mengevaluasi model Phi-3 / Phi-3.5 yang telah disesuaikan.

Sebelum memulai tutorial ini, pastikan Anda memiliki prasyarat berikut, seperti yang dijelaskan dalam tutorial sebelumnya:

1. Dataset yang disiapkan untuk mengevaluasi model Phi-3 / Phi-3.5 yang telah disesuaikan.
1. Model Phi-3 / Phi-3.5 yang telah disesuaikan dan diterapkan ke Azure Machine Learning.
1. Prompt flow yang terintegrasi dengan model Phi-3 / Phi-3.5 yang telah disesuaikan di Azure AI Foundry.

> [!NOTE]
> Anda akan menggunakan file *test_data.jsonl* yang terletak di folder data dari dataset **ULTRACHAT_200k** yang diunduh dalam postingan blog sebelumnya sebagai dataset untuk mengevaluasi model Phi-3 / Phi-3.5 yang telah disesuaikan.

#### Integrasi model Phi-3 / Phi-3.5 yang disesuaikan dengan Prompt flow di Azure AI Foundry (Pendekatan berbasis kode)

> [!NOTE]
> Jika Anda mengikuti pendekatan low-code yang dijelaskan dalam "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", Anda dapat melewati latihan ini dan melanjutkan ke langkah berikutnya.
> Namun, jika Anda mengikuti pendekatan berbasis kode yang dijelaskan dalam "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" untuk menyetel dan menerapkan model Phi-3 / Phi-3.5 Anda, proses menghubungkan model Anda ke Prompt flow sedikit berbeda. Anda akan mempelajari proses ini dalam latihan ini.

Untuk melanjutkan, Anda perlu mengintegrasikan model Phi-3 / Phi-3.5 yang telah disesuaikan ke dalam Prompt flow di Azure AI Foundry.

#### Membuat Hub Azure AI Foundry

Anda perlu membuat Hub sebelum membuat Proyek. Hub berfungsi seperti Resource Group, memungkinkan Anda mengatur dan mengelola beberapa Proyek dalam Azure AI Foundry.

1. Masuk ke [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pilih **All hubs** dari tab sisi kiri.

1. Pilih **+ New hub** dari menu navigasi.

    ![Membuat hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.id.png)

1. Lakukan tugas berikut:

    - Masukkan **Nama Hub**. Harus berupa nilai yang unik.
    - Pilih **Langganan Azure** Anda.
    - Pilih **Resource group** yang akan digunakan (buat baru jika diperlukan).
    - Pilih **Lokasi** yang ingin digunakan.
    - Pilih **Hubungkan Layanan Azure AI** yang akan digunakan (buat baru jika diperlukan).
    - Pilih **Hubungkan Azure AI Search** untuk **Lewati penghubungan**.
![Isi hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.id.png)

1. Pilih **Next**.

#### Buat Proyek Azure AI Foundry

1. Di Hub yang telah Anda buat, pilih **All projects** dari tab sisi kiri.

1. Pilih **+ New project** dari menu navigasi.

    ![Pilih proyek baru.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.id.png)

1. Masukkan **Project name**. Nama ini harus unik.

    ![Buat proyek.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.id.png)

1. Pilih **Create a project**.

#### Tambahkan koneksi kustom untuk model Phi-3 / Phi-3.5 yang telah disesuaikan

Untuk mengintegrasikan model Phi-3 / Phi-3.5 Anda yang telah disesuaikan dengan Prompt flow, Anda perlu menyimpan endpoint dan kunci model dalam koneksi kustom. Pengaturan ini memastikan akses ke model Phi-3 / Phi-3.5 Anda di Prompt flow.

#### Atur api key dan endpoint uri untuk model Phi-3 / Phi-3.5 yang telah disesuaikan

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Arahkan ke workspace Azure Machine Learning yang telah Anda buat.

1. Pilih **Endpoints** dari tab sisi kiri.

    ![Pilih endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.id.png)

1. Pilih endpoint yang telah Anda buat.

    ![Pilih endpoints.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.id.png)

1. Pilih **Consume** dari menu navigasi.

1. Salin **REST endpoint** dan **Primary key** Anda.

    ![Salin api key dan endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.id.png)

#### Tambahkan Koneksi Kustom

1. Kunjungi [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Arahkan ke proyek Azure AI Foundry yang telah Anda buat.

1. Di Proyek yang telah Anda buat, pilih **Settings** dari tab sisi kiri.

1. Pilih **+ New connection**.

    ![Pilih koneksi baru.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.id.png)

1. Pilih **Custom keys** dari menu navigasi.

    ![Pilih custom keys.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.id.png)

1. Lakukan tugas berikut:

    - Pilih **+ Add key value pairs**.
    - Untuk nama kunci, masukkan **endpoint** dan tempelkan endpoint yang Anda salin dari Azure ML Studio ke kolom nilai.
    - Pilih **+ Add key value pairs** lagi.
    - Untuk nama kunci, masukkan **key** dan tempelkan kunci yang Anda salin dari Azure ML Studio ke kolom nilai.
    - Setelah menambahkan kunci, pilih **is secret** untuk mencegah kunci terlihat.

    ![Tambahkan koneksi.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.id.png)

1. Pilih **Add connection**.

#### Buat Prompt flow

Anda telah menambahkan koneksi kustom di Azure AI Foundry. Sekarang, mari buat Prompt flow menggunakan langkah-langkah berikut. Kemudian, Anda akan menghubungkan Prompt flow ini ke koneksi kustom untuk menggunakan model yang telah disesuaikan dalam Prompt flow.

1. Arahkan ke proyek Azure AI Foundry yang telah Anda buat.

1. Pilih **Prompt flow** dari tab sisi kiri.

1. Pilih **+ Create** dari menu navigasi.

    ![Pilih Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.id.png)

1. Pilih **Chat flow** dari menu navigasi.

    ![Pilih chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.id.png)

1. Masukkan **Folder name** untuk digunakan.

    ![Pilih chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.id.png)

1. Pilih **Create**.

#### Atur Prompt flow untuk berinteraksi dengan model Phi-3 / Phi-3.5 Anda

Anda perlu mengintegrasikan model Phi-3 / Phi-3.5 yang telah disesuaikan ke dalam Prompt flow. Namun, Prompt flow yang ada tidak dirancang untuk tujuan ini. Oleh karena itu, Anda harus mendesain ulang Prompt flow untuk memungkinkan integrasi model kustom.

1. Di Prompt flow, lakukan tugas berikut untuk membangun ulang alur yang ada:

    - Pilih **Raw file mode**.
    - Hapus semua kode yang ada di file *flow.dag.yml*.
    - Tambahkan kode berikut ke *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Pilih **Save**.

    ![Pilih raw file mode.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.id.png)

1. Tambahkan kode berikut ke *integrate_with_promptflow.py* untuk menggunakan model Phi-3 / Phi-3.5 yang telah disesuaikan di Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Tempelkan kode prompt flow.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.id.png)

> [!NOTE]
> Untuk informasi lebih lanjut tentang penggunaan Prompt flow di Azure AI Foundry, Anda dapat merujuk ke [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Pilih **Chat input**, **Chat output** untuk mengaktifkan interaksi dengan model Anda.

    ![Pilih Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.id.png)

1. Sekarang Anda siap untuk berinteraksi dengan model Phi-3 / Phi-3.5 Anda. Pada latihan berikutnya, Anda akan mempelajari cara memulai Prompt flow dan menggunakannya untuk berinteraksi dengan model Phi-3 / Phi-3.5 yang telah disesuaikan.

> [!NOTE]
>
> Alur yang telah dibangun ulang seharusnya terlihat seperti gambar di bawah ini:
>
> ![Contoh Flow](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.id.png)
>

#### Mulai Prompt flow

1. Pilih **Start compute sessions** untuk memulai Prompt flow.

    ![Mulai sesi komputasi.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.id.png)

1. Pilih **Validate and parse input** untuk memperbarui parameter.

    ![Validasi input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.id.png)

1. Pilih **Value** dari **connection** ke koneksi kustom yang Anda buat. Misalnya, *connection*.

    ![Koneksi.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.id.png)

#### Berinteraksi dengan model Phi-3 / Phi-3.5 Anda

1. Pilih **Chat**.

    ![Pilih chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.id.png)

1. Berikut adalah contoh hasil: Sekarang Anda dapat berinteraksi dengan model Phi-3 / Phi-3.5 Anda. Disarankan untuk mengajukan pertanyaan berdasarkan data yang digunakan untuk fine-tuning.

    ![Berinteraksi dengan prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.id.png)

### Deploy Azure OpenAI untuk mengevaluasi model Phi-3 / Phi-3.5

Untuk mengevaluasi model Phi-3 / Phi-3.5 di Azure AI Foundry, Anda perlu menerapkan model Azure OpenAI. Model ini akan digunakan untuk mengevaluasi kinerja model Phi-3 / Phi-3.5.

#### Deploy Azure OpenAI

1. Masuk ke [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Arahkan ke proyek Azure AI Foundry yang telah Anda buat.

    ![Pilih Proyek.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.id.png)

1. Di Proyek yang telah Anda buat, pilih **Deployments** dari tab sisi kiri.

1. Pilih **+ Deploy model** dari menu navigasi.

1. Pilih **Deploy base model**.

    ![Pilih Deployments.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.id.png)

1. Pilih model Azure OpenAI yang ingin Anda gunakan. Misalnya, **gpt-4o**.

    ![Pilih model Azure OpenAI yang ingin Anda gunakan.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.id.png)

1. Pilih **Confirm**.

### Evaluasi model Phi-3 / Phi-3.5 yang telah disesuaikan menggunakan evaluasi Prompt flow di Azure AI Foundry

### Mulai evaluasi baru

1. Kunjungi [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Arahkan ke proyek Azure AI Foundry yang telah Anda buat.

    ![Pilih Proyek.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.id.png)

1. Di Proyek yang telah Anda buat, pilih **Evaluation** dari tab sisi kiri.

1. Pilih **+ New evaluation** dari menu navigasi.
![Pilih evaluasi.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.id.png)

1. Pilih evaluasi **Prompt flow**.

    ![Pilih evaluasi Prompt flow.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.id.png)

1. Lakukan tugas berikut:

    - Masukkan nama evaluasi. Nama ini harus unik.
    - Pilih **Pertanyaan dan jawaban tanpa konteks** sebagai jenis tugas. Karena, dataset **ULTRACHAT_200k** yang digunakan dalam tutorial ini tidak memiliki konteks.
    - Pilih prompt flow yang ingin Anda evaluasi.

    ![Evaluasi Prompt flow.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.id.png)

1. Pilih **Next**.

1. Lakukan tugas berikut:

    - Pilih **Tambahkan dataset Anda** untuk mengunggah dataset. Misalnya, Anda dapat mengunggah file dataset pengujian, seperti *test_data.json1*, yang disertakan saat Anda mengunduh dataset **ULTRACHAT_200k**.
    - Pilih **Kolom Dataset** yang sesuai dengan dataset Anda. Sebagai contoh, jika Anda menggunakan dataset **ULTRACHAT_200k**, pilih **${data.prompt}** sebagai kolom dataset.

    ![Evaluasi Prompt flow.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.id.png)

1. Pilih **Next**.

1. Lakukan tugas berikut untuk mengonfigurasi metrik kinerja dan kualitas:

    - Pilih metrik kinerja dan kualitas yang ingin Anda gunakan.
    - Pilih model Azure OpenAI yang Anda buat untuk evaluasi. Misalnya, pilih **gpt-4o**.

    ![Evaluasi Prompt flow.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.id.png)

1. Lakukan tugas berikut untuk mengonfigurasi metrik risiko dan keamanan:

    - Pilih metrik risiko dan keamanan yang ingin Anda gunakan.
    - Pilih ambang batas untuk menghitung tingkat cacat yang ingin Anda gunakan. Misalnya, pilih **Medium**.
    - Untuk **pertanyaan**, pilih **Sumber Data** menjadi **{$data.prompt}**.
    - Untuk **jawaban**, pilih **Sumber Data** menjadi **{$run.outputs.answer}**.
    - Untuk **ground_truth**, pilih **Sumber Data** menjadi **{$data.message}**.

    ![Evaluasi Prompt flow.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.id.png)

1. Pilih **Next**.

1. Pilih **Submit** untuk memulai evaluasi.

1. Evaluasi akan memakan waktu untuk selesai. Anda dapat memantau kemajuannya di tab **Evaluation**.

### Tinjau Hasil Evaluasi

> [!NOTE]
> Hasil yang disajikan di bawah ini dimaksudkan untuk menggambarkan proses evaluasi. Dalam tutorial ini, kami menggunakan model yang di-fine-tune pada dataset yang relatif kecil, sehingga dapat menghasilkan hasil yang kurang optimal. Hasil aktual dapat sangat bervariasi tergantung pada ukuran, kualitas, dan keragaman dataset yang digunakan, serta konfigurasi spesifik dari model tersebut.

Setelah evaluasi selesai, Anda dapat meninjau hasil untuk metrik kinerja dan keamanan.

1. Metrik kinerja dan kualitas:

    - Evaluasi efektivitas model dalam menghasilkan respons yang koheren, lancar, dan relevan.

    ![Hasil evaluasi.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.id.png)

1. Metrik risiko dan keamanan:

    - Pastikan output model aman dan selaras dengan Prinsip AI Bertanggung Jawab, menghindari konten yang berbahaya atau ofensif.

    ![Hasil evaluasi.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.id.png)

1. Anda dapat menggulir ke bawah untuk melihat **Hasil metrik terperinci**.

    ![Hasil evaluasi.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.id.png)

1. Dengan mengevaluasi model Phi-3 / Phi-3.5 kustom Anda terhadap metrik kinerja dan keamanan, Anda dapat memastikan bahwa model tersebut tidak hanya efektif, tetapi juga mematuhi praktik AI yang bertanggung jawab, sehingga siap untuk implementasi di dunia nyata.

## Selamat!

### Anda telah menyelesaikan tutorial ini

Anda telah berhasil mengevaluasi model Phi-3 yang di-fine-tune dan terintegrasi dengan Prompt flow di Azure AI Foundry. Ini adalah langkah penting untuk memastikan bahwa model AI Anda tidak hanya berkinerja baik, tetapi juga mematuhi prinsip AI Bertanggung Jawab Microsoft untuk membantu Anda membangun aplikasi AI yang dapat dipercaya dan andal.

![Arsitektur.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.id.png)

## Bersihkan Sumber Daya Azure

Bersihkan sumber daya Azure Anda untuk menghindari biaya tambahan pada akun Anda. Pergi ke portal Azure dan hapus sumber daya berikut:

- Sumber daya Azure Machine Learning.
- Endpoint model Azure Machine Learning.
- Sumber daya Proyek Azure AI Foundry.
- Sumber daya Prompt flow Azure AI Foundry.

### Langkah Selanjutnya

#### Dokumentasi

- [Menilai sistem AI menggunakan dasbor AI Bertanggung Jawab](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluasi dan pemantauan metrik untuk AI generatif](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Dokumentasi Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Dokumentasi Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Konten Pelatihan

- [Pendahuluan tentang Pendekatan AI Bertanggung Jawab Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Pendahuluan tentang Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referensi

- [Apa itu AI Bertanggung Jawab?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Pengumuman alat baru di Azure AI untuk membantu Anda membangun aplikasi AI generatif yang lebih aman dan terpercaya](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluasi aplikasi AI generatif](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan berbasis AI. Meskipun kami berupaya untuk memastikan keakuratan, harap disadari bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan untuk menggunakan penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.