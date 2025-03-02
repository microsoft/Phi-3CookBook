### Contoh Senario

Bayangkan anda mempunyai imej (`demo.png`) dan anda ingin menjana kod Python yang memproses imej ini dan menyimpan versi baharu daripadanya (`phi-3-vision.jpg`). 

Kod di atas mengautomasi proses ini dengan cara:

1. Menyediakan persekitaran dan konfigurasi yang diperlukan.
2. Membuat prompt yang mengarahkan model untuk menjana kod Python yang diperlukan.
3. Menghantar prompt kepada model dan mengumpulkan kod yang dijana.
4. Mengekstrak dan menjalankan kod yang dijana.
5. Memaparkan imej asal dan imej yang telah diproses.

Pendekatan ini memanfaatkan kuasa AI untuk mengautomasi tugas pemprosesan imej, menjadikannya lebih mudah dan cepat untuk mencapai matlamat anda. 

[Penyelesaian Kod Contoh](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Mari kita perincikan apa yang dilakukan oleh keseluruhan kod langkah demi langkah:

1. **Pasang Pakej Diperlukan**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Perintah ini memasang pakej `langchain_nvidia_ai_endpoints`, memastikan ia adalah versi terkini.

2. **Import Modul-Modul Penting**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Import ini membawa masuk modul-modul penting untuk berinteraksi dengan endpoint AI NVIDIA, menguruskan kata laluan dengan selamat, berinteraksi dengan sistem operasi, dan mengekod/mendekod data dalam format base64.

3. **Tetapkan Kunci API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Kod ini memeriksa sama ada pemboleh ubah persekitaran `NVIDIA_API_KEY` telah ditetapkan. Jika tidak, ia akan meminta pengguna memasukkan kunci API mereka secara selamat.

4. **Tentukan Model dan Laluan Imej**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Kod ini menetapkan model yang akan digunakan, mencipta instans `ChatNVIDIA` dengan model yang dinyatakan, dan menentukan laluan fail imej.

5. **Cipta Prompt Teks**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Kod ini mentakrifkan prompt teks yang mengarahkan model untuk menjana kod Python bagi memproses imej.

6. **Kodkan Imej dalam Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Kod ini membaca fail imej, mengkodkannya dalam base64, dan mencipta tag imej HTML dengan data yang telah dikodkan.

7. **Gabungkan Teks dan Imej ke dalam Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Kod ini menggabungkan prompt teks dan tag imej HTML ke dalam satu rentetan.

8. **Jana Kod Menggunakan ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Kod ini menghantar prompt kepada `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Ekstrak Kod Python daripada Kandungan yang Dihasilkan**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Kod ini mengekstrak kod Python sebenar daripada kandungan yang dijana dengan membuang format markdown.

10. **Jalankan Kod yang Dihasilkan**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Kod ini menjalankan kod Python yang telah diekstrak sebagai subprocess dan menangkap keluarannya.

11. **Paparkan Imej**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Baris ini memaparkan imej menggunakan modul `IPython.display`.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.