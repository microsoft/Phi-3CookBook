# Phi-3.5-vision फाइनट्यूनिङ प्रक्रिया

यो Phi-3.5-vision फाइनट्यूनिङको लागि आधिकारिक सपोर्ट हो, जुन huggingface लाइब्रेरीहरूको प्रयोग गरेर गरिएको छ। कृपया [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) को कोड डाइरेक्टरीमा जानुहोस् र तलका कमाण्डहरू चलाउनुहोस्।

## स्थापना

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

## छिटो सुरु गर्ने तरिका

हामीले दुईवटा उदाहरण फाइनट्यूनिङ स्क्रिप्टहरू उपलब्ध गराएका छौं, एउटा DocVQA को लागि र अर्को hateful meme classification को लागि।

न्यूनतम हार्डवेयर: 4x RTX8000 (प्रत्येक GPU मा 48GB RAM)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ले अब आधिकारिक रूपमा बहु-छवि इनपुटलाई समर्थन गर्दछ। NLVR2 फाइनट्यूनिङको उदाहरण यहाँ छ:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## प्रयोगकर्ता गाइड

हार्डवेयरको आधारमा, प्रयोगकर्ताहरूले विभिन्न फाइनट्यूनिङ रणनीतिहरू चयन गर्न सक्छन्। हामीले पूर्ण फाइनट्यूनिङ (Deepspeed Zero-2 सहित) को साथ, वैकल्पिक रूपमा frozen vision parameters, र LoRA (4bit QLoRA सहित) समर्थन गरेका छौं। सामान्यतया, flash attention र bf16 को साथ पूर्ण फाइनट्यूनिङ प्रयोग गर्न सिफारिस गरिन्छ।

### आफ्नो कस्टम डेटासेटलाई आवश्यक ढाँचामा रूपान्तरण गर्ने गाइड

हामीले न्यूनतम भिडियो वर्गीकरण डेटासेट (UCF-101 को उपसमूह) लाई अन्त्य-देखि-अन्त्य उदाहरणको रूपमा प्रयोग गरेर कस्टम डेटासेटलाई आवश्यक ढाँचामा कसरी रूपान्तरण गर्ने र Phi-3.5-vision मा फाइनट्यून गर्ने देखाएका छौं।

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

रूपान्तरण गरिएको डाटा यसरी देखिन्छ:

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

`jsonl` एनोटेसनको लागि, प्रत्येक लाइन यस्तो dictionary हुनुपर्छ:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

ध्यान दिनुहोस् कि `conversations` एउटा सूची हो, त्यसैले यदि यस्तो डाटा उपलब्ध छ भने बहु-टर्न संवादलाई समर्थन गर्न सकिन्छ।

## Azure GPU कोटा अनुरोध गर्ने

### आवश्यकताहरू

Contributor भूमिका (वा Contributor पहुँच समावेश गर्ने अर्को भूमिका) भएको Azure खाता।

