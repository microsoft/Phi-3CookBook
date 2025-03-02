## **Phi-4-miniを推論エキスパートとして使用する**

Phi-4の主な特徴の一つは、その強力な推論能力です。Phi-4-miniを通じて、その優れた推論能力を見てみましょう。

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

**免責事項**:  
本書類は、AIによる機械翻訳サービスを使用して翻訳されています。正確さを期すよう努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の母国語による文書が公式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や解釈の誤りについて、当方は一切責任を負いません。