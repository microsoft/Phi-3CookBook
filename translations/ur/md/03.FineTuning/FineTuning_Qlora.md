**Phi-3 کو QLoRA کے ساتھ بہتر بنانا**

Microsoft کے Phi-3 Mini لینگویج ماڈل کو [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) کے ذریعے بہتر بنانا۔

QLoRA گفتگو کو سمجھنے اور جوابات تیار کرنے کی صلاحیت کو بہتر بنانے میں مدد کرے گا۔

4 بٹ میں ماڈلز کو transformers اور bitsandbytes کے ساتھ لوڈ کرنے کے لیے، آپ کو accelerate اور transformers کو سورس سے انسٹال کرنا ہوگا اور یہ یقینی بنانا ہوگا کہ آپ کے پاس bitsandbytes لائبریری کا تازہ ترین ورژن موجود ہو۔

**نمونے**
- [اس نمونے کے نوٹ بک کے ذریعے مزید سیکھیں](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python میں FineTuning کا نمونہ](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub پر LORA کے ساتھ Fine Tuning کا نمونہ](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub پر QLORA کے ساتھ Fine Tuning کا نمونہ](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**ڈس کلیمر**:  
یہ دستاویز مشین پر مبنی AI ترجمہ خدمات کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا نقائص ہو سکتے ہیں۔ اصل دستاویز، جو اس کی مقامی زبان میں ہے، کو مستند ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