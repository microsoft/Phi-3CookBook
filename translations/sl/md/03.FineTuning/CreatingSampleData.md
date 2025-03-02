# Ustvari nabor podatkov slik z nalaganjem nabora podatkov iz Hugging Face in povezanih slik

### Pregled

Ta skripta pripravi nabor podatkov za strojno učenje z nalaganjem potrebnih slik, filtriranjem vrstic, kjer nalaganje slik ne uspe, in shranjevanjem nabora podatkov kot CSV datoteke.

### Predpogoji

Pred zagonom te skripte poskrbite, da imate nameščene naslednje knjižnice: `Pandas`, `Datasets`, `requests`, `PIL` in `io`. Prav tako boste morali zamenjati `'Insert_Your_Dataset'` v vrstici 2 z imenom vašega nabora podatkov iz Hugging Face.

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

Skripta izvaja naslednje korake:

1. Prenese nabor podatkov iz Hugging Face z uporabo `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` funkcija prenese sliko iz URL-ja in jo lokalno shrani z uporabo knjižnice Pillow Image Library (PIL) in modula `io`. Funkcija vrne True, če je slika uspešno prenesena, in False, če ni. Prav tako funkcija sproži izjemo z napako, če zahteva ne uspe.

### Kako deluje

Funkcija download_image sprejme dva parametra: image_url, ki je URL slike za prenos, in save_path, ki je pot, kamor bo prenesena slika shranjena.

Tukaj je, kako funkcija deluje:

Začne z izvedbo GET zahteve na image_url z uporabo metode requests.get. To pridobi podatke slike iz URL-ja.

Ukaz response.raise_for_status() preveri, ali je zahteva uspela. Če statusna koda odgovora kaže na napako (npr. 404 - Ni najdeno), bo sprožila izjemo. To zagotavlja, da nadaljujemo s prenosom slike samo, če je zahteva uspela.

Podatki slike se nato prenesejo v metodo Image.open iz modula PIL (Python Imaging Library). Ta metoda ustvari objekt Image iz podatkov slike.

Ukaz image.save(save_path) shrani sliko na določeno save_path. Save_path mora vključevati željeno ime datoteke in končnico.

Na koncu funkcija vrne True, kar pomeni, da je bila slika uspešno prenesena in shranjena. Če pride do kakršnekoli izjeme med procesom, ujame izjemo, izpiše sporočilo o napaki, ki označuje neuspeh, in vrne False.

Ta funkcija je uporabna za prenos slik iz URL-jev in njihovo lokalno shranjevanje. Obvladuje morebitne napake med procesom prenosa in zagotavlja povratne informacije o uspešnosti prenosa.

Omeniti velja, da se knjižnica requests uporablja za izvajanje HTTP zahtev, knjižnica PIL za delo s slikami, razred BytesIO pa za obdelavo podatkov slike kot tok bajtov.

### Zaključek

Ta skripta ponuja priročen način za pripravo nabora podatkov za strojno učenje z nalaganjem potrebnih slik, filtriranjem vrstic, kjer prenos slik ne uspe, in shranjevanjem nabora podatkov kot CSV datoteke.

### Vzorec skripte

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

### Prenos vzorčne kode 
[Ustvari novo skripto za nabor podatkov](../../../../code/04.Finetuning/generate_dataset.py)

### Vzorec nabora podatkov
[Primer vzorčnega nabora podatkov iz finetuninga z LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitev strojnega prevajanja na osnovi umetne inteligence. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku se šteje za avtoritativni vir. Za ključne informacije je priporočljivo profesionalno človeško prevajanje. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.