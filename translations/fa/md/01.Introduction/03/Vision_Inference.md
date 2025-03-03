# **استنتاج Phi-3-Vision به صورت محلی**

Phi-3-vision-128k-instruct به Phi-3 این امکان را می‌دهد که نه تنها زبان را درک کند، بلکه دنیای بصری را نیز ببیند. از طریق Phi-3-vision-128k-instruct، می‌توانیم مسائل مختلف بصری را حل کنیم، مانند OCR، تحلیل جداول، شناسایی اشیا، توصیف تصاویر و غیره. ما می‌توانیم به راحتی وظایفی را انجام دهیم که قبلاً نیاز به آموزش داده‌های زیادی داشتند. موارد زیر تکنیک‌ها و سناریوهای کاربردی مرتبطی هستند که توسط Phi-3-vision-128k-instruct ارائه شده‌اند.

## **0. آماده‌سازی**

لطفاً مطمئن شوید که کتابخانه‌های پایتون زیر قبل از استفاده نصب شده‌اند (پیشنهاد می‌شود از Python 3.10+ استفاده کنید)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

پیشنهاد می‌شود از ***CUDA 11.6+*** استفاده کنید و flatten را نصب کنید

```bash
pip install flash-attn --no-build-isolation
```

یک نوت‌بوک جدید ایجاد کنید. برای تکمیل مثال‌ها، پیشنهاد می‌شود ابتدا محتوای زیر را ایجاد کنید.

```python
from PIL import Image
import requests
import torch
from transformers import AutoModelForCausalLM
from transformers import AutoProcessor

model_id = "microsoft/Phi-3-vision-128k-instruct"

kwargs = {}
kwargs['torch_dtype'] = torch.bfloat16

processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True, torch_dtype="auto").cuda()

user_prompt = '<|user|>\n'
assistant_prompt = '<|assistant|>\n'
prompt_suffix = "<|end|>\n"
```

## **1. تحلیل تصویر با Phi-3-Vision**

ما می‌خواهیم هوش مصنوعی بتواند محتوای تصاویر ما را تحلیل کند و توضیحات مرتبط ارائه دهد.

```python
prompt = f"{user_prompt}<|image_1|>\nCould you please introduce this stock to me?{prompt_suffix}{assistant_prompt}"


url = "https://g.foolcdn.com/editorial/images/767633/nvidiadatacenterrevenuefy2017tofy2024.png"

image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(prompt, image, return_tensors="pt").to("cuda:0")

generate_ids = model.generate(**inputs, 
                              max_new_tokens=1000,
                              eos_token_id=processor.tokenizer.eos_token_id,
                              )
generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]

response = processor.batch_decode(generate_ids, 
                                  skip_special_tokens=True, 
                                  clean_up_tokenization_spaces=False)[0]
```

می‌توانیم با اجرای اسکریپت زیر در نوت‌بوک پاسخ‌های مرتبط را دریافت کنیم.

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. OCR با Phi-3-Vision**

علاوه بر تحلیل تصویر، می‌توانیم اطلاعات را نیز از تصویر استخراج کنیم. این فرآیند OCR است که قبلاً برای انجام آن نیاز به نوشتن کدهای پیچیده داشتیم.

```python
prompt = f"{user_prompt}<|image_1|>\nHelp me get the title and author information of this book?{prompt_suffix}{assistant_prompt}"

url = "https://marketplace.canva.com/EAFPHUaBrFc/1/0/1003w/canva-black-and-white-modern-alone-story-book-cover-QHBKwQnsgzs.jpg"

image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(prompt, image, return_tensors="pt").to("cuda:0")

generate_ids = model.generate(**inputs, 
                              max_new_tokens=1000,
                              eos_token_id=processor.tokenizer.eos_token_id,
                              )

generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]

response = processor.batch_decode(generate_ids, 
                                  skip_special_tokens=False, 
                                  clean_up_tokenization_spaces=False)[0]

```

نتیجه این است

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. مقایسه چندین تصویر**

Phi-3 Vision از مقایسه چندین تصویر پشتیبانی می‌کند. ما می‌توانیم از این مدل برای پیدا کردن تفاوت‌های بین تصاویر استفاده کنیم.

```python
prompt = f"{user_prompt}<|image_1|>\n<|image_2|>\n What is difference in this two images?{prompt_suffix}{assistant_prompt}"

print(f">>> Prompt\n{prompt}")

url = "https://hinhnen.ibongda.net/upload/wallpaper/doi-bong/2012/11/22/arsenal-wallpaper-free.jpg"

image_1 = Image.open(requests.get(url, stream=True).raw)

url = "https://assets-webp.khelnow.com/d7293de2fa93b29528da214253f1d8d0/news/uploads/2021/07/Arsenal-1024x576.jpg.webp"

image_2 = Image.open(requests.get(url, stream=True).raw)

images = [image_1, image_2]

inputs = processor(prompt, images, return_tensors="pt").to("cuda:0")

generate_ids = model.generate(**inputs, 
                              max_new_tokens=1000,
                              eos_token_id=processor.tokenizer.eos_token_id,
                              )

generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]

response = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
```

نتیجه این است

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه ماشینی مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس یا حیاتی، ترجمه انسانی حرفه‌ای توصیه می‌شود. ما هیچ گونه مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.