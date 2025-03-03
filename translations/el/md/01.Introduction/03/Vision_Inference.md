# **Εκτέλεση του Phi-3-Vision Τοπικά**

Το Phi-3-vision-128k-instruct επιτρέπει στο Phi-3 όχι μόνο να κατανοεί τη γλώσσα, αλλά και να βλέπει τον κόσμο οπτικά. Μέσω του Phi-3-vision-128k-instruct, μπορούμε να λύσουμε διάφορα οπτικά προβλήματα, όπως OCR, ανάλυση πινάκων, αναγνώριση αντικειμένων, περιγραφή εικόνων κ.λπ. Μπορούμε εύκολα να ολοκληρώσουμε εργασίες που παλαιότερα απαιτούσαν εκτενή εκπαίδευση δεδομένων. Ακολουθούν σχετικές τεχνικές και σενάρια εφαρμογής που αναφέρονται από το Phi-3-vision-128k-instruct.

## **0. Προετοιμασία**

Βεβαιωθείτε ότι έχουν εγκατασταθεί οι παρακάτω βιβλιοθήκες Python πριν τη χρήση (συνιστάται Python 3.10+)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

Συνιστάται η χρήση ***CUDA 11.6+*** και η εγκατάσταση του flatten

```bash
pip install flash-attn --no-build-isolation
```

Δημιουργήστε ένα νέο Notebook. Για να ολοκληρώσετε τα παραδείγματα, συνιστάται να δημιουργήσετε πρώτα το παρακάτω περιεχόμενο.

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

## **1. Ανάλυση εικόνας με το Phi-3-Vision**

Θέλουμε η τεχνητή νοημοσύνη να μπορεί να αναλύει το περιεχόμενο των εικόνων μας και να παρέχει σχετικές περιγραφές.

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

Μπορούμε να λάβουμε τις σχετικές απαντήσεις εκτελώντας το παρακάτω script στο Notebook.

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. OCR με το Phi-3-Vision**

Εκτός από την ανάλυση της εικόνας, μπορούμε επίσης να εξάγουμε πληροφορίες από την εικόνα. Αυτή είναι η διαδικασία OCR, την οποία παλαιότερα έπρεπε να ολοκληρώσουμε γράφοντας πολύπλοκο κώδικα.

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

Το αποτέλεσμα είναι

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. Σύγκριση πολλαπλών εικόνων**

Το Phi-3 Vision υποστηρίζει τη σύγκριση πολλαπλών εικόνων. Μπορούμε να χρησιμοποιήσουμε αυτό το μοντέλο για να βρούμε τις διαφορές μεταξύ των εικόνων.

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

Το αποτέλεσμα είναι

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**Αποποίηση Ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες μετάφρασης με βάση την τεχνητή νοημοσύνη. Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε καμία ευθύνη για τυχόν παρεξηγήσεις ή παρερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.