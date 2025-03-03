### Przykładowy scenariusz

Wyobraź sobie, że masz obraz (`demo.png`) i chcesz wygenerować kod w Pythonie, który przetwarza ten obraz i zapisuje jego nową wersję (`phi-3-vision.jpg`).

Powyższy kod automatyzuje ten proces poprzez:

1. Przygotowanie środowiska i niezbędnych konfiguracji.
2. Utworzenie polecenia, które instruuje model do wygenerowania wymaganego kodu w Pythonie.
3. Wysłanie polecenia do modelu i zebranie wygenerowanego kodu.
4. Wyodrębnienie i uruchomienie wygenerowanego kodu.
5. Wyświetlenie oryginalnego i przetworzonego obrazu.

Takie podejście wykorzystuje moc AI do automatyzacji zadań związanych z przetwarzaniem obrazów, co sprawia, że osiągnięcie celu staje się łatwiejsze i szybsze.

[Przykładowe rozwiązanie kodu](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Rozłóżmy teraz cały kod krok po kroku:

1. **Zainstaluj wymagany pakiet**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    To polecenie instaluje pakiet `langchain_nvidia_ai_endpoints`, upewniając się, że jest to najnowsza wersja.

2. **Zaimportuj niezbędne moduły**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Te importy umożliwiają korzystanie z niezbędnych modułów do interakcji z punktami końcowymi NVIDIA AI, bezpiecznego zarządzania hasłami, pracy z systemem operacyjnym oraz kodowania i dekodowania danych w formacie base64.

3. **Ustaw klucz API**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Ten kod sprawdza, czy zmienna środowiskowa `NVIDIA_API_KEY` jest ustawiona. Jeśli nie, użytkownik zostanie poproszony o bezpieczne wprowadzenie swojego klucza API.

4. **Zdefiniuj model i ścieżkę do obrazu**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Ustawia model, który ma być używany, tworzy instancję `ChatNVIDIA` z określonym modelem i definiuje ścieżkę do pliku obrazu.

5. **Utwórz tekstowe polecenie**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Definiuje tekstowe polecenie, które instruuje model do wygenerowania kodu w Pythonie do przetwarzania obrazu.

6. **Zakoduj obraz w base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Ten kod odczytuje plik obrazu, koduje go w base64 i tworzy znacznik HTML obrazu z zakodowanymi danymi.

7. **Połącz tekst i obraz w jedno polecenie**:
    ```python
    prompt = f"{text} {image}"
    ```
    Łączy tekstowe polecenie i znacznik HTML obrazu w jeden ciąg znaków.

8. **Wygeneruj kod za pomocą ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Ten kod wysyła polecenie do `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Wyodrębnij kod Python z wygenerowanej treści**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Wyodrębnia właściwy kod w Pythonie z wygenerowanej treści, usuwając formatowanie markdown.

10. **Uruchom wygenerowany kod**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Uruchamia wyodrębniony kod w Pythonie jako podproces i przechwytuje jego wynik.

11. **Wyświetl obrazy**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Te linie wyświetlają obrazy za pomocą modułu `IPython.display`.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usług automatycznego tłumaczenia opartego na sztucznej inteligencji. Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło nadrzędne. W przypadku istotnych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.