# Kreiranje skupa podataka sa slikama preuzimanjem sa Hugging Face i povezanih slika

### Pregled

Ovaj skript priprema skup podataka za mašinsko učenje preuzimanjem potrebnih slika, filtriranjem redova gde preuzimanje slika nije uspelo, i čuva skup podataka kao CSV fajl.

### Preduslovi

Pre pokretanja ovog skripta, uverite se da su sledeće biblioteke instalirane: `Pandas`, `Datasets`, `requests`, `PIL` i `io`. Takođe, potrebno je zameniti `'Insert_Your_Dataset'` u drugom redu nazivom vašeg skupa podataka sa Hugging Face-a.

Potrebne biblioteke:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funkcionalnosti

Skript izvršava sledeće korake:

1. Preuzima skup podataka sa Hugging Face koristeći funkciju `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`. Funkcija `download_image()` preuzima sliku sa URL-a i čuva je lokalno koristeći Pillow Image biblioteku (PIL) i modul `io`. Vraća True ako je slika uspešno preuzeta, a False u suprotnom. Funkcija takođe podiže izuzetak sa porukom o grešci kada zahtev ne uspe.

### Kako ovo funkcioniše

Funkcija `download_image` prima dva parametra: `image_url`, koji je URL slike koja se preuzima, i `save_path`, koji je putanja gde će preuzeta slika biti sačuvana.

Evo kako funkcija funkcioniše:

Počinje slanjem GET zahteva na `image_url` koristeći metodu `requests.get`. Ovo preuzima podatke o slici sa URL-a.

Linija `response.raise_for_status()` proverava da li je zahtev bio uspešan. Ako statusni kod odgovora ukazuje na grešku (npr. 404 - Nije pronađeno), podiže se izuzetak. Ovo osigurava da nastavljamo sa preuzimanjem slike samo ako je zahtev bio uspešan.

Podaci o slici se zatim prosleđuju metodi `Image.open` iz modula PIL (Python Imaging Library). Ova metoda kreira objekat slike iz podataka o slici.

Linija `image.save(save_path)` čuva sliku na specificiranoj putanji `save_path`. Putanja treba da uključuje željeno ime fajla i ekstenziju.

Na kraju, funkcija vraća True da označi da je slika uspešno preuzeta i sačuvana. Ako se bilo koji izuzetak dogodi tokom procesa, on hvata izuzetak, štampa poruku o grešci koja ukazuje na neuspeh i vraća False.

Ova funkcija je korisna za preuzimanje slika sa URL-ova i njihovo lokalno čuvanje. Ona obrađuje potencijalne greške tokom procesa preuzimanja i pruža povratnu informaciju o tome da li je preuzimanje bilo uspešno ili ne.

Vredno je napomenuti da se biblioteka `requests` koristi za HTTP zahteve, biblioteka PIL se koristi za rad sa slikama, a klasa `BytesIO` se koristi za obradu podataka o slici kao toka bajtova.

### Zaključak

Ovaj skript pruža praktičan način za pripremu skupa podataka za mašinsko učenje preuzimanjem potrebnih slika, filtriranjem redova gde preuzimanje slika nije uspelo, i čuvanjem skupa podataka kao CSV fajla.

### Primer skripta

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

### Preuzimanje primera koda
[Generiši skript za novi skup podataka](../../../../code/04.Finetuning/generate_dataset.py)

### Primer skupa podataka
[Primer skupa podataka iz finetuning primera sa LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако тежимо тачности, имајте на уму да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме настале услед коришћења овог превода.