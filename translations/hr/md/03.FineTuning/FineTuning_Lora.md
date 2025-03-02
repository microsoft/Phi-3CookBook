# **Fino podešavanje Phi-3 s Lora**

Fino podešavanje Microsoftovog Phi-3 Mini jezičnog modela pomoću [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) na prilagođenom skupu podataka s uputama za chat.

LoRA će pomoći u poboljšanju razumijevanja razgovora i generiranja odgovora.

## Vodič korak po korak za fino podešavanje Phi-3 Mini:

**Uvoz i postavljanje**

Instalacija loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Počnite uvozom potrebnih knjižnica kao što su datasets, transformers, peft, trl i torch. Postavite logiranje kako biste pratili proces treniranja.

Možete odabrati prilagoditi neke slojeve zamjenom s onima implementiranim u loralib. Trenutno podržavamo samo nn.Linear, nn.Embedding i nn.Conv2d. Također podržavamo MergedLinear za slučajeve kada jedan nn.Linear predstavlja više slojeva, kao što je to u nekim implementacijama projekcije pažnje qkv (vidi Dodatne napomene za više informacija).

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

Prije nego što započne petlja za treniranje, označite samo LoRA parametre kao trenirajuće.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Prilikom spremanja kontrolne točke, generirajte state_dict koji sadrži samo LoRA parametre.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Prilikom učitavanja kontrolne točke pomoću load_state_dict, obavezno postavite strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Sada treniranje može započeti kao i obično.

**Hiperparametri**

Definirajte dva rječnika: training_config i peft_config. training_config uključuje hiperparametre za treniranje, poput stope učenja, veličine serije i postavki logiranja.

peft_config specificira parametre vezane uz LoRA, poput rank, dropout i tip zadatka.

**Učitavanje modela i tokenizatora**

Navedite put do unaprijed istreniranog Phi-3 modela (npr. "microsoft/Phi-3-mini-4k-instruct"). Konfigurirajte postavke modela, uključujući korištenje predmemorije, tip podataka (bfloat16 za mješovitu preciznost) i implementaciju pažnje.

**Treniranje**

Fino podesite Phi-3 model pomoću prilagođenog skupa podataka s uputama za chat. Iskoristite LoRA postavke iz peft_config za učinkovitu prilagodbu. Pratite napredak treniranja koristeći specificiranu strategiju logiranja.

Evaluacija i spremanje: Evaluirajte fino podešeni model. Spremite kontrolne točke tijekom treniranja za kasniju upotrebu.

**Primjeri**
- [Saznajte više uz ovaj primjer bilježnice](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Primjer Python skripte za fino podešavanje](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Primjer fino podešavanja na Hugging Face Hub s LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Primjer Hugging Face kartice modela - uzorak fino podešavanja s LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Primjer fino podešavanja na Hugging Face Hub s QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden koristeći usluge strojno baziranog AI prevođenja. Iako nastojimo osigurati točnost, molimo vas da budete svjesni da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati mjerodavnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.