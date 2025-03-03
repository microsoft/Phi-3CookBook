# Hugging Faceからデータセットと関連画像をダウンロードして画像データセットを生成

### 概要

このスクリプトは、必要な画像をダウンロードし、画像のダウンロードに失敗した行を除外してデータセットを準備し、最終的にデータセットをCSVファイルとして保存します。

### 前提条件

このスクリプトを実行する前に、以下のライブラリがインストールされていることを確認してください：`Pandas`, `Datasets`, `requests`, `PIL`, `io`。また、2行目の`'Insert_Your_Dataset'`をHugging Faceから取得したデータセット名に置き換える必要があります。

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

1. `load_dataset()` を使用してHugging Faceからデータセットをダウンロードします。
2. `to_pandas()` を使ってデータセットをPandasデータフレームに変換します。
3. 各画像のURLに基づいて画像をダウンロードします。
4. ダウンロードに失敗した行をフィルタリングします。
5. 最終的にデータセットをCSVファイルとして保存します。

`download_image()` 関数は、URLから画像をダウンロードし、Pillow Image Library（PIL）および`io`モジュールを使用してローカルに保存します。この関数は画像のダウンロードが成功した場合はTrueを返し、失敗した場合はFalseを返します。また、リクエストが失敗した際にはエラーメッセージを含む例外を発生させます。

### 動作の仕組み

`download_image` 関数は2つのパラメータを受け取ります：`image_url`（ダウンロード対象の画像URL）と`save_path`（ダウンロードした画像を保存するパス）。

以下は関数の動作の流れです：

1. `requests.get` メソッドを使用して `image_url` にGETリクエストを送信し、URLから画像データを取得します。
2. `response.raise_for_status()` 行でリクエストが成功したかどうかを確認します。ステータスコードがエラーを示す場合（例：404 - Not Found）、例外を発生させます。これにより、リクエストが成功した場合のみ処理を進めることが保証されます。
3. 画像データはPIL（Python Imaging Library）モジュールの `Image.open` メソッドに渡されます。このメソッドは画像データからImageオブジェクトを作成します。
4. `image.save(save_path)` 行で、画像を指定された `save_path` に保存します。この `save_path` には保存したいファイル名と拡張子を含める必要があります。
5. 最終的に、画像のダウンロードと保存が成功したことを示すためにTrueを返します。処理中に例外が発生した場合は、例外をキャッチしてエラーメッセージを出力し、Falseを返します。

この関数は、URLから画像をダウンロードしてローカルに保存するのに役立ちます。ダウンロードプロセス中の潜在的なエラーを処理し、ダウンロードが成功したかどうかのフィードバックを提供します。

なお、HTTPリクエストには `requests` ライブラリが使用され、画像処理には `PIL` ライブラリが使用され、バイトストリームとして画像データを処理するために `BytesIO` クラスが使用されます。

### 結論

このスクリプトは、必要な画像をダウンロードし、ダウンロードに失敗した行をフィルタリングし、データセットをCSVファイルとして保存することで、機械学習用データセットを簡単に準備する方法を提供します。

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
[LORAを使用したファインチューニングの例からのサンプルデータセット](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があります。元の言語で記載された原文が信頼できる情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。