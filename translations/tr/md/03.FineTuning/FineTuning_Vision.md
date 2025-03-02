# Phi-3.5-vision ince ayar tarifi

Bu, huggingface kütüphanelerini kullanarak Phi-3.5-vision ince ayarını destekleyen resmi dökümandır. Lütfen aşağıdaki komutları çalıştırmadan önce [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) kod dizinine `cd` yapın.

## Kurulum

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

## Hızlı başlangıç

DocVQA ve nefret içerikli meme sınıflandırması için iki örnek ince ayar betiği sağlıyoruz.

Test edilen minimum donanım: 4x RTX8000 (GPU başına 48GB RAM)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision artık resmi olarak çoklu görüntü girişlerini destekliyor. NLVR2 ince ayarı için bir örnek aşağıda verilmiştir:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Kullanım rehberi

Donanıma bağlı olarak, kullanıcılar farklı ince ayar stratejileri seçebilir. Tam ince ayar (Deepspeed Zero-2 ile), isteğe bağlı olarak sabitlenmiş görüntü parametreleriyle ve LoRA (4bit QLoRA dahil) desteklenmektedir. Genel olarak, mümkün olduğunda flash attention ve bf16 ile tam ince ayar önerilir.

### Özel veri setinizi gerekli formata dönüştürmek için rehber

