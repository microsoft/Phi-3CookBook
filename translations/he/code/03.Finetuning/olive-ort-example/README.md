# כוונון עדין ל-Phi3 באמצעות Olive

בדוגמה זו תשתמשו ב-Olive כדי:

1. לבצע כוונון עדין למתאם LoRA על מנת לסווג ביטויים לקטגוריות: עצב, שמחה, פחד, הפתעה.
2. למזג את משקלות המתאם אל תוך מודל הבסיס.
3. לבצע אופטימיזציה וכימות של המודל אל `int4`.

נראה לכם גם איך לבצע הסקה עם המודל המכוון באמצעות Generate API של ONNX Runtime (ORT).

> **⚠️ לכוונון עדין, תצטרכו GPU מתאים - לדוגמה, A10, V100, A100.**

## 💾 התקנה

צרו סביבה וירטואלית חדשה של Python (לדוגמה, באמצעות `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

לאחר מכן, התקינו את Olive ואת התלויות הדרושות עבור זרימת עבודה של כוונון עדין:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 כוונון עדין ל-Phi3 באמצעות Olive
קובץ [תצורת Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) מכיל *זרימת עבודה* עם ה-*מעברים* הבאים:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

ברמה גבוהה, זרימת עבודה זו תבצע:

1. כוונון עדין ל-Phi3 (למשך 150 צעדים, ניתן לשנות) באמצעות הנתונים מתוך [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
2. מיזוג משקלות מתאם LoRA אל תוך מודל הבסיס. תוצאה זו תהיה מודל יחיד בפורמט ONNX.
3. Model Builder יבצע אופטימיזציה למודל עבור ONNX runtime *ו*יכמת את המודל אל `int4`.

כדי להפעיל את זרימת העבודה, הריצו:

```bash
olive run --config phrase-classification.json
```

לאחר ש-Olive תסיים, המודל המכוונן והמאופטם שלכם, `int4`, יהיה זמין בנתיב: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 שילוב Phi3 המכוונן באפליקציה שלכם 

כדי להריץ את האפליקציה:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

תשובת המערכת צריכה להיות סיווג בודד של הביטוי (עצב/שמחה/פחד/הפתעה).

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. בעוד שאנו שואפים לדיוק, אנא היו מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.