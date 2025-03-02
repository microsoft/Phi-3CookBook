## **Phi-4-mini-mm ব্যবহার করে কোড তৈরি করা**

Phi-4-mini Phi Family-এর শক্তিশালী কোডিং দক্ষতা অব্যাহত রেখেছে। আপনি প্রম্পট ব্যবহার করে কোডিং-সম্পর্কিত প্রশ্ন জিজ্ঞাসা করতে পারেন। অবশ্যই, শক্তিশালী যুক্তি করার ক্ষমতা যোগ করার পর, এটি আরও উন্নত কোডিং দক্ষতা অর্জন করেছে, যেমন চাহিদা অনুযায়ী প্রজেক্ট তৈরি করা। উদাহরণস্বরূপ, চাহিদা অনুযায়ী প্রজেক্ট তৈরি করা, যেমন:

### **চাহিদা**

একটি শপিং কার্ট অ্যাপ তৈরি করুন

- নিম্নলিখিত মেথডসহ একটি API Rest তৈরি করুন:
    - পেজ অফসেট এবং লিমিট ব্যবহার করে বিয়ারের একটি তালিকা পান।
    - আইডি দিয়ে বিয়ারের বিবরণ পান।
    - নাম, বিবরণ, ট্যাগলাইন, ফুড পেয়ারিংস, এবং দাম দিয়ে বিয়ার অনুসন্ধান করুন।
- মূল পৃষ্ঠায় পণ্যের একটি তালিকা তৈরি করুন।
    - পণ্য ফিল্টার করার জন্য একটি সার্চ বার তৈরি করুন।
    - ব্যবহারকারী যখন কোনো পণ্যের উপর ক্লিক করবে তখন বিবরণ পৃষ্ঠায় নিয়ে যান।
- (ঐচ্ছিক) পণ্যের দাম অনুযায়ী ফিল্টার করার জন্য একটি স্লাইসার।
- একটি শপিং কার্ট তৈরি করুন।
    - পণ্য কার্টে যোগ করুন।
    - পণ্য কার্ট থেকে সরান।
    - কার্টে থাকা পণ্যের মোট মূল্য গণনা করুন।

### **নমুনা কোড - পাইথন**


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

**অস্বীকৃতি**:  
এই নথিটি মেশিন-ভিত্তিক এআই অনুবাদ পরিষেবা ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিক অনুবাদের চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। এর মূল ভাষায় থাকা আসল নথিটিকেই প্রামাণিক উৎস হিসেবে গণ্য করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ ব্যবহার করার পরামর্শ দেওয়া হচ্ছে। এই অনুবাদ ব্যবহার থেকে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই। 