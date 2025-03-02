# 從 Hugging Face 下載數據集及相關圖片來生成影像數據集

### 概述

此腳本透過下載所需圖片，過濾掉無法下載圖片的行，並將數據集儲存為 CSV 文件，為機器學習準備數據集。

### 前置需求

在執行此腳本之前，請確保已安裝以下函式庫：`Pandas`、`Datasets`、`requests`、`PIL` 和 `io`。此外，您需要將第 2 行中的 `'Insert_Your_Dataset'` 替換為您從 Hugging Face 獲取的數據集名稱。

所需函式庫：

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 功能

此腳本執行以下步驟：

1. 使用 `load_dataset()` 從 Hugging Face 下載數據集。
2. 將數據集轉換為 Pandas 資料框格式，透過 `to_pandas()` 方法。
3. 使用 `download_image()` 函數下載圖片。
4. 過濾掉無法成功下載圖片的行。
5. 將結果保存為 CSV 文件。

#### `download_image()` 函數

`download_image()` 函數使用 Pillow 圖片庫（PIL）和 `io` 模組，從 URL 下載圖片並本地保存。若圖片成功下載，函數返回 True；否則返回 False。在請求失敗時，該函數會拋出包含錯誤訊息的異常。

### 運作方式

`download_image()` 函數接受兩個參數：`image_url` 和 `save_path`。`image_url` 是要下載的圖片的 URL，而 `save_path` 是下載後圖片的儲存路徑。

以下是函數的運作方式：

1. 使用 `requests.get` 方法對 `image_url` 發送 GET 請求，從 URL 獲取圖片數據。
2. `response.raise_for_status()` 檢查請求是否成功。如果狀態碼顯示錯誤（例如 404 - 找不到資源），則會拋出異常，確保僅在請求成功時繼續下載。
3. 使用 PIL（Python Imaging Library）模組的 `Image.open` 方法將圖片數據轉換為 Image 對象。
4. 通過 `image.save(save_path)` 將圖片儲存到指定的 `save_path`。`save_path` 應包含目標檔名及副檔名。
5. 最後，函數返回 True 表示圖片成功下載並保存。如果過程中出現異常，則捕捉該異常，打印錯誤訊息，並返回 False。

此函數適用於從 URL 下載圖片並將其本地保存。它能處理下載過程中的潛在錯誤，並提供下載是否成功的回饋。

值得注意的是，該函數使用 `requests` 庫進行 HTTP 請求，`PIL` 庫處理圖片，而 `BytesIO` 類則用於將圖片數據作為字節流處理。

### 結論

此腳本提供了一種方便的方法來為機器學習準備數據集，透過下載所需圖片，過濾掉下載失敗的行，並將結果保存為 CSV 文件。

### 範例腳本

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

### 範例代碼下載 
[生成新數據集腳本](../../../../code/04.Finetuning/generate_dataset.py)

### 範例數據集
[從 LORA 微調範例中取得的數據集範例](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**免責聲明**：  
本文件使用機器翻譯服務進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原文檔的母語版本應被視為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或錯誤解讀概不負責。