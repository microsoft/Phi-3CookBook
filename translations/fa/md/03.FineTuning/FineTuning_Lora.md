# **تنظیم دقیق Phi-3 با Lora**

تنظیم دقیق مدل زبان Phi-3 Mini مایکروسافت با استفاده از [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) روی یک مجموعه داده سفارشی برای دستورالعمل‌های چت.

LoRA به بهبود درک مکالمه و تولید پاسخ کمک می‌کند.

## راهنمای گام‌به‌گام برای تنظیم دقیق Phi-3 Mini:

**وارد کردن و آماده‌سازی**

نصب loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

ابتدا کتابخانه‌های لازم مانند datasets، transformers، peft، trl و torch را وارد کنید. 
برای ردیابی فرآیند آموزش، ثبت لاگ را تنظیم کنید.

می‌توانید برخی از لایه‌ها را با جایگزینی آن‌ها با نسخه‌های پیاده‌سازی‌شده در loralib تنظیم کنید. در حال حاضر، فقط nn.Linear، nn.Embedding و nn.Conv2d پشتیبانی می‌شوند. همچنین، یک MergedLinear برای مواقعی که یک nn.Linear نماینده بیش از یک لایه است (مانند برخی پیاده‌سازی‌های qkv در توجه) نیز پشتیبانی می‌شود (برای اطلاعات بیشتر به یادداشت‌های اضافی مراجعه کنید).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

قبل از شروع حلقه آموزش، فقط پارامترهای LoRA را به‌عنوان قابل‌آموزش علامت‌گذاری کنید.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

هنگام ذخیره یک نقطه‌چک، یک state_dict تولید کنید که فقط شامل پارامترهای LoRA باشد.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

هنگام بارگذاری یک نقطه‌چک با استفاده از load_state_dict، مطمئن شوید که strict=False تنظیم شده باشد.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

حالا می‌توانید فرآیند آموزش را به شکل عادی ادامه دهید.

**ابرپارامترها**

دو دیکشنری تعریف کنید: training_config و peft_config. 
training_config شامل ابرپارامترهای مربوط به آموزش است، مانند نرخ یادگیری، اندازه دسته، و تنظیمات لاگ.

peft_config پارامترهای مرتبط با LoRA مانند rank، dropout و نوع وظیفه را مشخص می‌کند.

**بارگذاری مدل و توکنایزر**

مسیر مدل پیش‌آموزش‌دیده Phi-3 (مثلاً "microsoft/Phi-3-mini-4k-instruct") را مشخص کنید. تنظیمات مدل را پیکربندی کنید، از جمله استفاده از کش، نوع داده (bfloat16 برای دقت ترکیبی)، و پیاده‌سازی توجه.

**آموزش**

مدل Phi-3 را با استفاده از مجموعه داده سفارشی برای دستورالعمل‌های چت تنظیم دقیق کنید. از تنظیمات LoRA در peft_config برای انطباق کارآمد استفاده کنید. پیشرفت آموزش را با استراتژی ثبت لاگ مشخص‌شده نظارت کنید.
ارزیابی و ذخیره: مدل تنظیم‌شده را ارزیابی کنید.
نقاط‌چک را در طول آموزش برای استفاده بعدی ذخیره کنید.

**نمونه‌ها**
- [با این دفترچه نمونه بیشتر بیاموزید](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [نمونه‌ای از اسکریپت تنظیم دقیق در پایتون](../../../../code/03.Finetuning/FineTrainingScript.py)
- [نمونه‌ای از تنظیم دقیق با Hugging Face Hub و LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [نمونه کارت مدل Hugging Face - تنظیم دقیق LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [نمونه‌ای از تنظیم دقیق با Hugging Face Hub و QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه ماشینی مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما هیچ‌گونه مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.