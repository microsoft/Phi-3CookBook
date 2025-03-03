## **Phi-4-mini-mm चा उपयोग करून कोड तयार करणे**

Phi-4-mini ने Phi Family च्या मजबूत कोडिंग क्षमतांना पुढे नेले आहे. तुम्ही कोडिंगशी संबंधित प्रश्न विचारण्यासाठी Prompt चा वापर करू शकता. अर्थात, मजबूत तर्कशक्ती जोडल्यामुळे, त्याच्या कोडिंग क्षमताही अधिक मजबूत झाल्या आहेत, जसे की आवश्यकता लक्षात घेऊन प्रकल्प तयार करणे. उदाहरणार्थ, आवश्यकता लक्षात घेऊन प्रकल्प तयार करणे, जसे:

### **आवश्यकता**

शॉपिंग कार्ट अ‍ॅप तयार करा

- खालील पद्धतींसह API Rest तयार करा:
    - पृष्ठ ऑफसेट आणि मर्यादा वापरून बियरची यादी मिळवा.
    - आयडीद्वारे बियरचे तपशील मिळवा.
    - नाव, वर्णन, टॅगलाइन, खाद्य संयोजन आणि किंमत यावरून बियर शोधा.
- मुख्य पृष्ठावर उत्पादनांची यादी तयार करा.
    - उत्पादने फिल्टर करण्यासाठी एक शोध बार तयार करा.
    - वापरकर्त्याने उत्पादनावर क्लिक केल्यावर वर्णन पृष्ठावर जा.
- (पर्यायी) किंमतीनुसार उत्पादने फिल्टर करण्यासाठी स्लायसर तयार करा.
- शॉपिंग कार्ट तयार करा.
    - उत्पादनांना कार्टमध्ये जोडा.
    - उत्पादनांना कार्टमधून काढा.
    - कार्टमधील उत्पादनांच्या किंमतींची एकूण रक्कम मोजा.

### **नमुना कोड - Python**

```python

import requests
import torch
from PIL import Image
import soundfile
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig,pipeline,AutoTokenizer

model_path = 'Your Phi-4-mini-mm-instruct'

kwargs = {}
kwargs['torch_dtype'] = torch.bfloat16

processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    trust_remote_code=True,
    torch_dtype='auto',
    _attn_implementation='flash_attention_2',
).cuda()

generation_config = GenerationConfig.from_pretrained(model_path, 'generation_config.json')

user_prompt = '<|user|>'
assistant_prompt = '<|assistant|>'
prompt_suffix = '<|end|>'

requirement = """

Create a Shopping Cart App

- Create an API Rest with the following methods:
    - Get a list of beers using page offset and limit.
    - Get beer details by id.
    - Search for beer by name, description, tagline, food pairings, and price.
- Create a list of products on the main page.
    - Create a search bar to filter products.
    - Navigate to the description page when the user clicks on a product.
- (Optional) Slicer to filter products by price.
- Create a shopping cart.
    - Add products to the cart.
    - Remove products from the cart.
    - Calculate the total price of the products in the cart."""

note = """ 

            Note:

            1. Use Python Flask to create a Repository pattern based on the following structure to generate the files

            ｜- models
            ｜- controllers
            ｜- repositories
            ｜- views

            2. For the view page, please use SPA + VueJS + TypeScript to build

            3. Firstly use markdown to output the generated project structure (including directories and files), and then generate the  file names and corresponding codes step by step, output like this 

               ## Project Structure

                    ｜- models
                        | - user.py
                    ｜- controllers
                        | - user_controller.py
                    ｜- repositories
                        | - user_repository.py
                    ｜- templates
                        | - index.html

               ## Backend
                 
                   #### `models/user.py`
                   ```python

                   ```
                   .......
               

               ## Frontend
                 
                   #### `templates/index.html`
                   ```html

                   ```
                   ......."""

prompt = f'{user_prompt}Please create a project with Python and Flask according to the following requirements：\n{requirement}{note}{prompt_suffix}{assistant_prompt}'

inputs = processor(prompt, images=None, return_tensors='pt').to('cuda:0')

generate_ids = model.generate(
    **inputs,
    max_new_tokens=2048,
    generation_config=generation_config,
)

generate_ids = generate_ids[:, inputs['input_ids'].shape[1] :]

response = processor.batch_decode(
    generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
)[0]

print(response)

```

**अस्वीकरण**:  
हे दस्तऐवज मशीन-आधारित AI अनुवाद सेवा वापरून अनुवादित केले गेले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज हा अधिकृत स्रोत मानला पाहिजे. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाचा वापर करून निर्माण झालेल्या कोणत्याही गैरसमजुतींसाठी किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.