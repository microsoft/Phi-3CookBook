# Создание набора данных изображений путем загрузки DataSet с Hugging Face и связанных изображений

### Обзор

Этот скрипт подготавливает набор данных для машинного обучения, загружая необходимые изображения, исключая строки, где загрузка изображений не удалась, и сохраняя набор данных в формате CSV.

### Предварительные условия

Перед запуском этого скрипта убедитесь, что у вас установлены следующие библиотеки: `Pandas`, `Datasets`, `requests`, `PIL` и `io`. Также необходимо заменить `'Insert_Your_Dataset'` на второй строке именем вашего набора данных из Hugging Face.

Необходимые библиотеки:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Функциональность

Скрипт выполняет следующие шаги:

1. Загружает набор данных из Hugging Face с использованием `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`.  
2. Исключает строки, где загрузка изображений не удалась.  
3. Сохраняет отфильтрованный набор данных в формате CSV.  

### Как это работает

Функция download_image принимает два параметра: image_url, который представляет собой URL изображения для загрузки, и save_path, который определяет путь, где будет сохранено загруженное изображение.

Вот как работает функция:

- Она начинает с выполнения GET-запроса к image_url с использованием метода requests.get. Это позволяет получить данные изображения с указанного URL.  
- Строка response.raise_for_status() проверяет успешность запроса. Если код состояния ответа указывает на ошибку (например, 404 - Не найдено), будет вызвано исключение. Это гарантирует, что процесс загрузки изображения продолжается только при успешном запросе.  
- Затем данные изображения передаются методу Image.open из модуля PIL (Python Imaging Library). Этот метод создает объект Image из данных изображения.  
- Строка image.save(save_path) сохраняет изображение по указанному пути save_path. Этот путь должен включать желаемое имя файла и расширение.  
- Наконец, функция возвращает True, указывая, что изображение было успешно загружено и сохранено. Если в процессе возникает исключение, оно перехватывается, выводится сообщение об ошибке, и функция возвращает False.  

Эта функция полезна для загрузки изображений по URL и их сохранения локально. Она обрабатывает возможные ошибки в процессе загрузки и предоставляет обратную связь о том, была ли загрузка успешной.

Стоит отметить, что библиотека requests используется для выполнения HTTP-запросов, библиотека PIL — для работы с изображениями, а класс BytesIO — для обработки данных изображения в виде потока байтов.

### Заключение

Этот скрипт предоставляет удобный способ подготовки набора данных для машинного обучения путем загрузки необходимых изображений, исключения строк с неудачной загрузкой и сохранения набора данных в формате CSV.

### Пример скрипта

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

### Пример загрузки кода
[Скрипт для создания нового набора данных](../../../../code/04.Finetuning/generate_dataset.py)

### Пример набора данных
[Пример набора данных из финетюнинга с использованием LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Отказ от ответственности**:  
Этот документ был переведен с использованием автоматизированных сервисов машинного перевода. Несмотря на наши усилия обеспечить точность, обратите внимание, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.