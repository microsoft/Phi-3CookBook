### مثال منظر

فرض کریں کہ آپ کے پاس ایک تصویر ہے (`demo.png`) اور آپ Python کوڈ تیار کرنا چاہتے ہیں جو اس تصویر کو پروسیس کرے اور اس کا ایک نیا ورژن محفوظ کرے (`phi-3-vision.jpg`)۔

اوپر دیا گیا کوڈ اس عمل کو خودکار کرتا ہے:

1. ماحول اور ضروری کنفیگریشنز کو سیٹ اپ کرنا۔
2. ایسا پرامپٹ بنانا جو ماڈل کو مطلوبہ Python کوڈ تیار کرنے کی ہدایت دے۔
3. پرامپٹ کو ماڈل کو بھیجنا اور تیار کردہ کوڈ کو اکٹھا کرنا۔
4. تیار کردہ کوڈ کو نکالنا اور چلانا۔
5. اصل اور پروسیس شدہ تصاویر کو دکھانا۔

یہ طریقہ AI کی طاقت کو استعمال کرتا ہے تاکہ امیج پروسیسنگ کے کاموں کو خودکار بنایا جا سکے، جس سے آپ کے مقاصد کو حاصل کرنا آسان اور تیز ہو جاتا ہے۔

[نمونہ کوڈ حل](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

آئیے پورے کوڈ کو مرحلہ وار سمجھتے ہیں:

1. **ضروری پیکج انسٹال کریں**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    یہ کمانڈ `langchain_nvidia_ai_endpoints` پیکج کو انسٹال کرتی ہے، یہ یقینی بناتے ہوئے کہ یہ تازہ ترین ورژن ہے۔

2. **ضروری ماڈیولز درآمد کریں**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    یہ درآمدات NVIDIA AI اینڈ پوائنٹس کے ساتھ تعامل، پاس ورڈز کو محفوظ طریقے سے ہینڈل کرنے، آپریٹنگ سسٹم کے ساتھ تعامل، اور بیس64 فارمیٹ میں ڈیٹا کو انکوڈ/ڈیکوڈ کرنے کے لیے ضروری ماڈیولز لاتی ہیں۔

3. **API کی چابی سیٹ کریں**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    یہ کوڈ چیک کرتا ہے کہ آیا `NVIDIA_API_KEY` ماحول متغیر سیٹ ہے۔ اگر نہیں، تو یہ صارف کو ان کی API کی چابی محفوظ طریقے سے داخل کرنے کا اشارہ دیتا ہے۔

4. **ماڈل اور تصویر کا راستہ متعین کریں**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    یہ استعمال ہونے والے ماڈل کو سیٹ کرتا ہے، مخصوص ماڈل کے ساتھ `ChatNVIDIA` کی ایک مثال بناتا ہے، اور تصویر فائل کے راستے کی وضاحت کرتا ہے۔

5. **متن پرامپٹ بنائیں**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    یہ ایک متن پرامپٹ کی وضاحت کرتا ہے جو ماڈل کو تصویر پروسیسنگ کے لیے Python کوڈ تیار کرنے کی ہدایت دیتا ہے۔

6. **تصویر کو بیس64 میں انکوڈ کریں**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    یہ کوڈ تصویر فائل کو پڑھتا ہے، اسے بیس64 میں انکوڈ کرتا ہے، اور انکوڈ شدہ ڈیٹا کے ساتھ ایک HTML تصویر ٹیگ بناتا ہے۔

7. **متن اور تصویر کو پرامپٹ میں یکجا کریں**:
    ```python
    prompt = f"{text} {image}"
    ```
    یہ متن پرامپٹ اور HTML تصویر ٹیگ کو ایک ہی سٹرنگ میں یکجا کرتا ہے۔

8. **ChatNVIDIA کا استعمال کرتے ہوئے کوڈ تیار کریں**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    یہ کوڈ پرامپٹ کو `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` سٹرنگ میں بھیجتا ہے۔

9. **تیار کردہ مواد سے Python کوڈ نکالیں**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    یہ تیار کردہ مواد سے اصل Python کوڈ نکالتا ہے، مارک ڈاؤن فارمیٹنگ کو ہٹا کر۔

10. **تیار کردہ کوڈ کو چلائیں**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    یہ نکالا گیا Python کوڈ ایک سب پروسیس کے طور پر چلاتا ہے اور اس کی آؤٹ پٹ کو کیپچر کرتا ہے۔

11. **تصاویر دکھائیں**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    یہ لائنیں `IPython.display` ماڈیول کا استعمال کرتے ہوئے تصاویر دکھاتی ہیں۔

**ڈسکلیمر**:  
یہ دستاویز مشین پر مبنی اے آئی ترجمہ خدمات کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمے کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