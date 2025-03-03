# Interaktív Phi 3 Mini 4K Utasításos Chatbot Whisperrel

## Áttekintés

Az Interaktív Phi 3 Mini 4K Utasításos Chatbot egy olyan eszköz, amely lehetővé teszi a felhasználók számára, hogy szöveges vagy hangbemenet segítségével kapcsolatba lépjenek a Microsoft Phi 3 Mini 4K utasításos demójával. A chatbot különféle feladatokra használható, például fordításra, időjárás-frissítésekre és általános információgyűjtésre.

### Első lépések

A chatbot használatához kövesse az alábbi utasításokat:

1. Nyisson meg egy új [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) fájlt.
2. A jegyzetfüzet főablakában egy chatbox felületet talál, szövegbeviteli mezővel és egy „Küldés” gombbal.
3. Ha a szöveges chatbotot szeretné használni, egyszerűen írja be üzenetét a szövegbeviteli mezőbe, majd kattintson a „Küldés” gombra. A chatbot egy audiofájllal válaszol, amelyet közvetlenül a jegyzetfüzetből lejátszhat.

**Megjegyzés**: Ez az eszköz GPU-t és hozzáférést igényel a Microsoft Phi-3 és OpenAI Whisper modellekhez, amelyeket beszédfelismerésre és fordításra használnak.

### GPU Követelmények

A demó futtatásához 12 GB GPU-memóriára van szükség.

A **Microsoft-Phi-3-Mini-4K utasításos** demó GPU-n való futtatásához szükséges memória a bemeneti adatok (hang vagy szöveg) méretétől, a fordítás nyelvétől, a modell sebességétől és a GPU rendelkezésre álló memóriájától függ.

Általánosságban elmondható, hogy a Whisper modellt GPU-kon való futtatásra tervezték. A Whisper modell futtatásához ajánlott minimális GPU-memória 8 GB, de szükség esetén nagyobb memóriamennyiséget is képes kezelni.

Fontos megjegyezni, hogy nagy mennyiségű adat vagy magas számú kérés futtatása a modellen több GPU-memóriát igényelhet, és/vagy teljesítményproblémákat okozhat. Javasolt az adott felhasználási eset tesztelése különböző konfigurációkkal, valamint a memóriahasználat figyelése az optimális beállítások meghatározásához.

## E2E Példa az Interaktív Phi 3 Mini 4K Utasításos Chatbot Whisperrel

Az [Interaktív Phi 3 Mini 4K Utasításos Chatbot Whisperrel](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) című Jupyter notebook bemutatja, hogyan lehet a Microsoft Phi 3 Mini 4K utasításos demót használni hang- vagy szöveges bemenetből történő szöveg előállítására. A jegyzetfüzet több funkciót definiál:

1. `tts_file_name(text)`: Ez a funkció fájlnevet generál a bemeneti szöveg alapján a létrehozott audiofájl mentéséhez.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ez a funkció az Edge TTS API-t használja egy audiofájl létrehozásához a bemeneti szöveg darabjaiból. A bemeneti paraméterek: a darabok listája, a beszéd sebessége, a hang neve és a létrehozott audiofájl mentési útvonala.
1. `talk(input_text)`: Ez a funkció audiofájlt generál az Edge TTS API használatával, és egy véletlenszerű fájlnevet ad neki a /content/audio könyvtárban. A bemeneti paraméter a beszéddé alakítandó szöveg.
1. `run_text_prompt(message, chat_history)`: Ez a funkció a Microsoft Phi 3 Mini 4K utasításos demót használja egy audiofájl létrehozásához egy üzenetbemenet alapján, és hozzáadja azt a csevegési előzményekhez.
1. `run_audio_prompt(audio, chat_history)`: Ez a funkció egy audiofájlt alakít szöveggé a Whisper modell API használatával, majd továbbítja a `run_text_prompt()` funkciónak.
1. A kód egy Gradio alkalmazást indít el, amely lehetővé teszi a felhasználók számára, hogy kapcsolatba lépjenek a Phi 3 Mini 4K utasításos demóval, akár üzenetek begépelésével, akár hangfájlok feltöltésével. Az eredmény szöveges üzenetként jelenik meg az alkalmazáson belül.

## Hibaelhárítás

Cuda GPU illesztőprogramok telepítése

1. Győződjön meg róla, hogy a Linux-alkalmazásai naprakészek:

    ```bash
    sudo apt update
    ```

1. Telepítse a Cuda illesztőprogramokat:

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Regisztrálja a Cuda illesztőprogram helyét:

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Ellenőrizze az Nvidia GPU memória méretét (12 GB GPU memória szükséges):

    ```bash
    nvidia-smi
    ```

1. Gyorsítótár ürítése: Ha PyTorch-ot használ, hívja meg a torch.cuda.empty_cache() függvényt az összes nem használt gyorsítótár-memória felszabadításához, hogy más GPU-alkalmazások is használhassák.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Nvidia Cuda ellenőrzése:

    ```bash
    nvcc --version
    ```

1. Hajtsa végre az alábbi lépéseket egy Hugging Face token létrehozásához:

    - Nyissa meg a [Hugging Face Token Beállítások oldalt](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Válassza az **Új token** lehetőséget.
    - Adja meg a használni kívánt projekt **Nevét**.
    - Válassza a **Típus** mezőben a **Write** lehetőséget.

> **Megjegyzés**
>
> Ha a következő hibával találkozik:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> A megoldáshoz írja be a következő parancsot a termináljába:
>
> ```bash
> sudo ldconfig
> ```

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítási szolgáltatásokkal készült fordítást tartalmaz. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekinthető hiteles forrásnak. Fontos információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.