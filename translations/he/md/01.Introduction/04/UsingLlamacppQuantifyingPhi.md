# **כימות משפחת Phi באמצעות llama.cpp**

## **מה זה llama.cpp**

llama.cpp היא ספריית תוכנה בקוד פתוח שנכתבה בעיקר ב-C++, שמבצעת אינפרנס על מודלים שפתיים גדולים (LLMs) כמו Llama. המטרה העיקרית שלה היא לספק ביצועים מתקדמים עבור אינפרנס של LLM על מגוון רחב של חומרות עם הגדרה מינימלית. בנוסף, קיימים חיבורים ל-Python לספרייה זו, שמציעים ממשק API ברמה גבוהה להשלמת טקסט ושרת רשת תואם OpenAI.

המטרה העיקרית של llama.cpp היא לאפשר אינפרנס של LLM עם הגדרה מינימלית וביצועים מתקדמים על מגוון רחב של חומרות - מקומית ובענן.

- מימוש פשוט ב-C/C++ ללא תלות בספריות חיצוניות  
- Apple silicon נתמך באופן מלא - אופטימיזציה באמצעות ARM NEON, Accelerate ו-Metal frameworks  
- תמיכה ב-AVX, AVX2 ו-AVX512 לארכיטקטורות x86  
- כימות של 1.5 ביט, 2 ביט, 3 ביט, 4 ביט, 5 ביט, 6 ביט ו-8 ביט עבור אינפרנס מהיר יותר ושימוש מופחת בזיכרון  
- קרנלים מותאמים ל-CUDA להרצת LLMs על GPUs של NVIDIA (תמיכה ב-GPUs של AMD באמצעות HIP)  
- תמיכה ב-Vulkan ו-SYCL backend  
- אינפרנס היברידי CPU+GPU להאצת מודלים שגדולים מסך קיבולת ה-VRAM  

## **כימות Phi-3.5 באמצעות llama.cpp**

מודל Phi-3.5-Instruct ניתן לכימות באמצעות llama.cpp, אך המודלים Phi-3.5-Vision ו-Phi-3.5-MoE עדיין לא נתמכים. הפורמט שמומר על ידי llama.cpp הוא gguf, שהוא גם פורמט הכימות הנפוץ ביותר.

קיימים מספר רב של מודלים בפורמט GGUF הכמותי ב-Hugging Face. AI Foundry, Ollama ו-LlamaEdge מתבססים על llama.cpp, ולכן גם מודלים בפורמט GGUF נמצאים בשימוש תדיר.

### **מה זה GGUF**

GGUF הוא פורמט בינארי שמותאם לטעינה ושמירה מהירה של מודלים, מה שהופך אותו ליעיל מאוד למטרות אינפרנס. GGUF מיועד לשימוש עם GGML ומנועי ביצוע אחרים. GGUF פותח על ידי @ggerganov, שגם פיתח את llama.cpp, מסגרת אינפרנס פופולרית ל-LLM ב-C/C++. מודלים שפותחו במקור במסגרת כמו PyTorch יכולים להיות מומרות לפורמט GGUF לשימוש עם מנועים אלו.

### **ONNX לעומת GGUF**

ONNX הוא פורמט מסורתי ללמידת מכונה/למידה עמוקה, שמקבל תמיכה רחבה במסגרת AI שונות ויש לו שימושים טובים במכשירי קצה. GGUF, לעומת זאת, מבוסס על llama.cpp וניתן לומר שהוא תוצר של עידן ה-GenAI. לשני הפורמטים שימושים דומים. אם אתם מחפשים ביצועים טובים יותר בחומרה משובצת ובשכבות יישום, ייתכן ש-ONNX הוא הבחירה שלכם. אם אתם משתמשים במסגרת וטכנולוגיה נגזרת של llama.cpp, אז GGUF עשוי להיות עדיף.

### **כימות Phi-3.5-Instruct באמצעות llama.cpp**

**1. הגדרת סביבה**

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```

**2. כימות**

באמצעות llama.cpp המירו את Phi-3.5-Instruct ל-FP16 GGUF  

```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

כימות Phi-3.5 ל-INT4  

```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```

**3. בדיקה**

התקנת llama-cpp-python  

```bash

pip install llama-cpp-python -U

```

***שימו לב***  

אם אתם משתמשים ב-Apple Silicon, התקינו את llama-cpp-python כך:  

```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

בדיקה  

```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```

## **משאבים**

1. למידע נוסף על llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  

2. למידע נוסף על GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)  

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים לכלול שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.