**Fino podešavanje Phi-3 s QLoRA**

Fino podešavanje Microsoftovog Phi-3 Mini jezičnog modela koristeći [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA će pomoći u poboljšanju razumijevanja razgovora i generiranja odgovora.

Za učitavanje modela u 4-bitnom formatu koristeći transformers i bitsandbytes, potrebno je instalirati accelerate i transformers iz izvornog koda te osigurati da imate najnoviju verziju bitsandbytes biblioteke.

**Primjeri**
- [Saznajte više s ovim primjerom bilježnice](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Primjer Python skripte za fino podešavanje](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Primjer finog podešavanja na Hugging Face Hubu s LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Primjer finog podešavanja na Hugging Face Hubu s QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Odricanje odgovornosti**:  
Ovaj dokument je preveden pomoću usluga strojno podržanog AI prijevoda. Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.