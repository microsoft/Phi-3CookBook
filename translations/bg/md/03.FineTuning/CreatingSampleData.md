# Генериране на набор от изображения чрез изтегляне на DataSet от Hugging Face и свързаните с него изображения

### Преглед

Този скрипт подготвя набор от данни за машинно обучение, като изтегля необходимите изображения, филтрира редовете, където изтеглянето на изображения се проваля, и запазва набора от данни като CSV файл.

### Предварителни изисквания

Преди да стартирате този скрипт, уверете се, че сте инсталирали следните библиотеки: `Pandas`, `Datasets`, `requests`, `PIL` и `io`. Също така трябва да замените `'Insert_Your_Dataset'` на ред 2 с името на вашия набор от данни от Hugging Face.

Необходими библиотеки:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Функционалност

Скриптът изпълнява следните стъпки:

1. Изтегля набора от данни от Hugging Face, използвайки функциите `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`.  
2. Филтрира редовете, където изтеглянето на изображения се проваля.  
3. Запазва актуализирания набор от данни като CSV файл.

### Как работи

Функцията download_image приема два параметъра: image_url, който е URL адресът на изображението, което трябва да бъде изтеглено, и save_path, който е пътят, където изтегленото изображение ще бъде запазено.

Ето как работи функцията:

- Тя започва, като прави GET заявка към image_url с помощта на метода requests.get. Това извлича данните за изображението от URL адреса.

- Линията response.raise_for_status() проверява дали заявката е успешна. Ако статус кодът на отговора показва грешка (например 404 - Не е намерено), ще бъде хвърлено изключение. Това гарантира, че продължаваме с изтеглянето на изображението само ако заявката е успешна.

- Данните за изображението след това се предават на метода Image.open от модула PIL (Python Imaging Library). Този метод създава обект Image от данните за изображението.

- Линията image.save(save_path) запазва изображението на посочения save_path. Save_path трябва да включва желаното име на файла и разширението.

- Накрая функцията връща True, за да покаже, че изображението е успешно изтеглено и запазено. Ако възникне някакво изключение по време на процеса, то прихваща изключението, отпечатва съобщение за грешка, което показва неуспеха, и връща False.

Тази функция е полезна за изтегляне на изображения от URL адреси и тяхното локално запазване. Тя обработва потенциални грешки по време на процеса на изтегляне и предоставя обратна връзка дали изтеглянето е успешно или не.

Заслужава да се отбележи, че библиотеката requests се използва за извършване на HTTP заявки, библиотеката PIL се използва за работа с изображения, а класът BytesIO се използва за обработка на данните за изображението като поток от байтове.

### Заключение

Този скрипт предоставя удобен начин за подготовка на набор от данни за машинно обучение, като изтегля необходимите изображения, филтрира редовете, където изтеглянето на изображения се проваля, и запазва набора от данни като CSV файл.

### Примерен скрипт

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

### Изтегляне на примерен код 
[Скрипт за генериране на нов набор от данни](../../../../code/04.Finetuning/generate_dataset.py)

### Примерен набор от данни
[Примерен набор от данни от фино настройване с пример LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Отказ от отговорност**:  
Този документ е преведен с помощта на автоматизирани AI услуги за превод. Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия изходен език трябва да се счита за авторитетния източник. За критична информация се препоръчва професионален превод от човек. Ние не носим отговорност за каквито и да е недоразумения или погрешни тълкувания, произтичащи от използването на този превод.