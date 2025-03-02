# **ਲੋਕਲ ਵਿੱਚ Phi-3-Vision ਦੀ ਅਨੁਮਾਨ ਲਗਾਉਣਾ**

Phi-3-vision-128k-instruct ਸਿਰਫ਼ ਭਾਸ਼ਾ ਨੂੰ ਸਮਝਣ ਵਿੱਚ ਹੀ ਨਹੀਂ, ਸਗੋਂ ਵਿਜੁਅਲ ਤੌਰ 'ਤੇ ਵੀ ਦੁਨੀਆ ਨੂੰ ਦੇਖਣ ਵਿੱਚ Phi-3 ਦੀ ਮਦਦ ਕਰਦਾ ਹੈ। Phi-3-vision-128k-instruct ਰਾਹੀਂ ਅਸੀਂ ਵੱਖ-ਵੱਖ ਵਿਜੁਅਲ ਸਮੱਸਿਆਵਾਂ ਹੱਲ ਕਰ ਸਕਦੇ ਹਾਂ, ਜਿਵੇਂ ਕਿ OCR, ਟੇਬਲ ਵਿਸ਼ਲੇਸ਼ਣ, ਵਸਤੂਆਂ ਦੀ ਪਹਿਚਾਣ, ਤਸਵੀਰ ਦਾ ਵੇਰਵਾ ਦੇਣਾ ਆਦਿ। ਅਸੀਂ ਉਹ ਕੰਮ ਆਸਾਨੀ ਨਾਲ ਕਰ ਸਕਦੇ ਹਾਂ ਜੋ ਪਹਿਲਾਂ ਬਹੁਤ ਸਾਰਾ ਡਾਟਾ ਟ੍ਰੇਨਿੰਗ ਦੀ ਲੋੜ ਰੱਖਦੇ ਸਨ। ਹੇਠਾਂ ਦਿੱਤੇ ਤਕਨਾਲੋਜੀਆਂ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਸਿਨਾਰਿਓਜ਼ ਹਨ ਜੋ Phi-3-vision-128k-instruct ਰਾਹੀਂ ਹਵਾਲਾ ਦਿੱਤੇ ਗਏ ਹਨ।

## **0. ਤਿਆਰੀ**

ਕਿਰਪਾ ਕਰਕੇ ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਹੇਠਾਂ ਦਿੱਤੀਆਂ Python ਲਾਇਬ੍ਰੇਰੀਆਂ ਪਹਿਲਾਂ ਹੀ ਇੰਸਟਾਲ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ (Python 3.10+ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** ਦੀ ਵਰਤੋਂ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਅਤੇ flatten ਇੰਸਟਾਲ ਕਰੋ

```bash
pip install flash-attn --no-build-isolation
```

ਇੱਕ ਨਵਾਂ Notebook ਬਣਾਓ। ਉਦਾਹਰਣਾਂ ਪੂਰੀਆਂ ਕਰਨ ਲਈ, ਇਹ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਕਿ ਤੁਸੀਂ ਪਹਿਲਾਂ ਹੇਠਾਂ ਦਿੱਤਾ ਸਮੱਗਰੀ ਬਣਾਓ।

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

## **1. ਤਸਵੀਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ Phi-3-Vision ਨਾਲ ਕਰੋ**

ਅਸੀਂ ਚਾਹੁੰਦੇ ਹਾਂ ਕਿ AI ਸਾਡੀਆਂ ਤਸਵੀਰਾਂ ਦੇ ਸਮੱਗਰੀ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੇ ਅਤੇ ਸਬੰਧਤ ਵੇਰਵੇ ਪ੍ਰਦਾਨ ਕਰੇ।

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

ਅਸੀਂ Notebook ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ ਸਕ੍ਰਿਪਟ ਨੂੰ ਚਲਾਉਣ ਰਾਹੀਂ ਸਬੰਧਤ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਾਂ।

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Vision ਨਾਲ OCR**

ਤਸਵੀਰ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨ ਤੋਂ ਇਲਾਵਾ, ਅਸੀਂ ਤਸਵੀਰ ਤੋਂ ਜਾਣਕਾਰੀ ਵੀ ਕੱਢ ਸਕਦੇ ਹਾਂ। ਇਹ OCR ਪ੍ਰਕਿਰਿਆ ਹੈ ਜਿਸ ਲਈ ਸਾਨੂੰ ਪਹਿਲਾਂ ਕਠਿਨ ਕੋਡ ਲਿਖਣ ਦੀ ਲੋੜ ਹੁੰਦੀ ਸੀ।

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

ਨਤੀਜਾ ਹੈ

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. ਕਈ ਤਸਵੀਰਾਂ ਦੀ ਤੁਲਨਾ**

Phi-3 Vision ਕਈ ਤਸਵੀਰਾਂ ਦੀ ਤੁਲਨਾ ਕਰਨ ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ। ਅਸੀਂ ਇਸ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤਸਵੀਰਾਂ ਵਿੱਚ ਅੰਤਰ ਲੱਭ ਸਕਦੇ ਹਾਂ।

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

ਨਤੀਜਾ ਹੈ

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ-ਅਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਆਟੋਮੇਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੱਜੇਪਣ ਹੋ ਸਕਦੇ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਉਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।