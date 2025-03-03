# מתכון לכיוונון עדין של Phi-3.5-vision

זהו המדריך הרשמי לתמיכה בכיוונון עדין של Phi-3.5-vision באמצעות ספריות huggingface.  
אנא `cd` לספריית הקוד [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) לפני הרצת הפקודות הבאות.

## התקנה

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

## התחלה מהירה

אנו מספקים שני סקריפטים לדוגמה לכיוונון עדין, אחד עבור DocVQA והשני עבור סיווג ממים פוגעניים.  

נבדק על חומרה מינימלית של 4x RTX8000 (48GB RAM לכל GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

כעת Phi-3.5-vision תומך באופן רשמי בקלטים מרובי-תמונות. הנה דוגמה לכיוונון עדין עבור NLVR2:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## מדריך שימוש

בהתאם לחומרה הזמינה, משתמשים יכולים לבחור אסטרטגיות שונות לכיוונון עדין. אנו תומכים בכיוונון מלא (עם Deepspeed Zero-2) עם אפשרות להקפיא את פרמטרי המודל הוויזואלי, וב-LoRA (כולל QLoRA ב-4bit).  
באופן כללי, אנו ממליצים להשתמש בכיוונון מלא עם flash attention ו-bf16 בכל פעם שזה אפשרי.

### מדריך להמרת מערך נתונים מותאם אישית לפורמט הנדרש

אנו משתמשים במערך נתונים מינימלי לסיווג וידאו (תת-קבוצה של UCF-101) כדוגמה מקצה לקצה להדגים כיצד להמיר את מערך הנתונים המותאם אישית לפורמט הנדרש ולבצע כיוונון עדין של Phi-3.5-vision עליו.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

הנתונים המומרים ייראו כך:

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

עבור ההערות בפורמט `jsonl`, כל שורה צריכה להיות מילון בצורה הבאה:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

שימו לב ש-`conversations` הוא רשימה, כך שניתן לתמוך בשיחות מרובות סבבים אם יש נתונים כאלה זמינים.

## בקשת מכסת GPU ב-Azure

### דרישות מוקדמות

חשבון Azure עם תפקיד Contributor (או תפקיד אחר הכולל גישת Contributor).  

אם אין לכם חשבון Azure, צרו [חשבון חינמי לפני שתתחילו](https://azure.microsoft.com).

### בקשת הגדלת מכסה

ניתן להגיש בקשה להגדלת מכסה ישירות מתוך My quotas. בצעו את השלבים הבאים כדי לבקש הגדלה למכסה. בדוגמה זו, ניתן לבחור כל מכסה מתכווננת במנוי שלכם.  

היכנסו ל-[פורטל Azure](https://portal.azure.com).  

הקלידו "quotas" בתיבת החיפוש, ולאחר מכן בחרו Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

בעמוד Overview, בחרו ספק, לדוגמה Compute או AML.  

**שימו לב** עבור כל הספקים למעט Compute, תראו עמודה בשם Request increase במקום העמודה Adjustable שמתוארת למטה. שם תוכלו לבקש הגדלה למכסה מסוימת או ליצור בקשת תמיכה להגדלה.  

בעמוד My quotas, תחת Quota name, בחרו במכסה שברצונכם להגדיל. ודאו שהעמודה Adjustable מציינת Yes עבור מכסה זו.  

בקרבת החלק העליון של העמוד, בחרו New Quota Request, ואז בחרו Enter a new limit.  

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

בחלונית New Quota Request, הזינו ערך מספרי עבור גבול המכסה החדש שלכם, ואז בחרו Submit.  

הבקשה שלכם תיבדק, ותקבלו הודעה אם ניתן לאשר את הבקשה. בדרך כלל זה מתבצע תוך דקות ספורות.  

אם הבקשה שלכם לא מאושרת, תראו קישור ליצירת בקשת תמיכה. כאשר תשתמשו בקישור זה, מהנדס תמיכה יסייע לכם בבקשת ההגדלה שלכם.

## הצעות למכונות GPU ב-Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)  

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)  

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)  

הנה כמה דוגמאות:

### אם יש לכם GPUs מסוג A100 או H100

כיוונון מלא בדרך כלל נותן את הביצועים הטובים ביותר. ניתן להשתמש בפקודה הבאה לכיוונון Phi-3-V עבור סיווג ממים פוגעניים:

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### אם יש לכם GPUs מסוג Standard_ND40rs_v2 8x V100-32GB

עדיין ניתן לבצע כיוונון מלא של Phi-3-V עבור סיווג ממים פוגעניים. עם זאת, צפו לתפוקה נמוכה יותר בהשוואה ל-GPUs מסוג A100 או H100 בשל היעדר תמיכה ב-flash attention.  
גם הדיוק עשוי להיפגע בשל היעדר תמיכה ב-bf16 (במקום זאת נעשה שימוש ב-fp16 לאימון בדיוק מעורב).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### אם אין לכם גישה ל-GPUs במרכזי נתונים
LoRA עשוי להיות האפשרות היחידה שלכם. ניתן להשתמש בפקודה הבאה לכיוונון Phi-3-V עבור סיווג ממים פוגעניים:

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

עבור GPUs מסוג Turing+ נתמכת QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## פרמטרים מומלצים ותוצאות צפויות
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

שיטת אימון | מודל ויזואלי מוקפא | סוג נתונים | דרגת LoRA | LoRA alpha | גודל מיני-אצווה | קצב למידה | מספר אפוכים | דיוק
--- | --- | --- | --- | --- | --- | --- | --- | --- |
כיוונון מלא |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
כיוונון מלא | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
תוצאות LoRA יגיעו בקרוב |  |  |  |  |  |  |  |  |

### הערה
תוצאות DocVQA וממים פוגעניים להלן מבוססות על הגרסה הקודמת (Phi-3-vision).  
התוצאות החדשות עם Phi-3.5-vision יעודכנו בקרוב.

### DocVQA (הערה: Phi-3-vision)

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

שיטת אימון | סוג נתונים | דרגת LoRA | LoRA alpha | גודל מיני-אצווה | קצב למידה | מספר אפוכים | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
כיוונון מלא | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
כיוונון מלא | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
מודל תמונה מוקפא | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
מודל תמונה מוקפא | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### ממים פוגעניים (הערה: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

שיטת אימון | סוג נתונים | דרגת LoRA | LoRA alpha | גודל מיני-אצווה | קצב למידה | מספר אפוכים | דיוק
--- | --- | --- | --- | --- | --- | --- | --- |
כיוונון מלא | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
כיוונון מלא | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
מודל תמונה מוקפא | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
מודל תמונה מוקפא | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## בדיקות מהירות (הערה: Phi-3-vision)

תוצאות בדיקות המהירות החדשות עם Phi-3.5-vision יעודכנו בקרוב.  

בדיקות המהירות בוצעו על מערך הנתונים DocVQA. אורך הרצף הממוצע במערך זה הוא 2443.23 טוקנים (בשימוש `num_crops=16` עבור מודל התמונה).

### 8x A100-80GB (Ampere)

שיטת אימון | \# צמתים | GPUs | flash attention | גודל מיני-אצווה אפקטיבי | תפוקה (תמונות/שנייה) | האצה | זיכרון GPU שיא (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
כיוונון מלא | 1 | 8 |  | 64 | 5.041 |  1x | ~42
כיוונון מלא | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
כיוונון מלא | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
כיוונון מלא | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
מודל תמונה מוקפא | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
מודל תמונה מוקפא | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

שיטת אימון | \# צמתים | GPUs | flash attention | גודל מיני-אצווה אפקטיבי | תפוקה (תמונות/שנייה) | האצה | זיכרון GPU שיא (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
כיוונון מלא | 1 | 8 | | 64 | 2.462 |  1x | ~32
כיוונון מלא | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
כיוונון מלא | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
מודל תמונה מוקפא | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## בעיות ידועות

- לא ניתן להריץ flash attention עם fp16 (bf16 תמיד מומלץ כשזמין, וכל ה-GPUs התומכים ב-flash attention תומכים גם ב-bf16).  
- אין תמיכה בשמירת נקודות בדיקה ביניים ובחידוש אימון בשלב זה.  

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים לכלול שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו אחראים לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.