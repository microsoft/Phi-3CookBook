### Scenario Esempio

Immagina di avere un'immagine (`demo.png`) e di voler generare codice Python che elabori questa immagine e salvi una nuova versione della stessa (`phi-3-vision.jpg`).

Il codice sopra automatizza questo processo attraverso:

1. Configurazione dell'ambiente e delle impostazioni necessarie.
2. Creazione di un prompt che istruisca il modello a generare il codice Python richiesto.
3. Invio del prompt al modello e raccolta del codice generato.
4. Estrazione ed esecuzione del codice generato.
5. Visualizzazione dell'immagine originale e di quella elaborata.

Questo approccio sfrutta la potenza dell'IA per automatizzare i compiti di elaborazione delle immagini, rendendo il tutto più semplice e veloce per raggiungere i tuoi obiettivi.

[Soluzione di Codice Esempio](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Analizziamo passo per passo cosa fa l'intero codice:

1. **Installare il Pacchetto Necessario**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Questo comando installa il pacchetto `langchain_nvidia_ai_endpoints`, assicurandosi che sia nella versione più recente.

2. **Importare i Moduli Necessari**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Questi import permettono di interagire con gli endpoint NVIDIA AI, gestire le password in modo sicuro, interagire con il sistema operativo e codificare/decodificare dati in formato base64.

3. **Configurare la Chiave API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Questo codice verifica se la variabile d'ambiente `NVIDIA_API_KEY` è impostata. In caso contrario, richiede all'utente di inserire la propria chiave API in modo sicuro.

4. **Definire il Modello e il Percorso dell'Immagine**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Qui viene definito il modello da utilizzare, viene creata un'istanza di `ChatNVIDIA` con il modello specificato e viene definito il percorso del file immagine.

5. **Creare un Prompt Testuale**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Questo codice definisce un prompt testuale che istruisce il modello a generare codice Python per l'elaborazione di un'immagine.

6. **Codificare l'Immagine in Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Questo codice legge il file immagine, lo codifica in base64 e crea un tag HTML dell'immagine con i dati codificati.

7. **Combinare Testo e Immagine nel Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    Questo passaggio combina il prompt testuale e il tag HTML dell'immagine in un'unica stringa.

8. **Generare Codice Utilizzando ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Questo codice invia il prompt a `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Estrarre il Codice Python dal Contenuto Generato**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Questo passaggio estrae il codice Python effettivo dal contenuto generato, rimuovendo la formattazione markdown.

10. **Eseguire il Codice Generato**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Questo codice esegue il codice Python estratto come un sottoprocesso e ne cattura l'output.

11. **Visualizzare le Immagini**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Queste righe visualizzano le immagini utilizzando il modulo `IPython.display`.

**Disclaimer (Avviso di responsabilità)**:  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati su intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.