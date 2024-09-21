# 透過從 Hugging Face 下載資料集並生成影像資料集

### 概述

這個腳本透過下載所需的影像、過濾掉下載失敗的行，並將資料集儲存為 CSV 檔案，來準備機器學習所需的資料集。

### 先決條件

在運行這個腳本之前，請確保已安裝以下庫：`Pandas`、`Datasets`、`requests`、`PIL` 和 `io`。你還需要將第 2 行的 `'Insert_Your_Dataset'` 替換為你從 Hugging Face 取得的資料集名稱。

所需庫：

```python
import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 功能說明

這個腳本執行以下步驟：

1. 使用 `load_dataset()` 函數從 Hugging Face 下載資料集。
2. 使用 `to_pandas()` 方法將 Hugging Face 資料集轉換為 Pandas DataFrame，以便更容易操作。
3. 創建目錄以儲存資料集和影像。
4. 通過遍歷 DataFrame 中的每一行，使用自定義的 `download_image()` 函數下載影像，並將下載失敗的行過濾掉，將過濾後的行附加到新的 DataFrame 中，稱為 `filtered_rows`。
5. 使用過濾後的行創建一個新的 DataFrame，並將其儲存為 CSV 檔案。
6. 打印一條訊息，指示資料集和影像的儲存位置。

### 自定義函數

`download_image()` 函數從 URL 下載影像並使用 Pillow 影像庫 (PIL) 和 `io` 模組將其儲存到本地。若影像成功下載，則返回 True，否則返回 False。當請求失敗時，該函數還會引發異常並顯示錯誤訊息。

### 如何運作

`download_image` 函數接受兩個參數：`image_url` 是要下載的影像 URL，`save_path` 是下載的影像將儲存的路徑。

函數的運作方式如下：

首先，使用 `requests.get` 方法對 `image_url` 發出 GET 請求。這將從 URL 獲取影像數據。

`response.raise_for_status()` 行檢查請求是否成功。如果響應狀態碼指示錯誤（例如 404 - 未找到），則會引發異常。這確保我們只有在請求成功時才繼續下載影像。

然後將影像數據傳遞給 PIL（Python Imaging Library）模組的 `Image.open` 方法。此方法從影像數據創建一個 Image 對象。

`image.save(save_path)` 行將影像儲存到指定的 `save_path`。`save_path` 應包含所需的文件名和擴展名。

最後，函數返回 True，表示影像已成功下載並儲存。如果在過程中發生任何異常，它會捕獲異常，打印一條指示失敗的錯誤訊息，並返回 False。

這個函數對於從 URL 下載影像並將其儲存到本地非常有用。它處理下載過程中的潛在錯誤，並提供有關下載是否成功的反饋。

值得注意的是，`requests` 庫用於發出 HTTP 請求，`PIL` 庫用於處理影像，而 `BytesIO` 類用於將影像數據作為字節流處理。

### 結論

這個腳本提供了一種方便的方法來準備機器學習所需的資料集，通過下載所需的影像、過濾掉下載失敗的行，並將資料集儲存為 CSV 檔案。

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
        response.raise_for_status()  # 檢查請求是否成功
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


# 創建目錄以儲存資料集和影像
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# 過濾掉影像下載失敗的行
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# 使用過濾後的行創建一個新的 DataFrame
filtered_df = pd.DataFrame(filtered_rows)


# 將更新後的資料集儲存到磁碟
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"Dataset and images saved to {dataset_dir}")
```

### 範例代碼下載 
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### 範例資料集
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

免責聲明：此翻譯由人工智慧模型從原文翻譯而來，可能不夠完美。請檢查輸出內容並進行任何必要的修正。