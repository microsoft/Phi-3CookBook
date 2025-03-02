# Contributi

Questo progetto accoglie con favore contributi e suggerimenti. La maggior parte dei contributi richiede che tu accetti un Contributor License Agreement (CLA) dichiarando di avere il diritto di concederci i diritti di utilizzo del tuo contributo. Per i dettagli, visita [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Quando invii una pull request, un bot CLA determinerà automaticamente se è necessario fornire un CLA e aggiornerà la PR di conseguenza (ad esempio, con un controllo di stato o un commento). Segui semplicemente le istruzioni fornite dal bot. Dovrai farlo solo una volta per tutti i repository che utilizzano il nostro CLA.

## Codice di Condotta

Questo progetto ha adottato il [Codice di Condotta Open Source di Microsoft](https://opensource.microsoft.com/codeofconduct/).  
Per maggiori informazioni, leggi le [FAQ sul Codice di Condotta](https://opensource.microsoft.com/codeofconduct/faq/) o contatta [opencode@microsoft.com](mailto:opencode@microsoft.com) per eventuali domande o commenti aggiuntivi.

## Avvertenze per la creazione di issue

Ti preghiamo di non aprire issue su GitHub per domande di supporto generale, poiché l'elenco di GitHub dovrebbe essere utilizzato per richieste di funzionalità e segnalazioni di bug. In questo modo possiamo tracciare più facilmente i problemi o i bug reali nel codice e mantenere le discussioni generali separate dal codice effettivo.

## Come Contribuire

### Linee Guida per le Pull Request

Quando invii una pull request (PR) al repository Phi-3 CookBook, segui queste linee guida:

- **Effettua un fork del repository**: Esegui sempre un fork del repository sul tuo account personale prima di apportare modifiche.

- **Pull request separate (PR)**:
  - Invia ogni tipo di modifica in una pull request separata. Ad esempio, le correzioni di bug e gli aggiornamenti della documentazione dovrebbero essere inviati in PR distinte.
  - Correzioni di errori di battitura e aggiornamenti minori della documentazione possono essere combinati in una singola PR, se appropriato.

- **Gestisci i conflitti di merge**: Se la tua pull request mostra conflitti di merge, aggiorna il tuo branch locale `main` per rispecchiare il repository principale prima di apportare modifiche.

- **Invio di traduzioni**: Quando invii una PR di traduzione, assicurati che la cartella di traduzione includa le traduzioni di tutti i file presenti nella cartella originale.

### Linee Guida per le Traduzioni

> [!IMPORTANT]
>
> Quando traduci il testo in questo repository, non utilizzare traduzioni automatiche. Partecipa solo per le traduzioni in lingue in cui sei competente.

Se sei competente in una lingua diversa dall'inglese, puoi contribuire traducendo il contenuto. Per assicurarti che i tuoi contributi di traduzione siano integrati correttamente, segui queste linee guida:

- **Crea una cartella di traduzione**: Vai alla sezione appropriata e crea una cartella di traduzione per la lingua a cui stai contribuendo. Ad esempio:
  - Per la sezione di introduzione: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - Per la sezione di avvio rapido: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Continua questo schema per altre sezioni (03.Inference, 04.Finetuning, ecc.).

- **Aggiorna i percorsi relativi**: Durante la traduzione, modifica la struttura della cartella aggiungendo `../../` all'inizio dei percorsi relativi nei file markdown per garantire che i collegamenti funzionino correttamente. Ad esempio, cambia come segue:
  - Cambia `(../../imgs/01/phi3aisafety.png)` in `(../../../../imgs/01/phi3aisafety.png)`

- **Organizza le tue traduzioni**: Ogni file tradotto deve essere collocato nella cartella di traduzione della sezione corrispondente. Ad esempio, se stai traducendo la sezione di introduzione in spagnolo, devi creare quanto segue:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Invia una PR completa**: Assicurati che tutti i file tradotti per una sezione siano inclusi in una singola PR. Non accettiamo traduzioni parziali per una sezione. Quando invii una PR di traduzione, assicurati che la cartella di traduzione includa le traduzioni di tutti i file presenti nella cartella originale.

### Linee Guida di Scrittura

Per garantire coerenza tra tutti i documenti, segui queste linee guida:

- **Formattazione degli URL**: Racchiudi tutti gli URL tra parentesi quadre seguite da parentesi tonde, senza spazi aggiuntivi intorno o all'interno. Ad esempio: `[example](https://example.com)`.

- **Collegamenti relativi**: Usa `./` per i collegamenti relativi a file o cartelle nella directory corrente, e `../` per quelli in una directory padre. Ad esempio: `[example](../../path/to/file)` o `[example](../../../path/to/file)`.

- **Locali non specifici per paese**: Assicurati che i tuoi collegamenti non includano locali specifici per paese. Ad esempio, evita `/en-us/` o `/en/`.

- **Archiviazione delle immagini**: Archivia tutte le immagini nella cartella `./imgs`.

- **Nomi descrittivi per le immagini**: Dai alle immagini nomi descrittivi utilizzando caratteri inglesi, numeri e trattini. Ad esempio: `example-image.jpg`.

## Flussi di lavoro GitHub

Quando invii una pull request, i seguenti flussi di lavoro verranno attivati per convalidare le modifiche. Segui le istruzioni seguenti per assicurarti che la tua pull request superi i controlli del flusso di lavoro:

- [Controlla percorsi relativi non funzionanti](../..)
- [Controlla che gli URL non abbiano locali](../..)

### Controlla percorsi relativi non funzionanti

Questo flusso di lavoro garantisce che tutti i percorsi relativi nei tuoi file siano corretti.

1. Per assicurarti che i tuoi collegamenti funzionino correttamente, esegui le seguenti operazioni utilizzando VS Code:
    - Passa il mouse sopra un collegamento nei tuoi file.
    - Premi **Ctrl + Click** per navigare nel collegamento.
    - Se fai clic su un collegamento e questo non funziona localmente, attiverà il flusso di lavoro e non funzionerà su GitHub.

1. Per risolvere questo problema, esegui le seguenti operazioni utilizzando i suggerimenti di percorso forniti da VS Code:
    - Digita `./` o `../`.
    - VS Code ti suggerirà opzioni basate su ciò che hai digitato.
    - Segui il percorso facendo clic sul file o sulla cartella desiderata per assicurarti che il percorso sia corretto.

Una volta aggiunto il percorso relativo corretto, salva e invia le modifiche.

### Controlla che gli URL non abbiano locali

Questo flusso di lavoro garantisce che nessun URL web includa un locale specifico per paese. Poiché questo repository è accessibile globalmente, è importante garantire che gli URL non contengano il locale del tuo paese.

1. Per verificare che i tuoi URL non abbiano locali specifici per paese, esegui le seguenti operazioni:

    - Controlla la presenza di testo come `/en-us/`, `/en/` o qualsiasi altro locale linguistico negli URL.
    - Se questi non sono presenti nei tuoi URL, supererai questo controllo.

1. Per risolvere questo problema, esegui le seguenti operazioni:
    - Apri il percorso del file evidenziato dal flusso di lavoro.
    - Rimuovi il locale specifico per paese dagli URL.

Una volta rimosso il locale, salva e invia le modifiche.

### Controlla URL non funzionanti

Questo flusso di lavoro garantisce che qualsiasi URL web nei tuoi file funzioni e restituisca un codice di stato 200.

1. Per verificare che i tuoi URL funzionino correttamente, esegui le seguenti operazioni:
    - Controlla lo stato degli URL nei tuoi file.

2. Per correggere eventuali URL non funzionanti, esegui le seguenti operazioni:
    - Apri il file che contiene l'URL non funzionante.
    - Aggiorna l'URL con quello corretto.

Una volta corretti gli URL, salva e invia le modifiche.

> [!NOTE]
>
> Potrebbero esserci casi in cui il controllo degli URL fallisce anche se il collegamento è accessibile. Questo può accadere per diversi motivi, tra cui:
>
> - **Restrizioni di rete:** I server delle azioni GitHub potrebbero avere restrizioni di rete che impediscono l'accesso a determinati URL.
> - **Problemi di timeout:** Gli URL che impiegano troppo tempo a rispondere possono attivare un errore di timeout nel flusso di lavoro.
> - **Problemi temporanei del server:** Occasionale downtime del server o manutenzione possono rendere un URL temporaneamente non disponibile durante la validazione.

**Disclaimer (Avvertenza):**  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati su intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua madre deve essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.