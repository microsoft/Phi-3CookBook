**כיוונון עדין של Phi-3 עם QLoRA**

כיוונון עדין של מודל השפה Phi-3 Mini של Microsoft באמצעות [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA יסייע בשיפור הבנת שיחות ויצירת תגובות.

כדי לטעון מודלים בפורמט של 4 ביטים באמצעות transformers ו-bitsandbytes, יש להתקין את accelerate ואת transformers מהקוד המקור, ולוודא שיש לכם את הגרסה העדכנית ביותר של ספריית bitsandbytes.

**דוגמאות**
- [למידע נוסף עם המחברת הזו](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [דוגמה של כיוונון עדין ב-Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [דוגמה לכיוונון עדין ב-Hugging Face Hub עם LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [דוגמה לכיוונון עדין ב-Hugging Face Hub עם QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. בעוד שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים לכלול טעויות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי בני אדם. איננו אחראים לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.  