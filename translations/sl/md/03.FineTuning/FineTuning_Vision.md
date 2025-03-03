# Recept za fino uglaševanje Phi-3.5-vision

To je uradna podpora za fino uglaševanje Phi-3.5-vision z uporabo knjižnic huggingface.  
Pred zagonom naslednjih ukazov se pomaknite do kode v imeniku [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning).

## Namestitev

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

## Hiter začetek

Na voljo sta dva primera skriptov za fino uglaševanje, eden za DocVQA in drugi za klasifikacijo sovražnih memov.

Minimalna strojna oprema testirana na 4x RTX8000 (48 GB RAM na GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision zdaj uradno podpira vnose z več slikami. Tukaj je primer za fino uglaševanje NLVR2.

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Navodila za uporabo

Glede na strojno opremo lahko uporabniki izbirajo med različnimi strategijami za fino uglaševanje. Podpiramo popolno fino uglaševanje (z Deepspeed Zero-2) z možnostjo zamrznitve parametrov vizualnega modela ter LoRA (vključno s 4bit QLoRA).  
Na splošno priporočamo uporabo popolnega finega uglaševanja z bliskovito pozornostjo (flash attention) in bf16, kadar je to mogoče.

### Navodila za pretvorbo vašega prilagojenega nabora podatkov v zahtevano obliko

Za demonstracijo, kako pretvoriti vaš prilagojen nabor podatkov v zahtevano obliko in fino uglaševati Phi-3.5-vision na njem, uporabljamo minimalni nabor podatkov za video klasifikacijo (podnabor UCF-101) kot primer od začetka do konca.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Pretvorjeni podatki bodo videti takole:

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

Za `jsonl` anotacijo mora vsaka vrstica biti slovar, kot je ta:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Opomba: `conversations` je seznam, kar pomeni, da je podprt večstopenjski pogovor, če so taki podatki na voljo.

## Zahtevanje kvote za Azure GPU

### Predpogoji

Azure račun z vlogo Contributor (ali drugo vlogo, ki vključuje dostop Contributorja).  

Če nimate Azure računa, ustvarite [brezplačen račun pred začetkom](https://azure.microsoft.com).

### Zahteva za povečanje kvote

Zahtevo za povečanje kvote lahko oddate neposredno iz razdelka My quotas. Sledite spodnjim korakom za zahtevo za povečanje kvote. Za ta primer lahko izberete katero koli prilagodljivo kvoto v svoji naročnini.

Prijavite se v [Azure portal](https://portal.azure.com).

V iskalno polje vnesite "quotas" in nato izberite Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Na strani Pregled (Overview) izberite ponudnika, kot sta Compute ali AML.

**Opomba**: Pri vseh ponudnikih razen Compute boste videli stolpec Request increase namesto opisanega stolpca Adjustable. Tam lahko zahtevate povečanje določene kvote ali ustvarite zahtevo za podporo za povečanje.

Na strani My quotas pod Quota name izberite kvoto, ki jo želite povečati. Prepričajte se, da stolpec Adjustable za to kvoto prikazuje Yes.

Blizu vrha strani izberite New Quota Request, nato pa Enter a new limit.  
![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

V podoknu New Quota Request vnesite številčno vrednost za svojo novo kvotno omejitev in nato izberite Submit.

Vaša zahteva bo pregledana, in obveščeni boste, če jo je mogoče izpolniti. To se običajno zgodi v nekaj minutah.

Če vaša zahteva ni izpolnjena, boste videli povezavo za ustvarjanje zahteve za podporo. Ko uporabite to povezavo, vam bo inženir za podporo pomagal pri vaši zahtevi za povečanje.

## Predlogi za SKU strojev z Azure Compute GPU

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Tukaj je nekaj primerov:

### Če imate A100 ali H100 GPU-je

Popolno fino uglaševanje običajno daje najboljše rezultate. Uporabite naslednji ukaz za fino uglaševanje Phi-3-V na klasifikaciji sovražnih memov.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Če imate Standard_ND40rs_v2 8x V100-32GB GPU-je

Še vedno je možno popolno fino uglaševanje Phi-3-V na klasifikaciji sovražnih memov. Vendar pričakujte precej nižjo prepustnost v primerjavi z A100 ali H100 GPU-ji zaradi pomanjkanja podpore za bliskovito pozornost.  
Točnost bi lahko bila prav tako prizadeta zaradi pomanjkanja podpore za bf16 (namesto tega se uporablja fp16 mešano natančno učenje).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Če nimate dostopa do podatkovno-centerskih GPU-jev

LoRA bi lahko bila vaša edina izbira. Uporabite naslednji ukaz za fino uglaševanje Phi-3-V na klasifikaciji sovražnih memov.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Za Turing+ GPU-je je podprt QLoRA.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Predlagani hiperparametri in pričakovana točnost

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

Metoda učenja | Zamrznjen vizualni model | Tip podatkov | LoRA rank | LoRA alpha | Velikost serije | Učna stopnja | Število epoh | Točnost  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
popolno fino uglaševanje |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
popolno fino uglaševanje | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
Rezultati LoRA prihajajo kmalu |  |  |  |  |  |  |  |  |

### OPOMBA

Spodnji rezultati za DocVQA in sovražne meme temeljijo na prejšnji različici (Phi-3-vision).  
Novi rezultati s Phi-3.5-vision bodo posodobljeni kmalu.

### DocVQA (OPOMBA: Phi-3-vision)

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

Metoda učenja | Tip podatkov | LoRA rank | LoRA alpha | Velikost serije | Učna stopnja | Število epoh | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
popolno fino uglaševanje | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
popolno fino uglaševanje | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
zamrznjen vizualni model | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
zamrznjen vizualni model | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  

### Sovražni memi (OPOMBA: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Metoda učenja | Tip podatkov | LoRA rank | LoRA alpha | Velikost serije | Učna stopnja | Število epoh | Točnost  
--- | --- | --- | --- | --- | --- | --- | --- |  
popolno fino uglaševanje | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
popolno fino uglaševanje | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
zamrznjen vizualni model | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
zamrznjen vizualni model | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |  

## Primerjava hitrosti (OPOMBA: Phi-3-vision)

Novi rezultati primerjave hitrosti s Phi-3.5-vision bodo posodobljeni kmalu.

Primerjava hitrosti je izvedena na naboru podatkov DocVQA. Povprečna dolžina zaporedja tega nabora podatkov je 2443.23 tokenov (z uporabo `num_crops=16` za vizualni model).

### 8x A100-80GB (Ampere)

Metoda učenja | \# vozlišč | GPU-ji | bliskovita pozornost | Efektivna velikost serije | Prepustnost (img/s) | Pospešek | Najvišja poraba GPU pomnilnika (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
popolno fino uglaševanje | 1 | 8 |  | 64 | 5.041 | 1x | ~42  
popolno fino uglaševanje | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
popolno fino uglaševanje | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
popolno fino uglaševanje | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
zamrznjen vizualni model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
zamrznjen vizualni model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Metoda učenja | \# vozlišč | GPU-ji | bliskovita pozornost | Efektivna velikost serije | Prepustnost (img/s) | Pospešek | Najvišja poraba GPU pomnilnika (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
popolno fino uglaševanje | 1 | 8 | | 64 | 2.462 | 1x | ~32  
popolno fino uglaševanje | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
popolno fino uglaševanje | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
zamrznjen vizualni model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Znane težave

- Flash attention ne deluje z fp16 (bf16 je vedno priporočljiv, kadar je na voljo, in vsi GPU-ji, ki podpirajo flash attention, podpirajo tudi bf16).  
- Trenutno ni podpore za shranjevanje vmesnih kontrolnih točk in nadaljevanje učenja.  

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvirnem jeziku se šteje za avtoritativni vir. Za ključne informacije priporočamo strokovno človeško prevajanje. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.