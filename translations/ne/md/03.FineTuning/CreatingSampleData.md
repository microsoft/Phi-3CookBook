# हगिंग फेसबाट डाटासेट र सम्बद्ध छविहरू डाउनलोड गरेर इमेज डाटासेट तयार गर्नुहोस्

### अवलोकन

यो स्क्रिप्टले मेसिन लर्निङको लागि आवश्यक छविहरू डाउनलोड गरेर, छवि डाउनलोड असफल हुने पङ्क्तिहरू हटाएर, र डाटासेटलाई CSV फाइलको रूपमा सुरक्षित गरेर डाटासेट तयार गर्दछ।

### आवश्यक तयारीहरू

यो स्क्रिप्ट चलाउनुअघि, तलका पुस्तकालयहरू स्थापना भएको सुनिश्चित गर्नुहोस्: `Pandas`, `Datasets`, `requests`, `PIL`, र `io`। साथै, लाइन २ मा रहेको `'Insert_Your_Dataset'` लाई हगिंग फेसबाट आफ्नो डाटासेटको नामले प्रतिस्थापन गर्नुहोस्।

आवश्यक पुस्तकालयहरू:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### कार्यक्षमता

यो स्क्रिप्टले तलका चरणहरू पूरा गर्छ:

1. हगिंग फेसबाट `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` प्रयोग गरेर डाटासेट डाउनलोड गर्दछ। 
2. छवि डाउनलोड असफल भएका पङ्क्तिहरू फिल्टर गर्दछ। 
3. अन्ततः, परिणामी डाटासेटलाई CSV फाइलको रूपमा सुरक्षित गर्दछ।

### यो कसरी काम गर्छ

`download_image` नामक फङ्क्शनले दुई पैरामीटर लिन्छ: `image_url`, जुन डाउनलोड गर्नुपर्ने छविको URL हो, र `save_path`, जुन डाउनलोड गरिएको छवि सुरक्षित गरिने स्थान हो।

यो फङ्क्शन यसरी काम गर्छ:

- सुरुमा, `requests.get` विधि प्रयोग गरेर `image_url` मा GET अनुरोध गर्छ। यसले URL बाट छविको डाटा प्राप्त गर्छ।
- `response.raise_for_status()` ले अनुरोध सफल भएको छ कि छैन भनेर जाँच्छ। यदि प्रतिक्रिया स्टेटस कोडले त्रुटि जनाउँछ (जस्तै, 404 - भेटिएन), यसले अपवाद फ्याँक्छ। यसले सुनिश्चित गर्छ कि अनुरोध सफल भए मात्र छवि डाउनलोड प्रक्रिया अघि बढ्छ।
- त्यसपछि, छवि डाटालाई PIL (Python Imaging Library) को `Image.open` विधिमा पठाइन्छ। यसले छवि डाटाबाट Image वस्तु सिर्जना गर्छ।
- `image.save(save_path)` ले निर्दिष्ट गरिएको `save_path` मा छविलाई सुरक्षित गर्छ। `save_path` मा फाइलको नाम र एक्स्टेन्सन समावेश हुनु पर्छ।
- अन्ततः, यो फङ्क्शनले छवि सफलतापूर्वक डाउनलोड र सुरक्षित भएको संकेत गर्न `True` फिर्ता गर्छ। यदि प्रक्रिया दौरान कुनै अपवाद आउँछ भने, यो अपवाद समात्छ, असफलताको सन्देश प्रिन्ट गर्छ, र `False` फिर्ता गर्छ।

यो फङ्क्शन URL बाट छविहरू डाउनलोड गर्न र तिनलाई स्थानीय रूपमा सुरक्षित गर्न उपयोगी छ। यो डाउनलोड प्रक्रियामा सम्भावित त्रुटिहरू ह्यान्डल गर्छ र डाउनलोड सफल भयो कि भएन भन्ने जानकारी दिन्छ।

विशेष रूपमा, HTTP अनुरोध गर्न `requests` पुस्तकालय प्रयोग गरिएको छ, छविहरूसँग काम गर्न `PIL` पुस्तकालय प्रयोग गरिएको छ, र छवि डाटालाई बाइटको स्ट्रिमको रूपमा ह्यान्डल गर्न `BytesIO` वर्ग प्रयोग गरिएको छ।

### निष्कर्ष

यो स्क्रिप्टले आवश्यक छविहरू डाउनलोड गरेर, छवि डाउनलोड असफल भएका पङ्क्तिहरू हटाएर, र डाटासेटलाई CSV फाइलको रूपमा सुरक्षित गरेर मेसिन लर्निङको लागि डाटासेट तयार गर्न सजिलो तरिका प्रदान गर्छ।

### नमुना स्क्रिप्ट

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

### नमुना कोड डाउनलोड
[नयाँ डाटासेट स्क्रिप्ट तयार गर्नुहोस्](../../../../code/04.Finetuning/generate_dataset.py)

### नमुना डाटासेट
[फाइनट्युनिङको लागि LORA उदाहरणबाट नमुना डाटासेट](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**अस्वीकरण**:  
यो कागजात मेसिन-आधारित एआई अनुवाद सेवाहरू प्रयोग गरेर अनुवाद गरिएको हो। हामी यथासम्भव सही अनुवाद प्रदान गर्न प्रयास गर्दछौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटि वा अशुद्धता हुन सक्छ। यसको मूल भाषामा रहेको कागजातलाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।