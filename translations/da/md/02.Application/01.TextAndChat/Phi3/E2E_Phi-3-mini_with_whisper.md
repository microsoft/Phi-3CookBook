# Interaktiv Phi 3 Mini 4K Instruct Chatbot med Whisper

## Oversigt

Den interaktive Phi 3 Mini 4K Instruct Chatbot er et værktøj, der giver brugere mulighed for at interagere med Microsoft Phi 3 Mini 4K instruct-demoen ved hjælp af tekst- eller lydinput. Chatbotten kan bruges til en række opgaver som oversættelse, vejropdateringer og generel informationssøgning.

### Kom godt i gang

For at bruge denne chatbot skal du blot følge disse trin:

1. Åbn en ny [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. I hovedvinduet i notebooken vil du se en chatboksgrænseflade med en tekstinputboks og en "Send"-knap.
3. For at bruge den tekstbaserede chatbot skal du blot skrive din besked i tekstinputboksen og klikke på "Send"-knappen. Chatbotten vil svare med en lydfil, som kan afspilles direkte fra notebooken.

**Bemærk**: Dette værktøj kræver en GPU og adgang til Microsoft Phi-3 og OpenAI Whisper-modellerne, som bruges til talegenkendelse og oversættelse.

### GPU-krav

For at køre denne demo har du brug for 12 GB GPU-hukommelse.

Hukommelseskravene til at køre **Microsoft-Phi-3-Mini-4K instruct**-demoen på en GPU afhænger af flere faktorer, såsom størrelsen af inputdata (lyd eller tekst), det sprog, der bruges til oversættelse, modellens hastighed og den tilgængelige hukommelse på GPU'en.

Generelt er Whisper-modellen designet til at køre på GPU'er. Den anbefalede minimumsmængde GPU-hukommelse til at køre Whisper-modellen er 8 GB, men den kan håndtere større mængder hukommelse, hvis det er nødvendigt.

Det er vigtigt at bemærke, at behandling af store datamængder eller et højt antal forespørgsler til modellen kan kræve mere GPU-hukommelse og/eller føre til ydeevneproblemer. Det anbefales at teste din brugssag med forskellige konfigurationer og overvåge hukommelsesforbruget for at finde de optimale indstillinger til dine specifikke behov.

## E2E Eksempel på Interaktiv Phi 3 Mini 4K Instruct Chatbot med Whisper

Jupyter-notebooken med titlen [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) viser, hvordan man bruger Microsoft Phi 3 Mini 4K instruct-demoen til at generere tekst ud fra lyd- eller tekstinput. Notebooken definerer flere funktioner:

1. `tts_file_name(text)`: Denne funktion genererer et filnavn baseret på inputteksten til at gemme den genererede lydfil.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Denne funktion bruger Edge TTS API til at generere en lydfil fra en liste af tekststykker. Inputparametrene er listen af tekststykker, taletempoet, stemmens navn og outputstien til at gemme den genererede lydfil.
1. `talk(input_text)`: Denne funktion genererer en lydfil ved at bruge Edge TTS API og gemmer den til et tilfældigt filnavn i /content/audio-mappen. Inputparameteren er den tekst, der skal konverteres til tale.
1. `run_text_prompt(message, chat_history)`: Denne funktion bruger Microsoft Phi 3 Mini 4K instruct-demoen til at generere en lydfil ud fra en beskedinput og tilføjer den til chathistorikken.
1. `run_audio_prompt(audio, chat_history)`: Denne funktion konverterer en lydfil til tekst ved hjælp af Whisper-modellens API og sender det videre til `run_text_prompt()`-funktionen.
1. Koden starter en Gradio-app, der giver brugere mulighed for at interagere med Phi 3 Mini 4K instruct-demoen ved enten at skrive beskeder eller uploade lydfiler. Outputtet vises som en tekstbesked i appen.

## Fejlfinding

Installation af Cuda GPU-drivere

1. Sørg for, at din Linux-applikation er opdateret

    ```bash
    sudo apt update
    ```

1. Installer Cuda-drivere

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registrer placeringen af Cuda-driveren

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Tjek Nvidia GPU-hukommelsesstørrelse (kræver 12 GB GPU-hukommelse)

    ```bash
    nvidia-smi
    ```

1. Tøm cache: Hvis du bruger PyTorch, kan du kalde torch.cuda.empty_cache() for at frigive al ubrugt cache-hukommelse, så den kan bruges af andre GPU-applikationer

    ```python
    torch.cuda.empty_cache() 
    ```

1. Tjek Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Udfør følgende trin for at oprette en Hugging Face-token.

    - Gå til [Hugging Face Token Settings-siden](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Vælg **New token**.
    - Indtast det projekt**navn**, du vil bruge.
    - Vælg **Type** til **Write**.

> **Bemærk**
>
> Hvis du støder på følgende fejl:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> For at løse dette skal du skrive følgende kommando i din terminal.
>
> ```bash
> sudo ldconfig
> ```

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brugen af denne oversættelse.