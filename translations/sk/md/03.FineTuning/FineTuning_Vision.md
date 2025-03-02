# Recept na doladenie Phi-3.5-vision

Toto je oficiálna podpora pre doladenie Phi-3.5-vision pomocou knižníc huggingface.  
Pred spustením nasledujúcich príkazov sa prosím `cd` do adresára s kódom [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning).

## Inštalácia

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

## Rýchly štart

Poskytujeme dva príkladové skripty na doladenie, jeden pre DocVQA a druhý pre klasifikáciu nenávistných mémov.

Minimálna testovaná hardvérová konfigurácia: 4x RTX8000 (48GB RAM na GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision teraz oficiálne podporuje vstupy s viacerými obrázkami. Tu je príklad doladenia pre NLVR2:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Príručka na použitie

V závislosti od hardvéru si používatelia môžu vybrať rôzne stratégie doladenia. Podporujeme úplné doladenie (s Deepspeed Zero-2) s voliteľne zmrazenými parametrami vizuálneho modelu, ako aj LoRA (vrátane 4bit QLoRA).  
Vo všeobecnosti odporúčame používať úplné doladenie s flash attention a bf16, ak je to možné.

### Návod na konverziu vlastného datasetu do požadovaného formátu

Ako príklad používame minimálny dataset pre klasifikáciu videí (podmnožina UCF-101), aby sme ukázali, ako previesť vlastný dataset do požadovaného formátu a doladiť na ňom Phi-3.5-vision.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Prevedené dáta budú vyzerať takto:

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

Pre anotáciu vo formáte `jsonl` by mal každý riadok obsahovať slovník, napríklad:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Poznámka: `conversations` je zoznam, takže je možné podporovať viacotáčkové konverzácie, ak sú takéto dáta k dispozícii.

## Žiadosť o kvótu GPU na Azure

### Predpoklady

Azure účet s rolou Contributor (alebo inou rolou, ktorá zahŕňa prístup Contributor).

Ak nemáte Azure účet, vytvorte si [bezplatný účet predtým, ako začnete](https://azure.microsoft.com).

### Žiadosť o zvýšenie kvóty

Žiadosť o zvýšenie kvóty môžete podať priamo z My quotas. Postupujte podľa nasledujúcich krokov na podanie žiadosti o zvýšenie kvóty. V tomto príklade môžete vybrať akúkoľvek nastaviteľnú kvótu vo vašom predplatnom.

Prihláste sa do [Azure portálu](https://portal.azure.com).

Do vyhľadávacieho poľa zadajte "quotas" a potom vyberte Quotas.  
![Kvóta](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Na stránke Overview vyberte poskytovateľa, napríklad Compute alebo AML.

**Poznámka**: Pre všetkých poskytovateľov okrem Compute uvidíte stĺpec Request increase namiesto stĺpca Adjustable popísaného nižšie. Tam môžete požiadať o zvýšenie konkrétnej kvóty alebo vytvoriť žiadosť o podporu na zvýšenie.

Na stránke My quotas, v stĺpci Quota name, vyberte kvótu, ktorú chcete zvýšiť. Uistite sa, že stĺpec Adjustable ukazuje Yes pre túto kvótu.

V hornej časti stránky vyberte New Quota Request a potom vyberte Enter a new limit.

![Zvýšenie kvóty](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

V paneli New Quota Request zadajte číselnú hodnotu pre nový limit kvóty a potom vyberte Submit.

Vaša žiadosť bude preskúmaná a budete informovaní, či ju možno splniť. Zvyčajne sa tak stane do niekoľkých minút.

Ak vaša žiadosť nebude splnená, zobrazí sa odkaz na vytvorenie žiadosti o podporu. Keď použijete tento odkaz, inžinier podpory vám pomôže s vašou žiadosťou o zvýšenie.

## Odporúčané SKU strojov GPU na Azure

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Tu sú niektoré príklady:

### Ak máte GPU A100 alebo H100

Úplné doladenie zvyčajne prináša najlepšiu výkonnosť. Na doladenie Phi-3-V pre klasifikáciu nenávistných mémov môžete použiť nasledujúci príkaz:

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Ak máte Standard_ND40rs_v2 8x V100-32GB GPU

Je stále možné plne doladiť Phi-3-V pre klasifikáciu nenávistných mémov. Avšak očakávajte oveľa nižší priepust v porovnaní s GPU A100 alebo H100 kvôli absencii podpory flash attention.  
Presnosť môže byť tiež ovplyvnená kvôli absencii podpory bf16 (namiesto toho sa používa fp16 mixed-precision tréning).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Ak nemáte prístup k datacentrovým GPU

LoRA môže byť vašou jedinou možnosťou. Na doladenie Phi-3-V pre klasifikáciu nenávistných mémov môžete použiť nasledujúci príkaz:

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Pre GPU Turing+ je podporovaný QLoRA.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Odporúčané hyperparametre a očakávaná presnosť
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

Metóda tréningu | Zmrazený vizuálny model | Typ dát | LoRA rank | LoRA alpha | Veľkosť batchu | Learning rate | Počet epoch | Presnosť
--- | --- | --- | --- | --- | --- | --- | --- | --- |
úplné doladenie |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
úplné doladenie | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA výsledky čoskoro |  |  |  |  |  |  |  |  |

### POZNÁMKA
Nižšie uvedené výsledky pre DocVQA a nenávistné mémy sú založené na predchádzajúcej verzii (Phi-3-vision).  
Nové výsledky s Phi-3.5-vision budú čoskoro aktualizované.

### DocVQA (POZNÁMKA: Phi-3-vision)

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

Metóda tréningu | Typ dát | LoRA rank | LoRA alpha | Veľkosť batchu | Learning rate | Počet epoch | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
úplné doladenie | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
úplné doladenie | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
zmrazený vizuálny model| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
zmrazený vizuálny model| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Nenávistné mémy (POZNÁMKA: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Metóda tréningu | Typ dát | LoRA rank | LoRA alpha | Veľkosť batchu | Learning rate | Počet epoch | Presnosť
--- | --- | --- | --- | --- | --- | --- | --- |
úplné doladenie | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
úplné doladenie | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
zmrazený vizuálny model| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
zmrazený vizuálny model| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Rýchlostné benchmarky (POZNÁMKA: Phi-3-vision)

Nové benchmarky s Phi-3.5-vision budú čoskoro aktualizované.

Rýchlostné benchmarky boli vykonané na datasete DocVQA. Priemerná dĺžka sekvencie tohto datasetu je 2443.23 tokenov (pri použití `num_crops=16` pre vizuálny model).

### 8x A100-80GB (Ampere)

Metóda tréningu | \# uzlov | GPU | flash attention | Efektívna veľkosť batchu | Priepustnosť (img/s) | Zrýchlenie | Maximálna pamäť GPU (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
úplné doladenie | 1 | 8 |  | 64 | 5.041 |  1x | ~42
úplné doladenie | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
úplné doladenie | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
úplné doladenie | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
zmrazený vizuálny model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
zmrazený vizuálny model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Metóda tréningu | \# uzlov | GPU | flash attention | Efektívna veľkosť batchu | Priepustnosť (img/s) | Zrýchlenie | Maximálna pamäť GPU (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
úplné doladenie | 1 | 8 | | 64 | 2.462 |  1x | ~32
úplné doladenie | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
úplné doladenie | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
zmrazený vizuálny model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Známé problémy

- Nemožno spustiť flash attention s fp16 (bf16 je vždy odporúčaný, ak je dostupný, a všetky GPU podporujúce flash attention podporujú aj bf16).  
- Zatiaľ nepodporujeme ukladanie medzičasu a obnovenie tréningu.

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových prekladových služieb založených na umelej inteligencii. Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.