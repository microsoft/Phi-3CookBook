# 通过从 Hugging Face 下载数据集并生成图像数据集

### 概述

此脚本通过下载所需图像，过滤掉下载图像失败的行，并将数据集保存为 CSV 文件，为机器学习准备数据集。

### 先决条件

在运行此脚本之前，请确保已安装以下库：`Pandas`、`Datasets`、`requests`、`PIL` 和 `io`。你还需要将第 2 行的 `'Insert_Your_Dataset'` 替换为你在 Hugging Face 上的数据集名称。

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

The `download_image()` 函数从 Hugging Face 下载数据集。该函数使用 Pillow 图像库 (PIL) 和 `io` 模块从 URL 下载图像并将其本地保存。如果图像成功下载，则返回 True，否则返回 False。当请求失败时，该函数还会引发包含错误信息的异常。

### 这是如何工作的

download_image 函数接收两个参数：image_url，即要下载的图像的 URL，和 save_path，即下载的图像将保存的路径。

函数的工作原理如下：

首先，它使用 requests.get 方法对 image_url 进行 GET 请求。这会从 URL 检索图像数据。

response.raise_for_status() 行检查请求是否成功。如果响应状态码表示错误（例如 404 - 未找到），则会引发异常。这确保我们只有在请求成功时才继续下载图像。

然后将图像数据传递给 PIL（Python Imaging Library）模块的 Image.open 方法。此方法从图像数据创建一个 Image 对象。

image.save(save_path) 行将图像保存到指定的 save_path。save_path 应包含所需的文件名和扩展名。

最后，函数返回 True，表示图像已成功下载并保存。如果在过程中发生任何异常，它会捕获异常，打印指示失败的错误消息，并返回 False。

此函数对于从 URL 下载图像并将其本地保存非常有用。它处理下载过程中的潜在错误，并提供有关下载是否成功的反馈。

值得注意的是，requests 库用于进行 HTTP 请求，PIL 库用于处理图像，BytesIO 类用于将图像数据作为字节流处理。

### 结论

此脚本通过下载所需图像，过滤掉下载图像失败的行，并将数据集保存为 CSV 文件，为机器学习准备数据集提供了一种方便的方法。

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
[来自使用 LORA 示例的微调示例数据集](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**免责声明**：
本文档已使用基于机器的人工智能翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原文档的母语版本视为权威来源。对于关键信息，建议进行专业人工翻译。我们对因使用此翻译而引起的任何误解或误释不承担责任。