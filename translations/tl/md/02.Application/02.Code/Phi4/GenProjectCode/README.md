## **Paggamit ng Phi-4-mini-mm para gumawa ng code**

Ang Phi-4-mini ay nagpapatuloy sa malakas na kakayahan sa pag-coding ng Phi Family. Maaari mong gamitin ang Prompt para magtanong ng mga katanungan na may kaugnayan sa pag-coding. Siyempre, dahil sa nadagdagang kakayahan sa pangangatwiran, mas malakas ang kakayahan nito sa pag-coding, tulad ng paggawa ng mga proyekto ayon sa mga pangangailangan. Halimbawa, gumawa ng mga proyekto ayon sa mga pangangailangan, tulad ng:

### **Pangangailangan**

Gumawa ng isang Shopping Cart App

- Gumawa ng isang API Rest na may mga sumusunod na methods:
    - Kumuha ng listahan ng mga beer gamit ang page offset at limit.
    - Kumuha ng detalye ng beer gamit ang id.
    - Maghanap ng beer ayon sa pangalan, paglalarawan, tagline, food pairings, at presyo.
- Gumawa ng listahan ng mga produkto sa pangunahing pahina.
    - Gumawa ng search bar para i-filter ang mga produkto.
    - Mag-navigate sa description page kapag nag-click ang user sa isang produkto.
- (Opsyonal) Slicer para i-filter ang mga produkto ayon sa presyo.
- Gumawa ng shopping cart.
    - Magdagdag ng mga produkto sa cart.
    - Mag-alis ng mga produkto mula sa cart.
    - Kalkulahin ang kabuuang presyo ng mga produkto sa cart.

### **Halimbawang Code - Python**


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

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI na nakabatay sa makina. Bagamat pinagsisikapan naming maging wasto, pakitandaan na ang mga awtomatikong salin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na pangunahing mapagkukunan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng salin na ito.