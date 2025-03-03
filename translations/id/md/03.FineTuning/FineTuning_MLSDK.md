## Cara Menggunakan Komponen Chat-Completion dari Azure ML System Registry untuk Fine-Tune Model

Dalam contoh ini, kita akan melakukan fine-tuning pada model Phi-3-mini-4k-instruct untuk melengkapi percakapan antara dua orang menggunakan dataset ultrachat_200k.

![MLFineTune](../../../../translated_images/MLFineTune.d8292fe1f146b4ff1153c2e5bdbbe5b0e7f96858d5054b525bd55f2641505138.id.png)

Contoh ini akan menunjukkan cara melakukan fine-tuning menggunakan Azure ML SDK dan Python, kemudian mendistribusikan model yang telah di-fine-tune ke endpoint online untuk inferensi real-time.

### Data Pelatihan

Kita akan menggunakan dataset ultrachat_200k. Dataset ini adalah versi yang sangat terfilter dari dataset UltraChat dan digunakan untuk melatih Zephyr-7B-β, sebuah model chat 7B canggih.

### Model

Kita akan menggunakan model Phi-3-mini-4k-instruct untuk menunjukkan bagaimana pengguna dapat melakukan fine-tuning pada model untuk tugas chat-completion. Jika Anda membuka notebook ini dari kartu model tertentu, ingatlah untuk mengganti nama model spesifik tersebut.

### Tugas

- Pilih model untuk di-fine-tune.
- Pilih dan eksplorasi data pelatihan.
- Konfigurasikan pekerjaan fine-tuning.
- Jalankan pekerjaan fine-tuning.
- Tinjau metrik pelatihan dan evaluasi.
- Registrasi model yang telah di-fine-tune.
- Distribusikan model yang telah di-fine-tune untuk inferensi real-time.
- Bersihkan sumber daya.

## 1. Persiapan Awal

- Instal dependensi.
- Hubungkan ke AzureML Workspace. Pelajari lebih lanjut di pengaturan autentikasi SDK. Ganti <WORKSPACE_NAME>, <RESOURCE_GROUP>, dan <SUBSCRIPTION_ID> di bawah ini.
- Hubungkan ke sistem registry AzureML.
- Tetapkan nama eksperimen opsional.
- Periksa atau buat komputasi.

> [!NOTE]
> Persyaratan: satu node GPU dapat memiliki beberapa kartu GPU. Misalnya, dalam satu node Standard_NC24rs_v3 terdapat 4 GPU NVIDIA V100, sedangkan di Standard_NC12s_v3 terdapat 2 GPU NVIDIA V100. Lihat dokumen untuk informasi ini. Jumlah kartu GPU per node diatur dalam parameter gpus_per_node di bawah ini. Menyetel nilai ini dengan benar akan memastikan pemanfaatan semua GPU dalam node. SKU komputasi GPU yang direkomendasikan dapat ditemukan di sini dan di sini.

### Pustaka Python

Instal dependensi dengan menjalankan sel di bawah ini. Langkah ini wajib dilakukan jika dijalankan di lingkungan baru.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Berinteraksi dengan Azure ML

1. Skrip Python ini digunakan untuk berinteraksi dengan layanan Azure Machine Learning (Azure ML). Berikut adalah penjelasan tentang apa yang dilakukan:

    - Mengimpor modul yang diperlukan dari paket azure.ai.ml, azure.identity, dan azure.ai.ml.entities. Juga mengimpor modul time.

    - Mencoba melakukan autentikasi menggunakan DefaultAzureCredential(), yang menyediakan pengalaman autentikasi yang disederhanakan untuk memulai pengembangan aplikasi di cloud Azure. Jika gagal, akan menggunakan InteractiveBrowserCredential(), yang menyediakan prompt login interaktif.

    - Selanjutnya mencoba membuat instance MLClient menggunakan metode from_config, yang membaca konfigurasi dari file config default (config.json). Jika gagal, akan membuat instance MLClient secara manual dengan menyediakan subscription_id, resource_group_name, dan workspace_name.

    - Membuat instance MLClient lain untuk registry Azure ML bernama "azureml". Registry ini adalah tempat model, pipeline fine-tuning, dan lingkungan disimpan.

    - Menetapkan experiment_name menjadi "chat_completion_Phi-3-mini-4k-instruct".

    - Menghasilkan timestamp unik dengan mengonversi waktu saat ini (dalam detik sejak epoch, sebagai angka floating point) menjadi integer dan kemudian menjadi string. Timestamp ini dapat digunakan untuk membuat nama dan versi unik.

    ```python
    # Import necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import time module
    
    # Try to authenticate using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try to create an MLClient instance using the default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If that fails, create an MLClient instance by manually providing the details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create another MLClient instance for the Azure ML registry named "azureml"
    # This registry is where models, fine-tuning pipelines, and environments are stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set the experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate a unique timestamp that can be used for names and versions that need to be unique
    timestamp = str(int(time.time()))
    ```

