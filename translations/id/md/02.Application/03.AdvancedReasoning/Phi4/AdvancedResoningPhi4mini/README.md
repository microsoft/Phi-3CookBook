## **Menggunakan Phi-4-mini sebagai Ahli Penalaran**

Salah satu fitur utama dari Phi-4 adalah kemampuannya dalam penalaran yang kuat. Mari kita lihat kemampuan penalaran yang kuat ini melalui Phi-4-mini.

```python

import torch
from transformers import AutoTokenizer,pipeline

model_path = "Your Phi-4-mini location"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="cuda",
    attn_implementation="flash_attention_2",
    torch_dtype="auto",
    trust_remote_code=True)

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": """I have $20,000 in my savings account, where I receive a 4% profit per year and payments twice a year. Can you please tell me how long it will take for me to become a millionaire? Thinks step by step carefully.
"""},
]

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

generation_args = {
    "max_new_tokens": 4096,
    "return_full_text": False,
    "temperature": 0.00001,
    "top_p": 1.0,
    "do_sample": True,
}

output = pipe(messages, **generation_args)

print(output[0]['generated_text'])



```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.