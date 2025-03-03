### Príkladový scenár

Predstavte si, že máte obrázok (`demo.png`) a chcete vygenerovať Python kód, ktorý tento obrázok spracuje a uloží jeho novú verziu (`phi-3-vision.jpg`).

Vyššie uvedený kód tento proces automatizuje pomocou:

1. Nastavenia prostredia a potrebných konfigurácií.
2. Vytvorenia výzvy, ktorá modelu zadá pokyn na vygenerovanie požadovaného Python kódu.
3. Odoslania výzvy modelu a zhromaždenia vygenerovaného kódu.
4. Extrahovania a spustenia vygenerovaného kódu.
5. Zobrazenia pôvodného a spracovaného obrázka.

Tento prístup využíva silu AI na automatizáciu úloh spracovania obrázkov, čím zjednodušuje a urýchľuje dosiahnutie vašich cieľov.

[Ukážkové riešenie kódu](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Rozdeľme si, čo celý kód robí, krok za krokom:

1. **Inštalácia potrebného balíka**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Tento príkaz nainštaluje balík `langchain_nvidia_ai_endpoints` a zabezpečí, že ide o najnovšiu verziu.

2. **Import potrebných modulov**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Tieto importy načítajú potrebné moduly na interakciu s NVIDIA AI endpointmi, bezpečné spracovanie hesiel, interakciu so systémom a kódovanie/dekódovanie údajov vo formáte base64.

3. **Nastavenie API kľúča**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Tento kód kontroluje, či je nastavená premenná prostredia `NVIDIA_API_KEY`. Ak nie, vyzve používateľa, aby zadal svoj API kľúč bezpečne.

4. **Definovanie modelu a cesty k obrázku**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Tu sa nastaví model, ktorý sa použije, vytvorí sa inštancia `ChatNVIDIA` so špecifikovaným modelom a definuje sa cesta k súboru s obrázkom.

5. **Vytvorenie textovej výzvy**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Tu sa definuje textová výzva, ktorá modelu zadáva pokyn na vygenerovanie Python kódu na spracovanie obrázka.

6. **Zakódovanie obrázka do formátu Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Tento kód načíta súbor s obrázkom, zakóduje ho do formátu base64 a vytvorí HTML značku obrázka s kódovanými údajmi.

7. **Kombinácia textu a obrázka do výzvy**:
    ```python
    prompt = f"{text} {image}"
    ```
    Tu sa textová výzva a HTML značka obrázka spoja do jedného reťazca.

8. **Generovanie kódu pomocou ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Tento kód odošle výzvu do `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` reťazca.

9. **Extrahovanie Python kódu z vygenerovaného obsahu**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Tento kód extrahuje skutočný Python kód z vygenerovaného obsahu odstránením markdown formátovania.

10. **Spustenie vygenerovaného kódu**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Tento krok spustí extrahovaný Python kód ako podproces a zachytí jeho výstup.

11. **Zobrazenie obrázkov**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Tieto riadky zobrazia obrázky pomocou modulu `IPython.display`.

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladateľských služieb. Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.