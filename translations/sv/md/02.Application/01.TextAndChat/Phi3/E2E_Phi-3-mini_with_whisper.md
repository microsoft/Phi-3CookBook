# Interaktiv Phi 3 Mini 4K Instruct Chatbot med Whisper

## Översikt

Den interaktiva Phi 3 Mini 4K Instruct Chatbot är ett verktyg som låter användare interagera med Microsoft Phi 3 Mini 4K instruct-demo via text- eller ljudinmatning. Chatboten kan användas för en rad olika uppgifter, såsom översättning, väderuppdateringar och informationssökning.

### Komma igång

Följ dessa instruktioner för att använda chatboten:

1. Öppna en ny [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. I huvudfönstret på notebooken ser du ett chattgränssnitt med en textruta och en "Skicka"-knapp.
3. För att använda textbaserade chatboten, skriv ditt meddelande i textrutan och klicka på "Skicka"-knappen. Chatboten svarar med en ljudfil som kan spelas upp direkt i notebooken.

**Obs**: Detta verktyg kräver en GPU och tillgång till Microsoft Phi-3 och OpenAI Whisper-modellerna, som används för taligenkänning och översättning.

### GPU-krav

För att köra denna demo behöver du 12 GB GPU-minne.

Minneskraven för att köra **Microsoft-Phi-3-Mini-4K instruct**-demon på en GPU beror på flera faktorer, såsom storleken på inmatningsdata (ljud eller text), språket som används för översättning, modellens hastighet och tillgängligt minne på GPU:n.

Generellt är Whisper-modellen utformad för att köras på GPU:er. Den rekommenderade minsta mängden GPU-minne för att köra Whisper-modellen är 8 GB, men den kan hantera större mängder minne om det behövs.

Det är viktigt att notera att körning av stora datamängder eller en hög volym av förfrågningar på modellen kan kräva mer GPU-minne och/eller orsaka prestandaproblem. Det rekommenderas att testa ditt användningsfall med olika konfigurationer och övervaka minnesanvändningen för att bestämma de optimala inställningarna för dina specifika behov.

## E2E-exempel för Interaktiv Phi 3 Mini 4K Instruct Chatbot med Whisper

Jupyter-notebooken med titeln [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstrerar hur man använder Microsoft Phi 3 Mini 4K instruct-demo för att generera text från ljud- eller textinmatning. Notebooken definierar flera funktioner:

1. `tts_file_name(text)`: Denna funktion genererar ett filnamn baserat på inmatningstexten för att spara den genererade ljudfilen.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Denna funktion använder Edge TTS API för att generera en ljudfil från en lista med textdelar. Inmatningsparametrarna är listan med textdelar, talhastigheten, röstnamnet och sökvägen för att spara den genererade ljudfilen.
1. `talk(input_text)`: Denna funktion genererar en ljudfil genom att använda Edge TTS API och sparar den till ett slumpmässigt filnamn i katalogen /content/audio. Inmatningsparametern är texten som ska omvandlas till tal.
1. `run_text_prompt(message, chat_history)`: Denna funktion använder Microsoft Phi 3 Mini 4K instruct-demo för att generera en ljudfil från ett meddelande och lägger till det i chattloggen.
1. `run_audio_prompt(audio, chat_history)`: Denna funktion omvandlar en ljudfil till text med hjälp av Whisper-modellens API och skickar den vidare till `run_text_prompt()`-funktionen.
1. Koden startar en Gradio-app som låter användare interagera med Phi 3 Mini 4K instruct-demo genom att antingen skriva meddelanden eller ladda upp ljudfiler. Utdata visas som ett textmeddelande i appen.

## Felsökning

Installera Cuda GPU-drivrutiner

1. Se till att dina Linux-applikationer är uppdaterade

    ```bash
    sudo apt update
    ```

1. Installera Cuda-drivrutiner

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registrera platsen för Cuda-drivrutinen

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Kontrollera Nvidia GPU-minnesstorlek (Krävs 12 GB GPU-minne)

    ```bash
    nvidia-smi
    ```

1. Töm cache: Om du använder PyTorch kan du kalla på torch.cuda.empty_cache() för att frigöra allt oanvänt cacheminne så att det kan användas av andra GPU-applikationer

    ```python
    torch.cuda.empty_cache() 
    ```

1. Kontrollera Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Utför följande uppgifter för att skapa en Hugging Face-token.

    - Navigera till [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Välj **New token**.
    - Ange projektets **Namn** som du vill använda.
    - Välj **Typ** till **Write**.

> **Obs**
>
> Om du stöter på följande fel:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> För att lösa detta, skriv följande kommando i din terminal.
>
> ```bash
> sudo ldconfig
> ```

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller inexaktheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell, mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.