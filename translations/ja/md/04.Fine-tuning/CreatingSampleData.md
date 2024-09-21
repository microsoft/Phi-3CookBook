# Hugging Faceからデータセットと関連画像をダウンロードして画像データセットを生成

### 概要

このスクリプトは、必要な画像をダウンロードし、ダウンロードに失敗した行をフィルタリングし、データセットをCSVファイルとして保存することで、機械学習用のデータセットを準備します。

### 前提条件

このスクリプトを実行する前に、以下のライブラリがインストールされていることを確認してください: `Pandas`, `Datasets`, `requests`, `PIL`, および `io`。また、Hugging Faceからのデータセット名を2行目の `'Insert_Your_Dataset'` に置き換える必要があります。

必要なライブラリ:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 機能

スクリプトは以下の手順を実行します:

1. `load_dataset()` 関数を使用してHugging Faceからデータセットをダウンロード。
2. `to_pandas()` メソッドを使用してHugging FaceデータセットをPandas DataFrameに変換し、操作しやすくする。
3. データセットと画像を保存するディレクトリを作成。
4. DataFrameの各行を繰り返し処理し、カスタム `download_image()` 関数を使用して画像をダウンロードし、ダウンロードに失敗した行をフィルタリングして新しいDataFrame `filtered_rows` に追加。
5. フィルタリングされた行で新しいDataFrameを作成し、CSVファイルとしてディスクに保存。
6. データセットと画像が保存された場所を示すメッセージを表示。

### カスタム関数

`download_image()` 関数は、URLから画像をダウンロードし、Pillow Image Library (PIL) と `io` モジュールを使用してローカルに保存します。画像が正常にダウンロードされた場合はTrueを返し、そうでない場合はFalseを返します。この関数は、リクエストが失敗した場合にエラーメッセージを含む例外を発生させます。

### 仕組み

`download_image` 関数は2つのパラメータを取ります: `image_url` はダウンロードする画像のURLで、`save_path` はダウンロードした画像を保存するパスです。

関数の動作は次の通りです:

まず、`requests.get` メソッドを使用して `image_url` にGETリクエストを行います。これにより、URLから画像データが取得されます。

`response.raise_for_status()` 行は、リクエストが成功したかどうかをチェックします。レスポンスステータスコードがエラーを示す場合（例：404 - Not Found）、例外が発生します。これにより、リクエストが成功した場合のみ画像のダウンロードを続行します。

次に、画像データがPIL（Python Imaging Library）モジュールの `Image.open` メソッドに渡されます。このメソッドは画像データからImageオブジェクトを作成します。

`image.save(save_path)` 行は、指定された `save_path` に画像を保存します。`save_path` には希望するファイル名と拡張子が含まれている必要があります。

最後に、関数は画像が正常にダウンロードおよび保存されたことを示すためにTrueを返します。プロセス中に例外が発生した場合、例外をキャッチし、失敗を示すエラーメッセージを表示し、Falseを返します。

この関数は、URLから画像をダウンロードしてローカルに保存するのに便利です。ダウンロードプロセス中の潜在的なエラーを処理し、ダウンロードが成功したかどうかに関するフィードバックを提供します。

HTTPリクエストを行うために `requests` ライブラリが使用され、画像を操作するために `PIL` ライブラリが使用され、バイトのストリームとして画像データを処理するために `BytesIO` クラスが使用されている点に注意してください。

### 結論

このスクリプトは、必要な画像をダウンロードし、ダウンロードに失敗した行をフィルタリングし、データセットをCSVファイルとして保存することで、機械学習用のデータセットを準備する便利な方法を提供します。

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
[新しいデータセット生成スクリプト](../../../../code/04.Finetuning/generate_dataset.py)

### サンプルデータセット
[サンプルデータセット例（LORAを使用したファインチューニング例から）](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。出力を確認し、必要な修正を行ってください。