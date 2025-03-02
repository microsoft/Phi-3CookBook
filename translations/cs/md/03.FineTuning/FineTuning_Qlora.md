**Doladění Phi-3 pomocí QLoRA**

Doladění jazykového modelu Phi-3 Mini od Microsoftu pomocí [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA pomůže zlepšit porozumění v konverzacích a generování odpovědí.

Pro načtení modelů ve 4bitové reprezentaci pomocí transformers a bitsandbytes je nutné nainstalovat knihovny accelerate a transformers ze zdrojového kódu a zajistit, že máte nejnovější verzi knihovny bitsandbytes.

**Ukázky**
- [Zjistěte více s tímto ukázkovým notebookem](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Příklad ukázkového skriptu pro doladění v Pythonu](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Příklad doladění pomocí Hugging Face Hub a LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Příklad doladění pomocí Hugging Face Hub a QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových AI překladatelských služeb. Přestože se snažíme o přesnost, mějte na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.