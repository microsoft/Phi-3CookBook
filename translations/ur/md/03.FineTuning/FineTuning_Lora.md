# **لورا کے ساتھ Phi-3 کو فائن ٹون کرنا**

مائیکروسافٹ کے Phi-3 Mini لینگویج ماڈل کو [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) کے ذریعے ایک حسب ضرورت چیٹ انسٹرکشن ڈیٹاسیٹ پر فائن ٹون کرنا۔

لورا چیٹ کے مواد کو بہتر سمجھنے اور جواب دینے کی صلاحیت کو بہتر بنائے گا۔

## Phi-3 Mini کو فائن ٹون کرنے کا مرحلہ وار طریقہ:

**امپورٹس اور سیٹ اپ**

loralib انسٹال کرنا

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

سب سے پہلے ضروری لائبریریاں امپورٹ کریں، جیسے کہ datasets، transformers، peft، trl، اور torch۔  
ٹریننگ کے عمل کو ٹریک کرنے کے لیے لاگنگ سیٹ اپ کریں۔

آپ کچھ لیئرز کو لورا لائبریری میں موجود متبادل کے ساتھ تبدیل کر سکتے ہیں۔ فی الحال، ہم صرف nn.Linear، nn.Embedding، اور nn.Conv2d کو سپورٹ کرتے ہیں۔ اس کے علاوہ، ہم MergedLinear کو بھی سپورٹ کرتے ہیں، جو ان کیسز کے لیے ہے جہاں ایک nn.Linear کئی لیئرز کی نمائندگی کرتا ہے، جیسا کہ کچھ attention qkv projection implementations میں ہوتا ہے (مزید معلومات کے لیے اضافی نوٹس دیکھیں)۔

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

loralib کو امپورٹ کریں:

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

ٹریننگ لوپ شروع ہونے سے پہلے، صرف LoRA پیرامیٹرز کو ٹرین ایبل کے طور پر نشان زد کریں۔

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

چیک پوائنٹ محفوظ کرتے وقت، ایسا state_dict تیار کریں جو صرف LoRA پیرامیٹرز پر مشتمل ہو۔

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

چیک پوائنٹ لوڈ کرتے وقت، load_state_dict استعمال کریں اور strict=False سیٹ کریں۔

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

اب ٹریننگ عام طریقے سے شروع کی جا سکتی ہے۔

**ہائپرپیرامیٹرز**

دو ڈکشنریاں ڈیفائن کریں: training_config اور peft_config۔  
training_config میں ٹریننگ کے ہائپرپیرامیٹرز شامل ہوں گے، جیسے کہ لرننگ ریٹ، بیچ سائز، اور لاگنگ سیٹنگز۔

peft_config لورا سے متعلق پیرامیٹرز جیسے rank، dropout، اور task type کو سپیسیفائی کرے گا۔

**ماڈل اور ٹوکنائزر لوڈ کرنا**

پہلے سے ٹرین شدہ Phi-3 ماڈل کا راستہ سپیسیفائی کریں (مثال کے طور پر، "microsoft/Phi-3-mini-4k-instruct")۔  
ماڈل کی سیٹنگز کنفیگر کریں، جن میں cache کا استعمال، ڈیٹا ٹائپ (mixed precision کے لیے bfloat16)، اور attention implementation شامل ہیں۔

**ٹریننگ**

Phi-3 ماڈل کو حسب ضرورت چیٹ انسٹرکشن ڈیٹاسیٹ پر فائن ٹون کریں۔  
لورا سیٹنگز کو peft_config سے استعمال کریں تاکہ ایفی شینٹ ایڈاپٹیشن ممکن ہو سکے۔  
ٹریننگ کی پیش رفت کو مانیٹر کریں، جیسا کہ لاگنگ اسٹریٹجی میں سپیسیفائی کیا گیا ہے۔

**ایویلیوایشن اور سیونگ**

فائن ٹون کیے گئے ماڈل کا جائزہ لیں۔  
ٹریننگ کے دوران چیک پوائنٹس محفوظ کریں تاکہ بعد میں استعمال ہو سکیں۔

**نمونے**
- [اس نمونہ نوٹ بک سے مزید سیکھیں](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python فائن ٹوننگ کا نمونہ](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub پر لورا کے ساتھ فائن ٹوننگ کی مثال](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face ماڈل کارڈ کی مثال - لورا فائن ٹوننگ](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub پر QLORA کے ساتھ فائن ٹوننگ کی مثال](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**ڈس کلیمر**:  
یہ دستاویز مشین پر مبنی AI ترجمہ خدمات کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غلط فہمیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