Özel veri setinizi gerekli formata dönüştürmek ve Phi-3.5-vision üzerinde ince ayar yapmak için uçtan uca bir örnek olarak minimum video sınıflandırma veri setini (UCF-101'in bir alt kümesi) kullanıyoruz.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Dönüştürülen veri şu şekilde görünecektir:

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

`jsonl` açıklaması için, her satır bir sözlük olmalıdır:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Dikkat edilmesi gereken nokta, `conversations` bir listedir, bu nedenle bu tür veriler mevcutsa çoklu dönüşümlü konuşmalar desteklenebilir.

## Azure GPU Kotası Talep Etme 

### Ön Gereksinimler

Katkıda Bulunan rolüne (veya Katkıda Bulunan erişimi içeren başka bir role) sahip bir Azure hesabı.

Bir Azure hesabınız yoksa, başlamadan önce bir [ücretsiz hesap oluşturun](https://azure.microsoft.com).

### Kota artırımı talebi gönderme

Kota artırımı talebinizi doğrudan Kotam sayfasından gönderebilirsiniz. Aboneliğinizdeki herhangi bir ayarlanabilir kotayı seçerek aşağıdaki adımları izleyin.

[Azure portalına](https://portal.azure.com) giriş yapın.

Arama kutusuna "kotalar" yazın ve ardından Kotalar'ı seçin.  
![Kota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Genel Bakış sayfasında, Compute veya AML gibi bir sağlayıcı seçin.

**Not** Compute dışındaki tüm sağlayıcılar için, aşağıda açıklanan Ayarlanabilir sütunu yerine Bir Artış Talep Et sütununu görürsünüz. Buradan belirli bir kota için bir artış talep edebilir veya artış için bir destek talebi oluşturabilirsiniz.

Kotalarım sayfasında, Kota adı altında artırmak istediğiniz kotayı seçin. Bu kotanın Ayarlanabilir sütununda Evet yazdığından emin olun.

Sayfanın üst kısmında Yeni Kota Talebi'ni seçin, ardından Yeni bir limit girin'i seçin.  
![Kota Artır](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Yeni Kota Talebi panelinde, yeni kota sınırınız için sayısal bir değer girin ve ardından Gönder'i seçin.

Talebiniz incelenecek ve talebin karşılanıp karşılanamayacağı size bildirilecektir. Bu genellikle birkaç dakika içinde gerçekleşir.

Talebiniz karşılanmazsa, bir destek talebi oluşturmak için bir bağlantı görürsünüz. Bu bağlantıyı kullandığınızda, bir destek mühendisi artış talebinizde size yardımcı olacaktır.

## Azure Compute GPU makine SKU önerileri

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Bazı örnekler:

### A100 veya H100 GPU'larınız varsa

Tam ince ayar genellikle en iyi performansı sağlar. Phi-3-V'yi nefret içerikli meme sınıflandırması için ince ayarlamak için aşağıdaki komutu kullanabilirsiniz.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Standard_ND40rs_v2 8x V100-32GB GPU'larınız varsa

Phi-3-V'yi nefret içerikli meme sınıflandırması için tam ince ayar yapmak hala mümkündür. Ancak, flash attention desteğinin olmaması nedeniyle çok daha düşük bir verim bekleyin. bf16 desteğinin olmaması (yerine fp16 karışık hassasiyetli eğitim kullanılır) nedeniyle doğruluk da etkilenebilir.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Veri merkezi GPU'larına erişiminiz yoksa

LoRA sizin tek seçeneğiniz olabilir. Phi-3-V'yi nefret içerikli meme sınıflandırması için ince ayarlamak için aşağıdaki komutu kullanabilirsiniz.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU için QLoRA desteklenmektedir.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Önerilen hiperparametreler ve beklenen doğruluk
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

Eğitim yöntemi | Sabitlenmiş görüntü modeli | veri tipi | LoRA rank | LoRA alpha | batch boyutu | öğrenme oranı | epoch | Doğruluk
--- | --- | --- | --- | --- | --- | --- | --- | --- |
tam ince ayar |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
tam ince ayar | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA sonuçları yakında gelecek |  |  |  |  |  |  |  |  |

### NOT
Aşağıdaki DocVQA ve Hateful memes sonuçları önceki sürüme (Phi-3-vision) dayanmaktadır. Phi-3.5-vision ile yeni sonuçlar yakında güncellenecektir.

### DocVQA (NOT: Phi-3-vision)

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

Eğitim yöntemi | veri tipi | LoRA rank | LoRA alpha | batch boyutu | öğrenme oranı | epoch | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
tam ince ayar | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
tam ince ayar | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
sabitlenmiş görüntü modeli| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
sabitlenmiş görüntü modeli| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (NOT: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Eğitim yöntemi | veri tipi | LoRA rank | LoRA alpha | batch boyutu | öğrenme oranı | epoch | Doğruluk
--- | --- | --- | --- | --- | --- | --- | --- |
tam ince ayar | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
tam ince ayar | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
sabitlenmiş görüntü modeli| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
sabitlenmiş görüntü modeli| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Hız kıyaslaması (NOT: Phi-3-vision)

Phi-3.5-vision ile yeni kıyaslama sonuçları yakında güncellenecektir.

Hız kıyaslaması DocVQA veri seti üzerinde gerçekleştirilmiştir. Bu veri setinin ortalama sekans uzunluğu 2443.23 tokendir (`num_crops=16` kullanılarak görüntü modeli için).

### 8x A100-80GB (Ampere)

Eğitim yöntemi | \# düğüm | GPU | flash attention | Etkili batch boyutu | Verim (img/s) | Hızlanma | Maks. GPU bellek (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
tam ince ayar | 1 | 8 |  | 64 | 5.041 |  1x | ~42
tam ince ayar | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
tam ince ayar | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
tam ince ayar | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
sabitlenmiş görüntü modeli | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
sabitlenmiş görüntü modeli | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Eğitim yöntemi | \# düğüm | GPU | flash attention | Etkili batch boyutu | Verim (img/s) | Hızlanma | Maks. GPU bellek (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
tam ince ayar | 1 | 8 | | 64 | 2.462 |  1x | ~32
tam ince ayar | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
tam ince ayar | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
sabitlenmiş görüntü modeli | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Bilinen sorunlar

- fp16 ile flash attention çalıştırılamıyor (bf16 her zaman önerilir ve flash attention destekleyen tüm GPU'lar bf16'yı da destekler).  
- Ara kontrol noktalarını kaydetme ve eğitimi yeniden başlatma henüz desteklenmiyor.

**Feragatname**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yorumlamalardan sorumlu değiliz.