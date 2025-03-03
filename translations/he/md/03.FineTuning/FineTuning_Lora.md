# **כיוונון עדין של Phi-3 עם LoRA**

כיוונון עדין של מודל השפה Phi-3 Mini של מיקרוסופט באמצעות [LoRA (התאמה בדירוג נמוך)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) על בסיס נתונים מותאם להוראות צ'אט.

LoRA תסייע לשפר את הבנת השיחה ויצירת התגובות.

## מדריך שלב אחר שלב לכיוונון עדין של Phi-3 Mini:

**ייבוא והגדרות**

התקנת loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

תחילה יש לייבא ספריות נחוצות כמו datasets, transformers, peft, trl, ו-torch.  
הגדירו לוגינג כדי לעקוב אחר תהליך האימון.

ניתן להתאים שכבות מסוימות על ידי החלפתן בגרסאות מקבילות המיושמות ב-loralib. כרגע נתמכות רק nn.Linear, nn.Embedding, ו-nn.Conv2d. בנוסף, קיימת תמיכה ב-MergedLinear עבור מקרים שבהם nn.Linear יחיד מייצג יותר משכבה אחת, כמו ביישומים מסוימים של qkv projection במנגנון תשומת הלב (ראו הערות נוספות לפרטים).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

לפני תחילת לולאת האימון, סמנו רק את הפרמטרים של LoRA כניתנים לאימון.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

בעת שמירת נקודת ביקורת, צרו state_dict שמכיל רק את הפרמטרים של LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

בעת טעינת נקודת ביקורת באמצעות load_state_dict, הקפידו להגדיר strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

כעת ניתן להמשיך באימון כרגיל.

**היפרפרמטרים**

הגדירו שני מילונים: training_config ו-peft_config.  
training_config כולל היפרפרמטרים לאימון, כמו קצב למידה, גודל אצווה, והגדרות לוגינג.

peft_config מגדיר פרמטרים הקשורים ל-LoRA כמו דירוג, dropout, וסוג המשימה.

**טעינת מודל וטוקניזר**

ציינו את הנתיב למודל Phi-3 המוכשר מראש (לדוגמה, "microsoft/Phi-3-mini-4k-instruct").  
הגדירו את הגדרות המודל, כולל שימוש במטמון, סוג נתונים (bfloat16 עבור דיוק מעורב), ומימוש תשומת הלב.

**אימון**

כווננו את מודל Phi-3 באמצעות בסיס הנתונים המותאם להוראות צ'אט.  
השתמשו בהגדרות LoRA מ-peft_config לצורך התאמה יעילה.  
עקבו אחר התקדמות האימון באמצעות אסטרטגיית הלוגינג שהוגדרה.

**הערכה ושמירה**

העריכו את המודל המכוונן.  
שמרו נקודות ביקורת במהלך האימון לשימוש עתידי.

**דוגמאות**
- [למדו עוד עם מחברת דוגמה זו](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [דוגמה לתסריט כיוונון עדין ב-Python](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [דוגמה לכיוונון עדין עם LoRA ב-Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [דוגמה לכרטיס מודל של Hugging Face - כיוונון עדין עם LoRA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [דוגמה לכיוונון עדין עם QLORA ב-Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)  

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים לכלול שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לכל אי-הבנות או פרשנויות שגויות הנובעות מהשימוש בתרגום זה.