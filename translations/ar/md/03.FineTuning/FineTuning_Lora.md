# **تخصيص Phi-3 باستخدام LoRA**

تخصيص نموذج اللغة Phi-3 Mini من مايكروسوفت باستخدام [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) على مجموعة بيانات مخصصة لتعليمات المحادثة.

يساعد LoRA في تحسين فهم المحادثات وتوليد الردود.

## دليل خطوة بخطوة لتخصيص Phi-3 Mini:

**الاستيرادات والإعداد**

تثبيت مكتبة loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

ابدأ باستيراد المكتبات الضرورية مثل datasets، transformers، peft، trl، وtorch. قم بإعداد تسجيل العمليات لتتبع عملية التدريب.

يمكنك اختيار تعديل بعض الطبقات عن طريق استبدالها بنظيراتها التي تم تنفيذها في loralib. حالياً، ندعم فقط nn.Linear، nn.Embedding، وnn.Conv2d. كما ندعم MergedLinear للحالات التي تمثل فيها nn.Linear واحدة أكثر من طبقة، كما هو الحال في بعض تنفيذات إسقاط qkv للانتباه (راجع الملاحظات الإضافية للمزيد).

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

قبل بدء حلقة التدريب، قم بتحديد معلمات LoRA فقط كمعلمات قابلة للتدريب.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

عند حفظ نقطة تحقق، قم بإنشاء state_dict يحتوي فقط على معلمات LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

عند تحميل نقطة تحقق باستخدام load_state_dict، تأكد من تعيين strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

الآن يمكن أن تستمر عملية التدريب كالمعتاد.

**المعلمات الفائقة**

حدد قاموسين: training_config وpeft_config. يحتوي training_config على معلمات التدريب، مثل معدل التعلم، حجم الدفعة، وإعدادات التسجيل.

peft_config يحدد معلمات LoRA مثل الرتبة، الإسقاط، ونوع المهمة.

**تحميل النموذج والمُرمِّز**

حدد المسار إلى نموذج Phi-3 المدرب مسبقاً (على سبيل المثال، "microsoft/Phi-3-mini-4k-instruct"). قم بتكوين إعدادات النموذج، بما في ذلك استخدام التخزين المؤقت، نوع البيانات (bfloat16 للدقة المختلطة)، وتنفيذ الانتباه.

**التدريب**

قم بتخصيص نموذج Phi-3 باستخدام مجموعة بيانات تعليمات المحادثة المخصصة. استخدم إعدادات LoRA من peft_config لتحقيق التكيف بكفاءة. راقب تقدم التدريب باستخدام استراتيجية التسجيل المحددة.

التقييم والحفظ: قم بتقييم النموذج المخصص.
احفظ نقاط التحقق أثناء التدريب لاستخدامها لاحقاً.

**أمثلة**
- [تعرف على المزيد من خلال هذا الدفتر التوضيحي](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [مثال على تخصيص Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [مثال على تخصيص Hugging Face Hub باستخدام LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [مثال على بطاقة نموذج Hugging Face - تخصيص LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [مثال على تخصيص Hugging Face Hub باستخدام QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمات الترجمة الآلية بالاعتماد على الذكاء الاصطناعي. بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الرسمي والموثوق. للحصول على معلومات حساسة أو حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة قد تنشأ عن استخدام هذه الترجمة.