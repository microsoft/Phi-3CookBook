# **כימות Phi-3.5 באמצעות Apple MLX Framework**

MLX הוא מסגרת מערכים למחקר למידת מכונה על גבי שבבים של Apple, שפותחה על ידי צוות מחקר למידת המכונה של Apple.

MLX נועדה על ידי חוקרי למידת מכונה עבור חוקרי למידת מכונה. המסגרת מיועדת להיות ידידותית למשתמש, אך עדיין יעילה לאימון ופריסת מודלים. העיצוב של המסגרת עצמו פשוט מבחינה רעיונית. אנו שואפים להקל על חוקרים להרחיב ולשפר את MLX מתוך מטרה לחקור במהירות רעיונות חדשים.

ניתן להאיץ מודלים לשפה גדולה (LLMs) במכשירי Apple Silicon באמצעות MLX, ולהריץ מודלים מקומית בנוחות רבה.

כעת, Apple MLX Framework תומך בהמרת כימות של Phi-3.5-Instruct (**תמיכה במסגרת Apple MLX Framework**), Phi-3.5-Vision (**תמיכה במסגרת MLX-VLM Framework**), ו-Phi-3.5-MoE (**תמיכה במסגרת Apple MLX Framework**). בואו ננסה זאת:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 דוגמאות עבור Phi-3.5 עם Apple MLX**

| מעבדות    | תיאור | מעבר |
| -------- | ------- |  ------- |
| 🚀 מעבדה - הצגת Phi-3.5 Instruct  | למדו כיצד להשתמש ב-Phi-3.5 Instruct עם מסגרת Apple MLX   |  [מעבר](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 מעבדה - הצגת Phi-3.5 Vision (תמונה) | למדו כיצד להשתמש ב-Phi-3.5 Vision לניתוח תמונות עם מסגרת Apple MLX     |  [מעבר](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 מעבדה - הצגת Phi-3.5 Vision (MoE)   | למדו כיצד להשתמש ב-Phi-3.5 MoE עם מסגרת Apple MLX  |  [מעבר](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **משאבים**

1. למדו על Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. מאגר GitHub של Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. מאגר GitHub של MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים לכלול שגיאות או אי-דיוקים. יש להתייחס למסמך המקורי בשפתו המקורית כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי בני אדם. איננו נושאים באחריות לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.