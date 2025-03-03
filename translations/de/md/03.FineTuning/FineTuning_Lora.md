# **Feinabstimmung von Phi-3 mit Lora**

Feinabstimmung des Microsoft Phi-3 Mini Sprachmodells mit [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) auf einem benutzerdefinierten Chat-Instruktionsdatensatz.

LoRA hilft dabei, das Verständnis für Konversationen und die Generierung von Antworten zu verbessern.

## Schritt-für-Schritt-Anleitung zur Feinabstimmung von Phi-3 Mini:

**Imports und Einrichtung**

Installation von loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Beginnen Sie mit dem Import der benötigten Bibliotheken wie datasets, transformers, peft, trl und torch.  
Richten Sie ein Logging ein, um den Trainingsprozess zu verfolgen.

Sie können einige Schichten anpassen, indem Sie sie durch Gegenstücke ersetzen, die in loralib implementiert sind. Aktuell unterstützen wir nn.Linear, nn.Embedding und nn.Conv2d. Außerdem unterstützen wir einen MergedLinear für Fälle, in denen ein einzelnes nn.Linear mehr als eine Schicht repräsentiert, wie es bei einigen Implementierungen der Attention qkv-Projektion der Fall ist (siehe Zusätzliche Hinweise für weitere Informationen).

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

Markieren Sie vor Beginn der Trainingsschleife nur die LoRA-Parameter als trainierbar.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Beim Speichern eines Checkpoints wird ein state_dict generiert, das nur die LoRA-Parameter enthält.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Beim Laden eines Checkpoints mit load_state_dict sollten Sie sicherstellen, dass strict=False gesetzt ist.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Jetzt kann das Training wie gewohnt fortgesetzt werden.

**Hyperparameter**

Definieren Sie zwei Dictionaries: training_config und peft_config.  
training_config enthält Hyperparameter für das Training, wie Lernrate, Batch-Größe und Logging-Einstellungen.

peft_config spezifiziert LoRA-bezogene Parameter wie Rank, Dropout und Aufgabentyp.

**Laden von Modell und Tokenizer**

Geben Sie den Pfad zum vortrainierten Phi-3-Modell an (z. B. "microsoft/Phi-3-mini-4k-instruct").  
Konfigurieren Sie die Modelleinstellungen, einschließlich Cache-Nutzung, Datentyp (bfloat16 für gemischte Präzision) und Attention-Implementierung.

**Training**

Feinabstimmung des Phi-3-Modells mithilfe des benutzerdefinierten Chat-Instruktionsdatensatzes.  
Nutzen Sie die LoRA-Einstellungen aus peft_config für eine effiziente Anpassung.  
Überwachen Sie den Trainingsfortschritt mit der angegebenen Logging-Strategie.  

**Auswertung und Speicherung**  
Bewerten Sie das feinabgestimmte Modell.  
Speichern Sie Checkpoints während des Trainings zur späteren Verwendung.

**Beispiele**  
- [Erfahren Sie mehr mit diesem Beispiel-Notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Beispiel eines Python-Feinabstimmungsskripts](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Beispiel für Feinabstimmung mit LORA auf Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Beispiel einer Hugging Face Model Card - LORA-Feinabstimmung](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Beispiel für Feinabstimmung mit QLORA auf Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)  

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung resultieren.