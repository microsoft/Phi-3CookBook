# การใช้ Windows GPU เพื่อสร้างโซลูชัน Prompt flow ด้วย Phi-3.5-Instruct ONNX

เอกสารนี้เป็นตัวอย่างวิธีการใช้ PromptFlow ร่วมกับ ONNX (Open Neural Network Exchange) ในการพัฒนาแอปพลิเคชัน AI ที่ใช้โมเดล Phi-3

PromptFlow เป็นชุดเครื่องมือสำหรับการพัฒนา ที่ออกแบบมาเพื่อช่วยลดความซับซ้อนในกระบวนการพัฒนาแอปพลิเคชัน AI ที่ใช้ LLM (Large Language Model) ตั้งแต่การสร้างไอเดีย การสร้างต้นแบบ ไปจนถึงการทดสอบและประเมินผล

การผสาน PromptFlow กับ ONNX จะช่วยให้ผู้พัฒนาสามารถ:

- **เพิ่มประสิทธิภาพของโมเดล**: ใช้ ONNX เพื่อการอนุมานและการปรับใช้โมเดลที่มีประสิทธิภาพสูง
- **ลดความซับซ้อนในการพัฒนา**: ใช้ PromptFlow ในการจัดการเวิร์กโฟลว์และลดงานที่ทำซ้ำ
- **เสริมสร้างการทำงานร่วมกัน**: สนับสนุนการทำงานร่วมกันในทีมด้วยสภาพแวดล้อมการพัฒนาที่เป็นเอกภาพ

**Prompt flow** เป็นชุดเครื่องมือพัฒนาที่ออกแบบมาเพื่อช่วยลดความซับซ้อนในกระบวนการพัฒนาแอปพลิเคชัน AI ที่ใช้ LLM ตั้งแต่การสร้างไอเดีย การสร้างต้นแบบ การทดสอบ การประเมินผล ไปจนถึงการปรับใช้ในระดับโปรดักชันและการติดตามผล มันช่วยให้งานการออกแบบ Prompt ง่ายขึ้น และช่วยให้คุณสร้างแอป LLM ที่มีคุณภาพระดับโปรดักชันได้

Prompt flow สามารถเชื่อมต่อกับ OpenAI, Azure OpenAI Service และโมเดลที่ปรับแต่งได้ (เช่น Huggingface, LLM/SLM ที่ใช้งานในเครื่อง) เราหวังที่จะปรับใช้โมเดล Phi-3.5 แบบ ONNX ที่ผ่านการปรับขนาดแล้วในแอปพลิเคชันในเครื่อง Prompt flow จะช่วยให้เราวางแผนธุรกิจได้ดีขึ้น และสร้างโซลูชันในเครื่องโดยใช้ Phi-3.5 ได้สมบูรณ์ ในตัวอย่างนี้ เราจะผสาน ONNX Runtime GenAI Library เพื่อสร้างโซลูชัน Prompt flow โดยใช้ Windows GPU

## **การติดตั้ง**

### **ONNX Runtime GenAI สำหรับ Windows GPU**

อ่านคำแนะนำการตั้งค่า ONNX Runtime GenAI สำหรับ Windows GPU [คลิกที่นี่](./ORTWindowGPUGuideline.md)

### **ตั้งค่า Prompt flow ใน VSCode**

1. ติดตั้ง Prompt flow VS Code Extension

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.th.png)

2. หลังจากติดตั้ง Prompt flow VS Code Extension แล้ว ให้คลิกที่ส่วนขยาย และเลือก **Installation dependencies** จากนั้นทำตามคำแนะนำเพื่อติดตั้ง Prompt flow SDK ในสภาพแวดล้อมของคุณ

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.th.png)

3. ดาวน์โหลด [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) และเปิดตัวอย่างนี้ใน VS Code

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.th.png)

4. เปิดไฟล์ **flow.dag.yaml** เพื่อเลือก Python env ของคุณ

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.th.png)

   เปิดไฟล์ **chat_phi3_ort.py** เพื่อเปลี่ยนตำแหน่งโมเดล Phi-3.5-instruct ONNX ของคุณ

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.th.png)

5. รัน Prompt flow เพื่อทดสอบ

เปิดไฟล์ **flow.dag.yaml** และคลิกที่ visual editor

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.th.png)

หลังจากคลิกแล้ว ให้รันเพื่อทดสอบ

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.th.png)

1. คุณสามารถรัน batch ใน terminal เพื่อดูผลลัพธ์เพิ่มเติม


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

คุณสามารถตรวจสอบผลลัพธ์ในเบราว์เซอร์เริ่มต้นของคุณ


![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.th.png)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI อัตโนมัติ แม้ว่าเราจะพยายามอย่างเต็มที่เพื่อให้ได้ความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้องเกิดขึ้น เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ ขอแนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่คลาดเคลื่อนอันเกิดจากการใช้การแปลนี้