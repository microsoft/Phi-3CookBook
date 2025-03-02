## **Uporaba Phi-4-mini-mm za generiranje kode**

Phi-4-mini nadaljuje z močnimi programerskimi zmožnostmi družine Phi. Uporabite lahko Prompt za postavljanje vprašanj, povezanih s programiranjem. Seveda, z dodano sposobnostjo močnega sklepanja, ima še močnejše programerske zmožnosti, kot je na primer generiranje projektov glede na zahteve. Na primer, generiranje projektov glede na zahteve, kot so:

### **Zahteva**

Ustvarite aplikacijo za nakupovalni voziček

- Ustvarite API Rest z naslednjimi metodami:
    - Pridobite seznam piv z uporabo zamika strani in omejitve.
    - Pridobite podrobnosti o pivu po ID-ju.
    - Iščite pivo po imenu, opisu, sloganu, kombinacijah hrane in ceni.
- Na glavni strani ustvarite seznam izdelkov.
    - Ustvarite iskalno vrstico za filtriranje izdelkov.
    - Ob kliku na izdelek omogočite navigacijo na stran z opisom.
- (Neobvezno) Drsnik za filtriranje izdelkov po ceni.
- Ustvarite nakupovalni voziček.
    - Dodajte izdelke v voziček.
    - Odstranite izdelke iz vozička.
    - Izračunajte skupno ceno izdelkov v vozičku.

### **Vzorčna koda - Python**

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

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazuma ali napačne razlage, ki bi izhajale iz uporabe tega prevoda.