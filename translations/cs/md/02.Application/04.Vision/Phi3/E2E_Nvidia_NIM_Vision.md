### Příklad Scénáře

Představte si, že máte obrázek (`demo.png`) a chcete vygenerovat Python kód, který tento obrázek zpracuje a uloží jeho novou verzi (`phi-3-vision.jpg`).

Výše uvedený kód automatizuje tento proces tím, že:

1. Nastaví prostředí a potřebné konfigurace.
2. Vytvoří prompt, který modelu zadá instrukce pro generování požadovaného Python kódu.
3. Odešle prompt modelu a získá vygenerovaný kód.
4. Extrahuje a spustí vygenerovaný kód.
5. Zobrazí původní a zpracovaný obrázek.

Tento přístup využívá sílu AI k automatizaci úkolů zpracování obrázků, což zjednodušuje a urychluje dosažení vašich cílů.

[Ukázkové řešení kódu](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Pojďme si rozebrat, co celý kód krok za krokem dělá:

1. **Instalace potřebného balíčku**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Tento příkaz instaluje balíček `langchain_nvidia_ai_endpoints` a zajistí, že bude mít nejnovější verzi.

2. **Import nezbytných modulů**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Tyto importy zpřístupní potřebné moduly pro interakci s NVIDIA AI endpointy, bezpečné zpracování hesel, práci se souborovým systémem a kódování/dekódování dat ve formátu base64.

3. **Nastavení API klíče**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Tento kód ověřuje, zda je proměnná prostředí `NVIDIA_API_KEY` nastavena. Pokud ne, vyzve uživatele k bezpečnému zadání jeho API klíče.

4. **Definice modelu a cesty k obrázku**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Zde se nastaví model, který se bude používat, vytvoří se instance `ChatNVIDIA` se specifikovaným modelem a definuje se cesta k souboru obrázku.

5. **Vytvoření textového promptu**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Zde se definuje textový prompt, který dává modelu instrukce pro generování Python kódu na zpracování obrázku.

6. **Kódování obrázku do base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Tento kód načte soubor obrázku, zakóduje ho do base64 a vytvoří HTML tag obrázku s tímto zakódovaným obsahem.

7. **Spojení textu a obrázku do promptu**:
    ```python
    prompt = f"{text} {image}"
    ```
    Zde se kombinuje textový prompt a HTML tag obrázku do jednoho řetězce.

8. **Generování kódu pomocí ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Tento kód odešle prompt `ChatNVIDIA` a uloží odpověď modelu do proměnné `code`.

9. **Extrahování Python kódu z vygenerovaného obsahu**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Tento kód extrahuje skutečný Python kód z vygenerovaného obsahu tím, že odstraní markdown formátování.

10. **Spuštění vygenerovaného kódu**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Tento kód spustí extrahovaný Python kód jako podproces a zachytí jeho výstup.

11. **Zobrazení obrázků**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Tyto řádky zobrazí obrázky pomocí modulu `IPython.display`.

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových AI překladatelských služeb. I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nenese zodpovědnost za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.