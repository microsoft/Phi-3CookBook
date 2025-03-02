## **Använda Phi-4-mini som resonemangsexpert**

En av de främsta egenskaperna hos Phi-4 är dess starka förmåga till resonemang. Låt oss titta närmare på denna förmåga genom Phi-4-mini.

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

**Ansvarsfriskrivning**:  
Detta dokument har översatts med maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen notera att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på sitt ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för missförstånd eller feltolkningar som uppstår vid användning av denna översättning.