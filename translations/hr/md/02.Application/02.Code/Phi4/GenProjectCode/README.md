## **Korištenje Phi-4-mini-mm za generiranje koda**

Phi-4-mini nastavlja snažne mogućnosti kodiranja Phi obitelji. Možete koristiti Prompt za postavljanje pitanja vezanih uz kodiranje. Naravno, uz dodavanje snažnih sposobnosti zaključivanja, ima još jače mogućnosti kodiranja, poput generiranja projekata prema zahtjevima. Na primjer, generiranje projekata prema zahtjevima, kao što su:

### **Zahtjev**

Kreiraj aplikaciju za košaricu

- Kreiraj REST API s sljedećim metodama:
    - Dohvati popis piva koristeći offset stranice i limit.
    - Dohvati detalje o pivu prema id-u.
    - Pretraži pivo prema nazivu, opisu, sloganu, kombinacijama hrane i cijeni.
- Kreiraj popis proizvoda na glavnoj stranici.
    - Dodaj traku za pretraživanje kako bi se filtrirali proizvodi.
    - Navigiraj na stranicu s opisom kada korisnik klikne na proizvod.
- (Opcionalno) Dodaj filter za proizvode prema cijeni.
- Kreiraj košaricu.
    - Dodaj proizvode u košaricu.
    - Ukloni proizvode iz košarice.
    - Izračunaj ukupnu cijenu proizvoda u košarici.

### **Primjer koda - Python**


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

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga automatskog prevođenja temeljenih na umjetnoj inteligenciji. Iako nastojimo osigurati točnost, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja proizašla iz korištenja ovog prijevoda.