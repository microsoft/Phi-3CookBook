# Interaktívny chatbot Phi 3 Mini 4K Instruct s Whisper

## Prehľad

Interaktívny chatbot Phi 3 Mini 4K Instruct je nástroj, ktorý umožňuje používateľom komunikovať s ukážkou Microsoft Phi 3 Mini 4K Instruct pomocou textového alebo zvukového vstupu. Chatbot je možné využiť na rôzne úlohy, ako sú preklady, aktualizácie počasia a zhromažďovanie všeobecných informácií.

### Začíname

Na používanie tohto chatbota postupujte podľa týchto pokynov:

1. Otvorte nový [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb).
2. V hlavnom okne notebooku uvidíte rozhranie chatu s textovým vstupným poľom a tlačidlom „Send“.
3. Ak chcete použiť textového chatbota, jednoducho napíšte svoju správu do textového vstupného poľa a kliknite na tlačidlo „Send“. Chatbot odpovie zvukovým súborom, ktorý si môžete priamo prehrať v rámci notebooku.

**Poznámka**: Tento nástroj vyžaduje GPU a prístup k modelom Microsoft Phi-3 a OpenAI Whisper, ktoré sa používajú na rozpoznávanie reči a preklad.

### Požiadavky na GPU

Na spustenie tejto ukážky potrebujete 12 GB pamäte GPU.

Požiadavky na pamäť GPU pre spustenie ukážky **Microsoft-Phi-3-Mini-4K instruct** závisia od viacerých faktorov, ako je veľkosť vstupných údajov (zvukových alebo textových), jazyk používaný na preklad, rýchlosť modelu a dostupná pamäť na GPU.

Vo všeobecnosti je model Whisper navrhnutý na spúšťanie na GPU. Odporúčaná minimálna veľkosť pamäte GPU na spustenie modelu Whisper je 8 GB, ale dokáže spracovať aj väčšie množstvo pamäte, ak je to potrebné.

Je dôležité poznamenať, že spustenie veľkého množstva údajov alebo vysokého objemu požiadaviek na model môže vyžadovať viac pamäte GPU a/alebo môže spôsobiť problémy s výkonom. Odporúča sa otestovať váš prípad použitia s rôznymi konfiguráciami a monitorovať využitie pamäte, aby ste určili optimálne nastavenia pre vaše konkrétne potreby.

## Ukážka E2E pre interaktívny chatbot Phi 3 Mini 4K Instruct s Whisper

Jupyter notebook s názvom [Interaktívny chatbot Phi 3 Mini 4K Instruct s Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonštruje, ako používať ukážku Microsoft Phi 3 Mini 4K Instruct na generovanie textu zo zvukového alebo písaného textového vstupu. Notebook definuje niekoľko funkcií:

1. `tts_file_name(text)`: Táto funkcia generuje názov súboru na základe vstupného textu na uloženie vygenerovaného zvukového súboru.
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Táto funkcia používa Edge TTS API na generovanie zvukového súboru zo zoznamu častí vstupného textu. Vstupné parametre sú zoznam častí, rýchlosť reči, názov hlasu a výstupná cesta na uloženie vygenerovaného zvukového súboru.
3. `talk(input_text)`: Táto funkcia generuje zvukový súbor pomocou Edge TTS API a ukladá ho pod náhodným názvom do adresára /content/audio. Vstupný parameter je vstupný text, ktorý sa má previesť na reč.
4. `run_text_prompt(message, chat_history)`: Táto funkcia používa ukážku Microsoft Phi 3 Mini 4K Instruct na generovanie zvukového súboru zo vstupnej správy a pridáva ho do histórie chatu.
5. `run_audio_prompt(audio, chat_history)`: Táto funkcia prevádza zvukový súbor na text pomocou Whisper model API a odovzdáva ho funkcii `run_text_prompt()`.
6. Kód spúšťa aplikáciu Gradio, ktorá umožňuje používateľom komunikovať s ukážkou Phi 3 Mini 4K Instruct buď písaním správ, alebo nahrávaním zvukových súborov. Výstup sa zobrazí ako textová správa v rámci aplikácie.

## Riešenie problémov

Inštalácia ovládačov Cuda GPU

1. Uistite sa, že vaše Linuxové aplikácie sú aktuálne:

    ```bash
    sudo apt update
    ```

2. Nainštalujte ovládače Cuda:

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. Zaregistrujte umiestnenie ovládača Cuda:

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. Kontrola veľkosti pamäte Nvidia GPU (vyžaduje sa 12 GB pamäte GPU):

    ```bash
    nvidia-smi
    ```

5. Vyprázdnenie vyrovnávacej pamäte: Ak používate PyTorch, môžete zavolať torch.cuda.empty_cache(), aby ste uvoľnili všetku nepoužitú vyrovnávaciu pamäť, aby ju mohli používať iné aplikácie GPU.

    ```python
    torch.cuda.empty_cache() 
    ```

6. Kontrola Nvidia Cuda:

    ```bash
    nvcc --version
    ```

7. Vykonajte nasledujúce kroky na vytvorenie Hugging Face tokenu:

    - Prejdite na stránku [Hugging Face Token Settings](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Vyberte **New token**.
    - Zadajte názov projektu (**Name**), ktorý chcete použiť.
    - Vyberte typ (**Type**) ako **Write**.

> **Poznámka**
>
> Ak narazíte na nasledujúcu chybu:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Na jej vyriešenie zadajte nasledujúci príkaz do vášho terminálu:
>
> ```bash
> sudo ldconfig
> ```

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových prekladateľských služieb založených na umelej inteligencii. Aj keď sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj by sa mal považovať pôvodný dokument v jeho pôvodnom jazyku. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.