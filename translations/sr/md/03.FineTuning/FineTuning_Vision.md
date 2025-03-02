# Phi-3.5-vision recept za fino podešavanje

Ovo je zvanična podrška za fino podešavanje Phi-3.5-vision koristeći huggingface biblioteke.  
Molimo vas da `cd` uđete u direktorijum koda [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) pre pokretanja sledećih komandi.

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

Pružamo dva primera skripti za fino podešavanje, jedan za DocVQA, a drugi za klasifikaciju mrziteljskih mimova.

Minimalni hardver testiran na 4x RTX8000 (48GB RAM-a po GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision sada zvanično podržava unos više slika. Evo primera za fino podešavanje NLVR2.

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Uputstvo za korišćenje

U zavisnosti od hardvera, korisnici mogu birati različite strategije za fino podešavanje. Podržavamo  
potpuno fino podešavanje (sa Deepspeed Zero-2) uz opcionalno zamrzavanje parametara za viziju, kao i LoRA (uključujući 4bit QLoRA).  
Generalno, preporučujemo korišćenje potpunog finog podešavanja sa flash pažnjom i bf16 kad god je to moguće.

### Vodič za konvertovanje prilagođenog skupa podataka u potrebni format

Koristimo minimalni dataset za video klasifikaciju (podskup UCF-101) kao primer od početka do kraja kako bismo demonstrirali kako da konvertujete vaš prilagođeni skup podataka u potrebni format i fino podesite Phi-3.5-vision na njemu.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Konvertovani podaci će izgledati ovako:

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

Za anotaciju u formatu `jsonl`, svaka linija treba da bude rečnik poput:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Napomena: `conversations` je lista, tako da je podržan višestruki tok razgovora ako su takvi podaci dostupni.

## Zahtevanje Azure GPU kvote 

### Preduslovi

Azure nalog sa Contributor ulogom (ili drugom ulogom koja uključuje pristup Contributor-u).  

Ako nemate Azure nalog, kreirajte [besplatan nalog pre nego što počnete](https://azure.microsoft.com).

### Zahtev za povećanje kvote

Možete podneti zahtev za povećanje kvote direktno iz Mojih kvota. Pratite korake ispod da biste zatražili povećanje kvote. U ovom primeru, možete odabrati bilo koju prilagodljivu kvotu u vašoj pretplati.

Prijavite se na [Azure portal](https://portal.azure.com).

Unesite "quotas" u polje za pretragu, a zatim odaberite Quotas.  
![Kvota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Na stranici Pregled, odaberite provajdera, kao što su Compute ili AML.  

**Napomena** Za sve provajdere osim Compute, videćete kolonu Zahtjev za povećanje umesto kolone Prilagodljivo opisane ispod. Tamo možete zatražiti povećanje za određenu kvotu ili kreirati zahtev za podršku za povećanje.  

Na stranici Moje kvote, ispod imena kvote, odaberite kvotu koju želite da povećate. Uverite se da kolona Prilagodljivo pokazuje Da za ovu kvotu.  

Blizu vrha stranice, odaberite Novi zahtev za kvotu, a zatim odaberite Unesite novu granicu.

![Povećanje kvote](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

U panelu Novi zahtev za kvotu, unesite numeričku vrednost za novu granicu kvote, a zatim odaberite Submit.  

Vaš zahtev će biti pregledan i bićete obavešteni da li zahtev može biti ispunjen. To se obično dešava u roku od nekoliko minuta.  

Ako vaš zahtev nije ispunjen, videćete link za kreiranje zahteva za podršku. Kada koristite ovaj link, inženjer podrške će vam pomoći sa vašim zahtevom za povećanje.

## Predlozi za Azure Compute GPU SKU mašine

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Evo nekoliko primera:

### Ako imate A100 ili H100 GPU-ove

Potpuno fino podešavanje obično daje najbolje performanse. Možete koristiti sledeću komandu za fino podešavanje Phi-3-V na klasifikaciji mrziteljskih mimova.

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

Još uvek je moguće potpuno fino podesiti Phi-3-V na klasifikaciji mrziteljskih mimova. Međutim, očekujte znatno manji protok u poređenju sa A100 ili H100 GPU-ovima zbog nedostatka podrške za flash pažnju.  
Preciznost takođe može biti pogođena zbog nedostatka podrške za bf16 (koristi se fp16 obuka sa mešovitom preciznošću).  

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Ako nemate pristup GPU-ovima iz data centra  
Lora može biti vaš jedini izbor. Možete koristiti sledeću komandu za fino podešavanje Phi-3-V na klasifikaciji mrziteljskih mimova.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Za Turing+ GPU, QLoRA je podržan.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Predloženi hiperparametri i očekivana preciznost  
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

Metod obuke | Zamrznut model vizije | Tip podataka | LoRA rank | LoRA alfa | Veličina batch-a | Learning rate | Epochs | Preciznost  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
potpuno fino podešavanje |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
potpuno fino podešavanje | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
Rezultati za LoRA uskoro dolaze |  |  |  |  |  |  |  |  |  

### Napomena  
Rezultati za DocVQA i Hateful memes ispod bazirani su na prethodnoj verziji (Phi-3-vision).  
Novi rezultati sa Phi-3.5-vision biće uskoro ažurirani.

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

Metod obuke | Tip podataka | LoRA rank | LoRA alfa | Veličina batch-a | Learning rate | Epochs | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
potpuno fino podešavanje | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
potpuno fino podešavanje | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
zamrznut model slike | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
zamrznut model slike | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  

### Hateful memes (NAPOMENA: Phi-3-vision)  

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Metod obuke | Tip podataka | LoRA rank | LoRA alfa | Veličina batch-a | Learning rate | Epochs | Preciznost  
--- | --- | --- | --- | --- | --- | --- | --- |  
potpuno fino podešavanje | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
potpuno fino podešavanje | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
zamrznut model slike | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
zamrznut model slike | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |  

## Benchmarking brzine (NAPOMENA: Phi-3-vision)  

Novi rezultati benchmarking-a sa Phi-3.5-vision biće uskoro ažurirani.  

Benchmarking brzine izveden je na DocVQA datasetu. Prosečna dužina sekvence ovog dataseta  
je 2443.23 tokena (koristeći `num_crops=16` za model slike).

### 8x A100-80GB (Ampere)  

Metod obuke | \# čvorova | GPU-ovi | flash pažnja | Efektivna veličina batch-a | Protok (slika/s) | Ubrzanje | Maksimalna GPU memorija (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
potpuno fino podešavanje | 1 | 8 |  | 64 | 5.041 | 1x | ~42  
potpuno fino podešavanje | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
potpuno fino podešavanje | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
potpuno fino podešavanje | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
zamrznut model slike | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
zamrznut model slike | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)  

Metod obuke | \# čvorova | GPU-ovi | flash pažnja | Efektivna veličina batch-a | Protok (slika/s) | Ubrzanje | Maksimalna GPU memorija (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
potpuno fino podešavanje | 1 | 8 |  | 64 | 2.462 | 1x | ~32  
potpuno fino podešavanje | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
potpuno fino podešavanje | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
zamrznut model slike | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Poznati problemi  

- Flash pažnja ne može raditi sa fp16 (bf16 se uvek preporučuje kada je dostupan, a svi GPU-ovi koji podržavaju flash pažnju takođe podržavaju bf16).  
- Još uvek nije podržano čuvanje međufaznih checkpoint-ova i nastavljanje obuke.  

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења на бази вештачке интелигенције. Иако настојимо да обезбедимо тачност, имајте у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква неспоразумевања или погрешна тумачења која могу проистећи из коришћења овог превода.