## 2. Pilih Model Dasar untuk Fine-Tuning

1. Phi-3-mini-4k-instruct adalah model ringan dengan 3.8 miliar parameter, model canggih berbasis dataset yang digunakan untuk Phi-2. Model ini termasuk dalam keluarga model Phi-3, dan versi Mini hadir dalam dua varian 4K dan 128K yang merupakan panjang konteks (dalam token) yang dapat didukung. Kita perlu melakukan fine-tuning model ini untuk tujuan spesifik kita. Anda dapat menelusuri model-model ini di Model Catalog di AzureML Studio dengan memfilter berdasarkan tugas chat-completion. Dalam contoh ini, kita menggunakan model Phi-3-mini-4k-instruct. Jika Anda membuka notebook ini untuk model lain, ganti nama dan versinya sesuai kebutuhan.

    > [!NOTE]
    > Properti id model adalah model id. Ini akan diteruskan sebagai input ke pekerjaan fine-tuning. Properti ini juga tersedia sebagai field Asset ID di halaman detail model di AzureML Studio Model Catalog.

2. Skrip Python ini berinteraksi dengan layanan Azure Machine Learning (Azure ML). Berikut adalah penjelasan tentang apa yang dilakukan:

    - Menetapkan model_name menjadi "Phi-3-mini-4k-instruct".

    - Menggunakan metode get dari properti models pada objek registry_ml_client untuk mengambil versi terbaru dari model dengan nama yang ditentukan dari registry Azure ML. Metode get dipanggil dengan dua argumen: nama model dan label yang menentukan bahwa versi terbaru dari model harus diambil.

    - Mencetak pesan ke konsol yang menunjukkan nama, versi, dan id model yang akan digunakan untuk fine-tuning. Metode format dari string digunakan untuk memasukkan nama, versi, dan id model ke dalam pesan. Nama, versi, dan id model diakses sebagai properti dari objek foundation_model.

    ```python
    # Set the model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Get the latest version of the model from the Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print the model name, version, and id
    # This information is useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Buat Komputasi untuk Digunakan dengan Pekerjaan

Pekerjaan fine-tune HANYA bekerja dengan komputasi GPU. Ukuran komputasi tergantung pada seberapa besar model, dan dalam banyak kasus menjadi rumit untuk mengidentifikasi komputasi yang tepat untuk pekerjaan tersebut. Dalam sel ini, kami membimbing pengguna untuk memilih komputasi yang tepat untuk pekerjaan tersebut.

> [!NOTE]
> Komputasi yang tercantum di bawah ini bekerja dengan konfigurasi yang paling dioptimalkan. Perubahan apa pun pada konfigurasi dapat menyebabkan kesalahan Cuda Out Of Memory. Dalam kasus seperti itu, coba tingkatkan komputasi ke ukuran komputasi yang lebih besar.

> [!NOTE]
> Saat memilih compute_cluster_size di bawah ini, pastikan komputasi tersedia di grup sumber daya Anda. Jika komputasi tertentu tidak tersedia, Anda dapat membuat permintaan untuk mendapatkan akses ke sumber daya komputasi.

### Memeriksa Model untuk Dukungan Fine-Tuning

1. Skrip Python ini berinteraksi dengan model Azure Machine Learning (Azure ML). Berikut adalah penjelasan tentang apa yang dilakukan:

    - Mengimpor modul ast, yang menyediakan fungsi untuk memproses pohon dari grammar sintaks abstrak Python.

    - Memeriksa apakah objek foundation_model (yang mewakili model di Azure ML) memiliki tag bernama finetune_compute_allow_list. Tag di Azure ML adalah pasangan kunci-nilai yang dapat Anda buat dan gunakan untuk memfilter dan mengurutkan model.

    - Jika tag finetune_compute_allow_list ada, menggunakan fungsi ast.literal_eval untuk secara aman mengurai nilai tag (string) menjadi daftar Python. Daftar ini kemudian ditetapkan ke variabel computes_allow_list. Kemudian mencetak pesan yang menunjukkan bahwa komputasi harus dibuat dari daftar.

    - Jika tag finetune_compute_allow_list tidak ada, menetapkan computes_allow_list menjadi None dan mencetak pesan yang menunjukkan bahwa tag finetune_compute_allow_list bukan bagian dari tag model.

    - Singkatnya, skrip ini memeriksa tag tertentu dalam metadata model, mengonversi nilai tag menjadi daftar jika ada, dan memberikan umpan balik kepada pengguna sesuai kebutuhan.

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Check if the 'finetune_compute_allow_list' tag is present in the model's tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert string to python list
        # Print a message indicating that a compute should be created from the list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If the tag is not present, set computes_allow_list to None
        computes_allow_list = None
        # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Memeriksa Instance Komputasi

1. Skrip Python ini berinteraksi dengan layanan Azure Machine Learning (Azure ML) dan melakukan beberapa pemeriksaan pada instance komputasi. Berikut adalah penjelasan tentang apa yang dilakukan:

    - Mencoba mengambil instance komputasi dengan nama yang disimpan dalam compute_cluster dari workspace Azure ML. Jika status provisioning instance komputasi adalah "failed", maka akan memunculkan ValueError.

    - Memeriksa apakah computes_allow_list bukan None. Jika tidak, mengonversi semua ukuran komputasi dalam daftar menjadi huruf kecil dan memeriksa apakah ukuran instance komputasi saat ini ada dalam daftar. Jika tidak, akan memunculkan ValueError.

    - Jika computes_allow_list adalah None, memeriksa apakah ukuran instance komputasi ada dalam daftar ukuran GPU VM yang tidak didukung. Jika ada, akan memunculkan ValueError.

    - Mengambil daftar semua ukuran komputasi yang tersedia di workspace. Kemudian iterasi melalui daftar ini, dan untuk setiap ukuran komputasi, memeriksa apakah namanya cocok dengan ukuran instance komputasi saat ini. Jika cocok, mengambil jumlah GPU untuk ukuran komputasi tersebut dan menetapkan gpu_count_found menjadi True.

    - Jika gpu_count_found adalah True, mencetak jumlah GPU dalam instance komputasi. Jika gpu_count_found adalah False, akan memunculkan ValueError.

    - Singkatnya, skrip ini melakukan beberapa pemeriksaan pada instance komputasi di workspace Azure ML, termasuk memeriksa status provisioning-nya, ukurannya terhadap daftar yang diperbolehkan atau tidak diperbolehkan, dan jumlah GPU yang dimilikinya.

    ```python
    # Print the exception message
    print(e)
    # Raise a ValueError if the compute size is not available in the workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve the compute instance from the Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if the provisioning state of the compute instance is "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise a ValueError if the provisioning state is "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list is not None
    if computes_allow_list is not None:
        # Convert all compute sizes in computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if the size of the compute instance is in computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define a list of unsupported GPU VM sizes
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if the size of the compute instance is in unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize a flag to check if the number of GPUs in the compute instance has been found
    gpu_count_found = False
    # Retrieve a list of all available compute sizes in the workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterate over the list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if the name of the compute size matches the size of the compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found is True, print the number of GPUs in the compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found is False, raise a ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Pilih Dataset untuk Fine-Tuning Model

