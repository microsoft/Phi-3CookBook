# 透過從 Hugging Face 下載數據集和相關圖片來生成圖像數據集

### 概述

這個腳本通過下載所需的圖片，過濾掉圖片下載失敗的行，並將數據集保存為 CSV 文件來為機器學習準備數據集。

### 先決條件

在運行此腳本之前，請確保已安裝以下庫：`Pandas`, `Datasets`, `requests`, `PIL` 和 `io`。你還需要在第 2 行將 `'Insert_Your_Dataset'` 替換為你從 Hugging Face 獲取的數據集名稱。

所需庫：

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 功能

腳本執行以下步驟：

1. 使用 `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` 函數從 Hugging Face 下載數據集，並將其轉換為 pandas DataFrame 格式。然後，它會嘗試下載數據集中每一行的圖片，並過濾掉下載失敗的行。最後，將過濾後的數據集保存為 CSV 文件。

### 這是如何工作的

download_image 函數接受兩個參數：image_url，即要下載的圖片的 URL，以及 save_path，即下載的圖片將保存的路徑。

函數的工作原理如下：

首先，它使用 requests.get 方法向 image_url 發送 GET 請求，從 URL 獲取圖片數據。

response.raise_for_status() 行檢查請求是否成功。如果響應狀態碼指示錯誤（例如 404 - 未找到），它將引發異常。這確保我們只有在請求成功的情況下才繼續下載圖片。

然後將圖片數據傳遞給 PIL（Python Imaging Library）模塊中的 Image.open 方法。此方法從圖片數據創建一個 Image 對象。

image.save(save_path) 行將圖片保存到指定的 save_path。save_path 應包括所需的文件名和擴展名。

最後，函數返回 True 表示圖片已成功下載並保存。如果過程中發生任何異常，它會捕獲異常，打印一條錯誤消息並返回 False。

此函數用於從 URL 下載圖片並將其保存到本地。它處理下載過程中的潛在錯誤，並提供下載是否成功的反饋。

值得注意的是，requests 庫用於發送 HTTP 請求，PIL 庫用於處理圖片，而 BytesIO 類用於將圖片數據作為字節流處理。

### 結論

這個腳本提供了一種方便的方法來為機器學習準備數據集，通過下載所需的圖片，過濾掉下載失敗的行，並將數據集保存為 CSV 文件。

### 示例腳本

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

### 示例代碼下載
[生成新數據集腳本](../../../../code/04.Finetuning/generate_dataset.py)

### 示例數據集
[從 LORA 示例微調的示例數據集](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**免責聲明**:
本文檔已使用基於機器的AI翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始語言的文檔視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀不承擔責任。