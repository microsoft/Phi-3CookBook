# Phi-3.5-vision फाइनट्यूनिंग रेसिपी

Phi-3.5-vision फाइनट्यूनिंगसाठी हगिंगफेस लायब्ररींच्या वापरासाठी अधिकृत मार्गदर्शक. खालील कमांड्स चालवण्यापूर्वी कृपया कोड डिरेक्टरी [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) येथे जा.

## इंस्टॉलेशन

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

## क्विक स्टार्ट

आम्ही दोन उदाहरण फाइनट्यूनिंग स्क्रिप्ट्स दिल्या आहेत, एक DocVQA साठी आणि दुसरी hateful meme वर्गीकरणासाठी.

किमान हार्डवेअर: 4x RTX8000 (प्रत्येक GPU साठी 48GB RAM)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision आता मल्टी-इमेज इनपुट्सला अधिकृतपणे सपोर्ट करते. NLVR2 साठी फाइनट्यूनिंगसाठी एक उदाहरण येथे दिले आहे.

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## वापर मार्गदर्शक

हार्डवेअरनुसार, वापरकर्ते विविध फाइनट्यूनिंग स्ट्रॅटेजी निवडू शकतात. आम्ही पूर्ण फाइनट्यूनिंग (Deepspeed Zero-2 सह) आणि LoRA (4bit QLoRA सहित) सपोर्ट करतो. शक्य असल्यास, फ्लॅश अटेंशन आणि bf16 सह पूर्ण फाइनट्यूनिंगचा वापर करण्याची शिफारस केली जाते.

### तुमच्या कस्टम डेटासेटला आवश्यक फॉरमॅटमध्ये कन्व्हर्ट करण्यासाठी मार्गदर्शक

किमान व्हिडिओ वर्गीकरण डेटासेट (UCF-101 चे उपसमुच्चय) एक एंड-टू-एंड उदाहरण म्हणून वापरले आहे, ज्याद्वारे तुमच्या कस्टम डेटासेटला आवश्यक फॉरमॅटमध्ये कन्व्हर्ट कसे करावे आणि Phi-3.5-vision वर फाइनट्यून कसे करावे हे दाखवले आहे.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

कन्व्हर्ट केलेले डेटा असे दिसेल:

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

`jsonl` अॅनोटेशनसाठी, प्रत्येक ओळ एका डिक्शनरीसारखी असावी:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

लक्षात घ्या की `conversations` ही यादी आहे, त्यामुळे मल्टी-टर्न संभाषण सपोर्ट केले जाऊ शकते जर अशा प्रकारचा डेटा उपलब्ध असेल.

## Azure GPU कोटा विनंती करणे

### पूर्वअटी

Contributor भूमिका (किंवा Contributor प्रवेश असलेली इतर भूमिका) असलेले Azure खाते.

