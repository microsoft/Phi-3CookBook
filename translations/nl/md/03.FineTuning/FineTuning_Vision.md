# Phi-3.5-vision finetuning recept

Dit is de officiële ondersteuning voor Phi-3.5-vision finetuning met behulp van de Huggingface-bibliotheken. 
Ga naar de code-directory [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) voordat je de volgende commando's uitvoert.

## Installatie

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

## Snel starten

We bieden twee voorbeeldscripts voor finetuning, één voor DocVQA en één voor classificatie van haatdragende memes.

Minimale hardware getest op 4x RTX8000 (48GB RAM per GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ondersteunt nu officieel invoer van meerdere afbeeldingen. Hier is een voorbeeld voor finetuning van NLVR2:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Gebruikersgids

Afhankelijk van de hardware kunnen gebruikers verschillende finetuning-strategieën kiezen. We ondersteunen 
volledige finetuning (met Deepspeed Zero-2) met optioneel bevroren visionparameters, en LoRA (inclusief 4bit QLoRA). 
In het algemeen raden we aan om volledige finetuning te gebruiken met flash attention en bf16 waar mogelijk.

### Gids voor het converteren van je aangepaste dataset naar het vereiste formaat

We gebruiken een minimale videoclassificatiedataset (een subset van UCF-101) als een end-to-end voorbeeld om te laten zien hoe je jouw aangepaste dataset kunt converteren naar het vereiste formaat en Phi-3.5-vision erop kunt finetunen.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

De geconverteerde gegevens zien er als volgt uit:

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

Voor de `jsonl`-annotatie moet elke regel een woordenboek zijn zoals:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Let op dat `conversations` een lijst is, waardoor meerstapsconversaties kunnen worden ondersteund als dergelijke gegevens beschikbaar zijn.

## Azure GPU-quotum aanvragen 

### Vereisten

Een Azure-account met de rol Contributor (of een andere rol met Contributor-toegang).

Als je nog geen Azure-account hebt, maak dan een [gratis account aan voordat je begint](https://azure.microsoft.com).

### Een quotumverhoging aanvragen

Je kunt een verzoek voor een quotumverhoging rechtstreeks indienen via Mijn quotas. Volg de onderstaande stappen om een verhoging aan te vragen voor een quotum. Voor dit voorbeeld kun je elk aanpasbaar quotum in je abonnement selecteren.

Log in op het [Azure-portaal](https://portal.azure.com).

Voer "quotas" in het zoekvak in en selecteer vervolgens Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Op de overzichtspagina selecteer je een provider, zoals Compute of AML.

**Opmerking** Voor alle providers behalve Compute zie je een kolom Verzoek om verhoging in plaats van de kolom Aanpasbaar zoals hieronder beschreven. Daar kun je een verhoging aanvragen voor een specifiek quotum of een ondersteuningsverzoek indienen voor de verhoging.

Op de pagina Mijn quotas selecteer je onder Quota-naam het quotum dat je wilt verhogen. Zorg ervoor dat de kolom Aanpasbaar Ja toont voor dit quotum.

Bovenaan de pagina selecteer je Nieuw quotumverzoek en vervolgens Voer een nieuwe limiet in.

![Quotum verhogen](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

In het paneel Nieuw quotumverzoek voer je een numerieke waarde in voor je nieuwe quotumlimiet en selecteer je vervolgens Verzenden.

Je verzoek wordt beoordeeld en je ontvangt een melding of het verzoek kan worden ingewilligd. Dit gebeurt meestal binnen een paar minuten.

Als je verzoek niet wordt ingewilligd, zie je een link om een ondersteuningsverzoek in te dienen. Via deze link zal een ondersteuningsmedewerker je helpen met je verzoek tot verhoging.

## Azure Compute GPU-machine SKU-voorstellen

[ND A100 v4-serie](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-serie](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Hier zijn enkele voorbeelden:

### Als je A100- of H100-GPU's hebt

Volledige finetuning geeft meestal de beste prestaties. Je kunt het volgende commando gebruiken om Phi-3-V te finetunen op classificatie van haatdragende memes.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Als je Standard_ND40rs_v2 8x V100-32GB GPU's hebt

Het is nog steeds mogelijk om Phi-3-V volledig te finetunen op classificatie van haatdragende memes. Verwacht echter een veel lagere doorvoer in vergelijking met A100- of H100-GPU's vanwege het ontbreken van flash attention-ondersteuning. De nauwkeurigheid kan ook worden beïnvloed door het ontbreken van bf16-ondersteuning (fp16 mixed-precision training wordt in plaats daarvan gebruikt).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Als je geen toegang hebt tot datacenter-GPU's
Lora kan je enige optie zijn. Je kunt het volgende commando gebruiken om Phi-3-V te finetunen op classificatie van haatdragende memes.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Voor Turing+ GPU wordt QLoRA ondersteund.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Voorgestelde hyperparameters en verwachte nauwkeurigheid
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

Trainingsmethode | Bevroren visionmodel | datatype | LoRA-rank | LoRA-alpha | batchgrootte | leersnelheid | epochs | Nauwkeurigheid
--- | --- | --- | --- | --- | --- | --- | --- | --- |
volledige finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
volledige finetuning | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA-resultaten volgen binnenkort |  |  |  |  |  |  |  |  |

### OPMERKING
De onderstaande DocVQA- en haatdragende memes-resultaten zijn gebaseerd op de vorige versie (Phi-3-vision). 
De nieuwe resultaten met Phi-3.5-vision worden binnenkort bijgewerkt.

### DocVQA (OPMERKING: Phi-3-vision)

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

Trainingsmethode | datatype | LoRA-rank | LoRA-alpha | batchgrootte | leersnelheid | epochs | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
volledige finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
volledige finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
bevroren imagemodel | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
bevroren imagemodel | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Haatdragende memes (OPMERKING: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Trainingsmethode | datatype | LoRA-rank | LoRA-alpha | batchgrootte | leersnelheid | epochs | Nauwkeurigheid
--- | --- | --- | --- | --- | --- | --- | --- |
volledige finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
volledige finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
bevroren imagemodel | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
bevroren imagemodel | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Snelheidsbenchmarking (OPMERKING: Phi-3-vision)

Nieuwe benchmarkingresultaten met Phi-3.5-vision worden binnenkort bijgewerkt.

Snelheidsbenchmarking wordt uitgevoerd op de DocVQA-dataset. De gemiddelde sequentielengte van deze dataset is 2443.23 tokens (met `num_crops=16` voor het imagemodel).

### 8x A100-80GB (Ampere)

Trainingsmethode | \# nodes | GPU's | flash attention | Effectieve batchgrootte | Doorvoer (img/s) | Snelheidswinst | Piekgpu-geheugen (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
volledige finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
volledige finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
volledige finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
volledige finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
bevroren imagemodel | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
bevroren imagemodel | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Trainingsmethode | \# nodes | GPU's | flash attention | Effectieve batchgrootte | Doorvoer (img/s) | Snelheidswinst | Piekgpu-geheugen (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
volledige finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
volledige finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
volledige finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
bevroren imagemodel | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Bekende problemen

- Flash attention kan niet worden uitgevoerd met fp16 (bf16 wordt altijd aanbevolen waar beschikbaar, en alle GPU's die flash attention ondersteunen, ondersteunen ook bf16).  
- Ondersteunt nog geen opslag van tussentijdse checkpoints en hervatten van training.

**Disclaimer**:  
Dit document is vertaald met behulp van machine-gebaseerde AI-vertalingsdiensten. Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.