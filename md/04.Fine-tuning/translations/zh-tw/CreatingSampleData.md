# 透過從 Hugging Face 下載 DataSet 和相關圖片來生成圖像數據集

### 概述

這個腳本透過下載所需的圖片來準備機器學習的資料集，過濾掉圖片下載失敗的行，並將資料集保存為 CSV 文件。

### 先決條件

在執行此腳本之前，請確保已安裝以下函式庫: `Pandas`、`Datasets`、`requests`、`PIL` 和 `io`。你還需要將第 2 行中的 `'Insert_Your_Dataset'` 替換為 Hugging Face 上你的數據集名稱。

所需函式庫:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 功能

這個腳本執行以下步驟:

1. 使用 `load_dataset()` 函式從 Hugging Face 下載數據集。
2. 使用 `to_pandas()` 方法將 Hugging Face 數據集轉換為 Pandas DataFrame 以便於操作。
3. 建立目錄以保存數據集和圖片。
4. 通過遍歷 DataFrame 中的每一行，使用自定義的 `download_image()` 函式下載圖片，並將過濾後的行附加到名為 `filtered_rows` 的新 DataFrame 中，過濾掉圖片下載失敗的行。
5. 建立一個包含過濾行的新 DataFrame，並將其保存到磁碟上作為 CSV 文件。
6. 列印一條訊息，指示數據集和圖片已保存的位置。

### 自訂函式

`download_image()` 函式從 URL 下載圖片並使用 Pillow Image 函式庫（PIL）和 `io` 模組將其本地保存。如果圖片成功下載則返回 True，否則返回 False。當請求失敗時，該函式還會引發帶有錯誤訊息的例外。

### 這是如何運作的

下載_圖片 函式 接受兩個參數: image_url, 即要下載的圖片的 URL, 和 save_path, 即下載的圖片將被保存的路徑。

以下是這個函式的運作方式:

它首先使用 requests.get 方法對 image_url 發出 GET 請求。這會從 URL 獲取圖片資料。

response.raise_for_status() 行檢查請求是否成功。如果回應狀態碼表示錯誤（例如，404 - Not Found），它將引發異常。這確保我們只有在請求成功時才繼續下載圖像。

圖像資料然後傳遞給 PIL (Python Imaging Library) 模組中的 Image.open 方法。此方法從圖像資料建立一個 Image 物件。

image.save(save_path) 行將圖像保存到指定的 save_path。save_path 應包括所需的文件名和擴展名。

最後，函式返回 True 以表示圖像已成功下載並保存。如果在過程中發生任何異常，它會捕獲異常，打印一條錯誤訊息以指示失敗，並返回 False。

此函式對於從 URL 下載圖片並將其本地保存非常有用。它處理下載過程中可能出現的錯誤，並提供下載是否成功的反饋。

值得注意的是，requests 函式庫用於發送 HTTP 請求，PIL 函式庫用於處理圖像，而 BytesIO 類別用於將圖像資料作為位元流來處理。

### 結論

這個腳本提供了一種方便的方法來準備機器學習的數據集，通過下載所需的圖像，過濾掉圖像下載失敗的行，並將數據集保存為 CSV 文件。

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


# 從 Hugging Face 下載資料集
dataset = load_dataset('Insert_Your_Dataset')


# 將 Hugging Face 資料集轉換為 Pandas DataFrame
df = dataset['train'].to_pandas()


# 建立目錄以保存資料集和圖片
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# 過濾出圖片下載失敗的行
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# 建立一個包含過濾行的新 DataFrame
filtered_df = pd.DataFrame(filtered_rows)


# 將更新的資料集保存到磁碟
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"Dataset and images saved to {dataset_dir}")
```

### 範例程式碼下載

[生成新的資料集腳本](../../../../code/04.Finetuning/translations/zh-tw/generate_dataset.py)

### 範例資料集

[範例 資料集 範例 from finetuning with LORA 範例](../../../../code/04.Finetuning/translations/zh-tw/olive-ort-example/dataset/dataset-classification.json)

