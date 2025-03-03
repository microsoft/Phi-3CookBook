Ez a bemutató azt mutatja be, hogyan használhatunk egy előre betanított modellt Python kód generálására egy kép és egy szöveges utasítás alapján.

[Mintakód](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Íme a lépések részletes magyarázata:

1. **Importálás és Beállítás**:
   - A szükséges könyvtárak és modulok importálása történik, beleértve a `requests` és `PIL` képfeldolgozáshoz, valamint a `transformers` a modell kezeléséhez és feldolgozáshoz.

2. **A Kép Betöltése és Megjelenítése**:
   - Egy kép fájl (`demo.png`) megnyitása a `PIL` könyvtár segítségével, majd annak megjelenítése.

3. **Az Utasítás Meghatározása**:
   - Egy üzenet készítése, amely tartalmazza a képet, és egy kérést Python kód generálására a kép feldolgozásához és mentéséhez a `plt` (matplotlib) használatával.

4. **A Feldolgozó Betöltése**:
   - A `AutoProcessor` betöltése egy előre betanított modellből, amelyet a `out_dir` könyvtár határoz meg. Ez a feldolgozó fogja kezelni a szöveges és képi bemeneteket.

5. **Az Utasítás Létrehozása**:
   - Az `apply_chat_template` metódus segítségével az üzenet olyan formátumúvá alakítása, amely alkalmas a modell számára.

6. **A Bemenetek Feldolgozása**:
   - Az utasítás és a kép tensorokká alakítása, amelyeket a modell képes értelmezni.

7. **Generálási Paraméterek Beállítása**:
   - A modell generálási folyamatához szükséges paraméterek meghatározása, beleértve az újonnan generált tokenek maximális számát és az output mintavételezésének beállítását.

8. **A Kód Generálása**:
   - A modell Python kódot generál a bemenetek és a generálási paraméterek alapján. A `TextStreamer` használatos az output kezeléséhez, figyelmen kívül hagyva az utasítást és a speciális tokeneket.

9. **Eredmény**:
   - A generált kód kiírásra kerül, amelynek tartalmaznia kell a kép feldolgozására és mentésére vonatkozó Python kódot, ahogyan azt az utasítás meghatározta.

Ez a bemutató szemlélteti, hogyan használhatunk egy előre betanított modellt az OpenVino segítségével dinamikusan kódot generálni a felhasználói bemenetek és képek alapján.

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítási szolgáltatások segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatizált fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.