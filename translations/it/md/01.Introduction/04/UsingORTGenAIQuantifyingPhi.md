## **Quantizzazione della famiglia Phi utilizzando le estensioni Generative AI per onnxruntime**

## **Cosa sono le estensioni Generative AI per onnxruntime**

Queste estensioni ti aiutano a eseguire l'IA generativa con ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Forniscono il ciclo generativo per i modelli ONNX, includendo inferenza con ONNX Runtime, elaborazione dei logits, ricerca e campionamento, e gestione della cache KV. Gli sviluppatori possono utilizzare un metodo di alto livello generate() o eseguire ogni iterazione del modello in un ciclo, generando un token alla volta, con la possibilità di aggiornare i parametri di generazione all'interno del ciclo. Supporta la ricerca greedy/beam e il campionamento TopP, TopK per generare sequenze di token, oltre a elaborazioni integrate dei logits come penalità per ripetizioni. È anche possibile aggiungere facilmente punteggi personalizzati.

A livello applicativo, puoi utilizzare le estensioni Generative AI per onnxruntime per costruire applicazioni usando C++/C#/Python. A livello di modello, puoi usarle per unire modelli fine-tuned e svolgere attività correlate alla distribuzione quantitativa.

## **Quantizzazione di Phi-3.5 con le estensioni Generative AI per onnxruntime**

### **Modelli supportati**

Le estensioni Generative AI per onnxruntime supportano la conversione quantizzata di Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Model Builder nelle estensioni Generative AI per onnxruntime**

Il Model Builder accelera notevolmente la creazione di modelli ONNX ottimizzati e quantizzati che funzionano con l'API generate() di ONNX Runtime.

Con Model Builder, puoi quantizzare il modello a INT4, INT8, FP16, FP32 e combinare diversi metodi di accelerazione hardware come CPU, CUDA, DirectML, Mobile, ecc.

Per utilizzare il Model Builder, è necessario installare

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Dopo l'installazione, puoi eseguire lo script Model Builder dal terminale per effettuare la conversione del formato del modello e la quantizzazione.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Comprendere i parametri rilevanti:

1. **model_name** Questo è il modello su Hugging Face, ad esempio microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, ecc. Può anche essere il percorso in cui memorizzi il modello.

2. **path_to_output_folder** Percorso di salvataggio della conversione quantizzata.

3. **execution_provider** Supporto per diverse accelerazioni hardware, come cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Scarichiamo il modello da Hugging Face e lo memorizziamo nella cache localmente.

***Nota:***

## **Come usare il Model Builder per quantizzare Phi-3.5**

Il Model Builder supporta ora la quantizzazione del modello ONNX per Phi-3.5 Instruct e Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Conversione quantizzata INT 4 accelerata dalla CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Conversione quantizzata INT 4 accelerata da CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Configura l'ambiente nel terminale:

```bash

mkdir models

cd models 

```

2. Scarica microsoft/Phi-3.5-vision-instruct nella cartella models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Scarica questi file nella tua cartella Phi-3.5-vision-instruct:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Scarica questo file nella cartella models:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Vai al terminale:  

   Converti il supporto ONNX con FP32.

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Nota:**

1. Il Model Builder supporta attualmente la conversione di Phi-3.5-Instruct e Phi-3.5-Vision, ma non Phi-3.5-MoE.

2. Per utilizzare il modello quantizzato di ONNX, puoi farlo tramite l'SDK delle estensioni Generative AI per onnxruntime.

3. È necessario considerare un'IA più responsabile, quindi dopo la conversione quantizzata del modello, si raccomanda di effettuare test più efficaci sui risultati.

4. Quantizzando il modello CPU INT4, possiamo distribuirlo su dispositivi Edge, che hanno scenari applicativi migliori. Per questo motivo, abbiamo completato Phi-3.5-Instruct con INT4.

## **Risorse**

1. Scopri di più sulle estensioni Generative AI per onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repository GitHub delle estensioni Generative AI per onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.