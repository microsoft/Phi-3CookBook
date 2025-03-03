# Phi-3.5-vision finomhangolási recept

Ez a Phi-3.5-vision hivatalos támogatása huggingface könyvtárak használatával történő finomhangoláshoz.
Kérjük, `cd` a kód könyvtárba [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning), mielőtt futtatná az alábbi parancsokat.

## Telepítés

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

## Gyors kezdés

Két példa finomhangolási szkriptet biztosítunk: az egyik a DocVQA-hoz, a másik a gyűlöletkeltő mémek osztályozásához.

Minimális hardver: 4x RTX8000 (48GB RAM GPU-nként)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

A Phi-3.5-vision most hivatalosan támogatja a több képből álló bemeneteket. Íme egy példa az NLVR2 finomhangolására:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Használati útmutató

A hardvertől függően a felhasználók különböző finomhangolási stratégiákat választhatnak. Támogatjuk a teljes finomhangolást (Deepspeed Zero-2-vel), opcionálisan rögzített látási paraméterekkel, valamint a LoRA-t (beleértve a 4 bites QLoRA-t is). Általánosságban javasoljuk a teljes finomhangolást flash attention-nel és bf16-tal, amikor csak lehetséges.

### Útmutató az egyéni adatállomány formátumra alakításához

Egy minimális videóosztályozási adatállományt használunk (az UCF-101 egy részhalmazát), hogy bemutassuk, hogyan alakíthatja át az egyéni adatállományát a szükséges formátumra, és hogyan finomhangolhatja rajta a Phi-3.5-vision-t.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Az átalakított adatok így fognak kinézni:

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

A `jsonl` annotáció esetében minden sor egy szótár legyen, például:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Figyelem: a `conversations` lista, így többszörös körös beszélgetéseket is támogathat, ha ilyen adatok rendelkezésre állnak.

## Azure GPU kvóta igénylése 

### Előfeltételek

Egy Azure-fiók, amely rendelkezik Hozzájáruló szerepkörrel (vagy más, Hozzájáruló hozzáférést biztosító szerepkörrel).

