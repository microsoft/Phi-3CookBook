# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo per mostrare WebGPU e il modello RAG

Il modello RAG con Phi-3.5 Onnx Hosted sfrutta l'approccio Retrieval-Augmented Generation, combinando la potenza dei modelli Phi-3.5 con l'hosting ONNX per implementazioni AI efficienti. Questo modello è fondamentale per perfezionare i modelli per attività specifiche di settore, offrendo un mix di qualità, convenienza e comprensione di contesti più lunghi. Fa parte della suite Azure AI, che offre una vasta selezione di modelli facili da trovare, provare e utilizzare, soddisfacendo le esigenze di personalizzazione di vari settori.

## Cos'è WebGPU 
WebGPU è un'API grafica web moderna progettata per fornire accesso efficiente all'unità di elaborazione grafica (GPU) di un dispositivo direttamente dai browser web. È destinata a essere il successore di WebGL, offrendo diversi miglioramenti chiave:

1. **Compatibilità con GPU moderne**: WebGPU è progettato per funzionare perfettamente con le architetture GPU contemporanee, sfruttando API di sistema come Vulkan, Metal e Direct3D 12.
2. **Prestazioni migliorate**: Supporta calcoli generici sulla GPU e operazioni più veloci, rendendolo adatto sia al rendering grafico che ai compiti di apprendimento automatico.
3. **Funzionalità avanzate**: WebGPU offre accesso a capacità GPU più avanzate, consentendo carichi di lavoro grafici e computazionali più complessi e dinamici.
4. **Riduzione del carico di lavoro JavaScript**: Delegando più compiti alla GPU, WebGPU riduce significativamente il carico di lavoro su JavaScript, migliorando le prestazioni e offrendo esperienze più fluide.

WebGPU è attualmente supportato in browser come Google Chrome, con lavori in corso per espandere il supporto ad altre piattaforme.

### 03.WebGPU
Requisiti dell'ambiente:

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
Nella casella di ricerca in alto nella pagina, digita 'enable-unsafe-webgpu'.

#### Abilita il flag:
Trova il flag #enable-unsafe-webgpu nell'elenco dei risultati.

Clicca sul menu a tendina accanto e seleziona Enabled.

#### Riavvia il tuo browser:

Dopo aver abilitato il flag, sarà necessario riavviare il browser affinché le modifiche abbiano effetto. Clicca sul pulsante Rilancia che appare in basso nella pagina.

- Per Linux, avvia il browser con `--enable-features=Vulkan`.
- Safari 18 (macOS 15) ha WebGPU abilitato di default.
- In Firefox Nightly, inserisci about:config nella barra degli indirizzi e `set dom.webgpu.enabled to true`.

### Configurare la GPU per Microsoft Edge 

Ecco i passaggi per configurare una GPU ad alte prestazioni per Microsoft Edge su Windows:

- **Apri Impostazioni:** Clicca sul menu Start e seleziona Impostazioni.
- **Impostazioni di sistema:** Vai su Sistema e poi su Schermo.
- **Impostazioni grafiche:** Scorri verso il basso e clicca su Impostazioni grafiche.
- **Scegli App:** Sotto “Scegli un'app per impostare la preferenza,” seleziona App desktop e poi Sfoglia.
- **Seleziona Edge:** Vai alla cartella di installazione di Edge (di solito `C:\Program Files (x86)\Microsoft\Edge\Application`) e seleziona `msedge.exe`.
- **Imposta Preferenza:** Clicca su Opzioni, scegli Alte prestazioni, e poi clicca su Salva.
Questo garantirà che Microsoft Edge utilizzi la tua GPU ad alte prestazioni per migliori prestazioni. 
- **Riavvia** il tuo dispositivo per applicare queste impostazioni.

### Esempi: Per favore [clicca su questo link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Disclaimer (Avvertenza)**:  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati su intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale effettuata da un umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.