[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Kod ini mengeksport model ke format OpenVINO, memuatnya, dan menggunakannya untuk menghasilkan respons berdasarkan prompt yang diberikan.

1. **Mengeksport Model**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Perintah ini menggunakan `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Mengimport Pustaka yang Diperlukan**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Baris ini mengimport kelas dari modul `transformers` library and the `optimum.intel.openvino`, yang diperlukan untuk memuat dan menggunakan model.

3. **Menyiapkan Direktori Model dan Konfigurasi**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` adalah sebuah kamus yang mengkonfigurasi model OpenVINO untuk mengutamakan latensi rendah, menggunakan satu aliran inferensi, dan tidak menggunakan direktori cache.

4. **Memuat Model**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Baris ini memuat model dari direktori yang ditentukan, menggunakan pengaturan konfigurasi yang telah didefinisikan sebelumnya. Ini juga memungkinkan eksekusi kode jarak jauh jika diperlukan.

5. **Memuat Tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Baris ini memuat tokenizer, yang bertanggung jawab untuk mengubah teks menjadi token yang dapat dipahami oleh model.

6. **Menyiapkan Argumen Tokenizer**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Kamus ini menentukan bahwa token khusus tidak boleh ditambahkan ke output yang telah di-tokenisasi.

7. **Mendefinisikan Prompt**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - String ini menyiapkan prompt percakapan di mana pengguna meminta asisten AI untuk memperkenalkan dirinya.

8. **Melakukan Tokenisasi pada Prompt**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Baris ini mengubah prompt menjadi token yang dapat diproses oleh model, mengembalikan hasilnya dalam bentuk tensor PyTorch.

9. **Menghasilkan Respons**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Baris ini menggunakan model untuk menghasilkan respons berdasarkan token input, dengan maksimum 1024 token baru.

10. **Mendekode Respons**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Baris ini mengubah token yang dihasilkan kembali menjadi string yang dapat dibaca manusia, mengabaikan token khusus, dan mengambil hasil pertama.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.