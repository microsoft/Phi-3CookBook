# 通过从 Hugging Face 下载数据集及相关图片生成图像数据集

### 概述

该脚本通过下载所需的图片，过滤掉图片下载失败的行，并将数据集保存为 CSV 文件，为机器学习准备数据集。

### 前置条件

在运行此脚本之前，请确保已安装以下库：`Pandas`、`Datasets`、`requests`、`PIL` 和 `io`。此外，需要将第 2 行的 `'Insert_Your_Dataset'` 替换为 Hugging Face 上数据集的名称。

所需库：

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 功能

该脚本执行以下步骤：

1. 使用 `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` 函数从 Hugging Face 下载数据集，将其转换为 Pandas 数据框，下载相关图片，并过滤掉下载失败的行。
2. 将过滤后的数据集保存为 CSV 文件。

### 工作原理

`download_image` 函数接收两个参数：`image_url`（要下载的图片的 URL）和 `save_path`（下载图片保存的路径）。

以下是函数的工作流程：

1. 使用 `requests.get` 方法向 `image_url` 发起 GET 请求，从 URL 获取图片数据。
2. `response.raise_for_status()` 检查请求是否成功。如果响应状态码表明请求出错（例如 404 - 未找到），将抛出异常。这确保仅在请求成功时继续下载图片。
3. 使用 PIL（Python Imaging Library）模块中的 `Image.open` 方法将图片数据转换为 Image 对象。
4. `image.save(save_path)` 将图片保存到指定的 `save_path`，该路径应包含文件名及其扩展名。
5. 函数返回 `True`，表示图片成功下载并保存。如果过程中出现任何异常，函数将捕获异常，打印错误信息并返回 `False`。

此函数适用于从 URL 下载图片并将其保存到本地。它处理下载过程中的潜在错误，并提供关于下载是否成功的反馈。

需要注意的是，该函数使用 `requests` 库发起 HTTP 请求，使用 PIL 库处理图片，并使用 `BytesIO` 类以字节流的形式处理图片数据。

### 结论

该脚本提供了一种便捷的方法，通过下载所需图片、过滤掉图片下载失败的行，并将数据集保存为 CSV 文件，为机器学习准备数据集。

### 示例脚本

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

### 示例代码下载 
[生成新数据集脚本](../../../../code/04.Finetuning/generate_dataset.py)

### 示例数据集
[微调 LORA 示例的示例数据集](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文件为权威来源。对于关键信息，建议寻求专业人工翻译。我们对因使用本翻译而导致的任何误解或误读不承担责任。