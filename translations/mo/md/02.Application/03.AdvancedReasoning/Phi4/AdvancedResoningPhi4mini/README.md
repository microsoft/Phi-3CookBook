## **Phi-4-mini ကို အကြံဉာဏ်ပေး ကျွမ်းကျင်သူအဖြစ် အသုံးပြုခြင်း**

Phi-4 ရဲ့ အဓိက အစွမ်းထက် လက္ခဏာတွေထဲက တစ်ခုကတော့ အကြံဉာဏ်ပေး စွမ်းရည် အရမ်းပြင်းထန်မှု ဖြစ်ပါတယ်။ Phi-4-mini ရဲ့ အကြံဉာဏ်ပေး စွမ်းရည် ပြင်းထန်မှုကို စမ်းသပ်ကြည့်ရအောင်။

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

It seems you might be referring to a language or code by "mo." Could you please clarify what you mean by "mo"? Are you referring to a specific language, such as Moldovan (Romanian), or something else? This will help me provide an accurate translation.