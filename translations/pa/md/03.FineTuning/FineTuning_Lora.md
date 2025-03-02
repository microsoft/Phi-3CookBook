# **Phi-3 ਨੂੰ Lora ਨਾਲ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ**

ਮਾਈਕਰੋਸਾਫਟ ਦੇ Phi-3 Mini ਭਾਸ਼ਾ ਮਾਡਲ ਨੂੰ ਇੱਕ ਕਸਟਮ ਚੈਟ ਨਿਰਦੇਸ਼ ਡਾਟਾਸੈੱਟ 'ਤੇ [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ। 

LoRA ਗੱਲਬਾਤ ਨੂੰ ਸਮਝਣ ਅਤੇ ਜਵਾਬ ਦੇਣ ਦੀ ਸਮਰੱਥਾ ਵਿੱਚ ਸੁਧਾਰ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ। 

## Phi-3 Mini ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨ ਲਈ ਕਦਮ-ਦਰ-ਕਦਮ ਗਾਈਡ:

**ਇੰਪੋਰਟਸ ਅਤੇ ਸੈਟਅੱਪ** 

loralib ਨੂੰ ਇੰਸਟਾਲ ਕਰਨਾ

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਜਿਵੇਂ ਕਿ datasets, transformers, peft, trl, ਅਤੇ torch ਨੂੰ ਇੰਪੋਰਟ ਕਰਕੇ ਸ਼ੁਰੂ ਕਰੋ। 
ਟ੍ਰੇਨਿੰਗ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਟ੍ਰੈਕ ਕਰਨ ਲਈ ਲੌਗਿੰਗ ਸੈਟਅੱਪ ਕਰੋ। 

ਤੁਸੀਂ ਕੁਝ ਲੇਅਰਾਂ ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰਨ ਲਈ ਉਨ੍ਹਾਂ ਨੂੰ loralib ਵਿੱਚ ਲਾਗੂ ਕੀਤੇ ਗਏ ਸਮਕਾਲੀ ਹਿੱਸਿਆਂ ਨਾਲ ਬਦਲਣ ਦੀ ਚੋਣ ਕਰ ਸਕਦੇ ਹੋ। ਅਸੀਂ ਇਸ ਵੇਲੇ ਸਿਰਫ nn.Linear, nn.Embedding, ਅਤੇ nn.Conv2d ਦਾ ਸਮਰਥਨ ਕਰਦੇ ਹਾਂ। ਅਸੀਂ MergedLinear ਦਾ ਵੀ ਸਮਰਥਨ ਕਰਦੇ ਹਾਂ ਜਿੱਥੇ ਇੱਕ nn.Linear ਕਈ ਲੇਅਰਾਂ ਦਾ ਪ੍ਰਤੀਨਿਧਿਤਾ ਕਰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਕੁਝ attention qkv projection ਦੀਆਂ ਲਾਗੂਆਂ ਵਿੱਚ (ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ ਅਤਿਰਿਕਤ ਨੋਟਸ ਵੇਖੋ)।

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

ਟ੍ਰੇਨਿੰਗ ਲੂਪ ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਸਿਰਫ LoRA ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ trainable ਦੇ ਤੌਰ 'ਤੇ ਮਾਰਕ ਕਰੋ।

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

ਜਦੋਂ ਇੱਕ checkpoint ਸੇਵ ਕਰਦੇ ਹੋ, ਤਾਂ state_dict ਪੈਦਾ ਕਰੋ ਜੋ ਸਿਰਫ LoRA ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਦਾ ਹੋਵੇ।

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

ਜਦੋਂ load_state_dict ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ checkpoint ਲੋਡ ਕਰਦੇ ਹੋ, ਤਾਂ strict=False ਸੈਟ ਕਰਨਾ ਯਕੀਨੀ ਬਣਾਓ।

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

