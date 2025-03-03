# Interaktiv Phi 3 Mini 4K Instruct Chatbot med Whisper

## Oversikt

Den interaktive Phi 3 Mini 4K Instruct Chatbot er et verktøy som lar brukere samhandle med Microsoft Phi 3 Mini 4K instruct-demoen ved hjelp av tekst- eller lydinnspill. Chatboten kan brukes til en rekke oppgaver, som oversettelse, værmeldinger og generell informasjonsinnhenting.

### Kom i gang

For å bruke denne chatboten, følg disse instruksjonene:

1. Åpne en ny [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. I hovedvinduet i notatboken vil du se et chatteboksgrensesnitt med et tekstinndatafelt og en "Send"-knapp.
3. For å bruke den tekstbaserte chatboten, skriv inn meldingen din i tekstfeltet og klikk på "Send"-knappen. Chatboten vil svare med en lydfil som kan spilles direkte fra notatboken.

**Merk**: Dette verktøyet krever en GPU og tilgang til Microsoft Phi-3 og OpenAI Whisper-modellene, som brukes til talegjenkjenning og oversettelse.

### GPU-krav

For å kjøre denne demoen trenger du 12 GB GPU-minne.

Minnekravene for å kjøre **Microsoft-Phi-3-Mini-4K instruct**-demoen på en GPU vil avhenge av flere faktorer, som størrelsen på inngangsdataene (lyd eller tekst), språket som brukes for oversettelse, modellens hastighet og tilgjengelig minne på GPU-en.

Generelt er Whisper-modellen designet for å kjøre på GPU-er. Det anbefalte minimumsminnet for å kjøre Whisper-modellen er 8 GB, men den kan håndtere større mengder minne om nødvendig.

Det er viktig å merke seg at behandling av store datamengder eller et høyt antall forespørsler på modellen kan kreve mer GPU-minne og/eller føre til ytelsesproblemer. Det anbefales å teste din brukstilfelle med ulike konfigurasjoner og overvåke minnebruken for å finne de optimale innstillingene for dine spesifikke behov.

## E2E-eksempel for Interaktiv Phi 3 Mini 4K Instruct Chatbot med Whisper

Jupyter-notatboken med tittelen [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstrerer hvordan man bruker Microsoft Phi 3 Mini 4K instruct-demoen til å generere tekst fra lyd- eller skriftlige tekstinnspill. Notatboken definerer flere funksjoner:

1. `tts_file_name(text)`: Denne funksjonen genererer et filnavn basert på inngangsteksten for lagring av den genererte lydfilen.
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Denne funksjonen bruker Edge TTS API til å generere en lydfil fra en liste med tekstbiter. Inndataene er listen med tekstbiter, taleraten, stemmens navn og banen for lagring av den genererte lydfilen.
3. `talk(input_text)`: Denne funksjonen genererer en lydfil ved hjelp av Edge TTS API og lagrer den med et tilfeldig filnavn i /content/audio-mappen. Inndataen er teksten som skal konverteres til tale.
4. `run_text_prompt(message, chat_history)`: Denne funksjonen bruker Microsoft Phi 3 Mini 4K instruct-demoen til å generere en lydfil fra en melding og legger den til i chatthistorikken.
5. `run_audio_prompt(audio, chat_history)`: Denne funksjonen konverterer en lydfil til tekst ved hjelp av Whisper-modellens API og sender den til `run_text_prompt()`-funksjonen.
6. Koden starter en Gradio-app som lar brukere samhandle med Phi 3 Mini 4K instruct-demoen ved enten å skrive meldinger eller laste opp lydfiler. Resultatet vises som en tekstmelding i appen.

## Feilsøking

Installere Cuda GPU-drivere

1. Sørg for at Linux-applikasjonene dine er oppdatert

    ```bash
    sudo apt update
    ```

2. Installer Cuda-drivere

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. Registrer plasseringen til Cuda-driveren

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. Sjekk Nvidia GPU-minnestørrelse (krever 12 GB GPU-minne)

    ```bash
    nvidia-smi
    ```

5. Tøm cache: Hvis du bruker PyTorch, kan du kalle torch.cuda.empty_cache() for å frigjøre ubrukt hurtigminne slik at det kan brukes av andre GPU-applikasjoner.

    ```python
    torch.cuda.empty_cache() 
    ```

6. Sjekk Nvidia Cuda

    ```bash
    nvcc --version
    ```

7. Utfør følgende oppgaver for å opprette en Hugging Face-token.

    - Gå til [Hugging Face Token Settings-siden](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Velg **New token**.
    - Angi prosjektets **Name** du ønsker å bruke.
    - Velg **Type** til **Write**.

> **Merk**
>
> Hvis du støter på følgende feil:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> For å løse dette, skriv følgende kommando i terminalen din.
>
> ```bash
> sudo ldconfig
> ```

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.