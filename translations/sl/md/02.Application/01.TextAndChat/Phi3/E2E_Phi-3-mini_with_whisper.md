# Interaktivni Phi 3 Mini 4K Instruct Chatbot z Whisper

## Pregled

Interaktivni Phi 3 Mini 4K Instruct Chatbot je orodje, ki uporabnikom omogoča interakcijo z Microsoft Phi 3 Mini 4K instruct demo prek besedilnega ali zvočnega vnosa. Chatbot lahko uporabite za različne naloge, kot so prevajanje, vremenske posodobitve in pridobivanje splošnih informacij.

### Začetek

Če želite uporabiti ta chatbot, sledite tem navodilom:

1. Odprite nov [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb).
2. V glavnem oknu beležnice boste videli vmesnik za klepet s poljem za vnos besedila in gumbom "Pošlji".
3. Če želite uporabiti chatbot na osnovi besedila, preprosto vnesite svoje sporočilo v polje za vnos besedila in kliknite gumb "Pošlji". Chatbot bo odgovoril z zvočno datoteko, ki jo lahko predvajate neposredno v beležnici.

**Opomba**: To orodje zahteva GPU in dostop do Microsoft Phi-3 in OpenAI Whisper modelov, ki se uporabljajo za prepoznavanje govora in prevajanje.

### Zahteve za GPU

Za zagon tega demo primera potrebujete 12 GB pomnilnika GPU.

Zahteve za pomnilnik za zagon demo primera **Microsoft-Phi-3-Mini-4K instruct** na GPU so odvisne od več dejavnikov, kot so velikost vhodnih podatkov (zvok ali besedilo), jezik za prevajanje, hitrost modela in razpoložljivi pomnilnik GPU.

Na splošno je model Whisper zasnovan za delovanje na GPU. Priporočena minimalna količina pomnilnika GPU za zagon modela Whisper je 8 GB, vendar lahko obravnava tudi večje količine pomnilnika, če je to potrebno.

Pomembno je omeniti, da zagon velike količine podatkov ali visokega števila zahtevkov na modelu lahko zahteva več pomnilnika GPU in/ali povzroči težave z zmogljivostjo. Priporočljivo je, da preizkusite svoj primer uporabe z različnimi konfiguracijami in spremljate porabo pomnilnika, da določite optimalne nastavitve za vaše specifične potrebe.

## E2E Primer za Interaktivni Phi 3 Mini 4K Instruct Chatbot z Whisper

Beležnica z naslovom [Interaktivni Phi 3 Mini 4K Instruct Chatbot z Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) prikazuje, kako uporabiti Microsoft Phi 3 Mini 4K instruct Demo za generiranje besedila iz zvočnega ali pisnega vnosa. Beležnica definira več funkcij:

1. `tts_file_name(text)`: Ta funkcija generira ime datoteke na podlagi vhodnega besedila za shranjevanje ustvarjene zvočne datoteke.
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ta funkcija uporablja Edge TTS API za generiranje zvočne datoteke iz seznama delov vhodnega besedila. Vhodni parametri so seznam delov, hitrost govora, ime glasu in pot za shranjevanje ustvarjene zvočne datoteke.
3. `talk(input_text)`: Ta funkcija generira zvočno datoteko z uporabo Edge TTS API in jo shrani pod naključnim imenom v imenik /content/audio. Vhodni parameter je besedilo, ki ga želite pretvoriti v govor.
4. `run_text_prompt(message, chat_history)`: Ta funkcija uporablja Microsoft Phi 3 Mini 4K instruct demo za generiranje zvočne datoteke iz vhodnega sporočila in jo doda zgodovini klepeta.
5. `run_audio_prompt(audio, chat_history)`: Ta funkcija pretvori zvočno datoteko v besedilo z uporabo API-ja modela Whisper in ga posreduje funkciji `run_text_prompt()`.
6. Koda zažene Gradio aplikacijo, ki uporabnikom omogoča interakcijo z demo primerom Phi 3 Mini 4K instruct bodisi z vnosom sporočil bodisi z nalaganjem zvočnih datotek. Izhod je prikazan kot besedilno sporočilo znotraj aplikacije.

## Odpravljanje težav

Namestitev gonilnikov Cuda GPU

1. Poskrbite, da so vaše Linux aplikacije posodobljene

    ```bash
    sudo apt update
    ```

2. Namestite Cuda gonilnike

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. Registrirajte lokacijo gonilnika cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. Preverjanje velikosti pomnilnika Nvidia GPU (zahtevano 12 GB pomnilnika GPU)

    ```bash
    nvidia-smi
    ```

5. Praznjenje predpomnilnika: Če uporabljate PyTorch, lahko pokličete torch.cuda.empty_cache(), da sprostite ves neuporabljen predpomnilnik, tako da ga lahko uporabijo druge aplikacije GPU.

    ```python
    torch.cuda.empty_cache() 
    ```

6. Preverjanje Nvidia Cuda

    ```bash
    nvcc --version
    ```

7. Izvedite naslednje naloge za ustvarjanje žetona Hugging Face.

    - Pojdite na [Stran z nastavitvami žetona Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Izberite **New token**.
    - Vnesite ime projekta (**Name**), ki ga želite uporabiti.
    - Izberite **Type** kot **Write**.

> **Opomba**
>
> Če naletite na naslednjo napako:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Za rešitev te težave vnesite naslednji ukaz v svoj terminal.
>
> ```bash
> sudo ldconfig
> ```

**Zavrnitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitev strojnega prevajanja na osnovi umetne inteligence. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni prevod s strani človeka. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.