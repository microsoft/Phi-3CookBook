# **הרצת Phi-3 עם מסגרת Apple MLX**

## **מהי מסגרת MLX**

MLX היא מסגרת ייעודית למחקר למידת מכונה על גבי מעבדי Apple Silicon, שפותחה על ידי צוות המחקר של Apple בתחום למידת מכונה.

MLX תוכננה על ידי חוקרי למידת מכונה עבור חוקרי למידת מכונה. המסגרת מיועדת להיות ידידותית למשתמש אך עדיין יעילה לאימון והפעלה של מודלים. התכנון של המסגרת עצמו פשוט מבחינה רעיונית, עם כוונה להקל על החוקרים להרחיב ולשפר את MLX במטרה לחקור רעיונות חדשים במהירות.

מודלים גדולים לשפה (LLMs) יכולים להיות מואצים על גבי מכשירי Apple Silicon באמצעות MLX, וניתן להפעיל את המודלים באופן מקומי בנוחות רבה.

## **שימוש ב-MLX להרצת Phi-3-mini**

### **1. הגדרת סביבת MLX**

1. Python 3.11.x  
2. התקנת ספריית MLX  

```bash

pip install mlx-lm

```

### **2. הרצת Phi-3-mini בטרמינל עם MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

התוצאה (בסביבה שלי Apple M1 Max, 64GB) היא:

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.he.png)

### **3. כיווץ Phi-3-mini עם MLX בטרמינל**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***הערה:*** ניתן לכווץ את המודל באמצעות הפונקציה mlx_lm.convert, והכיווץ המוגדר כברירת מחדל הוא INT4. בדוגמה זו כיווצנו את Phi-3-mini ל-INT4.

המודל ניתן לכיווץ באמצעות mlx_lm.convert, והכיווץ המוגדר כברירת מחדל הוא INT4. בדוגמה זו כיווצנו את Phi-3-mini לפורמט INT4. לאחר הכיווץ, הוא יישמר בתיקייה ברירת המחדל ./mlx_model.

ניתן לבדוק את המודל המכווּץ עם MLX מהטרמינל:

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

התוצאה היא:

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.he.png)

### **4. הרצת Phi-3-mini עם MLX ב-Jupyter Notebook**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.he.png)

***הערה:*** אנא קראו את הדוגמה הזו [לחצו על הקישור](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **משאבים**

1. למידע נוסף על מסגרת Apple MLX [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. מאגר GitHub של Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. בעוד אנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. יש להתייחס למסמך המקורי בשפתו המקורית כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום אנושי מקצועי. איננו נושאים באחריות לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.