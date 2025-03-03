# Interaktivní chatbot Phi 3 Mini 4K Instruct s Whisper

## Přehled

Interaktivní chatbot Phi 3 Mini 4K Instruct je nástroj, který umožňuje uživatelům komunikovat s demem Microsoft Phi 3 Mini 4K Instruct pomocí textového nebo hlasového vstupu. Chatbot lze použít pro různé úkoly, jako je překlad, informace o počasí nebo obecné vyhledávání informací.

### Jak začít

Chcete-li tento chatbot používat, postupujte podle těchto pokynů:

1. Otevřete nový [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. V hlavním okně notebooku uvidíte rozhraní chatu s textovým vstupním polem a tlačítkem „Odeslat“.
3. Pro použití textového chatbota jednoduše napište zprávu do textového vstupního pole a klikněte na tlačítko „Odeslat“. Chatbot odpoví zvukovým souborem, který lze přehrát přímo v notebooku.

**Poznámka**: Tento nástroj vyžaduje GPU a přístup k modelům Microsoft Phi-3 a OpenAI Whisper, které se používají pro rozpoznávání řeči a překlad.

### Požadavky na GPU

Pro spuštění tohoto dema potřebujete 12 GB paměti GPU.

Paměťové požadavky pro spuštění dema **Microsoft-Phi-3-Mini-4K Instruct** na GPU závisí na několika faktorech, jako je velikost vstupních dat (audio nebo text), jazyk použitý pro překlad, rychlost modelu a dostupná paměť na GPU.

Obecně je model Whisper navržen tak, aby běžel na GPU. Doporučené minimální množství paměti GPU pro spuštění modelu Whisper je 8 GB, ale model dokáže využít i větší množství paměti, pokud je k dispozici.

Je důležité poznamenat, že zpracování velkého množství dat nebo vysokého počtu požadavků na model může vyžadovat více paměti GPU a/nebo způsobit problémy s výkonem. Doporučuje se otestovat konkrétní použití s různými konfiguracemi a sledovat využití paměti, abyste určili optimální nastavení pro své potřeby.

## E2E Ukázka pro interaktivní chatbot Phi 3 Mini 4K Instruct s Whisper

Jupyter notebook s názvem [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ukazuje, jak použít demo Microsoft Phi 3 Mini 4K Instruct pro generování textu z audio nebo textového vstupu. Notebook definuje několik funkcí:

1. `tts_file_name(text)`: Tato funkce generuje název souboru na základě vstupního textu pro uložení vytvořeného zvukového souboru.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Tato funkce používá API Edge TTS k vytvoření zvukového souboru ze seznamu částí vstupního textu. Parametry vstupu jsou seznam částí, rychlost řeči, jméno hlasu a cesta pro uložení vytvořeného zvukového souboru.
1. `talk(input_text)`: Tato funkce generuje zvukový soubor pomocí API Edge TTS a ukládá jej pod náhodným názvem do adresáře /content/audio. Parametrem vstupu je text, který má být převeden na řeč.
1. `run_text_prompt(message, chat_history)`: Tato funkce používá demo Microsoft Phi 3 Mini 4K Instruct k vytvoření zvukového souboru ze vstupní zprávy a přidává jej do historie chatu.
1. `run_audio_prompt(audio, chat_history)`: Tato funkce převádí zvukový soubor na text pomocí API modelu Whisper a předává jej funkci `run_text_prompt()`.
1. Kód spouští aplikaci Gradio, která umožňuje uživatelům komunikovat s demem Phi 3 Mini 4K Instruct buď psaním zpráv, nebo nahráváním zvukových souborů. Výstup je zobrazen jako textová zpráva v rámci aplikace.

## Řešení problémů

Instalace ovladačů Cuda GPU

1. Ujistěte se, že je vaše aplikace Linux aktuální

    ```bash
    sudo apt update
    ```

1. Nainstalujte ovladače Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Zaregistrujte umístění ovladače Cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Kontrola velikosti paměti Nvidia GPU (vyžaduje 12 GB paměti GPU)

    ```bash
    nvidia-smi
    ```

1. Vyprázdnění mezipaměti: Pokud používáte PyTorch, můžete zavolat torch.cuda.empty_cache() pro uvolnění veškeré nepoužité mezipaměti, aby ji mohly využívat jiné aplikace GPU.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Kontrola Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Proveďte následující kroky pro vytvoření tokenu Hugging Face.

    - Přejděte na stránku [Hugging Face Token Settings](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Vyberte **New token**.
    - Zadejte název projektu (**Name**), který chcete použít.
    - Nastavte **Type** na **Write**.

> **Poznámka**
>
> Pokud narazíte na následující chybu:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Pro vyřešení tohoto problému zadejte následující příkaz do svého terminálu.
>
> ```bash
> sudo ldconfig
> ```

**Prohlášení**:  
Tento dokument byl přeložen pomocí strojových AI překladových služeb. I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Nejsme zodpovědní za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.