# Interactieve Phi 3 Mini 4K Instruct Chatbot met Whisper

## Overzicht

De Interactieve Phi 3 Mini 4K Instruct Chatbot is een tool waarmee gebruikers kunnen communiceren met de Microsoft Phi 3 Mini 4K instruct-demo via tekst- of audio-invoer. De chatbot kan worden gebruikt voor verschillende taken, zoals vertalingen, weerupdates en het verzamelen van algemene informatie.

### Aan de slag

Volg deze stappen om de chatbot te gebruiken:

1. Open een nieuwe [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb).
2. In het hoofdvenster van de notebook zie je een chatinterface met een tekstinvoerveld en een knop "Verzenden".
3. Om de tekstgebaseerde chatbot te gebruiken, typ je je bericht in het tekstinvoerveld en klik je op de knop "Verzenden". De chatbot reageert met een audiobestand dat direct vanuit de notebook kan worden afgespeeld.

**Opmerking**: Deze tool vereist een GPU en toegang tot de Microsoft Phi-3 en OpenAI Whisper-modellen, die worden gebruikt voor spraakherkenning en vertaling.

### GPU Vereisten

Om deze demo uit te voeren, heb je 12 GB GPU-geheugen nodig.

De geheugenvereisten voor het uitvoeren van de **Microsoft-Phi-3-Mini-4K instruct**-demo op een GPU hangen af van verschillende factoren, zoals de grootte van de invoergegevens (audio of tekst), de gebruikte taal voor vertaling, de snelheid van het model en het beschikbare geheugen op de GPU.

Over het algemeen is het Whisper-model ontworpen om op GPU's te draaien. De aanbevolen minimale hoeveelheid GPU-geheugen voor het uitvoeren van het Whisper-model is 8 GB, maar het kan grotere hoeveelheden geheugen verwerken indien nodig.

Het is belangrijk op te merken dat het verwerken van een grote hoeveelheid gegevens of een hoog aantal verzoeken aan het model meer GPU-geheugen kan vereisen en/of prestatieproblemen kan veroorzaken. Het wordt aanbevolen om je gebruiksscenario te testen met verschillende configuraties en het geheugenverbruik te monitoren om de optimale instellingen voor jouw specifieke behoeften te bepalen.

## E2E Voorbeeld voor Interactieve Phi 3 Mini 4K Instruct Chatbot met Whisper

De Jupyter-notebook met de titel [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) laat zien hoe je de Microsoft Phi 3 Mini 4K instruct-demo kunt gebruiken om tekst te genereren uit audio- of tekstinvoer. De notebook definieert verschillende functies:

1. `tts_file_name(text)`: Deze functie genereert een bestandsnaam op basis van de invoertekst om het gegenereerde audiobestand op te slaan.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Deze functie gebruikt de Edge TTS API om een audiobestand te genereren uit een lijst met tekstfragmenten. De invoerparameters zijn de lijst met fragmenten, de spreektempo, de stemnaam en het uitvoerpad voor het opslaan van het gegenereerde audiobestand.
1. `talk(input_text)`: Deze functie genereert een audiobestand met behulp van de Edge TTS API en slaat het op onder een willekeurige bestandsnaam in de map /content/audio. De invoerparameter is de tekst die moet worden omgezet in spraak.
1. `run_text_prompt(message, chat_history)`: Deze functie gebruikt de Microsoft Phi 3 Mini 4K instruct-demo om een audiobestand te genereren vanuit een berichtinvoer en voegt dit toe aan de chatgeschiedenis.
1. `run_audio_prompt(audio, chat_history)`: Deze functie zet een audiobestand om in tekst met behulp van de Whisper-model API en geeft dit door aan de `run_text_prompt()`-functie.
1. De code start een Gradio-app waarmee gebruikers kunnen communiceren met de Phi 3 Mini 4K instruct-demo door berichten te typen of audiobestanden te uploaden. De uitvoer wordt weergegeven als een tekstbericht binnen de app.

## Problemen oplossen

Cuda GPU-drivers installeren

1. Zorg ervoor dat je Linux-applicaties up-to-date zijn

    ```bash
    sudo apt update
    ```

1. Installeer Cuda Drivers

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registreer de locatie van de Cuda-driver

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Controleer de Nvidia GPU-geheugengrootte (vereist 12 GB GPU-geheugen)

    ```bash
    nvidia-smi
    ```

1. Cache legen: Als je PyTorch gebruikt, kun je torch.cuda.empty_cache() aanroepen om al het ongebruikte gecachte geheugen vrij te maken zodat het kan worden gebruikt door andere GPU-toepassingen.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Controleer Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Voer de volgende taken uit om een Hugging Face-token aan te maken.

    - Ga naar de [Hugging Face Token Settings-pagina](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Selecteer **Nieuw token**.
    - Voer de **Naam** van het project in dat je wilt gebruiken.
    - Selecteer **Type** als **Schrijven**.

> **Opmerking**
>
> Als je de volgende fout tegenkomt:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Los dit op door het volgende commando in je terminal in te typen.
>
> ```bash
> sudo ldconfig
> ```

**Disclaimer**:  
Dit document is vertaald met behulp van machinegebaseerde AI-vertalingsdiensten. Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.