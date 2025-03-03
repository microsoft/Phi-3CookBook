# ہیوگنگ فیس سے ڈیٹاسیٹ اور متعلقہ تصاویر ڈاؤنلوڈ کرکے امیج ڈیٹاسیٹ تیار کریں

### جائزہ

یہ اسکرپٹ مشین لرننگ کے لیے ایک ڈیٹاسیٹ تیار کرتا ہے۔ اس میں مطلوبہ تصاویر ڈاؤنلوڈ کرنا، ان قطاروں کو فلٹر کرنا جہاں تصویر ڈاؤنلوڈ نہ ہو سکے، اور آخر میں ڈیٹاسیٹ کو CSV فائل کے طور پر محفوظ کرنا شامل ہے۔

### پیشگی ضروریات

اس اسکرپٹ کو چلانے سے پہلے درج ذیل لائبریریوں کو انسٹال کرنا یقینی بنائیں: `Pandas`, `Datasets`, `requests`, `PIL`, اور `io`۔ آپ کو لائن 2 میں `'Insert_Your_Dataset'` کو اپنے ہیوگنگ فیس ڈیٹاسیٹ کے نام سے بھی تبدیل کرنا ہوگا۔

ضروری لائبریریاں:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### فعالیت

یہ اسکرپٹ درج ذیل اقدامات انجام دیتا ہے:

1. `load_dataset()` فنکشن کے ذریعے ہیوگنگ فیس سے ڈیٹاسیٹ ڈاؤنلوڈ کرتا ہے۔
2. ڈیٹاسیٹ کو `to_pandas()` کے ذریعے ایک pandas DataFrame میں تبدیل کرتا ہے۔
3. `download_image()` فنکشن کا استعمال کرتے ہوئے تصاویر ڈاؤنلوڈ کرتا ہے۔
4. ان قطاروں کو فلٹر کرتا ہے جہاں تصاویر ڈاؤنلوڈ نہ ہو سکیں۔
5. صاف شدہ ڈیٹاسیٹ کو CSV فائل کے طور پر محفوظ کرتا ہے۔

### یہ کیسے کام کرتا ہے

`download_image` فنکشن دو پیرامیٹرز لیتا ہے: `image_url`، جو ڈاؤنلوڈ کی جانے والی تصویر کا URL ہے، اور `save_path`، جہاں تصویر کو محفوظ کیا جائے گا۔

یہ فنکشن درج ذیل طریقے سے کام کرتا ہے:

- سب سے پہلے، `requests.get` میتھڈ کے ذریعے `image_url` پر GET درخواست بھیجی جاتی ہے تاکہ URL سے تصویر کا ڈیٹا حاصل کیا جا سکے۔
- `response.raise_for_status()` لائن چیک کرتی ہے کہ آیا درخواست کامیاب رہی۔ اگر کوئی غلطی ہو (جیسے 404 - نہ ملا)، تو ایک استثناء پیدا کیا جاتا ہے۔ یہ یقینی بناتا ہے کہ ہم صرف کامیاب درخواستوں پر ہی آگے بڑھیں۔
- تصویر کا ڈیٹا پھر PIL (Python Imaging Library) کے `Image.open` میتھڈ کو دیا جاتا ہے، جو تصویر کا ایک آبجیکٹ بناتا ہے۔
- `image.save(save_path)` لائن تصویر کو مخصوص `save_path` پر محفوظ کرتی ہے، جہاں فائل کا نام اور ایکسٹینشن شامل ہونا چاہیے۔
- آخر میں، اگر تصویر کامیابی سے ڈاؤنلوڈ اور محفوظ ہو جائے تو فنکشن `True` واپس کرتا ہے۔ اگر کسی بھی مرحلے پر کوئی استثناء ہو، تو یہ استثناء کو پکڑتا ہے، ایک غلطی کا پیغام پرنٹ کرتا ہے، اور `False` واپس کرتا ہے۔

یہ فنکشن URLs سے تصاویر ڈاؤنلوڈ کرنے اور انہیں لوکل سسٹم پر محفوظ کرنے کے لیے کارآمد ہے۔ یہ ڈاؤنلوڈ کے عمل کے دوران ممکنہ غلطیوں کو سنبھالتا ہے اور ڈاؤنلوڈ کی کامیابی یا ناکامی کے بارے میں معلومات فراہم کرتا ہے۔

یہ بات قابل ذکر ہے کہ:
- `requests` لائبریری HTTP درخواستیں کرنے کے لیے استعمال ہوتی ہے۔
- PIL لائبریری تصاویر کے ساتھ کام کرنے کے لیے استعمال ہوتی ہے۔
- `BytesIO` کلاس تصویر کے ڈیٹا کو بائٹس کی اسٹریم کے طور پر ہینڈل کرنے کے لیے استعمال ہوتی ہے۔

### نتیجہ

یہ اسکرپٹ مشین لرننگ کے لیے ڈیٹاسیٹ تیار کرنے کا ایک آسان طریقہ فراہم کرتا ہے۔ اس میں مطلوبہ تصاویر ڈاؤنلوڈ کرنا، ناکام ڈاؤنلوڈز کو فلٹر کرنا، اور ڈیٹاسیٹ کو CSV فائل کے طور پر محفوظ کرنا شامل ہے۔

### نمونہ اسکرپٹ

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

### نمونہ کوڈ ڈاؤنلوڈ کریں
[نیا ڈیٹاسیٹ اسکرپٹ تیار کریں](../../../../code/04.Finetuning/generate_dataset.py)

### نمونہ ڈیٹاسیٹ
[نمونہ ڈیٹاسیٹ، فائن ٹوننگ کے LORA مثال سے](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**ڈسکلیمر**:  
یہ دستاویز مشین پر مبنی اے آئی ترجمہ خدمات کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز، جو اس کی اصل زبان میں ہے، کو مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمے کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