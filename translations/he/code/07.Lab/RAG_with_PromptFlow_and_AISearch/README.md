## RAG עם PromptFlow ו-AISearch

בדוגמה זו, ניישם אפליקציית יצירה מוגברת על ידי אחזור (RAG) תוך שימוש ב-Phi3 כ-SLM, ב-AI Search כ-vectorDB וב-Prompt Flow כאורקסטרטור בעל קוד נמוך.

## מאפיינים

- פריסה קלה באמצעות Docker.
- ארכיטקטורה ניתנת להרחבה לטיפול בתהליכי עבודה של AI.
- גישה עם מעט קוד באמצעות Prompt Flow.

## דרישות מקדימות

לפני שתתחיל, ודא שעמדת בדרישות הבאות:

- Docker מותקן במחשב המקומי שלך.
- חשבון Azure עם הרשאות ליצירה וניהול של משאבי קונטיינרים.
- Azure AI Studio ו-Azure AI Search זמינים.
- מודל embedding ליצירת אינדקס (יכול להיות embedding של Azure OpenAI או מודל OS מתוך הקטלוג).
- Python בגרסה 3.8 או מאוחרת יותר מותקן במחשב המקומי שלך.
- Azure Container Registry (או כל רישום אחר לבחירתך).

## התקנה

1. צור flow חדש בפרויקט Azure AI Studio שלך באמצעות קובץ flow.yaml.
2. פרוס מודל Phi3 מתוך קטלוג המודלים של Azure AI וחבר אותו לפרויקט שלך. [פרוס את Phi-3 כמודל כשירות](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. צור אינדקס וקטורי ב-Azure AI Search באמצעות כל מסמך שתבחר. [צור אינדקס וקטורי ב-Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. פרוס את ה-flow על נקודת קצה מנוהלת והשתמש בו בקובץ prompt-flow-frontend.py. [פרוס flow על נקודת קצה מקוונת](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. שיבט את המאגר:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. בנה את תמונת ה-Docker:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. דחוף את תמונת ה-Docker ל-Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## שימוש

1. הפעל את קונטיינר ה-Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. גש לאפליקציה בדפדפן שלך בכתובת `http://localhost:8501`.

## יצירת קשר

ולנטינה אלטו - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

מאמר מלא: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל טעויות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.