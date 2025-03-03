## **Phi-4-mini-mm का उपयोग करके कोड जनरेट करना**

Phi-4-mini ने Phi परिवार की मजबूत कोडिंग क्षमताओं को आगे बढ़ाया है। आप कोडिंग से संबंधित सवाल पूछने के लिए Prompt का उपयोग कर सकते हैं। निश्चित रूप से, मजबूत तर्क क्षमता जोड़ने के बाद, इसकी कोडिंग क्षमताएं और भी अधिक मजबूत हो गई हैं, जैसे कि आवश्यकताओं के अनुसार प्रोजेक्ट जनरेट करना। उदाहरण के लिए, आवश्यकताओं के अनुसार प्रोजेक्ट जनरेट करना, जैसे:

### **आवश्यकता**

एक शॉपिंग कार्ट ऐप बनाएं

- निम्नलिखित विधियों के साथ एक API Rest बनाएं:
    - पेज ऑफसेट और लिमिट का उपयोग करके बियर की सूची प्राप्त करें।
    - आईडी द्वारा बियर का विवरण प्राप्त करें।
    - नाम, विवरण, टैगलाइन, फूड पेयरिंग्स और कीमत के आधार पर बियर खोजें।
- मुख्य पेज पर उत्पादों की एक सूची बनाएं।
    - उत्पादों को फ़िल्टर करने के लिए एक सर्च बार बनाएं।
    - जब उपयोगकर्ता किसी उत्पाद पर क्लिक करे, तो विवरण पेज पर नेविगेट करें।
- (वैकल्पिक) उत्पादों को कीमत के आधार पर फ़िल्टर करने के लिए एक स्लाइसर।
- एक शॉपिंग कार्ट बनाएं।
    - उत्पादों को कार्ट में जोड़ें।
    - उत्पादों को कार्ट से हटाएं।
    - कार्ट में उत्पादों की कुल कीमत की गणना करें।

### **नमूना कोड - पायथन**

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
यह दस्तावेज़ मशीन-आधारित एआई अनुवाद सेवाओं का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।