ਹੁਣ ਟ੍ਰੇਨਿੰਗ ਆਮ ਤਰ੍ਹਾਂ ਜਾਰੀ ਰਹਿ ਸਕਦੀ ਹੈ।

**ਹਾਈਪਰਪੈਰਾਮੀਟਰਸ** 

ਦੋ ਡਿਕਸ਼ਨਰੀਜ਼ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ: training_config ਅਤੇ peft_config। training_config ਵਿੱਚ ਟ੍ਰੇਨਿੰਗ ਲਈ ਹਾਈਪਰਪੈਰਾਮੀਟਰ ਸ਼ਾਮਲ ਹਨ, ਜਿਵੇਂ ਕਿ learning rate, batch size, ਅਤੇ logging ਸੈਟਿੰਗਜ਼।

peft_config ਵਿੱਚ LoRA ਨਾਲ ਸੰਬੰਧਤ ਪੈਰਾਮੀਟਰ ਸ਼ਾਮਲ ਹਨ ਜਿਵੇਂ ਕਿ rank, dropout, ਅਤੇ task type।

**ਮਾਡਲ ਅਤੇ Tokenizer ਲੋਡ ਕਰਨਾ** 

ਪਹਿਲਾਂ ਤੋਂ ਟ੍ਰੇਨ ਕੀਤਾ ਗਿਆ Phi-3 ਮਾਡਲ (ਜਿਵੇਂ ਕਿ "microsoft/Phi-3-mini-4k-instruct") ਦੇ ਪਾਥ ਨੂੰ ਨਿਰਧਾਰਿਤ ਕਰੋ। ਮਾਡਲ ਸੈਟਿੰਗਜ਼, ਜਿਸ ਵਿੱਚ cache ਦੀ ਵਰਤੋਂ, data type (bfloat16 ਮਿਕਸਡ ਪ੍ਰਿਸੀਜ਼ਨ ਲਈ), ਅਤੇ attention implementation ਸ਼ਾਮਲ ਹਨ, ਨੂੰ ਕਨਫਿਗਰ ਕਰੋ।

**ਟ੍ਰੇਨਿੰਗ** 

ਕਸਟਮ ਚੈਟ ਨਿਰਦੇਸ਼ ਡਾਟਾਸੈੱਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3 ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ। ਕੁਸ਼ਲ ਅਨੁਕੂਲਤਾ ਲਈ peft_config ਤੋਂ LoRA ਸੈਟਿੰਗਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ। ਨਿਰਧਾਰਿਤ ਲੌਗਿੰਗ ਰਣਨੀਤੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟ੍ਰੇਨਿੰਗ ਪ੍ਰਗਤੀ ਨੂੰ ਮਾਨੀਟਰ ਕਰੋ। 
**ਮੁਲਾਂਕਣ ਅਤੇ ਸੇਵ ਕਰਨਾ:** ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ। ਟ੍ਰੇਨਿੰਗ ਦੌਰਾਨ ਬਾਅਦ ਵਿੱਚ ਵਰਤੋਂ ਲਈ checkpoints ਸੇਵ ਕਰੋ।

**ਸੈਂਪਲਸ**
- [ਇਸ ਸੈਂਪਲ ਨੋਟਬੁੱਕ ਨਾਲ ਹੋਰ ਸਿੱਖੋ](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning ਦਾ ਉਦਾਹਰਣ](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub ਨਾਲ LoRA ਫਾਈਨ ਟਿਊਨਿੰਗ ਦਾ ਉਦਾਹਰਣ](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Model Card ਦਾ ਉਦਾਹਰਣ - LoRA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub ਨਾਲ QLORA ਫਾਈਨ ਟਿਊਨਿੰਗ ਦਾ ਉਦਾਹਰਣ](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**ਅਸਵੀਕਾਰਨਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ-ਆਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਆਟੋਮੇਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਣਨਪੱਤਰ ਹੋ ਸਕਦੇ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜੋ ਕਿ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੈ, ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।