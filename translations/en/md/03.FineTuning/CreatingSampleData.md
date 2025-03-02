# Generate Image Dataset by Downloading Dataset from Hugging Face and Related Images

### Overview

This script prepares a dataset for machine learning by downloading the necessary images, removing rows where image downloads fail, and saving the dataset as a CSV file.

### Prerequisites

Before running this script, ensure the following libraries are installed: `Pandas`, `Datasets`, `requests`, `PIL`, and `io`. Additionally, replace `'Insert_Your_Dataset'` in line 2 with the name of your Hugging Face dataset.

Required Libraries:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Functionality

The script performs the following steps:

1. Downloads the dataset from Hugging Face using the `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` function.  
2. The `download_image()` function retrieves an image from a URL and saves it locally using the Pillow Image Library (PIL) and the `io` module. It returns `True` if the image is successfully downloaded, and `False` otherwise. If the request fails, it raises an exception with the error message.

### How It Works

The `download_image()` function takes two parameters: `image_url`, which is the URL of the image to be downloaded, and `save_path`, which is the location where the downloaded image will be saved.

Here’s how the function operates:

1. It starts by sending a GET request to the `image_url` using the `requests.get` method to retrieve the image data.
2. The `response.raise_for_status()` line checks if the request was successful. If the response status code indicates an error (e.g., 404 - Not Found), it raises an exception, ensuring the download process only continues if the request is successful.
3. The image data is then passed to the `Image.open()` method from the PIL (Python Imaging Library) module, which creates an `Image` object from the image data.
4. The `image.save(save_path)` line saves the image to the specified `save_path`, which should include the desired file name and extension.
5. Finally, the function returns `True` to indicate a successful download and save. If an exception occurs during the process, it catches the exception, prints an error message indicating the failure, and returns `False`.

This function is useful for downloading images from URLs and saving them locally. It handles potential errors during the download process and provides feedback on whether the download was successful.

Note that the `requests` library is used to make HTTP requests, the `PIL` library is used to work with images, and the `BytesIO` class is used to handle image data as a stream of bytes.

### Conclusion

This script offers a straightforward way to prepare a dataset for machine learning by downloading the required images, filtering out rows where downloads fail, and saving the dataset as a CSV file.

### Sample Script

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

### Sample Code Download  
[Generate a New Dataset Script](../../../../code/04.Finetuning/generate_dataset.py)

### Sample Dataset  
[Sample Dataset Example from Fine-tuning with LoRA Example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.