# **Usando Microsoft Phi-3.5 tflite para criar um aplicativo Android**

Este é um exemplo de Android utilizando modelos tflite do Microsoft Phi-3.5.

## **📚 Conhecimento**

A API de Inferência LLM para Android permite executar modelos de linguagem de grande escala (LLMs) completamente no dispositivo para aplicativos Android, os quais você pode usar para realizar uma ampla gama de tarefas, como gerar texto, recuperar informações em linguagem natural e resumir documentos. A tarefa oferece suporte integrado para vários modelos de linguagem grandes baseados em texto, permitindo que você aplique os mais recentes modelos de IA generativa no dispositivo aos seus aplicativos Android.

Google AI Edge Torch é uma biblioteca em Python que suporta a conversão de modelos PyTorch para o formato .tflite, que pode ser executado com TensorFlow Lite e MediaPipe. Isso possibilita aplicações para Android, iOS e IoT que podem executar modelos completamente no dispositivo. O AI Edge Torch oferece ampla cobertura de CPU, com suporte inicial para GPU e NPU. O AI Edge Torch busca integrar-se estreitamente com o PyTorch, construindo sobre o torch.export() e fornecendo uma boa cobertura dos operadores Core ATen.

## **🪬 Diretrizes**

### **🔥 Converter Microsoft Phi-3.5 para suporte tflite**

0. Este exemplo é para Android 14+

1. Instale o Python 3.10.12

***Sugestão:*** usar conda para instalar seu ambiente Python

2. Ubuntu 20.04 / 22.04 (por favor, foque no [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Sugestão:*** Usar uma VM Linux do Azure ou uma VM de terceiros na nuvem para criar seu ambiente

3. Acesse seu bash no Linux para instalar a biblioteca Python

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Baixe o Microsoft-3.5-Instruct do Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Converta o Microsoft Phi-3.5 para tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Converter Microsoft Phi-3.5 para Android Mediapipe Bundle**

Por favor, instale o mediapipe primeiro

```bash

pip install mediapipe

```

Execute este código em [seu notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Usando adb push para transferir o modelo de tarefa para o caminho do seu dispositivo Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Executando seu código Android**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.pt.png)

**Aviso Legal**:  
Este documento foi traduzido usando serviços de tradução automatizada por IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.