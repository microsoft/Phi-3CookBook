# **Ottimizzazione di Phi-3 con LoRA**

Ottimizzazione del modello linguistico Phi-3 Mini di Microsoft utilizzando [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) su un dataset personalizzato di istruzioni per chat.

LoRA aiuterà a migliorare la comprensione conversazionale e la generazione di risposte.

## Guida passo passo su come ottimizzare Phi-3 Mini:

**Importazioni e Configurazione**

Installazione di loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Inizia importando le librerie necessarie come datasets, transformers, peft, trl e torch. Configura il logging per monitorare il processo di addestramento.

Puoi scegliere di adattare alcuni livelli sostituendoli con equivalenti implementati in loralib. Al momento supportiamo solo nn.Linear, nn.Embedding e nn.Conv2d. Supportiamo anche MergedLinear per i casi in cui un singolo nn.Linear rappresenta più di un livello, come in alcune implementazioni della proiezione qkv dell'attenzione (vedi Note Aggiuntive per maggiori dettagli).

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

Prima che il ciclo di addestramento inizi, contrassegna come allenabili solo i parametri di LoRA.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Quando salvi un checkpoint, genera uno state_dict che contenga solo i parametri di LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Quando carichi un checkpoint utilizzando load_state_dict, assicurati di impostare strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Ora l'addestramento può procedere come di consueto.

**Iperparametri**

Definisci due dizionari: training_config e peft_config. training_config include iperparametri per l'addestramento, come il tasso di apprendimento, la dimensione del batch e le impostazioni di logging.

peft_config specifica parametri relativi a LoRA come rank, dropout e tipo di attività.

**Caricamento del Modello e del Tokenizer**

Specifica il percorso al modello pre-addestrato Phi-3 (ad esempio, "microsoft/Phi-3-mini-4k-instruct"). Configura le impostazioni del modello, inclusi l'uso della cache, il tipo di dato (bfloat16 per la precisione mista) e l'implementazione dell'attenzione.

**Addestramento**

Ottimizza il modello Phi-3 utilizzando il dataset personalizzato di istruzioni per chat. Utilizza le impostazioni LoRA da peft_config per un adattamento efficiente. Monitora i progressi dell'addestramento utilizzando la strategia di logging specificata.

**Valutazione e Salvataggio**

Valuta il modello ottimizzato. Salva i checkpoint durante l'addestramento per un utilizzo futuro.

**Esempi**
- [Scopri di più con questo notebook di esempio](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Esempio di script Python per l'ottimizzazione](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Esempio di ottimizzazione con Hugging Face Hub e LoRA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Esempio di scheda modello Hugging Face - Ottimizzazione con LoRA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Esempio di ottimizzazione con Hugging Face Hub e QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Disclaimer (Avvertenza):**  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.