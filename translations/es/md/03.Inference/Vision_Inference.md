# **Inferencia de Phi-3-Vision en Local**

Phi-3-vision-128k-instruct permite a Phi-3 no solo entender el lenguaje, sino también ver el mundo visualmente. A través de Phi-3-vision-128k-instruct, podemos resolver diferentes problemas visuales, como OCR, análisis de tablas, reconocimiento de objetos, descripción de imágenes, etc. Podemos completar fácilmente tareas que anteriormente requerían mucho entrenamiento de datos. A continuación se presentan técnicas relacionadas y escenarios de aplicación citados por Phi-3-vision-128k-instruct.

## **0. Preparación**

Por favor, asegúrate de tener instaladas las siguientes bibliotecas de Python antes de usar (se recomienda Python 3.10+)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

Se recomienda usar ***CUDA 11.6+*** e instalar flatten

```bash
pip install flash-attn --no-build-isolation
```

Crea un nuevo Notebook. Para completar los ejemplos, se recomienda que primero crees el siguiente contenido.

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

## **1. Analizar la imagen con Phi-3-Vision**

Queremos que la IA pueda analizar el contenido de nuestras imágenes y dar descripciones relevantes.

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

Podemos obtener las respuestas relevantes ejecutando el siguiente script en el Notebook

```txt
¡Por supuesto! Nvidia Corporation es un líder global en computación avanzada e inteligencia artificial (IA). La compañía diseña y desarrolla unidades de procesamiento gráfico (GPUs), que son aceleradores de hardware especializados utilizados para procesar y renderizar imágenes y videos. Las GPUs de Nvidia son ampliamente utilizadas en visualización profesional, centros de datos y videojuegos. La compañía también proporciona software y servicios para mejorar las capacidades de sus GPUs. Las tecnologías innovadoras de Nvidia tienen aplicaciones en diversas industrias, incluyendo automotriz, salud y entretenimiento. Las acciones de la compañía se cotizan públicamente y se pueden encontrar en las principales bolsas de valores.
```

## **2. OCR con Phi-3-Vision**

Además de analizar la imagen, también podemos extraer información de la imagen. Este es el proceso de OCR que antes necesitábamos escribir código complejo para completar.

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

El resultado es

```txt
El título del libro es "ALONE" y el autor es Morgan Maxwell.
```

## **3. Comparación de múltiples imágenes**

Phi-3 Vision soporta la comparación de múltiples imágenes. Podemos usar este modelo para encontrar las diferencias entre las imágenes.

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

El resultado es

```txt
La primera imagen muestra a un grupo de jugadores de fútbol del Arsenal Football Club posando para una foto de equipo con sus trofeos, mientras que la segunda imagen muestra a un grupo de jugadores de fútbol del Arsenal Football Club celebrando una victoria con una gran multitud de fanáticos en el fondo. La diferencia entre las dos imágenes es el contexto en el que se tomaron las fotos, con la primera imagen enfocándose en el equipo y sus trofeos, y la segunda imagen capturando un momento de celebración y victoria.
```

Aviso legal: La traducción fue realizada a partir del original por un modelo de IA y puede no ser perfecta. Por favor, revise el resultado y haga las correcciones necesarias.