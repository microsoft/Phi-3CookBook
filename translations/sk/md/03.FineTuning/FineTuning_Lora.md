# **Jemné doladenie Phi-3 s Lora**

Jemné doladenie jazykového modelu Phi-3 Mini od Microsoftu pomocou [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) na vlastnom datasete s inštrukciami pre chat.

LORA pomôže zlepšiť pochopenie konverzácií a generovanie odpovedí.

## Krok za krokom, ako jemne doladiť Phi-3 Mini:

**Importy a nastavenie**

Inštalácia loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Začnite importovaním potrebných knižníc, ako sú datasets, transformers, peft, trl a torch. Nastavte logovanie na sledovanie procesu tréningu.

Môžete sa rozhodnúť prispôsobiť niektoré vrstvy nahradením ich ekvivalentmi implementovanými v loralib. Momentálne podporujeme nn.Linear, nn.Embedding a nn.Conv2d. Podporujeme aj MergedLinear pre prípady, keď jedna nn.Linear predstavuje viac vrstiev, napríklad v niektorých implementáciách projekcie qkv v pozornosti (pozrite si ďalšie poznámky pre viac informácií).

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

Pred začiatkom tréningového cyklu označte ako trénovateľné iba parametre LoRA.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Pri ukladaní kontrolného bodu (checkpoint) vygenerujte state_dict, ktorý obsahuje iba parametre LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Pri načítaní kontrolného bodu pomocou load_state_dict nezabudnite nastaviť strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Teraz môže tréning pokračovať ako zvyčajne.

**Hyperparametre**

Definujte dva slovníky: training_config a peft_config. training_config obsahuje hyperparametre pre tréning, ako je rýchlosť učenia, veľkosť dávky a nastavenia logovania.

peft_config špecifikuje parametre súvisiace s LoRA, ako sú rank, dropout a typ úlohy.

**Načítanie modelu a tokenizéra**

Špecifikujte cestu k predtrénovanému modelu Phi-3 (napr. "microsoft/Phi-3-mini-4k-instruct"). Nakonfigurujte nastavenia modelu vrátane použitia cache, dátového typu (bfloat16 pre zmiešanú presnosť) a implementácie pozornosti.

**Tréning**

Jemne dolaďte model Phi-3 pomocou vlastného datasetu s inštrukciami pre chat. Využite nastavenia LoRA z peft_config na efektívnu adaptáciu. Sledujte priebeh tréningu pomocou špecifikovanej stratégie logovania.  
Hodnotenie a uloženie: Vyhodnoťte jemne doladený model.  
Ukladajte kontrolné body počas tréningu na neskoršie použitie.

**Príklady**
- [Zistite viac pomocou tohto ukážkového notebooku](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Ukážka Python skriptu na jemné doladenie](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Príklad jemného doladenia s LORA na Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Príklad Hugging Face Model Card - Jemné doladenie s LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Príklad jemného doladenia s QLORA na Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladateľských služieb. Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.