### سيناريو مثال

تخيل أن لديك صورة (`demo.png`) وتريد إنشاء كود بايثون يعالج هذه الصورة ويحفظ نسخة جديدة منها (`phi-3-vision.jpg`).

يقوم الكود أعلاه بأتمتة هذه العملية من خلال:

1. إعداد البيئة والتكوينات اللازمة.
2. إنشاء موجه يطلب من النموذج توليد كود بايثون المطلوب.
3. إرسال الموجه إلى النموذج وجمع الكود الناتج.
4. استخراج الكود الناتج وتشغيله.
5. عرض الصورة الأصلية والصورة المعالجة.

هذا النهج يستفيد من قوة الذكاء الاصطناعي لأتمتة مهام معالجة الصور، مما يجعل تحقيق أهدافك أسهل وأسرع.

[حل الكود النموذجي](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

لنقم بتفصيل ما يفعله الكود بالكامل خطوة بخطوة:

1. **تثبيت الحزمة المطلوبة**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    يقوم هذا الأمر بتثبيت حزمة `langchain_nvidia_ai_endpoints`، مع التأكد من أنها أحدث إصدار.

2. **استيراد الوحدات اللازمة**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    تتيح هذه الاستيرادات استخدام الوحدات اللازمة للتفاعل مع نقاط نهاية NVIDIA AI، وتأمين كلمات المرور، والتفاعل مع نظام التشغيل، وترميز وفك ترميز البيانات بتنسيق base64.

3. **إعداد مفتاح API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    يتحقق هذا الكود مما إذا كان متغير البيئة `NVIDIA_API_KEY` مضبوطًا. إذا لم يكن كذلك، فإنه يطلب من المستخدم إدخال مفتاح API الخاص به بشكل آمن.

4. **تحديد النموذج ومسار الصورة**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    يتم تحديد النموذج المستخدم، وإنشاء مثيل لـ `ChatNVIDIA` باستخدام النموذج المحدد، وتحديد مسار ملف الصورة.

5. **إنشاء موجه نصي**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    يحدد هذا موجهًا نصيًا يطلب من النموذج إنشاء كود بايثون لمعالجة صورة.

6. **ترميز الصورة بتنسيق Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    يقرأ هذا الكود ملف الصورة، ويقوم بترميزها بتنسيق base64، ويُنشئ علامة HTML للصورة مع البيانات المشفرة.

7. **دمج النص والصورة في موجه واحد**:
    ```python
    prompt = f"{text} {image}"
    ```
    يقوم هذا بدمج الموجه النصي وعلامة HTML للصورة في سلسلة نصية واحدة.

8. **توليد الكود باستخدام ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    يرسل هذا الكود الموجه إلى `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` ويجمع الكود الناتج.

9. **استخراج كود بايثون من المحتوى الناتج**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    يستخرج هذا الكود كود بايثون الفعلي من المحتوى الناتج عن طريق إزالة تنسيق الماركداون.

10. **تشغيل الكود الناتج**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    يقوم هذا بتشغيل كود بايثون المستخرج كعملية فرعية ويلتقط مخرجاته.

11. **عرض الصور**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    تعرض هذه الأسطر الصور باستخدام وحدة `IPython.display`.

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمات الترجمة الآلية المعتمدة على الذكاء الاصطناعي. بينما نسعى جاهدين لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ نتيجة استخدام هذه الترجمة.