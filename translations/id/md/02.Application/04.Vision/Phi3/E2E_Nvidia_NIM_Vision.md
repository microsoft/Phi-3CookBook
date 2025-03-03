### Contoh Skenario

Bayangkan Anda memiliki sebuah gambar (`demo.png`) dan Anda ingin menghasilkan kode Python yang memproses gambar ini dan menyimpan versi barunya (`phi-3-vision.jpg`).

Kode di atas mengotomatisasi proses ini dengan:

1. Menyiapkan lingkungan dan konfigurasi yang diperlukan.
2. Membuat prompt yang menginstruksikan model untuk menghasilkan kode Python yang dibutuhkan.
3. Mengirimkan prompt ke model dan mengumpulkan kode yang dihasilkan.
4. Mengekstrak dan menjalankan kode yang dihasilkan.
5. Menampilkan gambar asli dan gambar yang telah diproses.

Pendekatan ini memanfaatkan kekuatan AI untuk mengotomatisasi tugas pemrosesan gambar, sehingga lebih mudah dan cepat untuk mencapai tujuan Anda.

[Solusi Contoh Kode](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Mari kita uraikan apa yang dilakukan oleh seluruh kode langkah demi langkah:

1. **Menginstal Paket yang Dibutuhkan**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Perintah ini menginstal paket `langchain_nvidia_ai_endpoints`, memastikan versinya adalah yang terbaru.

2. **Mengimpor Modul yang Diperlukan**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Impor ini membawa modul-modul yang dibutuhkan untuk berinteraksi dengan endpoint NVIDIA AI, menangani kata sandi dengan aman, berinteraksi dengan sistem operasi, dan melakukan encoding/decoding data dalam format base64.

3. **Mengatur API Key**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Kode ini memeriksa apakah variabel lingkungan `NVIDIA_API_KEY` sudah diatur. Jika belum, pengguna diminta untuk memasukkan API key mereka secara aman.

4. **Menentukan Model dan Path Gambar**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Kode ini menentukan model yang akan digunakan, membuat instance `ChatNVIDIA` dengan model yang dipilih, dan menetapkan path ke file gambar.

5. **Membuat Prompt Teks**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Kode ini mendefinisikan prompt teks yang menginstruksikan model untuk menghasilkan kode Python untuk memproses gambar.

6. **Meng-encode Gambar dalam Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Kode ini membaca file gambar, meng-encode-nya dalam base64, dan membuat tag gambar HTML dengan data yang telah di-encode.

7. **Menggabungkan Teks dan Gambar ke dalam Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Kode ini menggabungkan prompt teks dan tag gambar HTML menjadi satu string.

8. **Menghasilkan Kode Menggunakan ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Kode ini mengirimkan prompt ke `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Mengekstrak Kode Python dari Konten yang Dihasilkan**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Kode ini mengekstrak kode Python aktual dari konten yang dihasilkan dengan menghapus format markdown.

10. **Menjalankan Kode yang Dihasilkan**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Kode ini menjalankan kode Python yang diekstrak sebagai subprocess dan menangkap output-nya.

11. **Menampilkan Gambar**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Baris-baris ini menampilkan gambar menggunakan modul `IPython.display`.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan berbasis AI. Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat krusial, disarankan untuk menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.