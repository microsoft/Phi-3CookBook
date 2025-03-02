# Makmal. Optimumkan Model AI untuk Inferens Di Peranti

## Pengenalan 

> [!IMPORTANT]
> Makmal ini memerlukan **GPU Nvidia A10 atau A100** dengan pemacu yang berkaitan dan toolkit CUDA (versi 12+) dipasang.

> [!NOTE]
> Makmal ini mengambil masa **35 minit** dan akan memberi anda pengenalan praktikal kepada konsep utama dalam mengoptimumkan model untuk inferens di peranti menggunakan OLIVE.

## Objektif Pembelajaran

Pada akhir makmal ini, anda akan dapat menggunakan OLIVE untuk:

- Melakukan kuantisasi model AI menggunakan kaedah kuantisasi AWQ.
- Melaraskan model AI untuk tugas tertentu.
- Menjana penyesuai LoRA (model yang telah dilaraskan) untuk inferens di peranti yang cekap menggunakan ONNX Runtime.

### Apa itu Olive

Olive (*O*NNX *live*) ialah toolkit pengoptimuman model dengan CLI yang menyertainya yang membolehkan anda menyediakan model untuk ONNX runtime +++https://onnxruntime.ai+++ dengan kualiti dan prestasi.

![Aliran Olive](../../../../../translated_images/olive-flow.e4682fa65f77777f49e884482fa8dd83eadcb90904fcb41a54093af85c330060.ms.png)

Input kepada Olive biasanya merupakan model PyTorch atau Hugging Face dan outputnya adalah model ONNX yang telah dioptimumkan yang dijalankan pada peranti (sasaran penyebaran) menggunakan ONNX runtime. Olive akan mengoptimumkan model berdasarkan pemecut AI sasaran penyebaran (NPU, GPU, CPU) yang disediakan oleh vendor perkakasan seperti Qualcomm, AMD, Nvidia atau Intel.

Olive melaksanakan *workflow*, iaitu urutan teratur tugas pengoptimuman model individu yang dipanggil *passes* - contoh passes termasuk: pemampatan model, penangkapan graf, kuantisasi, pengoptimuman graf. Setiap pass mempunyai satu set parameter yang boleh diselaraskan untuk mencapai metrik terbaik, seperti ketepatan dan kependaman, yang dinilai oleh evaluator masing-masing. Olive menggunakan strategi pencarian dengan algoritma pencarian untuk melaraskan setiap pass secara automatik satu persatu atau beberapa pass bersama.

#### Manfaat Olive

- **Mengurangkan kekecewaan dan masa** percubaan dan kesilapan secara manual dengan pelbagai teknik untuk pengoptimuman graf, pemampatan dan kuantisasi. Tetapkan kekangan kualiti dan prestasi anda dan biarkan Olive secara automatik mencari model terbaik untuk anda.
- **40+ komponen pengoptimuman model terbina dalam** yang merangkumi teknik terkini dalam kuantisasi, pemampatan, pengoptimuman graf dan pelarasan.
- **CLI yang mudah digunakan** untuk tugas pengoptimuman model biasa. Sebagai contoh, olive quantize, olive auto-opt, olive finetune.
- Pembungkusan dan penyebaran model yang sudah terintegrasi.
- Menyokong penjanaan model untuk **Multi LoRA serving**.
- Membina workflow menggunakan YAML/JSON untuk mengatur tugas pengoptimuman dan penyebaran model.
- Integrasi dengan **Hugging Face** dan **Azure AI**.
- Mekanisme **caching** terbina dalam untuk **menjimatkan kos**.

## Arahan Makmal
> [!NOTE]
> Pastikan anda telah menyediakan Azure AI Hub dan Projek anda serta menetapkan komputasi A100 seperti yang dijelaskan dalam Makmal 1.

### Langkah 0: Sambung ke Azure AI Compute anda

Anda akan menyambung ke Azure AI compute menggunakan ciri jarak jauh dalam **VS Code.** 

1. Buka aplikasi desktop **VS Code** anda:
1. Buka **command palette** menggunakan **Shift+Ctrl+P**.
1. Dalam command palette, cari **AzureML - remote: Connect to compute instance in New Window**.
1. Ikuti arahan di skrin untuk menyambung ke Compute. Ini melibatkan memilih Langganan Azure, Kumpulan Sumber, Projek dan Nama Compute yang telah anda tetapkan dalam Makmal 1.
1. Setelah anda disambungkan ke nod Azure ML Compute anda, ini akan dipaparkan di **bahagian bawah kiri Visual Code** `><Azure ML: Compute Name`

