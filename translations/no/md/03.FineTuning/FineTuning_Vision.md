# Phi-3.5-vision finetuning-oppskrift

Dette er den offisielle veiledningen for finetuning av Phi-3.5-vision ved bruk av huggingface-biblioteker. Gå til kodekatalogen [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) før du kjører følgende kommandoer.

## Installasjon

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

## Komme raskt i gang

Vi tilbyr to eksempelskript for finetuning, ett for DocVQA og ett for klassifisering av hatefulle memer.

Minimum maskinvare testet: 4x RTX8000 (48GB RAM per GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision støtter nå offisielt multi-bilde-inndata. Her er et eksempel på finetuning av NLVR2:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Bruksveiledning

Avhengig av maskinvaren kan brukere velge forskjellige strategier for finetuning. Vi støtter full finetuning (med Deepspeed Zero-2) med mulighet for å fryse visuelle parametere, og LoRA (inkludert 4bit QLoRA). Generelt anbefaler vi full finetuning med flash attention og bf16 når det er mulig.

### Veiledning for å konvertere ditt egendefinerte datasett til riktig format

Vi bruker et minimalt videoklassifiseringsdatasett (et utdrag av UCF-101) som et eksempel for å demonstrere hvordan du kan konvertere ditt egendefinerte datasett til riktig format og finetune Phi-3.5-vision på det.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

De konverterte dataene vil se slik ut:

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

For `jsonl`-annotasjonen bør hver linje være en ordbok som dette:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Merk at `conversations` er en liste, slik at samtaler med flere vendinger kan støttes hvis slike data er tilgjengelige.

## Be om Azure GPU-kvote 

### Forutsetninger

En Azure-konto med Contributor-rolle (eller en annen rolle som inkluderer Contributor-tilgang).

Hvis du ikke har en Azure-konto, opprett en [gratis konto før du begynner](https://azure.microsoft.com).

### Be om økning av kvote

Du kan sende inn en forespørsel om å øke kvoten direkte fra Mine kvoter. Følg trinnene nedenfor for å be om en økning av en kvote. I dette eksemplet kan du velge en justerbar kvote i abonnementet ditt.

Logg inn på [Azure-portalen](https://portal.azure.com).

Skriv "kvoter" i søkefeltet, og velg deretter Kvoter.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

På oversiktssiden velger du en leverandør, som Compute eller AML.

**Merk** For alle leverandører bortsett fra Compute, vil du se en kolonne kalt Be om økning i stedet for kolonnen Justerbar beskrevet nedenfor. Der kan du be om en økning for en spesifikk kvote, eller opprette en støtteforespørsel for økningen.

På siden Mine kvoter, under Kvotenavn, velger du kvoten du vil øke. Sørg for at kolonnen Justerbar viser Ja for denne kvoten.

Øverst på siden velger du Ny kvoteforespørsel, og deretter Angi en ny grense.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

I panelet Ny kvoteforespørsel skriver du inn en numerisk verdi for din nye kvotegrense, og velger deretter Send.

Forespørselen din vil bli vurdert, og du vil bli varslet om den kan oppfylles. Dette skjer vanligvis i løpet av noen få minutter.

Hvis forespørselen din ikke blir oppfylt, vil du se en lenke for å opprette en støtteforespørsel. Når du bruker denne lenken, vil en støtteingeniør hjelpe deg med forespørselen om økning.

## Forslag til Azure Compute GPU-maskin SKU-er

[ND A100 v4-serien](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-serien](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Her er noen eksempler:

### Hvis du har A100- eller H100-GPUer

Full finetuning gir vanligvis best ytelse. Du kan bruke følgende kommando for å finetune Phi-3-V på klassifisering av hatefulle memer.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Hvis du har Standard_ND40rs_v2 8x V100-32GB GPUer

Det er fortsatt mulig å fullfinetune Phi-3-V på klassifisering av hatefulle memer. Imidlertid må du forvente mye lavere gjennomstrømning sammenlignet med A100- eller H100-GPUer på grunn av mangel på flash attention-støtte. Nøyaktigheten kan også bli påvirket på grunn av mangel på bf16-støtte (fp16 blandet presisjon brukes i stedet).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Hvis du ikke har tilgang til datasenter-GPUer
Lora kan være ditt eneste alternativ. Du kan bruke følgende kommando for å finetune Phi-3-V på klassifisering av hatefulle memer.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

For Turing+ GPUer støttes QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Forslåtte hyperparametere og forventet nøyaktighet
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

Treningsmetode | Frosset visjonsmodell | datatyper | LoRA-rang | LoRA alpha | batch-størrelse | læringsrate | epoker | Nøyaktighet
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA-resultater kommer snart |  |  |  |  |  |  |  |  |

### MERK
Nedenfor er DocVQA- og hatefulle memer-resultater basert på den forrige versjonen (Phi-3-vision).  
De nye resultatene med Phi-3.5-vision vil bli oppdatert snart.

### DocVQA (MERK: Phi-3-vision)

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

Treningsmetode | datatyper | LoRA-rang | LoRA alpha | batch-størrelse | læringsrate | epoker | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
frosset bildemodell | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
frosset bildemodell | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hatefulle memer (MERK: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Treningsmetode | datatyper | LoRA-rang | LoRA alpha | batch-størrelse | læringsrate | epoker | Nøyaktighet
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
frosset bildemodell | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
frosset bildemodell | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Hastighetsbenchmarking (MERK: Phi-3-vision)

Nye benchmarkresultater med Phi-3.5-vision vil bli oppdatert snart.

Hastighetsbenchmarking er utført på DocVQA-datasettet. Den gjennomsnittlige sekvenslengden for dette datasettet er 2443.23 tokens (ved bruk av `num_crops=16` for bildemodellen).

### 8x A100-80GB (Ampere)

Treningsmetode | \# noder | GPUer | flash attention | Effektiv batch-størrelse | Gjennomstrømning (img/s) | Hastighetsøkning | Topp GPU-minne (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
frosset bildemodell | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
frosset bildemodell | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Treningsmetode | \# noder | GPUer | flash attention | Effektiv batch-størrelse | Gjennomstrømning (img/s) | Hastighetsøkning | Topp GPU-minne (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
frosset bildemodell | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Kjente problemer

- Kan ikke kjøre flash attention med fp16 (bf16 anbefales alltid når tilgjengelig, og alle GPUer som støtter flash attention støtter også bf16).  
- Støtter ennå ikke lagring av mellomliggende sjekkpunkter eller gjenopptakelse av trening.  

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.