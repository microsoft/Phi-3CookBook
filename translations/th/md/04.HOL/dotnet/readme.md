## ยินดีต้อนรับสู่ Phi labs ด้วย C#

ในห้องทดลองนี้มีตัวอย่างที่แสดงวิธีการรวม Phi models เวอร์ชันต่างๆ ที่ทรงพลังเข้ากับสภาพแวดล้อม .NET

## ข้อกำหนดเบื้องต้น

ก่อนที่จะรันตัวอย่างโปรแกรม ให้ตรวจสอบว่าคุณได้ติดตั้งสิ่งต่อไปนี้แล้ว:

**.NET 9:** ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้ง [เวอร์ชันล่าสุดของ .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) บนเครื่องของคุณ

**(ตัวเลือก) Visual Studio หรือ Visual Studio Code:** คุณจะต้องมี IDE หรือโปรแกรมแก้ไขโค้ดที่สามารถรันโปรเจ็กต์ .NET ได้ แนะนำให้ใช้ [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) หรือ [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo)

**ใช้ git** โคลน Phi-3, Phi-3.5 หรือ Phi-4 เวอร์ชันที่มีอยู่จาก [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) มายังเครื่องของคุณ

**ดาวน์โหลด Phi-4 ONNX models** มายังเครื่องของคุณ:

### ไปยังโฟลเดอร์ที่จะเก็บโมเดล

```bash
cd c:\phi\models
```

### เพิ่มการสนับสนุนสำหรับ lfs

```bash
git lfs install 
```

### โคลนและดาวน์โหลด Phi-4 mini instruct model และ Phi-4 multi modal model

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**ดาวน์โหลด Phi-3 ONNX models** มายังเครื่องของคุณ:

### โคลนและดาวน์โหลด Phi-3 mini 4K instruct model และ Phi-3 vision 128K model

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**สำคัญ:** เดโมปัจจุบันถูกออกแบบให้ใช้เวอร์ชัน ONNX ของโมเดล ขั้นตอนก่อนหน้านี้จะโคลนโมเดลดังต่อไปนี้

## เกี่ยวกับห้องทดลอง

โซลูชันหลักมีตัวอย่างห้องทดลองหลายโปรเจ็กต์ที่แสดงความสามารถของ Phi models ด้วยการใช้ C#

| โปรเจ็กต์ | โมเดล | คำอธิบาย |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 หรือ Phi-3.5 | ตัวอย่างคอนโซลแชทที่ให้ผู้ใช้สามารถถามคำถามได้ โปรเจ็กต์นี้โหลด ONNX Phi-3 model จากเครื่องท้องถิ่นโดยใช้ `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. รันโปรเจ็กต์ด้วยคำสั่ง

    ```bash
    dotnet run
    ```

1. โปรเจ็กต์ตัวอย่างจะขอให้ผู้ใช้ป้อนข้อมูลและตอบกลับโดยใช้โหมดท้องถิ่น

   เดโมที่รันจะมีลักษณะคล้ายกับตัวอย่างนี้:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติด้วย AI แม้ว่าเราจะพยายามอย่างเต็มที่เพื่อความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นฉบับควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญที่เป็นมนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้