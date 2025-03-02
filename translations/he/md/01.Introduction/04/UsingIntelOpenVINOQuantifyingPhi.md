# **כימות Phi-3.5 באמצעות Intel OpenVINO**

אינטל היא אחת מיצרניות המעבדים הוותיקות ביותר עם משתמשים רבים. עם עליית תחום הלמידה החישובית והלמידה העמוקה, גם אינטל הצטרפה לתחרות בתחום ההאצה של בינה מלאכותית. לצורך הסקת מסקנות ממודלים, אינטל משתמשת לא רק ב-GPU ו-CPU, אלא גם ב-NPU.

אנו מקווים לפרוס את משפחת Phi-3.x בצד הקצה, מתוך שאיפה להפוך לחלק החשוב ביותר במחשב AI ובמחשב CoPilot. טעינת המודל בצד הקצה תלויה בשיתוף הפעולה של יצרני חומרה שונים. פרק זה מתמקד בעיקר בתרחיש היישום של Intel OpenVINO כמודל כמותי.

## **מה זה OpenVINO**

OpenVINO הוא ערכת כלים בקוד פתוח לאופטימיזציה ופריסה של מודלים של למידה עמוקה, החל מהענן ועד לקצה. הוא מאיץ הסקת מסקנות של למידה עמוקה במגוון תרחישים, כמו AI גנרטיבי, וידאו, אודיו ושפה, עם מודלים ממסגרות פופולריות כמו PyTorch, TensorFlow, ONNX ועוד. ניתן להמיר ולבצע אופטימיזציה למודלים, ולפרוס אותם על שילוב של חומרות וסביבות של אינטל®, באופן מקומי או בענן, בדפדפן או במכשיר.

כעת, עם OpenVINO, ניתן במהירות לכמת את מודל ה-GenAI על חומרת אינטל ולהאיץ את ביצוע המודל.

כיום OpenVINO תומך בהמרת כימות של Phi-3.5-Vision ו-Phi-3.5-Instruct.

### **הגדרת סביבה**

יש לוודא שהותקנו התלויות הבאות בסביבה. זהו הקובץ requirement.txt:

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **כימות Phi-3.5-Instruct באמצעות OpenVINO**

בטרמינל, יש להריץ את הסקריפט הבא:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **כימות Phi-3.5-Vision באמצעות OpenVINO**

יש להריץ את הסקריפט הבא ב-Python או ב-Jupyter Lab:

```python

import requests
from pathlib import Path
from ov_phi3_vision import convert_phi3_model
import nncf

if not Path("ov_phi3_vision.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/ov_phi3_vision.py")
    open("ov_phi3_vision.py", "w").write(r.text)


if not Path("gradio_helper.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/gradio_helper.py")
    open("gradio_helper.py", "w").write(r.text)

if not Path("notebook_utils.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/notebook_utils.py")
    open("notebook_utils.py", "w").write(r.text)



model_id = "microsoft/Phi-3.5-vision-instruct"
out_dir = Path("../model/phi-3.5-vision-128k-instruct-ov")
compression_configuration = {
    "mode": nncf.CompressWeightsMode.INT4_SYM,
    "group_size": 64,
    "ratio": 0.6,
}
if not out_dir.exists():
    convert_phi3_model(model_id, out_dir, compression_configuration)

```

### **🤖 דוגמאות ל-Phi-3.5 עם Intel OpenVINO**

| מעבדות    | תיאור | מעבר |
| -------- | ------- |  ------- |
| 🚀 מעבדה - היכרות עם Phi-3.5 Instruct  | למדו כיצד להשתמש ב-Phi-3.5 Instruct במחשב ה-AI שלכם    |  [מעבר](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 מעבדה - היכרות עם Phi-3.5 Vision (תמונה) | למדו כיצד להשתמש ב-Phi-3.5 Vision לניתוח תמונות במחשב ה-AI שלכם      |  [מעבר](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 מעבדה - היכרות עם Phi-3.5 Vision (וידאו)   | למדו כיצד להשתמש ב-Phi-3.5 Vision לניתוח תמונות במחשב ה-AI שלכם    |  [מעבר](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **משאבים**

1. למידע נוסף על Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. מאגר GitHub של Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. בעוד שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום אנושי מקצועי. אנו לא נושאים באחריות לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.