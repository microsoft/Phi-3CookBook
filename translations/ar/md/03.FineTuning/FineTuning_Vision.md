# وصفة تحسين Phi-3.5-vision

هذا هو الدعم الرسمي لتحسين Phi-3.5-vision باستخدام مكتبات Huggingface.  
يرجى `cd` إلى دليل الكود [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) قبل تشغيل الأوامر التالية.

## التثبيت

```bash
# create a new conda environment
conda create -n phi3v python=3.10
conda activate phi3v

# install pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# other libraries needed to run the example code
pip install -r requirements.txt

# (optional) flash attention -- Ampere+ GPUs (e.g., A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (optional) QLoRA -- Turing+ GPUs (e.g., RTX 8000)
pip install bitsandbytes==0.43.1
```

## البداية السريعة

نقدم مثالين لسكربتات تحسين، أحدهما لـ DocVQA والآخر لتصنيف الصور المسيئة.

تم الاختبار على الحد الأدنى من العتاد: 4x RTX8000 (48GB RAM لكل وحدة معالجة رسومات).

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

يدعم Phi-3.5-vision الآن إدخال صور متعددة بشكل رسمي. إليك مثال لتحسين NLVR2:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## دليل الاستخدام

بناءً على العتاد المتوفر، يمكن للمستخدمين اختيار استراتيجيات تحسين مختلفة. نحن ندعم  
التحسين الكامل (مع Deepspeed Zero-2) مع إمكانية تجميد معلمات الرؤية، وLoRA (بما في ذلك QLoRA بقدرة 4bit).  
بشكل عام، نوصي باستخدام التحسين الكامل مع flash attention وbf16 كلما أمكن ذلك.

### دليل لتحويل مجموعة البيانات الخاصة بك إلى التنسيق المطلوب

نستخدم مجموعة بيانات تصنيف فيديو صغيرة (جزء من UCF-101) كمثال شامل لتوضيح كيفية تحويل مجموعة البيانات الخاصة بك إلى التنسيق المطلوب وتحسين Phi-3.5-vision عليها.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

ستبدو البيانات المحولة كما يلي:

```bash
> tree --filelimit=10 /path/to/converted_ucf101
/path/to/converted_ucf101
├── images
│   ├── test
│   │   ├── ApplyEyeMakeup [48 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [32 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [56 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [72 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [32 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [72 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [80 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [88 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [48 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [72 entries exceeds filelimit, not opening dir]
│   ├── train
│   │   ├── ApplyEyeMakeup [240 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [240 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [240 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [240 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [240 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [240 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [240 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [240 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [240 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [240 entries exceeds filelimit, not opening dir]
│   └── val
│       ├── ApplyEyeMakeup [24 entries exceeds filelimit, not opening dir]
│       ├── ApplyLipstick [24 entries exceeds filelimit, not opening dir]
│       ├── Archery [24 entries exceeds filelimit, not opening dir]
│       ├── BabyCrawling [24 entries exceeds filelimit, not opening dir]
│       ├── BalanceBeam [24 entries exceeds filelimit, not opening dir]
│       ├── BandMarching [24 entries exceeds filelimit, not opening dir]
│       ├── BaseballPitch [24 entries exceeds filelimit, not opening dir]
│       ├── Basketball [24 entries exceeds filelimit, not opening dir]
│       ├── BasketballDunk [24 entries exceeds filelimit, not opening dir]
│       └── BenchPress [24 entries exceeds filelimit, not opening dir]
├── ucf101_test.jsonl
├── ucf101_train.jsonl
└── ucf101_val.jsonl

34 directories, 3 files
```

بالنسبة لتعليقات `jsonl`، يجب أن تكون كل سطر عبارة عن قاموس مثل:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

يرجى ملاحظة أن `conversations` هي قائمة، وبالتالي يمكن دعم المحادثات متعددة الجولات إذا كانت هذه البيانات متوفرة.

## طلب زيادة حصة GPU من Azure

### المتطلبات الأساسية

حساب Azure مع دور المساهم (أو أي دور آخر يتضمن صلاحيات المساهم).

