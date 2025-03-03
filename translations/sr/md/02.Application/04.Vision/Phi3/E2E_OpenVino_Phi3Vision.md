Ovaj demo prikazuje kako koristiti unapred trenirani model za generisanje Python koda na osnovu slike i tekstualnog upita.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Evo objašnjenja korak po korak:

1. **Uvoz i Podešavanje**:
   - Neophodne biblioteke i moduli se uvoze, uključujući `requests`, `PIL` za obradu slika i `transformers` za rad sa modelom i procesiranje.

2. **Učitavanje i Prikazivanje Slike**:
   - Fajl sa slikom (`demo.png`) se otvara koristeći biblioteku `PIL` i prikazuje.

3. **Definisanje Upita**:
   - Kreira se poruka koja uključuje sliku i zahtev za generisanje Python koda za obradu slike i njeno čuvanje koristeći `plt` (matplotlib).

4. **Učitavanje Procesora**:
   - `AutoProcessor` se učitava iz unapred treniranog modela specificiranog u direktorijumu `out_dir`. Ovaj procesor će obraditi tekstualne i slikovne ulaze.

5. **Kreiranje Upita**:
   - Metoda `apply_chat_template` se koristi za formatiranje poruke u upit koji je pogodan za model.

6. **Obrada Ulaza**:
   - Upit i slika se procesiraju u tenzore koje model može da razume.

7. **Podešavanje Parametara Generisanja**:
   - Definišu se parametri za proces generisanja modela, uključujući maksimalan broj novih tokena koji treba da se generišu i da li treba koristiti uzorkovanje za izlaz.

8. **Generisanje Koda**:
   - Model generiše Python kod na osnovu ulaza i definisanih parametara generisanja. `TextStreamer` se koristi za obradu izlaza, preskačući upit i specijalne tokene.

9. **Izlaz**:
   - Generisani kod se štampa, a trebalo bi da sadrži Python kod za obradu slike i njeno čuvanje, kao što je specificirano u upitu.

Ovaj demo ilustruje kako iskoristiti unapred trenirani model koristeći OpenVino za dinamičko generisanje koda na osnovu korisničkog unosa i slika.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако се трудимо да обезбедимо тачност, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неразумевања настала коришћењем овог превода.