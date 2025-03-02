# **Finjustering af Phi-3 med Lora**

Finjustering af Microsofts Phi-3 Mini sprogmodel ved hjælp af [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) på et brugerdefineret chat-instruktionsdatasæt.

LoRA vil hjælpe med at forbedre samtaleforståelse og generering af svar.

## Trin-for-trin guide til finjustering af Phi-3 Mini:

**Imports og Opsætning**

Installation af loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Start med at importere nødvendige biblioteker som datasets, transformers, peft, trl og torch.  
Opsæt logning for at spore træningsprocessen.

Du kan vælge at tilpasse nogle lag ved at erstatte dem med modstykker implementeret i loralib. Vi understøtter i øjeblikket kun nn.Linear, nn.Embedding og nn.Conv2d. Vi understøtter også en MergedLinear til tilfælde, hvor en enkelt nn.Linear repræsenterer mere end ét lag, som i nogle implementeringer af attention qkv-projektionen (se Yderligere Noter for mere).

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

Før træningsløkken begynder, markér kun LoRA-parametre som trænbare.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Når du gemmer et checkpoint, generér en state_dict, der kun indeholder LoRA-parametre.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Når du indlæser et checkpoint med load_state_dict, skal du sørge for at sætte strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Nu kan træningen fortsætte som normalt.

**Hyperparametre**

Definér to ordbøger: training_config og peft_config.  
training_config indeholder hyperparametre til træning, såsom læringsrate, batchstørrelse og logningsindstillinger.

peft_config specificerer LoRA-relaterede parametre som rank, dropout og opgavetype.

**Indlæsning af Model og Tokenizer**

Angiv stien til den fortrænede Phi-3-model (f.eks. "microsoft/Phi-3-mini-4k-instruct").  
Konfigurer modelindstillinger, herunder cachebrug, datatype (bfloat16 til mixed precision) og attention-implementering.

**Træning**

Finjustér Phi-3-modellen ved hjælp af det brugerdefinerede chat-instruktionsdatasæt.  
Udnyt LoRA-indstillingerne fra peft_config for effektiv tilpasning.  
Overvåg træningsfremskridt ved hjælp af den specificerede logningsstrategi.  
Evaluering og Gemning: Evaluer den finjusterede model.  
Gem checkpoints under træningen til senere brug.

**Eksempler**
- [Lær mere med denne sample notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Eksempel på Python Finjusteringsscript](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Eksempel på Hugging Face Hub Finjustering med LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Eksempel på Hugging Face Model Card - LORA Finjusteringseksempel](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Eksempel på Hugging Face Hub Finjustering med QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)  

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.