Tato ukázka předvádí, jak použít předtrénovaný model k vygenerování Python kódu na základě obrázku a textového zadání.

[Ukázkový kód](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Zde je podrobný popis krok za krokem:

1. **Importy a nastavení**:
   - Jsou importovány potřebné knihovny a moduly, včetně `requests`, `PIL` pro zpracování obrázků a `transformers` pro práci s modelem a jeho zpracování.

2. **Načtení a zobrazení obrázku**:
   - Soubor s obrázkem (`demo.png`) je otevřen pomocí knihovny `PIL` a zobrazen.

3. **Definování zadání**:
   - Vytvoří se zpráva, která obsahuje obrázek a požadavek na vygenerování Python kódu pro zpracování obrázku a jeho uložení pomocí `plt` (matplotlib).

4. **Načtení procesoru**:
   - `AutoProcessor` je načten z předtrénovaného modelu specifikovaného v adresáři `out_dir`. Tento procesor bude zpracovávat textové i obrazové vstupy.

5. **Vytvoření zadání**:
   - Metoda `apply_chat_template` je použita k formátování zprávy do podoby vhodné pro model.

6. **Zpracování vstupů**:
   - Zadání a obrázek jsou převedeny na tensory, kterým model rozumí.

7. **Nastavení parametrů generování**:
   - Jsou definovány parametry pro proces generování modelu, včetně maximálního počtu nových tokenů a toho, zda má být výstup generován náhodně.

8. **Generování kódu**:
   - Model na základě vstupů a parametrů generování vytvoří Python kód. `TextStreamer` je použit k práci s výstupem, přeskočení zadání a speciálních tokenů.

9. **Výstup**:
   - Vygenerovaný kód je vytištěn, měl by zahrnovat Python kód pro zpracování obrázku a jeho uložení podle zadaných požadavků.

Tato ukázka demonstruje, jak využít předtrénovaný model s OpenVino pro dynamické generování kódu na základě uživatelského vstupu a obrázků.

**Prohlášení:**  
Tento dokument byl přeložen pomocí strojových AI překladových služeb. I když se snažíme o co největší přesnost, upozorňujeme, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nezodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.