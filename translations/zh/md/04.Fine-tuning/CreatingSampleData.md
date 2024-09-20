# 通过从 Hugging Face 下载数据集并生成图像数据集

### 概述

此脚本通过下载所需的图像，过滤掉下载失败的行，并将数据集保存为 CSV 文件，为机器学习准备数据集。

### 前提条件

在运行此脚本之前，请确保安装了以下库：`Pandas`、`Datasets`、`requests`、`PIL` 和 `io`。您还需要将第 2 行中的 `'Insert_Your_Dataset'` 替换为您从 Hugging Face 获取的数据集名称。

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

脚本执行以下步骤：

1. 使用 `load_dataset()` 函数从 Hugging Face 下载数据集。
2. 使用 `to_pandas()` 方法将 Hugging Face 数据集转换为 Pandas DataFrame 以便于操作。
3. 创建目录以保存数据集和图像。
4. 通过遍历 DataFrame 中的每一行，使用自定义 `download_image()` 函数下载图像，并将过滤后的行附加到名为 `filtered_rows` 的新 DataFrame 中，过滤掉图像下载失败的行。
5. 创建一个包含过滤行的新 DataFrame 并将其保存到磁盘为 CSV 文件。
6. 打印一条消息，指示数据集和图像保存的位置。

### 自定义函数

`download_image()` 函数从 URL 下载图像并使用 Pillow 图像库 (PIL) 和 `io` 模块将其本地保存。如果图像成功下载，则返回 True，否则返回 False。当请求失败时，该函数还会引发带有错误消息的异常。

### 工作原理

`download_image` 函数接受两个参数：`image_url` 是要下载的图像的 URL，`save_path` 是下载的图像将保存的路径。

函数的工作原理如下：

首先使用 `requests.get` 方法对 `image_url` 进行 GET 请求。这将从 URL 检索图像数据。

`response.raise_for_status()` 行检查请求是否成功。如果响应状态码指示错误（例如 404 - 未找到），它将引发异常。这确保我们只有在请求成功时才继续下载图像。

然后将图像数据传递给 PIL（Python Imaging Library）模块中的 `Image.open` 方法。此方法从图像数据创建一个 `Image` 对象。

`image.save(save_path)` 行将图像保存到指定的 `save_path`。`save_path` 应包含所需的文件名和扩展名。

最后，函数返回 True 以指示图像已成功下载和保存。如果过程中发生任何异常，它会捕获异常，打印一条指示失败的错误消息，并返回 False。

此函数用于从 URL 下载图像并将其本地保存。它处理下载过程中的潜在错误，并提供下载是否成功的反馈。

值得注意的是，`requests` 库用于进行 HTTP 请求，PIL 库用于处理图像，`BytesIO` 类用于将图像数据处理为字节流。

### 结论

此脚本通过下载所需的图像，过滤掉下载失败的行，并将数据集保存为 CSV 文件，为机器学习准备数据集提供了一种方便的方法。

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
        response.raise_for_status()  # 检查请求是否成功
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")
        return False


# 从 Hugging Face 下载数据集
dataset = load_dataset('Insert_Your_Dataset')


# 将 Hugging Face 数据集转换为 Pandas DataFrame
df = dataset['train'].to_pandas()


# 创建目录以保存数据集和图像
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# 过滤掉图像下载失败的行
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# 创建一个包含过滤行的新 DataFrame
filtered_df = pd.DataFrame(filtered_rows)


# 将更新后的数据集保存到磁盘
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"数据集和图像已保存到 {dataset_dir}")
```

### 示例代码下载 
[生成新数据集脚本](../../../../code/04.Finetuning/generate_dataset.py)

### 示例数据集
[LORA 示例中的微调示例数据集](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

免责声明：此翻译由人工智能模型从原文翻译而来，可能并不完美。
请审核输出内容并进行必要的修改。