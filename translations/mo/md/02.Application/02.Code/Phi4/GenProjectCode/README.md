## **Phi-4-mini-mm-ийг ашиглан код үүсгэх**

Phi-4-mini нь Phi гэр бүлийн хүчирхэг код бичих чадварыг үргэлжлүүлэн сайжруулж байна. Та Prompt ашиглан кодтой холбоотой асуултуудыг асууж болно. Мэдээжийн хэрэг, хүчтэй логик сэтгэлгээг нэмснээр энэ нь илүү хүчирхэг код үүсгэх чадвартай болсон, жишээлбэл, шаардлагын дагуу төслүүдийг үүсгэх гэх мэт. Жишээ нь:

### **Шаардлага**

Худалдааны сагсны апп үүсгэх

- Дараах аргуудтай API Rest үүсгэх:
    - Хуудасны офсет болон лимит ашиглан шар айрагны жагсаалтыг авах.
    - ID-аар шар айрагны дэлгэрэнгүй мэдээллийг авах.
    - Нэр, тайлбар, уриа үг, хоолны хослол болон үнээр нь шар айраг хайх.
- Үндсэн хуудсан дээр бүтээгдэхүүний жагсаалт үүсгэх.
    - Бүтээгдэхүүн шүүх хайлтын талбар үүсгэх.
    - Хэрэглэгч бүтээгдэхүүн дээр дарахад тайлбарын хуудас руу шилжих.
- (Сонголттой) Үнэ шүүх слайсер үүсгэх.
- Худалдааны сагс үүсгэх.
    - Сагсанд бүтээгдэхүүн нэмэх.
    - Сагснаас бүтээгдэхүүн устгах.
    - Сагсанд байгаа бүтээгдэхүүний нийт үнийг тооцоолох.

### **Жишээ код - Python**

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

It seems like you are asking for a translation into "mo." Could you clarify what "mo" refers to? Are you referring to a specific language, such as Maori, Mongolian, or another language? Let me know so I can assist you better!