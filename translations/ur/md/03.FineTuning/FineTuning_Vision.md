# Phi-3.5-vision فائن ٹیوننگ ترکیب

یہ Phi-3.5-vision کو فائن ٹیوننگ کرنے کے لیے huggingface لائبریریز کی آفیشل سپورٹ ہے۔  
براہ کرم درج ذیل کمانڈز چلانے سے پہلے کوڈ ڈائریکٹری [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) پر `cd` کریں۔

## انسٹالیشن

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

## فوری آغاز

ہم دو مثال کے اسکرپٹس فراہم کرتے ہیں، ایک DocVQA کے لیے اور دوسرا hateful meme classification کے لیے۔

کم از کم ہارڈویئر: 4x RTX8000 (ہر GPU پر 48GB RAM)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision اب سرکاری طور پر ملٹی امیج ان پٹ کو سپورٹ کرتا ہے۔ یہاں NLVR2 کے لیے فائن ٹیوننگ کی ایک مثال دی گئی ہے:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## استعمال کی رہنمائی

ہارڈویئر کے مطابق، صارفین مختلف فائن ٹیوننگ حکمت عملیوں کا انتخاب کر سکتے ہیں۔ ہم مکمل فائن ٹیوننگ (Deepspeed Zero-2 کے ساتھ) کی سپورٹ فراہم کرتے ہیں، جس میں ویژن کے پیرامیٹرز کو فریز کرنے کا آپشن شامل ہے، اور LoRA (4bit QLoRA سمیت)۔  
عام طور پر، ہم فلیش اٹینشن اور bf16 کے ساتھ مکمل فائن ٹیوننگ کی سفارش کرتے ہیں جب بھی ممکن ہو۔

### آپ کے کسٹم ڈیٹا سیٹ کو مطلوبہ فارمیٹ میں تبدیل کرنے کی رہنمائی

ہم ایک کم از کم ویڈیو کلاسیفکیشن ڈیٹا سیٹ (UCF-101 کا ایک سب سیٹ) کو بطور اینڈ ٹو اینڈ مثال استعمال کرتے ہیں تاکہ دکھا سکیں کہ آپ کے کسٹم ڈیٹا سیٹ کو مطلوبہ فارمیٹ میں کیسے تبدیل کیا جائے اور Phi-3.5-vision پر فائن ٹیون کیا جائے۔

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

تبدیل شدہ ڈیٹا اس طرح نظر آئے گا:

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

`jsonl` اینوٹیشن کے لیے، ہر لائن ایک ڈکشنری ہونی چاہیے جیسا کہ:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

نوٹ کریں کہ `conversations` ایک فہرست ہے، اس لیے اگر ایسا ڈیٹا دستیاب ہو تو ملٹی ٹرن گفتگو کو سپورٹ کیا جا سکتا ہے۔

## Azure GPU کوٹا کی درخواست کرنا

### پیشگی ضروریات

