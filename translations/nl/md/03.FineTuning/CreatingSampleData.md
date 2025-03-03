# Genereer een afbeeldingsdataset door een dataset van Hugging Face en bijbehorende afbeeldingen te downloaden

### Overzicht

Dit script bereidt een dataset voor machine learning voor door de benodigde afbeeldingen te downloaden, rijen te filteren waar het downloaden van afbeeldingen mislukt, en de dataset op te slaan als een CSV-bestand.

### Vereisten

Voordat je dit script uitvoert, zorg ervoor dat je de volgende bibliotheken hebt geïnstalleerd: `Pandas`, `Datasets`, `requests`, `PIL` en `io`. Je moet ook `'Insert_Your_Dataset'` in regel 2 vervangen door de naam van je dataset van Hugging Face.

Benodigde bibliotheken:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Functionaliteit

Het script voert de volgende stappen uit:

1. Downloadt de dataset van Hugging Face met behulp van `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`.  
2. Filtert rijen waar het downloaden van afbeeldingen is mislukt.  
3. Slaat de gefilterde dataset op als een CSV-bestand.

De functie `download_image()` downloadt een afbeelding van een URL en slaat deze lokaal op met behulp van de Pillow Image Library (PIL) en de `io`-module. De functie retourneert True als de afbeelding succesvol is gedownload, en False anders. Bij een mislukte aanvraag wordt een uitzondering opgegooid met het foutbericht.

### Hoe werkt dit

De functie `download_image` accepteert twee parameters: `image_url`, de URL van de te downloaden afbeelding, en `save_path`, het pad waar de gedownloade afbeelding wordt opgeslagen.

Hier is hoe de functie werkt:

1. Het begint met het uitvoeren van een GET-verzoek naar `image_url` met de `requests.get`-methode. Hiermee wordt de afbeeldingsdata van de URL opgehaald.  
2. De regel `response.raise_for_status()` controleert of het verzoek succesvol was. Als de statuscode van de respons op een fout wijst (bijvoorbeeld 404 - Niet Gevonden), wordt een uitzondering opgegooid. Dit zorgt ervoor dat we alleen doorgaan met het downloaden van de afbeelding als het verzoek succesvol was.  
3. De afbeeldingsdata wordt vervolgens doorgegeven aan de methode `Image.open` van de PIL (Python Imaging Library)-module. Deze methode maakt een `Image`-object van de afbeeldingsdata.  
4. De regel `image.save(save_path)` slaat de afbeelding op in het opgegeven `save_path`. Het `save_path` moet de gewenste bestandsnaam en extensie bevatten.  
5. Tot slot retourneert de functie True om aan te geven dat de afbeelding succesvol is gedownload en opgeslagen. Als er een uitzondering optreedt tijdens het proces, vangt de functie deze op, print een foutmelding die de mislukking aangeeft, en retourneert False.

Deze functie is handig voor het downloaden van afbeeldingen van URL's en het lokaal opslaan ervan. Het behandelt mogelijke fouten tijdens het downloadproces en geeft feedback of de download succesvol was of niet.

Het is belangrijk op te merken dat de `requests`-bibliotheek wordt gebruikt om HTTP-verzoeken te doen, de PIL-bibliotheek wordt gebruikt om met afbeeldingen te werken, en de `BytesIO`-klasse wordt gebruikt om de afbeeldingsdata als een byte-stroom te verwerken.

### Conclusie

Dit script biedt een handige manier om een dataset voor machine learning voor te bereiden door benodigde afbeeldingen te downloaden, rijen te filteren waar het downloaden van afbeeldingen mislukt, en de dataset op te slaan als een CSV-bestand.

### Voorbeeldscript

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

### Voorbeeldcode downloaden 
[Genereer een nieuw dataset-script](../../../../code/04.Finetuning/generate_dataset.py)

### Voorbeelddataset
[Voorbeeld van een dataset uit het finetuning met LORA-voorbeeld](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Disclaimer (Vrijwaring):**  
Dit document is vertaald met behulp van machinegestuurde AI-vertalingsdiensten. Hoewel we ons best doen om nauwkeurigheid te waarborgen, moet u zich ervan bewust zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.