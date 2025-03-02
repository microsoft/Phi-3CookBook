[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

یہ کوڈ ایک ماڈل کو OpenVINO فارمیٹ میں ایکسپورٹ کرتا ہے، اسے لوڈ کرتا ہے، اور دیے گئے پرامپٹ کے جواب میں ایک ریسپانس تیار کرتا ہے۔

1. **ماڈل کو ایکسپورٹ کرنا**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - یہ کمانڈ `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` استعمال کرتی ہے۔

2. **ضروری لائبریریاں امپورٹ کرنا**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - یہ لائنیں `transformers` library and the `optimum.intel.openvino` ماڈیول سے کلاسز امپورٹ کرتی ہیں، جو ماڈل کو لوڈ کرنے اور استعمال کرنے کے لیے ضروری ہیں۔

3. **ماڈل ڈائریکٹری اور کنفیگریشن سیٹ اپ کرنا**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` ایک ڈکشنری ہے جو OpenVINO ماڈل کو کم تاخیر، ایک انفیرنس اسٹریم، اور کیش ڈائریکٹری کے بغیر ترجیح دینے کے لیے کنفیگر کرتی ہے۔

4. **ماڈل لوڈ کرنا**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - یہ لائن مخصوص ڈائریکٹری سے ماڈل کو لوڈ کرتی ہے، پہلے سے دی گئی کنفیگریشن سیٹنگز کا استعمال کرتے ہوئے۔ یہ ضرورت پڑنے پر ریموٹ کوڈ ایکزیکیوشن کی اجازت بھی دیتی ہے۔

5. **ٹوکینائزر لوڈ کرنا**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - یہ لائن ٹوکینائزر کو لوڈ کرتی ہے، جو ٹیکسٹ کو ایسے ٹوکنز میں تبدیل کرتا ہے جنہیں ماڈل سمجھ سکتا ہے۔

6. **ٹوکینائزر آرگومنٹس سیٹ اپ کرنا**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - یہ ڈکشنری یہ وضاحت کرتی ہے کہ ٹوکینائزڈ آؤٹ پٹ میں اسپیشل ٹوکنز شامل نہ کیے جائیں۔

7. **پرامپٹ ڈیفائن کرنا**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - یہ اسٹرنگ ایک گفتگو کا پرامپٹ سیٹ کرتی ہے، جہاں یوزر AI اسسٹنٹ سے اپنا تعارف کرانے کے لیے کہتا ہے۔

8. **پرامپٹ کو ٹوکینائز کرنا**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - یہ لائن پرامپٹ کو ایسے ٹوکنز میں تبدیل کرتی ہے جنہیں ماڈل پروسیس کر سکتا ہے، اور نتیجہ PyTorch ٹینسرز کی صورت میں دیتی ہے۔

9. **ریسپانس تیار کرنا**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - یہ لائن ماڈل کو استعمال کرتے ہوئے ان پٹ ٹوکنز کی بنیاد پر ایک ریسپانس تیار کرتی ہے، جس میں زیادہ سے زیادہ 1024 نئے ٹوکنز شامل ہو سکتے ہیں۔

10. **ریسپانس کو ڈی کوڈ کرنا**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - یہ لائن تیار کردہ ٹوکنز کو دوبارہ ایک انسانی سمجھنے کے قابل اسٹرنگ میں تبدیل کرتی ہے، کسی بھی اسپیشل ٹوکنز کو نظر انداز کرتے ہوئے، اور پہلا نتیجہ حاصل کرتی ہے۔

**اعلانِ لاتعلقی**:  
یہ دستاویز مشین پر مبنی اے آئی ترجمہ خدمات کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے پوری کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہیں۔ اصل دستاویز، جو اس کی اصل زبان میں ہے، مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