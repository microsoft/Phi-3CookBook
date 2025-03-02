# Tervetuloa VS Code -laajennukseesi

## Mitä kansio sisältää

* Tämä kansio sisältää kaikki tiedostot, joita laajennuksesi tarvitsee.
* `package.json` - tämä on manifestitiedosto, jossa määrittelet laajennuksesi ja komennon.
  * Esimerkkilaajennus rekisteröi komennon ja määrittelee sen otsikon ja komennon nimen. Näiden tietojen avulla VS Code voi näyttää komennon komentovalikossa. Pluginia ei tarvitse vielä ladata.
* `src/extension.ts` - tämä on pääasiallinen tiedosto, jossa toteutat komennon toiminnallisuuden.
  * Tiedosto vie yhden funktion, `activate`, jota kutsutaan ensimmäisellä kerralla, kun laajennuksesi aktivoidaan (tässä tapauksessa komennon suorittamisen yhteydessä). `activate`-funktiossa kutsumme `registerCommand`.
  * Annamme komennon toteutuksen sisältävän funktion toisena parametrina `registerCommand`-funktiolle.

## Asennus

* Asenna suositellut laajennukset (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ja dbaeumer.vscode-eslint).

## Käyttöönotto heti

* Paina `F5` avataksesi uuden ikkunan, jossa laajennuksesi on ladattu.
* Suorita komento komentovalikosta painamalla (`Ctrl+Shift+P` tai `Cmd+Shift+P` Macilla) ja kirjoittamalla `Hello World`.
* Aseta koodisi sisälle `src/extension.ts` -tiedostoon pysäytyspisteitä debugataksesi laajennustasi.
* Löydät laajennuksesi tuottaman tulosteen debug-konsolista.

## Muutosten tekeminen

* Voit käynnistää laajennuksen uudelleen debug-työkaluriviltä, kun olet tehnyt muutoksia tiedostoon `src/extension.ts`.
* Voit myös ladata (`Ctrl+R` tai `Cmd+R` Macilla) VS Code -ikkunan uudelleen, jotta muutokset tulevat voimaan.

## API:n tutkiminen

* Voit avata koko API:n, kun avaat tiedoston `node_modules/@types/vscode/index.d.ts`.

## Testien suorittaminen

* Asenna [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Suorita "watch"-tehtävä **Tasks: Run Task** -komennon kautta. Varmista, että tämä tehtävä on käynnissä, muuten testejä ei ehkä löydetä.
* Avaa Testaus-näkymä aktiviteettipalkista ja napsauta "Run Test" -painiketta tai käytä pikanäppäintä `Ctrl/Cmd + ; A`.
* Näet testitulokset Testitulokset-näkymässä.
* Tee muutoksia tiedostoon `src/test/extension.test.ts` tai luo uusia testitiedostoja kansioon `test`.
  * Tarjottu testiajo-ohjelma huomioi vain tiedostot, jotka vastaavat nimeämismallia `**.test.ts`.
  * Voit luoda kansioita `test`-kansioon järjestääksesi testit haluamallasi tavalla.

## Mene pidemmälle

* Pienennä laajennuksen kokoa ja paranna käynnistysaikaa [niputtamalla laajennuksesi](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Julkaise laajennuksesi](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) VS Code -laajennusmarkkinapaikalla.
* Automatisoi rakennusprosessi asettamalla [Jatkuva integraatio](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälykäännöspalveluilla. Vaikka pyrimme tarkkuuteen, on hyvä olla tietoinen siitä, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisten tietojen osalta suositellaan ammattimaista, ihmisen tekemää käännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.