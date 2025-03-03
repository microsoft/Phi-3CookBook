# Vytvorenie datasetu obrázkov stiahnutím datasetu z Hugging Face a priradených obrázkov

### Prehľad

Tento skript pripraví dataset pre strojové učenie stiahnutím potrebných obrázkov, odstránením riadkov, kde sa nepodarilo stiahnuť obrázky, a uložením datasetu ako CSV súbor.

### Predpoklady

Pred spustením tohto skriptu sa uistite, že máte nainštalované nasledujúce knižnice: `Pandas`, `Datasets`, `requests`, `PIL` a `io`. Tiež bude potrebné nahradiť `'Insert_Your_Dataset'` na riadku 2 názvom vášho datasetu z Hugging Face.

Potrebné knižnice:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funkcionalita

Skript vykonáva nasledujúce kroky:

1. Stiahne dataset z Hugging Face pomocou funkcie `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`. Funkcia `download_image()` stiahne obrázok z URL adresy a uloží ho lokálne pomocou knižnice Pillow Image Library (PIL) a modulu `io`. Funkcia vráti hodnotu True, ak sa obrázok úspešne stiahne, a hodnotu False v opačnom prípade. V prípade zlyhania požiadavky funkcia vyvolá výnimku s chybovou správou.

### Ako to funguje

Funkcia `download_image` prijíma dva parametre: `image_url`, čo je URL adresa obrázka, ktorý sa má stiahnuť, a `save_path`, čo je cesta, kam sa stiahnutý obrázok uloží.

Tu je popis, ako funkcia funguje:

1. Začína odoslaním GET požiadavky na `image_url` pomocou metódy `requests.get`. Táto požiadavka načíta dáta obrázka z URL adresy.

2. Riadok `response.raise_for_status()` kontroluje, či bola požiadavka úspešná. Ak kód odpovede naznačuje chybu (napr. 404 - Nenájdené), vyvolá výnimku. To zabezpečuje, že budeme pokračovať v sťahovaní obrázka len v prípade, že bola požiadavka úspešná.

3. Dáta obrázka sa potom odovzdajú metóde `Image.open` z modulu PIL (Python Imaging Library). Táto metóda vytvorí objekt `Image` z dát obrázka.

4. Riadok `image.save(save_path)` uloží obrázok do špecifikovanej cesty `save_path`. `save_path` by mal obsahovať požadovaný názov súboru a príponu.

5. Nakoniec funkcia vráti hodnotu True, aby naznačila, že obrázok bol úspešne stiahnutý a uložený. Ak počas procesu nastane akákoľvek výnimka, zachytí ju, vypíše chybovú správu a vráti hodnotu False.

Táto funkcia je užitočná na sťahovanie obrázkov z URL adries a ich lokálne uloženie. Rieši možné chyby počas procesu sťahovania a poskytuje spätnú väzbu o tom, či bolo sťahovanie úspešné alebo nie.

Je dôležité spomenúť, že knižnica `requests` sa používa na vykonávanie HTTP požiadaviek, knižnica PIL sa používa na prácu s obrázkami a trieda `BytesIO` sa používa na spracovanie dát obrázka ako prúdu bajtov.

### Záver

Tento skript poskytuje pohodlný spôsob, ako pripraviť dataset pre strojové učenie stiahnutím potrebných obrázkov, odstránením riadkov, kde sa nepodarilo stiahnuť obrázky, a uložením datasetu ako CSV súbor.

### Ukážkový skript

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

### Stiahnutie ukážkového kódu 
[Generovať nový skript datasetu](../../../../code/04.Finetuning/generate_dataset.py)

### Ukážkový dataset
[Príklad datasetu z jemného doladenia s LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladových služieb. Hoci sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.