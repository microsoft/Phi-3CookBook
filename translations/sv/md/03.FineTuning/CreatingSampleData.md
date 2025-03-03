# Skapa en bilddatamängd genom att ladda ner dataset från Hugging Face och tillhörande bilder

### Översikt

Det här skriptet förbereder en dataset för maskininlärning genom att ladda ner nödvändiga bilder, filtrera bort rader där bildnedladdningar misslyckas och spara datasetet som en CSV-fil.

### Förutsättningar

Innan du kör det här skriptet, se till att följande bibliotek är installerade: `Pandas`, `Datasets`, `requests`, `PIL` och `io`. Du måste också ersätta `'Insert_Your_Dataset'` på rad 2 med namnet på ditt dataset från Hugging Face.

Nödvändiga bibliotek:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funktionalitet

Skriptet utför följande steg:

1. Laddar ner datasetet från Hugging Face med `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`-funktionen som laddar ner en bild från en URL och sparar den lokalt med hjälp av Pillow Image Library (PIL) och modulen `io`. Den returnerar True om bilden laddas ner framgångsrikt, och False annars. Funktionen genererar också ett undantag med felmeddelandet om begäran misslyckas.

### Hur fungerar detta

Funktionen download_image tar två parametrar: image_url, som är URL:en till bilden som ska laddas ner, och save_path, som är sökvägen där den nedladdade bilden ska sparas.

Så här fungerar funktionen:

Den börjar med att göra en GET-begäran till image_url med metoden requests.get. Detta hämtar bilddata från URL:en.

Raden response.raise_for_status() kontrollerar om begäran lyckades. Om statuskoden för svaret indikerar ett fel (t.ex. 404 - Hittades inte), genererar den ett undantag. Detta säkerställer att vi bara fortsätter med att ladda ner bilden om begäran lyckades.

Bilddata skickas sedan till metoden Image.open från PIL-modulen (Python Imaging Library). Denna metod skapar ett Image-objekt från bilddatan.

Raden image.save(save_path) sparar bilden till den angivna save_path. Save_path bör inkludera önskat filnamn och tillägg.

Slutligen returnerar funktionen True för att indikera att bilden laddades ner och sparades framgångsrikt. Om något undantag inträffar under processen fångar den undantaget, skriver ut ett felmeddelande som indikerar misslyckandet och returnerar False.

Denna funktion är användbar för att ladda ner bilder från URL:er och spara dem lokalt. Den hanterar potentiella fel under nedladdningsprocessen och ger feedback om nedladdningen lyckades eller inte.

Det är värt att notera att biblioteket requests används för att göra HTTP-begäran, PIL-biblioteket används för att arbeta med bilder, och BytesIO-klassen används för att hantera bilddata som en byte-ström.

### Slutsats

Det här skriptet erbjuder ett smidigt sätt att förbereda en dataset för maskininlärning genom att ladda ner nödvändiga bilder, filtrera bort rader där bildnedladdningar misslyckas och spara datasetet som en CSV-fil.

### Exempelskript

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

### Exempelkod nedladdning 
[Generera ett nytt Dataset-skript](../../../../code/04.Finetuning/generate_dataset.py)

### Exempel på dataset
[Exempel på dataset från finetuning med LORA-exempel](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.