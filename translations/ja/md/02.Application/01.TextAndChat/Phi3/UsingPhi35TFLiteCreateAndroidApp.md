# **Microsoft Phi-3.5 tflite を使用して Android アプリを作成する**

このサンプルは、Microsoft Phi-3.5 tflite モデルを使用した Android アプリケーションの例です。

## **📚 知識**

Android LLM Inference API を使用すると、大規模言語モデル（LLM）を完全にオンデバイスで Android アプリケーションに実装できます。これにより、テキスト生成、自然言語形式での情報取得、ドキュメント要約など、幅広いタスクを実行できます。このタスクでは、複数のテキスト対テキストの大規模言語モデルをサポートしており、最新のオンデバイス生成型 AI モデルを Android アプリに適用できます。

Google AI Edge Torch は、PyTorch モデルを .tflite フォーマットに変換することをサポートする Python ライブラリであり、その後 TensorFlow Lite や MediaPipe で実行できます。これにより、Android、iOS、および IoT 向けのアプリケーションが完全にオンデバイスでモデルを実行できるようになります。AI Edge Torch は広範な CPU サポートを提供し、初期段階では GPU と NPU のサポートも備えています。AI Edge Torch は PyTorch と密接に統合することを目指しており、torch.export() を基盤に構築され、Core ATen オペレーターの優れたサポートを提供します。

## **🪬 ガイドライン**

### **🔥 Microsoft Phi-3.5 を tflite に変換する手順**

0. このサンプルは Android 14+ に対応しています。

1. Python 3.10.12 をインストールします。

***提案:*** conda を使用して Python 環境をインストールすることをお勧めします。

2. Ubuntu 20.04 / 22.04 を使用します（[google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) に注目してください）。

***提案:*** Azure Linux VM やサードパーティのクラウド VM を使用して環境を構築することをお勧めします。

3. Linux bash に移動し、Python ライブラリをインストールします。

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging Face から Microsoft-3.5-Instruct をダウンロードします。

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5 を tflite に変換します。

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 を Android Mediapipe バンドルに変換する手順**

最初に mediapipe をインストールしてください。

```bash

pip install mediapipe

```

以下のコードを [your notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) で実行します。

```python

import mediapipe as mp
from mediapipe.tasks.python.genai import bundler

config = bundler.BundleConfig(
    tflite_model='Your Phi-3.5 tflite model path',
    tokenizer_model='Your Phi-3.5 tokenizer model path',
    start_token='start_token',
    stop_tokens=[STOP_TOKENS],
    output_filename='Your Phi-3.5 task model path',
    enable_bytes_to_unicode_mapping=True or Flase,
)
bundler.create_bundle(config)

```

### **🔥 adb を使用してタスクモデルを Android デバイスのパスにプッシュする**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Android コードを実行する**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.ja.png)

**免責事項**:  
この文書は、AIによる機械翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があります。原文（元の言語で記載された文書）が正式な情報源として考慮されるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用により生じた誤解や解釈の相違について、当方は一切の責任を負いません。