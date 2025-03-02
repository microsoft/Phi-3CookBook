# **ביצוע Inference עם Phi-3 במכשירי אנדרואיד**

בואו נחקור כיצד ניתן לבצע Inference עם Phi-3-mini במכשירי אנדרואיד. Phi-3-mini היא סדרת מודלים חדשה של מיקרוסופט שמאפשרת פריסה של מודלים שפתיים גדולים (LLMs) על מכשירי קצה ומכשירי IoT.

## Semantic Kernel ו-Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) הוא מסגרת יישומים שמאפשרת ליצור אפליקציות תואמות ל-Azure OpenAI Service, מודלים של OpenAI ואפילו מודלים מקומיים. אם אתם חדשים ב-Semantic Kernel, אנו ממליצים לעיין ב-[Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### גישה ל-Phi-3-mini באמצעות Semantic Kernel

ניתן לשלב את המודל עם Hugging Face Connector ב-Semantic Kernel. ראו [קוד לדוגמה](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

ברירת המחדל היא שהמודל תואם ל-ID ב-Hugging Face. עם זאת, ניתן גם להתחבר לשרת מודלים של Phi-3-mini שנבנה מקומית.

### קריאה למודלים מוקטנים עם Ollama או LlamaEdge

משתמשים רבים מעדיפים להשתמש במודלים מוקטנים לצורך הפעלה מקומית. [Ollama](https://ollama.com/) ו-[LlamaEdge](https://llamaedge.com) מאפשרים למשתמשים לקרוא למודלים מוקטנים שונים:

#### Ollama

ניתן להפעיל ישירות `ollama run Phi-3` או להגדיר אותו במצב לא מקוון על ידי יצירת `Modelfile` עם הנתיב לקובץ `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[קוד לדוגמה](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

אם אתם מעוניינים להשתמש בקבצי `.gguf` בענן ובמכשירי קצה בו-זמנית, LlamaEdge היא אפשרות מצוינת. תוכלו לעיין ב-[קוד לדוגמה](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) כדי להתחיל.

### התקנה והפעלה במכשירי אנדרואיד

1. **הורידו את אפליקציית MLC Chat** (חינמית) למכשירי אנדרואיד.
2. הורידו את קובץ ה-APK (148MB) והתקינו אותו במכשיר שלכם.
3. הפעילו את אפליקציית MLC Chat. תראו רשימה של מודלים בינה מלאכותית, כולל Phi-3-mini.

לסיכום, Phi-3-mini פותח אפשרויות מרתקות עבור AI גנרטיבי במכשירי קצה, ואתם יכולים להתחיל לחקור את היכולות שלו במכשירי אנדרואיד.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בשירותי תרגום אנושיים מקצועיים. איננו נושאים באחריות לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.