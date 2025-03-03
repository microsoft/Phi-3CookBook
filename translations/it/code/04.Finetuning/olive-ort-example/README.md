# Affinare Phi3 utilizzando Olive

In questo esempio utilizzerai Olive per:

1. Affinare un adattatore LoRA per classificare frasi in Tristezza, Gioia, Paura, Sorpresa.
1. Unire i pesi dell'adattatore nel modello di base.
1. Ottimizzare e quantizzare il modello in `int4`.

Ti mostreremo anche come eseguire inferenze con il modello affinato utilizzando l'API Generate di ONNX Runtime (ORT).

> **⚠️ Per l'affinamento, è necessario disporre di una GPU adatta - ad esempio, una A10, V100, A100.**

## 💾 Installazione

Crea un nuovo ambiente virtuale Python (ad esempio, utilizzando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Successivamente, installa Olive e le dipendenze necessarie per un flusso di lavoro di affinamento:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Affinare Phi3 utilizzando Olive
Il [file di configurazione di Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) contiene un *workflow* con i seguenti *passaggi*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

A un livello generale, questo workflow eseguirà:

1. L'affinamento di Phi3 (per 150 step, modificabili) utilizzando i dati presenti in [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. La fusione dei pesi dell'adattatore LoRA nel modello di base. Questo produrrà un unico artefatto del modello in formato ONNX.
1. Il Model Builder ottimizzerà il modello per ONNX Runtime *e* quantizzerà il modello in `int4`.

Per eseguire il workflow, utilizza:

```bash
olive run --config phrase-classification.json
```

Quando Olive avrà terminato, il tuo modello Phi3 ottimizzato e affinato in `int4` sarà disponibile in: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrare Phi3 affinato nella tua applicazione 

Per eseguire l'applicazione:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

La risposta dovrebbe essere una classificazione a singola parola della frase (Tristezza/Gioia/Paura/Sorpresa).

**Disclaimer (Avvertenza):**  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati su intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.