# Interaktivni Phi 3 Mini 4K Instruct Chatbot s Whisperom

## Pregled

Interaktivni Phi 3 Mini 4K Instruct Chatbot alat je koji omogućuje korisnicima interakciju s Microsoft Phi 3 Mini 4K instruct demom putem tekstualnog ili audio unosa. Chatbot se može koristiti za razne zadatke, poput prijevoda, vremenskih prognoza i prikupljanja općih informacija.

### Početak rada

Za korištenje ovog chatbota, slijedite ove korake:

1. Otvorite novi [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. U glavnom prozoru bilježnice vidjet ćete sučelje za chat s tekstualnim unosom i gumbom "Send".
3. Za korištenje tekstualnog chatbota, jednostavno unesite svoju poruku u polje za unos teksta i kliknite gumb "Send". Chatbot će odgovoriti audio datotekom koja se može reproducirati izravno unutar bilježnice.

**Napomena**: Ovaj alat zahtijeva GPU i pristup Microsoft Phi-3 i OpenAI Whisper modelima, koji se koriste za prepoznavanje govora i prijevod.

### Zahtjevi za GPU

Za pokretanje ove demonstracije potrebno je 12 GB GPU memorije.

Zahtjevi za memorijom za pokretanje **Microsoft-Phi-3-Mini-4K instruct** demo na GPU-u ovise o nekoliko čimbenika, poput veličine ulaznih podataka (audio ili tekst), jezika koji se koristi za prijevod, brzine modela i dostupne memorije na GPU-u.

Općenito, Whisper model je dizajniran za rad na GPU-ima. Preporučena minimalna količina GPU memorije za pokretanje Whisper modela je 8 GB, ali može raditi s većim količinama memorije ako je potrebno.

Važno je napomenuti da pokretanje velikih količina podataka ili velikog broja zahtjeva na modelu može zahtijevati više GPU memorije i/ili uzrokovati probleme s performansama. Preporučuje se testiranje vašeg slučaja upotrebe s različitim konfiguracijama i praćenje korištenja memorije kako biste odredili optimalne postavke za vaše specifične potrebe.

## E2E Primjer za Interaktivni Phi 3 Mini 4K Instruct Chatbot s Whisperom

Jupyter bilježnica pod nazivom [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstrira kako koristiti Microsoft Phi 3 Mini 4K instruct Demo za generiranje teksta iz audio ili tekstualnog unosa. Bilježnica definira nekoliko funkcija:

1. `tts_file_name(text)`: Ova funkcija generira naziv datoteke na temelju ulaznog teksta za spremanje generirane audio datoteke.
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ova funkcija koristi Edge TTS API za generiranje audio datoteke iz liste dijelova ulaznog teksta. Ulazni parametri su lista dijelova, brzina govora, ime glasa i izlazna putanja za spremanje generirane audio datoteke.
3. `talk(input_text)`: Ova funkcija generira audio datoteku korištenjem Edge TTS API-ja i sprema je pod nasumičnim nazivom u direktorij /content/audio. Ulazni parametar je tekst koji treba pretvoriti u govor.
4. `run_text_prompt(message, chat_history)`: Ova funkcija koristi Microsoft Phi 3 Mini 4K instruct demo za generiranje audio datoteke iz unosa poruke i dodaje je povijesti razgovora.
5. `run_audio_prompt(audio, chat_history)`: Ova funkcija pretvara audio datoteku u tekst koristeći Whisper model API i prosljeđuje ga funkciji `run_text_prompt()`.
6. Kod pokreće Gradio aplikaciju koja omogućuje korisnicima interakciju s Phi 3 Mini 4K instruct demom unosom poruka ili učitavanjem audio datoteka. Izlaz se prikazuje kao tekstualna poruka unutar aplikacije.

## Rješavanje problema

Instalacija Cuda GPU upravljačkih programa

1. Osigurajte da su vaše Linux aplikacije ažurirane

    ```bash
    sudo apt update
    ```

2. Instalirajte Cuda upravljačke programe

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. Registrirajte lokaciju Cuda upravljačkog programa

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. Provjera veličine Nvidia GPU memorije (Potrebno 12 GB GPU memorije)

    ```bash
    nvidia-smi
    ```

5. Pražnjenje predmemorije: Ako koristite PyTorch, možete pozvati torch.cuda.empty_cache() za oslobađanje sve neiskorištene predmemorirane memorije kako bi je mogli koristiti drugi GPU programi

    ```python
    torch.cuda.empty_cache() 
    ```

6. Provjera Nvidia Cuda

    ```bash
    nvcc --version
    ```

7. Izvršite sljedeće zadatke kako biste stvorili Hugging Face token.

    - Otvorite [Hugging Face Token Settings stranicu](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Odaberite **New token**.
    - Unesite naziv projekta (**Name**) koji želite koristiti.
    - Odaberite **Type** kao **Write**.

> **Napomena**
>
> Ako naiđete na sljedeću pogrešku:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Za rješavanje ovog problema, unesite sljedeću naredbu u vaš terminal.
>
> ```bash
> sudo ldconfig
> ```

**Odricanje odgovornosti**:  
Ovaj dokument je preveden koristeći usluge strojno podržanog AI prijevoda. Iako težimo točnosti, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne snosimo odgovornost za nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.