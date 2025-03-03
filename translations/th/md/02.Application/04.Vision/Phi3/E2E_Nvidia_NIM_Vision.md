### ตัวอย่างสถานการณ์

ลองจินตนาการว่าคุณมีภาพหนึ่งภาพ (`demo.png`) และคุณต้องการสร้างโค้ด Python ที่ประมวลผลภาพนี้และบันทึกเวอร์ชันใหม่ของมัน (`phi-3-vision.jpg`)

โค้ดด้านบนช่วยทำให้กระบวนการนี้เป็นอัตโนมัติโดย:

1. ตั้งค่าสภาพแวดล้อมและการตั้งค่าที่จำเป็น
2. สร้างข้อความแจ้งที่สั่งให้โมเดลสร้างโค้ด Python ที่ต้องการ
3. ส่งข้อความแจ้งไปยังโมเดลและรับโค้ดที่สร้างขึ้น
4. ดึงและรันโค้ดที่สร้างขึ้น
5. แสดงภาพต้นฉบับและภาพที่ผ่านการประมวลผล

วิธีนี้ใช้ประโยชน์จากพลังของ AI เพื่อทำให้งานประมวลผลภาพง่ายขึ้นและรวดเร็วขึ้น

[ตัวอย่างโค้ด](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

มาดูรายละเอียดของสิ่งที่โค้ดทั้งหมดทำทีละขั้นตอน:

1. **ติดตั้งแพ็กเกจที่จำเป็น**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    คำสั่งนี้ติดตั้งแพ็กเกจ `langchain_nvidia_ai_endpoints` โดยให้แน่ใจว่าเป็นเวอร์ชันล่าสุด

2. **นำเข้ามอดูลที่จำเป็น**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    การนำเข้านี้ช่วยดึงมอดูลที่จำเป็นสำหรับการทำงานร่วมกับ NVIDIA AI endpoints, การจัดการรหัสผ่านอย่างปลอดภัย, การทำงานกับระบบปฏิบัติการ, และการเข้ารหัส/ถอดรหัสข้อมูลในรูปแบบ base64

3. **ตั้งค่า API Key**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    โค้ดนี้ตรวจสอบว่าได้ตั้งค่าตัวแปรสภาพแวดล้อม `NVIDIA_API_KEY` หรือไม่ ถ้ายังไม่ได้ตั้งค่า ระบบจะขอให้ผู้ใช้ป้อน API key อย่างปลอดภัย

4. **กำหนดโมเดลและเส้นทางของไฟล์ภาพ**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    กำหนดโมเดลที่ต้องการใช้งาน สร้างอินสแตนซ์ของ `ChatNVIDIA` ด้วยโมเดลที่กำหนด และกำหนดเส้นทางของไฟล์ภาพ

5. **สร้างข้อความแจ้ง (Prompt)**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    ข้อความนี้เป็นคำสั่งที่ให้โมเดลสร้างโค้ด Python สำหรับประมวลผลภาพ

6. **เข้ารหัสภาพในรูปแบบ Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    โค้ดนี้อ่านไฟล์ภาพ เข้ารหัสในรูปแบบ base64 และสร้างแท็ก HTML ของภาพด้วยข้อมูลที่เข้ารหัส

7. **รวมข้อความและภาพเข้าด้วยกันใน Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    รวมข้อความแจ้งและแท็ก HTML ของภาพเข้าเป็นสตริงเดียว

8. **สร้างโค้ดโดยใช้ ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    โค้ดนี้ส่งข้อความแจ้งไปยัง `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` สตริง

9. **ดึงโค้ด Python จากเนื้อหาที่สร้างขึ้น**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    โค้ดนี้ดึงโค้ด Python จริงจากเนื้อหาที่สร้างขึ้นโดยลบการจัดรูปแบบ markdown ออก

10. **รันโค้ดที่สร้างขึ้น**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    โค้ดนี้รันโค้ด Python ที่ดึงมาเป็น subprocess และเก็บผลลัพธ์ที่ได้

11. **แสดงภาพ**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    บรรทัดเหล่านี้ใช้โมดูล `IPython.display` เพื่อแสดงภาพ

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติด้วย AI แม้ว่าเราจะพยายามอย่างเต็มที่เพื่อความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์โดยมืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดอันเกิดจากการใช้การแปลนี้