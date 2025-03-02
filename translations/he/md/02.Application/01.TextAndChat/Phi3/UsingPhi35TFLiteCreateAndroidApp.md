# **שימוש ב-Microsoft Phi-3.5 tflite ליצירת אפליקציית אנדרואיד**

זהו דוגמה לאנדרואיד המשתמשת במודלים של Microsoft Phi-3.5 tflite.

## **📚 ידע**

Android LLM Inference API מאפשר להריץ מודלים גדולים לעיבוד שפה (LLMs) באופן מלא על המכשיר עבור אפליקציות אנדרואיד. ניתן להשתמש בהם לביצוע מגוון רחב של משימות, כמו יצירת טקסט, שליפת מידע בצורה טבעית וסיכום מסמכים. ה-API תומך באופן מובנה במודלים גדולים של טקסט לטקסט, כך שתוכלו ליישם את המודלים העדכניים ביותר של בינה מלאכותית על המכשיר באפליקציות שלכם.

Google AI Edge Torch הוא ספריית פייתון שתומכת בהמרת מודלים של PyTorch לפורמט .tflite, שניתן להריץ עם TensorFlow Lite ו-MediaPipe. זה מאפשר יישומים עבור אנדרואיד, iOS ו-IoT שיכולים להריץ מודלים באופן מלא על המכשיר. AI Edge Torch מציע תמיכה רחבה במעבדים (CPU), עם תמיכה ראשונית ב-GPU ו-NPU. AI Edge Torch שואף להשתלב באופן הדוק עם PyTorch, מבוסס על torch.export() ומספק כיסוי רחב של Core ATen operators.

## **🪬 הנחיות**

### **🔥 המרת Microsoft Phi-3.5 לתמיכה ב-tflite**

0. דוגמה זו מיועדת לאנדרואיד 14+

1. התקן Python 3.10.12

***הצעה:*** להשתמש ב-conda להתקנת סביבת הפייתון שלך

2. Ubuntu 20.04 / 22.04 (אנא התמקדו ב-[google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***הצעה:*** להשתמש ב-Azure Linux VM או ב-VM של ספק צד שלישי ליצירת הסביבה שלך

3. גשו ל-bash בלינוקס שלכם, להתקנת ספריית פייתון

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. הורידו את Microsoft-3.5-Instruct מ-Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. המירו את Microsoft Phi-3.5 ל-tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 המרת Microsoft Phi-3.5 לחבילת Mediapipe לאנדרואיד**

ראשית התקינו את mediapipe

```bash

pip install mediapipe

```

הריצו את הקוד הזה ב-[ה-notebook שלכם](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 שימוש ב-adb push להעברת מודל המשימה לנתיב במכשיר האנדרואיד שלכם**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 הרצת קוד האנדרואיד שלכם**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.he.png)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים לכלול שגיאות או אי-דיוקים. יש להתייחס למסמך המקורי בשפתו המקורית כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום אנושי מקצועי. איננו אחראים לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.