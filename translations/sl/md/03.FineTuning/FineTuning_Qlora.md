**Prilagajanje Phi-3 z QLoRA**

Prilagajanje Microsoftovega jezikovnega modela Phi-3 Mini z uporabo [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora). 

QLoRA bo pripomogla k izboljšanju razumevanja pogovorov in generiranja odgovorov.

Za nalaganje modelov v 4-bitnem formatu z uporabo transformers in bitsandbytes morate namestiti accelerate in transformers iz izvorne kode ter zagotoviti, da imate najnovejšo različico knjižnice bitsandbytes.

**Primeri**
- [Več informacij s tem vzorčnim zvezkom](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Primer Python skripte za prilagajanje](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Primer prilagajanja Hugging Face Hub z LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Primer prilagajanja Hugging Face Hub z QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Zavrnitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko samodejni prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije je priporočljivo profesionalno človeško prevajanje. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi izhajale iz uporabe tega prevoda.