ایک Azure اکاؤنٹ جس میں Contributor رول ہو (یا کوئی اور رول جس میں Contributor تک رسائی شامل ہو)۔  
اگر آپ کے پاس Azure اکاؤنٹ نہیں ہے، تو [یہاں مفت اکاؤنٹ بنائیں](https://azure.microsoft.com)۔

### کوٹا میں اضافہ کی درخواست

آپ My quotas سے براہ راست کوٹا میں اضافہ کی درخواست جمع کر سکتے ہیں۔ نیچے دیے گئے مراحل پر عمل کریں تاکہ کوٹا میں اضافہ کی درخواست دی جا سکے۔ اس مثال کے لیے، آپ اپنی سبسکرپشن میں کسی بھی ایڈجسٹ ایبل کوٹا کا انتخاب کر سکتے ہیں۔

Azure پورٹل پر سائن ان کریں: [Azure portal](https://portal.azure.com)۔

سرچ باکس میں "quotas" ٹائپ کریں اور پھر Quotas کو منتخب کریں۔  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Overview صفحے پر، ایک پرووائیڈر منتخب کریں، جیسے Compute یا AML۔

**نوٹ:** Compute کے علاوہ دیگر پرووائیڈرز کے لیے، آپ کو Adjustable کالم کی بجائے Request increase کالم نظر آئے گا۔ وہاں، آپ کسی خاص کوٹا کے لیے اضافہ کی درخواست دے سکتے ہیں یا اضافہ کی درخواست کے لیے سپورٹ ریکویسٹ بنا سکتے ہیں۔

My quotas صفحے پر، Quota name کے تحت، اس کوٹا کو منتخب کریں جسے آپ بڑھانا چاہتے ہیں۔ اس بات کو یقینی بنائیں کہ Adjustable کالم میں اس کوٹا کے لیے "Yes" دکھایا جا رہا ہے۔

صفحے کے اوپر New Quota Request کو منتخب کریں، پھر Enter a new limit کو منتخب کریں۔  
![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request پین میں، اپنے نئے کوٹا لیمٹ کے لیے ایک عددی قدر درج کریں، پھر Submit کو منتخب کریں۔

آپ کی درخواست کا جائزہ لیا جائے گا، اور آپ کو مطلع کیا جائے گا کہ آیا درخواست کو پورا کیا جا سکتا ہے۔ یہ عام طور پر چند منٹوں میں ہوتا ہے۔

اگر آپ کی درخواست پوری نہیں ہوتی، تو آپ کو سپورٹ ریکویسٹ بنانے کے لیے ایک لنک نظر آئے گا۔ جب آپ اس لنک کا استعمال کرتے ہیں، تو ایک سپورٹ انجینئر آپ کو آپ کی اضافہ کی درخواست میں مدد کرے گا۔

## Azure Compute GPU مشین SKU تجاویز

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)  
[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)  
[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

یہاں کچھ مثالیں دی گئی ہیں:

### اگر آپ کے پاس A100 یا H100 GPUs ہیں

مکمل فائن ٹیوننگ عام طور پر بہترین کارکردگی دیتی ہے۔ آپ مندرجہ ذیل کمانڈ استعمال کر سکتے ہیں hateful memes classification پر Phi-3-V کو فائن ٹیون کرنے کے لیے۔

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### اگر آپ کے پاس Standard_ND40rs_v2 8x V100-32GB GPUs ہیں

Phi-3-V کو hateful memes classification پر مکمل طور پر فائن ٹیون کرنا اب بھی ممکن ہے۔  
تاہم، A100 یا H100 GPUs کے مقابلے میں کم throughput کی توقع کریں کیونکہ فلیش اٹینشن سپورٹ نہیں ہے۔  
bf16 سپورٹ کی عدم موجودگی کی وجہ سے درستگی بھی متاثر ہو سکتی ہے (fp16 مکسڈ-پریسیژن ٹریننگ استعمال کی جاتی ہے)۔

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### اگر آپ کے پاس ڈیٹا سینٹر GPUs تک رسائی نہیں ہے

LoRA آپ کا واحد انتخاب ہو سکتا ہے۔ آپ مندرجہ ذیل کمانڈ استعمال کر سکتے ہیں hateful memes classification پر Phi-3-V کو فائن ٹیون کرنے کے لیے۔

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU کے لیے QLoRA سپورٹ ہے۔

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## تجویز کردہ ہائپر پیرامیٹرز اور متوقع درستگی

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

Training method | Frozen vision model | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
LoRA results comming soon |  |  |  |  |  |  |  |  |

### نوٹ  
نیچے دیے گئے DocVQA اور Hateful memes کے نتائج پچھلے ورژن (Phi-3-vision) پر مبنی ہیں۔  
Phi-3.5-vision کے ساتھ نئے نتائج جلد اپ ڈیٹ کیے جائیں گے۔

### DocVQA (نوٹ: Phi-3-vision)

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

Training method | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
frozen image model | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
frozen image model | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (نوٹ: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Training method | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
frozen image model | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
frozen image model | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## رفتار کا موازنہ (نوٹ: Phi-3-vision)

Phi-3.5-vision کے ساتھ نئے رفتار کے موازنے کے نتائج جلد اپ ڈیٹ کیے جائیں گے۔

رفتار کا موازنہ DocVQA ڈیٹا سیٹ پر کیا گیا ہے۔ اس ڈیٹا سیٹ کی اوسط سیکوینس لمبائی 2443.23 ٹوکنز ہے (`num_crops=16` کے ساتھ)۔

### 8x A100-80GB (Ampere)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
frozen image model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
frozen image model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## معلوم مسائل

- fp16 کے ساتھ فلیش اٹینشن نہیں چلایا جا سکتا (bf16 ہمیشہ تجویز کیا جاتا ہے جب دستیاب ہو، اور تمام GPUs جو فلیش اٹینشن کو سپورٹ کرتے ہیں وہ bf16 کو بھی سپورٹ کرتے ہیں)۔  
- درمیانی چیک پوائنٹس کو محفوظ کرنے اور ٹریننگ دوبارہ شروع کرنے کی فی الحال سپورٹ نہیں ہے۔  

**ڈسکلیمر**:  
یہ دستاویز مشین پر مبنی اے آئی ترجمہ خدمات کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غلط بیانی ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