# **লোকাল পরিবেশে Phi-3-Vision ইন্টারফারেন্স**

Phi-3-vision-128k-instruct Phi-3 কে শুধু ভাষা বুঝতেই নয়, দৃষ্টিশক্তির মাধ্যমে বিশ্বকে দেখার ক্ষমতাও প্রদান করে। Phi-3-vision-128k-instruct এর মাধ্যমে আমরা বিভিন্ন ভিজ্যুয়াল সমস্যার সমাধান করতে পারি, যেমন OCR, টেবিল বিশ্লেষণ, অবজেক্ট শনাক্তকরণ, ছবি বর্ণনা ইত্যাদি। এটি আমাদের এমন কাজ সহজে করতে সাহায্য করে যা পূর্বে অনেক ডেটা প্রশিক্ষণের প্রয়োজন হতো। নিচে Phi-3-vision-128k-instruct দ্বারা ব্যবহৃত সম্পর্কিত কৌশল এবং প্রয়োগের ক্ষেত্র উল্লেখ করা হয়েছে।

## **0. প্রস্তুতি**

ব্যবহার করার আগে নিশ্চিত করুন যে নিম্নলিখিত Python লাইব্রেরিগুলি ইনস্টল করা হয়েছে (Python 3.10+ ব্যবহার করার সুপারিশ করা হয়)।

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** ব্যবহার করার সুপারিশ করা হয় এবং flatten ইনস্টল করুন।

```bash
pip install flash-attn --no-build-isolation
```

একটি নতুন নোটবুক তৈরি করুন। উদাহরণগুলি সম্পূর্ণ করতে, প্রথমে নিম্নলিখিত বিষয়বস্তু তৈরি করার পরামর্শ দেওয়া হয়।

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

## **1. Phi-3-Vision দিয়ে ছবির বিশ্লেষণ**

আমরা চাই AI আমাদের ছবির বিষয়বস্তু বিশ্লেষণ করতে পারুক এবং সংশ্লিষ্ট বর্ণনা প্রদান করুক।

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

নোটবুকে নিম্নলিখিত স্ক্রিপ্ট চালিয়ে আমরা সংশ্লিষ্ট উত্তর পেতে পারি।

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Vision দিয়ে OCR**

ছবির বিশ্লেষণের পাশাপাশি, আমরা ছবির তথ্যও বের করতে পারি। এটি OCR প্রক্রিয়া, যা আগে জটিল কোড লিখে সম্পন্ন করতে হতো।

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

ফলাফল হল:

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. একাধিক ছবির তুলনা**

Phi-3 Vision একাধিক ছবির তুলনা সমর্থন করে। এই মডেলটি ব্যবহার করে আমরা ছবিগুলোর মধ্যে পার্থক্য খুঁজে পেতে পারি।

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

ফলাফল হল:

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**অস্বীকৃতি**:  
এই নথিটি মেশিন-ভিত্তিক এআই অনুবাদ পরিষেবার মাধ্যমে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য নির্ভুলতার জন্য চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকেই প্রামাণ্য উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী থাকব না।