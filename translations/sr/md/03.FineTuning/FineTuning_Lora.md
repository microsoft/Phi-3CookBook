# **Fino podešavanje Phi-3 sa Lora**

Fino podešavanje Microsoftovog Phi-3 Mini jezičkog modela koristeći [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) na prilagođenom datasetu sa uputstvima za razgovor.

LoRA će pomoći u poboljšanju razumevanja konteksta u razgovoru i generisanja odgovora.

## Vodič korak po korak za fino podešavanje Phi-3 Mini:

**Uvoz i postavljanje**

Instalacija loralib-a

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Započnite uvozom potrebnih biblioteka kao što su datasets, transformers, peft, trl i torch. Podesite logovanje kako biste pratili proces treniranja.

Možete odabrati da prilagodite određene slojeve zamenjujući ih ekvivalentima implementiranim u loralib-u. Trenutno podržavamo samo nn.Linear, nn.Embedding i nn.Conv2d. Takođe podržavamo MergedLinear za slučajeve gde jedan nn.Linear predstavlja više slojeva, kao što je u nekim implementacijama qkv projekcije pažnje (pogledajte Dodatne napomene za više informacija).

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

Pre nego što započne petlja za treniranje, označite samo LoRA parametre kao podesive.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Kada čuvate checkpoint, generišite state_dict koji sadrži samo LoRA parametre.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Kada učitavate checkpoint koristeći load_state_dict, obavezno postavite strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Sada treniranje može da se nastavi kao i obično.

**Hiperparametri**

Definišite dva rečnika: training_config i peft_config. training_config uključuje hiperparametre za treniranje, kao što su brzina učenja, veličina batch-a i podešavanja za logovanje.

peft_config specificira parametre vezane za LoRA, kao što su rank, dropout i tip zadatka.

**Učitavanje modela i tokenizera**

Navedite putanju do unapred treniranog Phi-3 modela (npr. "microsoft/Phi-3-mini-4k-instruct"). Konfigurišite podešavanja modela, uključujući korišćenje keša, tip podataka (bfloat16 za mešovitu preciznost) i implementaciju pažnje.

**Treniranje**

Fino podesite Phi-3 model koristeći prilagođeni dataset sa uputstvima za razgovor. Iskoristite LoRA podešavanja iz peft_config za efikasnu adaptaciju. Pratite napredak treniranja koristeći specificiranu strategiju logovanja.  
Evaluacija i čuvanje: Evaluirajte fino podešen model.  
Čuvajte checkpoint-ove tokom treniranja za kasniju upotrebu.

**Primeri**
- [Saznajte više uz ovaj primer u beležnici](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Primer Python skripte za fino podešavanje](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Primer fino podešavanja na Hugging Face Hub-u koristeći LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Primer Hugging Face Model Card - LORA fino podešavanje](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Primer fino podešavanja na Hugging Face Hub-u koristeći QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем машинских услуга за превођење заснованих на вештачкој интелигенцији. Иако настојимо да обезбедимо тачност, молимо вас да будете свесни да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме који могу проистећи из коришћења овог превода.