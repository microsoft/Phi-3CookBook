# **Inference Phi-3-Vision sa Lokal**

Ang Phi-3-vision-128k-instruct ay nagbibigay-daan sa Phi-3 na hindi lang maunawaan ang wika, kundi makita rin ang mundo gamit ang biswal na aspeto. Sa pamamagitan ng Phi-3-vision-128k-instruct, maaari nating lutasin ang iba't ibang biswal na problema, tulad ng OCR, pagsusuri ng mga talahanayan, pagkilala ng mga bagay, paglarawan ng larawan, at iba pa. Madali nating magagawa ang mga gawaing dati'y nangangailangan ng maraming pagsasanay sa datos. Ang mga sumusunod ay mga kaugnay na teknolohiya at senaryo ng aplikasyon na binanggit ng Phi-3-vision-128k-instruct.

## **0. Paghahanda**

Siguraduhing na-install na ang mga sumusunod na Python libraries bago gamitin (inirerekomenda ang Python 3.10+)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

Inirerekomenda ang paggamit ng ***CUDA 11.6+*** at pag-install ng flatten

```bash
pip install flash-attn --no-build-isolation
```

Gumawa ng bagong Notebook. Upang makumpleto ang mga halimbawa, inirerekomenda na likhain mo muna ang mga sumusunod na nilalaman.

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

## **1. Suriin ang larawan gamit ang Phi-3-Vision**

Nais natin na ang AI ay magkaroon ng kakayahang suriin ang nilalaman ng ating mga larawan at magbigay ng mga kaugnay na paglalarawan.

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

Makakakuha tayo ng mga kaugnay na sagot sa pamamagitan ng pagpapatakbo ng sumusunod na script sa Notebook.

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. OCR gamit ang Phi-3-Vision**

Bukod sa pagsusuri ng larawan, maaari rin tayong kumuha ng impormasyon mula sa larawan. Ito ang proseso ng OCR na dati'y nangangailangan ng pagsusulat ng komplikadong code upang magawa.

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

Ang resulta ay

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. Paghahambing ng maraming larawan**

Sinusuportahan ng Phi-3 Vision ang paghahambing ng maraming larawan. Maaari nating gamitin ang modelong ito upang hanapin ang mga pagkakaiba sa pagitan ng mga larawan.

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

Ang resulta ay

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI na nakabatay sa makina. Bagama't pinagsisikapan naming maging wasto, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-wika ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.