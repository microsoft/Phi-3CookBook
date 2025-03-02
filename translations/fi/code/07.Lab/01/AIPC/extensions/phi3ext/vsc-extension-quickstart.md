# Tervetuloa käyttämään VS Code -laajennustasi

## Mitä kansio sisältää

* Tämä kansio sisältää kaikki tiedostot, jotka ovat tarpeen laajennuksesi toimintaan.
* `package.json` - tämä on manifest-tiedosto, jossa määrittelet laajennuksesi ja komennon.
  * Esimerkkilaajennus rekisteröi komennon ja määrittää sen otsikon ja komennon nimen. Näiden tietojen avulla VS Code voi näyttää komennon komennopalettissa. Pluginia ei vielä tarvitse ladata.
* `src/extension.ts` - tämä on pääasiallinen tiedosto, jossa toteutat komennon.
  * Tiedosto vie yhden funktion, `activate`, joka kutsutaan ensimmäisellä kerralla, kun laajennus aktivoidaan (tässä tapauksessa komennon suorittamisella). `activate`-funktion sisällä kutsumme `registerCommand`.
  * Välitämme komennon toteutuksen sisältävän funktion toisena parametrina `registerCommand`:lle.

## Asetukset

* asenna suositellut laajennukset (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ja dbaeumer.vscode-eslint)

## Käynnistä heti

* Paina `F5` avataksesi uuden ikkunan, jossa laajennuksesi on ladattu.
* Suorita komento komennopalettista painamalla (`Ctrl+Shift+P` tai `Cmd+Shift+P` Macissa) ja kirjoittamalla `Hello World`.
* Aseta murto- eli breakpointit koodiisi `src/extension.ts`-tiedostossa debugataksesi laajennustasi.
* Löydät laajennuksesi tulosteen debug-konsolista.

## Tee muutoksia

* Voit käynnistää laajennuksen uudelleen debug-työkalupalkista, kun olet tehnyt muutoksia `src/extension.ts`-tiedostoon.
* Voit myös päivittää (`Ctrl+R` tai `Cmd+R` Macissa) VS Code -ikkunan laajennuksesi lataamiseksi uudelleen.

## Tutustu API:in

* Voit avata koko API-valikoimamme avaamalla tiedoston `node_modules/@types/vscode/index.d.ts`.

## Suorita testejä

* Asenna [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Suorita "watch"-tehtävä **Tasks: Run Task** -komennon kautta. Varmista, että tämä on käynnissä, tai testejä ei ehkä löydy.
* Avaa Testaus-näkymä aktiviteettipalkista ja napsauta "Run Test" -painiketta tai käytä pikanäppäintä `Ctrl/Cmd + ; A`.
* Näet testitulosten tulosteen Test Results -näkymässä.
* Tee muutoksia `src/test/extension.test.ts`-tiedostoon tai luo uusia testitiedostoja `test`-kansioon.
  * Mukana tuleva test runner huomioi vain tiedostot, jotka vastaavat nimeämismallia `**.test.ts`.
  * Voit luoda kansioita `test`-kansioon järjestelläksesi testejä haluamallasi tavalla.

## Mene pidemmälle

* Pienennä laajennuksen kokoa ja paranna käynnistysaikaa [paketoimalla laajennuksesi](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Julkaise laajennuksesi](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) VS Code -laajennusmarkkinapaikalle.
* Automatisoi rakennusprosessit ottamalla käyttöön [Jatkuva integraatio](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälykäännöspalveluilla. Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisten tietojen osalta suositellaan ammattimaista ihmisen tekemää käännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.