# **ローカルでPhi-3-Visionを推論する**

Phi-3-vision-128k-instructは、Phi-3が言語を理解するだけでなく、視覚的に世界を見ることを可能にします。Phi-3-vision-128k-instructを使用すると、OCR、表の分析、物体認識、画像の説明など、さまざまな視覚的な問題を解決できます。以前は大量のデータトレーニングが必要だったタスクを簡単に完了できます。以下は、Phi-3-vision-128k-instructが引用する関連技術とアプリケーションシナリオです。

## **0. 準備**

使用前に、以下のPythonライブラリがインストールされていることを確認してください（Python 3.10+を推奨）。


```bash

pip install transformers -U
pip install datasets -U
pip install torch -U

```

***CUDA 11.6+***を使用し、flattenをインストールすることをお勧めします。


```bash

pip install flash-attn --no-build-isolation

```

新しいNotebookを作成します。例を完了するには、最初に以下の内容を作成することをお勧めします。


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


## **1. Phi-3-Visionで画像を分析する**

AIが画像の内容を分析し、関連する説明を提供できるようにしたいと考えています。


```python

prompt = f"{user_prompt}<|image_1|>\nこの株について紹介してください。{prompt_suffix}{assistant_prompt}"


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

Notebookで以下のスクリプトを実行して、関連する回答を取得できます。


```txt

もちろんです！Nvidia Corporationは、先進的なコンピューティングと人工知能（AI）の分野で世界をリードする企業です。同社は、画像やビデオの処理とレンダリングに使用される特殊なハードウェアアクセラレータであるグラフィックス処理ユニット（GPU）を設計および開発しています。NvidiaのGPUは、プロフェッショナルなビジュアライゼーション、データセンター、ゲームで広く使用されています。同社はまた、GPUの機能を強化するためのソフトウェアとサービスも提供しています。Nvidiaの革新的な技術は、自動車、医療、エンターテイメントなど、さまざまな業界で応用されています。同社の株式は公開取引されており、主要な株式市場で見つけることができます。

```


## **2. Phi-3-Visionを使用したOCR**


画像の分析に加えて、画像から情報を抽出することもできます。これは、以前は複雑なコードを記述する必要があったOCRプロセスです。


```python

prompt = f"{user_prompt}<|image_1|>\nこの本のタイトルと著者情報を教えてください。{prompt_suffix}{assistant_prompt}"

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

結果は以下の通りです


```txt

本のタイトルは「ALONE」で、著者はMorgan Maxwellです。

```

## **3. 複数の画像の比較**

Phi-3 Visionは、複数の画像の比較をサポートしています。このモデルを使用して、画像間の違いを見つけることができます。


```python

prompt = f"{user_prompt}<|image_1|>\n<|image_2|>\n この2つの画像の違いは何ですか？{prompt_suffix}{assistant_prompt}"

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


結果は以下の通りです


```txt

最初の画像は、アーセナルフットボールクラブのサッカー選手たちがトロフィーと一緒にチーム写真を撮っている様子を示しており、2番目の画像は、アーセナルフットボールクラブのサッカー選手たちが大勢のファンと一緒に勝利を祝っている様子を示しています。2つの画像の違いは、写真が撮影された背景にあり、最初の画像はチームとトロフィーに焦点を当てており、2番目の画像は祝賀と勝利の瞬間を捉えています。

```