जर तुमच्याकडे Azure खाते नसेल, तर [फ्री खाते तयार करा](https://azure.microsoft.com).

### कोटा वाढीसाठी विनंती करा

तुम्ही My quotas वरून थेट कोटा वाढीसाठी विनंती करू शकता. कोटा वाढीसाठी खालील स्टेप्स फॉलो करा. या उदाहरणासाठी, तुमच्या सबस्क्रिप्शनमधील कोणताही adjustable कोटा निवडू शकता.

[Azure पोर्टल](https://portal.azure.com) वर साइन इन करा.

शोध बॉक्समध्ये "quotas" टाका आणि Quotas निवडा.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

ओव्हरव्ह्यू पृष्ठावर, Compute किंवा AML सारखा प्रोव्हायडर निवडा.

**टीप:** Compute वगळता इतर सर्व प्रोव्हायडर्ससाठी, तुम्हाला Adjustable कॉलमऐवजी Request increase कॉलम दिसेल. येथे, तुम्ही विशिष्ट कोटासाठी वाढीची विनंती करू शकता किंवा वाढीसाठी सपोर्ट विनंती तयार करू शकता.

My quotas पृष्ठावर, Quota name अंतर्गत तुम्हाला वाढवायचा असलेला कोटा निवडा. सुनिश्चित करा की Adjustable कॉलममध्ये Yes दर्शविले आहे.

पृष्ठाच्या वरती, New Quota Request निवडा, आणि Enter a new limit निवडा.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request पॅनमध्ये, तुमच्या नवीन कोटा मर्यादेसाठी संख्यात्मक मूल्य प्रविष्ट करा आणि Submit निवडा.

तुमच्या विनंतीचे पुनरावलोकन केले जाईल, आणि ती पूर्ण होऊ शकते की नाही याची माहिती दिली जाईल. हे सहसा काही मिनिटांत होते.

जर तुमची विनंती पूर्ण झाली नाही, तर तुम्हाला सपोर्ट विनंती तयार करण्यासाठी लिंक दिसेल. या लिंकचा वापर केल्यावर, सपोर्ट इंजिनियर तुम्हाला तुमच्या वाढीच्या विनंतीसाठी मदत करेल.

## Azure Compute GPU मशीन SKU सूचना

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

उदाहरणे येथे दिली आहेत:

### जर तुमच्याकडे A100 किंवा H100 GPUs असतील

पूर्ण फाइनट्यूनिंग सामान्यतः सर्वोत्तम कार्यक्षमता देते. तुम्ही खालील कमांडचा वापर करून hateful memes वर्गीकरणासाठी Phi-3-V फाइनट्यून करू शकता.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### जर तुमच्याकडे Standard_ND40rs_v2 8x V100-32GB GPUs असतील

Phi-3-V ला पूर्ण फाइनट्यून करणे अजूनही शक्य आहे, परंतु फ्लॅश अटेंशन सपोर्टच्या अभावामुळे खूपच कमी थ्रूपुट अपेक्षित आहे. bf16 सपोर्टच्या अभावामुळे अचूकतेवरही परिणाम होऊ शकतो (fp16 मिश्र-प्रेसिजन प्रशिक्षण वापरले जाते).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### जर तुम्हाला डेटा सेंटर GPUs वर प्रवेश नसेल
Lora हा तुमच्यासाठी एकमेव पर्याय असू शकतो. तुम्ही खालील कमांड वापरून hateful memes वर्गीकरणासाठी Phi-3-V फाइनट्यून करू शकता.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU साठी, QLoRA सपोर्टेड आहे.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## सुचवलेले हायपरपॅरामिटर्स आणि अपेक्षित अचूकता
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

### टीप
खालील DocVQA आणि Hateful memes परिणाम Phi-3-vision च्या मागील आवृत्तीवर आधारित आहेत. Phi-3.5-vision सह नवीन परिणाम लवकरच अपडेट केले जातील.

### DocVQA (टीप: Phi-3-vision)

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

### Hateful memes (टीप: Phi-3-vision)

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

## स्पीड बेंचमार्किंग (टीप: Phi-3-vision)

Phi-3.5-vision सह नवीन बेंचमार्किंग परिणाम लवकरच अपडेट केले जातील.

स्पीड बेंचमार्किंग DocVQA डेटासेटवर केले गेले आहे. या डेटासेटची सरासरी सिक्वेन्स लांबी 2443.23 टोकन्स आहे (`num_crops=16` इमेज मॉडेलसाठी वापरले आहे).

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

- fp16 सह फ्लॅश अटेंशन चालवू शकत नाही (bf16 नेहमी शिफारस केले जाते, आणि फ्लॅश अटेंशनला सपोर्ट करणारे सर्व GPUs bf16 ला देखील सपोर्ट करतात).
- अद्याप इंटरमिजिएट चेकपॉइंट्स सेव्ह करणे आणि प्रशिक्षण पुन्हा सुरू करणे सपोर्ट केले जात नाही.

**अस्वीकरण**:  
हे दस्तऐवज मशीन-आधारित AI भाषांतर सेवांचा वापर करून अनुवादित केले गेले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज अधिकृत स्रोत मानावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे निर्माण होणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थ लावण्यास आम्ही जबाबदार राहणार नाही.