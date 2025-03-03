# **כימות משפחת Phi באמצעות הרחבות Generative AI ל-onnxruntime**

## **מהן הרחבות Generative AI ל-onnxruntime**

ההרחבות האלו מסייעות להריץ בינה מלאכותית גנרטיבית באמצעות ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). הן מספקות לולאת בינה מלאכותית גנרטיבית עבור מודלים של ONNX, כולל ביצוע חיזוי עם ONNX Runtime, עיבוד logits, חיפוש ודגימה, וניהול מטמון KV. מפתחים יכולים להשתמש בשיטת generate() ברמת על, או להריץ כל איטרציה של המודל בלולאה, וליצור טוקן אחד בכל פעם, עם אפשרות לעדכן את פרמטרי היצירה בתוך הלולאה. ההרחבות תומכות בחיפוש גרידי/קרן ובדגימה TopP, TopK ליצירת רצפי טוקנים, וכן בעיבוד logits מובנה כמו עונשים על חזרות. ניתן גם להוסיף דירוג מותאם אישית בקלות.

ברמת היישום, ניתן להשתמש בהרחבות Generative AI ל-onnxruntime כדי לבנות יישומים באמצעות C++/C#/Python. ברמת המודל, ניתן להשתמש בהן למיזוג מודלים מותאמים ולעבודות פריסה כמותיות קשורות.


## **כימות Phi-3.5 עם הרחבות Generative AI ל-onnxruntime**

### **מודלים נתמכים**

הרחבות Generative AI ל-onnxruntime תומכות בהמרת כימות של Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Model Builder בהרחבות Generative AI ל-onnxruntime**

ה-Model Builder מאיץ משמעותית את יצירת מודלים של ONNX מותאמים ומכוילים שמריצים את ה-API של ONNX Runtime generate().

באמצעות Model Builder, ניתן לכמת את המודל ל-INT4, INT8, FP16, FP32, ולשלב שיטות האצת חומרה שונות כגון CPU, CUDA, DirectML, Mobile ועוד.

כדי להשתמש ב-Model Builder יש להתקין

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

לאחר ההתקנה, ניתן להריץ את הסקריפט של Model Builder מהטרמינל כדי לבצע המרת פורמט וכימות של המודל.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

הבנת הפרמטרים הרלוונטיים:

1. **model_name** זהו המודל ב-Hugging Face, כגון microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct וכו'. זה יכול להיות גם הנתיב שבו שמור המודל.

2. **path_to_output_folder** נתיב השמירה של המרת הכימות.

3. **execution_provider** תמיכה בהאצת חומרה שונה, כגון cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** אנו מורידים את המודל מ-Hugging Face ומאחסנים אותו במטמון מקומי.


***הערה:***


## **כיצד להשתמש ב-Model Builder לכימות Phi-3.5**

Model Builder תומך כעת בכימות מודלים של ONNX עבור Phi-3.5 Instruct ו-Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**המרת כימות INT 4 מואצת CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**המרת כימות INT 4 מואצת CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. הגדרת סביבה בטרמינל:

```bash

mkdir models

cd models 

```

2. הורדת microsoft/Phi-3.5-vision-instruct לתיקיית models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. יש להוריד את הקבצים הבאים לתיקיית Phi-3.5-vision-instruct שלכם:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. הורידו את הקובץ הזה לתיקיית models:
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. גשו לטרמינל:

    המרת תמיכה של ONNX עם FP32:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **הערות:**

1. Model Builder תומך כרגע בהמרת Phi-3.5-Instruct ו-Phi-3.5-Vision, אך לא Phi-3.5-MoE.

2. כדי להשתמש במודל הכימות של ONNX, ניתן להשתמש בו באמצעות ה-SDK של Generative AI extensions ל-onnxruntime.

3. יש לשקול יותר אחריות בבינה מלאכותית, ולכן לאחר המרת כימות המודל, מומלץ לבצע בדיקות תוצאה יעילות יותר.

4. באמצעות כימות מודל CPU INT4, ניתן לפרוס אותו למכשירי קצה, מה שמציע תרחישי יישום טובים יותר. לכן, השלמנו את Phi-3.5-Instruct סביב INT 4.


## **משאבים**

1. למידע נוסף על Generative AI extensions ל-onnxruntime:
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. מאגר GitHub של Generative AI extensions ל-onnxruntime:
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. בעוד שאנו שואפים לדיוק, אנא היו מודעים לכך שתרגומים אוטומטיים עשויים לכלול טעויות או אי-דיוקים. יש לראות במסמך המקורי בשפתו המקורית כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו אחראים לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.