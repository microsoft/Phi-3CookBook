# **Phi-3 Fine-tunen met Lora**

Fine-tunen van Microsoft's Phi-3 Mini taalmodel met behulp van [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) op een aangepaste dataset met chatinstructies.

LORA helpt bij het verbeteren van conversatiebegrip en het genereren van reacties.

## Stapsgewijze handleiding voor het fine-tunen van Phi-3 Mini:

**Imports en Setup**

Installeren van loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Begin met het importeren van de benodigde bibliotheken, zoals datasets, transformers, peft, trl en torch. Stel logging in om het trainingsproces te volgen.

Je kunt ervoor kiezen om enkele lagen aan te passen door ze te vervangen door equivalenten geïmplementeerd in loralib. We ondersteunen momenteel alleen nn.Linear, nn.Embedding en nn.Conv2d. We ondersteunen ook een MergedLinear voor gevallen waarin een enkele nn.Linear meerdere lagen vertegenwoordigt, zoals in sommige implementaties van de attention qkv-projectie (zie Aanvullende Notities voor meer informatie).

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

Markeer vóór het trainingsproces alleen de LoRA-parameters als trainable.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Bij het opslaan van een checkpoint, genereer een state_dict die alleen LoRA-parameters bevat.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Bij het laden van een checkpoint met load_state_dict, zorg ervoor dat strict=False is ingesteld.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Nu kan de training zoals gebruikelijk doorgaan.

**Hyperparameters**

Definieer twee woordenboeken: training_config en peft_config. training_config bevat hyperparameters voor training, zoals de learning rate, batchgrootte en loginstellingen.

peft_config specificeert LoRA-gerelateerde parameters zoals rank, dropout en het type taak.

**Model- en Tokenizer Laden**

Specificeer het pad naar het voorgetrainde Phi-3 model (bijvoorbeeld "microsoft/Phi-3-mini-4k-instruct"). Configureer modelinstellingen, waaronder cachegebruik, datatype (bfloat16 voor mixed precision) en de implementatie van attention.

**Training**

Fine-tune het Phi-3 model met behulp van de aangepaste dataset met chatinstructies. Maak gebruik van de LoRA-instellingen uit peft_config voor efficiënte aanpassing. Volg de voortgang van de training met de gespecificeerde loggingstrategie.

Evaluatie en Opslaan: Evalueer het gefinetunede model. Sla checkpoints op tijdens de training voor later gebruik.

**Voorbeelden**
- [Meer leren met dit voorbeeldnotebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Voorbeeld van Python FineTuning Script](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Voorbeeld van Hugging Face Hub Fine Tuning met LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Voorbeeld Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Voorbeeld van Hugging Face Hub Fine Tuning met QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Disclaimer**:  
Dit document is vertaald met behulp van machine-gebaseerde AI-vertalingsdiensten. Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.