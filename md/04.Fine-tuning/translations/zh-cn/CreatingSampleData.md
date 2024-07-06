
# 通过从Hugging Face下载数据集和关联图片生成图像数据集


### 概述

该脚本通过下载所需图片、过滤下载失败的行，并将数据集保存为CSV文件，为机器学习准备数据集。

### 先决条件

在运行此脚本之前，请确保已安装以下库：`Pandas`, `Datasets`, `requests`, `PIL` 和  `io`. 同时，需要将第2行的 `'Insert_Your_Dataset'` 替换为来自Hugging Face的数据集名称。

需要安装的库:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 功能

脚本执行以下步骤：

1. 使用 `load_dataset()` 函数从 Hugging Face 下载数据集。
2. 使用 `to_pandas()` 方法将 Hugging Face 数据集转换为 Pandas DataFrame，以便更容易地进行操作。.
3. 创建目录以保存数据集和图像。
4. 通过遍历 DataFrame 中的每一行，使用自定义的 `download_image()` 函数下载图像，并将过滤后的行追加到名为 `filtered_rows` 的新 DataFrame 中，从而过滤掉图像下载失败的行。
5. 使用过滤后的行创建一个新的 DataFrame，并将其保存为 CSV 文件。
6. 打印一条消息，指示数据集和图像已保存的位置。

### 自定义函数

`download_image()` 函数使用 Pillow 图像库（PIL）和 `io` 模块从 URL 下载图像并将其本地保存。如果图像成功下载，则返回 True，否则返回 False。当请求失败时，该函数还会引发带有错误消息的异常。

### 它如何工作

`download_image()` 函数接受两个参数：image_url，即要下载的图像的 URL；以及 save_path，即下载的图像将被保存的路径。

该函数的工作原理如下：

该函数首先使用 requests.get 方法向 image_url 发送 GET 请求。这将从 URL 检索图像数据。

response.raise_for_status() 行检查请求是否成功。如果响应状态代码表示错误（例如，404 - 未找到），则会引发异常。这确保我们只在请求成功时才继续下载图像。

然后将图像数据传递给 PIL（Python Imaging Library）模块的 Image.open 方法。此方法从图像数据创建一个 Image 对象。

image.save(save_path) 行将图像保存到指定的 save_path。save_path 应包括所需的文件名和扩展名。

最后，该函数返回 True，表示图像已成功下载并保存。如果在过程中发生任何异常，它将捕获异常，打印指示失败的错误消息，并返回 False。

此函数可用于从 URL 下载图像并将其本地保存。它处理下载过程中可能出现的错误，并提供有关下载是否成功的反馈。

值得注意的是，requests 库用于发出 HTTP 请求，PIL 库用于处理图像，BytesIO 类用于将图像数据作为字节流处理。



### 总结

该脚本通过下载所需的图像、过滤掉图像下载失败的行以及将数据集保存为 CSV 文件，为机器学习提供了一个便捷的方式来准备数据集。

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
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### 示例数据集
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)
