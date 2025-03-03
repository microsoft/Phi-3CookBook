[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

โค้ดนี้ทำการแปลงโมเดลเป็นรูปแบบ OpenVINO, โหลดโมเดล และใช้โมเดลเพื่อสร้างคำตอบสำหรับข้อความที่กำหนด

1. **การแปลงโมเดล**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - คำสั่งนี้ใช้ `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`

2. **การนำเข้าคลาสและไลบรารีที่จำเป็น**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - บรรทัดเหล่านี้นำเข้าคลาสจากโมดูล `transformers` library and the `optimum.intel.openvino` ซึ่งจำเป็นสำหรับการโหลดและใช้งานโมเดล

3. **การตั้งค่าดirectoryและการกำหนดค่าโมเดล**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` เป็น dictionary ที่กำหนดค่าโมเดล OpenVINO ให้เน้นความหน่วงต่ำ ใช้ inference stream เดียว และไม่ใช้ cache directory

4. **การโหลดโมเดล**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - บรรทัดนี้โหลดโมเดลจาก directory ที่ระบุไว้ โดยใช้การตั้งค่าที่กำหนดไว้ก่อนหน้านี้ และอนุญาตให้มีการรันโค้ดจากระยะไกลหากจำเป็น

5. **การโหลด Tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - บรรทัดนี้โหลด tokenizer ซึ่งทำหน้าที่แปลงข้อความให้เป็น tokens ที่โมเดลสามารถเข้าใจได้

6. **การตั้งค่า Argument ของ Tokenizer**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - dictionary นี้กำหนดว่าไม่ควรเพิ่ม special tokens ลงในผลลัพธ์ที่ถูก tokenized

7. **การกำหนด Prompt**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - สตริงนี้กำหนดข้อความสนทนา โดยผู้ใช้ขอให้ AI assistant แนะนำตัวเอง

8. **การแปลง Prompt ให้เป็น Tokens**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - บรรทัดนี้แปลงข้อความ prompt ให้เป็น tokens ที่โมเดลสามารถประมวลผลได้ และส่งคืนผลลัพธ์ในรูปแบบ PyTorch tensors

9. **การสร้างคำตอบ**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - บรรทัดนี้ใช้โมเดลเพื่อสร้างคำตอบจาก tokens ที่ได้รับ โดยกำหนดให้สร้าง tokens ใหม่ได้สูงสุด 1024 tokens

10. **การถอดรหัสคำตอบ**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - บรรทัดนี้แปลง tokens ที่สร้างขึ้นกลับเป็นข้อความที่มนุษย์อ่านได้ โดยข้าม special tokens และดึงผลลัพธ์แรกออกมา

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติด้วย AI แม้ว่าเราจะพยายามอย่างเต็มที่เพื่อให้การแปลถูกต้อง แต่อาจมีข้อผิดพลาดหรือความไม่แม่นยำเกิดขึ้นได้ โปรดพิจารณาว่าเอกสารต้นฉบับในภาษาต้นทางเป็นแหล่งข้อมูลที่ถูกต้องและเชื่อถือได้ สำหรับข้อมูลสำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่เป็นมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้