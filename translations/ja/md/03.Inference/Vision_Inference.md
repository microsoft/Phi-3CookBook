# **ローカルでのPhi-3-Vision推論**

Phi-3-vision-128k-instructは、Phi-3が言語を理解するだけでなく、視覚的にも世界を認識できるようにします。Phi-3-vision-128k-instructを通じて、OCR、テーブル解析、物体認識、画像の説明など、さまざまな視覚的問題を解決できます。以前は大量のデータトレーニングが必要だったタスクも簡単に完了できます。以下に、Phi-3-vision-128k-instructが引用する関連技術と応用シナリオを示します。

## **0. 準備**

使用前に以下のPythonライブラリがインストールされていることを確認してください（Python 3.10+を推奨）


```bash

pip install transformers -U
pip install datasets -U
pip install torch -U

```

***CUDA 11.6+***の使用を推奨し、flattenをインストールしてください


```bash

pip install flash-attn --no-build-isolation

```

新しいNotebookを作成します。例を完了するには、まず以下の内容を作成することをお勧めします。


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


## **1. Phi-3-Visionで画像を解析する**

AIが画像の内容を解析し、関連する説明を提供できるようにします


```python

prompt = f"{user_prompt}<|image_1|>\nこの株について紹介してもらえますか？{prompt_suffix}{assistant_prompt}"


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

Notebookで以下のスクリプトを実行することで、関連する回答を得ることができます


```txt

もちろんです！Nvidia Corporationは、高度なコンピューティングと人工知能（AI）の分野で世界をリードする企業です。Nvidiaは、画像やビデオの処理とレンダリングに特化したグラフィックス処理ユニット（GPU）を設計・開発しています。NvidiaのGPUは、プロフェッショナルビジュアライゼーション、データセンター、ゲーミングなどで広く使用されています。同社はまた、GPUの機能を強化するためのソフトウェアとサービスも提供しています。Nvidiaの革新的な技術は、自動車、医療、エンターテイメントなど、さまざまな産業で応用されています。同社の株式は主要な株式市場で公開取引されています。

```


## **2. Phi-3-VisionでのOCR**

画像の解析に加えて、画像から情報を抽出することもできます。これがOCRプロセスであり、以前は複雑なコードを書く必要がありました。


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

## **3. 複数画像の比較**

Phi-3 Visionは複数の画像の比較をサポートしています。このモデルを使用して画像間の違いを見つけることができます。


```python

prompt = f"{user_prompt}<|image_1|>\n<|image_2|>\nこの2つの画像の違いは何ですか？{prompt_suffix}{assistant_prompt}"

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

最初の画像は、アーセナルフットボールクラブのサッカー選手がトロフィーと一緒にチーム写真を撮っている様子を示しており、2番目の画像は、アーセナルフットボールクラブのサッカー選手が大勢のファンと一緒に勝利を祝っている様子を示しています。2つの画像の違いは、写真が撮影された状況にあります。最初の画像はチームとそのトロフィーに焦点を当てており、2番目の画像は祝勝と勝利の瞬間を捉えています。

```

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完全ではない可能性があります。
出力を確認し、必要な修正を行ってください。