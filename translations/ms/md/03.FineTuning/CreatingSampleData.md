# Hasilkan Set Data Imej dengan memuat turun DataSet daripada Hugging Face dan imej berkaitan

### Gambaran Keseluruhan

Skrip ini menyediakan set data untuk pembelajaran mesin dengan memuat turun imej yang diperlukan, menapis baris di mana muat turun imej gagal, dan menyimpan set data sebagai fail CSV.

### Prasyarat

Sebelum menjalankan skrip ini, pastikan perpustakaan berikut telah dipasang: `Pandas`, `Datasets`, `requests`, `PIL`, dan `io`. Anda juga perlu menggantikan `'Insert_Your_Dataset'` pada baris ke-2 dengan nama set data anda daripada Hugging Face.

Perpustakaan yang Diperlukan:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Fungsi

Skrip ini melaksanakan langkah-langkah berikut:

1. Memuat turun set data daripada Hugging Face menggunakan fungsi `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`. Fungsi ini memuat turun imej daripada URL dan menyimpannya secara tempatan menggunakan Perpustakaan Imej Pillow (PIL) dan modul `io`. Ia mengembalikan True jika imej berjaya dimuat turun, dan False jika tidak. Fungsi ini juga akan membangkitkan pengecualian dengan mesej ralat jika permintaan gagal.

### Bagaimana ia berfungsi

Fungsi download_image menerima dua parameter: image_url, iaitu URL imej yang akan dimuat turun, dan save_path, iaitu laluan di mana imej yang dimuat turun akan disimpan.

Inilah cara fungsi ini berfungsi:

1. Ia bermula dengan membuat permintaan GET ke image_url menggunakan kaedah requests.get. Ini mengambil data imej daripada URL.

2. Baris response.raise_for_status() memeriksa sama ada permintaan berjaya. Jika kod status respons menunjukkan ralat (contohnya, 404 - Tidak Dijumpai), ia akan membangkitkan pengecualian. Ini memastikan kita hanya meneruskan proses muat turun imej jika permintaan berjaya.

3. Data imej kemudiannya dihantar ke kaedah Image.open daripada modul PIL (Perpustakaan Imej Python). Kaedah ini mencipta objek Imej daripada data imej.

4. Baris image.save(save_path) menyimpan imej ke save_path yang ditentukan. Save_path harus merangkumi nama fail dan sambungan yang diinginkan.

5. Akhirnya, fungsi ini mengembalikan True untuk menunjukkan bahawa imej berjaya dimuat turun dan disimpan. Jika terdapat sebarang pengecualian semasa proses, ia akan menangkap pengecualian tersebut, mencetak mesej ralat yang menunjukkan kegagalan, dan mengembalikan False.

Fungsi ini berguna untuk memuat turun imej daripada URL dan menyimpannya secara tempatan. Ia mengendalikan ralat yang berpotensi semasa proses muat turun dan memberikan maklum balas sama ada muat turun berjaya atau tidak.

Perlu diingatkan bahawa perpustakaan requests digunakan untuk membuat permintaan HTTP, perpustakaan PIL digunakan untuk bekerja dengan imej, dan kelas BytesIO digunakan untuk mengendalikan data imej sebagai aliran bait.

### Kesimpulan

Skrip ini menyediakan cara yang mudah untuk menyediakan set data bagi pembelajaran mesin dengan memuat turun imej yang diperlukan, menapis baris di mana muat turun imej gagal, dan menyimpan set data sebagai fail CSV.

### Skrip Contoh

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

### Muat Turun Kod Contoh 
[Hasilkan skrip set data baharu](../../../../code/04.Finetuning/generate_dataset.py)

### Set Data Contoh
[Contoh set data daripada contoh fine-tuning dengan LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.