# **کوانتیزه کردن خانواده Phi با استفاده از افزونه‌های هوش مصنوعی مولد برای onnxruntime**

## **افزونه‌های هوش مصنوعی مولد برای onnxruntime چیست؟**

این افزونه‌ها به شما کمک می‌کنند تا هوش مصنوعی مولد را با ONNX Runtime اجرا کنید ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). این افزونه‌ها حلقه هوش مصنوعی مولد را برای مدل‌های ONNX فراهم می‌کنند که شامل استنتاج با ONNX Runtime، پردازش لاجیت‌ها، جستجو و نمونه‌گیری، و مدیریت کش KV است. توسعه‌دهندگان می‌توانند از متد سطح بالای generate() استفاده کنند یا هر تکرار مدل را در یک حلقه اجرا کنند، یک توکن در هر بار تولید کنند و در صورت نیاز، پارامترهای تولید را در داخل حلقه به‌روزرسانی کنند. این افزونه‌ها از جستجوی حریصانه/پرتو و نمونه‌گیری TopP و TopK برای تولید دنباله‌های توکن پشتیبانی می‌کنند و پردازش لاجیت‌های داخلی مانند جریمه‌های تکرار را ارائه می‌دهند. همچنین به راحتی می‌توانید امتیازدهی سفارشی اضافه کنید.

در سطح برنامه، می‌توانید از افزونه‌های هوش مصنوعی مولد برای onnxruntime برای ساخت برنامه‌ها با استفاده از C++/ C# / Python استفاده کنید. در سطح مدل، می‌توانید از آن برای ادغام مدل‌های تنظیم‌شده و انجام کارهای استقرار کمی مرتبط بهره ببرید.

## **کوانتیزه کردن Phi-3.5 با استفاده از افزونه‌های هوش مصنوعی مولد برای onnxruntime**

### **مدل‌های پشتیبانی‌شده**

افزونه‌های هوش مصنوعی مولد برای onnxruntime از تبدیل کوانتیزه مدل‌های Microsoft Phi، Google Gemma، Mistral، و Meta LLaMA پشتیبانی می‌کنند.

### **سازنده مدل در افزونه‌های هوش مصنوعی مولد برای onnxruntime**

سازنده مدل به طور چشمگیری فرآیند ایجاد مدل‌های ONNX بهینه و کوانتیزه شده که با API تولید onnxruntime اجرا می‌شوند را تسریع می‌بخشد.

با استفاده از سازنده مدل، می‌توانید مدل را به INT4، INT8، FP16، FP32 کوانتیزه کنید و روش‌های مختلف شتاب‌دهنده سخت‌افزاری مانند CPU، CUDA، DirectML، Mobile و غیره را ترکیب کنید.

برای استفاده از سازنده مدل، باید نصب کنید:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

پس از نصب، می‌توانید اسکریپت سازنده مدل را از طریق ترمینال اجرا کنید تا تبدیل قالب و کوانتیزه مدل انجام شود.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

درک پارامترهای مرتبط:

1. **model_name** این مدل موجود در Hugging Face است، مانند microsoft/Phi-3.5-mini-instruct، microsoft/Phi-3.5-vision-instruct و غیره. همچنین می‌تواند مسیری باشد که مدل را در آن ذخیره کرده‌اید.

2. **path_to_output_folder** مسیر ذخیره تبدیل کوانتیزه‌شده

3. **execution_provider** پشتیبانی از شتاب‌دهنده‌های سخت‌افزاری مختلف، مانند CPU، CUDA، DirectML

4. **cache_dir_to_save_hf_files** ما مدل را از Hugging Face دانلود کرده و به صورت محلی کش می‌کنیم.

***توجه:***

## **چگونه از سازنده مدل برای کوانتیزه کردن Phi-3.5 استفاده کنیم**

سازنده مدل اکنون از کوانتیزه کردن مدل ONNX برای Phi-3.5 Instruct و Phi-3.5-Vision پشتیبانی می‌کند.

### **Phi-3.5-Instruct**

**تبدیل کوانتیزه INT 4 با شتاب CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**تبدیل کوانتیزه INT 4 با شتاب CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. تنظیم محیط در ترمینال

```bash

mkdir models

cd models 

```

2. دانلود microsoft/Phi-3.5-vision-instruct در پوشه models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. لطفاً این فایل‌ها را به پوشه Phi-3.5-vision-instruct خود دانلود کنید:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. این فایل را به پوشه models دانلود کنید:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. به ترمینال بروید:

   تبدیل پشتیبانی ONNX با FP32  

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **توجه:**

1. سازنده مدل در حال حاضر از تبدیل Phi-3.5-Instruct و Phi-3.5-Vision پشتیبانی می‌کند، اما از Phi-3.5-MoE پشتیبانی نمی‌کند.

2. برای استفاده از مدل کوانتیزه شده ONNX، می‌توانید از طریق SDK افزونه‌های هوش مصنوعی مولد برای onnxruntime از آن استفاده کنید.

3. ما باید به هوش مصنوعی مسئولانه‌تر توجه کنیم، بنابراین پس از تبدیل کوانتیزه مدل، توصیه می‌شود تست‌های مؤثرتری انجام شود.

4. با کوانتیزه کردن مدل CPU INT4، می‌توانیم آن را به دستگاه‌های Edge مستقر کنیم که سناریوهای کاربردی بهتری دارند، بنابراین ما Phi-3.5-Instruct را حول INT 4 تکمیل کرده‌ایم.

## **منابع**

1. اطلاعات بیشتر درباره افزونه‌های هوش مصنوعی مولد برای onnxruntime:  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. مخزن GitHub افزونه‌های هوش مصنوعی مولد برای onnxruntime:  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه ماشینی مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما تلاش می‌کنیم تا دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل اشتباهات یا نادقتی‌هایی باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا برداشت‌های نادرست ناشی از استفاده از این ترجمه نداریم.