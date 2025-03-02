# ایجاد مجموعه داده تصویری با دانلود مجموعه داده از Hugging Face و تصاویر مرتبط

### مرور کلی

این اسکریپت یک مجموعه داده برای یادگیری ماشین آماده می‌کند. این کار با دانلود تصاویر مورد نیاز، حذف ردیف‌هایی که دانلود تصاویرشان با شکست مواجه شده و ذخیره مجموعه داده به‌صورت فایل CSV انجام می‌شود.

### پیش‌نیازها

قبل از اجرای این اسکریپت، اطمینان حاصل کنید که کتابخانه‌های زیر نصب شده باشند: `Pandas`، `Datasets`، `requests`، `PIL` و `io`. همچنین، باید `'Insert_Your_Dataset'` در خط ۲ را با نام مجموعه داده خود از Hugging Face جایگزین کنید.

کتابخانه‌های مورد نیاز:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### عملکرد

این اسکریپت مراحل زیر را انجام می‌دهد:

1. مجموعه داده را از Hugging Face با استفاده از توابع `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` دانلود می‌کند.
2. تصاویر مربوطه را از طریق URL‌های موجود در مجموعه داده دانلود کرده و به‌صورت محلی ذخیره می‌کند.
3. ردیف‌هایی را که دانلود تصاویرشان ناموفق بوده است، فیلتر می‌کند.
4. مجموعه داده را به‌صورت فایل CSV ذخیره می‌کند.

تابع `download_image()` یک تصویر را از یک URL دانلود کرده و با استفاده از کتابخانه تصویری Pillow (PIL) و ماژول `io` به‌صورت محلی ذخیره می‌کند. این تابع در صورت موفقیت در دانلود تصویر مقدار True را برمی‌گرداند و در غیر این صورت مقدار False را بازمی‌گرداند. همچنین، در صورت بروز خطا، یک استثنا با پیام خطا ایجاد می‌کند.

### این چگونه کار می‌کند؟

تابع `download_image` دو پارامتر می‌گیرد: `image_url` که URL تصویر برای دانلود است و `save_path` که مسیری است که تصویر دانلود شده در آن ذخیره می‌شود.

مراحل کار این تابع به شرح زیر است:

1. ابتدا یک درخواست GET به `image_url` با استفاده از متد `requests.get` ارسال می‌کند. این کار داده‌های تصویر را از URL دریافت می‌کند.
2. خط `response.raise_for_status()` بررسی می‌کند که آیا درخواست موفقیت‌آمیز بوده است یا خیر. اگر کد وضعیت پاسخ نشان‌دهنده خطا باشد (مثلاً ۴۰۴ - یافت نشد)، یک استثنا ایجاد می‌کند. این تضمین می‌کند که تنها در صورت موفقیت درخواست، فرآیند دانلود تصویر ادامه یابد.
3. داده‌های تصویر سپس به متد `Image.open` از ماژول PIL (کتابخانه تصویری پایتون) ارسال می‌شود. این متد یک شیء Image از داده‌های تصویر ایجاد می‌کند.
4. خط `image.save(save_path)` تصویر را در مسیر مشخص‌شده ذخیره می‌کند. `save_path` باید شامل نام فایل و پسوند دلخواه باشد.
5. در نهایت، این تابع مقدار True را برای نشان دادن موفقیت‌آمیز بودن دانلود و ذخیره تصویر برمی‌گرداند. اگر در طول فرآیند هرگونه استثنایی رخ دهد، استثنا را دریافت کرده، پیام خطا را چاپ می‌کند و مقدار False را برمی‌گرداند.

این تابع برای دانلود تصاویر از URL‌ها و ذخیره محلی آن‌ها مفید است. همچنین، خطاهای احتمالی در طول فرآیند دانلود را مدیریت کرده و بازخوردی در مورد موفقیت یا شکست دانلود ارائه می‌دهد.

شایان ذکر است که کتابخانه `requests` برای ارسال درخواست‌های HTTP، کتابخانه PIL برای کار با تصاویر و کلاس `BytesIO` برای مدیریت داده‌های تصویر به‌عنوان یک جریان بایت استفاده می‌شود.

### نتیجه‌گیری

این اسکریپت راهی ساده برای آماده‌سازی یک مجموعه داده برای یادگیری ماشین فراهم می‌کند. این کار با دانلود تصاویر مورد نیاز، حذف ردیف‌هایی که دانلود تصاویرشان شکست خورده و ذخیره مجموعه داده به‌صورت فایل CSV انجام می‌شود.

### نمونه اسکریپت

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

### دانلود کد نمونه 
[ایجاد اسکریپت مجموعه داده جدید](../../../../code/04.Finetuning/generate_dataset.py)

### نمونه مجموعه داده
[نمونه مجموعه داده از مثال تنظیم دقیق با LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادقتی‌هایی باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا برداشت‌های نادرست ناشی از استفاده از این ترجمه نداریم.