# Phi-3.5-vision recept za fino podešavanje

Ovo je službena podrška za fino podešavanje Phi-3.5-vision koristeći huggingface biblioteke.  
Molimo `cd` u direktorij koda [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) prije pokretanja sljedećih naredbi.

## Instalacija

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

## Brzi početak

Pružamo dva primjera skripti za fino podešavanje, jednu za DocVQA, a drugu za klasifikaciju mrziteljskih memova.  

Minimalni hardver testiran na 4x RTX8000 (48GB RAM-a po GPU-u)  

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision sada službeno podržava ulaze s više slika. Evo primjera za fino podešavanje NLVR2.  

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Vodič za korištenje

Ovisno o hardveru, korisnici mogu birati između različitih strategija finog podešavanja. Podržavamo  
potpuno fino podešavanje (s Deepspeed Zero-2) uz opcionalno zamrzavanje parametara vizualnog modela, kao i LoRA (uključujući 4bit QLoRA).  
Općenito, preporučujemo korištenje potpunog finog podešavanja s flash attention i bf16 kad god je to moguće.  

### Vodič za konvertiranje prilagođenih skupova podataka u traženi format

Koristimo minimalni dataset za klasifikaciju videa (podskup UCF-101) kao primjer od početka do kraja kako bismo demonstrirali kako konvertirati prilagođeni dataset u traženi format i fino podesiti Phi-3.5-vision na njemu.  

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Konvertirani podaci izgledat će ovako:  

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

Za `jsonl` anotaciju, svaki redak treba biti rječnik poput:  

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Napomena: `conversations` je lista, tako da se može podržati višekratna razmjena ako su takvi podaci dostupni.  

## Zahtjev za Azure GPU kvotom 

### Preduvjeti

Azure račun s ulogom Contributor (ili nekom drugom ulogom koja uključuje pristup Contributoru).  

Ako nemate Azure račun, napravite [besplatan račun prije početka](https://azure.microsoft.com).  

### Podnošenje zahtjeva za povećanje kvote

Možete podnijeti zahtjev za povećanje kvote izravno s My quotas. Slijedite korake u nastavku kako biste zatražili povećanje kvote. U ovom primjeru možete odabrati bilo koju prilagodljivu kvotu u svojoj pretplati.  

Prijavite se u [Azure portal](https://portal.azure.com).  

Unesite "quotas" u okvir za pretraživanje, a zatim odaberite Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)  

Na stranici Pregled (Overview) odaberite pružatelja usluga, poput Compute ili AML.  

**Napomena**: Za sve pružatelje usluga osim Compute, vidjet ćete stupac Request increase umjesto stupca Adjustable opisanog u nastavku. Tamo možete zatražiti povećanje za određenu kvotu ili kreirati zahtjev za podršku za povećanje.  

Na stranici My quotas, ispod naziva kvote (Quota name), odaberite kvotu koju želite povećati. Provjerite prikazuje li stupac Adjustable "Yes" za ovu kvotu.  

Blizu vrha stranice, odaberite New Quota Request, a zatim odaberite Enter a new limit.  

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)  

U oknu New Quota Request unesite numeričku vrijednost za svoju novu granicu kvote, a zatim odaberite Submit.  

Vaš zahtjev će biti pregledan, i bit ćete obaviješteni ako se zahtjev može ispuniti. Ovo obično traje nekoliko minuta.  

Ako vaš zahtjev nije ispunjen, vidjet ćete poveznicu za kreiranje zahtjeva za podršku. Kada koristite ovu poveznicu, inženjer podrške pomoći će vam s vašim zahtjevom za povećanje.  

## Preporuke za Azure Compute GPU strojeve

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)  

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)  

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)  

Evo nekoliko primjera:  

### Ako imate A100 ili H100 GPU-ove  

Potpuno fino podešavanje obično daje najbolje rezultate. Možete koristiti sljedeću naredbu za fino podešavanje Phi-3-V na klasifikaciji mrziteljskih memova.  

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Ako imate Standard_ND40rs_v2 8x V100-32GB GPU-ove  

Još uvijek je moguće potpuno fino podesiti Phi-3-V na klasifikaciji mrziteljskih memova. Međutim, očekujte  
znatno niži throughput u usporedbi s A100 ili H100 GPU-ovima zbog nedostatka podrške za flash attention.  
Točnost također može biti pogođena zbog nedostatka podrške za bf16 (koristi se fp16 mješovita preciznost za treniranje).  

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Ako nemate pristup GPU-ovima u podatkovnim centrima  
LoRA bi mogla biti vaša jedina opcija. Možete koristiti sljedeću naredbu za fino podešavanje Phi-3-V na klasifikaciji mrziteljskih memova.  

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Za Turing+ GPU, QLoRA je podržana.  

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Predloženi hiperparametri i očekivana točnost  

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

Metoda treniranja | Zamrznut vizualni model | Tip podataka | LoRA rank | LoRA alpha | Batch size | Learning rate | Epochs | Točnost  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
potpuno fino podešavanje |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
potpuno fino podešavanje | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
Rezultati za LoRA uskoro dolaze |  |  |  |  |  |  |  |  |  

### NAPOMENA  
Sljedeći rezultati za DocVQA i mrziteljske meme temelje se na prethodnoj verziji (Phi-3-vision).  
Novi rezultati s Phi-3.5-vision bit će uskoro ažurirani.  

### DocVQA (NAPOMENA: Phi-3-vision)

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

Metoda treniranja | Tip podataka | LoRA rank | LoRA alpha | Batch size | Learning rate | Epochs | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
potpuno fino podešavanje | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
potpuno fino podešavanje | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
zamrznut vizualni model | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
zamrznut vizualni model | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  

### Mrziteljski memovi (NAPOMENA: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Metoda treniranja | Tip podataka | LoRA rank | LoRA alpha | Batch size | Learning rate | Epochs | Točnost  
--- | --- | --- | --- | --- | --- | --- | --- |  
potpuno fino podešavanje | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
potpuno fino podešavanje | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
zamrznut vizualni model | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
zamrznut vizualni model | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |  

## Benchmarking brzine (NAPOMENA: Phi-3-vision)

Novi rezultati benchmarkinga s Phi-3.5-vision bit će uskoro ažurirani.  

Benchmarking brzine proveden je na DocVQA datasetu. Prosječna duljina sekvenci ovog dataseta je  
2443.23 tokena (koristeći `num_crops=16` za vizualni model).  

### 8x A100-80GB (Ampere)

Metoda treniranja | \# čvorova | GPU-ovi | flash attention | Efektivni batch size | Protok (img/s) | Ubrzanje | Maks. GPU memorija (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
potpuno fino podešavanje | 1 | 8 |  | 64 | 5.041 | 1x | ~42  
potpuno fino podešavanje | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
potpuno fino podešavanje | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
potpuno fino podešavanje | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
zamrznut vizualni model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
zamrznut vizualni model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Metoda treniranja | \# čvorova | GPU-ovi | flash attention | Efektivni batch size | Protok (img/s) | Ubrzanje | Maks. GPU memorija (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
potpuno fino podešavanje | 1 | 8 | | 64 | 2.462 | 1x | ~32  
potpuno fino podešavanje | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
potpuno fino podešavanje | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
zamrznut vizualni model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Poznati problemi

- Flash attention ne radi s fp16 (bf16 se uvijek preporučuje kad je dostupan, a svi GPU-ovi koji podržavaju flash attention također podržavaju bf16).  
- Još uvijek ne podržavamo spremanje međukoraka i nastavak treniranja.  

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden koristeći usluge strojnog prijevoda temeljenog na umjetnoj inteligenciji. Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.