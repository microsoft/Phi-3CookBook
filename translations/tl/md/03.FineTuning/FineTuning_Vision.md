# Recipe para sa Phi-3.5-vision Finetuning

Ito ang opisyal na gabay para sa finetuning ng Phi-3.5-vision gamit ang mga huggingface libraries. Mangyaring pumunta sa direktoryo ng code [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) bago patakbuhin ang mga sumusunod na utos.

## Pag-install

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

## Mabilisang Simula

Mayroon kaming dalawang halimbawa ng finetuning scripts: isa para sa DocVQA at isa para sa hateful meme classification.

Minimal na hardware na nasubukan: 4x RTX8000 (48GB RAM bawat GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Ngayon, opisyal nang sinusuportahan ng Phi-3.5-vision ang multi-image inputs. Narito ang isang halimbawa para sa finetuning ng NLVR2:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Gabay sa Paggamit

Depende sa hardware, maaaring pumili ang mga user ng iba't ibang finetuning strategies. Sinusuportahan namin ang full-finetuning (gamit ang Deepspeed Zero-2) na may opsyonal na frozen vision parameters, at LoRA (kasama ang 4bit QLoRA). Sa pangkalahatan, inirerekomenda namin ang paggamit ng full finetuning na may flash attention at bf16 kung posible.

### Gabay para sa pag-convert ng iyong custom dataset sa kinakailangang format

Ginagamit namin ang isang minimum na video classification dataset (isang subset ng UCF-101) bilang isang end-to-end na halimbawa upang ipakita kung paano i-convert ang iyong custom dataset sa kinakailangang format at i-finetune ang Phi-3.5-vision dito.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Ang na-convert na data ay magmumukhang ganito:

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

Para sa `jsonl` annotation, ang bawat linya ay dapat na isang dictionary tulad nito:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Tandaan na ang `conversations` ay isang listahan, kaya maaaring suportahan ang multi-turn na pag-uusap kung may ganitong data.

## Paghingi ng Azure GPU Quota 

### Mga Kinakailangan

Isang Azure account na may Contributor role (o iba pang role na may kasamang Contributor access).

Kung wala ka pang Azure account, gumawa ng [libreng account bago magsimula](https://azure.microsoft.com).

### Paghingi ng quota increase

Maaari kang magsumite ng kahilingan para sa quota increase nang direkta mula sa My quotas. Sundin ang mga hakbang sa ibaba upang humiling ng pagtaas para sa isang quota. Para sa halimbawang ito, maaari kang pumili ng anumang adjustable quota sa iyong subscription.

Mag-sign in sa [Azure portal](https://portal.azure.com).

Ilagay ang "quotas" sa search box, at pagkatapos ay piliin ang Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Sa Overview page, pumili ng provider, tulad ng Compute o AML.

**Tandaan** Para sa lahat ng provider maliban sa Compute, makikita mo ang Request increase column sa halip na Adjustable column na inilarawan sa ibaba. Doon, maaari kang humiling ng pagtaas para sa isang partikular na quota, o lumikha ng support request para sa pagtaas.

Sa My quotas page, sa ilalim ng Quota name, piliin ang quota na nais mong taasan. Siguraduhing nagpapakita ng Yes ang Adjustable column para sa quota na ito.

Sa itaas ng pahina, piliin ang New Quota Request, pagkatapos ay piliin ang Enter a new limit.  
![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Sa New Quota Request pane, maglagay ng numerical value para sa iyong bagong quota limit, pagkatapos ay piliin ang Submit.

Ang iyong kahilingan ay susuriin, at aabisuhan ka kung maaaring matupad ang kahilingan. Karaniwang nangyayari ito sa loob ng ilang minuto.

Kung hindi matupad ang iyong kahilingan, makikita mo ang isang link upang lumikha ng support request. Kapag ginamit mo ang link na ito, tutulungan ka ng isang support engineer sa iyong kahilingan para sa pagtaas.

## Mga Mungkahi sa Azure Compute GPU Machine SKU

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Narito ang ilang halimbawa:

### Kung mayroon kang A100 o H100 GPUs

Karaniwan, ang full finetuning ang nagbibigay ng pinakamahusay na performance. Maaari mong gamitin ang sumusunod na utos upang i-finetune ang Phi-3-V sa hateful memes classification.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Kung mayroon kang Standard_ND40rs_v2 8x V100-32GB GPUs

Maaari pa ring i-finetune nang buo ang Phi-3-V sa hateful memes classification. Gayunpaman, asahan ang mas mababang throughput kumpara sa A100 o H100 GPUs dahil sa kawalan ng flash attention support. Ang accuracy ay maaari ring maapektuhan dahil sa kawalan ng bf16 support (fp16 mixed-precision training ang ginagamit sa halip).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Kung wala kang access sa data center GPUs
Ang LoRA ang maaaring maging tanging opsyon mo. Maaari mong gamitin ang sumusunod na utos upang i-finetune ang Phi-3-V sa hateful memes classification.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Para sa Turing+ GPU, sinusuportahan ang QLoRA.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Mga Inirekomendang Hyperparameters at Inaasahang Accuracy
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

Paraan ng Pagsasanay | Frozen vision model | uri ng data | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
LoRA results comming soon |  |  |  |  |  |  |  |  |

### TANDAAN
Ang mga resulta sa ibaba para sa DocVQA at Hateful memes ay batay sa nakaraang bersyon (Phi-3-vision).  
Ang mga bagong resulta gamit ang Phi-3.5-vision ay ia-update sa lalong madaling panahon.

### DocVQA (TANDAAN: Phi-3-vision)

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

Paraan ng Pagsasanay | uri ng data | LoRA rank | LoRA alpha | batch size | learning rate | epochs | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
frozen image model| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
frozen image model| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (TANDAAN: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Paraan ng Pagsasanay | uri ng data | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
frozen image model| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
frozen image model| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Speed Benchmarking (TANDAAN: Phi-3-vision)

Ang mga bagong resulta ng benchmarking gamit ang Phi-3.5-vision ay ia-update sa lalong madaling panahon.

Ang speed benchmarking ay isinagawa sa DocVQA dataset. Ang average sequence length ng dataset na ito ay 2443.23 tokens (gamit ang `num_crops=16` para sa image model).

### 8x A100-80GB (Ampere)

Paraan ng Pagsasanay | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)  
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

Paraan ng Pagsasanay | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Mga Kilalang Isyu

- Hindi maaaring patakbuhin ang flash attention gamit ang fp16 (palaging inirerekomenda ang bf16 kung available, at lahat ng GPUs na sumusuporta sa flash attention ay sumusuporta rin sa bf16).  
- Hindi pa sinusuportahan ang pag-save ng intermediate checkpoints at ang pagpapatuloy ng pagsasanay.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyong pang-AI na awtomatikong pagsasalin. Bagama't sinisikap naming maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Kami ay hindi mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.