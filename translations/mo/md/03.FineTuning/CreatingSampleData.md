# 生成图像数据集：从 Hugging Face 下载数据集及相关图片

### 概述

此脚本通过下载所需的图片、过滤掉下载失败的行，并将数据集保存为 CSV 文件，为机器学习准备数据集。

### 前提条件

在运行此脚本之前，请确保已安装以下库：`Pandas`、`Datasets`、`requests`、`PIL` 和 `io`。此外，需要将第 2 行中的 `'Insert_Your_Dataset'` 替换为 Hugging Face 数据集的名称。

所需库：

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 功能说明

脚本执行以下步骤：

1. 使用 `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` 函数从 Hugging Face 下载数据集并转换为 Pandas 数据框。
2. 下载失败的行会被过滤掉。
3. 处理后的数据集将保存为 CSV 文件。

#### download_image 函数说明

`download_image()` 函数通过 PIL 图像库（Pillow）和 `io` 模块从 URL 下载图像并将其本地保存。函数在成功下载时返回 True，失败时返回 False。如果请求失败，还会抛出异常并显示错误信息。

### 工作原理

`download_image` 函数接收两个参数：`image_url`（待下载图像的 URL）和 `save_path`（图像保存路径）。

以下是函数的工作流程：

1. 使用 `requests.get` 方法对 `image_url` 发起 GET 请求，从 URL 获取图像数据。
2. `response.raise_for_status()` 检查请求是否成功。如果状态码显示错误（如 404 - 未找到），则抛出异常。确保仅在请求成功时继续下载图像。
3. 将图像数据传递给 PIL 模块的 `Image.open` 方法。该方法从图像数据中创建一个 Image 对象。
4. `image.save(save_path)` 将图像保存到指定的 `save_path`，路径应包括所需的文件名和扩展名。
5. 如果图像成功下载并保存，函数返回 True。如果过程中发生任何异常，捕获异常并打印错误信息，同时返回 False。

此函数可用于从 URL 下载图像并将其本地保存。它处理下载过程中的潜在错误，并提供下载是否成功的反馈。

需要注意的是，此函数使用 `requests` 库进行 HTTP 请求，`PIL` 库处理图像，`BytesIO` 类以字节流形式处理图像数据。

### 结论

此脚本提供了一种便捷的方法，通过下载所需的图像、过滤掉下载失败的行，并将数据集保存为 CSV 文件，为机器学习准备数据集。

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
[微调 LORA 示例中的数据集示例](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

It seems like "mo" might refer to a language or abbreviation, but it is unclear what specific language or context you're referring to. Could you clarify what "mo" stands for? For example, is it Maori, Mongolian, or something else? Let me know so I can assist you better!