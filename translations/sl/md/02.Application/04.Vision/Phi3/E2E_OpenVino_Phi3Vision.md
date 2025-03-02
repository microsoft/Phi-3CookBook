Ta demo prikazuje, kako uporabiti vnaprej izurjen model za generiranje Python kode na podlagi slike in besedilnega poziva.

[Primer kode](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Tukaj je razlaga po korakih:

1. **Uvoz in priprava**:
   - Uvožene so potrebne knjižnice in moduli, vključno z `requests`, `PIL` za obdelavo slik in `transformers` za upravljanje modela in obdelavo.

2. **Nalaganje in prikaz slike**:
   - Datoteka slike (`demo.png`) se odpre z uporabo knjižnice `PIL` in prikaže.

3. **Definiranje poziva**:
   - Ustvari se sporočilo, ki vključuje sliko in zahtevo za generiranje Python kode za obdelavo slike in njeno shranjevanje z uporabo `plt` (matplotlib).

4. **Nalaganje procesorja**:
   - `AutoProcessor` se naloži iz vnaprej izurjenega modela, ki je določen v imeniku `out_dir`. Ta procesor bo obravnaval besedilne in slikovne vnose.

5. **Ustvarjanje poziva**:
   - Metoda `apply_chat_template` se uporabi za oblikovanje sporočila v poziv, primeren za model.

6. **Obdelava vnosov**:
   - Poziv in slika se obdelata v tenzorje, ki jih model lahko razume.

7. **Nastavitev argumentov za generiranje**:
   - Določeni so argumenti za proces generiranja modela, vključno z največjim številom novih generiranih tokenov in ali naj se izhod vzorči.

8. **Generiranje kode**:
   - Model generira Python kodo na podlagi vhodov in argumentov za generiranje. `TextStreamer` se uporabi za obdelavo izhoda, pri čemer se preskočijo poziv in posebni tokeni.

9. **Izhod**:
   - Generirana koda se izpiše, kar bi moralo vključevati Python kodo za obdelavo slike in njeno shranjevanje, kot je določeno v pozivu.

Ta demo prikazuje, kako uporabiti vnaprej izurjen model z OpenVino za dinamično generiranje kode na podlagi uporabniških vnosov in slik.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj velja za avtoritativni vir. Za ključne informacije priporočamo strokovno človeško prevajanje. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.