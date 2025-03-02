# Mwongozo wa Kuweka Mazoezi kwa Phi-3.5-vision

Hii ni msaada rasmi wa kuweka mazoezi kwa Phi-3.5-vision kwa kutumia maktaba za huggingface. Tafadhali `cd` kwenye folda ya msimbo [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) kabla ya kuendesha amri zifuatazo.

## Usakinishaji

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

## Mwanzo wa Haraka

Tunatoa skripti mbili za mfano za kuweka mazoezi, moja kwa DocVQA na nyingine kwa uainishaji wa memes za chuki.

Vifaa vya chini vilivyopimwa: 4x RTX8000 (48GB RAM kwa kila GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision sasa inasaidia rasmi pembejeo za picha nyingi. Hapa kuna mfano wa kuweka mazoezi kwa NLVR2.

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Mwongozo wa Matumizi

Kulingana na vifaa, watumiaji wanaweza kuchagua mikakati tofauti ya kuweka mazoezi. Tunasaidia kuweka mazoezi kamili (kwa Deepspeed Zero-2) huku vigezo vya picha vikibaki kufungwa, na LoRA (ikiwa ni pamoja na QLoRA ya 4bit). Kwa ujumla, tunapendekeza kutumia kuweka mazoezi kamili na flash attention na bf16 inapowezekana.

### Mwongozo wa kubadilisha seti yako ya data kuwa muundo unaohitajika

Tunatumia seti ndogo ya data ya uainishaji wa video (sehemu ndogo ya UCF-101) kama mfano wa mwisho hadi mwisho kuonyesha jinsi ya kubadilisha seti yako ya data kuwa muundo unaohitajika na kuweka mazoezi ya Phi-3.5-vision juu yake.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Data iliyobadilishwa itaonekana kama ifuatavyo:

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

Kwa anotesheni ya `jsonl`, kila mstari unapaswa kuwa kamusi kama:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Kumbuka kuwa `conversations` ni orodha, hivyo mazungumzo ya zamu nyingi yanaweza kuungwa mkono ikiwa data kama hiyo inapatikana.

## Kuomba Kiwango cha GPU cha Azure

### Mahitaji ya Awali

Akaunti ya Azure yenye jukumu la Mchangiaji (au jukumu jingine linalojumuisha ufikiaji wa Mchangiaji).

Ikiwa huna akaunti ya Azure, unda [akaunti ya bure kabla ya kuanza](https://azure.microsoft.com).

### Kuomba ongezeko la kiwango

Unaweza kuwasilisha ombi la ongezeko la kiwango moja kwa moja kutoka kwa My quotas. Fuata hatua zilizo hapa chini kuomba ongezeko la kiwango. Kwa mfano huu, unaweza kuchagua kiwango chochote kinachoweza kubadilishwa kwenye usajili wako.

Ingia kwenye [Azure portal](https://portal.azure.com).

Weka "quotas" kwenye kisanduku cha utafutaji, kisha uchague Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Kwenye ukurasa wa Muhtasari, chagua mtoa huduma, kama vile Compute au AML.

**Kumbuka** Kwa watoa huduma wote isipokuwa Compute, utaona safu ya Request increase badala ya safu ya Adjustable iliyotajwa hapa chini. Hapo, unaweza kuomba ongezeko kwa kiwango maalum, au kuunda ombi la msaada kwa ongezeko hilo.

Kwenye ukurasa wa My quotas, chini ya Quota name, chagua kiwango unachotaka kuongeza. Hakikisha kuwa safu ya Adjustable inaonyesha Ndiyo kwa kiwango hiki.

Karibu juu ya ukurasa, chagua New Quota Request, kisha uchague Enter a new limit.  
![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Katika sehemu ya New Quota Request, ingiza thamani ya nambari kwa kiwango chako kipya, kisha uchague Submit.

Ombi lako litakaguliwa, na utaarifiwa ikiwa ombi linaweza kutekelezwa. Hii kwa kawaida hufanyika ndani ya dakika chache.

Ikiwa ombi lako halitatekelezwa, utaona kiungo cha kuunda ombi la msaada. Unapotumia kiungo hiki, mhandisi wa msaada atakusaidia na ombi lako la ongezeko.

## Mapendekezo ya SKU ya Mashine za GPU za Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Hapa kuna baadhi ya mifano:

### Ikiwa una GPU za A100 au H100

Kuweka mazoezi kamili kwa kawaida hutoa utendaji bora. Unaweza kutumia amri ifuatayo kuweka mazoezi ya Phi-3-V kwenye uainishaji wa memes za chuki.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Ikiwa una Standard_ND40rs_v2 8x V100-32GB GPUs

Bado inawezekana kuweka mazoezi kamili ya Phi-3-V kwenye uainishaji wa memes za chuki. Hata hivyo, tarajia kasi ya chini zaidi ikilinganishwa na GPU za A100 au H100 kutokana na ukosefu wa msaada wa flash attention. Usahihi pia unaweza kuathiriwa kwa sababu ya ukosefu wa msaada wa bf16 (badala yake, mafunzo ya mchanganyiko wa usahihi wa fp16 hutumiwa).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Ikiwa huna ufikiaji wa GPU za kituo cha data

LoRA inaweza kuwa chaguo lako pekee. Unaweza kutumia amri ifuatayo kuweka mazoezi ya Phi-3-V kwenye uainishaji wa memes za chuki.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Kwa GPU za Turing+, QLoRA inasaidiwa.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Hyperparameters Zilizopendekezwa na Usahihi Unaotarajiwa
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

Njia ya Mafunzo | Mfano wa picha uliogandishwa | aina ya data | LoRA rank | LoRA alpha | ukubwa wa kundi | kiwango cha kujifunza | vipindi | Usahihi  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
LoRA results comming soon |  |  |  |  |  |  |  |  |

### KUMBUKA
Matokeo ya DocVQA na Memes za Chuki yaliyo hapa chini yanatokana na toleo la awali (Phi-3-vision).  
Matokeo mapya na Phi-3.5-vision yataongezwa hivi karibuni.

### DocVQA (KUMBUKA: Phi-3-vision)

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

Njia ya Mafunzo | aina ya data | LoRA rank | LoRA alpha | ukubwa wa kundi | kiwango cha kujifunza | vipindi | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
frozen image model| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
frozen image model| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Memes za Chuki (KUMBUKA: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Njia ya Mafunzo | aina ya data | LoRA rank | LoRA alpha | ukubwa wa kundi | kiwango cha kujifunza | vipindi | Usahihi  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
frozen image model| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
frozen image model| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Upimaji wa Kasi (KUMBUKA: Phi-3-vision)

Matokeo mapya ya upimaji wa kasi na Phi-3.5-vision yataongezwa hivi karibuni.

Upimaji wa kasi unafanywa kwenye seti ya data ya DocVQA. Urefu wa wastani wa mlolongo wa seti hii ya data ni tokeni 2443.23 (kwa kutumia `num_crops=16` kwa mfano wa picha).

### 8x A100-80GB (Ampere)

Njia ya Mafunzo | \# nodes | GPUs | flash attention | Ukubwa wa Kundi Halisi | Kasi ya Uzalishaji (img/s) | Kuongeza Kasi | Kumbukumbu ya Juu ya GPU (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
frozen image model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
frozen image model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Njia ya Mafunzo | \# nodes | GPUs | flash attention | Ukubwa wa Kundi Halisi | Kasi ya Uzalishaji (img/s) | Kuongeza Kasi | Kumbukumbu ya Juu ya GPU (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Masuala Yanayojulikana

- Haiwezi kuendesha flash attention na fp16 (bf16 inapendekezwa kila wakati inapopatikana, na GPU zote zinazounga mkono flash attention pia zinaunga mkono bf16).  
- Haikubali kuhifadhi alama za kati na kuendelea na mafunzo bado.  

**Kanusho:**  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za kiakili za mashine. Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa habari muhimu, inashauriwa kutumia tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.