1. Kita menggunakan dataset ultrachat_200k. Dataset ini memiliki empat pembagian, cocok untuk fine-tuning terawasi (sft).
Generation ranking (gen). Jumlah contoh per pembagian ditampilkan sebagai berikut:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Beberapa sel berikutnya menunjukkan persiapan data dasar untuk fine-tuning:

### Visualisasikan Beberapa Baris Data

Kita ingin sampel ini berjalan dengan cepat, jadi simpan file train_sft dan test_sft yang berisi 5% dari baris yang sudah dipangkas. Artinya, model yang telah di-fine-tune akan memiliki akurasi lebih rendah, sehingga tidak boleh digunakan untuk dunia nyata.  
Skrip download-dataset.py digunakan untuk mengunduh dataset ultrachat_200k dan mengubah dataset menjadi format yang dapat dikonsumsi oleh komponen pipeline fine-tune. Karena dataset ini besar, di sini kita hanya menggunakan sebagian dataset.

1. Menjalankan skrip di bawah ini hanya akan mengunduh 5% data. Persentase ini dapat ditingkatkan dengan mengubah parameter dataset_split_pc ke persentase yang diinginkan.

    > [!NOTE]
    > Beberapa model bahasa memiliki kode bahasa yang berbeda sehingga nama kolom dalam dataset harus mencerminkan hal ini.

1. Berikut adalah contoh bagaimana data harus terlihat.  
Dataset chat-completion disimpan dalam format parquet dengan setiap entri menggunakan skema berikut:

    - Ini adalah dokumen JSON (JavaScript Object Notation), yang merupakan format pertukaran data yang populer. Ini bukan kode yang dapat dieksekusi, tetapi cara untuk menyimpan dan mengangkut data. Berikut adalah penjelasan strukturnya:

    - "prompt": Kunci ini berisi nilai string yang mewakili tugas atau pertanyaan yang diajukan kepada asisten AI.

    - "messages": Kunci ini berisi array objek. Setiap objek mewakili pesan dalam percakapan antara pengguna dan asisten AI. Setiap objek pesan memiliki dua kunci:

    - "content": Kunci ini berisi nilai string yang mewakili isi pesan.
    - "role": Kunci ini berisi nilai string yang mewakili peran entitas yang mengirim pesan. Bisa berupa "user" atau "assistant".
    - "prompt_id": Kunci ini berisi nilai string yang mewakili pengenal unik untuk prompt.

