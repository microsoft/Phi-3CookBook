**Phi-3 ਨੂੰ QLoRA ਨਾਲ Fine-tuning ਕਰਨਾ**

Microsoft ਦੇ Phi-3 Mini ਭਾਸ਼ਾ ਮਾਡਲ ਨੂੰ [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) ਦੀ ਵਰਤੋਂ ਕਰਕੇ fine-tune ਕਰਨਾ। 

QLoRA ਗੱਲਬਾਤ ਦੀ ਸਮਝ ਅਤੇ ਜਵਾਬ ਪੈਦਾ ਕਰਨ ਦੀ ਯੋਗਤਾ ਨੂੰ ਬਹਿਤਰ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ। 

ਮਾਡਲਾਂ ਨੂੰ 4bits ਵਿੱਚ transformers ਅਤੇ bitsandbytes ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲੋਡ ਕਰਨ ਲਈ, ਤੁਹਾਨੂੰ accelerate ਅਤੇ transformers ਨੂੰ source ਤੋਂ install ਕਰਨਾ ਪਵੇਗਾ ਅਤੇ ਯਕੀਨੀ ਬਣਾਉਣਾ ਪਵੇਗਾ ਕਿ ਤੁਹਾਡੇ ਕੋਲ bitsandbytes ਲਾਇਬ੍ਰੇਰੀ ਦਾ ਸਭ ਤੋਂ ਨਵਾਂ ਵਰਜਨ ਹੈ।

**ਨਮੂਨੇ**
- [ਇਸ ਨਮੂਨਾ ਨੋਟਬੁੱਕ ਨਾਲ ਹੋਰ ਸਿੱਖੋ](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning ਦਾ ਉਦਾਹਰਨ ਨਮੂਨਾ](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub Fine Tuning ਦਾ ਉਦਾਹਰਨ LORA ਨਾਲ](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub Fine Tuning ਦਾ ਉਦਾਹਰਨ QLORA ਨਾਲ](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**ਅਸਵੀਕਾਰਨ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ-ਆਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਆਟੋਮੇਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਨਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪ੍ਰੋਫੈਸ਼ਨਲ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।