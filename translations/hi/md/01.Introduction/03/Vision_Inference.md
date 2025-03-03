# **लोकल में Phi-3-Vision का उपयोग**

Phi-3-vision-128k-instruct Phi-3 को केवल भाषा समझने तक सीमित नहीं रखता, बल्कि उसे दुनिया को दृश्य रूप से देखने में भी सक्षम बनाता है। Phi-3-vision-128k-instruct के माध्यम से, हम विभिन्न दृश्य समस्याओं को हल कर सकते हैं, जैसे OCR, टेबल विश्लेषण, ऑब्जेक्ट पहचान, चित्र का वर्णन आदि। हम उन कार्यों को आसानी से पूरा कर सकते हैं, जिनके लिए पहले बहुत अधिक डेटा प्रशिक्षण की आवश्यकता होती थी। नीचे Phi-3-vision-128k-instruct द्वारा उद्धृत संबंधित तकनीकें और अनुप्रयोग परिदृश्य दिए गए हैं।

## **0. तैयारी**

कृपया सुनिश्चित करें कि उपयोग से पहले निम्नलिखित Python लाइब्रेरी इंस्टॉल की गई हों (Python 3.10+ की सिफारिश की जाती है)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

***CUDA 11.6+*** का उपयोग करने और flatten इंस्टॉल करने की सिफारिश की जाती है।

```bash
pip install flash-attn --no-build-isolation
```

एक नया Notebook बनाएं। उदाहरणों को पूरा करने के लिए, यह सिफारिश की जाती है कि आप पहले निम्नलिखित सामग्री बनाएं।

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

## **1. Phi-3-Vision के साथ छवि का विश्लेषण करें**

हम चाहते हैं कि AI हमारी तस्वीरों की सामग्री का विश्लेषण कर सके और प्रासंगिक विवरण प्रदान कर सके।

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

हम Notebook में निम्नलिखित स्क्रिप्ट को निष्पादित करके प्रासंगिक उत्तर प्राप्त कर सकते हैं।

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. Phi-3-Vision के साथ OCR**

छवि का विश्लेषण करने के अलावा, हम छवि से जानकारी भी निकाल सकते हैं। यह OCR प्रक्रिया है, जिसे पहले पूरा करने के लिए जटिल कोड लिखने की आवश्यकता होती थी।

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

परिणाम है

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. कई छवियों की तुलना**

Phi-3 Vision कई छवियों की तुलना का समर्थन करता है। हम इस मॉडल का उपयोग छवियों के बीच अंतर खोजने के लिए कर सकते हैं।

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

परिणाम है

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**अस्वीकरण**:  
यह दस्तावेज़ मशीन-आधारित एआई अनुवाद सेवाओं का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल दस्तावेज़, जो इसकी मूल भाषा में है, को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।