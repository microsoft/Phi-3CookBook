**Fino podešavanje Phi-3 sa QLoRA**

Fino podešavanje Microsoft-ovog Phi-3 Mini jezičkog modela koristeći [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA će pomoći u poboljšanju razumevanja u konverzaciji i generisanju odgovora.

Da biste učitali modele u 4 bita koristeći transformers i bitsandbytes, potrebno je da instalirate accelerate i transformers iz izvornog koda i da se uverite da imate najnoviju verziju bitsandbytes biblioteke.

**Primeri**
- [Saznajte više uz ovaj primer beležnice](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Primer Python skripte za fino podešavanje](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Primer fino podešavanja na Hugging Face Hub-u sa LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Primer fino podešavanja na Hugging Face Hub-u sa QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква неспоразума или погрешна тумачења која могу произаћи из употребе овог превода.