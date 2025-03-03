# Chatbot Interactiv Phi 3 Mini 4K Instruct cu Whisper

## Prezentare generală

Chatbot-ul Interactiv Phi 3 Mini 4K Instruct este un instrument care permite utilizatorilor să interacționeze cu demo-ul Microsoft Phi 3 Mini 4K instruct folosind input text sau audio. Chatbot-ul poate fi utilizat pentru diverse sarcini, cum ar fi traducerea, actualizările meteo și colectarea de informații generale.

### Început rapid

Pentru a utiliza acest chatbot, urmați aceste instrucțiuni:

1. Deschideți un nou [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. În fereastra principală a notebook-ului, veți vedea o interfață de chat cu o casetă de input text și un buton "Send".
3. Pentru a utiliza chatbot-ul bazat pe text, introduceți pur și simplu mesajul în caseta de input text și apăsați butonul "Send". Chatbot-ul va răspunde cu un fișier audio care poate fi redat direct din notebook.

**Notă**: Acest instrument necesită un GPU și acces la modelele Microsoft Phi-3 și OpenAI Whisper, care sunt utilizate pentru recunoaștere vocală și traducere.

### Cerințe GPU

Pentru a rula acest demo, aveți nevoie de 12 GB de memorie GPU.

Cerințele de memorie pentru rularea demo-ului **Microsoft-Phi-3-Mini-4K instruct** pe un GPU depind de mai mulți factori, cum ar fi dimensiunea datelor de intrare (audio sau text), limba utilizată pentru traducere, viteza modelului și memoria disponibilă pe GPU.

În general, modelul Whisper este conceput pentru a rula pe GPU-uri. Cantitatea minimă recomandată de memorie GPU pentru rularea modelului Whisper este de 8 GB, dar poate gestiona cantități mai mari de memorie, dacă este necesar.

Este important de menționat că rularea unui volum mare de date sau a unui număr mare de cereri pe model poate necesita mai multă memorie GPU și/sau poate cauza probleme de performanță. Este recomandat să testați cazul dumneavoastră de utilizare cu diferite configurații și să monitorizați utilizarea memoriei pentru a determina setările optime pentru nevoile specifice.

## Exemplu E2E pentru Chatbot-ul Interactiv Phi 3 Mini 4K Instruct cu Whisper

Notebook-ul jupyter intitulat [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstrează cum să utilizați demo-ul Microsoft Phi 3 Mini 4K instruct pentru a genera text din input audio sau text scris. Notebook-ul definește mai multe funcții:

1. `tts_file_name(text)`: Această funcție generează un nume de fișier bazat pe textul de intrare pentru salvarea fișierului audio generat.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Această funcție utilizează Edge TTS API pentru a genera un fișier audio dintr-o listă de segmente de text de intrare. Parametrii de intrare sunt lista de segmente, viteza vorbirii, numele vocii și calea de ieșire pentru salvarea fișierului audio generat.
1. `talk(input_text)`: Această funcție generează un fișier audio folosind Edge TTS API și îl salvează cu un nume de fișier aleatoriu în directorul /content/audio. Parametrul de intrare este textul care trebuie convertit în vorbire.
1. `run_text_prompt(message, chat_history)`: Această funcție utilizează demo-ul Microsoft Phi 3 Mini 4K instruct pentru a genera un fișier audio dintr-un mesaj de intrare și îl adaugă la istoricul conversației.
1. `run_audio_prompt(audio, chat_history)`: Această funcție convertește un fișier audio în text utilizând Whisper model API și îl transmite funcției `run_text_prompt()`.
1. Codul lansează o aplicație Gradio care permite utilizatorilor să interacționeze cu demo-ul Phi 3 Mini 4K instruct fie tastând mesaje, fie încărcând fișiere audio. Rezultatul este afișat ca mesaj text în cadrul aplicației.

## Depanare

Instalarea driverelor GPU Cuda

1. Asigurați-vă că aplicațiile Linux sunt actualizate

    ```bash
    sudo apt update
    ```

1. Instalați driverele Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Înregistrați locația driverului Cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Verificați dimensiunea memoriei GPU Nvidia (Necesar 12GB de memorie GPU)

    ```bash
    nvidia-smi
    ```

1. Goliți memoria cache: Dacă utilizați PyTorch, puteți apela torch.cuda.empty_cache() pentru a elibera toată memoria cache neutilizată, astfel încât să poată fi folosită de alte aplicații GPU.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Verificați Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Efectuați următoarele sarcini pentru a crea un token Hugging Face.

    - Navigați la [Pagina de setări a token-ului Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Selectați **New token**.
    - Introduceți **Name** pentru proiectul pe care doriți să-l utilizați.
    - Selectați **Type** ca **Write**.

> **Notă**
>
> Dacă întâmpinați următoarea eroare:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Pentru a rezolva acest lucru, introduceți următoarea comandă în terminalul dvs.
>
> ```bash
> sudo ldconfig
> ```

**Declinarea responsabilității**:  
Acest document a fost tradus folosind servicii de traducere bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea umană realizată de profesioniști. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.