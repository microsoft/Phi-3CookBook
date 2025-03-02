# إنشاء مجموعة بيانات الصور عن طريق تنزيل مجموعة البيانات من Hugging Face والصور المرتبطة بها

### نظرة عامة

يعمل هذا السكربت على إعداد مجموعة بيانات لتعلم الآلة من خلال تنزيل الصور المطلوبة، واستبعاد الصفوف التي تفشل فيها عملية تنزيل الصور، وحفظ مجموعة البيانات كملف CSV.

### المتطلبات الأساسية

قبل تشغيل هذا السكربت، تأكد من تثبيت المكتبات التالية: `Pandas`، `Datasets`، `requests`، `PIL`، و`io`. ستحتاج أيضًا إلى استبدال `'Insert_Your_Dataset'` في السطر الثاني باسم مجموعة البيانات الخاصة بك من Hugging Face.

المكتبات المطلوبة:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### الوظائف

يقوم السكربت بالخطوات التالية:

1. تنزيل مجموعة البيانات من Hugging Face باستخدام `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`.
2. تصفية الصفوف التي فشلت فيها عملية تنزيل الصور.
3. حفظ مجموعة البيانات المعدلة في ملف CSV.

### كيفية عمل ذلك

تقوم دالة download_image بأخذ متغيرين: image_url، وهو رابط الصورة التي سيتم تنزيلها، وsave_path، وهو المسار الذي سيتم حفظ الصورة فيه.

إليك كيفية عمل الدالة:

- تبدأ بإجراء طلب GET إلى image_url باستخدام الطريقة requests.get. يسترجع هذا الطلب بيانات الصورة من الرابط.
- يتحقق السطر response.raise_for_status() مما إذا كان الطلب ناجحًا. إذا كان رمز حالة الاستجابة يشير إلى خطأ (مثل 404 - غير موجود)، فإنه يثير استثناءً. يضمن ذلك المتابعة فقط إذا كان الطلب ناجحًا.
- يتم تمرير بيانات الصورة إلى الطريقة Image.open من مكتبة PIL (Python Imaging Library). تقوم هذه الطريقة بإنشاء كائن صورة من بيانات الصورة.
- السطر image.save(save_path) يحفظ الصورة في المسار المحدد save_path. يجب أن يتضمن save_path اسم الملف المطلوب وامتداده.
- أخيرًا، تعيد الدالة True للإشارة إلى أن الصورة تم تنزيلها وحفظها بنجاح. إذا حدث أي استثناء أثناء العملية، فإنه يتم التقاطه وطباعة رسالة خطأ تشير إلى الفشل، ثم تعيد الدالة False.

تعد هذه الدالة مفيدة لتنزيل الصور من الروابط وحفظها محليًا. كما أنها تتعامل مع الأخطاء المحتملة أثناء عملية التنزيل وتوفر ملاحظات حول نجاح العملية أو فشلها.

من الجدير بالذكر أن مكتبة requests تُستخدم لإجراء طلبات HTTP، ومكتبة PIL تُستخدم للعمل مع الصور، وفئة BytesIO تُستخدم للتعامل مع بيانات الصور كتيار من البايتات.

### الخاتمة

يوفر هذا السكربت طريقة مريحة لإعداد مجموعة بيانات لتعلم الآلة من خلال تنزيل الصور المطلوبة، وتصفيتها، وحفظها كملف CSV.

### سكربت تجريبي

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

### تنزيل الكود التجريبي
[إنشاء سكربت لمجموعة بيانات جديدة](../../../../code/04.Finetuning/generate_dataset.py)

### مثال لمجموعة بيانات
[مثال على مجموعة بيانات من تجربة Fine-tuning باستخدام LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمات الترجمة الآلية المدعومة بالذكاء الاصطناعي. بينما نسعى جاهدين لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. بالنسبة للمعلومات الحرجة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.