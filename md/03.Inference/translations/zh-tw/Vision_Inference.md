# **在本地推論 Phi-3-Vision**

Phi-3-vision-128k-instruct 允許 Phi-3 不僅理解語言，還能視覺化地看見世界。通過 Phi-3-vision-128k-instruct，我們可以解決不同的視覺問題，例如 OCR、表格分析、物件識別、描述圖片等。我們可以輕鬆完成以前需要大量數據訓練的任務。以下是 Phi-3-vision-128k-instruct 引用的相關技術和應用場景。

## **0. 準備**

請確保在使用前已安裝以下 Python 函式庫（建議使用 Python 3.10+）

```bash

pip install transformers -U
pip install datasets -U
pip install torch -U

```

建議使用 ***CUDA 11.6+*** 並安裝 flatten

```bash

pip install flash-attn --no-build-isolation

```

建立一個新的 Notebook。要完成這些範例，建議您先建立以下內容。

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

## **1. 使用 Phi-3-Vision 分析圖像**

我們希望 AI 能夠分析我們圖片的內容並給出相關描述

```python

prompt = f"{user_prompt}<|image_1|>\n你可以向我介紹這支股票嗎？{prompt_suffix}{assistant_prompt}"

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

我們可以通過在 Notebook 中執行以下腳本來獲取相關答案

```txt

當然可以！Nvidia Corporation 是先進運算和人工智慧（AI）領域的全球領導者。該公司設計和開發圖形處理單元（GPUs），這些是用於處理和渲染圖像和影片的專用硬體加速器。Nvidia 的 GPUs 被廣泛應用於專業視覺化、資料中心和遊戲領域。該公司還提供軟體和服務，以增強其 GPUs 的功能。Nvidia 的創新技術在各行各業中都有應用，包括汽車、醫療保健和娛樂。該公司的股票是公開交易的，可以在主要的股票交易所找到。

```

## **2. 使用 Phi-3-Vision 進行 OCR**

除了分析影像之外，我們還可以從影像中提取資訊。這是我們以前需要編寫複雜程式碼才能完成的 OCR 過程。

```python

prompt = f"{user_prompt}<|image_1|>\n幫我獲取這本書的標題和作者資訊?{prompt_suffix}{assistant_prompt}"

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

結果是

```txt

這本書的書名是 "ALONE"，作者是 Morgan Maxwell。

```

## **3. 多張圖片的比較**

Phi-3 Vision 支援多張影像的比較。我們可以使用此模型來找出影像之間的差異。

```python

prompt = f"{user_prompt}<|image_1|>\n<|image_2|>\n 這兩張圖片有什麼不同？{prompt_suffix}{assistant_prompt}"

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

結果是

```txt

第一張圖片顯示了一群來自阿森納足球俱樂部的足球運動員與他們的獎盃一起拍攝團隊照片，而第二張圖片顯示了一群來自阿森納足球俱樂部的足球運動員在背景中與大量球迷一起慶祝勝利。兩張圖片之間的區別在於拍攝照片的背景，第一張圖片側重於團隊和他們的獎盃，第二張圖片捕捉到了慶祝和勝利的時刻。

```

