# **Utiliser Microsoft Phi-3.5 tflite pour créer une application Android**

Ceci est un exemple Android utilisant les modèles Microsoft Phi-3.5 tflite.

## **📚 Connaissances**

L'API d'inférence LLM pour Android vous permet d'exécuter des modèles de langage de grande taille (LLM) entièrement sur l'appareil pour des applications Android. Vous pouvez l'utiliser pour effectuer une large gamme de tâches, comme générer du texte, récupérer des informations sous forme de langage naturel et résumer des documents. Cette fonctionnalité offre un support intégré pour plusieurs modèles de langage de grande taille text-to-text, vous permettant d'appliquer les derniers modèles d'IA générative sur l'appareil à vos applications Android.

Googld AI Edge Torch est une bibliothèque Python qui permet de convertir des modèles PyTorch au format .tflite, qui peut ensuite être exécuté avec TensorFlow Lite et MediaPipe. Cela permet de créer des applications pour Android, iOS et IoT capables d'exécuter des modèles entièrement sur l'appareil. AI Edge Torch offre une large couverture CPU, avec un support initial pour GPU et NPU. AI Edge Torch vise à s'intégrer étroitement avec PyTorch, en s'appuyant sur torch.export() et en offrant une bonne couverture des opérateurs Core ATen.

## **🪬 Instructions**

### **🔥 Convertir Microsoft Phi-3.5 en support tflite**

0. Cet exemple est pour Android 14+

1. Installez Python 3.10.12

***Suggestion :*** utilisez conda pour installer votre environnement Python

2. Ubuntu 20.04 / 22.04 (veuillez vous concentrer sur [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Suggestion :*** utilisez une machine virtuelle Azure Linux ou une machine virtuelle cloud tierce pour créer votre environnement

3. Accédez à votre terminal Linux pour installer la bibliothèque Python 

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Téléchargez Microsoft-3.5-Instruct depuis Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Convertissez Microsoft Phi-3.5 en tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Convertir Microsoft Phi-3.5 en Bundle Android Mediapipe**

Veuillez installer Mediapipe en premier lieu

```bash

pip install mediapipe

```

Exécutez ce code dans [votre notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Utiliser adb pour transférer le modèle de tâche sur le chemin de vos appareils Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Exécuter votre code Android**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.fr.png)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous fassions de notre mieux pour garantir l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.