1. Dalam dokumen JSON spesifik ini, percakapan direpresentasikan di mana pengguna meminta asisten AI untuk membuat protagonis untuk cerita distopia. Asisten merespons, dan pengguna kemudian meminta detail lebih lanjut. Asisten setuju untuk memberikan detail lebih lanjut. Seluruh percakapan dikaitkan dengan prompt id tertentu.

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### Unduh Data

1. Skrip Python ini digunakan untuk mengunduh dataset menggunakan skrip pembantu bernama download-dataset.py. Berikut adalah penjelasan tentang apa yang dilakukan:

    - Mengimpor modul os, yang menyediakan cara portabel untuk menggunakan fungsi yang bergantung pada sistem operasi.

    - Menggunakan fungsi os.system untuk menjalankan skrip download-dataset.py di shell dengan argumen baris perintah tertentu. Argumen menentukan dataset yang akan diunduh (HuggingFaceH4/ultrachat_200k), direktori tempat dataset akan diunduh (ultrachat_200k_dataset), dan persentase dataset yang akan dipisah (5). Fungsi os.system mengembalikan status keluar dari perintah yang dieksekusi; status ini disimpan dalam variabel exit_status.

    - Memeriksa apakah exit_status bukan 0. Dalam sistem operasi mirip Unix, status keluar 0 biasanya menunjukkan bahwa perintah berhasil, sedangkan angka lain menunjukkan kesalahan. Jika exit_status bukan 0, akan memunculkan Exception dengan pesan yang menunjukkan bahwa ada kesalahan saat mengunduh dataset.

    - Singkatnya, skrip ini menjalankan perintah untuk mengunduh dataset menggunakan skrip pembantu dan memunculkan pengecualian jika perintah gagal.

    ```python
    # Import the os module, which provides a way of using operating system dependent functionality
    import os
    
    # Use the os.system function to run the download-dataset.py script in the shell with specific command-line arguments
    # The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5)
    # The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Check if exit_status is not 0
    # In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error
    # If exit_status is not 0, raise an Exception with a message indicating that there was an error downloading the dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Memuat Data ke DataFrame

1. Skrip Python ini memuat file JSON Lines ke dalam DataFrame pandas dan menampilkan 5 baris pertama. Berikut adalah penjelasan tentang apa yang dilakukan:

    - Mengimpor pustaka pandas, yang merupakan pustaka manipulasi dan analisis data yang kuat.

    - Menetapkan lebar kolom maksimum untuk opsi tampilan pandas menjadi 0. Ini berarti teks penuh dari setiap kolom akan ditampilkan tanpa pemotongan saat DataFrame dicetak.

    - Menggunakan fungsi pd.read_json untuk memuat file train_sft.jsonl dari direktori ultrachat_200k_dataset ke dalam DataFrame. Argumen lines=True menunjukkan bahwa file tersebut dalam format JSON Lines, di mana setiap baris adalah objek JSON terpisah.

    - Menggunakan metode head untuk menampilkan 5 baris pertama dari DataFrame. Jika DataFrame memiliki kurang dari 5 baris, semua baris akan ditampilkan.

    - Singkatnya, skrip ini memuat file JSON Lines ke dalam DataFrame dan menampilkan 5 baris pertama dengan teks kolom penuh.

    ```python
    # Import the pandas library, which is a powerful data manipulation and analysis library
    import pandas as pd
    
    # Set the maximum column width for pandas' display options to 0
    # This means that the full text of each column will be displayed without truncation when the DataFrame is printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
    # The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use the head method to display the first 5 rows of the DataFrame
    # If the DataFrame has less than 5 rows, it will display all of them
    df.head()
    ```

## 5. Kirim Pekerjaan Fine-Tuning Menggunakan Model dan Data sebagai Input

Buat pekerjaan yang menggunakan komponen pipeline chat-completion. Pelajari lebih lanjut tentang semua parameter yang didukung untuk fine-tuning.

### Tentukan Parameter Fine-Tune

1. Parameter fine-tune dapat dikelompokkan menjadi 2 kategori - parameter pelatihan dan parameter optimasi.

1. Parameter pelatihan mendefinisikan aspek pelatihan seperti:

    - Optimizer dan scheduler yang akan digunakan.
    - Metrik untuk mengoptimalkan fine-tuning.
    - Jumlah langkah pelatihan, ukuran batch, dan sebagainya.
    - Parameter optimasi membantu mengoptimalkan memori GPU dan menggunakan sumber daya komputasi secara efektif.

1. Di bawah ini adalah beberapa parameter yang termasuk dalam kategori ini. Parameter optimasi berbeda untuk setiap model dan dikemas bersama model untuk menangani variasi ini.

    - Aktifkan deepspeed dan LoRA.
    - Aktifkan pelatihan presisi campuran.
    - Aktifkan pelatihan multi-node.

> [!NOTE]
> Fine-tuning terawasi dapat menyebabkan kehilangan alignment atau lupa yang bersifat destruktif. Kami merekomendasikan untuk memeriksa masalah ini dan menjalankan tahap alignment setelah Anda melakukan fine-tuning.

### Parameter Fine-Tuning

1. Skrip Python ini mengatur parameter untuk fine-tuning model pembelajaran mesin. Berikut adalah penjelasan tentang apa yang dilakukan:

    - Mengatur parameter pelatihan default seperti jumlah epoch pelatihan, ukuran batch untuk pelatihan dan evaluasi, learning rate, dan jenis scheduler learning rate.

    - Mengatur parameter optimasi default seperti apakah Layer-wise Relevance Propagation (LoRa) dan DeepSpeed diterapkan, serta tahap DeepSpeed.

    - Menggabungkan parameter pelatihan dan optimasi ke dalam satu dictionary yang disebut finetune_parameters.

    - Memeriksa apakah foundation_model memiliki parameter default spesifik model. Jika ada, mencetak pesan peringatan dan memperbarui dictionary finetune_parameters dengan default spesifik model ini. Fungsi ast.literal_eval digunakan untuk mengonversi default spesifik model dari string menjadi dictionary Python.

    - Mencetak set parameter fine-tuning akhir yang akan digunakan untuk menjalankan.

    - Singkatnya, skrip ini mengatur dan menampilkan parameter untuk fine-tuning model pembelajaran mesin, dengan kemampuan untuk menggantikan parameter default dengan parameter spesifik model.

    ```python
    # Set up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Set up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Combine the training and optimization parameters into a single dictionary called finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Check if the foundation_model has any model-specific default parameters
    # If it does, print a warning message and update the finetune_parameters dictionary with these model-specific defaults
    # The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # convert string to python dict
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Print the final set of fine-tuning parameters that will be used for the run
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Pipeline Pelatihan

