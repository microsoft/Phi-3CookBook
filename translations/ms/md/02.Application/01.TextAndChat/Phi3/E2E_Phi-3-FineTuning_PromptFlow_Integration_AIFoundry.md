# Melarasikan dan Mengintegrasikan Model Phi-3 Kustom dengan Prompt Flow di Azure AI Foundry

Contoh end-to-end (E2E) ini didasarkan pada panduan "[Melarasikan dan Mengintegrasikan Model Phi-3 Kustom dengan Prompt Flow di Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" dari Komunitas Teknologi Microsoft. Panduan ini menjelaskan proses melarasikan, menyebarkan, dan mengintegrasikan model Phi-3 kustom dengan Prompt Flow di Azure AI Foundry.  
Berbeda dengan contoh E2E "[Melarasikan dan Mengintegrasikan Model Phi-3 Kustom dengan Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" yang dijalankan secara lokal, tutorial ini sepenuhnya berfokus pada melarasikan dan mengintegrasikan model Anda di dalam Azure AI / ML Studio.

## Ikhtisar

Dalam contoh E2E ini, Anda akan mempelajari cara melarasikan model Phi-3 dan mengintegrasikannya dengan Prompt Flow di Azure AI Foundry. Dengan memanfaatkan Azure AI / ML Studio, Anda akan membangun alur kerja untuk menyebarkan dan menggunakan model AI kustom. Contoh E2E ini dibagi menjadi tiga skenario:

**Skenario 1: Mengatur sumber daya Azure dan Mempersiapkan pelarasan**  
**Skenario 2: Melarasikan model Phi-3 dan Menyebarkannya di Azure Machine Learning Studio**  
**Skenario 3: Mengintegrasikan dengan Prompt Flow dan Berinteraksi dengan model kustom Anda di Azure AI Foundry**

Berikut adalah ikhtisar dari contoh E2E ini.

![Ikhtisar FineTuning_PromptFlow_Integration.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.ms.png)

### Daftar Isi

