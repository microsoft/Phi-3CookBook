# Dobrodošli v svojem VS Code razširitvi

## Kaj je v mapi

* Ta mapa vsebuje vse datoteke, potrebne za vašo razširitev.
* `package.json` - to je manifestna datoteka, v kateri določite svojo razširitev in ukaze.
  * Vzorčni vtičnik registrira ukaz in določi njegov naslov ter ime ukaza. Na podlagi teh informacij lahko VS Code prikaže ukaz v ukazni paleti. Vtičnika še ni treba naložiti.
* `src/extension.ts` - to je glavna datoteka, kjer implementirate svoj ukaz.
  * Datoteka izvozi eno funkcijo, `activate`, ki se pokliče prvič, ko se vaša razširitev aktivira (v tem primeru z izvedbo ukaza). Znotraj funkcije `activate` pokličemo `registerCommand`.
  * Funkcijo, ki vsebuje implementacijo ukaza, posredujemo kot drugi parameter funkciji `registerCommand`.

## Nastavitev

* Namestite priporočene razširitve (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner in dbaeumer.vscode-eslint).

## Takoj začnite z delom

* Pritisnite `F5`, da odprete novo okno z naloženo razširitvijo.
* Svoj ukaz zaženite iz ukazne palete s pritiskom (`Ctrl+Shift+P` ali `Cmd+Shift+P` na Macu) in vpisom `Hello World`.
* Nastavite točke prekinitve v svoji kodi znotraj `src/extension.ts`, da razhroščujete svojo razširitev.
* Izhod svoje razširitve poiščite v razhroščevalni konzoli.

## Uredite spremembe

* Razširitev lahko ponovno zaženete iz razhroščevalne orodne vrstice po spremembi kode v `src/extension.ts`.
* Okno VS Code z vašo razširitvijo lahko ponovno naložite (`Ctrl+R` ali `Cmd+R` na Macu), da naložite svoje spremembe.

## Raziščite API

* Celoten nabor našega API-ja lahko odprete, ko odprete datoteko `node_modules/@types/vscode/index.d.ts`.

## Zagon testov

* Namestite [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Zaženite nalogo "watch" prek ukaza **Tasks: Run Task**. Prepričajte se, da ta naloga teče, sicer testi morda ne bodo zaznani.
* Odprite pogled Testing iz aktivnosti in kliknite gumb "Run Test" ali uporabite bližnjico `Ctrl/Cmd + ; A`.
* Rezultate testov si oglejte v pogledu Test Results.
* Spremenite `src/test/extension.test.ts` ali ustvarite nove testne datoteke znotraj mape `test`.
  * Zagotovljen testni izvajalec bo upošteval samo datoteke, ki ustrezajo imenskemu vzorcu `**.test.ts`.
  * Znotraj mape `test` lahko ustvarite mape, da strukturirate svoje teste po želji.

## Razširite svoje znanje

* Zmanjšajte velikost razširitve in izboljšajte čas zagona z [združevanjem razširitve](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Objavite svojo razširitev](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na tržnici razširitev za VS Code.
* Avtomatizirajte gradnje z nastavitvijo [neprekinjene integracije](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj velja za avtoritativni vir. Za ključne informacije je priporočljivo profesionalno človeško prevajanje. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.