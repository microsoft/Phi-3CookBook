# Phi-3.5-vision -hienosäädön ohjeet

Tämä on virallinen tuki Phi-3.5-visionin hienosäädölle käyttäen huggingface-kirjastoja. 
Siirry koodihakemistoon [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) ennen seuraavien komentojen suorittamista.

## Asennus

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

## Nopea aloitus

Tarjoamme kaksi esimerkkiskriptiä hienosäädölle: toinen DocVQA:lle ja toinen vihamielisten meemien luokittelulle.

Vähimmäislaitteistovaatimukset: 4x RTX8000 (48GB RAM per GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision tukee nyt virallisesti monikuvasyötteitä. Tässä esimerkki NLVR2:n hienosäädöstä:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Käyttöopas

Riippuen laitteistosta käyttäjät voivat valita erilaisia hienosäätöstrategioita. Tuemme
täyshienosäätöä (Deepspeed Zero-2) valinnaisesti jäädytetyillä visio-parametreilla, sekä LoRA:a (mukaan lukien 4bit QLoRA).
Yleisesti suosittelemme täyshienosäätöä flash attentionilla ja bf16:lla aina kun mahdollista.

### Opas mukautetun datasetin muuntamiseksi vaadittuun formaattiin

Käytämme pientä videoluokitteludatasettiä (UCF-101:n alijoukko) esimerkkinä, joka näyttää, kuinka mukautettu datasetti muunnetaan vaadittuun formaattiin ja Phi-3.5-vision hienosäädetään sen avulla.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Muunnettu data näyttää tältä:

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

`jsonl`-annotaatiossa jokainen rivi on sanakirja, kuten:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Huomaa, että `conversations` on lista, joten monivaiheiset keskustelut voidaan tukea, jos tällaisia tietoja on saatavilla.

## Azure GPU -kiintiön pyytäminen 

### Esivaatimukset

Azure-tili, jolla on Contributor-rooli (tai muu rooli, joka sisältää Contributor-pääsyn).

Jos sinulla ei ole Azure-tiliä, luo [ilmainen tili ennen aloittamista](https://azure.microsoft.com).

### Kiintiön lisäyksen pyytäminen

Voit pyytää kiintiön lisäystä suoraan My quotas -sivulta. Seuraa alla olevia ohjeita pyytääksesi lisäystä kiintiöön. Tässä esimerkissä voit valita minkä tahansa säädettävän kiintiön tilauksestasi.

Kirjaudu sisään [Azure-portaaliin](https://portal.azure.com).

Kirjoita hakukenttään "quotas" ja valitse Quotas.
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Yleiskatsaus-sivulla valitse palveluntarjoaja, kuten Compute tai AML.

**Huom** Kaikille muille palveluntarjoajille kuin Computelle näet Request increase -sarakkeen Adjustable-sarakkeen sijaan. Siellä voit pyytää lisäystä tiettyyn kiintiöön tai luoda tukipyynnön lisäystä varten.

My quotas -sivulla, kohdassa Quota name, valitse kiintiö, jota haluat lisätä. Varmista, että Adjustable-sarakkeessa lukee Yes kyseiselle kiintiölle.

Sivun yläosassa valitse New Quota Request ja sitten Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request -paneelissa syötä numeerinen arvo uudelle kiintiörajalle ja valitse Submit.

Pyyntösi tarkistetaan, ja sinulle ilmoitetaan, voidaanko pyyntö täyttää. Tämä tapahtuu yleensä muutamassa minuutissa.

Jos pyyntöäsi ei täytetä, näet linkin luoda tukipyynnön. Kun käytät tätä linkkiä, tukihenkilö auttaa sinua lisäyspyynnössäsi.

## Azure Compute GPU -konetyyppisuositukset

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Tässä muutamia esimerkkejä:

### Jos sinulla on A100- tai H100-GPU:ita

Täyshienosäätö antaa yleensä parhaan suorituskyvyn. Voit käyttää seuraavaa komentoa hienosäätääksesi Phi-3-V:n vihamielisten meemien luokitteluun.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Jos sinulla on Standard_ND40rs_v2 8x V100-32GB GPU:ita

On edelleen mahdollista tehdä täyshienosäätö Phi-3-V:lle vihamielisten meemien luokitteluun. Kuitenkin odota huomattavasti alhaisempaa läpimenoaikaa verrattuna A100- tai H100-GPU:ihin, koska flash attention -tuki puuttuu.
Tarkkuus voi myös kärsiä bf16-tuen puutteen vuoksi (fp16-sekakäytännön koulutusta käytetään sen sijaan).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Jos sinulla ei ole pääsyä datakeskus-GPU:ihin
LoRA voi olla ainoa vaihtoehtosi. Voit käyttää seuraavaa komentoa hienosäätääksesi Phi-3-V:n vihamielisten meemien luokitteluun.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+-GPU:ille QLoRA on tuettu

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Suositellut hyperparametrit ja odotettu tarkkuus
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

Koulutusmenetelmä | Jäädytetty visiomalli | datatyyppi | LoRA rank | LoRA alpha | eräkoko | oppimisnopeus | epochit | Tarkkuus
--- | --- | --- | --- | --- | --- | --- | --- | --- |
täyshienosäätö |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
täyshienosäätö | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA-tulokset tulossa pian |  |  |  |  |  |  |  |  |

### HUOM
Alla olevat DocVQA- ja vihamielisten meemien tulokset perustuvat aiempaan versioon (Phi-3-vision).
Uudet tulokset Phi-3.5-visionilla päivitetään pian.

### DocVQA (HUOM: Phi-3-vision)

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

Koulutusmenetelmä | datatyyppi | LoRA rank | LoRA alpha | eräkoko | oppimisnopeus | epochit | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
täyshienosäätö | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
täyshienosäätö | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
jäädytetty kuvamalli| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
jäädytetty kuvamalli| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Vihamieliset meemit (HUOM: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Koulutusmenetelmä | datatyyppi | LoRA rank | LoRA alpha | eräkoko | oppimisnopeus | epochit | Tarkkuus
--- | --- | --- | --- | --- | --- | --- | --- |
täyshienosäätö | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
täyshienosäätö | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
jäädytetty kuvamalli| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
jäädytetty kuvamalli| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Nopeusvertailu (HUOM: Phi-3-vision)

Uudet vertailutulokset Phi-3.5-visionilla päivitetään pian.

Nopeusvertailu on tehty DocVQA-datasetillä. Datasetin keskimääräinen sekvenssipituus on 2443.23 tokenia (käyttäen `num_crops=16` kuvamallille).

### 8x A100-80GB (Ampere)

Koulutusmenetelmä | \# solmut | GPU:t | flash attention | Efektiivinen eräkoko | Läpimeno (kuvaa/s) | Nopeutus | Huippu GPU-muisti (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
täyshienosäätö | 1 | 8 |  | 64 | 5.041 |  1x | ~42
täyshienosäätö | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
täyshienosäätö | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
täyshienosäätö | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
jäädytetty kuvamalli | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
jäädytetty kuvamalli | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Koulutusmenetelmä | \# solmut | GPU:t | flash attention | Efektiivinen eräkoko | Läpimeno (kuvaa/s) | Nopeutus | Huippu GPU-muisti (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
täyshienosäätö | 1 | 8 | | 64 | 2.462 |  1x | ~32
täyshienosäätö | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
täyshienosäätö | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
jäädytetty kuvamalli | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Tunnetut ongelmat

- Flash attention ei toimi fp16:n kanssa (bf16 on aina suositeltava, kun se on saatavilla, ja kaikki flash attentionia tukevat GPU:t tukevat myös bf16:ta).
- Välitallennuspisteiden tallentaminen ja koulutuksen jatkaminen ei ole vielä tuettua.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisten tekoälykäännöspalveluiden avulla. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.