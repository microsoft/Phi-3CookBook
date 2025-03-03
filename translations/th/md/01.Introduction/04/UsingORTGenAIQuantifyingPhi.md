# **การควอนไทซ์ตระกูล Phi ด้วย Generative AI extensions สำหรับ onnxruntime**

## **Generative AI extensions สำหรับ onnxruntime คืออะไร**

ส่วนขยายนี้ช่วยให้คุณสามารถใช้งาน Generative AI กับ ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) ได้ โดยมีการจัดการวงจร Generative AI สำหรับโมเดล ONNX เช่น การทำ inference กับ ONNX Runtime, การประมวลผล logits, การค้นหาและการสุ่มตัวอย่าง, รวมถึงการจัดการ KV cache นักพัฒนาสามารถเรียกใช้เมธอด generate() ระดับสูง หรือดำเนินการวนซ้ำในแต่ละรอบของโมเดลเพื่อสร้างโทเค็นทีละตัว และสามารถปรับพารามิเตอร์การสร้างได้ตามต้องการในระหว่างการวนซ้ำ รองรับการค้นหาแบบ greedy/beam และการสุ่มตัวอย่างแบบ TopP, TopK เพื่อสร้างลำดับโทเค็น รวมถึงมีการประมวลผล logits ในตัว เช่น การลงโทษการทำซ้ำ และยังสามารถเพิ่มคะแนนแบบกำหนดเองได้ง่าย ๆ

ในระดับแอปพลิเคชัน คุณสามารถใช้ Generative AI extensions สำหรับ onnxruntime เพื่อสร้างแอปพลิเคชันโดยใช้ C++/C#/Python ในระดับโมเดล คุณสามารถใช้เพื่อรวมโมเดลที่ได้รับการปรับแต่ง (fine-tuned) และดำเนินการปรับใช้เชิงปริมาณที่เกี่ยวข้องได้


## **การควอนไทซ์ Phi-3.5 ด้วย Generative AI extensions สำหรับ onnxruntime**

### **โมเดลที่รองรับ**

Generative AI extensions สำหรับ onnxruntime รองรับการแปลงควอนไทซ์ของ Microsoft Phi, Google Gemma, Mistral, และ Meta LLaMA


### **Model Builder ใน Generative AI extensions สำหรับ onnxruntime**

Model Builder ช่วยเร่งกระบวนการสร้างโมเดล ONNX ที่ได้รับการปรับแต่งและควอนไทซ์เพื่อใช้งานกับ API generate() ของ ONNX Runtime

ด้วย Model Builder คุณสามารถควอนไทซ์โมเดลเป็น INT4, INT8, FP16, FP32 และรวมวิธีการเร่งฮาร์ดแวร์ที่แตกต่างกัน เช่น CPU, CUDA, DirectML, Mobile เป็นต้น

ในการใช้งาน Model Builder คุณจำเป็นต้องติดตั้ง

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

หลังจากติดตั้งแล้ว คุณสามารถรันสคริปต์ Model Builder จากเทอร์มินัลเพื่อแปลงรูปแบบและควอนไทซ์โมเดล


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

ทำความเข้าใจกับพารามิเตอร์ที่เกี่ยวข้อง

1. **model_name** ชื่อโมเดลใน Hugging Face เช่น microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct เป็นต้น หรือสามารถเป็นเส้นทางที่คุณเก็บโมเดลไว้ได้

2. **path_to_output_folder** เส้นทางที่บันทึกผลลัพธ์การแปลงควอนไทซ์

3. **execution_provider** การรองรับการเร่งฮาร์ดแวร์ที่แตกต่างกัน เช่น cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** เราดาวน์โหลดโมเดลจาก Hugging Face และแคชไว้ในเครื่อง


***หมายเหตุ:*** 

## **วิธีการใช้ Model Builder เพื่อควอนไทซ์ Phi-3.5**

Model Builder ตอนนี้รองรับการควอนไทซ์โมเดล ONNX สำหรับ Phi-3.5 Instruct และ Phi-3.5-Vision

### **Phi-3.5-Instruct**

**การแปลงควอนไทซ์ INT4 ด้วยการเร่งโดย CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**การแปลงควอนไทซ์ INT4 ด้วยการเร่งโดย CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. ตั้งค่าสภาพแวดล้อมในเทอร์มินัล

```bash

mkdir models

cd models 

```

2. ดาวน์โหลด microsoft/Phi-3.5-vision-instruct ในโฟลเดอร์ models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. โปรดดาวน์โหลดไฟล์เหล่านี้ไปยังโฟลเดอร์ Phi-3.5-vision-instruct ของคุณ  

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. ดาวน์โหลดไฟล์นี้ไปยังโฟลเดอร์ models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ไปที่เทอร์มินัล  

   แปลงให้รองรับ ONNX ด้วย FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **หมายเหตุ:**

1. Model Builder ปัจจุบันรองรับการแปลง Phi-3.5-Instruct และ Phi-3.5-Vision แต่ยังไม่รองรับ Phi-3.5-MoE

2. ในการใช้งานโมเดลควอนไทซ์ของ ONNX คุณสามารถใช้งานได้ผ่าน Generative AI extensions สำหรับ onnxruntime SDK

3. เราจำเป็นต้องพิจารณา AI ที่มีความรับผิดชอบมากขึ้น ดังนั้นหลังจากการแปลงควอนไทซ์ของโมเดล ขอแนะนำให้ทำการทดสอบผลลัพธ์อย่างมีประสิทธิภาพมากขึ้น

4. โดยการควอนไทซ์โมเดล CPU INT4 เราสามารถนำไปใช้ใน Edge Device ได้ ซึ่งมีสถานการณ์การใช้งานที่ดีกว่า ดังนั้นเราจึงได้ดำเนินการ Phi-3.5-Instruct ในรูปแบบ INT4


## **แหล่งข้อมูล**

1. เรียนรู้เพิ่มเติมเกี่ยวกับ Generative AI extensions สำหรับ onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. GitHub Repo ของ Generative AI extensions สำหรับ onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติที่ขับเคลื่อนด้วย AI แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยระบบอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นฉบับควรถูกพิจารณาว่าเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์มืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้