إذا لم يكن لديك حساب Azure، قم بإنشاء [حساب مجاني قبل البدء](https://azure.microsoft.com).

### طلب زيادة الحصة

يمكنك تقديم طلب لزيادة الحصة مباشرة من My quotas. اتبع الخطوات أدناه لطلب زيادة الحصة. في هذا المثال، يمكنك اختيار أي حصة قابلة للتعديل في اشتراكك.

سجل الدخول إلى [بوابة Azure](https://portal.azure.com).

أدخل "quotas" في مربع البحث، ثم اختر Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

في صفحة النظرة العامة، اختر مزوداً مثل Compute أو AML.

**ملاحظة** بالنسبة لجميع المزودين غير Compute، سترى عمود "Request increase" بدلاً من العمود "Adjustable" الموضح أدناه. هناك، يمكنك طلب زيادة لحصة معينة أو إنشاء طلب دعم لهذه الزيادة.

في صفحة My quotas، ضمن Quota name، اختر الحصة التي تريد زيادتها. تأكد من أن العمود Adjustable يعرض "Yes" لهذه الحصة.

بالقرب من أعلى الصفحة، اختر New Quota Request، ثم اختر Enter a new limit.  
![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

في جزء New Quota Request، أدخل قيمة رقمية للحد الجديد لحصتك، ثم اختر Submit.

سيتم مراجعة طلبك، وستتلقى إشعاراً إذا كان من الممكن تلبية الطلب. عادةً ما يحدث ذلك في غضون دقائق.

إذا لم يتم تلبية طلبك، سترى رابطاً لإنشاء طلب دعم. عند استخدام هذا الرابط، سيساعدك مهندس دعم في طلب الزيادة.

## اقتراحات SKU لآلات GPU من Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

إليك بعض الأمثلة:

### إذا كان لديك وحدات معالجة A100 أو H100

عادةً ما يقدم التحسين الكامل أفضل أداء. يمكنك استخدام الأمر التالي لتحسين Phi-3-V لتصنيف الصور المسيئة.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### إذا كان لديك وحدات معالجة Standard_ND40rs_v2 8x V100-32GB

لا يزال من الممكن تحسين Phi-3-V بشكل كامل لتصنيف الصور المسيئة. ومع ذلك، توقع  
معدل إنتاجية أقل بكثير مقارنة بـ A100 أو H100 بسبب عدم دعم flash attention.  
قد تتأثر الدقة أيضاً بسبب عدم دعم bf16 (يتم استخدام تدريب fp16 بدقة مختلطة بدلاً من ذلك).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### إذا لم يكن لديك وصول إلى وحدات معالجة رسومات لمراكز البيانات  
قد تكون LoRA خيارك الوحيد. يمكنك استخدام الأمر التالي لتحسين Phi-3-V لتصنيف الصور المسيئة.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

بالنسبة لوحدات معالجة Turing+، يتم دعم QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## المعلمات الموصى بها والدقة المتوقعة
### NLVR2

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_nlvr2.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

طريقة التدريب | نموذج الرؤية مجمد | نوع البيانات | رتبة LoRA | LoRA alpha | حجم الدفعة | معدل التعلم | عدد العصور | الدقة
--- | --- | --- | --- | --- | --- | --- | --- | --- |
التحسين الكامل |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
التحسين الكامل | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
نتائج LoRA قريباً |  |  |  |  |  |  |  |  |

### ملاحظة
النتائج أدناه لـ DocVQA وتصنيف الصور المسيئة تستند إلى النسخة السابقة (Phi-3-vision).  
سيتم تحديث النتائج الجديدة مع Phi-3.5-vision قريباً.

### DocVQA (ملاحظة: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_docvqa.py \
  --full_train \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

طريقة التدريب | نوع البيانات | رتبة LoRA | LoRA alpha | حجم الدفعة | معدل التعلم | عدد العصور | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
التحسين الكامل | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
التحسين الكامل | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
نموذج صورة مجمد | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
نموذج صورة مجمد | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### تصنيف الصور المسيئة (ملاحظة: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

طريقة التدريب | نوع البيانات | رتبة LoRA | LoRA alpha | حجم الدفعة | معدل التعلم | عدد العصور | الدقة
--- | --- | --- | --- | --- | --- | --- | --- |
التحسين الكامل | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
التحسين الكامل | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
نموذج صورة مجمد | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
نموذج صورة مجمد | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## قياس السرعة (ملاحظة: Phi-3-vision)

سيتم تحديث نتائج قياس السرعة الجديدة مع Phi-3.5-vision قريباً.

تم قياس السرعة باستخدام مجموعة بيانات DocVQA. متوسط طول التسلسل لهذه المجموعة  
هو 2443.23 رمزاً (باستخدام `num_crops=16` لنموذج الصورة).

### 8x A100-80GB (Ampere)

طريقة التدريب | \# العقد | وحدات معالجة الرسومات | flash attention | حجم الدفعة الفعّال | معدل الإنتاجية (img/s) | التسريع | أقصى ذاكرة GPU (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
التحسين الكامل | 1 | 8 |  | 64 | 5.041 | 1x | ~42
التحسين الكامل | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
التحسين الكامل | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
التحسين الكامل | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
نموذج صورة مجمد | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
نموذج صورة مجمد | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

طريقة التدريب | \# العقد | وحدات معالجة الرسومات | flash attention | حجم الدفعة الفعّال | معدل الإنتاجية (img/s) | التسريع | أقصى ذاكرة GPU (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
التحسين الكامل | 1 | 8 | | 64 | 2.462 | 1x | ~32
التحسين الكامل | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
التحسين الكامل | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
نموذج صورة مجمد | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## المشكلات المعروفة

- لا يمكن تشغيل flash attention مع fp16 (يوصى دائماً باستخدام bf16 عند توفره، وجميع وحدات معالجة الرسومات التي تدعم flash attention تدعم أيضاً bf16).  
- لا يوجد دعم لحفظ نقاط التحقق الوسيطة واستئناف التدريب حتى الآن.  

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمات الترجمة الآلية المعتمدة على الذكاء الاصطناعي. بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.