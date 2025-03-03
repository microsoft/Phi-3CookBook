## **Phi-4-mini-এ ফাংশন কলিং**

ফাংশন কলিং প্রথমে Phi Family পরিবারে প্রবর্তিত হয়েছিল, এবং এখন আপনি এটি Phi-4-mini-এর মাধ্যমে ব্যবহার করতে পারেন।

এই উদাহরণটি প্রিমিয়ার লিগের ফলাফলের সিমুলেশন প্রদর্শন করে। লক্ষ্য হল Phi-4-mini-এর মাধ্যমে রিয়েল-টাইম গেম তথ্য প্রদান করা। নিচে নমুনা কোড দেওয়া হলো:



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

**অস্বীকৃতি**:  
এই নথিটি মেশিন-ভিত্তিক এআই অনুবাদ পরিষেবাগুলির মাধ্যমে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা বজায় রাখার চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকেই প্রামাণিক উৎস হিসাবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।