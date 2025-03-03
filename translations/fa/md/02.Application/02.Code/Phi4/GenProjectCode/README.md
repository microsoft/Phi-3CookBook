## **استفاده از Phi-4-mini-mm برای تولید کد**

Phi-4-mini همچنان توانایی‌های کدنویسی قدرتمند خانواده Phi را ادامه می‌دهد. شما می‌توانید از Prompt برای پرسیدن سوالات مرتبط با کدنویسی استفاده کنید. البته، با افزودن قابلیت استدلال قوی، توانایی‌های کدنویسی آن نیز تقویت شده است، مانند تولید پروژه‌ها بر اساس نیازها. برای مثال، تولید پروژه‌ها بر اساس نیازها، مانند:

### **نیازمندی**

ایجاد یک اپلیکیشن سبد خرید

- ایجاد یک API Rest با روش‌های زیر:
  - دریافت لیستی از آبجوها با استفاده از جابجایی صفحه و محدودیت.
  - دریافت جزئیات آبجو با شناسه.
  - جستجوی آبجو بر اساس نام، توضیحات، شعار، جفت‌های غذایی و قیمت.
- ایجاد لیستی از محصولات در صفحه اصلی.
  - ایجاد یک نوار جستجو برای فیلتر کردن محصولات.
  - هدایت به صفحه توضیحات وقتی کاربر روی یک محصول کلیک می‌کند.
- (اختیاری) ایجاد یک فیلتر برای فیلتر کردن محصولات بر اساس قیمت.
- ایجاد یک سبد خرید.
  - افزودن محصولات به سبد خرید.
  - حذف محصولات از سبد خرید.
  - محاسبه قیمت کل محصولات در سبد خرید.

### **نمونه کد - Python**

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

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه ماشینی مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادقتی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.