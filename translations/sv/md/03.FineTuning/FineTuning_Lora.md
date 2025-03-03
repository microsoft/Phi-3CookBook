# **Finjustering av Phi-3 med Lora**

Finjustering av Microsofts språkmodell Phi-3 Mini med hjälp av [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) på en anpassad dataset för chattinstruktioner.

LoRA hjälper till att förbättra förståelsen för samtal och genereringen av svar.

## Steg-för-steg-guide för att finjustera Phi-3 Mini:

**Importeringar och inställning**

Installera loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Börja med att importera nödvändiga bibliotek som datasets, transformers, peft, trl och torch.  
Ställ in loggning för att spåra träningsprocessen.

Du kan välja att anpassa vissa lager genom att ersätta dem med motsvarigheter implementerade i loralib. För närvarande stöds endast nn.Linear, nn.Embedding och nn.Conv2d. Vi stöder också MergedLinear för fall där en enda nn.Linear representerar flera lager, som i vissa implementationer av attention qkv-projektion (se Ytterligare Anteckningar för mer information).

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

Innan träningsloopen börjar, markera endast LoRA-parametrar som träningsbara.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

När en checkpoint sparas, generera ett state_dict som endast innehåller LoRA-parametrar.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

När du laddar en checkpoint med load_state_dict, se till att ställa in strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Nu kan träningen fortsätta som vanligt.

**Hyperparametrar**

Definiera två ordböcker: training_config och peft_config.  
training_config inkluderar hyperparametrar för träning, såsom inlärningshastighet, batchstorlek och loggningsinställningar.

peft_config specificerar LoRA-relaterade parametrar som rank, dropout och uppgiftstyp.

**Laddning av Modell och Tokenizer**

Specificera sökvägen till den förtränade Phi-3-modellen (t.ex. "microsoft/Phi-3-mini-4k-instruct").  
Konfigurera modellinställningar, inklusive cacheanvändning, datatyp (bfloat16 för blandad precision) och attention-implementation.

**Träning**

Finjustera Phi-3-modellen med den anpassade dataseten för chattinstruktioner.  
Använd LoRA-inställningarna från peft_config för effektiv anpassning.  
Övervaka träningsprocessen med den angivna loggningsstrategin.

**Utvärdering och Sparande**  
Utvärdera den finjusterade modellen.  
Spara checkpoints under träningen för senare användning.

**Exempel**
- [Lär dig mer med detta exempelnotebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exempel på Python Finjusteringsskript](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Exempel på finjustering med LORA på Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Exempel på Hugging Face Model Card - LORA Finjustering](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Exempel på finjustering med QLORA på Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen notera att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell human översättning. Vi ansvarar inte för missförstånd eller feltolkningar som uppstår vid användning av denna översättning.