# হাগিং ফেস থেকে ডেটাসেট এবং সংশ্লিষ্ট ইমেজ ডাউনলোড করে ইমেজ ডেটাসেট তৈরি করুন

### ওভারভিউ

এই স্ক্রিপ্টটি মেশিন লার্নিংয়ের জন্য একটি ডেটাসেট প্রস্তুত করে, যেখানে প্রয়োজনীয় ইমেজ ডাউনলোড করা হয়, যেসব সারির ইমেজ ডাউনলোড ব্যর্থ হয় সেগুলো ফিল্টার করা হয় এবং শেষে ডেটাসেটটি একটি CSV ফাইল হিসেবে সংরক্ষণ করা হয়।

### প্রয়োজনীয় শর্তাবলী

এই স্ক্রিপ্ট চালানোর আগে নিশ্চিত করুন যে নিম্নলিখিত লাইব্রেরিগুলো ইনস্টল করা আছে: `Pandas`, `Datasets`, `requests`, `PIL`, এবং `io`। এছাড়াও, লাইনের `'Insert_Your_Dataset'`-এ আপনার হাগিং ফেস ডেটাসেটের নাম প্রতিস্থাপন করতে হবে।

প্রয়োজনীয় লাইব্রেরি:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### কার্যকারিতা

স্ক্রিপ্টটি নিচের ধাপগুলো সম্পন্ন করে:

1. হাগিং ফেস থেকে ডেটাসেট ডাউনলোড করে `load_dataset()` ব্যবহার করে। 
2. ` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `-এর মাধ্যমে ডেটাসেটকে প্যান্ডাস ডেটাফ্রেমে রূপান্তর করে। 
3. ` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom ` ব্যবহার করে ইমেজ ডাউনলোড করে। 
4. ` function, and appending the filtered row to a new DataFrame called ` এবং `.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The ` ব্যবহার করে যেসব সারিতে ইমেজ ডাউনলোড ব্যর্থ হয় সেগুলো ফিল্টার করে। 
5. সফলভাবে ডাউনলোড হওয়া ডেটাসেটটি CSV ফাইল হিসেবে সংরক্ষণ করে। 

` function, and appending the filtered row to a new DataFrame called ` ফাংশনটি একটি URL থেকে ইমেজ ডাউনলোড করে এবং এটি স্থানীয়ভাবে সংরক্ষণ করে Pillow Image Library (PIL) এবং `io` মডিউল ব্যবহার করে। যদি ইমেজ সফলভাবে ডাউনলোড হয় তবে এটি True রিটার্ন করে, অন্যথায় False রিটার্ন করে। রিকোয়েস্ট ব্যর্থ হলে এটি একটি এক্সেপশন তুলে ধরে এবং ত্রুটির বার্তা প্রদান করে।

### এটি কীভাবে কাজ করে

`download_image` ফাংশনটি দুটি প্যারামিটার গ্রহণ করে: `image_url`, যা ডাউনলোড করার ইমেজের URL, এবং `save_path`, যেখানে ডাউনলোড করা ইমেজটি সংরক্ষণ করা হবে।

ফাংশনটি যেভাবে কাজ করে:

1. এটি `requests.get` মেথড ব্যবহার করে `image_url`-এ একটি GET রিকোয়েস্ট করে। এর মাধ্যমে URL থেকে ইমেজ ডেটা রিট্রিভ করা হয়।  
2. `response.raise_for_status()` লাইনটি চেক করে রিকোয়েস্ট সফল হয়েছে কিনা। যদি রেসপন্স স্ট্যাটাস কোডে কোনো ত্রুটি থাকে (যেমন 404 - Not Found), এটি একটি এক্সেপশন তুলে ধরে। এটি নিশ্চিত করে যে রিকোয়েস্ট সফল হলে তবেই ইমেজ ডাউনলোডের প্রক্রিয়া শুরু হবে।  
3. এরপর ইমেজ ডেটা `PIL` মডিউলের `Image.open` মেথডে পাঠানো হয়। এটি ইমেজ ডেটা থেকে একটি ইমেজ অবজেক্ট তৈরি করে।  
4. `image.save(save_path)` লাইনটি ইমেজটিকে নির্দিষ্ট `save_path`-এ সংরক্ষণ করে। `save_path`-এ কাঙ্ক্ষিত ফাইলের নাম এবং এক্সটেনশন অন্তর্ভুক্ত থাকতে হবে।  
5. শেষ পর্যন্ত, ফাংশনটি True রিটার্ন করে যদি ইমেজ সফলভাবে ডাউনলোড এবং সংরক্ষণ হয়। যদি কোনো এক্সেপশন ঘটে, এটি এক্সেপশন ক্যাচ করে, একটি ত্রুটির বার্তা প্রিন্ট করে এবং False রিটার্ন করে।  

এই ফাংশনটি URL থেকে ইমেজ ডাউনলোড করে স্থানীয়ভাবে সংরক্ষণ করার জন্য কার্যকর। এটি ডাউনলোড প্রক্রিয়ার সময় সম্ভাব্য ত্রুটিগুলি পরিচালনা করে এবং ডাউনলোড সফল হয়েছে কিনা সে বিষয়ে ফিডব্যাক দেয়। 

উল্লেখযোগ্য যে, HTTP রিকোয়েস্টের জন্য `requests` লাইব্রেরি ব্যবহার করা হয়, ইমেজের জন্য `PIL` লাইব্রেরি ব্যবহার করা হয়, এবং ইমেজ ডেটাকে বাইট স্ট্রিম হিসেবে হ্যান্ডেল করার জন্য `BytesIO` ক্লাস ব্যবহার করা হয়।

### উপসংহার

এই স্ক্রিপ্টটি মেশিন লার্নিংয়ের জন্য ডেটাসেট প্রস্তুত করার একটি সহজ উপায় প্রদান করে। এটি প্রয়োজনীয় ইমেজ ডাউনলোড করে, ব্যর্থ সারিগুলো ফিল্টার করে এবং ডেটাসেটটিকে একটি CSV ফাইল হিসেবে সংরক্ষণ করে।

### নমুনা স্ক্রিপ্ট

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

### নমুনা কোড ডাউনলোড
[নতুন ডেটাসেট স্ক্রিপ্ট তৈরি করুন](../../../../code/04.Finetuning/generate_dataset.py)

### নমুনা ডেটাসেট
[ফাইনটিউনিং উইথ লোরা উদাহরণের নমুনা ডেটাসেট](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**অস্বীকৃতি**:  
এই নথিটি মেশিন-ভিত্তিক এআই অনুবাদ পরিষেবা ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিক অনুবাদের চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ভাষায় লেখা আসল নথিটিকে প্রামাণিক উৎস হিসাবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই। 