# Tervetuloa VS Code -laajennukseesi

## Mitä kansiossa on

* Tämä kansio sisältää kaikki tiedostot, joita laajennuksesi tarvitsee.
* `package.json` - tämä on manifestitiedosto, jossa määrittelet laajennuksesi ja komennon.
  * Esimerkkilaajennus rekisteröi komennon ja määrittelee sen otsikon ja komennon nimen. Näiden tietojen avulla VS Code voi näyttää komennon komennonhallinnassa. Pluginia ei tarvitse vielä ladata.
* `src/extension.ts` - tämä on pääasiallinen tiedosto, jossa toteutat komennon toiminnallisuuden.
  * Tiedosto vie yhden funktion, `activate`, joka kutsutaan ensimmäisellä kerralla, kun laajennuksesi aktivoidaan (tässä tapauksessa suorittamalla komento). `activate`-funktiossa kutsutaan `registerCommand`.
  * Komennon toteutuksen sisältävä funktio välitetään `registerCommand`:lle toisena parametrina.

## Asennus

* Asenna suositellut laajennukset (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ja dbaeumer.vscode-eslint).

## Pääse alkuun heti

* Paina `F5` avataksesi uuden ikkunan, jossa laajennuksesi on ladattu.
* Suorita komento komennonhallinnasta painamalla (`Ctrl+Shift+P` tai `Cmd+Shift+P` Macilla) ja kirjoittamalla `Hello World`.
* Aseta taukopisteitä koodiisi `src/extension.ts`-tiedostossa, jotta voit debugata laajennustasi.
* Löydät laajennuksesi tulosteet debug-konsolista.

## Tee muutoksia

* Voit käynnistää laajennuksen uudelleen debug-työkalupalkista, kun olet tehnyt muutoksia `src/extension.ts`-tiedostoon.
* Voit myös päivittää (`Ctrl+R` tai `Cmd+R` Macilla) VS Code -ikkunan laajennuksesi kanssa ladataksesi muutokset.

## Tutustu API:in

* Voit avata koko API-valikoimamme avaamalla tiedoston `node_modules/@types/vscode/index.d.ts`.

## Suorita testejä

* Asenna [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Suorita "watch"-tehtävä **Tasks: Run Task** -komennolla. Varmista, että tämä on käynnissä, tai testejä ei ehkä löydy.
* Avaa Testaus-näkymä toimintopalkista ja napsauta "Run Test" -painiketta tai käytä pikanäppäintä `Ctrl/Cmd + ; A`.
* Katso testitulosten tuloste Testitulokset-näkymästä.
* Tee muutoksia `src/test/extension.test.ts`-tiedostoon tai luo uusia testitiedostoja `test`-kansioon.
  * Mukana tuleva testirunneri huomioi vain tiedostot, jotka vastaavat nimeämismallia `**.test.ts`.
  * Voit luoda kansioita `test`-kansion sisälle järjestääksesi testisi haluamallasi tavalla.

## Mene pidemmälle

* Pienennä laajennuksen kokoa ja paranna käynnistysaikaa [paketoimalla laajennuksesi](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Julkaise laajennuksesi](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) VS Code -laajennusmarkkinapaikalla.
* Automatisoi buildit ottamalla käyttöön [Jatkuva integraatio](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälykäännöspalveluilla. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaisen ihmiskääntäjän käyttöä. Emme ole vastuussa mahdollisista väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.