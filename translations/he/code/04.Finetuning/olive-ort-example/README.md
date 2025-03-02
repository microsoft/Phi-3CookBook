# כוונון עדין של Phi3 עם Olive

בדוגמה הזו תשתמשו ב-Olive כדי:

1. לכוון עדין LoRA adapter כדי לסווג ביטויים לקטגוריות עצב, שמחה, פחד, הפתעה.
1. למזג את משקלי ה-adapter עם המודל הבסיסי.
1. לבצע אופטימיזציה וכיווץ של המודל ל-`int4`.

נראה לכם גם איך לבצע הסקה עם המודל המכוונן באמצעות ה-ONNX Runtime (ORT) Generate API.

> **⚠️ לכיוונון עדין, תצטרכו GPU מתאים - לדוגמה, A10, V100, A100.**

## 💾 התקנה

צרו סביבה וירטואלית חדשה של Python (לדוגמה, באמצעות `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

לאחר מכן, התקינו את Olive ואת התלויות הנדרשות לזרימת עבודה של כיוונון עדין:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 כוונון עדין של Phi3 עם Olive
[קובץ הקונפיגורציה של Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) מכיל *זרימת עבודה* עם ה-*מעברים* הבאים:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

ברמה גבוהה, זרימת העבודה הזו תבצע:

1. כוונון עדין של Phi3 (למשך 150 צעדים, שניתן לשנות) באמצעות הנתונים מהקובץ [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. מיזוג משקלי ה-LoRA adapter עם המודל הבסיסי. זה יפיק לכם מודל יחיד בפורמט ONNX.
1. Model Builder יבצע אופטימיזציה למודל עבור ONNX runtime *וגם* יכווץ את המודל ל-`int4`.

כדי להריץ את זרימת העבודה, הריצו:

```bash
olive run --config phrase-classification.json
```

כשהתהליך יושלם, המודל המכוונן והאופטימלי `int4` של Phi3 יהיה זמין בנתיב: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 שילוב Phi3 המכוונן באפליקציה שלכם

כדי להריץ את האפליקציה:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

התוצאה אמורה להיות סיווג חד-מילתי של הביטוי (עצב/שמחה/פחד/הפתעה).

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים לכלול טעויות או אי-דיוקים. המסמך המקורי בשפתו המקורית ייחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי בני אדם. איננו נושאים באחריות לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.