# **การใช้งาน Phi-3 บน Android**

มาดูกันว่าคุณสามารถทำการใช้งาน Phi-3-mini บนอุปกรณ์ Android ได้อย่างไร Phi-3-mini เป็นชุดโมเดลใหม่จาก Microsoft ที่ช่วยให้สามารถใช้งานโมเดลภาษาใหญ่ (LLMs) บนอุปกรณ์ edge และ IoT ได้

## Semantic Kernel และการใช้งานโมเดล

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) เป็นเฟรมเวิร์กสำหรับสร้างแอปพลิเคชันที่รองรับ Azure OpenAI Service, โมเดลของ OpenAI และโมเดลที่ทำงานในเครื่อง หากคุณยังใหม่กับ Semantic Kernel เราแนะนำให้คุณดู [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)

### การเข้าถึง Phi-3-mini ด้วย Semantic Kernel

คุณสามารถใช้งานร่วมกับ Hugging Face Connector ใน Semantic Kernel ดูตัวอย่างได้ที่ [ตัวอย่างโค้ด](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)

โดยค่าเริ่มต้น จะสอดคล้องกับ ID ของโมเดลใน Hugging Face แต่คุณยังสามารถเชื่อมต่อกับเซิร์ฟเวอร์ Phi-3-mini ที่สร้างขึ้นในเครื่องได้เช่นกัน

### การเรียกใช้โมเดลที่ถูกปรับขนาดด้วย Ollama หรือ LlamaEdge

ผู้ใช้จำนวนมากนิยมใช้โมเดลที่ถูกปรับขนาด (quantized models) เพื่อให้สามารถรันโมเดลในเครื่องได้ [Ollama](https://ollama.com/) และ [LlamaEdge](https://llamaedge.com) ช่วยให้ผู้ใช้สามารถเรียกใช้โมเดลที่ถูกปรับขนาดได้หลากหลาย:

#### Ollama

คุณสามารถรัน `ollama run Phi-3` ได้โดยตรง หรือกำหนดค่าแบบออฟไลน์โดยสร้าง `Modelfile` ที่มีเส้นทางไปยังไฟล์ `.gguf` ของคุณ

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[ตัวอย่างโค้ด](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

หากคุณต้องการใช้ไฟล์ `.gguf` ทั้งในระบบคลาวด์และบนอุปกรณ์ edge พร้อมกัน LlamaEdge เป็นตัวเลือกที่ดี คุณสามารถดู [ตัวอย่างโค้ด](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) เพื่อเริ่มต้น

### การติดตั้งและใช้งานบนโทรศัพท์ Android

1. **ดาวน์โหลดแอป MLC Chat** (ฟรี) สำหรับโทรศัพท์ Android
2. ดาวน์โหลดไฟล์ APK (148MB) และติดตั้งลงในอุปกรณ์ของคุณ
3. เปิดแอป MLC Chat คุณจะเห็นรายการของโมเดล AI รวมถึง Phi-3-mini

สรุปได้ว่า Phi-3-mini ช่วยเปิดโอกาสที่น่าตื่นเต้นสำหรับ AI เชิงสร้างสรรค์บนอุปกรณ์ edge และคุณสามารถเริ่มสำรวจความสามารถของมันบน Android ได้แล้ว

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติด้วย AI แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นฉบับควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่คลาดเคลื่อนซึ่งเกิดจากการใช้การแปลนี้