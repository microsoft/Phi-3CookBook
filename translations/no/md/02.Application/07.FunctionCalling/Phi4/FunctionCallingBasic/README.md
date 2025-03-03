## **Funksjonskall i Phi-4-mini**

Funksjonskall dukket først opp i Phi-familien, og nå kan du bruke det gjennom Phi-4-mini.

Dette eksempelet viser en simulering av Premier League-resultater. Målet er at Phi-4-mini skal levere sanntidsinformasjon om kampene. Nedenfor er eksempel på kode:



```python

import torch
import json
import random
import string
import re
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig,pipeline,AutoTokenizer

model_path = "Your Phi-4-mini location"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="cuda",
    attn_implementation="flash_attention_2",
    torch_dtype="auto",
    trust_remote_code=True)

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

# Tools should be a list of functions stored in json format
tools = [
    {
        "name": "get_match_result",
        "description": "get match result",
        "parameters": {
            "match": {
                "description": "The name of the match",
                "type": "str",
                "default": "Arsenal vs ManCity"
            }
        }
    },
]

# Function implementations

def get_match_result(match: str) -> str:
    # This would be replaced by a weather API
    match_data = {
        "Arsenal vs ManCity": "1:1",
        "Chelsea vs ManUnited": "0:2"
    }
    return match_data.get(match, "I don't know")


messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant",
        "tools": json.dumps(tools), # pass the tools into system message using tools argument
    },
    {
        "role": "user",
        "content": "What is the result of Arsenal vs ManCity today?"
    }
]

inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_dict=True, return_tensors="pt")

inputs = {k: v.to(model.device) for k, v in inputs.items()}
output = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(output[0][len(inputs["input_ids"][0]):]))

tokenizer.batch_decode(output)

response = tokenizer.decode(output[0][len(inputs["input_ids"][0]):], skip_special_tokens=True)

tool_call_id = ''.join(random.choices(string.ascii_letters + string.digits, k=9))

messages.append({"role": "assistant", "tool_calls": [{"type": "function", "id": tool_call_id, "function": response}]})

try :
    tool_call = json.loads(response)[0]

except :
    json_part = re.search(r'\[.*\]', response, re.DOTALL).group(0)

    tool_call = json.loads(json_part)[0]


function_name = tool_call["name"]   

arguments = tool_call["arguments"]

result = get_match_result(**arguments) 

messages.append({"role": "tool", "tool_call_id": tool_call_id, "name": "get_match_result", "content": str(result)})

print(messages)

```

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi bestreber oss på nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.