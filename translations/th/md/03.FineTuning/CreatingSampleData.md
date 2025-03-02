# สร้างชุดข้อมูลภาพโดยการดาวน์โหลดชุดข้อมูลจาก Hugging Face และรูปภาพที่เกี่ยวข้อง

### ภาพรวม

สคริปต์นี้เตรียมชุดข้อมูลสำหรับการเรียนรู้ของเครื่องโดยการดาวน์โหลดรูปภาพที่จำเป็น กรองแถวที่ไม่สามารถดาวน์โหลดรูปภาพได้ และบันทึกชุดข้อมูลในรูปแบบไฟล์ CSV

### ข้อกำหนดเบื้องต้น

ก่อนที่จะรันสคริปต์นี้ ให้ตรวจสอบว่าคุณได้ติดตั้งไลบรารีดังต่อไปนี้แล้ว: `Pandas`, `Datasets`, `requests`, `PIL` และ `io` นอกจากนี้ คุณยังต้องเปลี่ยน `'Insert_Your_Dataset'` ในบรรทัดที่ 2 ให้เป็นชื่อชุดข้อมูลของคุณจาก Hugging Face

ไลบรารีที่จำเป็น:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### ฟังก์ชันการทำงาน

สคริปต์นี้ทำงานตามขั้นตอนดังต่อไปนี้:

1. ดาวน์โหลดชุดข้อมูลจาก Hugging Face โดยใช้ฟังก์ชัน `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` ฟังก์ชันนี้จะดาวน์โหลดรูปภาพจาก URL และบันทึกไว้ในเครื่องโดยใช้ไลบรารี Pillow Image Library (PIL) และโมดูล `io` ฟังก์ชันจะคืนค่าเป็น True หากดาวน์โหลดรูปภาพสำเร็จ และคืนค่าเป็น False หากไม่สำเร็จ นอกจากนี้ ฟังก์ชันยังสามารถแจ้งข้อผิดพลาดในกรณีที่การร้องขอล้มเหลว

### วิธีการทำงาน

ฟังก์ชัน download_image รับพารามิเตอร์สองตัว: image_url ซึ่งเป็น URL ของรูปภาพที่จะดาวน์โหลด และ save_path ซึ่งเป็นเส้นทางที่รูปภาพที่ดาวน์โหลดจะถูกบันทึก

นี่คือวิธีการทำงานของฟังก์ชัน:

1. เริ่มต้นด้วยการทำคำร้องขอ GET ไปยัง image_url โดยใช้เมธอด requests.get เพื่อดึงข้อมูลรูปภาพจาก URL
2. บรรทัด response.raise_for_status() จะตรวจสอบว่าคำร้องขอสำเร็จหรือไม่ หากสถานะของคำร้องขอแสดงข้อผิดพลาด (เช่น 404 - ไม่พบ) จะมีการแจ้งข้อยกเว้น ซึ่งช่วยให้มั่นใจว่าเราจะดำเนินการดาวน์โหลดรูปภาพต่อเมื่อคำร้องขอสำเร็จเท่านั้น
3. ข้อมูลรูปภาพจะถูกส่งไปยังเมธอด Image.open จากโมดูล PIL (Python Imaging Library) เพื่อสร้างวัตถุภาพ (Image object) จากข้อมูลรูปภาพ
4. บรรทัด image.save(save_path) จะบันทึกรูปภาพไปยัง save_path ที่ระบุ ซึ่งควรประกอบด้วยชื่อไฟล์และนามสกุลไฟล์ที่ต้องการ
5. สุดท้าย ฟังก์ชันจะคืนค่า True เพื่อแสดงว่าดาวน์โหลดและบันทึกรูปภาพสำเร็จ หากเกิดข้อยกเว้นใด ๆ ในระหว่างกระบวนการ ฟังก์ชันจะจับข้อยกเว้นนั้น แสดงข้อความข้อผิดพลาด และคืนค่า False

ฟังก์ชันนี้มีประโยชน์สำหรับการดาวน์โหลดรูปภาพจาก URL และบันทึกไว้ในเครื่อง โดยสามารถจัดการข้อผิดพลาดที่อาจเกิดขึ้นระหว่างกระบวนการดาวน์โหลด และให้ข้อมูลว่าการดาวน์โหลดสำเร็จหรือไม่

ควรทราบว่าไลบรารี requests ถูกใช้สำหรับการทำคำร้องขอ HTTP ไลบรารี PIL ถูกใช้สำหรับการจัดการรูปภาพ และคลาส BytesIO ถูกใช้สำหรับจัดการข้อมูลรูปภาพในรูปแบบสตรีมของไบต์

### สรุป

สคริปต์นี้เป็นวิธีที่สะดวกในการเตรียมชุดข้อมูลสำหรับการเรียนรู้ของเครื่องโดยการดาวน์โหลดรูปภาพที่จำเป็น กรองแถวที่ไม่สามารถดาวน์โหลดรูปภาพได้ และบันทึกชุดข้อมูลในรูปแบบไฟล์ CSV

### ตัวอย่างสคริปต์

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

### ดาวน์โหลดโค้ดตัวอย่าง 
[สร้างสคริปต์ชุดข้อมูลใหม่](../../../../code/04.Finetuning/generate_dataset.py)

### ตัวอย่างชุดข้อมูล
[ตัวอย่างชุดข้อมูลจากการปรับแต่งด้วย LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**คำปฏิเสธความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาโดยปัญญาประดิษฐ์ แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญที่เป็นมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่อาจเกิดขึ้นจากการใช้การแปลนี้