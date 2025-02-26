**Fine-tuning Phi-3 with QLoRA**

Fine-tuning Microsoft’s Phi-3 Mini language model using [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora). 

QLoRA will help improve conversational understanding and response generation. 

To load models in 4bits with transformers and bitsandbytes, you have to install accelerate and transformers from source and make sure you have the latest version of the bitsandbytes library.

**Samples**
- [Learn More with this sample notebook](../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Example of Python FineTuning Sample](../../code/03.Finetuning/FineTrainingScript.py)
- [Example of Hugging Face Hub Fine Tuning with LORA](../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Example of Hugging Face Hub Fine Tuning with QLORA](../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)