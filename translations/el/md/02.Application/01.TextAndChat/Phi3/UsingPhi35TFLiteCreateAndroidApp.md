# **Χρήση του Microsoft Phi-3.5 tflite για τη δημιουργία Android εφαρμογής**

Αυτό είναι ένα δείγμα εφαρμογής Android που χρησιμοποιεί τα μοντέλα Microsoft Phi-3.5 tflite.

## **📚 Γνώση**

Το Android LLM Inference API σας επιτρέπει να εκτελείτε μεγάλα μοντέλα γλώσσας (LLMs) εξ ολοκλήρου στη συσκευή για εφαρμογές Android. Μπορείτε να το χρησιμοποιήσετε για μια ευρεία γκάμα εργασιών, όπως τη δημιουργία κειμένου, την ανάκτηση πληροφοριών σε φυσική γλώσσα και τη σύνοψη εγγράφων. Η εργασία παρέχει ενσωματωμένη υποστήριξη για πολλά text-to-text μοντέλα γλώσσας, επιτρέποντάς σας να εφαρμόσετε τα πιο πρόσφατα μοντέλα γεννητικής AI στη συσκευή στις εφαρμογές σας Android.

Το Googld AI Edge Torch είναι μια βιβλιοθήκη python που υποστηρίζει τη μετατροπή PyTorch μοντέλων σε μορφή .tflite, η οποία μπορεί στη συνέχεια να εκτελεστεί με το TensorFlow Lite και το MediaPipe. Αυτό επιτρέπει τη δημιουργία εφαρμογών για Android, iOS και IoT που μπορούν να εκτελούν μοντέλα εξ ολοκλήρου στη συσκευή. Το AI Edge Torch προσφέρει ευρεία κάλυψη CPU, με αρχική υποστήριξη για GPU και NPU. Το AI Edge Torch επιδιώκει στενή ενσωμάτωση με το PyTorch, βασιζόμενο στο torch.export() και παρέχοντας καλή κάλυψη των Core ATen operators.

## **🪬 Οδηγίες**

### **🔥 Μετατροπή του Microsoft Phi-3.5 σε υποστήριξη tflite**

0. Αυτό το δείγμα είναι για Android 14+

1. Εγκαταστήστε το Python 3.10.12

***Πρόταση:*** Χρησιμοποιήστε το conda για την εγκατάσταση του περιβάλλοντος Python σας

2. Ubuntu 20.04 / 22.04 (εστιάστε στο [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Πρόταση:*** Χρησιμοποιήστε Azure Linux VM ή VM από τρίτους παρόχους για να δημιουργήσετε το περιβάλλον σας

3. Μεταβείτε στο Linux bash σας και εγκαταστήστε τη βιβλιοθήκη Python

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Κατεβάστε το Microsoft-3.5-Instruct από το Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Μετατρέψτε το Microsoft Phi-3.5 σε tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Μετατροπή του Microsoft Phi-3.5 σε Android Mediapipe Bundle**

Πρώτα εγκαταστήστε το mediapipe

```bash

pip install mediapipe

```

Εκτελέστε αυτόν τον κώδικα στο [σημειωματάριό σας](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Χρήση του adb push task model στη διαδρομή της συσκευής σας Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Εκτέλεση του κώδικα Android**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.el.png)

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες αυτόματης μετάφρασης με βάση την τεχνητή νοημοσύνη. Ενώ καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η έγκυρη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.