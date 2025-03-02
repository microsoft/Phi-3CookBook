# Rețetă de finetuning Phi-3.5-vision

Acesta este suportul oficial pentru finetuning-ul Phi-3.5-vision folosind bibliotecile huggingface. 
Vă rugăm să `cd` în directorul de cod [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) înainte de a rula comenzile următoare.

## Instalare

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

## Începere rapidă

Oferim două scripturi de finetuning exemplu, unul pentru DocVQA și unul pentru clasificarea memelor ofensatoare.

Hardware minim testat pe 4x RTX8000 (48GB RAM per GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision suportă acum oficial intrări multiple de imagini. Iată un exemplu pentru finetuning NLVR2:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Ghid de utilizare

În funcție de hardware, utilizatorii pot alege diferite strategii de finetuning. Suportăm finetuning complet (cu Deepspeed Zero-2) cu parametrii de viziune opțional congelați, și LoRA (inclusiv 4bit QLoRA). 
În general, recomandăm utilizarea finetuning-ului complet cu flash attention și bf16 ori de câte ori este posibil.

### Ghid pentru convertirea dataset-ului personalizat în formatul necesar

Folosim un dataset minim de clasificare video (un subset din UCF-101) ca exemplu end-to-end pentru a demonstra cum să convertiți dataset-ul personalizat în formatul necesar și să finetunați Phi-3.5-vision pe acesta.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Datele convertite vor arăta astfel:

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

Pentru adnotarea `jsonl`, fiecare linie ar trebui să fie un dicționar de forma:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Rețineți că `conversations` este o listă, astfel încât se poate susține o conversație cu mai multe schimburi dacă astfel de date sunt disponibile.

## Solicitarea unei cote GPU Azure 

### Cerințe preliminare

Un cont Azure cu rolul de Contributor (sau alt rol care include acces Contributor).

Dacă nu aveți un cont Azure, creați unul [gratuit înainte de a începe](https://azure.microsoft.com).

### Solicitarea unei creșteri a cotei

Puteți trimite o solicitare pentru creșterea cotei direct din My quotas. Urmați pașii de mai jos pentru a solicita o creștere a unei cote. Pentru acest exemplu, puteți selecta orice cotă ajustabilă din abonamentul dvs.

Conectați-vă la [portalul Azure](https://portal.azure.com).

Introduceți "quotas" în caseta de căutare, apoi selectați Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Pe pagina Overview, selectați un furnizor, cum ar fi Compute sau AML.

**Notă** Pentru toți furnizorii, în afară de Compute, veți vedea o coloană Request increase în loc de coloana Adjustable descrisă mai jos. Acolo, puteți solicita o creștere pentru o cotă specifică sau puteți crea o solicitare de suport pentru creștere.

Pe pagina My quotas, sub Quota name, selectați cota pe care doriți să o creșteți. Asigurați-vă că coloana Adjustable arată Yes pentru această cotă.

În partea de sus a paginii, selectați New Quota Request, apoi selectați Enter a new limit.  
![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

În panoul New Quota Request, introduceți o valoare numerică pentru noua limită a cotei dvs., apoi selectați Submit.

Solicitarea dvs. va fi analizată, iar dacă poate fi aprobată, veți fi notificat. De obicei, acest lucru se întâmplă în câteva minute.

Dacă solicitarea dvs. nu este aprobată, veți vedea un link pentru a crea o solicitare de suport. Când utilizați acest link, un inginer de suport vă va ajuta cu cererea dvs. de creștere.

## Sugestii pentru SKU-uri de mașini GPU Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Iată câteva exemple:

### Dacă aveți GPU-uri A100 sau H100

Finetuning-ul complet oferă de obicei cea mai bună performanță. Puteți folosi următoarea comandă pentru a finetuna Phi-3-V pe clasificarea memelor ofensatoare.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Dacă aveți Standard_ND40rs_v2 8x V100-32GB GPUs

Este încă posibil să finetunați complet Phi-3-V pe clasificarea memelor ofensatoare. Totuși, așteptați-vă la un throughput mult mai scăzut comparativ cu GPU-urile A100 sau H100 din cauza lipsei suportului pentru flash attention. 
Acuratețea ar putea fi, de asemenea, afectată din cauza lipsei suportului bf16 (se folosește în schimb antrenarea cu precizie mixtă fp16).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Dacă nu aveți acces la GPU-uri din centre de date
Lora ar putea fi singura dvs. opțiune. Puteți folosi următoarea comandă pentru a finetuna Phi-3-V pe clasificarea memelor ofensatoare.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Pentru GPU-urile Turing+, QLoRA este suportat.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Parametri hiper sugerați și acuratețe așteptată
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

Metoda de antrenare | Model vizual congelat | Tip de date | Rang LoRA | Alpha LoRA | Batch size | Rata de învățare | Epoci | Acuratețe
--- | --- | --- | --- | --- | --- | --- | --- | --- |
finetuning complet |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
finetuning complet | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
Rezultate LoRA în curând |  |  |  |  |  |  |  |  |

### NOTĂ
Rezultatele de mai jos pentru DocVQA și Hateful memes sunt bazate pe versiunea anterioară (Phi-3-vision). 
Noile rezultate cu Phi-3.5-vision vor fi actualizate în curând.

### DocVQA (NOTĂ: Phi-3-vision)

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

Metoda de antrenare | Tip de date | Rang LoRA | Alpha LoRA | Batch size | Rata de învățare | Epoci | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
finetuning complet | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
finetuning complet | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
model vizual congelat| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
model vizual congelat| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (NOTĂ: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Metoda de antrenare | Tip de date | Rang LoRA | Alpha LoRA | Batch size | Rata de învățare | Epoci | Acuratețe
--- | --- | --- | --- | --- | --- | --- | --- |
finetuning complet | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
finetuning complet | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
model vizual congelat| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
model vizual congelat| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Benchmarking de viteză (NOTĂ: Phi-3-vision)

Noile rezultate de benchmarking cu Phi-3.5-vision vor fi actualizate în curând.

Benchmarking-ul de viteză este realizat pe dataset-ul DocVQA. Lungimea medie a secvenței acestui dataset este de 2443.23 token-uri (folosind `num_crops=16` pentru modelul de imagine).

### 8x A100-80GB (Ampere)

Metoda de antrenare | \# noduri | GPU-uri | flash attention | Batch size efectiv | Throughput (img/s) | Accelerare | Memorie GPU maximă (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
finetuning complet | 1 | 8 |  | 64 | 5.041 |  1x | ~42
finetuning complet | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
finetuning complet | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
finetuning complet | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
model vizual congelat | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
model vizual congelat | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Metoda de antrenare | \# noduri | GPU-uri | flash attention | Batch size efectiv | Throughput (img/s) | Accelerare | Memorie GPU maximă (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
finetuning complet | 1 | 8 | | 64 | 2.462 |  1x | ~32
finetuning complet | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
finetuning complet | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
model vizual congelat | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Probleme cunoscute

- Nu se poate rula flash attention cu fp16 (bf16 este întotdeauna recomandat când este disponibil, iar toate GPU-urile care suportă flash attention suportă și bf16).
- Nu suportă salvarea checkpoint-urilor intermediare și reluarea antrenamentului încă.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind servicii de traducere bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea umană realizată de profesioniști. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.