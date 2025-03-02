**Phi-3 finomhangolása QLoRA-val**

A Microsoft Phi-3 Mini nyelvi modelljének finomhangolása [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) segítségével.

A QLoRA segít javítani a beszélgetési megértést és a válaszgenerálást.

Ahhoz, hogy modelleket 4 biten betölts transformers és bitsandbytes használatával, telepítened kell az accelerate-t és a transformers-t forrásból, valamint meg kell győződnöd arról, hogy a bitsandbytes könyvtár legújabb verziója van telepítve.

**Minták**
- [Tudj meg többet ezzel a minta notebookkal](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python finomhangolási példa](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub finomhangolási példa LORA-val](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub finomhangolási példa QLORA-val](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítási szolgáltatások segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatizált fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.