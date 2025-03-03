# **Prilagajanje Phi-3 z Lora**

Prilagajanje Microsoftovega jezikovnega modela Phi-3 Mini z uporabo [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) na prilagojenem naboru podatkov za navodila za klepet.

LoRA bo pripomogla k izboljšanju razumevanja pogovorov in generiranja odgovorov.

## Korak za korakom vodič za prilagajanje Phi-3 Mini:

**Uvoz in nastavitev**

Namestitev loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Najprej uvozite potrebne knjižnice, kot so datasets, transformers, peft, trl in torch. Nastavite beleženje za sledenje poteku treninga.

Lahko se odločite za prilagoditev nekaterih plasti z zamenjavo z različicami, implementiranimi v loralib. Trenutno podpiramo samo nn.Linear, nn.Embedding in nn.Conv2d. Prav tako podpiramo MergedLinear za primere, kjer en sam nn.Linear predstavlja več plasti, kot je to v nekaterih implementacijah projekcije attention qkv (glejte Dodatne opombe za več informacij).

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

Pred začetkom zanke za trening označite le parametre LoRA kot trenirljive.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Pri shranjevanju kontrolne točke ustvarite state_dict, ki vsebuje samo parametre LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Pri nalaganju kontrolne točke z uporabo load_state_dict poskrbite, da nastavite strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Zdaj lahko trening poteka kot običajno.

**Hiperparametri**

Določite dva slovarja: training_config in peft_config. training_config vključuje hiperparametre za trening, kot so hitrost učenja, velikost serije in nastavitve beleženja.

peft_config določa parametre, povezane z LoRA, kot so rank, dropout in vrsta naloge.

**Nalaganje modela in tokenizatorja**

Določite pot do predhodno usposobljenega modela Phi-3 (npr. "microsoft/Phi-3-mini-4k-instruct"). Konfigurirajte nastavitve modela, vključno z uporabo predpomnilnika, podatkovnim tipom (bfloat16 za mešano natančnost) in implementacijo attention.

**Trening**

Prilagodite model Phi-3 z uporabo prilagojenega nabora podatkov za navodila za klepet. Uporabite nastavitve LoRA iz peft_config za učinkovito prilagajanje. Spremljajte napredek treninga z določeno strategijo beleženja.

Ocena in shranjevanje: Ocenite prilagojeni model. Shranjujte kontrolne točke med treningom za poznejšo uporabo.

**Primeri**
- [Več informacij s tem primerom v zvezku](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Primer Python skripte za prilagajanje](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Primer prilagajanja na Hugging Face Hub z LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Primer Hugging Face modelne kartice - vzorec prilagajanja z LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Primer prilagajanja na Hugging Face Hub z QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvirnem jeziku se šteje za avtoritativni vir. Za ključne informacije je priporočljivo profesionalno človeško prevajanje. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.