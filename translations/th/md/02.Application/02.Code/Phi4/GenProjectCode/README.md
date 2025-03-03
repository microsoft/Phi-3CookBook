## **การใช้ Phi-4-mini-mm เพื่อสร้างโค้ด**

Phi-4-mini ยังคงความสามารถในการเขียนโค้ดที่ยอดเยี่ยมของตระกูล Phi คุณสามารถใช้ Prompt เพื่อถามคำถามที่เกี่ยวข้องกับการเขียนโค้ดได้ แน่นอนว่าเมื่อเพิ่มความสามารถในการให้เหตุผลที่แข็งแกร่งเข้าไปแล้ว ก็ยิ่งทำให้ความสามารถในการเขียนโค้ดนั้นทรงพลังขึ้น เช่น การสร้างโปรเจกต์ตามความต้องการ ตัวอย่างเช่น สร้างโปรเจกต์ตามความต้องการ เช่น:

### **ความต้องการ**

สร้างแอปพลิเคชันตะกร้าสินค้า (Shopping Cart App)

- สร้าง API Rest พร้อมกับเมธอดดังต่อไปนี้:
    - ดึงรายการเบียร์โดยใช้ page offset และ limit
    - ดึงรายละเอียดของเบียร์ตาม id
    - ค้นหาเบียร์ตามชื่อ, คำอธิบาย, tagline, การจับคู่กับอาหาร และราคา
- สร้างรายการสินค้าในหน้าแรก
    - สร้างแถบค้นหาเพื่อกรองสินค้า
    - นำทางไปยังหน้ารายละเอียดเมื่อผู้ใช้คลิกที่สินค้า
- (ตัวเลือก) ตัวกรองเพื่อกรองสินค้าตามราคา
- สร้างตะกร้าสินค้า
    - เพิ่มสินค้าไปยังตะกร้า
    - ลบสินค้าออกจากตะกร้า
    - คำนวณราคารวมของสินค้าที่อยู่ในตะกร้า

### **ตัวอย่างโค้ด - Python**


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

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติด้วย AI แม้ว่าเราจะพยายามอย่างเต็มที่เพื่อความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาดั้งเดิมควรถูกพิจารณาให้เป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้