# Phi-3.5-vision finetuning-recept

Det här är den officiella guiden för finetuning av Phi-3.5-vision med hjälp av huggingface-bibliotek.
Gå till kodkatalogen [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) innan du kör följande kommandon.

## Installation

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

## Snabbstart

Vi tillhandahåller två exempel på finetuning-skript, ett för DocVQA och ett för klassificering av hatiska memes.

Minimal hårdvara som har testats är 4x RTX8000 (48GB RAM per GPU).

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision stöder nu officiellt indata med flera bilder. Här är ett exempel för finetuning av NLVR2.

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Användarguide

Beroende på hårdvaran kan användare välja olika finetuning-strategier. Vi stöder fullständig finetuning (med Deepspeed Zero-2) med möjlighet att frysa vision-parametrar, samt LoRA (inklusive 4bit QLoRA). Generellt rekommenderar vi att använda fullständig finetuning med flash attention och bf16 när det är möjligt.

### Guide för att konvertera ditt egna dataset till rätt format

Vi använder ett minimalt dataset för videoklassificering (en delmängd av UCF-101) som ett end-to-end-exempel för att visa hur du kan konvertera ditt eget dataset till rätt format och finetuna Phi-3.5-vision på det.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Den konverterade datan kommer att se ut så här:

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

För `jsonl`-annoteringen bör varje rad vara en ordbok som:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Observera att `conversations` är en lista, vilket innebär att fleromgångs-konversationer kan stödjas om sådan data finns tillgänglig.

## Begära Azure GPU-kvot 

### Förutsättningar

Ett Azure-konto med Contributor-roll (eller annan roll som inkluderar Contributor-åtkomst).

Om du inte har ett Azure-konto kan du skapa ett [gratis konto innan du börjar](https://azure.microsoft.com).

### Begäran om kvotökning

Du kan skicka en begäran om kvotökning direkt från Mina kvoter. Följ stegen nedan för att begära en ökning av en kvot. För det här exemplet kan du välja vilken justerbar kvot som helst i ditt abonnemang.

Logga in på [Azure-portalen](https://portal.azure.com).

Skriv "kvoter" i sökrutan och välj sedan Kvoter.  
![Kvot](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

På översiktssidan väljer du en leverantör, till exempel Compute eller AML.

**Notera** För alla leverantörer utom Compute ser du en kolumn med "Begär ökning" istället för kolumnen "Justerbar" som beskrivs nedan. Där kan du begära en ökning för en specifik kvot eller skapa en supportbegäran för ökningen.

På sidan Mina kvoter, under Kvotnamn, välj den kvot du vill öka. Kontrollera att kolumnen Justerbar visar Ja för denna kvot.

Högst upp på sidan, välj Ny kvotbegäran och sedan Ange en ny gräns.

![Öka kvot](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

I panelen Ny kvotbegäran, ange ett numeriskt värde för din nya kvotgräns och välj sedan Skicka.

Din begäran kommer att granskas och du får besked om begäran kan uppfyllas. Detta sker vanligtvis inom några minuter.

Om din begäran inte uppfylls, ser du en länk för att skapa en supportbegäran. När du använder den här länken kommer en supportingenjör att hjälpa dig med din begäran om ökning.

## Förslag på Azure Compute GPU-maskin SKU

[ND A100 v4-serien](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-serien](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Här är några exempel:

### Om du har A100- eller H100-GPU:er

Fullständig finetuning ger vanligtvis bäst prestanda. Du kan använda följande kommando för att finetuna Phi-3-V på klassificering av hatiska memes.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Om du har Standard_ND40rs_v2 8x V100-32GB GPU:er

Det är fortfarande möjligt att fullt ut finetuna Phi-3-V på klassificering av hatiska memes. Men förvänta dig mycket lägre genomströmning jämfört med A100- eller H100-GPU:er på grund av brist på stöd för flash attention. Noggrannheten kan också påverkas på grund av brist på bf16-stöd (fp16 mixed-precision-träning används istället).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Om du inte har tillgång till datacenter-GPU:er

LoRA kan vara ditt enda alternativ. Du kan använda följande kommando för att finetuna Phi-3-V på klassificering av hatiska memes.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

För Turing+ GPU stöds QLoRA.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Föreslagna hyperparametrar och förväntad noggrannhet
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

Träningsmetod | Fryst visionsmodell | datatyp | LoRA-rank | LoRA-alfa | batchstorlek | inlärningshastighet | epoker | Noggrannhet
--- | --- | --- | --- | --- | --- | --- | --- | --- |
fullständig finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
fullständig finetuning | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA-resultat kommer snart |  |  |  |  |  |  |  |  |

### OBS
Resultaten för DocVQA och hatiska memes nedan är baserade på den tidigare versionen (Phi-3-vision). De nya resultaten med Phi-3.5-vision kommer att uppdateras snart.

### DocVQA (OBS: Phi-3-vision)

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

Träningsmetod | datatyp | LoRA-rank | LoRA-alfa | batchstorlek | inlärningshastighet | epoker | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
fullständig finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
fullständig finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
fryst bildmodell| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
fryst bildmodell| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hatiska memes (OBS: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Träningsmetod | datatyp | LoRA-rank | LoRA-alfa | batchstorlek | inlärningshastighet | epoker | Noggrannhet
--- | --- | --- | --- | --- | --- | --- | --- |
fullständig finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
fullständig finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
fryst bildmodell| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
fryst bildmodell| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Hastighetsbenchmarking (OBS: Phi-3-vision)

Nya benchmarkresultat med Phi-3.5-vision kommer att uppdateras snart.

Hastighetsbenchmarking utförs på DocVQA-datasetet. Den genomsnittliga sekvenslängden för detta dataset är 2443.23 tokens (med `num_crops=16` för bildmodellen).

### 8x A100-80GB (Ampere)

Träningsmetod | \# noder | GPU:er | flash attention | Effektiv batchstorlek | Genomströmning (img/s) | Hastighetsökning | Max GPU-minne (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
fullständig finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
fullständig finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
fullständig finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
fullständig finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
fryst bildmodell | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
fryst bildmodell | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Träningsmetod | \# noder | GPU:er | flash attention | Effektiv batchstorlek | Genomströmning (img/s) | Hastighetsökning | Max GPU-minne (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
fullständig finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
fullständig finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
fullständig finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
fryst bildmodell | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Kända problem

- Flash attention fungerar inte med fp16 (bf16 rekommenderas alltid när det är tillgängligt, och alla GPU:er som stöder flash attention stöder också bf16).
- Stöd för att spara mellanliggande checkpoints och återuppta träning saknas fortfarande.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-baserade maskinöversättningstjänster. Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell human översättning. Vi tar inget ansvar för missförstånd eller feltolkningar som uppstår vid användning av denna översättning.