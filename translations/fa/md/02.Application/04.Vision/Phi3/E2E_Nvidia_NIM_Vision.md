### سناریوی نمونه

تصور کنید یک تصویر (`demo.png`) دارید و می‌خواهید کدی به زبان پایتون تولید کنید که این تصویر را پردازش کرده و نسخه جدیدی از آن را ذخیره کند (`phi-3-vision.jpg`).

کد بالا این فرآیند را با انجام مراحل زیر خودکار می‌کند:

1. تنظیم محیط و پیکربندی‌های لازم.
2. ایجاد یک پرامپت که مدل را راهنمایی می‌کند تا کد پایتون مورد نیاز را تولید کند.
3. ارسال پرامپت به مدل و جمع‌آوری کد تولیدشده.
4. استخراج و اجرای کد تولیدشده.
5. نمایش تصویر اصلی و تصویر پردازش‌شده.

این روش از قدرت هوش مصنوعی برای خودکارسازی وظایف پردازش تصویر بهره می‌برد و دستیابی به اهداف شما را ساده‌تر و سریع‌تر می‌کند.

[راه‌حل نمونه کد](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

بیایید قدم به قدم بررسی کنیم که کل کد چه کاری انجام می‌دهد:

1. **نصب بسته مورد نیاز**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    این دستور بسته `langchain_nvidia_ai_endpoints` را نصب می‌کند و اطمینان می‌دهد که آخرین نسخه آن استفاده می‌شود.

2. **وارد کردن ماژول‌های لازم**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    این واردات، ماژول‌های مورد نیاز برای تعامل با نقاط پایانی NVIDIA AI، مدیریت ایمن رمزها، تعامل با سیستم‌عامل و کدگذاری/رمزگشایی داده‌ها در قالب base64 را فراهم می‌کنند.

3. **تنظیم کلید API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    این کد بررسی می‌کند که آیا متغیر محیطی `NVIDIA_API_KEY` تنظیم شده است یا خیر. اگر تنظیم نشده باشد، از کاربر می‌خواهد که کلید API خود را به‌صورت ایمن وارد کند.

4. **تعریف مدل و مسیر تصویر**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    این قسمت مدل مورد استفاده را تنظیم می‌کند، یک نمونه از `ChatNVIDIA` با مدل مشخص ایجاد می‌کند و مسیر فایل تصویر را تعریف می‌کند.

5. **ایجاد پرامپت متنی**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    این قسمت یک پرامپت متنی تعریف می‌کند که مدل را برای تولید کد پایتون جهت پردازش تصویر راهنمایی می‌کند.

6. **کدگذاری تصویر در base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    این کد فایل تصویر را می‌خواند، آن را در base64 کدگذاری می‌کند و یک تگ HTML تصویر با داده‌های کدگذاری‌شده ایجاد می‌کند.

7. **ترکیب متن و تصویر در پرامپت**:
    ```python
    prompt = f"{text} {image}"
    ```
    این قسمت متن پرامپت و تگ HTML تصویر را در یک رشته واحد ترکیب می‌کند.

8. **تولید کد با استفاده از ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    این کد پرامپت را به `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` ارسال می‌کند و پاسخ تولیدشده را دریافت می‌کند.

9. **استخراج کد پایتون از محتوای تولیدشده**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    این قسمت کد پایتون واقعی را از محتوای تولیدشده استخراج می‌کند و قالب‌بندی markdown را حذف می‌کند.

10. **اجرای کد تولیدشده**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    این کد استخراج‌شده را به‌عنوان یک زیر‌فرآیند اجرا کرده و خروجی آن را دریافت می‌کند.

11. **نمایش تصاویر**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    این خطوط با استفاده از ماژول `IPython.display` تصاویر را نمایش می‌دهند.

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه ماشینی مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را رعایت کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی باید به‌عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ‌گونه مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.