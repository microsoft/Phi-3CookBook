# Generiranje skupa podataka s slikama preuzimanjem skupa podataka s Hugging Face platforme i povezanih slika

### Pregled

Ovaj skript priprema skup podataka za strojno učenje preuzimanjem potrebnih slika, filtriranjem redaka gdje preuzimanje slika ne uspije, i spremanjem skupa podataka kao CSV datoteku.

### Preduvjeti

Prije pokretanja ovog skripta, provjerite imate li instalirane sljedeće knjižnice: `Pandas`, `Datasets`, `requests`, `PIL` i `io`. Također, trebate zamijeniti `'Insert_Your_Dataset'` u liniji 2 s nazivom vašeg skupa podataka s Hugging Face platforme.

Potrebne knjižnice:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funkcionalnost

Skript izvodi sljedeće korake:

1. Preuzima skup podataka s Hugging Face platforme koristeći funkcije `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`. Funkcija `download_image()` preuzima sliku s URL-a i sprema je lokalno koristeći Pillow Image Library (PIL) i modul `io`. Vraća True ako je slika uspješno preuzeta, a False u suprotnom. Funkcija također izbacuje iznimku s porukom o pogrešci ako zahtjev ne uspije.

### Kako ovo funkcionira

Funkcija `download_image` prima dva parametra: `image_url`, koji je URL slike za preuzimanje, i `save_path`, koji je put gdje će preuzeta slika biti spremljena.

Evo kako funkcija radi:

- Počinje slanjem GET zahtjeva prema `image_url` koristeći metodu `requests.get`. Ovo dohvaća podatke slike s URL-a.

- Linija `response.raise_for_status()` provjerava je li zahtjev bio uspješan. Ako statusni kod odgovora ukazuje na pogrešku (npr. 404 - Nije pronađeno), izbacit će iznimku. Ovo osigurava da nastavljamo s preuzimanjem slike samo ako je zahtjev bio uspješan.

- Podaci slike zatim se prosljeđuju metodi `Image.open` iz modula PIL (Python Imaging Library). Ova metoda stvara objekt slike iz podataka slike.

- Linija `image.save(save_path)` sprema sliku na određeni `save_path`. `save_path` bi trebao uključivati željeno ime datoteke i ekstenziju.

- Na kraju, funkcija vraća True kako bi naznačila da je slika uspješno preuzeta i spremljena. Ako se tijekom procesa dogodi bilo kakva iznimka, funkcija hvata iznimku, ispisuje poruku o pogrešci koja ukazuje na neuspjeh i vraća False.

Ova funkcija je korisna za preuzimanje slika s URL-ova i njihovo lokalno spremanje. Rješava potencijalne pogreške tijekom procesa preuzimanja i pruža povratne informacije o tome je li preuzimanje bilo uspješno ili ne.

Važno je napomenuti da se knjižnica `requests` koristi za slanje HTTP zahtjeva, knjižnica `PIL` koristi se za rad sa slikama, a klasa `BytesIO` koristi se za obradu podataka slike kao toka bajtova.

### Zaključak

Ovaj skript pruža praktičan način za pripremu skupa podataka za strojno učenje preuzimanjem potrebnih slika, filtriranjem redaka gdje preuzimanje slika ne uspije i spremanjem skupa podataka kao CSV datoteku.

### Primjer skripta

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

### Preuzimanje primjera koda 
[Generirajte novi skript za skup podataka](../../../../code/04.Finetuning/generate_dataset.py)

### Primjer skupa podataka
[Primjer skupa podataka iz finetuninga s LORA primjerom](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Odricanje odgovornosti**:  
Ovaj dokument je preveden koristeći usluge automatskog prevođenja putem AI tehnologije. Iako se trudimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba se smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za bilo kakva nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.