1. Skrip Python ini mendefinisikan fungsi untuk menghasilkan nama tampilan untuk pipeline pelatihan pembelajaran mesin, kemudian memanggil fungsi ini untuk menghasilkan dan mencetak nama tampilan. Berikut adalah penjelasan tentang apa yang dilakukan:

    1. Fungsi get_pipeline_display_name didefinisikan. Fungsi ini menghasilkan nama tampilan berdasarkan berbagai parameter yang terkait dengan pipeline pelatihan.

    1. Di dalam fungsi, menghitung total ukuran batch dengan mengalikan ukuran batch per perangkat, jumlah langkah akumulasi gradien, jumlah GPU per node, dan jumlah node yang digunakan untuk fine-tuning.

    1. Mengambil berbagai parameter lain seperti jenis scheduler learning rate, apakah DeepSpeed diterapkan, tahap DeepSpeed, apakah Layer-wise Relevance Propagation (LoRa) diterapkan, batas jumlah checkpoint model yang akan disimpan, dan panjang urutan maksimum.

    1. Membuat string yang mencakup semua parameter ini, dipisahkan oleh tanda hubung. Jika DeepSpeed atau LoRa diterapkan, string mencakup "ds" diikuti oleh tahap DeepSpeed, atau "lora", masing-masing. Jika tidak, string mencakup "nods" atau "nolora", masing-masing.

    1. Fungsi ini mengembalikan string ini, yang berfungsi sebagai nama tampilan untuk pipeline pelatihan.

    1. Setelah fungsi didefinisikan, fungsi ini dipanggil untuk menghasilkan nama tampilan, yang kemudian dicetak.

    1. Singkatnya, skrip ini menghasilkan nama tampilan untuk pipeline pelatihan pembelajaran mesin.
## Pipeline Pelatihan Berdasarkan Berbagai Parameter

