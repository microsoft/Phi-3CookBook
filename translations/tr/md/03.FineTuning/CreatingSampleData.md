# Hugging Face'ten Veri Seti ve İlgili Görselleri İndirerek Görsel Veri Seti Oluşturma

### Genel Bakış

Bu betik, makine öğrenimi için bir veri seti hazırlamak amacıyla gerekli görselleri indirir, görsel indirme işleminin başarısız olduğu satırları filtreler ve veri setini bir CSV dosyası olarak kaydeder.

### Gereksinimler

Bu betiği çalıştırmadan önce aşağıdaki kütüphanelerin kurulu olduğundan emin olun: `Pandas`, `Datasets`, `requests`, `PIL` ve `io`. Ayrıca, 2. satırda yer alan `'Insert_Your_Dataset'`'i Hugging Face'ten indirmek istediğiniz veri setinin adıyla değiştirmeniz gerekmektedir.

Gerekli Kütüphaneler:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### İşlevsellik

Betik şu adımları gerçekleştirir:

1. Hugging Face'ten `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` fonksiyonlarını kullanarak veri setini indirir.
2. Görselleri verilen URL'lerden indirir ve yerel olarak kaydeder.
3. Görsel indirme işlemi başarısız olan satırları filtreler.
4. Filtrelenmiş veri setini bir CSV dosyası olarak kaydeder.

### Nasıl Çalışır?

`download_image` fonksiyonu iki parametre alır: `image_url` (indirilecek görselin URL'si) ve `save_path` (indirilen görselin kaydedileceği yol).

Fonksiyon şu şekilde çalışır:

1. `requests.get` yöntemiyle `image_url`'e bir GET isteği yapar. Bu işlem, URL'den görsel verisini alır.
2. `response.raise_for_status()` satırı, isteğin başarılı olup olmadığını kontrol eder. Eğer yanıt durumu bir hata içeriyorsa (örneğin, 404 - Bulunamadı), bir istisna oluşturur. Bu, yalnızca isteğin başarılı olduğu durumlarda indirme işlemine devam edilmesini sağlar.
3. Görsel verisi, PIL (Python Imaging Library) modülünden `Image.open` yöntemi ile bir Görsel Nesnesi (`Image object`) olarak oluşturulur.
4. `image.save(save_path)` satırı, görseli belirtilen `save_path` konumuna kaydeder. `save_path`, istenen dosya adı ve uzantısını içermelidir.
5. Son olarak, fonksiyon görselin başarıyla indirildiğini ve kaydedildiğini belirtmek için `True` döner. Eğer işlem sırasında bir istisna oluşursa, bu istisna yakalanır, bir hata mesajı yazdırılır ve `False` döner.

Bu fonksiyon, URL'lerden görseller indirip yerel olarak kaydetmek için kullanışlıdır. İndirme sürecindeki potansiyel hataları ele alır ve indirme işleminin başarılı olup olmadığını geri bildirir.

Dikkat edilmesi gereken nokta, HTTP istekleri için `requests` kütüphanesinin kullanıldığı, görsellerle çalışmak için PIL kütüphanesinin kullanıldığı ve görsel verisinin bayt akışı olarak işlenmesi için `BytesIO` sınıfının kullanıldığıdır.

### Sonuç

Bu betik, gerekli görselleri indirerek, başarısız indirme işlemlerini filtreleyerek ve veri setini bir CSV dosyası olarak kaydederek makine öğrenimi için bir veri seti hazırlamanın kolay bir yolunu sunar.

### Örnek Betik

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

### Örnek Kod İndirme 
[Yeni Veri Seti Betiği Oluştur](../../../../code/04.Finetuning/generate_dataset.py)

### Örnek Veri Seti
[Finetuning ile LORA örneğinden örnek veri seti](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi ana dilindeki versiyonu yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.