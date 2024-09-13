# **Inférence Phi-3-Vision en Local**

Phi-3-vision-128k-instruct permet à Phi-3 non seulement de comprendre le langage, mais aussi de voir le monde visuellement. Grâce à Phi-3-vision-128k-instruct, nous pouvons résoudre différents problèmes visuels, tels que l'OCR, l'analyse de tableaux, la reconnaissance d'objets, la description d'images, etc. Nous pouvons facilement accomplir des tâches qui nécessitaient auparavant beaucoup de formation de données. Voici les techniques et scénarios d'application associés à Phi-3-vision-128k-instruct.



## **0. Préparation**

Veuillez vous assurer que les bibliothèques Python suivantes sont installées avant utilisation (Python 3.10+ est recommandé)


```bash

pip install transformers -U
pip install datasets -U
pip install torch -U

```

Il est recommandé d'utiliser ***CUDA 11.6+*** et d'installer flatten


```bash

pip install flash-attn --no-build-isolation

```

Créez un nouveau Notebook. Pour compléter les exemples, il est recommandé de créer d'abord le contenu suivant.


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


## **1. Analyser l'image avec Phi-3-Vision**

Nous voulons que l'IA puisse analyser le contenu de nos images et fournir des descriptions pertinentes.


```python

prompt = f"{user_prompt}<|image_1|>\nPourriez-vous me présenter cette action ?{prompt_suffix}{assistant_prompt}"


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

Nous pouvons obtenir les réponses pertinentes en exécutant le script suivant dans Notebook


```txt

Certainement ! Nvidia Corporation est un leader mondial de l'informatique avancée et de l'intelligence artificielle (IA). L'entreprise conçoit et développe des unités de traitement graphique (GPU), qui sont des accélérateurs matériels spécialisés utilisés pour traiter et rendre des images et des vidéos. Les GPU de Nvidia sont largement utilisés dans la visualisation professionnelle, les centres de données et les jeux. L'entreprise propose également des logiciels et des services pour améliorer les capacités de ses GPU. Les technologies innovantes de Nvidia ont des applications dans divers secteurs, notamment l'automobile, la santé et le divertissement. L'action de l'entreprise est cotée en bourse et peut être trouvée sur les principales places boursières.

```


## **2. OCR avec Phi-3-Vision**


En plus d'analyser l'image, nous pouvons également extraire des informations de l'image. C'est le processus OCR que nous devions auparavant coder de manière complexe pour le réaliser.


```python

prompt = f"{user_prompt}<|image_1|>\nAidez-moi à obtenir le titre et les informations sur l'auteur de ce livre ?{prompt_suffix}{assistant_prompt}"

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

Le résultat est


```txt

Le titre du livre est "ALONE" et l'auteur est Morgan Maxwell.

```

## **3. Comparaison de plusieurs images**

Phi-3 Vision prend en charge la comparaison de plusieurs images. Nous pouvons utiliser ce modèle pour trouver les différences entre les images.


```python

prompt = f"{user_prompt}<|image_1|>\n<|image_2|>\n Quelle est la différence entre ces deux images ?{prompt_suffix}{assistant_prompt}"

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


Le résultat est


```txt

La première image montre un groupe de joueurs de football du club Arsenal posant pour une photo d'équipe avec leurs trophées, tandis que la deuxième image montre un groupe de joueurs de football du club Arsenal célébrant une victoire avec une grande foule de fans en arrière-plan. La différence entre les deux images réside dans le contexte dans lequel les photos ont été prises, avec la première image centrée sur l'équipe et leurs trophées, et la deuxième image capturant un moment de célébration et de victoire.

```

Avertissement : La traduction a été réalisée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.