यदि तपाईं सँग Azure खाता छैन भने, [निःशुल्क खाता बनाउनुहोस्](https://azure.microsoft.com)।

### कोटा वृद्धि अनुरोध

तपाईं My quotas बाट सीधै कोटा वृद्धि अनुरोध पेश गर्न सक्नुहुन्छ। तलका चरणहरू अनुसरण गरेर कोटा वृद्धि गर्न सक्नुहुन्छ। यस उदाहरणको लागि, तपाईं आफ्नो सब्सक्रिप्शनमा कुनै पनि समायोज्य कोटा चयन गर्न सक्नुहुन्छ।

Azure पोर्टलमा [साइन इन गर्नुहोस्](https://portal.azure.com)।

"quotas" सर्च गर्नुहोस् र Quotas चयन गर्नुहोस्।  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Overview पृष्ठमा, Compute वा AML जस्ता provider चयन गर्नुहोस्।

**Note** Compute बाहेकका सबै provider हरूको लागि, Adjustable स्तम्भको सट्टा Request increase स्तम्भ देख्नुहुनेछ। त्यहाँ तपाईं विशिष्ट कोटाको लागि वृद्धि अनुरोध गर्न सक्नुहुन्छ वा वृद्धि अनुरोधको लागि समर्थन अनुरोध सिर्जना गर्न सक्नुहुन्छ।

My quotas पृष्ठमा, Quota name अन्तर्गत तपाईं वृद्धि गर्न चाहनुभएको कोटा चयन गर्नुहोस्। यो कोटाका लागि Adjustable स्तम्भमा "Yes" देखिनु पर्छ।

पृष्ठको माथि, New Quota Request चयन गर्नुहोस्, त्यसपछि Enter a new limit चयन गर्नुहोस्।  
![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request प्यानमा, आफ्नो नयाँ कोटा सीमा लागि संख्यात्मक मान प्रविष्ट गर्नुहोस्, त्यसपछि Submit चयन गर्नुहोस्।

तपाईंको अनुरोध समीक्षा गरिनेछ, र अनुरोध पूरा गर्न सकिन्छ कि सकिँदैन भन्ने जानकारी दिइनेछ। यो सामान्यतया केही मिनेटभित्र हुन्छ।

यदि तपाईंको अनुरोध पूरा गरिँदैन भने, तपाईंलाई समर्थन अनुरोध सिर्जना गर्न लिङ्क देखिनेछ। जब तपाईं यो लिङ्क प्रयोग गर्नुहुन्छ, एक समर्थन ईन्जिनियरले तपाईंलाई वृद्धि अनुरोधको साथ मद्दत गर्नेछन्।

## Azure Compute GPU मेसिन SKU सिफारिसहरू

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

यहाँ केही उदाहरणहरू छन्:

### यदि तपाईं सँग A100 वा H100 GPUs छन्

पूर्ण फाइनट्यूनिङले सामान्यतया उत्कृष्ट प्रदर्शन दिन्छ। तपाईं तलको कमाण्ड प्रयोग गरेर Phi-3-V लाई hateful memes classification मा फाइनट्यून गर्न सक्नुहुन्छ।

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### यदि तपाईं सँग Standard_ND40rs_v2 8x V100-32GB GPUs छन्

तपाईं अझै पनि Phi-3-V लाई hateful memes classification मा पूर्ण रूपमा फाइनट्यून गर्न सक्नुहुन्छ। तर, flash attention समर्थनको अभावका कारण throughput निकै कम हुने अपेक्षा गर्नुहोस्। bf16 समर्थनको अभावले (fp16 mixed-precision training प्रयोग गरिन्छ) accuracy पनि प्रभावित हुन सक्छ।

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### यदि तपाईं सँग डेटा सेन्टर GPUs पहुँच छैन भने

Lora तपाईंको एक मात्र विकल्प हुन सक्छ। तपाईं तलको कमाण्ड प्रयोग गरेर Phi-3-V लाई hateful memes classification मा फाइनट्यून गर्न सक्नुहुन्छ।

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU को लागि, QLoRA समर्थन गरिएको छ।

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## सिफारिस गरिएका हाइपरप्यारामिटरहरू र अपेक्षित सटीकता
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

Training method | Frozen vision model | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA results comming soon |  |  |  |  |  |  |  |  |

### NOTE
तलका DocVQA र Hateful memes नतिजाहरू पहिलेको संस्करण (Phi-3-vision) मा आधारित छन्। Phi-3.5-vision सँग नयाँ नतिजाहरू छिट्टै अपडेट गरिनेछ।

### DocVQA (NOTE: Phi-3-vision)

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

Training method | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (NOTE: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Training method | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## गति बेंचमार्किङ (NOTE: Phi-3-vision)

Phi-3.5-vision सँग नयाँ बेंचमार्किङ नतिजाहरू छिट्टै अपडेट गरिनेछ।

गति बेंचमार्किङ DocVQA डेटासेटमा गरिएको छ। यस डेटासेटको औसत अनुक्रम लम्बाइ 2443.23 टोकन छ (`num_crops=16` प्रयोग गरी छवि मोडलका लागि)।

### 8x A100-80GB (Ampere)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
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

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## ज्ञात समस्या

- fp16 सँग flash attention चलाउन सकिँदैन (bf16 सधैं सिफारिस गरिन्छ, र flash attention समर्थन गर्ने सबै GPUs ले bf16 पनि समर्थन गर्छन्)।
- हालसम्म इन्टरमिडियट चेकप्वाइन्टहरू बचत गर्न र तालिम पुनः सुरु गर्न समर्थन छैन।

**अस्वीकरण**:  
यो दस्तावेज़ मेशिन-आधारित एआई अनुवाद सेवाहरू प्रयोग गरेर अनुवाद गरिएको छ। हामी यथासम्भव शुद्धता सुनिश्चित गर्न प्रयास गर्छौं, तर कृपया सचेत रहनुहोस् कि स्वचालित अनुवादहरूले त्रुटिहरू वा अशुद्धताहरू समावेश गर्न सक्छ। यसको मूल भाषामा रहेको मूल दस्तावेजलाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवादको सिफारिस गरिन्छ। यो अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।