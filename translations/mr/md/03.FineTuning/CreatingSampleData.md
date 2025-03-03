# हगिंग फेसवरून डेटासेट आणि संबंधित प्रतिमा डाउनलोड करून इमेज डेटासेट तयार करा

### आढावा

हा स्क्रिप्ट मशीन लर्निंगसाठी डेटासेट तयार करतो. यामध्ये आवश्यक प्रतिमा डाउनलोड करणे, ज्या ठिकाणी प्रतिमा डाउनलोड अपयशी ठरतात त्या पंक्ती फिल्टर करणे आणि डेटासेट CSV फाइल म्हणून सेव्ह करणे यांचा समावेश आहे.

### पूर्वतयारी

हा स्क्रिप्ट चालवण्यापूर्वी, खालील लायब्ररी तुमच्या सिस्टमवर इन्स्टॉल केलेल्या असाव्यात: `Pandas`, `Datasets`, `requests`, `PIL`, आणि `io`. तसेच, दुसऱ्या ओळीतल्या `'Insert_Your_Dataset'` जागी तुमच्या हगिंग फेस डेटासेटचे नाव द्यावे.

आवश्यक लायब्ररी:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### कार्यप्रणाली

हा स्क्रिप्ट खालील स्टेप्स पार पाडतो:

1. `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` फंक्शनचा वापर करून हगिंग फेसवरून डेटासेट डाउनलोड करतो. 

2. फंक्शन `download_image()` URL वरून प्रतिमा डाउनलोड करून ती स्थानिक पातळीवर सेव्ह करते. यासाठी Pillow Image Library (PIL) आणि `io` मॉड्यूलचा वापर केला जातो. प्रतिमा यशस्वीरीत्या डाउनलोड झाल्यास फंक्शन True परत करते; अन्यथा False परत करते. विनंती अपयशी झाल्यास फंक्शन अपवाद (exception) उचलते आणि त्रुटी संदेश दर्शवते.

### हे कसे कार्य करते

`download_image` फंक्शन दोन पॅरामीटर्स घेतं: `image_url` (डाउनलोड करावयाच्या प्रतिमेचा URL) आणि `save_path` (डाउनलोड केलेली प्रतिमा ज्या ठिकाणी सेव्ह होईल ती जागा).

फंक्शनचे कार्यप्रणाली:

1. `requests.get` मेथडचा वापर करून `image_url` वर GET विनंती करते. यामुळे URL वरून प्रतिमेचा डेटा मिळतो.

2. `response.raise_for_status()` ओळ तपासते की विनंती यशस्वी आहे का. जर स्टेटस कोड एरर दाखवत असेल (उदा. 404 - सापडले नाही), तर अपवाद उचलला जातो. यामुळे फक्त यशस्वी विनंतीवरच प्रतिमा डाउनलोड केली जाते.

3. मिळालेला प्रतिमा डेटा PIL (Python Imaging Library) मधल्या `Image.open` मेथडला दिला जातो, जो प्रतिमा डेटा वापरून Image ऑब्जेक्ट तयार करतो.

4. `image.save(save_path)` ओळ प्रतिमा दिलेल्या `save_path` वर सेव्ह करते. `save_path` मध्ये फाइलचे नाव आणि एक्स्टेंशन असावे.

5. शेवटी, फंक्शन True परत करते, जे यशस्वी डाउनलोड सूचित करते. जर प्रक्रियेच्या दरम्यान काही अपवाद घडला, तर तो अपवाद पकडला जातो, त्रुटी संदेश छापला जातो आणि False परत केले जाते.

हे फंक्शन URL वरून प्रतिमा डाउनलोड करण्यासाठी आणि स्थानिक पातळीवर सेव्ह करण्यासाठी उपयुक्त आहे. हे डाउनलोड प्रक्रियेदरम्यान संभाव्य त्रुटी हाताळते आणि डाउनलोड यशस्वी झाले की नाही याबद्दल फीडबॅक देते.

हे लक्षात घेण्यासारखे आहे की, HTTP विनंत्यांसाठी `requests` लायब्ररी, प्रतिमांसाठी `PIL` लायब्ररी, आणि बाइट्स स्ट्रीम डेटा हाताळण्यासाठी `BytesIO` क्लास वापरला जातो.

### निष्कर्ष

हा स्क्रिप्ट मशीन लर्निंगसाठी डेटासेट तयार करण्याचा सोपा मार्ग प्रदान करतो. आवश्यक प्रतिमा डाउनलोड करतो, अपयशी डाउनलोड झालेल्या पंक्ती फिल्टर करतो, आणि डेटासेट CSV फाइल म्हणून सेव्ह करतो.

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
[नवीन डेटासेट स्क्रिप्ट तयार करा](../../../../code/04.Finetuning/generate_dataset.py)

### नमुना डेटासेट
[फाइनट्यूनिंगसाठी LORA उदाहरणातील नमुना डेटासेट](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**अस्वीकरण**:  
हे दस्तऐवज मशीन-आधारित एआय अनुवाद सेवांचा वापर करून अनुवादित केले गेले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज अधिकृत स्रोत मानावा. महत्त्वाच्या माहितीकरिता व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाचा वापर करून उद्भवणाऱ्या कोणत्याही गैरसमजुतींसाठी किंवा चुकीच्या अर्थ लावण्यास आम्ही जबाबदार राहणार नाही.