Ha még nincs Azure-fiókja, hozzon létre egy [ingyenes fiókot a kezdés előtt](https://azure.microsoft.com).

### Kvóta növelésének igénylése

Közvetlenül a Saját kvóták oldalról nyújthat be kérelmet a kvóta növelésére. Kövesse az alábbi lépéseket egy kvóta növelésének igényléséhez. Ebben a példában bármelyik állítható kvótát kiválaszthatja az előfizetésében.

Jelentkezzen be az [Azure portálra](https://portal.azure.com).

Írja be a keresőmezőbe a "kvóták" szót, majd válassza a Kvóták lehetőséget.
![Kvóta](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Az Áttekintés oldalon válasszon ki egy szolgáltatót, például a Compute-t vagy az AML-t.

**Megjegyzés**: A Compute kivételével minden más szolgáltatónál a Kérés növelése oszlopot fogja látni az Állítható oszlop helyett, amelyet alább leírtunk. Itt kérelmezhet egy konkrét kvóta növelését, vagy létrehozhat egy támogatási kérelmet a növeléshez.

A Saját kvóták oldalon, a Kvóta neve alatt válassza ki a növelni kívánt kvótát. Győződjön meg arról, hogy az Állítható oszlopban Igen szerepel ennél a kvótánál.

Az oldal tetején válassza az Új kvóta kérelem lehetőséget, majd válassza az Új limit megadása lehetőséget.

![Kvóta növelése](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Az Új kvóta kérelem panelen adjon meg egy numerikus értéket az új kvótahatárhoz, majd kattintson a Küldés gombra.

Kérelmét felülvizsgálják, és értesítést kap arról, hogy a kérelmet teljesíteni lehet-e. Ez általában néhány percen belül megtörténik.

Ha kérelmét nem teljesítik, egy linket fog látni, amelyen keresztül támogatási kérelmet hozhat létre. Ha ezt a linket használja, egy támogatási mérnök segít Önnek a növelési kérelemben.

## Azure Compute GPU gép SKU javaslatok

[ND A100 v4-sorozat](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-sorozat](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Íme néhány példa:

### Ha A100 vagy H100 GPU-k állnak rendelkezésre

A teljes finomhangolás általában a legjobb teljesítményt nyújtja. Az alábbi parancsot használhatja a Phi-3-V finomhangolására gyűlöletkeltő mémek osztályozásához.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Ha Standard_ND40rs_v2 8x V100-32GB GPU-k állnak rendelkezésre

Még mindig lehetséges teljes finomhangolást végezni a Phi-3-V-n gyűlöletkeltő mémek osztályozására. Azonban számítson sokkal alacsonyabb átviteli sebességre az A100 vagy H100 GPU-khoz képest, mivel a flash attention támogatása hiányzik. A pontosságot is befolyásolhatja a bf16 támogatás hiánya (helyette fp16 vegyes precíziós tréninget használnak).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Ha nincs hozzáférése adatközponti GPU-khoz
A LoRA lehet az egyetlen választása. Az alábbi parancsot használhatja a Phi-3-V finomhangolására gyűlöletkeltő mémek osztályozására.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU esetén a QLoRA támogatott.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Javasolt hiperparaméterek és várható pontosság
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

Tréning módszer | Rögzített látási modell | adat típus | LoRA rang | LoRA alpha | batch méret | tanulási ráta | epochok száma | Pontosság
--- | --- | --- | --- | --- | --- | --- | --- | --- |
teljes finomhangolás |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
teljes finomhangolás | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA eredmények hamarosan |  |  |  |  |  |  |  |  |

### MEGJEGYZÉS
Az alábbi DocVQA és gyűlöletkeltő mémek eredményei a korábbi verzión (Phi-3-vision) alapulnak.
Az új eredményeket a Phi-3.5-vision-nel hamarosan frissítjük.

### DocVQA (MEGJEGYZÉS: Phi-3-vision)

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

Tréning módszer | adat típus | LoRA rang | LoRA alpha | batch méret | tanulási ráta | epochok száma | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
teljes finomhangolás | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
teljes finomhangolás | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
rögzített kép modell | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
rögzített kép modell | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Gyűlöletkeltő mémek (MEGJEGYZÉS: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Tréning módszer | adat típus | LoRA rang | LoRA alpha | batch méret | tanulási ráta | epochok száma | Pontosság
--- | --- | --- | --- | --- | --- | --- | --- |
teljes finomhangolás | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
teljes finomhangolás | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
rögzített kép modell | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
rögzített kép modell | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Sebesség benchmark (MEGJEGYZÉS: Phi-3-vision)

Az új benchmark eredményeket a Phi-3.5-vision-nel hamarosan frissítjük.

A sebesség benchmarkot a DocVQA adatállományon végeztük. Az adatállomány átlagos szekvencia hossza
2443.23 token (a `num_crops=16` beállítással a kép modellnél).

### 8x A100-80GB (Ampere)

Tréning módszer | \# csomópontok | GPU-k | flash attention | Effektív batch méret | Átviteli sebesség (kép/s) | Gyorsulás | Csúcsmemória (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
teljes finomhangolás | 1 | 8 |  | 64 | 5.041 |  1x | ~42
teljes finomhangolás | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
teljes finomhangolás | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
teljes finomhangolás | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
rögzített kép modell | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
rögzített kép modell | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Tréning módszer | \# csomópontok | GPU-k | flash attention | Effektív batch méret | Átviteli sebesség (kép/s) | Gyorsulás | Csúcsmemória (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
teljes finomhangolás | 1 | 8 | | 64 | 2.462 |  1x | ~32
teljes finomhangolás | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
teljes finomhangolás | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
rögzített kép modell | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Ismert problémák

- A flash attention nem futtatható fp16-tal (bf16 mindig ajánlott, ha elérhető, és minden flash attention-t támogató GPU bf16-ot is támogat).
- Még nem támogatjuk köztes ellenőrzőpontok mentését és a tréning folytatását.

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítószolgáltatások használatával készült fordítás. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.