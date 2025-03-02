# Interaktivni Phi 3 Mini 4K Instruct Četbot sa Whisper-om

## Pregled

Interaktivni Phi 3 Mini 4K Instruct Četbot je alat koji omogućava korisnicima da komuniciraju sa Microsoft Phi 3 Mini 4K Instruct demo-om koristeći tekstualni ili audio unos. Četbot se može koristiti za razne zadatke, kao što su prevođenje, vremenske prognoze i prikupljanje opštih informacija.

### Kako početi

Da biste koristili ovaj četbot, pratite sledeće korake:

1. Otvorite novi [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. U glavnom prozoru beležnice videćete interfejs sa poljem za unos teksta i dugmetom „Send“.
3. Da biste koristili tekstualni četbot, jednostavno unesite svoju poruku u polje za unos teksta i kliknite na dugme „Send“. Četbot će odgovoriti audio fajlom koji možete reprodukovati direktno u beležnici.

**Napomena**: Ovaj alat zahteva GPU i pristup Microsoft Phi-3 i OpenAI Whisper modelima, koji se koriste za prepoznavanje govora i prevođenje.

### Zahtevi za GPU

Za pokretanje ovog demo-a potrebno je 12GB GPU memorije.

Zahtevi za memoriju pri pokretanju **Microsoft-Phi-3-Mini-4K Instruct** demo-a na GPU-u zavise od nekoliko faktora, kao što su veličina ulaznih podataka (audio ili tekst), jezik koji se koristi za prevođenje, brzina modela i dostupna memorija na GPU-u.

Generalno, Whisper model je dizajniran za rad na GPU-ovima. Preporučena minimalna količina GPU memorije za pokretanje Whisper modela je 8 GB, ali može raditi sa većom količinom memorije ako je potrebno.

Važno je napomenuti da pokretanje velike količine podataka ili velikog broja zahteva na modelu može zahtevati više GPU memorije i/ili uzrokovati probleme sa performansama. Preporučuje se da testirate svoj slučaj upotrebe sa različitim konfiguracijama i pratite upotrebu memorije kako biste odredili optimalna podešavanja za svoje specifične potrebe.

## E2E Primer za Interaktivni Phi 3 Mini 4K Instruct Četbot sa Whisper-om

Jupyter beležnica pod nazivom [Interaktivni Phi 3 Mini 4K Instruct Četbot sa Whisper-om](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstrira kako koristiti Microsoft Phi 3 Mini 4K Instruct demo za generisanje teksta iz audio ili tekstualnog unosa. Beležnica definiše nekoliko funkcija:

1. `tts_file_name(text)`: Ova funkcija generiše naziv fajla na osnovu unetog teksta za čuvanje generisanog audio fajla.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ova funkcija koristi Edge TTS API za generisanje audio fajla iz liste delova unetog teksta. Ulazni parametri su lista delova, brzina govora, ime glasa i putanja za čuvanje generisanog audio fajla.
1. `talk(input_text)`: Ova funkcija generiše audio fajl koristeći Edge TTS API i čuva ga pod nasumičnim nazivom fajla u direktorijumu /content/audio. Ulazni parametar je tekst koji treba konvertovati u govor.
1. `run_text_prompt(message, chat_history)`: Ova funkcija koristi Microsoft Phi 3 Mini 4K Instruct demo za generisanje audio fajla iz unosa poruke i dodaje ga istoriji četa.
1. `run_audio_prompt(audio, chat_history)`: Ova funkcija konvertuje audio fajl u tekst koristeći Whisper model API i prosleđuje ga funkciji `run_text_prompt()`.
1. Kod pokreće Gradio aplikaciju koja omogućava korisnicima da komuniciraju sa Phi 3 Mini 4K Instruct demo-om unosom poruka ili otpremanjem audio fajlova. Izlaz se prikazuje kao tekstualna poruka unutar aplikacije.

## Rešavanje problema

Instalacija Cuda GPU drajvera

1. Uverite se da je vaša Linux aplikacija ažurirana

    ```bash
    sudo apt update
    ```

1. Instalirajte Cuda drajvere

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registrujte lokaciju Cuda drajvera

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Provera veličine Nvidia GPU memorije (Potrebno 12GB GPU memorije)

    ```bash
    nvidia-smi
    ```

1. Pražnjenje keša: Ako koristite PyTorch, možete pozvati torch.cuda.empty_cache() da oslobodite svu nekorišćenu keš memoriju kako bi je mogle koristiti druge GPU aplikacije

    ```python
    torch.cuda.empty_cache() 
    ```

1. Provera Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Izvršite sledeće zadatke za kreiranje Hugging Face tokena.

    - Idite na [Hugging Face Token Settings stranicu](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Izaberite **New token**.
    - Unesite ime projekta **Name** koji želite da koristite.
    - Izaberite **Type** na **Write**.

> **Napomena**
>
> Ako naiđete na sledeću grešku:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Da biste ovo rešili, unesite sledeću komandu u vaš terminal.
>
> ```bash
> sudo ldconfig
> ```

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако настојимо да обезбедимо тачност, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.