Script ini mencetak nama tampilan pipeline pelatihan berdasarkan berbagai parameter. ```python
    # Define a function to generate a display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Retrieve the learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Retrieve whether DeepSpeed is applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Retrieve the DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Retrieve the limit on the number of model checkpoints to keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Retrieve the maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct the display name by concatenating all these parameters, separated by hyphens
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Call the function to generate the display name
    pipeline_display_name = get_pipeline_display_name()
    # Print the display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Mengonfigurasi Pipeline

Script Python ini mendefinisikan dan mengonfigurasi pipeline machine learning menggunakan Azure Machine Learning SDK. Berikut adalah penjelasan langkah-langkahnya:

1. Mengimpor modul yang diperlukan dari Azure AI ML SDK.  
2. Mengambil komponen pipeline bernama "chat_completion_pipeline" dari registry.  
3. Mendefinisikan pekerjaan pipeline menggunakan `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False`, yang berarti pipeline akan berhenti jika ada langkah yang gagal.  
4. Singkatnya, script ini mendefinisikan dan mengonfigurasi pipeline machine learning untuk tugas penyelesaian percakapan menggunakan Azure Machine Learning SDK.  

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch the pipeline component named "chat_completion_pipeline" from the registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define the pipeline job using the @pipeline decorator and the function create_pipeline
    # The name of the pipeline is set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize the fetched pipeline component with various parameters
        # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map the dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
            **finetune_parameters
        )
        return {
            # Map the output of the fine tuning job to the output of pipeline job
            # This is done so that we can easily register the fine tuned model
            # Registering the model is required to deploy the model to an online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create an instance of the pipeline by calling the create_pipeline function
    pipeline_object = create_pipeline()
    
    # Don't use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # This means that the pipeline will stop if any step fails
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Kirim Pekerjaan

1. Script Python ini mengirimkan pekerjaan pipeline machine learning ke workspace Azure Machine Learning dan menunggu pekerjaan selesai. Berikut adalah penjelasannya:

   - Memanggil metode `create_or_update` dari objek jobs di `workspace_ml_client` untuk mengirimkan pekerjaan pipeline. Pipeline yang akan dijalankan ditentukan oleh `pipeline_object`, dan eksperimen di mana pekerjaan dijalankan ditentukan oleh `experiment_name`.  
   - Memanggil metode `stream` dari objek jobs di `workspace_ml_client` untuk menunggu pekerjaan pipeline selesai. Pekerjaan yang ditunggu ditentukan oleh atribut `name` dari objek `pipeline_job`.  
   - Singkatnya, script ini mengirimkan pekerjaan pipeline machine learning ke workspace Azure Machine Learning, lalu menunggu pekerjaan selesai.  

```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Mendaftarkan Model yang Telah Disesuaikan ke Workspace

Kita akan mendaftarkan model dari output pekerjaan penyesuaian. Ini akan melacak keterkaitan antara model yang disesuaikan dan pekerjaan penyesuaian. Pekerjaan penyesuaian juga melacak keterkaitan dengan model dasar, data, dan kode pelatihan.

### Mendaftarkan Model ML

