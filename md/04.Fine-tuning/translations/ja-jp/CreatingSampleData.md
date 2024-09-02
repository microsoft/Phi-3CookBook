# Hugging Faceからデータセットと関連画像をダウンロードして画像データセットを生成する

### 概要

このスクリプトは、必要な画像をダウンロードし、画像のダウンロードが失敗した行をフィルタリングし、データセットをCSVファイルとして保存することで、機械学習のためのデータセットを準備します。

### 前提条件

このスクリプトを実行する前に、以下のライブラリがインストールされていることを確認してください：`Pandas`、`Datasets`、`requests`、`PIL`、および`io`。また、Hugging Faceからのデータセット名を第2行の`'Insert_Your_Dataset'`に置き換える必要があります。

必要なライブラリ：

```python
import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 機能

このスクリプトは以下の手順を実行します：

1. `load_dataset()`関数を使用してHugging Faceからデータセットをダウンロードします。
2. `to_pandas()`メソッドを使用してHugging Faceデータセットを操作しやすいようにPandas DataFrameに変換します。
3. データセットと画像を保存するためのディレクトリを作成します。
4. DataFrameの各行を反復処理し、カスタム`download_image()`関数を使用して画像をダウンロードし、フィルタリングされた行を`filtered_rows`という新しいDataFrameに追加することで、画像のダウンロードが失敗した行をフィルタリングします。
5. フィルタリングされた行を含む新しいDataFrameを作成し、それをディスクにCSVファイルとして保存します。
6. データセットと画像が保存された場所を示すメッセージを表示します。

### カスタム関数

`download_image()`関数は、URLから画像をダウンロードし、Pillow Image Library（PIL）と`io`モジュールを使用してローカルに保存します。画像が正常にダウンロードされた場合はTrueを返し、そうでない場合はFalseを返します。リクエストが失敗した場合、この関数はエラーメッセージを含む例外を発生させます。

### 仕組み

`download_image`関数は、ダウンロードする画像のURLである`image_url`と、ダウンロードした画像を保存するパスである`save_path`の2つのパラメータを受け取ります。

この関数の動作は次のとおりです：

まず、`requests.get`メソッドを使用して`image_url`にGETリクエストを送信します。これにより、URLから画像データが取得されます。

`response.raise_for_status()`行は、リクエストが成功したかどうかを確認します。応答ステータスコードがエラーを示している場合（例：404 - 見つかりません）、例外が発生します。これにより、リクエストが成功した場合にのみ画像のダウンロードを続行することが保証されます。

次に、画像データがPIL（Python Imaging Library）モジュールの`Image.open`メソッドに渡されます。このメソッドは、画像データからImageオブジェクトを作成します。

`image.save(save_path)`行は、画像を指定された`save_path`に保存します。`save_path`には、必要なファイル名と拡張子が含まれている必要があります。

最後に、この関数はTrueを返し、画像が正常にダウンロードおよび保存されたことを示します。プロセス中に何らかの例外が発生した場合、例外をキャッチし、失敗を示すエラーメッセージを表示し、Falseを返します。

この関数は、URLから画像をダウンロードしてローカルに保存するのに役立ちます。ダウンロードプロセス中に発生する可能性のあるエラーを処理し、ダウンロードが成功したかどうかのフィードバックを提供します。

requestsライブラリはHTTPリクエストを行うために使用され、PILライブラリは画像を操作するために使用され、BytesIOクラスは画像データをバイトストリームとして処理するために使用されます。

### 結論

このスクリプトは、必要な画像をダウンロードし、画像のダウンロードが失敗した行をフィルタリングし、データセットをCSVファイルとして保存することで、機械学習のためのデータセットを準備する便利な方法を提供します。

### サンプルスクリプト

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

### サンプルコードのダウンロード
[新しいデータセットスクリプトを生成](../../../../code/04.Finetuning/generate_dataset.py)

### サンプルデータセット
[LORAの例でファインチューニングされたサンプルデータセットの例](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)
