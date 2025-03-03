**Doladenie Phi-3 s QLoRA**

Doladenie jazykového modelu Microsoft Phi-3 Mini pomocou [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora). 

QLoRA pomôže zlepšiť porozumenie v konverzáciách a generovanie odpovedí.

Na načítanie modelov v 4 bitoch pomocou transformers a bitsandbytes je potrebné nainštalovať accelerate a transformers zo zdroja a uistiť sa, že máte najnovšiu verziu knižnice bitsandbytes.

**Príklady**
- [Viac informácií v tomto ukážkovom notebooku](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Príklad ukážky doladenia v Pythone](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Príklad doladenia na Hugging Face Hub pomocou LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Príklad doladenia na Hugging Face Hub pomocou QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Upozornenie**:  
Tento dokument bol preložený pomocou služieb strojového prekladu založených na umelej inteligencii. Aj keď sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za záväzný zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.