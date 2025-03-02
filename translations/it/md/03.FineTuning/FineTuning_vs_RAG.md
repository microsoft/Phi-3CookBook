## Affinamento vs RAG

## Generazione Arricchita da Recupero (RAG)

RAG combina il recupero di dati con la generazione di testo. I dati strutturati e non strutturati dell'azienda vengono memorizzati nel database vettoriale. Durante la ricerca di contenuti rilevanti, vengono trovati il riassunto e i contenuti pertinenti per formare un contesto, e la capacità di completamento testuale di LLM/SLM viene utilizzata per generare contenuti.

## Processo RAG
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.it.png)

## Affinamento
L'affinamento si basa sul miglioramento di un modello esistente. Non è necessario partire dall'algoritmo del modello, ma è fondamentale accumulare continuamente dati. Se si desiderano terminologie e modalità di espressione linguistica più precise per applicazioni industriali, l'affinamento è la scelta migliore. Tuttavia, se i dati cambiano frequentemente, l'affinamento può diventare complesso.

## Come scegliere
Se la nostra risposta richiede l'introduzione di dati esterni, RAG è la scelta migliore.

Se è necessario fornire conoscenze industriali stabili e precise, l'affinamento sarà una buona scelta. RAG dà priorità al recupero di contenuti pertinenti, ma potrebbe non cogliere sempre le sfumature specialistiche.

L'affinamento richiede un set di dati di alta qualità e, se si tratta solo di una piccola quantità di dati, non farà molta differenza. RAG è più flessibile.  
L'affinamento è una sorta di "scatola nera", una metafisica, ed è difficile comprendere il meccanismo interno. Tuttavia, RAG consente di individuare più facilmente la fonte dei dati, correggendo in modo efficace allucinazioni o errori nei contenuti e offrendo maggiore trasparenza.

**Disclaimer (Avvertenza):**  
Questo documento è stato tradotto utilizzando servizi di traduzione automatizzati basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.