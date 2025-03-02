Questa demo mostra come utilizzare un modello preaddestrato per generare codice Python basato su un'immagine e un prompt testuale.

[Codice di esempio](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Ecco una spiegazione passo-passo:

1. **Importazioni e Configurazione**:
   - Vengono importate le librerie e i moduli necessari, inclusi `requests`, `PIL` per l'elaborazione delle immagini, e `transformers` per la gestione del modello e l'elaborazione.

2. **Caricamento e Visualizzazione dell'Immagine**:
   - Un file immagine (`demo.png`) viene aperto utilizzando la libreria `PIL` e visualizzato.

3. **Definizione del Prompt**:
   - Viene creato un messaggio che include l'immagine e una richiesta per generare codice Python per elaborare l'immagine e salvarla utilizzando `plt` (matplotlib).

4. **Caricamento del Processor**:
   - Il `AutoProcessor` viene caricato da un modello preaddestrato specificato nella directory `out_dir`. Questo processor gestirà gli input testuali e visivi.

5. **Creazione del Prompt**:
   - Il metodo `apply_chat_template` viene utilizzato per formattare il messaggio in un prompt adatto al modello.

6. **Elaborazione degli Input**:
   - Il prompt e l'immagine vengono trasformati in tensori comprensibili dal modello.

7. **Impostazione degli Argomenti di Generazione**:
   - Vengono definiti gli argomenti per il processo di generazione del modello, inclusi il numero massimo di nuovi token da generare e se campionare l'output.

8. **Generazione del Codice**:
   - Il modello genera il codice Python basandosi sugli input e sugli argomenti di generazione. Il `TextStreamer` viene utilizzato per gestire l'output, saltando il prompt e i token speciali.

9. **Output**:
   - Viene stampato il codice generato, che dovrebbe includere il codice Python per elaborare l'immagine e salvarla come specificato nel prompt.

Questa demo illustra come sfruttare un modello preaddestrato utilizzando OpenVino per generare codice in modo dinamico basandosi su input dell'utente e immagini.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati su intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.