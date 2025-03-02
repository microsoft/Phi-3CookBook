# Luo kuvadatasarja lataamalla DataSet Hugging Facesta ja siihen liittyvät kuvat

### Yleiskatsaus

Tämä skripti valmistaa datasarjan koneoppimista varten lataamalla tarvittavat kuvat, suodattamalla pois rivit, joissa kuvien lataaminen epäonnistuu, ja tallentamalla datasarjan CSV-tiedostona.

### Esivaatimukset

Ennen tämän skriptin suorittamista varmista, että seuraavat kirjastot on asennettu: `Pandas`, `Datasets`, `requests`, `PIL` ja `io`. Lisäksi sinun tulee korvata `'Insert_Your_Dataset'` rivillä 2 Hugging Facesta valitsemasi datasarjan nimellä.

Tarvittavat kirjastot:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Toiminnallisuus

Skripti suorittaa seuraavat vaiheet:

1. Lataa datasarjan Hugging Facesta käyttämällä `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` -funktiota. Tämä lataa kuvat ja tallentaa ne paikallisesti Pillow Image Library (PIL) -kirjaston ja `io`-moduulin avulla. Funktio palauttaa arvon True, jos kuvan lataus onnistuu, ja arvon False, jos se epäonnistuu. Funktio myös nostaa poikkeuksen virheilmoituksella, jos pyyntö epäonnistuu.

### Kuinka tämä toimii

`download_image`-funktio ottaa kaksi parametria: `image_url`, joka on ladattavan kuvan URL-osoite, ja `save_path`, joka on polku, johon ladattu kuva tallennetaan.

Näin funktio toimii:

- Se aloittaa tekemällä GET-pyynnön `image_url`-osoitteeseen käyttäen `requests.get`-metodia. Tämä hakee kuvan tiedot URL-osoitteesta.
  
- `response.raise_for_status()` tarkistaa, oliko pyyntö onnistunut. Jos vastauskoodi osoittaa virheen (esim. 404 - Ei löydy), se nostaa poikkeuksen. Tämä varmistaa, että jatkamme kuvan lataamista vain, jos pyyntö onnistui.

- Kuvadata siirretään sitten `Image.open`-metodille, joka kuuluu PIL (Python Imaging Library) -moduuliin. Tämä metodi luo `Image`-objektin kuvadatasta.

- `image.save(save_path)` tallentaa kuvan määritettyyn `save_path`-polkuun. `save_path`-polun tulee sisältää haluttu tiedostonimi ja tiedostopääte.

- Lopuksi funktio palauttaa arvon True osoittaakseen, että kuva ladattiin ja tallennettiin onnistuneesti. Jos prosessin aikana ilmenee poikkeuksia, ne käsitellään, virheilmoitus tulostetaan ja funktio palauttaa arvon False.

Tämä funktio on hyödyllinen kuvien lataamiseen URL-osoitteista ja niiden tallentamiseen paikallisesti. Se käsittelee mahdolliset virheet latausprosessin aikana ja antaa palautetta latauksen onnistumisesta.

On hyvä huomata, että `requests`-kirjastoa käytetään HTTP-pyyntöjen tekemiseen, PIL-kirjastoa kuvien käsittelyyn ja `BytesIO`-luokkaa kuvadatan käsittelyyn tavujonona.

### Yhteenveto

Tämä skripti tarjoaa kätevän tavan valmistella datasarja koneoppimista varten lataamalla tarvittavat kuvat, suodattamalla pois rivit, joissa kuvien lataaminen epäonnistuu, ja tallentamalla datasarjan CSV-tiedostona.

### Esimerkkiskripti

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

### Esimerkkikoodin lataus 
[Luo uusi datasarja -skripti](../../../../code/04.Finetuning/generate_dataset.py)

### Esimerkkidatasarja
[Esimerkkidatasarja LORA-hienosäätöesimerkistä](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisten tekoälyyn perustuvien käännöspalvelujen avulla. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.