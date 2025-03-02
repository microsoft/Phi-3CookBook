# ਹੱਗਿੰਗ ਫੇਸ ਤੋਂ ਡਾਟਾਸੈਟ ਅਤੇ ਸੰਬੰਧਿਤ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰਕੇ ਚਿੱਤਰ ਡਾਟਾ ਸੈੱਟ ਤਿਆਰ ਕਰੋ

### ਝਲਕ

ਇਹ ਸਕ੍ਰਿਪਟ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਲਈ ਡਾਟਾਸੈਟ ਤਿਆਰ ਕਰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਲੋੜੀਂਦੇ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰਨਾ, ਉਹਨਾਂ ਕਤਾਰਾਂ ਨੂੰ ਹਟਾਉਣਾ ਜਿੱਥੇ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਫੇਲ੍ਹ ਹੋ ਜਾਂਦੇ ਹਨ, ਅਤੇ ਡਾਟਾਸੈਟ ਨੂੰ CSV ਫਾਈਲ ਦੇ ਰੂਪ ਵਿੱਚ ਸੇਵ ਕਰਨਾ ਸ਼ਾਮਲ ਹੈ।

### ਲੋੜੀਂਦੀਆਂ ਚੀਜ਼ਾਂ

ਇਸ ਸਕ੍ਰਿਪਟ ਨੂੰ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਹੇਠ ਲਿਖੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਸਟਾਲ ਕੀਤੀਆਂ ਹਨ: `Pandas`, `Datasets`, `requests`, `PIL`, ਅਤੇ `io`। ਤੁਸੀਂ ਲਾਈਨ 2 ਵਿੱਚ `'Insert_Your_Dataset'` ਨੂੰ ਆਪਣੇ ਹੱਗਿੰਗ ਫੇਸ ਡਾਟਾਸੈਟ ਦੇ ਨਾਮ ਨਾਲ ਬਦਲਣਾ ਵੀ ਲੋੜੀਂਦਾ ਹੈ।

ਲੋੜੀਂਦੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### ਫੰਕਸ਼ਨਾਲਿਟੀ

ਸਕ੍ਰਿਪਟ ਹੇਠ ਲਿਖੇ ਕਦਮ ਕਰਦਾ ਹੈ:

1. ਹੱਗਿੰਗ ਫੇਸ ਤੋਂ `load_dataset()` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਡਾਟਾਸੈਟ ਡਾਊਨਲੋਡ ਕਰਦਾ ਹੈ।
2. ਡਾਟਾਸੈਟ ਨੂੰ pandas ਡਾਟਾ ਫਰੇਮ ਵਿੱਚ ਬਦਲਦਾ ਹੈ।
3. ਹਰ ਕਤਾਰ ਲਈ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰਦਾ ਹੈ।
4. ਉਹ ਕਤਾਰਾਂ ਹਟਾਉਂਦਾ ਹੈ ਜਿੱਥੇ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਫੇਲ੍ਹ ਹੋ ਜਾਂਦਾ ਹੈ।
5. ਨਤੀਜੇ ਵਾਲੇ ਡਾਟਾਸੈਟ ਨੂੰ CSV ਫਾਈਲ ਵਜੋਂ ਸੇਵ ਕਰਦਾ ਹੈ।

### ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ

`download_image()` ਫੰਕਸ਼ਨ ਚਿੱਤਰ URL ਤੋਂ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰਦਾ ਹੈ ਅਤੇ ਇਸਨੂੰ ਲੋਕਲ ਸਟੋਰੇਜ ਵਿੱਚ ਸੇਵ ਕਰਦਾ ਹੈ। ਇਹ True ਵਾਪਸ ਕਰਦਾ ਹੈ ਜੇ ਚਿੱਤਰ ਸਫਲਤਾਪੂਰਵਕ ਡਾਊਨਲੋਡ ਹੋ ਜਾਂਦਾ ਹੈ, ਨਹੀਂ ਤਾਂ False ਵਾਪਸ ਕਰਦਾ ਹੈ। ਜਦੋਂ ਰਿਕਵੈਸਟ ਫੇਲ੍ਹ ਹੁੰਦੀ ਹੈ, ਫੰਕਸ਼ਨ ਗਲਤੀ ਦਾ ਸੁਨੇਹਾ ਦੇ ਕੇ ਇੱਕ ਐਕਸਪਸ਼ਨ ਉਠਾਉਂਦਾ ਹੈ।

### ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ

`download_image()` ਫੰਕਸ਼ਨ ਵਿੱਚ ਦੋ ਪੈਰਾਮੀਟਰ ਹੁੰਦੇ ਹਨ: `image_url`, ਜੋ ਡਾਊਨਲੋਡ ਕੀਤੇ ਜਾਣ ਵਾਲੇ ਚਿੱਤਰ ਦੀ URL ਹੈ, ਅਤੇ `save_path`, ਜੋ ਉਹ ਜਗ੍ਹਾ ਹੈ ਜਿੱਥੇ ਡਾਊਨਲੋਡ ਕੀਤਾ ਚਿੱਤਰ ਸੇਵ ਕੀਤਾ ਜਾਵੇਗਾ।

ਇਹ ਹੈ ਕਿ ਇਹ ਫੰਕਸ਼ਨ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ:

1. ਇਹ `requests.get` ਮੈਥਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ `image_url` ਨੂੰ GET ਰਿਕਵੈਸਟ ਭੇਜਦਾ ਹੈ। ਇਹ URL ਤੋਂ ਚਿੱਤਰ ਡਾਟਾ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ।
2. `response.raise_for_status()` ਲਾਈਨ ਜਾਂਚਦੀ ਹੈ ਕਿ ਰਿਕਵੈਸਟ ਸਫਲ ਰਹੀ। ਜੇਕਰ ਰਿਸਪਾਂਸ ਸਟੇਟਸ ਕੋਡ ਵਿੱਚ ਗਲਤੀ ਦਿਖਾਈ ਦਿੰਦੀ ਹੈ (ਜਿਵੇਂ ਕਿ 404 - ਨਹੀਂ ਮਿਲਿਆ), ਤਾਂ ਇਹ ਐਕਸਪਸ਼ਨ ਉਠਾਉਂਦਾ ਹੈ। ਇਸ ਨਾਲ ਇਹ ਯਕੀਨੀ ਬਣਦਾ ਹੈ ਕਿ ਅਸੀਂ ਸਿਰਫ ਸਫਲ ਰਿਕਵੈਸਟ ਮਗਰੋਂ ਹੀ ਅੱਗੇ ਵਧਦੇ ਹਾਂ।
3. ਚਿੱਤਰ ਡਾਟਾ ਨੂੰ PIL (Python Imaging Library) ਮੋਡੀਊਲ ਦੇ `Image.open` ਮੈਥਡ ਵਿੱਚ ਪਾਸ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਇਹ ਮੈਥਡ ਚਿੱਤਰ ਡਾਟਾ ਤੋਂ ਇੱਕ ਚਿੱਤਰ ਓਬਜੈਕਟ ਬਣਾਉਂਦਾ ਹੈ।
4. `image.save(save_path)` ਲਾਈਨ ਚਿੱਤਰ ਨੂੰ ਦਿੱਖਾਏ ਗਏ ਸੇਵ ਪਾਥ ਤੇ ਸੇਵ ਕਰਦੀ ਹੈ। ਸੇਵ ਪਾਥ ਵਿੱਚ ਫਾਈਲ ਦਾ ਨਾਮ ਅਤੇ ਐਕਸਟੈਂਸ਼ਨ ਸ਼ਾਮਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।
5. ਅੰਤ ਵਿੱਚ, ਫੰਕਸ਼ਨ True ਵਾਪਸ ਕਰਦਾ ਹੈ ਜੇ ਚਿੱਤਰ ਸਫਲਤਾਪੂਰਵਕ ਡਾਊਨਲੋਡ ਅਤੇ ਸੇਵ ਹੋ ਜਾਂਦਾ ਹੈ। ਜੇ ਪ੍ਰਕਿਰਿਆ ਦੌਰਾਨ ਕੋਈ ਵੀ ਐਕਸਪਸ਼ਨ ਆਉਂਦੀ ਹੈ, ਤਾਂ ਇਹ ਐਕਸਪਸ਼ਨ ਨੂੰ ਪਕੜਦਾ ਹੈ, ਗਲਤੀ ਦਾ ਸੁਨੇਹਾ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ, ਅਤੇ False ਵਾਪਸ ਕਰਦਾ ਹੈ।

