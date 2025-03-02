# **Phi-3 Mini ကို Lora ဖြင့် Fine-tuning**

Microsoft ၏ Phi-3 Mini ဘာသာပြန်မော်ဒယ်ကို [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) ဖြင့် စိတ်ကြိုက်ပြင်ဆင်ထားသော စကားပြောလမ်းညွှန်ဒေတာစနစ်ပေါ်တွင် Fine-tune ပြုလုပ်ခြင်း။

LORA သည် စကားပြောနားလည်မှုနှင့် အဖြေထုတ်ပေးမှုကို တိုးတက်စေပါမည်။

## Phi-3 Mini ကို Fine-tune ပြုလုပ်ရန် လမ်းညွှန်လက်စွဲ

**Imports နှင့် Setup**

loralib ကို install ပြုလုပ်ခြင်း

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

လိုအပ်သော libraries များ (datasets, transformers, peft, trl, torch) ကို import ပြုလုပ်ခြင်းဖြင့် စတင်ပါ။
Training process ကို မှတ်တမ်းတင်ရန် logging ကို ပြင်ဆင်ပါ။

တစ်ချို့သော layers များကို loralib တွင် ဖန်တီးထားသော နည်းလမ်းများဖြင့် အစားထိုးနိုင်ပါသည်။ ယခုအခါ nn.Linear, nn.Embedding, nn.Conv2d ကိုသာ အထောက်အပံ့ပြုလုပ်ထားပါသည်။ ထို့အပြင် attention qkv projection ကို အချို့သော implementation များတွင် nn.Linear တစ်ခုအား အလွှာများစွာကို ကိုယ်စားပြုသော MergedLinear ကိုလည်း ထောက်ပံ့ပါသည် (အောက်တွင် Additional Notes ကိုကြည့်ပါ)။

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

Training loop စတင်မီတွင် LoRA parameters များကိုသာ trainable အဖြစ် သတ်မှတ်ပါ။

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Checkpoint ကို save ပြုလုပ်သည့်အခါ LoRA parameters များသာ ပါဝင်သော state_dict ကို ဖန်တီးပါ။

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict ကို အသုံးပြု၍ checkpoint ကို load ပြုလုပ်သည့်အခါ strict=False ကို သတ်မှတ်ပါ။

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

အခုမှ training ကို သာမန်အတိုင်း ဆက်လက်လုပ်ဆောင်နိုင်ပါပြီ။

**Hyperparameters**

training_config နှင့် peft_config ဟူသော dictionaries နှစ်ခုကို သတ်မှတ်ပါ။ training_config တွင် learning rate, batch size, logging settings ကဲ့သို့သော training အတွက် hyperparameters များပါဝင်သည်။

peft_config တွင် LoRA ဆိုင်ရာ parameters များ (ဥပမာ rank, dropout, task type) ကို သတ်မှတ်ပါ။

**Model နှင့် Tokenizer Loading**

Phi-3 model ကို preload ပြုလုပ်ရန် path (ဥပမာ "microsoft/Phi-3-mini-4k-instruct") ကို သတ်မှတ်ပါ။ model settings (cache အသုံးပြုမှု, data type (mixed precision အတွက် bfloat16), attention implementation) ကို ပြင်ဆင်ပါ။

**Training**

စိတ်ကြိုက်ပြင်ဆင်ထားသော စကားပြောလမ်းညွှန်ဒေတာစနစ်ကို အသုံးပြု၍ Phi-3 model ကို fine-tune ပြုလုပ်ပါ။ LoRA ဆက်တင်များကို peft_config မှ ချိန်ညှိ၍ ထိရောက်မှုရှိစွာ ပြုလုပ်ပါ။ သတ်မှတ်ထားသော logging strategy ကို အသုံးပြု၍ training progress ကို ကြည့်ရှုပါ။

Evaluation နှင့် Save: Fine-tuned model ကို စမ်းသပ်ပါ။
Training လုပ်စဉ်အတွင်း Checkpoints များကို save ပြုလုပ်ပါ။

**Samples**
- [ဤ sample notebook ဖြင့် ပိုမိုလေ့လာရန်](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning Sample နမူနာ](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub Fine Tuning with LORA နမူနာ](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Model Card - LORA Fine Tuning Sample နမူနာ](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub Fine Tuning with QLORA နမူနာ](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

It seems you are asking for a translation into "mo." Could you clarify what language or dialect "mo" refers to? If you mean a specific language (e.g., Mongolian, Maori, or something else), please provide additional context so I can assist you accurately.