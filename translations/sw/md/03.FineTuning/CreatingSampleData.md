# Tengeneza Seti ya Data ya Picha kwa kupakua DataSet kutoka Hugging Face na picha zinazohusiana

### Muhtasari

Skript hii inaandaa seti ya data kwa ajili ya ujifunzaji wa mashine kwa kupakua picha zinazohitajika, kuchuja safu ambazo upakuaji wa picha umeshindikana, na kuhifadhi seti ya data kama faili ya CSV.

### Vitu Vinavyohitajika

Kabla ya kuendesha skript hii, hakikisha una maktaba zifuatazo zimesakinishwa: `Pandas`, `Datasets`, `requests`, `PIL`, na `io`. Pia utahitaji kubadilisha `'Insert_Your_Dataset'` katika mstari wa 2 na jina la seti yako ya data kutoka Hugging Face.

Maktaba Zinazohitajika:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Utendaji

Skript hufanya hatua zifuatazo:

1. Inapakua seti ya data kutoka Hugging Face kwa kutumia `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`.

2. Inachuja safu ambazo upakuaji wa picha umeshindikana.

3. Inahifadhi seti ya data iliyochakatwa kama faili ya CSV.

### Jinsi Inavyofanya Kazi

Kazi ya `download_image` inachukua vigezo viwili: `image_url`, ambayo ni URL ya picha inayopakuliwa, na `save_path`, ambayo ni njia ya kuhifadhi picha iliyopakuliwa.

Hivi ndivyo kazi inavyofanya kazi:

- Inaanza kwa kutuma ombi la GET kwa `image_url` kwa kutumia njia ya `requests.get`. Hii hupakua data ya picha kutoka URL.

- Mstari wa `response.raise_for_status()` hukagua ikiwa ombi lilifanikiwa. Ikiwa msimbo wa hali ya majibu unaonyesha hitilafu (mfano, 404 - Haikupatikana), itatoa hitilafu. Hii inahakikisha kwamba tunaendelea tu na upakuaji wa picha ikiwa ombi lilifanikiwa.

- Data ya picha kisha inapitishwa kwa njia ya `Image.open` kutoka moduli ya PIL (Python Imaging Library). Njia hii huunda kitu cha Picha kutoka kwa data ya picha.

- Mstari wa `image.save(save_path)` huokoa picha kwenye `save_path` iliyoainishwa. `save_path` inapaswa kujumuisha jina na kiendelezi cha faili kinachotakiwa.

- Hatimaye, kazi inarudisha `True` kuonyesha kuwa picha ilipakuliwa na kuhifadhiwa kwa mafanikio. Ikiwa hitilafu yoyote itatokea wakati wa mchakato, inakamata hitilafu hiyo, inachapisha ujumbe wa kosa unaoonyesha kushindwa, na kurudisha `False`.

Kazi hii ni muhimu kwa kupakua picha kutoka URL na kuzihifadhi kwa ndani. Inashughulikia hitilafu zinazoweza kutokea wakati wa mchakato wa upakuaji na hutoa maoni kuhusu kama upakuaji ulifanikiwa au la.

Ni vyema kutambua kwamba maktaba ya `requests` inatumika kufanya maombi ya HTTP, maktaba ya PIL inatumika kufanya kazi na picha, na darasa la `BytesIO` linatumika kushughulikia data ya picha kama mkondo wa baiti.

### Hitimisho

Skript hii inatoa njia rahisi ya kuandaa seti ya data kwa ujifunzaji wa mashine kwa kupakua picha zinazohitajika, kuchuja safu ambazo upakuaji wa picha umeshindikana, na kuhifadhi seti ya data kama faili ya CSV.

### Skript ya Mfano

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

### Pakua Msimbo wa Mfano
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Mfano wa Seti ya Data
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za kutafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo rasmi. Kwa taarifa muhimu, inashauriwa kutumia huduma za utafsiri wa kibinadamu wa kitaalamu. Hatutawajibika kwa maelewano mabaya au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.