ਇਹ ਫੰਕਸ਼ਨ URLs ਤੋਂ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰਨ ਅਤੇ ਇਨ੍ਹਾਂ ਨੂੰ ਲੋਕਲ ਸਟੋਰੇਜ ਵਿੱਚ ਸੇਵ ਕਰਨ ਲਈ ਲਾਭਦਾਇਕ ਹੈ। ਇਹ ਡਾਊਨਲੋਡ ਪ੍ਰਕਿਰਿਆ ਦੌਰਾਨ ਆਉਣ ਵਾਲੀਆਂ ਸੰਭਾਵਿਤ ਗਲਤੀਆਂ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ ਅਤੇ ਇਹ ਦੱਸਦਾ ਹੈ ਕਿ ਡਾਊਨਲੋਡ ਸਫਲ ਹੋਇਆ ਜਾਂ ਨਹੀਂ।

ਇਹ ਨੋਟ ਕਰਨ ਵਾਲੀ ਗੱਲ ਹੈ ਕਿ HTTP ਰਿਕਵੈਸਟ ਕਰਨ ਲਈ `requests` ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਚਿੱਤਰਾਂ ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ PIL ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਅਤੇ ਚਿੱਤਰ ਡਾਟਾ ਨੂੰ ਬਾਈਟਸ ਦੇ ਸਟ੍ਰੀਮ ਵਜੋਂ ਸੰਭਾਲਣ ਲਈ `BytesIO` ਕਲਾਸ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

### ਨਤੀਜਾ

ਇਹ ਸਕ੍ਰਿਪਟ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਲਈ ਡਾਟਾਸੈਟ ਤਿਆਰ ਕਰਨ ਦਾ ਇੱਕ ਆਸਾਨ ਤਰੀਕਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਲੋੜੀਂਦੇ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰਨਾ, ਉਹਨਾਂ ਕਤਾਰਾਂ ਨੂੰ ਹਟਾਉਣਾ ਜਿੱਥੇ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਫੇਲ੍ਹ ਹੋ ਜਾਂਦੇ ਹਨ, ਅਤੇ ਡਾਟਾਸੈਟ ਨੂੰ CSV ਫਾਈਲ ਦੇ ਰੂਪ ਵਿੱਚ ਸੇਵ ਕਰਨਾ ਸ਼ਾਮਲ ਹੈ।

### ਨਮੂਨਾ ਸਕ੍ਰਿਪਟ

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

### ਨਮੂਨਾ ਕੋਡ ਡਾਊਨਲੋਡ 
[ਨਵਾਂ ਡਾਟਾ ਸੈੱਟ ਤਿਆਰ ਕਰਨ ਵਾਲਾ ਸਕ੍ਰਿਪਟ](../../../../code/04.Finetuning/generate_dataset.py)

### ਨਮੂਨਾ ਡਾਟਾ ਸੈੱਟ
[ਫਾਈਨਟਿਊਨਿੰਗ ਨਾਲ LORA ਉਦਾਹਰਨ ਤੋਂ ਨਮੂਨਾ ਡਾਟਾ ਸੈੱਟ](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ-ਅਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੱਜੇਪਣ ਹੋ ਸਕਦੇ ਹਨ। ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਇਸਤੇਮਾਲ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।  