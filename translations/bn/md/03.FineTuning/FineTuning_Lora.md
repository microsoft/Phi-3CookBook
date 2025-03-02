# **Phi-3-কে Lora দিয়ে ফাইন-টিউন করা**

মাইক্রোসফটের Phi-3 Mini ভাষার মডেলকে [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) ব্যবহার করে একটি কাস্টম চ্যাট ইনস্ট্রাকশন ডেটাসেটে ফাইন-টিউন করা হচ্ছে।

LORA কথোপকথনের বোঝাপড়া এবং প্রতিক্রিয়া তৈরির দক্ষতা বাড়াতে সাহায্য করবে।

## Phi-3 Mini ফাইন-টিউন করার ধাপ-ধাপে নির্দেশিকা:

**ইমপোর্ট এবং সেটআপ**

loralib ইনস্টল করা

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

প্রয়োজনীয় লাইব্রেরি যেমন datasets, transformers, peft, trl এবং torch ইমপোর্ট করে শুরু করুন।  
ট্রেনিং প্রক্রিয়া ট্র্যাক করার জন্য লগিং সেটআপ করুন।

কিছু লেয়ারকে loralib দিয়ে ইমপ্লিমেন্ট করা বিকল্প লেয়ার দিয়ে পরিবর্তন করার জন্য নির্বাচন করতে পারেন।  
বর্তমানে আমরা শুধুমাত্র nn.Linear, nn.Embedding এবং nn.Conv2d সাপোর্ট করি।  
এছাড়াও, এমন কিছু ক্ষেত্রে যেখানে একটি nn.Linear একাধিক লেয়ারকে উপস্থাপন করে, যেমন কিছু অ্যাটেনশন qkv প্রজেকশনের ইমপ্লিমেন্টেশনে, আমরা MergedLinear সাপোর্ট করি (অতিরিক্ত নোট দেখুন)।

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

ট্রেনিং লুপ শুরু হওয়ার আগে শুধুমাত্র LoRA প্যারামিটারগুলোকে ট্রেনেবল হিসেবে মার্ক করুন।

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

চেকপয়েন্ট সংরক্ষণ করার সময়, এমন একটি state_dict তৈরি করুন যা শুধুমাত্র LoRA প্যারামিটারগুলো ধারণ করে।

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict ব্যবহার করে চেকপয়েন্ট লোড করার সময় strict=False সেট করতে ভুলবেন না।

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

এখন ট্রেনিং স্বাভাবিকভাবে চালিয়ে যেতে পারেন।

**হাইপারপ্যারামিটার**

দুটি ডিকশনারি ডিফাইন করুন: training_config এবং peft_config।  
training_config-এ ট্রেনিংয়ের জন্য হাইপারপ্যারামিটার যেমন লার্নিং রেট, ব্যাচ সাইজ, এবং লগিং সেটিংস অন্তর্ভুক্ত থাকবে।  

peft_config-এ LoRA সম্পর্কিত প্যারামিটার যেমন rank, dropout এবং task type নির্ধারণ করুন।

**মডেল এবং টোকেনাইজার লোড করা**

প্রি-ট্রেইন্ড Phi-3 মডেলের পথ নির্দিষ্ট করুন (যেমন "microsoft/Phi-3-mini-4k-instruct")।  
মডেলের সেটিংস কনফিগার করুন, যার মধ্যে থাকবে ক্যাশ ব্যবহার, ডেটা টাইপ (মিশ্র প্রিসিশনের জন্য bfloat16), এবং অ্যাটেনশন ইমপ্লিমেন্টেশন।

**ট্রেনিং**

কাস্টম চ্যাট ইনস্ট্রাকশন ডেটাসেট ব্যবহার করে Phi-3 মডেল ফাইন-টিউন করুন।  
peft_config থেকে LoRA সেটিংস ব্যবহার করে দক্ষতার সাথে অ্যাডাপ্ট করুন।  
নির্ধারিত লগিং স্ট্র্যাটেজি ব্যবহার করে ট্রেনিং প্রগ্রেস মনিটর করুন।  
**মূল্যায়ন এবং সংরক্ষণ:**  
ফাইন-টিউন করা মডেলের মূল্যায়ন করুন।  
পরবর্তী ব্যবহারের জন্য ট্রেনিং চলাকালে চেকপয়েন্ট সংরক্ষণ করুন।

**উদাহরণসমূহ**
- [এই স্যাম্পল নোটবুক থেকে আরও জানুন](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [পাইথন ফাইন-টিউনিং স্যাম্পলের উদাহরণ](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub-এ LoRA দিয়ে ফাইন-টিউনিংয়ের উদাহরণ](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face মডেল কার্ড উদাহরণ - LoRA ফাইন-টিউনিং স্যাম্পল](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub-এ QLORA দিয়ে ফাইন-টিউনিংয়ের উদাহরণ](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**অস্বীকৃতি**:  
এই নথি মেশিন-ভিত্তিক কৃত্রিম বুদ্ধিমত্তা অনুবাদ পরিষেবা ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য নির্ভুলতার জন্য চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহার থেকে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী থাকব না।