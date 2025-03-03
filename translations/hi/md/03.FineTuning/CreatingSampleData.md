# हगिंग फेस से डेटा सेट और संबंधित छवियों को डाउनलोड करके इमेज डेटा सेट तैयार करें

### अवलोकन

यह स्क्रिप्ट मशीन लर्निंग के लिए एक डेटा सेट तैयार करती है। इसमें आवश्यक छवियों को डाउनलोड करना, उन पंक्तियों को फ़िल्टर करना जहां छवि डाउनलोड विफल हो जाती है, और डेटा सेट को CSV फ़ाइल के रूप में सहेजना शामिल है।

### पूर्वापेक्षाएँ

इस स्क्रिप्ट को चलाने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित लाइब्रेरीज़ इंस्टॉल हैं: `Pandas`, `Datasets`, `requests`, `PIL`, और `io`। आपको लाइन 2 में `'Insert_Your_Dataset'` को अपने हगिंग फेस डेटा सेट के नाम से बदलने की भी आवश्यकता होगी।

आवश्यक लाइब्रेरीज़:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### कार्यक्षमता

स्क्रिप्ट निम्नलिखित चरणों को पूरा करती है:

1. `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` फ़ंक्शन का उपयोग करके हगिंग फेस से डेटा सेट डाउनलोड करती है।
2. छवियों को डाउनलोड करने का प्रयास करती है और असफल डाउनलोड वाली पंक्तियों को हटा देती है।
3. अंतिम डेटा सेट को CSV फ़ाइल के रूप में सहेजती है।

` function, and appending the filtered row to a new DataFrame called ` फ़ंक्शन एक URL से छवि डाउनलोड करता है और इसे लोकल रूप से Pillow इमेज लाइब्रेरी (PIL) और `io` मॉड्यूल का उपयोग करके सहेजता है। यह True लौटाता है यदि छवि सफलतापूर्वक डाउनलोड हो जाती है, अन्यथा False। यदि अनुरोध विफल होता है, तो यह एक अपवाद उठाता है और त्रुटि संदेश प्रदर्शित करता है।

### यह कैसे काम करता है

`download_image` फ़ंक्शन दो पैरामीटर लेता है: `image_url`, जो डाउनलोड की जाने वाली छवि का URL है, और `save_path`, जो वह पथ है जहां डाउनलोड की गई छवि को सहेजा जाएगा।

यहाँ यह फ़ंक्शन कैसे काम करता है:

1. यह `requests.get` मेथड का उपयोग करके `image_url` पर एक GET अनुरोध करता है। यह URL से छवि डेटा प्राप्त करता है।
2. `response.raise_for_status()` यह जांचता है कि अनुरोध सफल था या नहीं। यदि प्रतिक्रिया स्थिति कोड किसी त्रुटि (जैसे, 404 - नॉट फाउंड) को इंगित करता है, तो यह एक अपवाद उठाता है। यह सुनिश्चित करता है कि हम केवल सफल अनुरोधों के साथ आगे बढ़ें।
3. छवि डेटा को PIL (Python Imaging Library) मॉड्यूल से `Image.open` मेथड में पास किया जाता है। यह मेथड छवि डेटा से एक Image ऑब्जेक्ट बनाता है।
4. `image.save(save_path)` पंक्ति छवि को निर्दिष्ट `save_path` पर सहेजती है। `save_path` में इच्छित फ़ाइल नाम और एक्सटेंशन शामिल होना चाहिए।
5. अंत में, फ़ंक्शन True लौटाता है, यह इंगित करने के लिए कि छवि सफलतापूर्वक डाउनलोड और सहेजी गई थी। यदि प्रक्रिया के दौरान कोई अपवाद होता है, तो यह अपवाद को पकड़ता है, विफलता का संकेत देने वाला एक त्रुटि संदेश प्रिंट करता है, और False लौटाता है।

यह फ़ंक्शन URL से छवियों को डाउनलोड करने और उन्हें लोकल रूप से सहेजने के लिए उपयोगी है। यह डाउनलोड प्रक्रिया के दौरान संभावित त्रुटियों को संभालता है और यह फीडबैक देता है कि डाउनलोड सफल रहा या नहीं।

यह ध्यान देने योग्य है कि HTTP अनुरोध करने के लिए `requests` लाइब्रेरी का उपयोग किया जाता है, छवियों के साथ काम करने के लिए `PIL` लाइब्रेरी का उपयोग किया जाता है, और `BytesIO` क्लास का उपयोग छवि डेटा को बाइट्स की स्ट्रीम के रूप में संभालने के लिए किया जाता है।

### निष्कर्ष

यह स्क्रिप्ट मशीन लर्निंग के लिए एक डेटा सेट तैयार करने का एक सुविधाजनक तरीका प्रदान करती है। यह आवश्यक छवियों को डाउनलोड करती है, असफल डाउनलोड वाली पंक्तियों को फ़िल्टर करती है, और डेटा सेट को CSV फ़ाइल के रूप में सहेजती है।

### नमूना स्क्रिप्ट

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

### नमूना कोड डाउनलोड करें
[नया डेटा सेट स्क्रिप्ट जनरेट करें](../../../../code/04.Finetuning/generate_dataset.py)

### नमूना डेटा सेट
[फाइन-ट्यूनिंग के साथ LORA के उदाहरण से नमूना डेटा सेट](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**अस्वीकरण**:  
यह दस्तावेज़ मशीन-आधारित एआई अनुवाद सेवाओं का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़, जो इसकी मूल भाषा में है, को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।