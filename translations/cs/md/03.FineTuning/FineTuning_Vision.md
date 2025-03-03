# Recept pro doladění Phi-3.5-vision

Toto je oficiální podpora doladění Phi-3.5-vision pomocí knihoven huggingface.  
Přejděte prosím do adresáře s kódem [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) před spuštěním následujících příkazů.

## Instalace

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

## Rychlý start

Poskytujeme dva příklady skriptů pro doladění, jeden pro DocVQA a druhý pro klasifikaci nenávistných memů.

Minimální hardware testován na 4x RTX8000 (48 GB RAM na GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision nyní oficiálně podporuje vstupy s více obrázky. Zde je příklad doladění NLVR2:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Uživatelská příručka

V závislosti na hardwaru si uživatelé mohou zvolit různé strategie doladění. Podporujeme plné doladění (s Deepspeed Zero-2) s volitelně zmrazenými parametry vizuálního modelu a LoRA (včetně 4bit QLoRA).  
Obecně doporučujeme používat plné doladění s flash attention a bf16, kdykoli je to možné.

### Příručka pro převod vlastního datasetu na požadovaný formát

Používáme minimální dataset pro klasifikaci videí (podmnožinu UCF-101) jako end-to-end příklad, který ukazuje, jak převést vlastní dataset na požadovaný formát a doladit Phi-3.5-vision na něm.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Převedená data budou vypadat takto:

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

Pro anotaci `jsonl` by měl každý řádek být slovníkem jako:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Všimněte si, že `conversations` je seznam, což umožňuje podporu víceotáčkové konverzace, pokud jsou taková data k dispozici.

## Žádost o kvótu GPU na Azure 

### Předpoklady

Účet Azure s rolí Contributor (nebo jinou rolí zahrnující přístup Contributor).

Pokud ještě nemáte účet Azure, vytvořte si [bezplatný účet před začátkem](https://azure.microsoft.com).

### Požadavek na zvýšení kvóty

Žádost o zvýšení kvóty můžete podat přímo z My quotas. Postupujte podle níže uvedených kroků, abyste požádali o zvýšení kvóty. Pro tento příklad můžete vybrat jakoukoli nastavitelnou kvótu ve svém předplatném.

Přihlaste se do [Azure portálu](https://portal.azure.com).

Do vyhledávacího pole zadejte "quotas" a poté vyberte Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Na stránce Přehled vyberte poskytovatele, například Compute nebo AML.

**Poznámka**: Pro všechny poskytovatele kromě Compute uvidíte sloupec Request increase místo sloupce Adjustable popsaného níže. Tam můžete požádat o zvýšení konkrétní kvóty nebo vytvořit žádost o podporu pro zvýšení.

Na stránce My quotas, pod názvem kvóty, vyberte kvótu, kterou chcete zvýšit. Ujistěte se, že sloupec Adjustable zobrazuje Ano pro tuto kvótu.

V horní části stránky vyberte New Quota Request a poté zadejte nový limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

V panelu New Quota Request zadejte číselnou hodnotu pro svůj nový limit kvóty a poté vyberte Submit.

Vaše žádost bude přezkoumána a budete informováni, zda ji lze splnit. To obvykle trvá jen několik minut.

Pokud vaše žádost nebude splněna, uvidíte odkaz na vytvoření žádosti o podporu. Když použijete tento odkaz, inženýr podpory vám pomůže s vaší žádostí o zvýšení.

## Doporučení pro SKU strojů GPU na Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Zde jsou některé příklady:

### Pokud máte A100 nebo H100 GPU

Plné doladění obvykle poskytuje nejlepší výkon. Pro doladění Phi-3-V na klasifikaci nenávistných memů můžete použít následující příkaz:

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Pokud máte Standard_ND40rs_v2 8x V100-32GB GPU

Je stále možné plně doladit Phi-3-V na klasifikaci nenávistných memů. Nicméně očekávejte mnohem nižší propustnost ve srovnání s A100 nebo H100 GPU kvůli absenci podpory flash attention. Přesnost může být také ovlivněna kvůli absenci podpory bf16 (místo toho se používá fp16 smíšená přesnost trénování).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Pokud nemáte přístup k datacentrovým GPU
Lora může být vaše jediná volba. Pro doladění Phi-3-V na klasifikaci nenávistných memů můžete použít následující příkaz:

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Pro Turing+ GPU je podporováno QLoRA:

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Doporučené hyperparametry a očekávaná přesnost
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

Metoda trénování | Zmrazený vizuální model | Datový typ | LoRA rank | LoRA alpha | Velikost batch | Learning rate | Epochy | Přesnost
--- | --- | --- | --- | --- | --- | --- | --- | --- |
plné doladění |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
plné doladění | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
Výsledky LoRA budou brzy |  |  |  |  |  |  |  |  |

### POZNÁMKA
Níže uvedené výsledky DocVQA a nenávistných memů jsou založeny na předchozí verzi (Phi-3-vision).  
Nové výsledky s Phi-3.5-vision budou brzy aktualizovány.

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

Metoda trénování | Datový typ | LoRA rank | LoRA alpha | Velikost batch | Learning rate | Epochy | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
plné doladění | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
plné doladění | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
zmrazený vizuální model | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
zmrazený vizuální model | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Nenávistné memy (POZNÁMKA: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Metoda trénování | Datový typ | LoRA rank | LoRA alpha | Velikost batch | Learning rate | Epochy | Přesnost
--- | --- | --- | --- | --- | --- | --- | --- |
plné doladění | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
plné doladění | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
zmrazený vizuální model | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
zmrazený vizuální model | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Benchmarking rychlosti (POZNÁMKA: Phi-3-vision)

Nové výsledky benchmarkingu s Phi-3.5-vision budou brzy aktualizovány.

Benchmarking rychlosti je prováděn na datasetu DocVQA. Průměrná délka sekvence tohoto datasetu je 2443,23 tokenů (s použitím `num_crops=16` pro vizuální model).

### 8x A100-80GB (Ampere)

Metoda trénování | \# uzlů | GPU | flash attention | Efektivní velikost batch | Propustnost (img/s) | Zrychlení | Maximální paměť GPU (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
plné doladění | 1 | 8 |  | 64 | 5.041 |  1x | ~42
plné doladění | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
plné doladění | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
plné doladění | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
zmrazený vizuální model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
zmrazený vizuální model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Metoda trénování | \# uzlů | GPU | flash attention | Efektivní velikost batch | Propustnost (img/s) | Zrychlení | Maximální paměť GPU (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
plné doladění | 1 | 8 | | 64 | 2.462 |  1x | ~32
plné doladění | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
plné doladění | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
zmrazený vizuální model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Známé problémy

- Nelze spustit flash attention s fp16 (bf16 je vždy doporučeno, pokud je k dispozici, a všechny GPU podporující flash attention také podporují bf16).  
- Zatím nepodporujeme ukládání průběžných checkpointů a obnovení trénování.

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových AI překladatelských služeb. I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za jakékoli nedorozumění nebo mylné výklady vyplývající z použití tohoto překladu.