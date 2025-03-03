# **Tworzenie aplikacji na Androida z wykorzystaniem Microsoft Phi-3.5 tflite**

To jest przykład aplikacji na Androida wykorzystującej modele Microsoft Phi-3.5 tflite.

## **📚 Wiedza**

Android LLM Inference API pozwala uruchamiać duże modele językowe (LLM) bezpośrednio na urządzeniu w aplikacjach na Androida. Możesz je wykorzystać do wykonywania różnorodnych zadań, takich jak generowanie tekstu, wyszukiwanie informacji w formie naturalnego języka czy podsumowywanie dokumentów. API zapewnia wbudowaną obsługę wielu modeli tekst-tekst, dzięki czemu możesz zastosować najnowsze modele generatywnej sztucznej inteligencji na swoich urządzeniach z Androidem.

Googld AI Edge Torch to biblioteka w Pythonie, która wspiera konwersję modeli PyTorch na format .tflite, który następnie można uruchamiać za pomocą TensorFlow Lite i MediaPipe. Umożliwia to tworzenie aplikacji na Androida, iOS oraz IoT, które mogą działać całkowicie na urządzeniu. AI Edge Torch oferuje szerokie wsparcie dla CPU, a także początkowe wsparcie dla GPU i NPU. AI Edge Torch dąży do ścisłej integracji z PyTorch, bazując na torch.export() i zapewniając szerokie pokrycie dla operatorów Core ATen.

## **🪬 Wytyczne**

### **🔥 Konwersja Microsoft Phi-3.5 do obsługi tflite**

0. Ten przykład dotyczy Androida 14+

1. Zainstaluj Python 3.10.12

***Sugestia:*** użyj conda do instalacji środowiska Pythona

2. Ubuntu 20.04 / 22.04 (skup się na [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Sugestia:*** użyj Azure Linux VM lub zewnętrznej chmury do stworzenia środowiska

3. Przejdź do terminala Linux, aby zainstalować bibliotekę Pythona 

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Pobierz Microsoft-3.5-Instruct z Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Przekonwertuj Microsoft Phi-3.5 na tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Konwersja Microsoft Phi-3.5 do Android Mediapipe Bundle**

Najpierw zainstaluj MediaPipe

```bash

pip install mediapipe

```

Uruchom ten kod w [swoim notebooku](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Przesyłanie modelu za pomocą adb push na urządzenie z Androidem**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Uruchamianie kodu na Androidzie**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.pl.png)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku kluczowych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.