# יצירת מאגר תמונות על ידי הורדת מאגר נתונים מ-Hugging Face והתמונות הקשורות אליו

### סקירה כללית

הסקריפט הזה מכין מאגר נתונים ללמידת מכונה על ידי הורדת תמונות נדרשות, סינון שורות שבהן הורדת התמונות נכשלה, ושמירת המאגר כקובץ CSV.

### דרישות מקדימות

לפני הרצת הסקריפט, ודא שיש לך את הספריות הבאות מותקנות: `Pandas`, `Datasets`, `requests`, `PIL` ו-`io`. בנוסף, תצטרך להחליף את `'Insert_Your_Dataset'` בשורה 2 בשם המאגר שלך מ-Hugging Face.

ספריות נדרשות:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### פונקציונליות

הסקריפט מבצע את השלבים הבאים:

1. מוריד את המאגר מ-Hugging Face באמצעות `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`.
2. מוריד את התמונות הקשורות לכל שורה במאגר הנתונים.
3. מסנן שורות שבהן הורדת התמונות נכשלה.
4. שומר את המאגר המעודכן כקובץ CSV.

### איך זה עובד

הפונקציה download_image מקבלת שני פרמטרים: image_url, שהוא ה-URL של התמונה שצריך להוריד, ו-save_path, שהוא הנתיב שבו התמונה תישמר.

כך הפונקציה פועלת:

1. מתחילה בביצוע בקשת GET ל-image_url באמצעות המתודה requests.get. פעולה זו משיגה את נתוני התמונה מה-URL.
2. השורה response.raise_for_status() בודקת אם הבקשה הצליחה. אם קוד הסטטוס של התגובה מצביע על שגיאה (לדוגמה, 404 - לא נמצא), היא תזרוק חריגה. פעולה זו מבטיחה שנמשיך להוריד את התמונה רק אם הבקשה הצליחה.
3. נתוני התמונה מועברים ל-Image.open מהמודול PIL (Python Imaging Library). מתודה זו יוצרת אובייקט תמונה מנתוני התמונה.
4. השורה image.save(save_path) שומרת את התמונה בנתיב שצוין. ה-save_path צריך לכלול את שם הקובץ והסיומת הרצויים.
5. לבסוף, הפונקציה מחזירה True כדי לציין שהתמונה הורדה ונשמרה בהצלחה. אם מתרחשת חריגה כלשהי במהלך התהליך, היא תופסת את החריגה, מדפיסה הודעת שגיאה שמציינת את הכישלון, ומחזירה False.

הפונקציה הזו שימושית להורדת תמונות מ-URLs ושמירתן באופן מקומי. היא מטפלת בשגיאות אפשריות בתהליך ההורדה ומספקת חיווי אם ההורדה הצליחה או לא.

חשוב לציין שספריית requests משמשת לביצוע בקשות HTTP, ספריית PIL משמשת לעבודה עם תמונות, והמחלקה BytesIO משמשת לטיפול בנתוני התמונה כזרם של בתים.

### סיכום

הסקריפט הזה מספק דרך נוחה להכין מאגר נתונים ללמידת מכונה על ידי הורדת תמונות נדרשות, סינון שורות שבהן הורדת התמונות נכשלה, ושמירת המאגר כקובץ CSV.

### סקריפט לדוגמה

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

### הורדת קוד לדוגמה 
[יצירת סקריפט למאגר נתונים חדש](../../../../code/04.Finetuning/generate_dataset.py)

### מאגר נתונים לדוגמה
[דוגמת מאגר נתונים מתוך דוגמת finetuning עם LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל טעויות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעות משימוש בתרגום זה.