### Példa Forgatókönyv

Képzeljük el, hogy van egy képed (`demo.png`), és Python kódot szeretnél generálni, amely feldolgozza ezt a képet, majd elmenti egy új verzióját (`phi-3-vision.jpg`).

A fent bemutatott kód ezt a folyamatot automatizálja az alábbi lépésekkel:

1. A környezet és a szükséges beállítások előkészítése.
2. Egy olyan prompt létrehozása, amely utasítja a modellt a szükséges Python kód generálására.
3. A prompt elküldése a modellnek és a generált kód begyűjtése.
4. A generált kód kinyerése és futtatása.
5. Az eredeti és a feldolgozott képek megjelenítése.

Ez a megközelítés az AI erejét használja fel a képfeldolgozási feladatok automatizálására, így gyorsabbá és egyszerűbbé téve céljaid elérését.

[Mintakód Megoldás](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Nézzük meg lépésről lépésre, mit csinál a teljes kód:

1. **Szükséges Csomag Telepítése**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Ez a parancs telepíti a `langchain_nvidia_ai_endpoints` csomagot, biztosítva, hogy a legfrissebb verzió legyen használatban.

2. **Szükséges Modulok Importálása**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Ezek az importálások biztosítják a szükséges modulokat az NVIDIA AI végpontokkal való kommunikációhoz, jelszavak biztonságos kezeléséhez, az operációs rendszerrel való interakcióhoz, valamint az adatok base64 formátumban történő kódolásához/dekódolásához.

3. **API Kulcs Beállítása**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Ez a kód ellenőrzi, hogy az `NVIDIA_API_KEY` környezeti változó be van-e állítva. Ha nincs, akkor biztonságosan bekéri a felhasználótól az API kulcsot.

4. **Modell és Képfájl Útvonal Meghatározása**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Ez beállítja a használni kívánt modellt, létrehoz egy `ChatNVIDIA` példányt a megadott modellel, és meghatározza a képfájl elérési útját.

5. **Szöveges Prompt Létrehozása**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Ez meghatároz egy szöveges promptot, amely utasítja a modellt, hogy generáljon Python kódot egy kép feldolgozására.

6. **Kép Base64 Formátumba Kódolása**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Ez a kód beolvassa a képfájlt, base64 formátumba kódolja, és létrehoz egy HTML kép címkét a kódolt adatokkal.

7. **Szöveg és Kép Kombinálása a Promptban**:
    ```python
    prompt = f"{text} {image}"
    ```
    Ez egyesíti a szöveges promptot és a HTML kép címkét egyetlen karakterláncba.

8. **Kód Generálása a ChatNVIDIA Segítségével**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Ez a kód elküldi a promptot a `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` karakterláncnak.

9. **Python Kód Kinyerése a Generált Tartalomból**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Ez a kód kinyeri a tényleges Python kódot a generált tartalomból azáltal, hogy eltávolítja a markdown formázást.

10. **Generált Kód Futtatása**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Ez futtatja a kinyert Python kódot egy alfolyamatként, és rögzíti annak kimenetét.

11. **Képek Megjelenítése**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Ezek a sorok az `IPython.display` modul segítségével jelenítik meg a képeket.

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítószolgáltatások segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatizált fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt a professzionális emberi fordítás igénybevétele. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.