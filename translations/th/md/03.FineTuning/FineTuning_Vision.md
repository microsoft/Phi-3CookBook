# สูตรการปรับแต่ง Phi-3.5-vision

นี่คือการสนับสนุนอย่างเป็นทางการสำหรับการปรับแต่ง Phi-3.5-vision โดยใช้ไลบรารีของ huggingface  
โปรด `cd` ไปยังไดเรกทอรีโค้ด [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) ก่อนรันคำสั่งต่อไปนี้

## การติดตั้ง

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

## เริ่มต้นอย่างรวดเร็ว

เรามีสคริปต์ตัวอย่างสำหรับการปรับแต่งสองแบบ ได้แก่ DocVQA และการจัดประเภทมีมที่แสดงความเกลียดชัง  

ฮาร์ดแวร์ขั้นต่ำที่ผ่านการทดสอบ: 4x RTX8000 (RAM 48GB ต่อ GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ตอนนี้รองรับการป้อนข้อมูลหลายภาพอย่างเป็นทางการ ตัวอย่างสำหรับการปรับแต่ง NLVR2 มีดังนี้

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## คู่มือการใช้งาน

ขึ้นอยู่กับฮาร์ดแวร์ ผู้ใช้อาจเลือกกลยุทธ์การปรับแต่งที่แตกต่างกัน เรารองรับการปรับแต่งแบบเต็ม (ด้วย Deepspeed Zero-2) พร้อมตัวเลือกการแช่แข็งพารามิเตอร์วิชัน และ LoRA (รวมถึง 4bit QLoRA)  
โดยทั่วไป แนะนำให้ใช้การปรับแต่งแบบเต็มพร้อม flash attention และ bf16 หากเป็นไปได้

### คู่มือการแปลงชุดข้อมูลของคุณให้เป็นรูปแบบที่ต้องการ

เราใช้ชุดข้อมูลการจัดประเภทวิดีโอขั้นต่ำ (ส่วนย่อยของ UCF-101) เป็นตัวอย่างแบบ end-to-end เพื่อแสดงวิธีแปลงชุดข้อมูลของคุณให้เป็นรูปแบบที่ต้องการและปรับแต่ง Phi-3.5-vision บนชุดข้อมูลนั้น

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

ข้อมูลที่แปลงแล้วจะมีลักษณะดังนี้:

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

สำหรับการกำหนดคำอธิบายแบบ `jsonl` แต่ละบรรทัดควรเป็นพจนานุกรมลักษณะนี้:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

โปรดทราบว่า `conversations` เป็นรายการ ดังนั้นจึงรองรับการสนทนาแบบหลายเทิร์นหากมีข้อมูลดังกล่าว

## การขอเพิ่มโควต้า GPU บน Azure

### ข้อกำหนดเบื้องต้น

บัญชี Azure ที่มีบทบาท Contributor (หรือบทบาทอื่นที่มีสิทธิ์ Contributor)

หากคุณยังไม่มีบัญชี Azure ให้สร้าง [บัญชีฟรีก่อนเริ่มต้น](https://azure.microsoft.com)

### การขอเพิ่มโควต้า

คุณสามารถส่งคำขอเพิ่มโควต้าได้โดยตรงจาก My quotas ทำตามขั้นตอนด้านล่างเพื่อขอเพิ่มโควต้า สำหรับตัวอย่างนี้ คุณสามารถเลือกโควต้าที่ปรับได้ในบัญชีสมัครสมาชิกของคุณ

เข้าสู่ระบบที่ [Azure portal](https://portal.azure.com)

พิมพ์ "quotas" ในช่องค้นหา จากนั้นเลือก Quotas  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

ในหน้า Overview เลือกผู้ให้บริการ เช่น Compute หรือ AML  

**หมายเหตุ** สำหรับผู้ให้บริการทั้งหมดนอกเหนือจาก Compute คุณจะเห็นคอลัมน์ Request increase แทนคอลัมน์ Adjustable ที่อธิบายด้านล่าง คุณสามารถขอเพิ่มสำหรับโควต้าเฉพาะ หรือสร้างคำขอสนับสนุนสำหรับการเพิ่มโควต้า

ในหน้า My quotas ภายใต้ Quota name เลือกโควต้าที่คุณต้องการเพิ่ม ตรวจสอบให้แน่ใจว่าคอลัมน์ Adjustable แสดงว่า Yes สำหรับโควต้านั้น  

ใกล้ด้านบนของหน้า ให้เลือก New Quota Request จากนั้นเลือก Enter a new limit  

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

ในหน้าต่าง New Quota Request ให้ป้อนค่าตัวเลขสำหรับโควต้าใหม่ของคุณ จากนั้นเลือก Submit  

คำขอของคุณจะได้รับการตรวจสอบ และคุณจะได้รับการแจ้งเตือนหากคำขอสามารถดำเนินการได้ โดยปกติจะใช้เวลาเพียงไม่กี่นาที  

หากคำขอของคุณไม่ได้รับการอนุมัติ คุณจะเห็นลิงก์เพื่อสร้างคำขอสนับสนุน เมื่อคุณใช้ลิงก์นี้ วิศวกรสนับสนุนจะช่วยเหลือคุณในคำขอเพิ่มโควต้า

## คำแนะนำ SKU เครื่อง GPU บน Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

ตัวอย่างมีดังนี้:

### หากคุณมี A100 หรือ H100 GPUs

การปรับแต่งแบบเต็มมักให้ประสิทธิภาพดีที่สุด คุณสามารถใช้คำสั่งต่อไปนี้เพื่อปรับแต่ง Phi-3-V สำหรับการจัดประเภทมีมที่แสดงความเกลียดชัง

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### หากคุณมี Standard_ND40rs_v2 8x V100-32GB GPUs

ยังสามารถปรับแต่ง Phi-3-V สำหรับการจัดประเภทมีมที่แสดงความเกลียดชังได้ อย่างไรก็ตาม คาดว่าจะมีอัตราการประมวลผลต่ำกว่า A100 หรือ H100 GPUs อย่างมากเนื่องจากไม่มีการสนับสนุน flash attention  
ความแม่นยำอาจได้รับผลกระทบเนื่องจากไม่มีการสนับสนุน bf16 (ใช้การฝึกอบรมแบบ fp16 mixed-precision แทน)

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### หากคุณไม่มี GPU ระดับดาต้าเซ็นเตอร์

LoRA อาจเป็นตัวเลือกเดียวของคุณ คุณสามารถใช้คำสั่งต่อไปนี้เพื่อปรับแต่ง Phi-3-V สำหรับการจัดประเภทมีมที่แสดงความเกลียดชัง

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

สำหรับ Turing+ GPU รองรับ QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## ค่าพารามิเตอร์ที่แนะนำและความแม่นยำที่คาดหวัง
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

วิธีการฝึกอบรม | แช่แข็งโมเดลวิชัน | ประเภทข้อมูล | LoRA rank | LoRA alpha | batch size | learning rate | epochs | ความแม่นยำ
--- | --- | --- | --- | --- | --- | --- | --- | --- |
การปรับแต่งแบบเต็ม |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
การปรับแต่งแบบเต็ม | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
ผลลัพธ์ LoRA กำลังมา |  |  |  |  |  |  |  |  |

### หมายเหตุ
ผลลัพธ์ DocVQA และ Hateful memes ด้านล่างนี้อิงตามเวอร์ชันก่อนหน้า (Phi-3-vision)  
ผลลัพธ์ใหม่ด้วย Phi-3.5-vision จะได้รับการอัปเดตเร็ว ๆ นี้

### DocVQA (หมายเหตุ: Phi-3-vision)

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

วิธีการฝึกอบรม | ประเภทข้อมูล | LoRA rank | LoRA alpha | batch size | learning rate | epochs | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
การปรับแต่งแบบเต็ม | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
การปรับแต่งแบบเต็ม | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
โมเดลภาพแช่แข็ง | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
โมเดลภาพแช่แข็ง | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (หมายเหตุ: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

วิธีการฝึกอบรม | ประเภทข้อมูล | LoRA rank | LoRA alpha | batch size | learning rate | epochs | ความแม่นยำ
--- | --- | --- | --- | --- | --- | --- | --- |
การปรับแต่งแบบเต็ม | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
การปรับแต่งแบบเต็ม | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
โมเดลภาพแช่แข็ง | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
โมเดลภาพแช่แข็ง | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## การวัดความเร็ว (หมายเหตุ: Phi-3-vision)

ผลลัพธ์การวัดความเร็วใหม่ด้วย Phi-3.5-vision จะได้รับการอัปเดตเร็ว ๆ นี้  

การวัดความเร็วทำบนชุดข้อมูล DocVQA ความยาวเฉลี่ยของลำดับในชุดข้อมูลนี้คือ 2443.23 โทเค็น (ใช้ `num_crops=16` สำหรับโมเดลภาพ)

### 8x A100-80GB (Ampere)

วิธีการฝึกอบรม | \# nodes | GPUs | flash attention | batch size ที่มีประสิทธิภาพ | Throughput (img/s) | Speedup | หน่วยความจำ GPU สูงสุด (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
การปรับแต่งแบบเต็ม | 1 | 8 |  | 64 | 5.041 |  1x | ~42
การปรับแต่งแบบเต็ม | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
การปรับแต่งแบบเต็ม | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
การปรับแต่งแบบเต็ม | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
โมเดลภาพแช่แข็ง | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
โมเดลภาพแช่แข็ง | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

วิธีการฝึกอบรม | \# nodes | GPUs | flash attention | batch size ที่มีประสิทธิภาพ | Throughput (img/s) | Speedup | หน่วยความจำ GPU สูงสุด (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
การปรับแต่งแบบเต็ม | 1 | 8 | | 64 | 2.462 |  1x | ~32
การปรับแต่งแบบเต็ม | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
การปรับแต่งแบบเต็ม | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
โมเดลภาพแช่แข็ง | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## ปัญหาที่ทราบ

- ไม่สามารถใช้ flash attention กับ fp16 ได้ (แนะนำให้ใช้ bf16 เสมอเมื่อสามารถทำได้ และ GPU ที่รองรับ flash attention ทั้งหมดก็รองรับ bf16 ด้วย)
- ยังไม่รองรับการบันทึกจุดตรวจสอบระหว่างทางและการกลับมาฝึกอบรมใหม่

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติด้วย AI แม้ว่าเราจะพยายามอย่างเต็มที่เพื่อให้เกิดความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้องเกิดขึ้นได้ เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ แนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญที่เป็นมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดพลาดใด ๆ ที่อาจเกิดขึ้นจากการใช้การแปลนี้