1. Script Python ini mendaftarkan model machine learning yang telah dilatih dalam pipeline Azure Machine Learning. Berikut adalah penjelasannya:

   - Mengimpor modul yang diperlukan dari Azure AI ML SDK.  
   - Memeriksa apakah output `trained_model` tersedia dari pekerjaan pipeline dengan memanggil metode `get` dari objek jobs di `workspace_ml_client` dan mengakses atribut `outputs`.  
   - Membuat path ke model yang dilatih dengan memformat string menggunakan nama pekerjaan pipeline dan nama output ("trained_model").  
   - Mendefinisikan nama untuk model yang telah disesuaikan dengan menambahkan "-ultrachat-200k" ke nama model asli dan mengganti semua garis miring dengan tanda hubung.  
   - Mempersiapkan pendaftaran model dengan membuat objek `Model` dengan berbagai parameter, termasuk path ke model, jenis model (model MLflow), nama dan versi model, serta deskripsi model.  
   - Mendaftarkan model dengan memanggil metode `create_or_update` dari objek models di `workspace_ml_client` dengan objek `Model` sebagai argumen.  
   - Mencetak model yang telah terdaftar.  

   - Singkatnya, script ini mendaftarkan model machine learning yang telah dilatih dalam pipeline Azure Machine Learning.  

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if the `trained_model` output is available from the pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register the model by creating a Model object with various parameters
    # These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version to avoid version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print the registered model
    print("registered model: \n", registered_model)
    ```

## 7. Menerapkan Model yang Telah Disesuaikan ke Endpoint Online

Endpoint online memberikan API REST yang tahan lama untuk diintegrasikan dengan aplikasi yang memerlukan model tersebut.

### Mengelola Endpoint

1. Script Python ini membuat endpoint online terkelola di Azure Machine Learning untuk model yang telah terdaftar. Berikut adalah penjelasannya:

   - Mengimpor modul yang diperlukan dari Azure AI ML SDK.  
   - Mendefinisikan nama unik untuk endpoint online dengan menambahkan timestamp ke string "ultrachat-completion-".  
   - Mempersiapkan pembuatan endpoint online dengan membuat objek `ManagedOnlineEndpoint` dengan berbagai parameter, termasuk nama endpoint, deskripsi endpoint, dan mode autentikasi ("key").  
   - Membuat endpoint online dengan memanggil metode `begin_create_or_update` dari `workspace_ml_client` dengan objek `ManagedOnlineEndpoint` sebagai argumen. Lalu menunggu operasi pembuatan selesai dengan memanggil metode `wait`.  

   - Singkatnya, script ini membuat endpoint online terkelola di Azure Machine Learning untuk model yang telah terdaftar.  

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
    # These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
    # Then wait for the creation operation to complete by calling the wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]  
> Anda dapat menemukan daftar SKU yang didukung untuk penerapan di sini - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Menerapkan Model ML

1. Script Python ini menerapkan model machine learning yang telah terdaftar ke endpoint online terkelola di Azure Machine Learning. Berikut adalah penjelasannya:

   - Mengimpor modul `ast`, yang menyediakan fungsi untuk memproses pohon sintaks abstrak Python.  
   - Menetapkan tipe instance untuk penerapan ke "Standard_NC6s_v3".  
   - Memeriksa apakah tag `inference_compute_allow_list` ada di model dasar. Jika ada, tag tersebut diubah dari string menjadi daftar Python dan ditetapkan ke `inference_computes_allow_list`. Jika tidak ada, `inference_computes_allow_list` diatur ke None.  
   - Memeriksa apakah tipe instance yang ditentukan ada di daftar yang diizinkan. Jika tidak, mencetak pesan yang meminta pengguna untuk memilih tipe instance dari daftar yang diizinkan.  
   - Mempersiapkan pembuatan penerapan dengan membuat objek `ManagedOnlineDeployment` dengan berbagai parameter, termasuk nama penerapan, nama endpoint, ID model, tipe dan jumlah instance, pengaturan liveness probe, serta pengaturan permintaan.  
   - Membuat penerapan dengan memanggil metode `begin_create_or_update` dari `workspace_ml_client` dengan objek `ManagedOnlineDeployment` sebagai argumen. Lalu menunggu operasi selesai dengan memanggil metode `wait`.  
   - Mengatur lalu lintas endpoint untuk mengarahkan 100% lalu lintas ke penerapan "demo".  
   - Memperbarui endpoint dengan memanggil metode `begin_create_or_update` dari `workspace_ml_client` dengan objek endpoint sebagai argumen. Lalu menunggu pembaruan selesai dengan memanggil metode `result`.  

   - Singkatnya, script ini menerapkan model machine learning yang telah terdaftar ke endpoint online terkelola di Azure Machine Learning.  

```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Set the instance type for the deployment
    instance_type = "Standard_NC6s_v3"
    
    # Check if the `inference_compute_allow_list` tag is present in the foundation model
    if "inference_compute_allow_list" in foundation_model.tags:
        # If it is, convert the tag value from a string to a Python list and assign it to `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If it's not, set `inference_computes_allow_list` to `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Check if the specified instance type is in the allow list
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare to create the deployment by creating a `ManagedOnlineDeployment` object with various parameters
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Create the deployment by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `ManagedOnlineDeployment` object as the argument
    # Then wait for the creation operation to complete by calling the `wait` method
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment
    endpoint.traffic = {"demo": 100}
    
    # Update the endpoint by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `endpoint` object as the argument
    # Then wait for the update operation to complete by calling the `result` method
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Menguji Endpoint dengan Data Contoh

Kita akan mengambil beberapa data contoh dari dataset pengujian dan mengirimkannya ke endpoint online untuk inferensi. Kita kemudian akan menampilkan label yang telah dinilai bersama dengan label kebenaran dasar.

### Membaca Hasil

1. Script Python ini membaca file JSON Lines ke dalam DataFrame pandas, mengambil sampel acak, dan mengatur ulang indeks. Berikut adalah penjelasannya:

   - Membaca file `./ultrachat_200k_dataset/test_gen.jsonl` ke dalam DataFrame pandas. Fungsi `read_json` digunakan dengan argumen `lines=True` karena file tersebut dalam format JSON Lines, di mana setiap baris adalah objek JSON terpisah.  
   - Mengambil sampel acak 1 baris dari DataFrame. Fungsi `sample` digunakan dengan argumen `n=1` untuk menentukan jumlah baris acak yang dipilih.  
   - Mengatur ulang indeks DataFrame. Fungsi `reset_index` digunakan dengan argumen `drop=True` untuk menghapus indeks asli dan menggantinya dengan indeks baru berupa nilai integer default.  
   - Menampilkan 2 baris pertama dari DataFrame menggunakan fungsi `head` dengan argumen 2. Namun, karena DataFrame hanya berisi satu baris setelah pengambilan sampel, hanya baris itu yang akan ditampilkan.  

   - Singkatnya, script ini membaca file JSON Lines ke dalam DataFrame pandas, mengambil sampel acak 1 baris, mengatur ulang indeks, dan menampilkan baris pertama.  

