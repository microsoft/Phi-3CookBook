# Generați un set de date de imagini descărcând setul de date de pe Hugging Face și imaginile asociate

### Prezentare generală

Acest script pregătește un set de date pentru învățarea automată prin descărcarea imaginilor necesare, eliminarea rândurilor unde descărcările imaginilor eșuează și salvarea setului de date ca fișier CSV.

### Cerințe preliminare

Înainte de a rula acest script, asigurați-vă că aveți instalate următoarele biblioteci: `Pandas`, `Datasets`, `requests`, `PIL` și `io`. De asemenea, va trebui să înlocuiți `'Insert_Your_Dataset'` de la linia 2 cu numele setului de date de pe Hugging Face.

Biblioteci necesare:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funcționalitate

Scriptul efectuează următorii pași:

1. Descarcă setul de date de pe Hugging Face folosind funcțiile `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`. Funcția `download_image()` descarcă o imagine de la o adresă URL și o salvează local folosind biblioteca Pillow Image Library (PIL) și modulul `io`. Returnează True dacă imaginea este descărcată cu succes și False în caz contrar. De asemenea, funcția generează o excepție cu mesajul de eroare atunci când solicitarea eșuează.

### Cum funcționează

Funcția `download_image` primește doi parametri: `image_url`, care reprezintă URL-ul imaginii ce urmează să fie descărcată, și `save_path`, care reprezintă calea unde imaginea descărcată va fi salvată.

Iată cum funcționează funcția:

1. Începe prin efectuarea unei cereri GET la `image_url` utilizând metoda `requests.get`. Aceasta preia datele imaginii de la URL.

2. Linia `response.raise_for_status()` verifică dacă cererea a fost efectuată cu succes. Dacă codul de stare al răspunsului indică o eroare (de exemplu, 404 - Not Found), va genera o excepție. Acest lucru asigură că procesul continuă doar dacă cererea a fost efectuată cu succes.

3. Datele imaginii sunt apoi transmise metodei `Image.open` din modulul PIL (Python Imaging Library). Această metodă creează un obiect Imagine din datele imaginii.

4. Linia `image.save(save_path)` salvează imaginea în `save_path` specificat. `save_path` ar trebui să includă numele fișierului dorit și extensia.

5. În final, funcția returnează True pentru a indica faptul că imaginea a fost descărcată și salvată cu succes. Dacă apare vreo excepție în timpul procesului, aceasta este capturată, se afișează un mesaj de eroare care indică eșecul și se returnează False.

Această funcție este utilă pentru descărcarea imaginilor de la URL-uri și salvarea lor local. Gestionează eventualele erori apărute în timpul procesului de descărcare și oferă feedback despre succesul operației.

Este important de menționat că biblioteca `requests` este utilizată pentru efectuarea cererilor HTTP, biblioteca PIL este utilizată pentru lucrul cu imagini, iar clasa `BytesIO` este utilizată pentru a gestiona datele imaginii ca un flux de octeți.

### Concluzie

Acest script oferă o modalitate convenabilă de a pregăti un set de date pentru învățarea automată prin descărcarea imaginilor necesare, eliminarea rândurilor unde descărcările imaginilor eșuează și salvarea setului de date ca fișier CSV.

### Script exemplu

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

### Descărcare cod exemplu
[Generați un script nou pentru setul de date](../../../../code/04.Finetuning/generate_dataset.py)

### Set de date exemplu
[Exemplu de set de date din fine-tuning cu exemplul LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Declinarea responsabilității**:  
Acest document a fost tradus folosind servicii de traducere bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa natală, ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care ar putea apărea din utilizarea acestei traduceri.