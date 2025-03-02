# **Phi-3-Vision-ийг Локал орчинд хэрэгжүүлэх**

Phi-3-vision-128k-instruct нь Phi-3-д зөвхөн хэл ойлгох бус, мөн дэлхийг харах чадварыг олгодог. Phi-3-vision-128k-instruct-ийн тусламжтайгаар бид OCR, хүснэгтийн шинжилгээ, объект таних, зураг тайлбарлах гэх мэт олон төрлийн харааны асуудлыг шийдвэрлэх боломжтой. Өмнө нь их хэмжээний өгөгдлийн сургалт шаарддаг байсан даалгавруудыг бид хялбархан гүйцэтгэх боломжтой болсон. Доор Phi-3-vision-128k-instruct-ийн ашигладаг холбогдох арга техник, хэрэглээний жишээнүүдийг дурдсан болно.

## **0. Бэлтгэл**

Хэрэглэхийн өмнө дараах Python сангуудыг суулгасан эсэхээ шалгана уу (Python 3.10+ хувилбарыг санал болгож байна)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** хувилбарыг ашиглахыг зөвлөж байна, мөн flatten-ийг суулгах шаардлагатай.

```bash
pip install flash-attn --no-build-isolation
```

Шинэ Notebook үүсгэнэ үү. Жишээнүүдийг гүйцэтгэхийн тулд доорх агуулгыг эхлээд үүсгэхийг санал болгож байна.

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

## **1. Phi-3-Vision ашиглан зургийг шинжлэх**

Бид AI-ийг зургийн агуулгыг шинжлэх, холбогдох тайлбар гаргах чадвартай болгохыг хүсэж байна.

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

Notebook дотор дараах скриптийг ажиллуулснаар бид холбогдох хариултыг авах боломжтой.

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Vision ашиглан OCR хийх**

Зургийг шинжлэхээс гадна бид зургийн мэдээллийг гаргаж авах боломжтой. Энэ нь OCR процесс бөгөөд өмнө нь нарийн төвөгтэй код бичих шаардлагатай байсан.

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

Үр дүн нь:

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. Олон зургийг харьцуулах**

Phi-3 Vision нь олон зургийг харьцуулах боломжийг олгодог. Бид энэ загварыг ашиглан зургуудын ялгааг олох боломжтой.

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

Үр дүн нь:

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

It seems you've mentioned "mo," but it's unclear which specific language or dialect you're referring to with "mo." Could you clarify the language you would like the text translated into? For example, are you referring to Māori, Mongolian, or another language? Let me know, and I'd be happy to assist!