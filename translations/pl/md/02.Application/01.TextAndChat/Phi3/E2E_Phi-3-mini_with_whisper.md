# Interaktywny chatbot Phi 3 Mini 4K Instruct z Whisper

## Przegląd

Interaktywny chatbot Phi 3 Mini 4K Instruct to narzędzie, które umożliwia użytkownikom interakcję z demonstracją Microsoft Phi 3 Mini 4K Instruct za pomocą tekstu lub dźwięku. Chatbot może być wykorzystywany do różnych zadań, takich jak tłumaczenie, aktualizacje pogodowe czy zbieranie ogólnych informacji.

### Pierwsze kroki

Aby skorzystać z tego chatbota, wykonaj następujące kroki:

1. Otwórz nowy plik [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. W głównym oknie notebooka zobaczysz interfejs czatu z polem do wprowadzania tekstu i przyciskiem "Wyślij".
3. Aby skorzystać z tekstowego chatbota, wpisz swoją wiadomość w pole tekstowe i kliknij przycisk "Wyślij". Chatbot odpowie plikiem audio, który można odtworzyć bezpośrednio w notebooku.

**Uwaga**: To narzędzie wymaga GPU oraz dostępu do modeli Microsoft Phi-3 i OpenAI Whisper, które są wykorzystywane do rozpoznawania mowy i tłumaczenia.

### Wymagania GPU

Do uruchomienia tej demonstracji potrzebujesz GPU o pamięci 12 GB.

Wymagania pamięciowe dla uruchomienia demonstracji **Microsoft-Phi-3-Mini-4K Instruct** na GPU zależą od kilku czynników, takich jak rozmiar danych wejściowych (audio lub tekst), język używany do tłumaczenia, szybkość modelu oraz dostępna pamięć GPU.

Ogólnie rzecz biorąc, model Whisper został zaprojektowany do pracy na GPU. Zalecana minimalna ilość pamięci GPU to 8 GB, ale model może obsługiwać większe ilości pamięci, jeśli jest to konieczne.

Należy pamiętać, że przetwarzanie dużej ilości danych lub dużej liczby żądań może wymagać większej pamięci GPU i/lub powodować problemy z wydajnością. Zaleca się przetestowanie swojego przypadku użycia z różnymi konfiguracjami oraz monitorowanie użycia pamięci w celu określenia optymalnych ustawień dla swoich potrzeb.

## Przykład E2E dla interaktywnego chatbota Phi 3 Mini 4K Instruct z Whisper

Notebook Jupyter zatytułowany [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) pokazuje, jak korzystać z demonstracji Microsoft Phi 3 Mini 4K Instruct do generowania tekstu z danych wejściowych audio lub tekstowych. Notebook definiuje kilka funkcji:

1. `tts_file_name(text)`: Funkcja generuje nazwę pliku na podstawie tekstu wejściowego w celu zapisania wygenerowanego pliku audio.
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Funkcja korzysta z Edge TTS API do wygenerowania pliku audio z listy fragmentów tekstu wejściowego. Parametry wejściowe to lista fragmentów, szybkość mowy, nazwa głosu oraz ścieżka wyjściowa do zapisania wygenerowanego pliku audio.
3. `talk(input_text)`: Funkcja generuje plik audio, korzystając z Edge TTS API, i zapisuje go pod losową nazwą w katalogu /content/audio. Parametrem wejściowym jest tekst wejściowy do przekształcenia na mowę.
4. `run_text_prompt(message, chat_history)`: Funkcja korzysta z demonstracji Microsoft Phi 3 Mini 4K Instruct do wygenerowania pliku audio z wiadomości wejściowej i dodaje go do historii czatu.
5. `run_audio_prompt(audio, chat_history)`: Funkcja konwertuje plik audio na tekst, używając API modelu Whisper, i przekazuje go do funkcji `run_text_prompt()`.
6. Kod uruchamia aplikację Gradio, która pozwala użytkownikom na interakcję z demonstracją Phi 3 Mini 4K Instruct poprzez wpisywanie wiadomości lub przesyłanie plików audio. Wynik jest wyświetlany jako wiadomość tekstowa w aplikacji.

## Rozwiązywanie problemów

Instalacja sterowników GPU Cuda

1. Upewnij się, że Twoje aplikacje na Linuxie są aktualne:

    ```bash
    sudo apt update
    ```

2. Zainstaluj sterowniki Cuda:

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. Zarejestruj lokalizację sterownika Cuda:

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. Sprawdź rozmiar pamięci Nvidia GPU (wymagane 12 GB pamięci GPU):

    ```bash
    nvidia-smi
    ```

5. Opróżnij pamięć podręczną: Jeśli używasz PyTorch, możesz wywołać funkcję torch.cuda.empty_cache(), aby zwolnić całą nieużywaną pamięć podręczną, która może zostać wykorzystana przez inne aplikacje GPU.

    ```python
    torch.cuda.empty_cache() 
    ```

6. Sprawdź Cuda Nvidia:

    ```bash
    nvcc --version
    ```

7. Wykonaj następujące kroki, aby utworzyć token Hugging Face:

    - Przejdź na stronę [Hugging Face Token Settings](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Wybierz **New token**.
    - Wprowadź **Name** projektu, którego chcesz użyć.
    - Wybierz **Type** jako **Write**.

> **Uwaga**
>
> Jeśli napotkasz następujący błąd:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Aby go rozwiązać, wpisz następujące polecenie w terminalu:
>
> ```bash
> sudo ldconfig
> ```

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usług tłumaczeniowych opartych na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uważany za wiarygodne źródło. W przypadku kluczowych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.