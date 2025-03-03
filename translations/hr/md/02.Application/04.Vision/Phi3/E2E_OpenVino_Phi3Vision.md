Ovaj demo prikazuje kako koristiti unaprijed istrenirani model za generiranje Python koda na temelju slike i tekstualnog upita.

[Primjer koda](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Evo objašnjenja korak po korak:

1. **Uvoz i postavljanje**:
   - Potrebne biblioteke i moduli se uvoze, uključujući `requests`, `PIL` za obradu slika i `transformers` za rad s modelom i obradom.

2. **Učitavanje i prikaz slike**:
   - Datoteka slike (`demo.png`) otvara se pomoću biblioteke `PIL` i prikazuje.

3. **Definiranje upita**:
   - Kreira se poruka koja uključuje sliku i zahtjev za generiranje Python koda za obradu slike i spremanje pomoću `plt` (matplotlib).

4. **Učitavanje procesora**:
   - `AutoProcessor` se učitava iz unaprijed istreniranog modela specificiranog u direktoriju `out_dir`. Ovaj procesor obrađuje tekstualne i slikovne ulaze.

5. **Kreiranje upita**:
   - Metoda `apply_chat_template` koristi se za formatiranje poruke u upit koji je prikladan za model.

6. **Obrada ulaza**:
   - Upit i slika obrađuju se u tenzore koje model može razumjeti.

7. **Postavljanje parametara generiranja**:
   - Definiraju se parametri za proces generiranja modela, uključujući maksimalni broj novih tokena koji će se generirati i hoće li se koristiti uzorkovanje izlaza.

8. **Generiranje koda**:
   - Model generira Python kod na temelju ulaza i parametara generiranja. `TextStreamer` koristi se za obradu izlaza, preskačući upit i posebne tokene.

9. **Izlaz**:
   - Generirani kod se ispisuje, a trebao bi sadržavati Python kod za obradu slike i njeno spremanje kako je specificirano u upitu.

Ovaj demo pokazuje kako iskoristiti unaprijed istrenirani model koristeći OpenVino za dinamičko generiranje koda na temelju korisničkog unosa i slika.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluga za strojno prevođenje. Iako nastojimo osigurati točnost, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.