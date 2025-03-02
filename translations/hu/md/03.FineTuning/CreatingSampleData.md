# Képadatbázis létrehozása a Hugging Face adatbázis és a kapcsolódó képek letöltésével

### Áttekintés

Ez a szkript egy gépi tanuláshoz szükséges adatbázist készít elő azáltal, hogy letölti a szükséges képeket, kiszűri azokat a sorokat, ahol a képletöltés nem sikerül, és CSV fájlként menti az adatbázist.

### Előfeltételek

A szkript futtatása előtt győződj meg róla, hogy a következő könyvtárak telepítve vannak: `Pandas`, `Datasets`, `requests`, `PIL` és `io`. Emellett cseréld ki a `'Insert_Your_Dataset'` változót a 2. sorban a Hugging Face-ről származó adatbázis nevére.

Szükséges könyvtárak:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funkcionalitás

A szkript a következő lépéseket hajtja végre:

1. Letölti az adatbázist a Hugging Face-ről a `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` függvény segítségével.
2. Letölti a képeket az adatbázisban található URL-ekről.
3. Kiszűri azokat a sorokat, ahol a képek letöltése nem sikerült.
4. A feldolgozott adatbázist CSV fájlként menti.

### Hogyan működik

A `download_image` függvény két paramétert fogad: `image_url`, amely a letölteni kívánt kép URL-je, és `save_path`, amely az útvonal, ahová a letöltött képet menteni kell.

Így működik a függvény:

1. A függvény egy GET kérést küld az `image_url`-ra a `requests.get` metódus segítségével, hogy lekérje az URL-hez tartozó képadatokat.
2. A `response.raise_for_status()` sor ellenőrzi, hogy a kérés sikeres volt-e. Ha a válasz státuszkódja hibát jelez (például 404 - Nem található), akkor kivételt dob. Ez biztosítja, hogy csak sikeres kérés esetén folytatódjon a kép letöltése.
3. A képadatokat átadja a PIL (Python Imaging Library) `Image.open` metódusának, amely egy Image objektumot hoz létre a képadatokból.
4. Az `image.save(save_path)` sor elmenti a képet a megadott `save_path` útvonalra. Az útvonalnak tartalmaznia kell a kívánt fájlnevet és kiterjesztést.
5. Végül a függvény `True` értéket ad vissza, jelezve, hogy a kép sikeresen letöltődött és elmentődött. Ha bármilyen kivétel történik a folyamat során, a függvény elkapja a kivételt, hibaüzenetet ír ki, és `False` értéket ad vissza.

Ez a függvény hasznos képek letöltésére URL-ekről és azok helyi mentésére. Kezeli a letöltési folyamat során fellépő hibákat, és visszajelzést ad arról, hogy a letöltés sikeres volt-e.

Érdemes megjegyezni, hogy a `requests` könyvtár HTTP kérések küldésére szolgál, a PIL könyvtár képek kezelésére, és a `BytesIO` osztály a képadatok byte-adatfolyamként való kezelésére.

### Következtetés

Ez a szkript kényelmes módot nyújt egy gépi tanuláshoz szükséges adatbázis előkészítésére azáltal, hogy letölti a szükséges képeket, kiszűri azokat a sorokat, ahol a képletöltés nem sikerült, és az adatbázist CSV fájlként menti.

### Példa szkript

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

### Példa kód letöltése
[Új adatbázis-generáló szkript](../../../../code/04.Finetuning/generate_dataset.py)

### Példa adatbázis
[Példa adatbázis a finomhangolás LORA példájából](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Felelősség kizárása**:  
Ez a dokumentum gépi AI fordítószolgáltatások segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.