## **Phi-4-mini-mm használata kód generálására**

A Phi-4-mini továbbviszi a Phi család erős kódolási képességeit. A Prompt segítségével kódolással kapcsolatos kérdéseket tehetsz fel. Természetesen az erős érvelési képesség hozzáadásával még erősebb kódolási képességekkel rendelkezik, például projektek generálására az igények szerint. Például projektek generálása az igények alapján, mint például:

### **Feladat**

Hozz létre egy Bevásárlókosár alkalmazást!

- Hozz létre egy REST API-t a következő metódusokkal:
    - Kérj le egy sörlistát oldaleltolás és limit használatával.
    - Kérj le sör részleteket azonosító alapján.
    - Keress söröket név, leírás, szlogen, ételpárosítások és ár alapján.
- Hozz létre egy terméklistát a főoldalon.
    - Hozz létre egy keresősávot a termékek szűréséhez.
    - Navigálj a leírás oldalra, amikor a felhasználó egy termékre kattint.
- (Opcionális) Ár szerinti szűrő a termékekhez.
- Hozz létre egy bevásárlókosarat.
    - Adj termékeket a kosárhoz.
    - Távolíts el termékeket a kosárból.
    - Számítsd ki a kosárban lévő termékek összárát.

### **Mintakód - Python**


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

**Jogi nyilatkozat**:  
Ez a dokumentum gépi AI fordítási szolgáltatásokkal lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.