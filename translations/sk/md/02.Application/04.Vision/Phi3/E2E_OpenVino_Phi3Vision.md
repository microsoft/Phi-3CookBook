Táto ukážka demonštruje, ako použiť predtrénovaný model na generovanie Python kódu na základe obrázka a textového zadania.

[Ukážkový kód](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Tu je podrobný postup:

1. **Importy a nastavenie**:
   - Importujú sa potrebné knižnice a moduly, vrátane `requests`, `PIL` na spracovanie obrázkov a `transformers` na prácu s modelom a jeho spracovanie.

2. **Načítanie a zobrazenie obrázka**:
   - Obrázkový súbor (`demo.png`) sa otvorí pomocou knižnice `PIL` a zobrazí sa.

3. **Definovanie zadania**:
   - Vytvorí sa správa, ktorá obsahuje obrázok a požiadavku na generovanie Python kódu na spracovanie obrázka a jeho uloženie pomocou `plt` (matplotlib).

4. **Načítanie procesora**:
   - `AutoProcessor` sa načíta z predtrénovaného modelu, ktorý je špecifikovaný v adresári `out_dir`. Tento procesor spracuje textové a obrázkové vstupy.

5. **Vytvorenie zadania**:
   - Metóda `apply_chat_template` sa použije na formátovanie správy do zadania vhodného pre model.

6. **Spracovanie vstupov**:
   - Zadanie a obrázok sa spracujú na tensory, ktoré model dokáže pochopiť.

7. **Nastavenie parametrov generovania**:
   - Definujú sa argumenty pre proces generovania modelu, vrátane maximálneho počtu nových tokenov na generovanie a či sa má výstup generovať náhodne.

8. **Generovanie kódu**:
   - Model vygeneruje Python kód na základe vstupov a parametrov generovania. `TextStreamer` sa použije na spracovanie výstupu, pričom sa vynechá zadanie a špeciálne tokeny.

9. **Výstup**:
   - Vygenerovaný kód sa vytlačí, pričom by mal obsahovať Python kód na spracovanie obrázka a jeho uloženie podľa zadania.

Táto ukážka ilustruje, ako využiť predtrénovaný model pomocou OpenVino na dynamické generovanie kódu na základe vstupov od používateľa a obrázkov.

**Upozornenie**:  
Tento dokument bol preložený pomocou služieb strojového prekladu založených na umelej inteligencii. Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj by sa mal považovať pôvodný dokument v jeho rodnom jazyku. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.