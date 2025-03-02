# Gumawa ng Image Data Set sa pamamagitan ng pag-download ng DataSet mula sa Hugging Face at mga kaugnay na larawan

### Pangkalahatang-ideya

Ang script na ito ay naghahanda ng dataset para sa machine learning sa pamamagitan ng pag-download ng kinakailangang mga larawan, pag-filter ng mga row kung saan nabigo ang pag-download ng larawan, at pag-save ng dataset bilang isang CSV file.

### Mga Kinakailangan

Bago patakbuhin ang script na ito, tiyakin na ang mga sumusunod na library ay naka-install: `Pandas`, `Datasets`, `requests`, `PIL`, at `io`. Kailangan mo ring palitan ang `'Insert_Your_Dataset'` sa linya 2 ng pangalan ng iyong dataset mula sa Hugging Face.

Mga Kinakailangang Library:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Mga Gawain

Ang script ay gumagawa ng mga sumusunod na hakbang:

1. Dina-download ang dataset mula sa Hugging Face gamit ang `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` na function na nagda-download ng larawan mula sa isang URL at sine-save ito nang lokal gamit ang Pillow Image Library (PIL) at ang module na `io`. Ibinabalik nito ang True kung matagumpay na na-download ang larawan, at False kung hindi. Ang function ay nagbubukas din ng exception na may error message kapag nabigo ang request.

### Paano ito gumagana

Ang function na `download_image` ay tumatanggap ng dalawang parameter: ang `image_url`, na siyang URL ng larawang ida-download, at ang `save_path`, na siyang path kung saan ise-save ang na-download na larawan.

Narito kung paano gumagana ang function:

- Nagsisimula ito sa paggawa ng GET request sa `image_url` gamit ang `requests.get` method. Kinukuha nito ang data ng larawan mula sa URL.

- Ang `response.raise_for_status()` na linya ay sinusuri kung matagumpay ang request. Kung ang status code ng response ay nagpapakita ng error (halimbawa, 404 - Not Found), magbubukas ito ng exception. Tinitiyak nito na magpapatuloy lang ang pag-download ng larawan kung matagumpay ang request.

- Ang data ng larawan ay ipinapasa sa `Image.open` method mula sa PIL (Python Imaging Library) module. Ang method na ito ay lumilikha ng Image object mula sa data ng larawan.

- Ang `image.save(save_path)` na linya ay sine-save ang larawan sa tinukoy na `save_path`. Ang `save_path` ay dapat may kasamang nais na pangalan ng file at extension.

- Sa wakas, ang function ay nagbabalik ng True upang ipahiwatig na ang larawan ay matagumpay na na-download at na-save. Kung may naganap na exception sa proseso, sinasalo nito ang exception, nagpi-print ng error message na nagpapahiwatig ng kabiguan, at nagbabalik ng False.

Ang function na ito ay kapaki-pakinabang para sa pag-download ng mga larawan mula sa mga URL at pagsi-save nito nang lokal. Pinangangasiwaan nito ang mga posibleng error sa proseso ng pag-download at nagbibigay ng feedback kung matagumpay o hindi ang pag-download.

Mahalagang tandaan na ang `requests` library ay ginagamit para sa paggawa ng HTTP requests, ang `PIL` library ay ginagamit para sa pagproseso ng mga larawan, at ang `BytesIO` class ay ginagamit upang pangasiwaan ang data ng larawan bilang isang stream ng bytes.

### Konklusyon

Ang script na ito ay nagbibigay ng isang maginhawang paraan upang maghanda ng dataset para sa machine learning sa pamamagitan ng pag-download ng kinakailangang mga larawan, pag-filter ng mga row kung saan nabigo ang pag-download ng larawan, at pag-save ng dataset bilang isang CSV file.

### Halimbawang Script

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

### Pag-download ng Halimbawang Code 
[Mag-generate ng bagong Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Halimbawang Data Set
[Halimbawa ng Data Set mula sa finetuning gamit ang LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyong pang-translation na pinapagana ng AI. Bagama't pinagsisikapan naming maging wasto, pakatandaan na ang mga awtomatikong salin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa sarili nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng saling ito.