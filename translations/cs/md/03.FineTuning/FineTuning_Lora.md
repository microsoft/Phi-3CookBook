# **Doladění Phi-3 pomocí Lora**

Doladění jazykového modelu Microsoft Phi-3 Mini pomocí [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) na vlastním datasetu s instrukcemi pro chat. 

LoRA pomůže zlepšit porozumění konverzaci a generování odpovědí. 

## Krok za krokem, jak doladit Phi-3 Mini:

**Importy a nastavení** 

Instalace loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Začněte importem potřebných knihoven, jako jsou datasets, transformers, peft, trl a torch. 
Nastavte logování pro sledování průběhu tréninku.

Můžete se rozhodnout přizpůsobit některé vrstvy jejich nahrazením alternativami implementovanými v loralib. Aktuálně podporujeme nn.Linear, nn.Embedding a nn.Conv2d. Také podporujeme MergedLinear pro případy, kdy jediný nn.Linear představuje více vrstev, například v některých implementacích projekce qkv v pozornosti (viz Další poznámky pro více informací).

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

Před zahájením tréninkové smyčky označte pouze parametry LoRA jako trénovatelné.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Při ukládání checkpointu vytvořte state_dict, který obsahuje pouze parametry LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Při načítání checkpointu pomocí load_state_dict nezapomeňte nastavit strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Nyní může trénink pokračovat jako obvykle.

**Hyperparametry** 

Definujte dva slovníky: training_config a peft_config. training_config obsahuje hyperparametry pro trénink, jako je rychlost učení, velikost batch a nastavení logování.

peft_config specifikuje parametry související s LoRA, jako je rank, dropout a typ úlohy.

**Načtení modelu a tokenizéru** 

Uveďte cestu k předtrénovanému modelu Phi-3 (např. "microsoft/Phi-3-mini-4k-instruct"). Nakonfigurujte nastavení modelu, včetně použití cache, datového typu (bfloat16 pro smíšenou přesnost) a implementace pozornosti.

**Trénink** 

Doladěte model Phi-3 pomocí vlastního datasetu s instrukcemi pro chat. Využijte nastavení LoRA z peft_config pro efektivní přizpůsobení. Sledujte průběh tréninku pomocí specifikované strategie logování.
Hodnocení a ukládání: Vyhodnoťte doladěný model.
Ukládejte checkpointy během tréninku pro pozdější použití.

**Ukázky**
- [Více informací v tomto ukázkovém notebooku](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Příklad skriptu pro doladění v Pythonu](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Příklad doladění na Hugging Face Hub pomocí LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Příklad karty modelu na Hugging Face - ukázka doladění pomocí LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Příklad doladění na Hugging Face Hub pomocí QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových AI překladatelských služeb. Přestože se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.