### Langkah 1: Klon repositori ini

Dalam VS Code, anda boleh membuka terminal baru dengan **Ctrl+J** dan klon repositori ini:

Dalam terminal anda akan melihat prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
Klon penyelesaian 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Langkah 2: Buka Folder dalam VS Code

Untuk membuka VS Code dalam folder yang berkaitan, jalankan arahan berikut dalam terminal, yang akan membuka tetingkap baru:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Sebagai alternatif, anda boleh membuka folder dengan memilih **File** > **Open Folder**. 

### Langkah 3: Kebergantungan

Buka tetingkap terminal dalam VS Code dalam Instance Azure AI Compute anda (tip: **Ctrl+J**) dan jalankan arahan berikut untuk memasang kebergantungan:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Ia akan mengambil masa ~5 minit untuk memasang semua kebergantungan.

Dalam makmal ini, anda akan memuat turun dan memuat naik model ke katalog Model Azure AI. Supaya anda boleh mengakses katalog model, anda perlu log masuk ke Azure menggunakan:

```bash
az login
```

> [!NOTE]
> Semasa log masuk, anda akan diminta untuk memilih langganan anda. Pastikan anda menetapkan langganan kepada yang disediakan untuk makmal ini.

### Langkah 4: Jalankan arahan Olive 

Buka tetingkap terminal dalam VS Code dalam Instance Azure AI Compute anda (tip: **Ctrl+J**) dan pastikan persekitaran `olive-ai` conda diaktifkan:

```bash
conda activate olive-ai
```

Seterusnya, jalankan arahan Olive berikut dalam baris arahan.

1. **Periksa data:** Dalam contoh ini, anda akan melaraskan model Phi-3.5-Mini supaya ia pakar dalam menjawab soalan berkaitan perjalanan. Kod di bawah memaparkan beberapa rekod pertama dataset, yang berada dalam format JSON lines:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Kuantisasi model:** Sebelum melatih model, anda terlebih dahulu melakukan kuantisasi dengan arahan berikut yang menggunakan teknik yang dipanggil Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ mengkuantisasi berat model dengan mengambil kira aktivasi yang dihasilkan semasa inferens. Ini bermakna proses kuantisasi mengambil kira taburan data sebenar dalam aktivasi, yang membawa kepada pemeliharaan ketepatan model yang lebih baik berbanding kaedah kuantisasi berat tradisional.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    Ia mengambil masa **~8 minit** untuk melengkapkan kuantisasi AWQ, yang akan **mengurangkan saiz model daripada ~7.5GB kepada ~2.5GB**.
   
   Dalam makmal ini, kami menunjukkan kepada anda cara memasukkan model dari Hugging Face (contohnya: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` arahan melaraskan model yang telah dikuantisasi. Melakukan kuantisasi *sebelum* pelarasan dan bukannya selepas memberikan ketepatan yang lebih baik kerana proses pelarasan memulihkan beberapa kehilangan daripada kuantisasi.
    
    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```
    
    Ia mengambil masa **~6 minit** untuk melengkapkan Pelarasan (dengan 100 langkah).

1. **Optimumkan:** Dengan model yang telah dilatih, anda kini mengoptimumkan model menggunakan arahan `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` Olive - tetapi untuk tujuan makmal ini, kami akan menggunakan CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```
    
    Ia mengambil masa **~5 minit** untuk melengkapkan pengoptimuman.

### Langkah 5: Ujian cepat inferens model

Untuk menguji inferens model, buat fail Python dalam folder anda yang dipanggil **app.py** dan salin-tampal kod berikut:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Jalankan kod menggunakan:

```bash
python app.py
```

### Langkah 6: Muat naik model ke Azure AI

Memuat naik model ke repositori model Azure AI menjadikan model itu boleh dikongsi dengan ahli pasukan pembangunan anda yang lain dan juga mengurus kawalan versi model. Untuk memuat naik model jalankan arahan berikut:

> [!NOTE]
> Kemas kini `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"dan nama Projek Azure AI, jalankan arahan berikut 

```
az ml workspace show
```

Atau dengan pergi ke +++ai.azure.com+++ dan memilih **management center** **project** **overview**

Kemas kini `{}` dengan nama kumpulan sumber anda dan Nama Projek Azure AI.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
Anda kemudian boleh melihat model yang dimuat naik dan menyebarkan model anda di https://ml.azure.com/model/list

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.