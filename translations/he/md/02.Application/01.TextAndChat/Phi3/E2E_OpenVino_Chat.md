[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

קוד זה מייצא מודל לפורמט OpenVINO, טוען אותו ומשתמש בו ליצירת תגובה להנחיה נתונה.

1. **ייצוא המודל**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - הפקודה הזו משתמשת ב-`optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **ייבוא הספריות הנדרשות**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - השורות האלו מייבאות מחלקות מהמודול `transformers` library and the `optimum.intel.openvino`, שנדרשות לטעינת המודל ושימוש בו.

3. **הגדרת ספריית המודל והקונפיגורציה**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` הוא מילון שמגדיר את מודל OpenVINO כך שייתן עדיפות ללטנטיות נמוכה, ישתמש בזרם חיזוי יחיד ולא ישתמש בספריית מטמון.

4. **טעינת המודל**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - שורה זו טוענת את המודל מהספרייה שצוינה, תוך שימוש בהגדרות הקונפיגורציה שהוגדרו קודם. היא גם מאפשרת הרצת קוד מרוחק במידת הצורך.

5. **טעינת הטוקניזר**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - שורה זו טוענת את הטוקניזר, שאחראי על המרת טקסט לטוקנים שהמודל יכול להבין.

6. **הגדרת פרמטרים לטוקניזר**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - מילון זה מגדיר שאין להוסיף טוקנים מיוחדים לפלט הטוקניזציה.

7. **הגדרת ההנחיה**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - מחרוזת זו מגדירה הנחיה לשיחה שבה המשתמש מבקש מהעוזר המלאכותי להציג את עצמו.

8. **טוקניזציה של ההנחיה**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - שורה זו ממירה את ההנחיה לטוקנים שהמודל יכול לעבד, ומחזירה את התוצאה כטנסורים של PyTorch.

9. **יצירת תגובה**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - שורה זו משתמשת במודל ליצירת תגובה על בסיס טוקני הקלט, עם מקסימום של 1024 טוקנים חדשים.

10. **פענוח התגובה**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - שורה זו ממירה את הטוקנים שנוצרו בחזרה למחרוזת קריאה לאדם, מדלגת על טוקנים מיוחדים ומחזירה את התוצאה הראשונה.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. יש לראות במסמך המקורי בשפתו המקורית כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.