# **การปรับแต่ง Phi-3 ด้วย LoRA**

การปรับแต่งโมเดลภาษา Phi-3 Mini ของ Microsoft โดยใช้ [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) กับชุดข้อมูลคำสั่งสนทนาที่กำหนดเอง

LoRA จะช่วยเพิ่มความเข้าใจในการสนทนาและการสร้างคำตอบที่ดีขึ้น

## ขั้นตอนการปรับแต่ง Phi-3 Mini:

**การนำเข้าและการตั้งค่า**

ติดตั้ง loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

เริ่มต้นด้วยการนำเข้าไลบรารีที่จำเป็น เช่น datasets, transformers, peft, trl และ torch  
ตั้งค่าการบันทึกข้อมูลเพื่อติดตามกระบวนการฝึกโมเดล

คุณสามารถเลือกปรับแต่งบางเลเยอร์ได้โดยการแทนที่ด้วยเลเยอร์ที่ถูกนำมาใช้ใน loralib  
ปัจจุบันรองรับเฉพาะ nn.Linear, nn.Embedding และ nn.Conv2d  
นอกจากนี้ยังรองรับ MergedLinear สำหรับกรณีที่ nn.Linear หนึ่งตัวแทนมากกว่าหนึ่งเลเยอร์ เช่น ในการคำนวณ qkv projection ของ attention (ดูหมายเหตุเพิ่มเติมด้านล่าง)

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

ก่อนเริ่มการฝึก ให้ตั้งค่าให้เฉพาะพารามิเตอร์ของ LoRA เป็น trainable เท่านั้น

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

เมื่อบันทึก checkpoint ให้สร้าง state_dict ที่มีเฉพาะพารามิเตอร์ของ LoRA

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

เมื่อโหลด checkpoint โดยใช้ load_state_dict อย่าลืมตั้งค่า strict=False

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

จากนั้นสามารถเริ่มการฝึกโมเดลได้ตามปกติ

**ไฮเปอร์พารามิเตอร์**

กำหนดพจนานุกรมสองตัว: training_config และ peft_config  
training_config รวมถึงไฮเปอร์พารามิเตอร์สำหรับการฝึก เช่น อัตราการเรียนรู้ ขนาด batch และการตั้งค่าการบันทึก

peft_config ระบุพารามิเตอร์ที่เกี่ยวข้องกับ LoRA เช่น rank, dropout และ task type

**การโหลดโมเดลและ Tokenizer**

ระบุเส้นทางไปยังโมเดล Phi-3 ที่ถูกฝึกมาก่อน (เช่น "microsoft/Phi-3-mini-4k-instruct")  
ตั้งค่าการกำหนดค่าของโมเดล เช่น การใช้ cache, ประเภทข้อมูล (bfloat16 สำหรับ precision แบบผสม) และการใช้งาน attention

**การฝึก**

ปรับแต่งโมเดล Phi-3 โดยใช้ชุดข้อมูลคำสั่งสนทนาที่กำหนดเอง  
ใช้การตั้งค่า LoRA จาก peft_config เพื่อการปรับแต่งที่มีประสิทธิภาพ  
ติดตามความคืบหน้าของการฝึกโดยใช้กลยุทธ์การบันทึกที่กำหนดไว้

**การประเมินผลและการบันทึก**  
ประเมินโมเดลที่ถูกปรับแต่งแล้ว  
บันทึก checkpoint ระหว่างการฝึกเพื่อนำไปใช้ในอนาคต

**ตัวอย่าง**
- [เรียนรู้เพิ่มเติมด้วยโน้ตบุ๊กตัวอย่างนี้](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [ตัวอย่างการปรับแต่งด้วย Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [ตัวอย่างการปรับแต่งบน Hugging Face Hub ด้วย LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [ตัวอย่าง Model Card ของ Hugging Face - การปรับแต่ง LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [ตัวอย่างการปรับแต่งบน Hugging Face Hub ด้วย QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติด้วย AI แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นฉบับควรถูกพิจารณาว่าเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่อาจเกิดขึ้นจากการใช้การแปลนี้