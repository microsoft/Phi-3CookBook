Phi-3-mini WebGPU RAG Chatbot

## Demo per mostrare WebGPU e il modello RAG
Il modello RAG con Phi-3 Onnx Hosted utilizza l'approccio Retrieval-Augmented Generation, combinando la potenza dei modelli Phi-3 con l'hosting ONNX per implementazioni AI efficienti. Questo modello è fondamentale per perfezionare i modelli per compiti specifici di settore, offrendo una combinazione di qualità, convenienza e comprensione di contesti lunghi. Fa parte della suite Azure AI, che fornisce una vasta selezione di modelli facili da trovare, provare e utilizzare, rispondendo alle esigenze di personalizzazione di vari settori. I modelli Phi-3, tra cui Phi-3-mini, Phi-3-small e Phi-3-medium, sono disponibili nel catalogo modelli di Azure AI e possono essere perfezionati e distribuiti autonomamente o tramite piattaforme come HuggingFace e ONNX, dimostrando l'impegno di Microsoft per soluzioni AI accessibili ed efficienti.

## Cos'è WebGPU
WebGPU è una moderna API grafica per il web progettata per fornire un accesso efficiente all'unità di elaborazione grafica (GPU) di un dispositivo direttamente dai browser. È destinata a essere il successore di WebGL, offrendo diversi miglioramenti chiave:

1. **Compatibilità con GPU moderne**: WebGPU è progettata per funzionare perfettamente con le architetture GPU contemporanee, sfruttando API di sistema come Vulkan, Metal e Direct3D 12.
2. **Prestazioni migliorate**: Supporta calcoli generici sulla GPU e operazioni più veloci, rendendola adatta sia per il rendering grafico che per i compiti di machine learning.
3. **Funzionalità avanzate**: WebGPU offre accesso a capacità GPU più avanzate, consentendo carichi di lavoro grafici e computazionali più complessi e dinamici.
4. **Riduzione del carico su JavaScript**: Delegando più compiti alla GPU, WebGPU riduce significativamente il carico su JavaScript, migliorando le prestazioni e garantendo esperienze più fluide.

WebGPU è attualmente supportata da browser come Google Chrome, con lavori in corso per estendere il supporto ad altre piattaforme.

### 03.WebGPU
Requisiti di ambiente:

**Browser supportati:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Abilitare WebGPU:

- In Chrome/Microsoft Edge 

Abilita il flag `chrome://flags/#enable-unsafe-webgpu`.

#### Apri il tuo browser:
Avvia Google Chrome o Microsoft Edge.

#### Accedi alla pagina Flags:
Nella barra degli indirizzi, digita `chrome://flags` e premi Invio.

#### Cerca il flag:
Nella barra di ricerca in alto, digita 'enable-unsafe-webgpu'.

#### Abilita il flag:
Trova il flag #enable-unsafe-webgpu nell'elenco dei risultati.

Clicca sul menu a discesa accanto e seleziona Enabled.

#### Riavvia il browser:

Dopo aver abilitato il flag, sarà necessario riavviare il browser affinché le modifiche abbiano effetto. Clicca sul pulsante Relaunch che appare in fondo alla pagina.

- Per Linux, avvia il browser con `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ha WebGPU abilitato di default.
- In Firefox Nightly, digita about:config nella barra degli indirizzi e `set dom.webgpu.enabled to true`.

### Configurare la GPU per Microsoft Edge 

Ecco i passaggi per configurare una GPU ad alte prestazioni per Microsoft Edge su Windows:

- **Apri Impostazioni:** Clicca sul menu Start e seleziona Impostazioni.
- **Impostazioni di sistema:** Vai su Sistema e poi su Schermo.
- **Impostazioni grafiche:** Scorri verso il basso e clicca su Impostazioni grafiche.
- **Scegli App:** Sotto "Scegli un'app per impostare la preferenza", seleziona App desktop e poi Sfoglia.
- **Seleziona Edge:** Naviga nella cartella di installazione di Edge (di solito `C:\Program Files (x86)\Microsoft\Edge\Application`) e seleziona `msedge.exe`.
- **Imposta preferenza:** Clicca su Opzioni, scegli Prestazioni elevate e poi clicca su Salva.
Questo assicurerà che Microsoft Edge utilizzi la tua GPU ad alte prestazioni per prestazioni migliori. 
- **Riavvia** il tuo computer affinché queste impostazioni abbiano effetto.

### Apri il tuo Codespace:
Vai al tuo repository su GitHub.
Clicca sul pulsante Code e seleziona Open with Codespaces.

Se non hai ancora un Codespace, puoi crearne uno cliccando su New codespace.

**Nota:** Installare l'ambiente Node nel tuo Codespace
Eseguire un demo npm da un Codespace di GitHub è un ottimo modo per testare e sviluppare il tuo progetto. Ecco una guida passo-passo per iniziare:

### Configura il tuo ambiente:
Una volta aperto il tuo Codespace, assicurati di avere Node.js e npm installati. Puoi verificarlo eseguendo:
```
node -v
```
```
npm -v
```

Se non sono installati, puoi installarli utilizzando:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Naviga nella directory del tuo progetto:
Usa il terminale per navigare nella directory in cui si trova il tuo progetto npm:
```
cd path/to/your/project
```

### Installa le dipendenze:
Esegui il seguente comando per installare tutte le dipendenze necessarie elencate nel tuo file package.json:

```
npm install
```

### Esegui il demo:
Una volta installate le dipendenze, puoi eseguire il tuo script demo. Questo è solitamente specificato nella sezione scripts del tuo package.json. Ad esempio, se il tuo script demo si chiama start, puoi eseguire:

```
npm run build
```
```
npm run dev
```

### Accedi al demo:
Se il tuo demo coinvolge un server web, Codespaces fornirà un URL per accedervi. Cerca una notifica o controlla la scheda Ports per trovare l'URL.

**Nota:** Il modello deve essere memorizzato nella cache nel browser, quindi potrebbe richiedere un po' di tempo per caricarsi.

### Demo RAG
Carica il file markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Seleziona il tuo file:
Clicca sul pulsante “Scegli file” per selezionare il documento che desideri caricare.

### Carica il documento:
Dopo aver selezionato il file, clicca sul pulsante “Carica” per caricare il documento per il RAG (Retrieval-Augmented Generation).

### Inizia la chat:
Una volta caricato il documento, puoi avviare una sessione di chat utilizzando RAG basato sul contenuto del tuo documento.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando servizi di traduzione automatizzati basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.