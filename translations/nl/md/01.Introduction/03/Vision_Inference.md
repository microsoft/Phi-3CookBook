# **Inference Phi-3-Vision lokaal**

Phi-3-vision-128k-instruct stelt Phi-3 in staat om niet alleen taal te begrijpen, maar ook de wereld visueel te zien. Met Phi-3-vision-128k-instruct kunnen we verschillende visuele problemen oplossen, zoals OCR, tabelanalyse, objectherkenning, het beschrijven van afbeeldingen, enzovoort. We kunnen eenvoudig taken uitvoeren die eerder veel datatraining vereisten. Hieronder staan de gerelateerde technieken en toepassingsscenario's die door Phi-3-vision-128k-instruct worden gebruikt.

## **0. Voorbereiding**

Zorg ervoor dat de volgende Python-bibliotheken zijn geïnstalleerd voordat je begint (Python 3.10+ wordt aanbevolen)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

Het wordt aanbevolen om ***CUDA 11.6+*** te gebruiken en flatten te installeren

```bash
pip install flash-attn --no-build-isolation
```

Maak een nieuw Notebook aan. Om de voorbeelden te voltooien, wordt aanbevolen om eerst de volgende inhoud te creëren.

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

## **1. Analyseer de afbeelding met Phi-3-Vision**

We willen dat AI de inhoud van onze afbeeldingen kan analyseren en relevante beschrijvingen kan geven.

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

We kunnen de relevante antwoorden verkrijgen door het volgende script in Notebook uit te voeren.

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. OCR met Phi-3-Vision**

Naast het analyseren van de afbeelding kunnen we ook informatie uit de afbeelding halen. Dit is het OCR-proces dat we vroeger met complexe code moesten voltooien.

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

Het resultaat is

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. Vergelijking van meerdere afbeeldingen**

Phi-3 Vision ondersteunt het vergelijken van meerdere afbeeldingen. Met dit model kunnen we de verschillen tussen afbeeldingen vinden.

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

Het resultaat is

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**Disclaimer**:  
Dit document is vertaald met behulp van AI-gestuurde vertaaldiensten. Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet verantwoordelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.