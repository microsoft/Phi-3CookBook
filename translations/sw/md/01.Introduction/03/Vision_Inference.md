# **Kutumia Phi-3-Vision Katika Mazingira ya Ndani**

Phi-3-vision-128k-instruct inamwezesha Phi-3 sio tu kuelewa lugha, bali pia kuona ulimwengu kwa njia ya picha. Kupitia Phi-3-vision-128k-instruct, tunaweza kutatua matatizo mbalimbali ya picha, kama vile OCR, uchambuzi wa jedwali, utambuzi wa vitu, kuelezea picha, na mengineyo. Tunaweza kukamilisha kazi kwa urahisi ambazo hapo awali zilihitaji mafunzo mengi ya data. Zifuatazo ni mbinu na hali za matumizi zinazohusiana na Phi-3-vision-128k-instruct.

## **0. Maandalizi**

Tafadhali hakikisha maktaba zifuatazo za Python zimewekwa kabla ya kutumia (inapendekezwa Python 3.10+)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

Inapendekezwa kutumia ***CUDA 11.6+*** na kusakinisha flatten

```bash
pip install flash-attn --no-build-isolation
```

Tengeneza Notebook mpya. Ili kukamilisha mifano, inapendekezwa uunde maudhui yafuatayo kwanza.

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

## **1. Kuchambua Picha kwa Kutumia Phi-3-Vision**

Tunataka AI iweze kuchambua maudhui ya picha zetu na kutoa maelezo yanayofaa.

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

Tunaweza kupata majibu yanayofaa kwa kutekeleza script ifuatayo kwenye Notebook.

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. OCR kwa Kutumia Phi-3-Vision**

Mbali na kuchambua picha, tunaweza pia kutoa taarifa kutoka kwenye picha. Hii ni mchakato wa OCR ambao hapo awali tulihitaji kuandika msimbo mgumu kuukamilisha.

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

Matokeo ni

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. Kulinganisha Picha Nyingi**

Phi-3 Vision ina uwezo wa kulinganisha picha nyingi. Tunaweza kutumia mfano huu kutafuta tofauti kati ya picha.

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

Matokeo ni

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**Kanusho:**  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa maelezo muhimu, inashauriwa kutumia huduma za mtafsiri wa kibinadamu aliyebobea. Hatutawajibika kwa tafsiri zisizo sahihi au kutokuelewana kunakotokana na matumizi ya tafsiri hii.