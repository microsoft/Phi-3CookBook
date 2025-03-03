# 허깅 페이스에서 데이터셋과 관련 이미지를 다운로드하여 이미지 데이터셋 생성하기

### 개요

이 스크립트는 머신러닝을 위한 데이터셋을 준비하기 위해 필요한 이미지를 다운로드하고, 이미지 다운로드에 실패한 행을 필터링한 후 데이터셋을 CSV 파일로 저장합니다.

### 사전 준비

이 스크립트를 실행하기 전에 다음 라이브러리들이 설치되어 있어야 합니다: `Pandas`, `Datasets`, `requests`, `PIL`, `io`. 또한, 2번째 줄의 `'Insert_Your_Dataset'`를 허깅 페이스에서 사용할 데이터셋 이름으로 교체해야 합니다.

필수 라이브러리:

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

1. 허깅 페이스에서 `load_dataset()`을 사용하여 데이터셋을 다운로드합니다.  
2. `to_pandas()`를 호출하여 데이터를 판다스 데이터프레임으로 변환합니다.  
3. `download_image()` 함수를 사용하여 이미지를 다운로드합니다.  
4. 다운로드에 실패한 행을 필터링합니다.  
5. 필터링된 데이터셋을 CSV 파일로 저장합니다.  

`download_image()` 함수는 URL에서 이미지를 다운로드하여 로컬에 저장하는 역할을 합니다. 이 함수는 Pillow 이미지 라이브러리(PIL)와 `io` 모듈을 사용합니다. 이미지 다운로드에 성공하면 True를 반환하며, 실패 시 False를 반환합니다. 요청이 실패하면 오류 메시지와 함께 예외를 발생시킵니다.

### 작동 방식

`download_image` 함수는 두 개의 매개변수를 받습니다:  
- `image_url`: 다운로드할 이미지의 URL  
- `save_path`: 다운로드한 이미지를 저장할 경로  

함수의 작동 방식은 다음과 같습니다:

1. `requests.get` 메서드를 사용하여 `image_url`에 GET 요청을 보냅니다. 이를 통해 URL에서 이미지 데이터를 가져옵니다.
2. `response.raise_for_status()`는 요청이 성공했는지 확인합니다. 상태 코드가 오류를 나타내면(e.g., 404 - Not Found) 예외를 발생시킵니다. 이를 통해 요청이 성공했을 때만 이미지 다운로드를 진행합니다.
3. 이미지 데이터는 PIL(Python Imaging Library) 모듈의 `Image.open` 메서드에 전달됩니다. 이 메서드는 이미지 데이터로부터 Image 객체를 생성합니다.
4. `image.save(save_path)`는 이미지를 지정된 `save_path`에 저장합니다. `save_path`에는 원하는 파일 이름과 확장자가 포함되어야 합니다.
5. 함수는 이미지 다운로드 및 저장이 성공적으로 완료되었음을 나타내기 위해 True를 반환합니다.  
6. 과정 중 예외가 발생하면 예외를 잡아 실패를 알리는 오류 메시지를 출력하고 False를 반환합니다.

이 함수는 URL에서 이미지를 다운로드하여 로컬에 저장하는 데 유용합니다. 다운로드 과정에서 발생할 수 있는 오류를 처리하며, 다운로드 성공 여부에 대한 피드백을 제공합니다.

참고로, HTTP 요청을 위해 `requests` 라이브러리를 사용하고, 이미지를 처리하기 위해 `PIL` 라이브러리를 사용하며, 이미지 데이터를 바이트 스트림으로 처리하기 위해 `BytesIO` 클래스를 사용합니다.

### 결론

이 스크립트는 필요한 이미지를 다운로드하고, 다운로드 실패한 행을 필터링하며, 데이터를 CSV 파일로 저장하여 머신러닝을 위한 데이터셋을 편리하게 준비할 수 있는 방법을 제공합니다.

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
[새 데이터셋 생성 스크립트](../../../../code/04.Finetuning/generate_dataset.py)

### 샘플 데이터셋  
[LORA 예제를 사용한 파인튜닝 샘플 데이터셋 예제](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)  

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원어로 작성된 원본 문서를 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.