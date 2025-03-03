### תרחיש לדוגמה

דמיינו שיש לכם תמונה (`demo.png`) ואתם רוצים ליצור קוד Python שמעבד את התמונה ושומר גרסה חדשה שלה (`phi-3-vision.jpg`).

הקוד למעלה מבצע את התהליך באופן אוטומטי על ידי:

1. הגדרת הסביבה והקונפיגורציות הנדרשות.
2. יצירת פרומפט שמנחה את המודל לייצר את קוד ה-Python הדרוש.
3. שליחת הפרומפט למודל ואיסוף הקוד שנוצר.
4. חילוץ והרצת הקוד שנוצר.
5. הצגת התמונה המקורית והתמונה המעובדת.

הגישה הזו מנצלת את הכוח של AI לאוטומציה של משימות עיבוד תמונה, מה שמקל ומזרז את השגת המטרות שלכם.

[פתרון קוד לדוגמה](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

בואו נפרק את מה שהקוד כולו עושה שלב אחר שלב:

1. **התקנת החבילה הנדרשת**:  
   ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```  
   הפקודה הזו מתקינה את החבילה `langchain_nvidia_ai_endpoints`, ומוודאת שהיא בגרסה העדכנית ביותר.

2. **ייבוא המודולים הנחוצים**:  
   ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```  
   הייבוא הזה מביא את המודולים הנדרשים לעבודה עם נקודות הקצה של NVIDIA AI, לטיפול בסיסמאות בצורה מאובטחת, לעבודה עם מערכת ההפעלה, ולביצוע קידוד/פענוח של נתונים בפורמט base64.

3. **הגדרת מפתח API**:  
   ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```  
   הקוד הזה בודק אם משתנה הסביבה `NVIDIA_API_KEY` מוגדר. אם לא, הוא מבקש מהמשתמש להזין את מפתח ה-API בצורה מאובטחת.

4. **הגדרת מודל ונתיב התמונה**:  
   ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```  
   כאן מוגדר המודל לשימוש, נוצר מופע של `ChatNVIDIA` עם המודל שצוין, ומוגדר נתיב לקובץ התמונה.

5. **יצירת פרומפט טקסטואלי**:  
   ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```  
   הפרומפט הזה מגדיר הנחיה טקסטואלית שמנחה את המודל לייצר קוד Python לעיבוד תמונה.

6. **קידוד התמונה בפורמט Base64**:  
   ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```  
   הקוד הזה קורא את קובץ התמונה, מקודד אותו בפורמט base64, ויוצר תג HTML של תמונה עם הנתונים המקודדים.

7. **שילוב הטקסט והתמונה בפרומפט**:  
   ```python
    prompt = f"{text} {image}"
    ```  
   כאן הטקסט של הפרומפט ותג התמונה ב-HTML משולבים למחרוזת אחת.

8. **יצירת קוד בעזרת ChatNVIDIA**:  
   ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```  
   הקוד הזה שולח את הפרומפט ל-`ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` ומקבל את הקוד שנוצר.

9. **חילוץ קוד Python מהתוכן שנוצר**:  
   ```python
    begin = code.index('```python') + 9  
   code = code[begin:]  
   end = code.index('```')
    code = code[:end]
    ```  
   הקוד הזה מחלץ את קוד ה-Python מתוך התוכן שנוצר על ידי הסרת הפורמט של Markdown.

10. **הרצת הקוד שנוצר**:  
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```  
    הקוד הזה מריץ את קוד ה-Python שנחולץ כתהליך משנה ומקליט את הפלט שלו.

11. **הצגת התמונות**:  
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```  
    השורות האלו מציגות את התמונות בעזרת המודול `IPython.display`.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום אנושי מקצועי. איננו אחראים לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.