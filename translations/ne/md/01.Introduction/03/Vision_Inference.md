# **स्थानीय रूपमा Phi-3-Vision को इनफरेन्स गर्नुहोस्**

Phi-3-vision-128k-instruct ले Phi-3 लाई भाषाको मात्र बुझाइ नभई दृश्य रूपमा संसारलाई हेर्न पनि सक्षम बनाउँछ। Phi-3-vision-128k-instruct को माध्यमबाट हामी विभिन्न दृश्य समस्याहरू समाधान गर्न सक्छौं, जस्तै OCR, तालिका विश्लेषण, वस्तु पहिचान, चित्र वर्णन आदि। यसले पहिला धेरै डाटा तालिम आवश्यक पर्ने कामहरू सजिलै पूरा गर्न सक्षम बनाउँछ। तल Phi-3-vision-128k-instruct द्वारा उद्धृत सम्बन्धित प्रविधिहरू र अनुप्रयोग परिदृश्यहरू छन्।  

## **0. तयारी**

प्रयोग गर्नु अघि कृपया तलका Python पुस्तकालयहरू स्थापना भएको सुनिश्चित गर्नुहोस् (Python 3.10+ सिफारिस गरिन्छ)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** प्रयोग गर्न सिफारिस गरिन्छ र flatten स्थापना गर्नुहोस्

```bash
pip install flash-attn --no-build-isolation
```

नयाँ Notebook सिर्जना गर्नुहोस्। उदाहरणहरू पूरा गर्न, तपाईंले निम्न सामग्री पहिले सिर्जना गर्नुहोस् भन्ने सिफारिस गरिन्छ।

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

## **1. Phi-3-Vision को साथ चित्रको विश्लेषण गर्नुहोस्**

हामी चाहन्छौं कि AI ले हाम्रो तस्बिरहरूको सामग्री विश्लेषण गरोस् र सम्बन्धित विवरणहरू प्रदान गरोस्।

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

Notebook मा निम्न स्क्रिप्ट कार्यान्वयन गरेर हामी सम्बन्धित उत्तरहरू प्राप्त गर्न सक्छौं।

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Vision को साथ OCR**

चित्र विश्लेषण गर्न बाहेक, हामी चित्रबाट जानकारी पनि निकाल्न सक्छौं। यो OCR प्रक्रिया हो, जसलाई पहिला जटिल कोड लेख्न आवश्यक थियो।

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

परिणाम हो

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. धेरै तस्बिरहरूको तुलना**

Phi-3 Vision ले धेरै तस्बिरहरूको तुलना समर्थन गर्दछ। हामी यस मोडललाई तस्बिरहरू बीचका भिन्नताहरू पत्ता लगाउन प्रयोग गर्न सक्छौं।

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

परिणाम हो

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```  

**अस्वीकरण**:  
यो दस्तावेज़ मेसिन-आधारित एआई अनुवाद सेवाहरू प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयास गर्दछौं, तर कृपया जानकार रहनुहोस् कि स्वचालित अनुवादहरूले त्रुटिहरू वा असत्यताहरू समावेश गर्न सक्छ। यसको मूल भाषामा रहेको मूल दस्तावेजलाई प्राधिकृत स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवादको सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुनेछैनौं।