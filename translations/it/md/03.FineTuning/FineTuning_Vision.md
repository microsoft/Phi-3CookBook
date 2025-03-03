# Ricetta per il fine-tuning di Phi-3.5-vision

Questo è il supporto ufficiale per il fine-tuning di Phi-3.5-vision utilizzando le librerie di huggingface.  
Si prega di `cd` nella directory del codice [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) prima di eseguire i seguenti comandi.

## Installazione

```bash
# create a new conda environment
conda create -n phi3v python=3.10
conda activate phi3v

# install pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# other libraries needed to run the example code
pip install -r requirements.txt

# (optional) flash attention -- Ampere+ GPUs (e.g., A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (optional) QLoRA -- Turing+ GPUs (e.g., RTX 8000)
pip install bitsandbytes==0.43.1
```

## Guida rapida

Forniamo due script di esempio per il fine-tuning: uno per DocVQA e uno per la classificazione dei meme offensivi.  

Hardware minimo testato: 4x RTX8000 (48GB di RAM per GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ora supporta ufficialmente input con immagini multiple. Ecco un esempio per il fine-tuning di NLVR2:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Guida all'uso

A seconda dell'hardware, gli utenti possono scegliere diverse strategie di fine-tuning. Supportiamo il fine-tuning completo (con Deepspeed Zero-2) con parametri visivi eventualmente congelati, e LoRA (incluso QLoRA a 4 bit).  
In generale, consigliamo di utilizzare il fine-tuning completo con flash attention e bf16 quando possibile.

### Guida per convertire il tuo dataset personalizzato nel formato richiesto

Utilizziamo un dataset minimo per la classificazione video (un sottoinsieme di UCF-101) come esempio end-to-end per dimostrare come convertire il tuo dataset personalizzato nel formato richiesto e fare il fine-tuning di Phi-3.5-vision su di esso.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

I dati convertiti avranno questo aspetto:

```bash
> tree --filelimit=10 /path/to/converted_ucf101
/path/to/converted_ucf101
├── images
│   ├── test
│   │   ├── ApplyEyeMakeup [48 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [32 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [56 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [72 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [32 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [72 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [80 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [88 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [48 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [72 entries exceeds filelimit, not opening dir]
│   ├── train
│   │   ├── ApplyEyeMakeup [240 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [240 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [240 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [240 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [240 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [240 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [240 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [240 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [240 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [240 entries exceeds filelimit, not opening dir]
│   └── val
│       ├── ApplyEyeMakeup [24 entries exceeds filelimit, not opening dir]
│       ├── ApplyLipstick [24 entries exceeds filelimit, not opening dir]
│       ├── Archery [24 entries exceeds filelimit, not opening dir]
│       ├── BabyCrawling [24 entries exceeds filelimit, not opening dir]
│       ├── BalanceBeam [24 entries exceeds filelimit, not opening dir]
│       ├── BandMarching [24 entries exceeds filelimit, not opening dir]
│       ├── BaseballPitch [24 entries exceeds filelimit, not opening dir]
│       ├── Basketball [24 entries exceeds filelimit, not opening dir]
│       ├── BasketballDunk [24 entries exceeds filelimit, not opening dir]
│       └── BenchPress [24 entries exceeds filelimit, not opening dir]
├── ucf101_test.jsonl
├── ucf101_train.jsonl
└── ucf101_val.jsonl

34 directories, 3 files
```

Per l'annotazione `jsonl`, ogni riga dovrebbe essere un dizionario simile a:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Nota che `conversations` è una lista, quindi è possibile supportare conversazioni multi-turno se tali dati sono disponibili.

## Richiedere una quota GPU su Azure 

### Prerequisiti

Un account Azure con il ruolo di Contributor (o un altro ruolo che include l'accesso come Contributor).  

Se non hai un account Azure, crea un [account gratuito prima di iniziare](https://azure.microsoft.com).

### Richiedere un aumento della quota

Puoi inviare una richiesta di aumento della quota direttamente da My quotas. Segui i passaggi seguenti per richiedere un aumento per una quota. Per questo esempio, puoi selezionare qualsiasi quota regolabile nella tua sottoscrizione.

Accedi al [portale di Azure](https://portal.azure.com).

Inserisci "quotas" nella barra di ricerca e seleziona Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Nella pagina Panoramica, seleziona un provider, ad esempio Compute o AML.

**Nota** Per tutti i provider diversi da Compute, vedrai una colonna Richiedi aumento invece della colonna Regolabile descritta sotto. Qui, puoi richiedere un aumento per una quota specifica o creare una richiesta di supporto per l'aumento.

Nella pagina My quotas, sotto Nome quota, seleziona la quota che desideri aumentare. Assicurati che la colonna Regolabile mostri Sì per questa quota.

Nella parte superiore della pagina, seleziona Nuova richiesta di quota, quindi seleziona Inserisci un nuovo limite.  
![Aumenta Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Nel pannello Nuova richiesta di quota, inserisci un valore numerico per il tuo nuovo limite di quota, quindi seleziona Invia.

La tua richiesta sarà esaminata e sarai notificato se può essere soddisfatta. Questo di solito avviene entro pochi minuti.

Se la tua richiesta non viene soddisfatta, vedrai un link per creare una richiesta di supporto. Quando utilizzi questo link, un ingegnere del supporto ti assisterà con la tua richiesta di aumento.

## Suggerimenti per SKU di macchine GPU Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)  

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)  

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)  

Ecco alcuni esempi:

### Se hai GPU A100 o H100

Il fine-tuning completo di solito offre le migliori prestazioni. Puoi usare il seguente comando per fare il fine-tuning di Phi-3-V per la classificazione dei meme offensivi.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Se hai GPU Standard_ND40rs_v2 8x V100-32GB

È ancora possibile fare il fine-tuning completo di Phi-3-V per la classificazione dei meme offensivi. Tuttavia, aspettati una velocità molto inferiore rispetto alle GPU A100 o H100 a causa della mancanza di supporto per la flash attention.  
La precisione potrebbe anche essere influenzata a causa della mancanza di supporto per bf16 (viene invece utilizzato l'addestramento a precisione mista fp16).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Se non hai accesso a GPU per data center
Lora potrebbe essere la tua unica scelta. Puoi usare il seguente comando per fare il fine-tuning di Phi-3-V per la classificazione dei meme offensivi.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Per GPU Turing+ è supportato QLoRA.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Iperparametri suggeriti e precisione attesa
### NLVR2

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_nlvr2.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Metodo di addestramento | Modello visivo congelato | Tipo di dato | LoRA rank | LoRA alpha | Dimensione batch | Learning rate | Epochs | Precisione
--- | --- | --- | --- | --- | --- | --- | --- | --- |
fine-tuning completo |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
fine-tuning completo | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
Risultati LoRA in arrivo |  |  |  |  |  |  |  |  |

### NOTA
I risultati di seguito per DocVQA e Hateful memes si basano sulla versione precedente (Phi-3-vision).  
I nuovi risultati con Phi-3.5-vision saranno aggiornati a breve.

### DocVQA (NOTA: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_docvqa.py \
  --full_train \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Metodo di addestramento | Tipo di dato | LoRA rank | LoRA alpha | Dimensione batch | Learning rate | Epochs | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
fine-tuning completo | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
fine-tuning completo | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
modello immagine congelato | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
modello immagine congelato | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (NOTA: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Metodo di addestramento | Tipo di dato | LoRA rank | LoRA alpha | Dimensione batch | Learning rate | Epochs | Precisione
--- | --- | --- | --- | --- | --- | --- | --- |
fine-tuning completo | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
fine-tuning completo | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
modello immagine congelato | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
modello immagine congelato | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Benchmarking delle prestazioni (NOTA: Phi-3-vision)

I nuovi risultati di benchmarking con Phi-3.5-vision saranno aggiornati a breve.

Il benchmarking delle prestazioni è stato effettuato sul dataset DocVQA. La lunghezza media delle sequenze in questo dataset è di 2443.23 token (utilizzando `num_crops=16` per il modello immagine).

### 8x A100-80GB (Ampere)

Metodo di addestramento | \# nodi | GPU | flash attention | Dimensione batch effettiva | Throughput (img/s) | Speedup | Memoria GPU di picco (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
fine-tuning completo | 1 | 8 |  | 64 | 5.041 | 1x | ~42
fine-tuning completo | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
fine-tuning completo | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
fine-tuning completo | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
modello immagine congelato | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
modello immagine congelato | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Metodo di addestramento | \# nodi | GPU | flash attention | Dimensione batch effettiva | Throughput (img/s) | Speedup | Memoria GPU di picco (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
fine-tuning completo | 1 | 8 | | 64 | 2.462 | 1x | ~32
fine-tuning completo | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
fine-tuning completo | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
modello immagine congelato | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Problemi noti

- Non è possibile eseguire flash attention con fp16 (bf16 è sempre consigliato quando disponibile, e tutte le GPU che supportano flash attention supportano anche bf16).  
- Non è ancora supportato il salvataggio di checkpoint intermedi e la ripresa dell'addestramento.

**Disclaimer (Avvertenza)**:  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.