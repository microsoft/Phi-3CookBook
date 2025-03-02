## **Phi-4-mini-mm ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੋਡ ਤਿਆਰ ਕਰਨਾ**

Phi-4-mini, Phi ਪਰਿਵਾਰ ਦੀ ਮਜ਼ਬੂਤ ਕੋਡਿੰਗ ਸਮਰਥਾਵਾਂ ਨੂੰ ਜਾਰੀ ਰੱਖਦਾ ਹੈ। ਤੁਸੀਂ ਕੋਡਿੰਗ ਨਾਲ ਸਬੰਧਤ ਪ੍ਰਸ਼ਨ ਪੁੱਛਣ ਲਈ Prompt ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। ਬੇਸ਼ੱਕ, ਮਜ਼ਬੂਤ ਤਰਕ ਸ਼ਕਤੀ ਦੇ ਸ਼ਾਮਲ ਹੋਣ ਤੋਂ ਬਾਅਦ, ਇਸ ਵਿੱਚ ਹੋਰ ਵੀ ਮਜ਼ਬੂਤ ਕੋਡਿੰਗ ਸਮਰਥਾਵਾਂ ਹਨ, ਜਿਵੇਂ ਕਿ ਲੋੜਾਂ ਅਨੁਸਾਰ ਪ੍ਰੋਜੈਕਟ ਤਿਆਰ ਕਰਨਾ। ਉਦਾਹਰਨ ਲਈ, ਲੋੜਾਂ ਅਨੁਸਾਰ ਪ੍ਰੋਜੈਕਟ ਤਿਆਰ ਕਰੋ, ਜਿਵੇਂ:

### **ਲੋੜ**

ਖਰੀਦਦਾਰੀ ਕਾਰਟ ਐਪ ਬਣਾਓ

- ਹੇਠਾਂ ਦਿੱਤੇ ਤਰੀਕਿਆਂ ਨਾਲ ਇੱਕ API Rest ਬਣਾਓ:
    - ਪੇਜ ਆਫਸੈਟ ਅਤੇ ਲਿਮਿਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਬੀਅਰਜ਼ ਦੀ ਸੂਚੀ ਪ੍ਰਾਪਤ ਕਰੋ।
    - ID ਰਾਹੀਂ ਬੀਅਰ ਦਾ ਵੇਰਵਾ ਪ੍ਰਾਪਤ ਕਰੋ।
    - ਨਾਂ, ਵੇਰਵਾ, ਟੈਗਲਾਈਨ, ਭੋਜਨ ਜੋੜੀਆਂ, ਅਤੇ ਕੀਮਤ ਰਾਹੀਂ ਬੀਅਰ ਨੂੰ ਖੋਜੋ।
- ਮੁੱਖ ਪੇਜ 'ਤੇ ਉਤਪਾਦਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ।
    - ਉਤਪਾਦਾਂ ਨੂੰ ਫਿਲਟਰ ਕਰਨ ਲਈ ਇੱਕ ਖੋਜ ਬਾਰ ਬਣਾਓ।
    - ਜਦੋਂ ਯੂਜ਼ਰ ਕਿਸੇ ਉਤਪਾਦ 'ਤੇ ਕਲਿੱਕ ਕਰਦਾ ਹੈ ਤਾਂ ਵੇਰਵਾ ਪੇਜ 'ਤੇ ਜਾਓ।
- (ਵਿਕਲਪਿਕ) ਕੀਮਤ ਰਾਹੀਂ ਉਤਪਾਦਾਂ ਨੂੰ ਫਿਲਟਰ ਕਰਨ ਲਈ ਸਲਾਈਸਰ ਬਣਾਓ।
- ਖਰੀਦਦਾਰੀ ਕਾਰਟ ਬਣਾਓ।
    - ਉਤਪਾਦਾਂ ਨੂੰ ਕਾਰਟ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ।
    - ਉਤਪਾਦਾਂ ਨੂੰ ਕਾਰਟ ਵਿੱਚੋਂ ਹਟਾਓ।
    - ਕਾਰਟ ਵਿੱਚ ਉਤਪਾਦਾਂ ਦੀ ਕੁੱਲ ਕੀਮਤ ਦੀ ਗਿਣਤੀ ਕਰੋ।

### **ਨਮੂਨਾ ਕੋਡ - ਪਾਇਥਨ**

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

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ-ਅਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਪੂਰੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਸੰਗਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਲਿਖਿਆ ਦਸਤਾਵੇਜ਼ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।