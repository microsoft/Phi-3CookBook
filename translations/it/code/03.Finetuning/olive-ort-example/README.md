# Ottimizzare Phi3 con Olive

In questo esempio utilizzerai Olive per:

1. Ottimizzare un adattatore LoRA per classificare frasi in Sad, Joy, Fear, Surprise.
1. Unire i pesi dell'adattatore al modello base.
1. Ottimizzare e quantizzare il modello in `int4`.

Ti mostreremo anche come eseguire inferenze con il modello ottimizzato utilizzando l'API Generate di ONNX Runtime (ORT).

> **⚠️ Per l'ottimizzazione, è necessario disporre di una GPU adeguata, ad esempio una A10, V100, A100.**

## 💾 Installazione

Crea un nuovo ambiente virtuale Python (ad esempio, utilizzando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Successivamente, installa Olive e le dipendenze necessarie per il flusso di lavoro di ottimizzazione:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ottimizzare Phi3 con Olive
Il [file di configurazione di Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) contiene un *workflow* con i seguenti *passaggi*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

A livello generale, questo workflow:

1. Ottimizza Phi3 (per 150 passaggi, modificabili) utilizzando i dati di [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Unisce i pesi dell'adattatore LoRA al modello base. Questo produce un unico artefatto del modello in formato ONNX.
1. Il Model Builder ottimizzerà il modello per ONNX Runtime *e* lo quantizzerà in `int4`.

Per eseguire il workflow, utilizza il comando:

```bash
olive run --config phrase-classification.json
```

Al termine di Olive, il modello Phi3 ottimizzato e quantizzato in `int4` sarà disponibile in: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrare Phi3 ottimizzato nella tua applicazione

Per eseguire l'app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

La risposta dovrebbe essere una classificazione a singola parola della frase (Sad/Joy/Fear/Surprise).

**Disclaimer (Avvertenza)**:  
Questo documento è stato tradotto utilizzando servizi di traduzione automatizzati basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.