# **Fine-tuning Phi-3 cu Lora**

Fine-tuning al modelului de limbaj Phi-3 Mini de la Microsoft folosind [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) pe un set de date personalizat pentru instrucțiuni de chat.

LoRA va ajuta la îmbunătățirea înțelegerii conversaționale și a generării de răspunsuri.

## Ghid pas cu pas pentru fine-tuning al Phi-3 Mini:

**Importuri și Configurare**

Instalarea loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Începeți prin a importa bibliotecile necesare, cum ar fi datasets, transformers, peft, trl și torch. Configurați logging-ul pentru a urmări procesul de antrenare.

Puteți alege să adaptați unele straturi înlocuindu-le cu variante implementate în loralib. În prezent, sunt suportate doar nn.Linear, nn.Embedding și nn.Conv2d. De asemenea, este suportat un MergedLinear pentru cazurile în care un singur nn.Linear reprezintă mai multe straturi, cum ar fi în unele implementări ale proiecției qkv din atenție (consultați Note Adiționale pentru mai multe detalii).

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

Înainte de a începe bucla de antrenare, marcați doar parametrii LoRA ca fiind antrenabili.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Când salvați un checkpoint, generați un state_dict care conține doar parametrii LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Când încărcați un checkpoint folosind load_state_dict, asigurați-vă că setați strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Acum, antrenarea poate continua în mod obișnuit.

**Hyperparametri**

Definiți două dicționare: training_config și peft_config. training_config include hyperparametri pentru antrenare, cum ar fi rata de învățare, mărimea batch-ului și setările de logging.

peft_config specifică parametrii legați de LoRA, cum ar fi rank, dropout și tipul de task.

**Încărcarea Modelului și Tokenizer-ului**

Specificați calea către modelul Phi-3 pre-antrenat (de exemplu, "microsoft/Phi-3-mini-4k-instruct"). Configurați setările modelului, inclusiv utilizarea cache-ului, tipul de date (bfloat16 pentru precizie mixtă) și implementarea atenției.

**Antrenare**

Realizați fine-tuning al modelului Phi-3 folosind setul de date personalizat pentru instrucțiuni de chat. Utilizați setările LoRA din peft_config pentru o adaptare eficientă. Monitorizați progresul antrenării folosind strategia de logging specificată.  
Evaluare și Salvare: Evaluați modelul fine-tuned.  
Salvați checkpoint-uri în timpul antrenării pentru utilizare ulterioară.

**Exemple**
- [Aflați mai multe cu acest notebook de exemplu](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exemplu de script Python pentru FineTuning](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Exemplu de Fine Tuning cu LORA pe Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Exemplu de Model Card Hugging Face - Fine Tuning cu LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Exemplu de Fine Tuning cu QLORA pe Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Declinări de responsabilitate**:  
Acest document a fost tradus folosind servicii de traducere bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa de autoritate. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.