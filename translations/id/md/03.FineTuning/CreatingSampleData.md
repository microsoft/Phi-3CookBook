# Menghasilkan Data Set Gambar dengan Mengunduh DataSet dari Hugging Face dan Gambar Terkait

### Ikhtisar

Script ini mempersiapkan dataset untuk pembelajaran mesin dengan mengunduh gambar yang diperlukan, menyaring baris di mana pengunduhan gambar gagal, dan menyimpan dataset sebagai file CSV.

### Prasyarat

Sebelum menjalankan script ini, pastikan Anda telah menginstal pustaka berikut: `Pandas`, `Datasets`, `requests`, `PIL`, dan `io`. Anda juga perlu mengganti `'Insert_Your_Dataset'` pada baris 2 dengan nama dataset Anda dari Hugging Face.

Pustaka yang Dibutuhkan:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Fungsionalitas

Script ini melakukan langkah-langkah berikut:

1. Mengunduh dataset dari Hugging Face menggunakan `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` fungsi yang mengunduh gambar dari URL dan menyimpannya secara lokal menggunakan Pillow Image Library (PIL) dan modul `io`. Fungsi ini mengembalikan True jika gambar berhasil diunduh, dan False jika tidak. Fungsi ini juga akan memunculkan pengecualian dengan pesan kesalahan jika permintaan gagal.

### Bagaimana Cara Kerjanya

Fungsi `download_image` menerima dua parameter: `image_url`, yaitu URL gambar yang akan diunduh, dan `save_path`, yaitu jalur di mana gambar yang diunduh akan disimpan.

Berikut cara kerja fungsi ini:

1. Fungsi memulai dengan membuat permintaan GET ke `image_url` menggunakan metode `requests.get`. Ini mengambil data gambar dari URL.

2. Baris `response.raise_for_status()` memeriksa apakah permintaan berhasil. Jika kode status respons menunjukkan kesalahan (misalnya, 404 - Tidak Ditemukan), maka akan memunculkan pengecualian. Ini memastikan bahwa kita hanya melanjutkan pengunduhan gambar jika permintaan berhasil.

3. Data gambar kemudian diteruskan ke metode `Image.open` dari modul PIL (Python Imaging Library). Metode ini membuat objek Image dari data gambar.

4. Baris `image.save(save_path)` menyimpan gambar ke `save_path` yang ditentukan. `save_path` harus mencakup nama file dan ekstensi yang diinginkan.

5. Akhirnya, fungsi mengembalikan True untuk menunjukkan bahwa gambar berhasil diunduh dan disimpan. Jika terjadi pengecualian selama proses, fungsi akan menangkap pengecualian tersebut, mencetak pesan kesalahan yang menunjukkan kegagalan, dan mengembalikan False.

Fungsi ini berguna untuk mengunduh gambar dari URL dan menyimpannya secara lokal. Fungsi ini menangani potensi kesalahan selama proses pengunduhan dan memberikan umpan balik apakah pengunduhan berhasil atau tidak.

Perlu dicatat bahwa pustaka `requests` digunakan untuk membuat permintaan HTTP, pustaka PIL digunakan untuk bekerja dengan gambar, dan kelas `BytesIO` digunakan untuk menangani data gambar sebagai aliran byte.

### Kesimpulan

Script ini menyediakan cara yang praktis untuk mempersiapkan dataset untuk pembelajaran mesin dengan mengunduh gambar yang diperlukan, menyaring baris di mana pengunduhan gambar gagal, dan menyimpan dataset sebagai file CSV.

### Contoh Script

```python
import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO

def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check if the request was successful
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")
        return False


# Download the dataset from Hugging Face
dataset = load_dataset('Insert_Your_Dataset')


# Convert the Hugging Face dataset to a Pandas DataFrame
df = dataset['train'].to_pandas()


# Create directories to save the dataset and images
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# Filter out rows where image download fails
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# Create a new DataFrame with the filtered rows
filtered_df = pd.DataFrame(filtered_rows)


# Save the updated dataset to disk
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"Dataset and images saved to {dataset_dir}")
```

### Unduh Kode Contoh 
[Script untuk Menghasilkan Data Set Baru](../../../../code/04.Finetuning/generate_dataset.py)

### Contoh Data Set
[Contoh Data Set dari finetuning dengan contoh LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI berbasis mesin. Meskipun kami berupaya untuk mencapai akurasi, harap disadari bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan untuk menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah penafsiran yang timbul dari penggunaan terjemahan ini.