```python
    # Import pandas library
    import pandas as pd
    
    # Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' into a pandas DataFrame
    # The 'lines=True' argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Take a random sample of 1 row from the DataFrame
    # The 'n=1' argument specifies the number of random rows to select
    test_df = test_df.sample(n=1)
    
    # Reset the index of the DataFrame
    # The 'drop=True' argument indicates that the original index should be dropped and replaced with a new index of default integer values
    # The 'inplace=True' argument indicates that the DataFrame should be modified in place (without creating a new object)
    test_df.reset_index(drop=True, inplace=True)
    
    # Display the first 2 rows of the DataFrame
    # However, since the DataFrame only contains one row after the sampling, this will only display that one row
    test_df.head(2)
    ```

### Membuat Objek JSON

1. Script Python ini membuat objek JSON dengan parameter tertentu dan menyimpannya ke dalam file. Berikut adalah penjelasannya:

   - Mengimpor modul `json`, yang menyediakan fungsi untuk bekerja dengan data JSON.  
   - Membuat dictionary `parameters` dengan kunci dan nilai yang mewakili parameter untuk model machine learning. Kuncinya adalah "temperature", "top_p", "do_sample", dan "max_new_tokens", dengan nilai masing-masing 0.6, 0.9, True, dan 200.  
   - Membuat dictionary lain `test_json` dengan dua kunci: "input_data" dan "params". Nilai dari "input_data" adalah dictionary lain dengan kunci "input_string" dan "parameters". Nilai dari "input_string" adalah daftar yang berisi pesan pertama dari DataFrame `test_df`. Nilai dari "parameters" adalah dictionary `parameters` yang dibuat sebelumnya. Nilai dari "params" adalah dictionary kosong.  
   - Membuka file bernama `sample_score.json`.  

```python
    # Import the json module, which provides functions to work with JSON data
    import json
    
    # Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
    # The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` with two keys: "input_data" and "params"
    # The value of "input_data" is another dictionary with keys "input_string" and "parameters"
    # The value of "input_string" is a list containing the first message from the `test_df` DataFrame
    # The value of "parameters" is the `parameters` dictionary created earlier
    # The value of "params" is an empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
        json.dump(test_json, f)
    ```

### Memanggil Endpoint

1. Script Python ini memanggil endpoint online di Azure Machine Learning untuk menilai file JSON. Berikut adalah penjelasannya:

   - Memanggil metode `invoke` dari properti `online_endpoints` dari objek `workspace_ml_client`. Metode ini digunakan untuk mengirim permintaan ke endpoint online dan mendapatkan respons.  
   - Menentukan nama endpoint dan penerapan dengan argumen `endpoint_name` dan `deployment_name`. Dalam hal ini, nama endpoint disimpan dalam variabel `online_endpoint_name` dan nama penerapan adalah "demo".  
   - Menentukan path ke file JSON yang akan dinilai dengan argumen `request_file`. Dalam hal ini, file tersebut adalah `./ultrachat_200k_dataset/sample_score.json`.  
   - Menyimpan respons dari endpoint ke dalam variabel `response`.  
   - Mencetak respons mentah.  

   - Singkatnya, script ini memanggil endpoint online di Azure Machine Learning untuk menilai file JSON dan mencetak responsnya.  

```python
    # Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
    # The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
    # The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
    # The `deployment_name` argument specifies the name of the deployment, which is "demo"
    # The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Print the raw response from the endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. Menghapus Endpoint Online

1. Jangan lupa untuk menghapus endpoint online, jika tidak, meteran penagihan akan tetap berjalan untuk komputasi yang digunakan oleh endpoint. Baris kode Python ini menghapus endpoint online di Azure Machine Learning. Berikut adalah penjelasannya:

   - Memanggil metode `begin_delete` dari properti `online_endpoints` dari objek `workspace_ml_client`. Metode ini digunakan untuk memulai penghapusan endpoint online.  
   - Menentukan nama endpoint yang akan dihapus dengan argumen `name`. Dalam hal ini, nama endpoint disimpan dalam variabel `online_endpoint_name`.  
   - Memanggil metode `wait` untuk menunggu operasi penghapusan selesai. Ini adalah operasi pemblokiran, yang berarti script tidak akan dilanjutkan sampai penghapusan selesai.  

   - Singkatnya, baris kode ini memulai penghapusan endpoint online di Azure Machine Learning dan menunggu operasi selesai.  

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat krusial, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.