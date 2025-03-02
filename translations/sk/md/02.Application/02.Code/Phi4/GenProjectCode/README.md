## **Použitie Phi-4-mini-mm na generovanie kódu**

Phi-4-mini pokračuje v silných schopnostiach kódovania rodiny Phi. Môžete použiť Prompt na kladenie otázok týkajúcich sa kódovania. Samozrejme, po pridaní schopnosti silného uvažovania má ešte lepšie schopnosti kódovania, ako napríklad generovanie projektov podľa požiadaviek. Napríklad generovanie projektov podľa požiadaviek, ako napríklad:

### **Požiadavka**

Vytvoriť aplikáciu Shopping Cart

- Vytvoriť API Rest s nasledujúcimi metódami:
    - Získať zoznam pív pomocou stránkovania (offset a limit).
    - Získať detaily o pive podľa ID.
    - Vyhľadávať pivo podľa názvu, popisu, sloganu, párovania s jedlom a ceny.
- Vytvoriť zoznam produktov na hlavnej stránke.
    - Vytvoriť vyhľadávací panel na filtrovanie produktov.
    - Pri kliknutí na produkt prejsť na stránku s popisom.
- (Voliteľné) Posuvník na filtrovanie produktov podľa ceny.
- Vytvoriť nákupný košík.
    - Pridať produkty do košíka.
    - Odstrániť produkty z košíka.
    - Vypočítať celkovú cenu produktov v košíku.

### **Ukážkový kód - Python**

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

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladových služieb. Aj keď sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za záväzný zdroj. Pre dôležité informácie sa odporúča profesionálny preklad od človeka. Nezodpovedáme za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.