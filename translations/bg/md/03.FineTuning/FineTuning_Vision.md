# Phi-3.5-vision рецепта за фина настройка

Това е официалната поддръжка за фина настройка на Phi-3.5-vision с помощта на библиотеките на huggingface.  
Моля, `cd` към директорията с кода [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning), преди да изпълните следните команди.

## Инсталация

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

## Бърз старт

Предоставяме два примерни скрипта за фина настройка: един за DocVQA и един за класификация на обидни мемове.

Минимален тестван хардуер: 4x RTX8000 (48GB RAM на GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision вече официално поддържа входове с множество изображения. Ето пример за фина настройка за NLVR2:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Ръководство за използване

В зависимост от хардуера потребителите могат да изберат различни стратегии за фина настройка. Поддържаме пълна фина настройка (с Deepspeed Zero-2) с опционално замразени параметри за визия, както и LoRA (включително 4bit QLoRA).  
Обикновено препоръчваме използването на пълна фина настройка с flash attention и bf16, когато е възможно.

### Ръководство за конвертиране на вашия персонализиран набор от данни във формата, който е необходим

Използваме минимален набор от данни за видео класификация (подмножество на UCF-101) като пример от край до край, за да демонстрираме как да конвертирате вашия персонализиран набор от данни във необходимия формат и да настроите Phi-3.5-vision върху него.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Конвертираните данни ще изглеждат така:

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

За анотацията `jsonl`, всеки ред трябва да бъде речник като този:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Имайте предвид, че `conversations` е списък, което означава, че може да се поддържа многопосочен разговор, ако такива данни са налични.

## Искане за GPU квота в Azure

### Предварителни изисквания

Акаунт в Azure с роля на Contributor (или друга роля, която включва достъп на Contributor).  

Ако нямате акаунт в Azure, създайте [безплатен акаунт преди да започнете](https://azure.microsoft.com).

### Искане за увеличение на квотата

Можете да подадете заявка за увеличение на квотата директно от My quotas. Следвайте стъпките по-долу, за да поискате увеличение на квотата. За този пример можете да изберете всяка регулируема квота във вашия абонамент.

Влезте в [портала на Azure](https://portal.azure.com).

Въведете "quotas" в полето за търсене и след това изберете Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

На страницата Overview изберете доставчик, например Compute или AML.

**Забележка** За всички доставчици, различни от Compute, ще видите колона Request increase вместо Adjustable column, описана по-долу. Там можете да поискате увеличение за конкретна квота или да създадете заявка за поддръжка за увеличението.

На страницата My quotas, под Quota name, изберете квотата, която искате да увеличите. Уверете се, че колоната Adjustable показва Yes за тази квота.

В горната част на страницата изберете New Quota Request, след което изберете Enter a new limit.  
![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

В панела New Quota Request въведете числена стойност за новия си лимит на квотата и след това изберете Submit.

Вашата заявка ще бъде прегледана и ще бъдете уведомени дали заявката може да бъде изпълнена. Това обикновено става в рамките на няколко минути.

Ако вашата заявка не бъде изпълнена, ще видите връзка за създаване на заявка за поддръжка. Когато използвате тази връзка, инженер по поддръжката ще ви помогне с вашата заявка за увеличение.

## Препоръчителни SKU за GPU машини в Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Ето няколко примера:

### Ако имате A100 или H100 GPU

Пълната фина настройка обикновено дава най-добра производителност. Можете да използвате следната команда, за да настроите Phi-3-V за класификация на обидни мемове.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Ако имате Standard_ND40rs_v2 8x V100-32GB GPU

Все още е възможно да настроите Phi-3-V за класификация на обидни мемове. Въпреки това, очаквайте много по-ниска пропускателна способност в сравнение с A100 или H100 GPU поради липсата на поддръжка за flash attention. Точността също може да бъде засегната поради липсата на поддръжка за bf16 (използва се fp16 смесено-прецизно обучение).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Ако нямате достъп до GPU в центрове за данни

LoRA може да бъде единствената ви опция. Можете да използвате следната команда, за да настроите Phi-3-V за класификация на обидни мемове.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

За GPU от поколението Turing+ се поддържа QLoRA.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Препоръчителни хиперпараметри и очаквана точност

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

Метод на обучение | Замразен модел за визия | Тип данни | LoRA ранг | LoRA alpha | Размер на партидата | Скорост на обучение | Епохи | Точност  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
пълна фина настройка |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
пълна фина настройка | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
Резултати за LoRA скоро |  |  |  |  |  |  |  |  |

### ЗАБЕЛЕЖКА  
Резултатите по-долу за DocVQA и обидни мемове са базирани на предишната версия (Phi-3-vision).  
Новите резултати с Phi-3.5-vision ще бъдат актуализирани скоро.

### DocVQA (ЗАБЕЛЕЖКА: Phi-3-vision)

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

Метод на обучение | Тип данни | LoRA ранг | LoRA alpha | Размер на партидата | Скорост на обучение | Епохи | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
пълна фина настройка | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
пълна фина настройка | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
замразен модел за изображения | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
замразен модел за изображения | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  

### Обидни мемове (ЗАБЕЛЕЖКА: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Метод на обучение | Тип данни | LoRA ранг | LoRA alpha | Размер на партидата | Скорост на обучение | Епохи | Точност  
--- | --- | --- | --- | --- | --- | --- | --- |  
пълна фина настройка | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
пълна фина настройка | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
замразен модел за изображения | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
замразен модел за изображения | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |  

## Бенчмаркинг на скорост (ЗАБЕЛЕЖКА: Phi-3-vision)

Новите резултати за бенчмаркинг с Phi-3.5-vision ще бъдат актуализирани скоро.

Бенчмаркингът на скорост е извършен върху набора от данни DocVQA. Средната дължина на последователностите в този набор е 2443.23 токена (използвайки `num_crops=16` за модела за изображения).

### 8x A100-80GB (Ampere)

Метод на обучение | \# възли | GPU-та | flash attention | Ефективен размер на партидата | Пропускателна способност (img/s) | Ускорение | Пикова GPU памет (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
пълна фина настройка | 1 | 8 |  | 64 | 5.041 |  1x | ~42  
пълна фина настройка | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
пълна фина настройка | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
пълна фина настройка | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
замразен модел за изображения | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
замразен модел за изображения | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Метод на обучение | \# възли | GPU-та | flash attention | Ефективен размер на партидата | Пропускателна способност (img/s) | Ускорение | Пикова GPU памет (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
пълна фина настройка | 1 | 8 | | 64 | 2.462 |  1x | ~32  
пълна фина настройка | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
пълна фина настройка | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
замразен модел за изображения | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Известни проблеми

- Flash attention не може да работи с fp16 (bf16 винаги се препоръчва, когато е наличен, и всички GPU-та, които поддържат flash attention, също поддържат bf16).  
- Все още не се поддържа запазване на междинни чекпойнтове и възобновяване на обучението.

**Отказ от отговорност**:  
Този документ е преведен с помощта на машинни AI услуги за превод. Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия оригинален език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален превод от човек. Не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.