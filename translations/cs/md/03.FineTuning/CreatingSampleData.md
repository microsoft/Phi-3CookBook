# Generování datové sady obrázků stažením datové sady z Hugging Face a přidružených obrázků

### Přehled

Tento skript připravuje datovou sadu pro strojové učení stažením požadovaných obrázků, filtrováním řádků, kde stahování obrázků selže, a uložením datové sady jako CSV souboru.

### Požadavky

Před spuštěním tohoto skriptu se ujistěte, že máte nainstalované následující knihovny: `Pandas`, `Datasets`, `requests`, `PIL` a `io`. Také bude nutné nahradit `'Insert_Your_Dataset'` ve druhém řádku názvem vaší datové sady z Hugging Face.

Požadované knihovny:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funkcionalita

Skript provádí následující kroky:

1. Stáhne datovou sadu z Hugging Face pomocí funkcí `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`.  
2. Funkce `download_image()` stáhne obrázek z URL a uloží ho lokálně pomocí knihovny Pillow Image Library (PIL) a modulu `io`. Vrátí hodnotu True, pokud je obrázek úspěšně stažen, a False v opačném případě. Funkce také vyvolá výjimku s chybovou zprávou, pokud požadavek selže.

### Jak to funguje

Funkce `download_image` přijímá dva parametry: `image_url`, což je URL obrázku ke stažení, a `save_path`, což je cesta, kam bude stažený obrázek uložen.

Jak funkce funguje:

1. Funkce začíná provedením GET požadavku na `image_url` pomocí metody `requests.get`. Tím získá obrazová data z URL.  
2. Řádek `response.raise_for_status()` kontroluje, zda byl požadavek úspěšný. Pokud kód odpovědi indikuje chybu (např. 404 - Nenalezeno), vyvolá výjimku. Tím je zajištěno, že pokračujeme ve stahování obrázku pouze v případě, že byl požadavek úspěšný.  
3. Obrazová data jsou následně předána metodě `Image.open` z modulu PIL (Python Imaging Library). Tato metoda vytvoří objekt `Image` z obrazových dat.  
4. Řádek `image.save(save_path)` uloží obrázek do zadané cesty `save_path`. `save_path` by měl zahrnovat požadovaný název souboru a příponu.  
5. Nakonec funkce vrátí hodnotu True, aby indikovala, že obrázek byl úspěšně stažen a uložen. Pokud během procesu dojde k jakékoli výjimce, funkce ji zachytí, vypíše chybovou zprávu indikující selhání a vrátí hodnotu False.

Tato funkce je užitečná pro stahování obrázků z URL a jejich ukládání lokálně. Zpracovává potenciální chyby během procesu stahování a poskytuje zpětnou vazbu o úspěšnosti stahování.

Je třeba poznamenat, že knihovna `requests` se používá pro provádění HTTP požadavků, knihovna `PIL` se používá pro práci s obrázky a třída `BytesIO` se používá pro zpracování obrazových dat jako proudu bajtů.

### Závěr

Tento skript poskytuje pohodlný způsob, jak připravit datovou sadu pro strojové učení stažením požadovaných obrázků, filtrováním řádků, kde stahování obrázků selže, a uložením datové sady jako CSV souboru.

### Ukázkový skript

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

### Ukázkový kód ke stažení  
[Generovat skript pro novou datovou sadu](../../../../code/04.Finetuning/generate_dataset.py)

### Ukázková datová sada  
[Příklad ukázkové datové sady z ladění pomocí LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Prohlášení:**  
Tento dokument byl přeložen pomocí strojových AI překladatelských služeb. Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro kritické informace doporučujeme profesionální lidský překlad. Nezodpovídáme za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.