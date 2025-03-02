# **ใช้งาน Phi-3-Vision ในเครื่อง Local**

Phi-3-vision-128k-instruct ช่วยให้ Phi-3 ไม่เพียงแค่เข้าใจภาษา แต่ยังสามารถมองเห็นโลกในเชิงภาพได้อีกด้วย ผ่าน Phi-3-vision-128k-instruct เราสามารถแก้ปัญหาภาพต่าง ๆ ได้ เช่น OCR, การวิเคราะห์ตาราง, การจดจำวัตถุ, การอธิบายภาพ เป็นต้น เราสามารถทำงานที่เคยต้องใช้ข้อมูลการฝึกฝนจำนวนมากได้อย่างง่ายดาย ตัวอย่างต่อไปนี้คือเทคนิคและสถานการณ์การใช้งานที่เกี่ยวข้องกับ Phi-3-vision-128k-instruct

## **0. การเตรียมตัว**

โปรดตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งไลบรารี Python ต่อไปนี้แล้วก่อนการใช้งาน (แนะนำให้ใช้ Python 3.10+)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

แนะนำให้ใช้ ***CUDA 11.6+*** และติดตั้ง flatten

```bash
pip install flash-attn --no-build-isolation
```

สร้าง Notebook ใหม่ เพื่อทำตัวอย่าง แนะนำให้คุณสร้างเนื้อหาต่อไปนี้ก่อน

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

## **1. การวิเคราะห์ภาพด้วย Phi-3-Vision**

เราต้องการให้ AI สามารถวิเคราะห์เนื้อหาของภาพและให้คำอธิบายที่เกี่ยวข้อง

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

เราสามารถรับคำตอบที่เกี่ยวข้องได้โดยการรันสคริปต์ต่อไปนี้ใน Notebook

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. OCR ด้วย Phi-3-Vision**

นอกจากการวิเคราะห์ภาพแล้ว เรายังสามารถดึงข้อมูลจากภาพได้ด้วย นี่คือกระบวนการ OCR ซึ่งในอดีตเราจำเป็นต้องเขียนโค้ดที่ซับซ้อนเพื่อทำงานนี้

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

ผลลัพธ์คือ

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. การเปรียบเทียบภาพหลายภาพ**

Phi-3 Vision รองรับการเปรียบเทียบภาพหลายภาพ เราสามารถใช้โมเดลนี้เพื่อหาความแตกต่างระหว่างภาพได้

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

ผลลัพธ์คือ

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI อัตโนมัติ แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่ถูกต้องที่สุด สำหรับข้อมูลที่มีความสำคัญ ขอแนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดพลาดที่เกิดจากการใช้การแปลนี้