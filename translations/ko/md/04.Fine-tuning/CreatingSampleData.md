# Hugging Face에서 데이터셋과 관련 이미지를 다운로드하여 이미지 데이터셋 생성하기

### 개요

이 스크립트는 필요한 이미지를 다운로드하고, 이미지 다운로드에 실패한 행을 필터링하여 데이터셋을 CSV 파일로 저장하여 머신 러닝을 위한 데이터셋을 준비합니다.

### 사전 요구 사항

이 스크립트를 실행하기 전에 `Pandas`, `Datasets`, `requests`, `PIL`, `io` 라이브러리가 설치되어 있는지 확인하세요. 또한, 2번째 줄에 있는 `'Insert_Your_Dataset'`을 Hugging Face에서 사용할 데이터셋 이름으로 교체해야 합니다.

필요한 라이브러리:

```python
import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### 기능

이 스크립트는 다음 단계를 수행합니다:

1. `load_dataset()` 함수를 사용하여 Hugging Face에서 데이터셋을 다운로드합니다.
2. Hugging Face 데이터셋을 `to_pandas()` 메서드를 사용하여 Pandas DataFrame으로 변환합니다.
3. 데이터셋과 이미지를 저장할 디렉토리를 생성합니다.
4. DataFrame의 각 행을 반복하면서 커스텀 `download_image()` 함수를 사용하여 이미지를 다운로드하고, 다운로드에 실패한 행을 필터링하여 새로운 DataFrame인 `filtered_rows`에 추가합니다.
5. 필터링된 행으로 새로운 DataFrame을 생성하고, 이를 CSV 파일로 디스크에 저장합니다.
6. 데이터셋과 이미지가 저장된 위치를 나타내는 메시지를 출력합니다.

### 커스텀 함수

`download_image()` 함수는 URL에서 이미지를 다운로드하고 Pillow Image Library (PIL)와 `io` 모듈을 사용하여 로컬에 저장합니다. 이 함수는 이미지가 성공적으로 다운로드되면 True를 반환하고, 그렇지 않으면 False를 반환합니다. 요청이 실패할 경우 오류 메시지와 함께 예외를 발생시킵니다.

### 작동 방식

`download_image` 함수는 두 개의 매개변수를 받습니다: 다운로드할 이미지의 URL인 `image_url`과 다운로드된 이미지를 저장할 경로인 `save_path`입니다.

함수의 작동 방식은 다음과 같습니다:

먼저 `requests.get` 메서드를 사용하여 `image_url`에 GET 요청을 보냅니다. 이를 통해 URL에서 이미지 데이터를 가져옵니다.

`response.raise_for_status()` 줄은 요청이 성공했는지 확인합니다. 응답 상태 코드가 오류를 나타내면(예: 404 - 찾을 수 없음) 예외를 발생시킵니다. 이는 요청이 성공한 경우에만 이미지를 다운로드하도록 합니다.

이미지 데이터는 PIL(Python Imaging Library) 모듈의 `Image.open` 메서드에 전달됩니다. 이 메서드는 이미지 데이터로부터 Image 객체를 생성합니다.

`image.save(save_path)` 줄은 이미지를 지정된 `save_path`에 저장합니다. `save_path`는 원하는 파일 이름과 확장자를 포함해야 합니다.

마지막으로, 함수는 이미지가 성공적으로 다운로드되고 저장되었음을 나타내기 위해 True를 반환합니다. 과정 중에 예외가 발생하면 예외를 잡아 오류 메시지를 출력하고 False를 반환합니다.

이 함수는 URL에서 이미지를 다운로드하고 로컬에 저장하는 데 유용합니다. 다운로드 과정 중 발생할 수 있는 잠재적인 오류를 처리하고 다운로드가 성공했는지 여부에 대한 피드백을 제공합니다.

참고로, `requests` 라이브러리는 HTTP 요청을 만들기 위해 사용되며, `PIL` 라이브러리는 이미지를 다루기 위해 사용되고, `BytesIO` 클래스는 이미지 데이터를 바이트 스트림으로 처리하는 데 사용됩니다.

### 결론

이 스크립트는 필요한 이미지를 다운로드하고, 이미지 다운로드에 실패한 행을 필터링하여 데이터셋을 CSV 파일로 저장함으로써 머신 러닝을 위한 데이터셋을 준비하는 편리한 방법을 제공합니다.

### 샘플 스크립트

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

### 샘플 코드 다운로드
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### 샘플 데이터셋
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

면책 조항: 이 번역은 원본을 AI 모델에 의해 번역된 것이며 완벽하지 않을 수 있습니다. 
출력을 검토하고 필요한 수정 사항을 반영해 주시기 바랍니다.