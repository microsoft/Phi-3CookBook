# Chatbot Interattivo Phi 3 Mini 4K Instruct con Whisper

## Panoramica

Il Chatbot Interattivo Phi 3 Mini 4K Instruct è uno strumento che consente agli utenti di interagire con la demo Microsoft Phi 3 Mini 4K Instruct utilizzando input testuali o vocali. Il chatbot può essere utilizzato per una varietà di attività, come traduzioni, aggiornamenti meteo e raccolta di informazioni generali.

### Per iniziare

Per utilizzare questo chatbot, segui semplicemente queste istruzioni:

1. Apri un nuovo [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb).
2. Nella finestra principale del notebook, vedrai un'interfaccia con una casella di testo e un pulsante "Send".
3. Per utilizzare il chatbot testuale, scrivi il tuo messaggio nella casella di testo e clicca sul pulsante "Send". Il chatbot risponderà con un file audio che potrà essere riprodotto direttamente dal notebook.

**Nota**: Questo strumento richiede una GPU e l'accesso ai modelli Microsoft Phi-3 e OpenAI Whisper, utilizzati per il riconoscimento vocale e la traduzione.

### Requisiti GPU

Per eseguire questa demo è necessaria una GPU con almeno 12 GB di memoria.

I requisiti di memoria per eseguire la demo **Microsoft-Phi-3-Mini-4K Instruct** su una GPU dipendono da diversi fattori, come la dimensione dei dati in input (audio o testo), la lingua utilizzata per la traduzione, la velocità del modello e la memoria disponibile sulla GPU.

In generale, il modello Whisper è progettato per funzionare su GPU. La quantità minima raccomandata di memoria GPU per eseguire il modello Whisper è di 8 GB, ma può gestire quantità maggiori di memoria, se necessario.

È importante notare che l'elaborazione di grandi quantità di dati o un elevato volume di richieste potrebbe richiedere più memoria GPU e/o causare problemi di prestazioni. Si consiglia di testare il proprio caso d'uso con configurazioni diverse e monitorare l'utilizzo della memoria per determinare le impostazioni ottimali per le proprie esigenze specifiche.

## Esempio E2E per Chatbot Interattivo Phi 3 Mini 4K Instruct con Whisper

Il notebook Jupyter intitolato [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) dimostra come utilizzare la demo Microsoft Phi 3 Mini 4K Instruct per generare testo a partire da input audio o testuali. Il notebook definisce diverse funzioni:

1. `tts_file_name(text)`: Questa funzione genera un nome file basato sul testo in input per salvare il file audio generato.
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Questa funzione utilizza l'API Edge TTS per generare un file audio da una lista di segmenti di testo in input. I parametri in input includono la lista di segmenti, la velocità del parlato, il nome della voce e il percorso di output per salvare il file audio generato.
3. `talk(input_text)`: Questa funzione genera un file audio utilizzando l'API Edge TTS e lo salva con un nome casuale nella directory /content/audio. Il parametro in input è il testo da convertire in parlato.
4. `run_text_prompt(message, chat_history)`: Questa funzione utilizza la demo Microsoft Phi 3 Mini 4K Instruct per generare un file audio da un messaggio in input e lo aggiunge alla cronologia della chat.
5. `run_audio_prompt(audio, chat_history)`: Questa funzione converte un file audio in testo utilizzando l'API del modello Whisper e lo passa alla funzione `run_text_prompt()`.
6. Il codice avvia un'app Gradio che consente agli utenti di interagire con la demo Phi 3 Mini 4K Instruct digitando messaggi o caricando file audio. L'output viene mostrato come messaggio di testo all'interno dell'app.

## Risoluzione dei problemi

Installazione dei driver GPU Cuda

1. Assicurati che le applicazioni Linux siano aggiornate.

    ```bash
    sudo apt update
    ```

2. Installa i driver Cuda.

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. Registra la posizione del driver Cuda.

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. Controlla la dimensione della memoria GPU Nvidia (richiesti 12 GB di memoria GPU).

    ```bash
    nvidia-smi
    ```

5. Svuota la cache: Se stai usando PyTorch, puoi chiamare torch.cuda.empty_cache() per rilasciare tutta la memoria inutilizzata nella cache, rendendola disponibile per altre applicazioni GPU.

    ```python
    torch.cuda.empty_cache() 
    ```

6. Controlla Cuda Nvidia.

    ```bash
    nvcc --version
    ```

7. Esegui le seguenti operazioni per creare un token Hugging Face.

    - Vai alla [pagina delle impostazioni dei token di Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Seleziona **Nuovo token**.
    - Inserisci il **Nome** del progetto che desideri utilizzare.
    - Seleziona il **Tipo** come **Scrittura**.

> **Nota**
>
> Se incontri il seguente errore:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Per risolverlo, digita il seguente comando nel terminale:
>
> ```bash
> sudo ldconfig
> ```

**Disclaimer (Avvertenza):**  
Questo documento è stato tradotto utilizzando servizi di traduzione automatizzati basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale eseguita da un umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.