1. **[Skenario 1: Mengatur sumber daya Azure dan Mempersiapkan pelarasan](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Membuat Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Meminta kuota GPU di Langganan Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Menambahkan penugasan peran](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Mengatur proyek](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Mempersiapkan dataset untuk pelarasan](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[Skenario 2: Melarasikan model Phi-3 dan Menyebarkannya di Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Melarasikan model Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Menyebarkan model Phi-3 yang telah dilarasikan](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[Skenario 3: Mengintegrasikan dengan Prompt Flow dan Berinteraksi dengan model kustom Anda di Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Mengintegrasikan model Phi-3 kustom dengan Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Berinteraksi dengan model Phi-3 kustom Anda](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

## Skenario 1: Mengatur sumber daya Azure dan Mempersiapkan pelarasan

### Membuat Azure Machine Learning Workspace

1. Ketik *azure machine learning* di **bilah pencarian** di bagian atas halaman portal dan pilih **Azure Machine Learning** dari opsi yang muncul.

    ![Ketik azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.ms.png)

2. Pilih **+ Create** dari menu navigasi.  

3. Pilih **New workspace** dari menu navigasi.  

    ![Pilih new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.ms.png)

4. Lakukan langkah-langkah berikut:  

    - Pilih **Subscription** Azure Anda.  
    - Pilih **Resource group** yang akan digunakan (buat yang baru jika diperlukan).  
    - Masukkan **Workspace Name**. Nama ini harus unik.  
    - Pilih **Region** yang akan digunakan.  
    - Pilih **Storage account** yang akan digunakan (buat yang baru jika diperlukan).  
    - Pilih **Key vault** yang akan digunakan (buat yang baru jika diperlukan).  
    - Pilih **Application insights** yang akan digunakan (buat yang baru jika diperlukan).  
    - Pilih **Container registry** yang akan digunakan (buat yang baru jika diperlukan).  

    ![Isi azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.ms.png)

5. Pilih **Review + Create**.  

6. Pilih **Create**.  

### Meminta kuota GPU di Langganan Azure

Dalam tutorial ini, Anda akan mempelajari cara melarasikan dan menyebarkan model Phi-3 menggunakan GPU. Untuk pelarasan, Anda akan menggunakan GPU *Standard_NC24ads_A100_v4*, yang memerlukan permintaan kuota. Untuk penyebaran, Anda akan menggunakan GPU *Standard_NC6s_v3*, yang juga memerlukan permintaan kuota.

> [!NOTE]  
> Hanya langganan Pay-As-You-Go (jenis langganan standar) yang memenuhi syarat untuk alokasi GPU; langganan manfaat saat ini tidak didukung.  

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).  

1. Lakukan langkah-langkah berikut untuk meminta kuota *Standard NCADSA100v4 Family*:  

    - Pilih **Quota** dari tab sisi kiri.  
    - Pilih **Virtual machine family** yang akan digunakan. Misalnya, pilih **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, yang mencakup GPU *Standard_NC24ads_A100_v4*.  
    - Pilih **Request quota** dari menu navigasi.  

        ![Meminta kuota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.ms.png)

    - Di halaman Request quota, masukkan **New cores limit** yang ingin Anda gunakan. Misalnya, 24.  
    - Di halaman Request quota, pilih **Submit** untuk meminta kuota GPU.  

1. Lakukan langkah-langkah berikut untuk meminta kuota *Standard NCSv3 Family*:  

    - Pilih **Quota** dari tab sisi kiri.  
    - Pilih **Virtual machine family** yang akan digunakan. Misalnya, pilih **Standard NCSv3 Family Cluster Dedicated vCPUs**, yang mencakup GPU *Standard_NC6s_v3*.  
    - Pilih **Request quota** dari menu navigasi.  
    - Di halaman Request quota, masukkan **New cores limit** yang ingin Anda gunakan. Misalnya, 24.  
    - Di halaman Request quota, pilih **Submit** untuk meminta kuota GPU.  

### Menambahkan penugasan peran

Untuk melarasikan dan menyebarkan model Anda, Anda harus terlebih dahulu membuat User Assigned Managed Identity (UAI) dan memberikan izin yang sesuai. UAI ini akan digunakan untuk autentikasi selama penyebaran.

#### Membuat User Assigned Managed Identity (UAI)

1. Ketik *managed identities* di **bilah pencarian** di bagian atas halaman portal dan pilih **Managed Identities** dari opsi yang muncul.

    ![Ketik managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.ms.png)

1. Pilih **+ Create**.

    ![Pilih create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.ms.png)

1. Lakukan langkah-langkah berikut:  

    - Pilih **Subscription** Azure Anda.  
    - Pilih **Resource group** yang akan digunakan (buat yang baru jika diperlukan).  
    - Pilih **Region** yang akan digunakan.  
    - Masukkan **Name**. Nama ini harus unik.  

    ![Isi managed identities.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.ms.png)

1. Pilih **Review + create**.  

1. Pilih **+ Create**.  

#### Menambahkan peran Contributor ke Managed Identity

1. Navigasikan ke resource Managed Identity yang Anda buat.  

1. Pilih **Azure role assignments** dari tab sisi kiri.  

1. Pilih **+Add role assignment** dari menu navigasi.  

1. Di halaman Add role assignment, lakukan langkah-langkah berikut:  
    - Pilih **Scope** ke **Resource group**.  
    - Pilih **Subscription** Azure Anda.  
    - Pilih **Resource group** yang akan digunakan.  
    - Pilih **Role** ke **Contributor**.  

    ![Isi peran Contributor.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.ms.png)

2. Pilih **Save**.  

#### Menambahkan peran Storage Blob Data Reader ke Managed Identity

1. Ketik *storage accounts* di **bilah pencarian** di bagian atas halaman portal dan pilih **Storage accounts** dari opsi yang muncul.

    ![Ketik storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.ms.png)

1. Pilih akun penyimpanan yang terkait dengan Azure Machine Learning workspace yang Anda buat. Misalnya, *finetunephistorage*.  

1. Lakukan langkah-langkah berikut untuk navigasi ke halaman Add role assignment:  

    - Navigasikan ke akun penyimpanan Azure yang Anda buat.  
    - Pilih **Access Control (IAM)** dari tab sisi kiri.  
    - Pilih **+ Add** dari menu navigasi.  
    - Pilih **Add role assignment** dari menu navigasi.  

    ![Tambahkan peran.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.ms.png)

1. Di halaman Add role assignment, lakukan langkah-langkah berikut:  

    - Di halaman Role, ketik *Storage Blob Data Reader* di **bilah pencarian** dan pilih **Storage Blob Data Reader** dari opsi yang muncul.  
    - Di halaman Role, pilih **Next**.  
    - Di halaman Members, pilih **Assign access to** **Managed identity**.  
    - Di halaman Members, pilih **+ Select members**.  
    - Di halaman Select managed identities, pilih **Subscription** Azure Anda.  
    - Di halaman Select managed identities, pilih **Managed identity** ke **Manage Identity**.  
    - Di halaman Select managed identities, pilih Managed Identity yang Anda buat. Misalnya, *finetunephi-managedidentity*.  
    - Di halaman Select managed identities, pilih **Select**.  

    ![Pilih managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.ms.png)

1. Pilih **Review + assign**.  

#### Menambahkan peran AcrPull ke Managed Identity

1. Ketik *container registries* di **bilah pencarian** di bagian atas halaman portal dan pilih **Container registries** dari opsi yang muncul.

    ![Ketik container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.ms.png)

1. Pilih container registry yang terkait dengan Azure Machine Learning workspace. Misalnya, *finetunephicontainerregistry*.  

1. Lakukan langkah-langkah berikut untuk navigasi ke halaman Add role assignment:  

    - Pilih **Access Control (IAM)** dari tab sisi kiri.  
    - Pilih **+ Add** dari menu navigasi.  
    - Pilih **Add role assignment** dari menu navigasi.  

1. Di halaman Add role assignment, lakukan langkah-langkah berikut:  

    - Di halaman Role, ketik *AcrPull* di **bilah pencarian** dan pilih **AcrPull** dari opsi yang muncul.  
    - Di halaman Role, pilih **Next**.  
    - Di halaman Members, pilih **Assign access to** **Managed identity**.  
    - Di halaman Members, pilih **+ Select members**.  
    - Di halaman Select managed identities, pilih **Subscription** Azure Anda.  
    - Di halaman Select managed identities, pilih **Managed identity** ke **Manage Identity**.  
    - Di halaman Select managed identities, pilih Managed Identity yang Anda buat. Misalnya, *finetunephi-managedidentity*.  
    - Di halaman Select managed identities, pilih **Select**.  
    - Pilih **Review + assign**.  

### Mengatur proyek

Untuk mengunduh dataset yang diperlukan untuk pelarasan, Anda akan mengatur lingkungan lokal.  

Dalam latihan ini, Anda akan:  

- Membuat folder untuk bekerja di dalamnya.  
- Membuat virtual environment.  
- Menginstal paket yang diperlukan.  
- Membuat file *download_dataset.py* untuk mengunduh dataset.  

#### Membuat folder untuk bekerja di dalamnya

1. Buka jendela terminal dan ketik perintah berikut untuk membuat folder bernama *finetune-phi* di jalur default.

    ```console
    mkdir finetune-phi
    ```  

2. Ketik perintah berikut di terminal Anda untuk masuk ke folder *finetune-phi* yang Anda buat.

    ```console
    cd finetune-phi
    ```  

#### Membuat virtual environment

1. Ketik perintah berikut di terminal Anda untuk membuat virtual environment bernama *.venv*.  

    ```console
    python -m venv .venv
    ```  

2. Ketik perintah berikut di terminal Anda untuk mengaktifkan virtual environment.  

    ```console
    .venv\Scripts\activate.bat
    ```  

> [!NOTE]  
> Jika berhasil, Anda akan melihat *(.venv)* sebelum prompt perintah.  

#### Menginstal paket yang diperlukan

1. Ketik perintah berikut di terminal Anda untuk menginstal paket yang diperlukan.

    ```console
    pip install datasets==2.19.1
    ```  

#### Membuat `download_dataset.py`

> [!NOTE]  
> Struktur folder lengkap:  
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```  

1. Buka **Visual Studio Code**.  

1. Pilih **File** dari menu bar.  

1. Pilih **Open Folder**.  

1. Pilih folder *finetune-phi* yang Anda buat, yang terletak di *C:\Users\yourUserName\finetune-phi*.  

    ![Pilih folder yang Anda buat.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.ms.png)  

1. Di panel kiri Visual Studio Code, klik kanan dan pilih **New File** untuk membuat file baru bernama *download_dataset.py*.  

    ![Buat file baru.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.ms.png)  

### Mempersiapkan dataset untuk pelarasan

Dalam latihan ini, Anda akan menjalankan file *download_dataset.py* untuk mengunduh dataset *ultrachat_200k* ke lingkungan lokal Anda. Dataset ini akan digunakan untuk melarasikan model Phi-3 di Azure Machine Learning.  

Dalam latihan ini, Anda akan:  

- Menambahkan kode ke file *download_dataset.py* untuk mengunduh dataset.  
- Menjalankan file *download_dataset.py* untuk mengunduh dataset ke lingkungan lokal Anda.  

#### Mengunduh dataset menggunakan *download_dataset.py*

1. Buka file *download_dataset.py* di Visual Studio Code.  

1. Tambahkan kode berikut ke file *download_dataset.py*.  

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```  

1. Ketik perintah berikut di terminal Anda untuk menjalankan skrip dan mengunduh dataset ke lingkungan lokal Anda.  

    ```console
    python download_dataset.py
    ```  

1. Verifikasi bahwa dataset berhasil disimpan ke direktori lokal *finetune-phi/data*.  

> [!NOTE]  
>
> #### Catatan tentang ukuran dataset dan waktu pelarasan  
>
> Dalam tutorial ini, Anda hanya menggunakan 1% dari dataset (`split='train[:1%]'`). Ini secara signifikan mengurangi jumlah data, mempercepat proses pengunggahan dan pelarasan. Anda dapat menyesuaikan persentase untuk menemukan keseimbangan yang tepat antara waktu pelatihan dan performa model. Menggunakan subset dataset yang lebih kecil mengurangi waktu yang diperlukan untuk pelarasan, sehingga proses lebih mudah dikelola untuk tutorial ini.  

## Skenario 2: Melarasikan model Phi-3 dan Menyebarkannya di Azure Machine Learning Studio

### Melarasikan model Phi-3

Dalam latihan ini, Anda akan melarasikan model Phi-3 di Azure Machine Learning Studio.  

Dalam latihan ini, Anda akan:  

- Membuat kluster komputer untuk pelarasan.  
- Melarasikan model Phi-3 di Azure Machine Learning Studio.  

#### Membuat kluster komputer untuk pelarasan  
1. Lawati [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih **Compute** dari tab di sebelah kiri.

1. Pilih **Compute clusters** dari menu navigasi.

1. Pilih **+ New**.

    ![Pilih compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.ms.png)

1. Lakukan tugas berikut:

    - Pilih **Region** yang ingin digunakan.
    - Pilih **Virtual machine tier** ke **Dedicated**.
    - Pilih **Virtual machine type** ke **GPU**.
    - Pilih penapis **Virtual machine size** ke **Select from all options**.
    - Pilih **Virtual machine size** ke **Standard_NC24ads_A100_v4**.

    ![Cipta kluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.ms.png)

1. Pilih **Next**.

1. Lakukan tugas berikut:

    - Masukkan **Compute name**. Ia mestilah nilai unik.
    - Pilih **Minimum number of nodes** ke **0**.
    - Pilih **Maximum number of nodes** ke **1**.
    - Pilih **Idle seconds before scale down** ke **120**.

    ![Cipta kluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.ms.png)

1. Pilih **Create**.

#### Melaras model Phi-3

1. Lawati [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih ruang kerja Azure Machine Learning yang anda cipta.

    ![Pilih ruang kerja yang anda cipta.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ms.png)

1. Lakukan tugas berikut:

    - Pilih **Model catalog** dari tab di sebelah kiri.
    - Taip *phi-3-mini-4k* dalam **search bar** dan pilih **Phi-3-mini-4k-instruct** dari pilihan yang muncul.

    ![Taip phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.ms.png)

1. Pilih **Fine-tune** dari menu navigasi.

    ![Pilih fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.ms.png)

1. Lakukan tugas berikut:

    - Pilih **Select task type** ke **Chat completion**.
    - Pilih **+ Select data** untuk memuat naik **Training data**.
    - Pilih jenis muat naik data pengesahan ke **Provide different validation data**.
    - Pilih **+ Select data** untuk memuat naik **Validation data**.

    ![Isi halaman fine-tuning.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.ms.png)

    > [!TIP]
    >
    > Anda boleh memilih **Advanced settings** untuk menyesuaikan konfigurasi seperti **learning_rate** dan **lr_scheduler_type** bagi mengoptimumkan proses fine-tuning mengikut keperluan anda.

1. Pilih **Finish**.

1. Dalam latihan ini, anda berjaya melaras model Phi-3 menggunakan Azure Machine Learning. Harap maklum bahawa proses fine-tuning boleh mengambil masa yang lama. Selepas menjalankan tugas fine-tuning, anda perlu menunggu sehingga selesai. Anda boleh memantau status tugas fine-tuning dengan pergi ke tab Jobs di sebelah kiri ruang kerja Azure Machine Learning anda. Dalam siri seterusnya, anda akan menyebarkan model yang telah dilaras dan mengintegrasikannya dengan Prompt flow.

    ![Lihat tugas fine-tuning.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.ms.png)

### Menyebarkan model Phi-3 yang telah dilaras

Untuk mengintegrasikan model Phi-3 yang telah dilaras dengan Prompt flow, anda perlu menyebarkan model tersebut supaya boleh diakses untuk inferens masa nyata. Proses ini melibatkan pendaftaran model, penciptaan endpoint dalam talian, dan penyebaran model.

Dalam latihan ini, anda akan:

- Mendaftar model yang telah dilaras dalam ruang kerja Azure Machine Learning.
- Mencipta endpoint dalam talian.
- Menyebarkan model Phi-3 yang telah didaftarkan.

#### Mendaftar model yang telah dilaras

1. Lawati [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Pilih ruang kerja Azure Machine Learning yang anda cipta.

    ![Pilih ruang kerja yang anda cipta.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ms.png)

1. Pilih **Models** dari tab di sebelah kiri.
1. Pilih **+ Register**.
1. Pilih **From a job output**.

    ![Daftar model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.ms.png)

1. Pilih tugas yang anda cipta.

    ![Pilih tugas.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.ms.png)

1. Pilih **Next**.

1. Pilih **Model type** ke **MLflow**.

1. Pastikan **Job output** dipilih; ia sepatutnya dipilih secara automatik.

    ![Pilih output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.ms.png)

2. Pilih **Next**.

3. Pilih **Register**.

    ![Pilih daftar.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.ms.png)

4. Anda boleh melihat model yang telah didaftarkan dengan pergi ke menu **Models** dari tab di sebelah kiri.

    ![Model didaftarkan.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.ms.png)

#### Menyebarkan model yang telah dilaras

1. Pergi ke ruang kerja Azure Machine Learning yang anda cipta.

1. Pilih **Endpoints** dari tab di sebelah kiri.

1. Pilih **Real-time endpoints** dari menu navigasi.

    ![Cipta endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.ms.png)

1. Pilih **Create**.

1. Pilih model yang telah didaftarkan.

    ![Pilih model yang telah didaftarkan.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.ms.png)

1. Pilih **Select**.

1. Lakukan tugas berikut:

    - Pilih **Virtual machine** ke *Standard_NC6s_v3*.
    - Pilih **Instance count** yang anda mahu gunakan. Sebagai contoh, *1*.
    - Pilih **Endpoint** ke **New** untuk mencipta endpoint.
    - Masukkan **Endpoint name**. Ia mestilah nilai unik.
    - Masukkan **Deployment name**. Ia mestilah nilai unik.

    ![Isi tetapan penyebaran.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.ms.png)

1. Pilih **Deploy**.

> [!WARNING]
> Untuk mengelakkan caj tambahan pada akaun anda, pastikan anda memadam endpoint yang dicipta di ruang kerja Azure Machine Learning.
>

#### Periksa status penyebaran dalam Azure Machine Learning Workspace

1. Pergi ke ruang kerja Azure Machine Learning yang anda cipta.

1. Pilih **Endpoints** dari tab di sebelah kiri.

1. Pilih endpoint yang anda cipta.

    ![Pilih endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.ms.png)

1. Pada halaman ini, anda boleh mengurus endpoint semasa proses penyebaran.

> [!NOTE]
> Setelah penyebaran selesai, pastikan **Live traffic** ditetapkan ke **100%**. Jika tidak, pilih **Update traffic** untuk menyesuaikan tetapan trafik. Harap maklum bahawa anda tidak boleh menguji model jika trafik ditetapkan ke 0%.
>
> ![Tetapkan trafik.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.ms.png)
>

## Senario 3: Mengintegrasikan dengan Prompt flow dan Berinteraksi dengan model khusus anda dalam Azure AI Foundry

### Mengintegrasikan model Phi-3 khusus dengan Prompt flow

Selepas berjaya menyebarkan model yang telah dilaras, anda kini boleh mengintegrasikannya dengan Prompt Flow untuk menggunakan model anda dalam aplikasi masa nyata, membolehkan pelbagai tugas interaktif dengan model Phi-3 khusus anda.

Dalam latihan ini, anda akan:

- Mencipta Azure AI Foundry Hub.
- Mencipta Azure AI Foundry Project.
- Mencipta Prompt flow.
- Menambah sambungan khusus untuk model Phi-3 yang telah dilaras.
- Menyediakan Prompt flow untuk berinteraksi dengan model Phi-3 khusus anda.

> [!NOTE]
> Anda juga boleh mengintegrasikan dengan Promptflow menggunakan Azure ML Studio. Proses integrasi yang sama boleh digunakan di Azure ML Studio.

#### Mencipta Azure AI Foundry Hub

Anda perlu mencipta Hub sebelum mencipta Projek. Hub bertindak seperti Resource Group, membolehkan anda mengatur dan menguruskan pelbagai Projek dalam Azure AI Foundry.

1. Lawati [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Pilih **All hubs** dari tab di sebelah kiri.

1. Pilih **+ New hub** dari menu navigasi.

    ![Cipta hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.ms.png)

1. Lakukan tugas berikut:

    - Masukkan **Hub name**. Ia mestilah nilai unik.
    - Pilih **Subscription** Azure anda.
    - Pilih **Resource group** yang ingin digunakan (cipta baru jika perlu).
    - Pilih **Location** yang ingin digunakan.
    - Pilih **Connect Azure AI Services** yang ingin digunakan (cipta baru jika perlu).
    - Pilih **Connect Azure AI Search** ke **Skip connecting**.

    ![Isi hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.ms.png)

1. Pilih **Next**.

#### Mencipta Azure AI Foundry Project

1. Dalam Hub yang anda cipta, pilih **All projects** dari tab di sebelah kiri.

1. Pilih **+ New project** dari menu navigasi.

    ![Pilih projek baru.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.ms.png)

1. Masukkan **Project name**. Ia mestilah nilai unik.

    ![Cipta projek.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.ms.png)

1. Pilih **Create a project**.

#### Menambah sambungan khusus untuk model Phi-3 yang telah dilaras

Untuk mengintegrasikan model Phi-3 khusus anda dengan Prompt flow, anda perlu menyimpan endpoint dan kunci model dalam sambungan khusus. Persediaan ini memastikan akses ke model Phi-3 khusus anda dalam Prompt flow.

#### Tetapkan kunci API dan URI endpoint model Phi-3 yang telah dilaras

1. Lawati [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Pergi ke ruang kerja Azure Machine Learning yang anda cipta.

1. Pilih **Endpoints** dari tab di sebelah kiri.

    ![Pilih endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.ms.png)

1. Pilih endpoint yang anda cipta.

    ![Pilih endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.ms.png)

1. Pilih **Consume** dari menu navigasi.

1. Salin **REST endpoint** dan **Primary key** anda.
![Salin kunci API dan URI titik akhir.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.ms.png)

#### Tambah Sambungan Khusus

1. Lawati [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Pergi ke projek Azure AI Foundry yang telah anda cipta.

1. Dalam projek yang telah anda cipta, pilih **Settings** dari tab sebelah kiri.

1. Pilih **+ New connection**.

    ![Pilih sambungan baharu.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.ms.png)

1. Pilih **Custom keys** dari menu navigasi.

    ![Pilih kunci khusus.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.ms.png)

1. Lakukan langkah berikut:

    - Pilih **+ Add key value pairs**.
    - Untuk nama kunci, masukkan **endpoint** dan tampal endpoint yang anda salin dari Azure ML Studio ke dalam medan nilai.
    - Pilih **+ Add key value pairs** sekali lagi.
    - Untuk nama kunci, masukkan **key** dan tampal kunci yang anda salin dari Azure ML Studio ke dalam medan nilai.
    - Selepas menambah kunci, pilih **is secret** untuk memastikan kunci tidak terdedah.

    ![Tambah sambungan.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.ms.png)

1. Pilih **Add connection**.

#### Cipta Prompt flow

Anda telah menambah sambungan khusus dalam Azure AI Foundry. Sekarang, mari kita cipta Prompt flow dengan mengikuti langkah-langkah berikut. Kemudian, anda akan menghubungkan Prompt flow ini ke sambungan khusus supaya anda boleh menggunakan model yang telah disesuaikan dalam Prompt flow.

1. Pergi ke projek Azure AI Foundry yang telah anda cipta.

1. Pilih **Prompt flow** dari tab sebelah kiri.

1. Pilih **+ Create** dari menu navigasi.

    ![Pilih Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.ms.png)

1. Pilih **Chat flow** dari menu navigasi.

    ![Pilih chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.ms.png)

1. Masukkan **Folder name** yang akan digunakan.

    ![Masukkan nama.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.ms.png)

2. Pilih **Create**.

#### Sediakan Prompt flow untuk berinteraksi dengan model Phi-3 khusus anda

Anda perlu mengintegrasikan model Phi-3 yang telah disesuaikan ke dalam Prompt flow. Walau bagaimanapun, Prompt flow yang sedia ada tidak direka untuk tujuan ini. Oleh itu, anda mesti merancang semula Prompt flow untuk membolehkan integrasi model khusus tersebut.

1. Dalam Prompt flow, lakukan langkah berikut untuk membina semula aliran yang sedia ada:

    - Pilih **Raw file mode**.
    - Padam semua kod yang sedia ada dalam fail *flow.dag.yml*.
    - Tambahkan kod berikut ke dalam fail *flow.dag.yml*.

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

    ![Pilih mod fail mentah.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.ms.png)

1. Tambahkan kod berikut ke dalam fail *integrate_with_promptflow.py* untuk menggunakan model Phi-3 khusus dalam Prompt flow.

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
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
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
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Tampal kod prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.ms.png)

> [!NOTE]
> Untuk maklumat lebih terperinci tentang menggunakan Prompt flow dalam Azure AI Foundry, anda boleh merujuk kepada [Prompt flow dalam Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Pilih **Chat input**, **Chat output** untuk membolehkan perbualan dengan model anda.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.ms.png)

1. Kini anda bersedia untuk berinteraksi dengan model Phi-3 khusus anda. Dalam latihan seterusnya, anda akan belajar cara memulakan Prompt flow dan menggunakannya untuk berinteraksi dengan model Phi-3 yang telah disesuaikan.

> [!NOTE]
>
> Aliran yang telah dibina semula sepatutnya kelihatan seperti imej di bawah:
>
> ![Contoh aliran.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.ms.png)
>

### Berinteraksi dengan model Phi-3 khusus anda

Sekarang bahawa anda telah menyesuaikan dan mengintegrasikan model Phi-3 khusus anda dengan Prompt flow, anda sudah bersedia untuk mula berinteraksi dengannya. Latihan ini akan membimbing anda melalui proses menyediakan dan memulakan perbualan dengan model anda menggunakan Prompt flow. Dengan mengikuti langkah-langkah ini, anda dapat sepenuhnya memanfaatkan kemampuan model Phi-3 yang telah disesuaikan untuk pelbagai tugas dan perbualan.

- Berinteraksi dengan model Phi-3 khusus anda menggunakan Prompt flow.

#### Mulakan Prompt flow

1. Pilih **Start compute sessions** untuk memulakan Prompt flow.

    ![Mulakan sesi pengiraan.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.ms.png)

1. Pilih **Validate and parse input** untuk memperbaharui parameter.

    ![Sahkan input.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.ms.png)

1. Pilih **Value** bagi **connection** ke sambungan khusus yang anda cipta. Sebagai contoh, *connection*.

    ![Sambungan.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.ms.png)

#### Berinteraksi dengan model khusus anda

1. Pilih **Chat**.

    ![Pilih chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.ms.png)

1. Berikut adalah contoh hasil: Kini anda boleh berinteraksi dengan model Phi-3 khusus anda. Disarankan untuk mengemukakan soalan berdasarkan data yang digunakan untuk penyesuaian.

    ![Berinteraksi dengan prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.ms.png)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.