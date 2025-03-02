# 透過下載 Hugging Face 的數據集及相關圖片生成圖像數據集

### 概覽

此腳本通過下載所需圖片，過濾掉無法成功下載圖片的行，並將數據集保存為 CSV 文件，來準備機器學習所需的數據集。

### 前置條件

在運行此腳本之前，請確保已安裝以下庫：`Pandas`、`Datasets`、`requests`、`PIL` 和 `io`。此外，需將第 2 行的 `'Insert_Your_Dataset'` 替換為來自 Hugging Face 的數據集名稱。

所需庫：

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 功能介紹

此腳本執行以下步驟：

1. 使用 `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` 函數從 Hugging Face 下載數據集。
2. 過濾掉無法成功下載圖片的行。
3. 將過濾後的數據集保存為 CSV 文件。

` function, and appending the filtered row to a new DataFrame called ` 函數通過 URL 下載圖片，並使用 Pillow 圖像庫（PIL）及 `io` 模組將圖片保存至本地。如果圖片成功下載，則返回 True，否則返回 False。當請求失敗時，該函數還會拋出包含錯誤訊息的異常。

### 運作方式

`download_image` 函數接收兩個參數：  
- `image_url`：要下載圖片的 URL。  
- `save_path`：下載後圖片保存的路徑。

以下是該函數的運作方式：

1. 首先使用 `requests.get` 方法向 `image_url` 發送 GET 請求，從 URL 獲取圖片數據。
2. 使用 `response.raise_for_status()` 檢查請求是否成功。如果響應的狀態碼顯示錯誤（例如 404 - 未找到），則拋出異常，確保只有在請求成功時才繼續下載圖片。
3. 將圖片數據傳遞給 PIL（Python Imaging Library）的 `Image.open` 方法，該方法會從圖片數據中創建一個 Image 對象。
4. 使用 `image.save(save_path)` 將圖片保存到指定的 `save_path`，其中應包含目標文件名及擴展名。
5. 最後，函數返回 True，表示圖片成功下載並保存。如果過程中出現異常，則捕獲異常，打印失敗的錯誤訊息，並返回 False。

此函數用於從 URL 下載圖片並保存至本地。它在下載過程中處理潛在的錯誤，並提供有關下載是否成功的反饋。

需要注意的是，該函數使用 `requests` 庫進行 HTTP 請求，使用 PIL 庫處理圖像，並使用 `BytesIO` 類作為字節流處理圖片數據。

### 結論

此腳本提供了一種方便的方法來準備機器學習所需的數據集，通過下載所需圖片、過濾掉下載失敗的行，並將數據集保存為 CSV 文件。

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
[微調 LORA 示例中的數據集範例](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**免責聲明**:  
此文件是使用機器翻譯人工智能服務進行翻譯的。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原文的母語版本應被視為權威來源。對於關鍵信息，建議尋求專業的人手翻譯。我們對因使用此翻譯而產生的任何誤解或誤釋不承擔責任。