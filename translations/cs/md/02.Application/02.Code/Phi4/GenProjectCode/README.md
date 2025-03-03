## **Použití Phi-4-mini-mm k vytváření kódu**

Phi-4-mini pokračuje v silných schopnostech kódování rodiny Phi. Můžete použít Prompt k pokládání otázek souvisejících s programováním. Samozřejmě, díky přidané silné schopnosti logického uvažování má ještě lepší možnosti kódování, například generování projektů podle požadavků. Například generování projektů podle požadavků, jako:

### **Požadavek**

Vytvořit aplikaci Nákupní košík

- Vytvořit API Rest s následujícími metodami:
    - Získat seznam piv s použitím stránkování (offset a limit).
    - Získat detaily piva podle jeho ID.
    - Vyhledávat piva podle názvu, popisu, sloganu, kombinace s jídlem a ceny.
- Vytvořit seznam produktů na hlavní stránce.
    - Vytvořit vyhledávací pole pro filtrování produktů.
    - Přejít na stránku s popisem produktu, když uživatel klikne na produkt.
- (Volitelné) Posuvník pro filtrování produktů podle ceny.
- Vytvořit nákupní košík.
    - Přidávat produkty do košíku.
    - Odstraňovat produkty z košíku.
    - Vypočítat celkovou cenu produktů v košíku.

### **Ukázkový kód - Python**

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

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových překladatelských služeb využívajících umělou inteligenci. I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.