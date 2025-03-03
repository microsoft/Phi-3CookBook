# Dobrodošli v svoji razširitvi za VS Code

## Kaj je v mapi

* Ta mapa vsebuje vse datoteke, ki so potrebne za vašo razširitev.
* `package.json` - to je manifestna datoteka, v kateri definirate svojo razširitev in ukaz.
  * Vzorčni vtičnik registrira ukaz in določi njegov naslov ter ime ukaza. S temi informacijami lahko VS Code prikaže ukaz v ukazni paleti. Vtičnika še ni treba naložiti.
* `src/extension.ts` - to je glavna datoteka, kjer boste implementirali svoj ukaz.
  * Datoteka izvozi eno funkcijo, `activate`, ki se pokliče prvič, ko se vaša razširitev aktivira (v tem primeru z izvedbo ukaza). Znotraj funkcije `activate` kličemo `registerCommand`.
  * Funkcijo, ki vsebuje implementacijo ukaza, posredujemo kot drugi parameter funkciji `registerCommand`.

## Nastavitev

* Namestite priporočene razširitve (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner in dbaeumer.vscode-eslint).

## Takoj začnite z delom

* Pritisnite `F5`, da odprete novo okno z naloženo razširitvijo.
* Izvedite svoj ukaz iz ukazne palete s pritiskom na (`Ctrl+Shift+P` ali `Cmd+Shift+P` na Macu) in vtipkajte `Hello World`.
* Nastavite točke prekinitve v svoji kodi znotraj `src/extension.ts` za odpravljanje napak v vaši razširitvi.
* Izhod iz vaše razširitve najdete v konzoli za odpravljanje napak.

## Spremenite kodo

* Razširitev lahko znova zaženete iz orodne vrstice za odpravljanje napak po spremembi kode v `src/extension.ts`.
* Okno VS Code z vašo razširitvijo lahko znova naložite (`Ctrl+R` ali `Cmd+R` na Macu), da naložite svoje spremembe.

## Raziščite API

* Celoten nabor našega API-ja lahko odprete, ko odprete datoteko `node_modules/@types/vscode/index.d.ts`.

## Izvedite teste

* Namestite [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Zaženite nalogo "watch" prek ukaza **Tasks: Run Task**. Poskrbite, da je to aktivno, sicer testi morda ne bodo zaznani.
* Odprite pogled za testiranje iz orodne vrstice in kliknite gumb "Run Test" ali uporabite bližnjico `Ctrl/Cmd + ; A`.
* Rezultate testov si oglejte v pogledu Test Results.
* Spremenite `src/test/extension.test.ts` ali ustvarite nove testne datoteke znotraj mape `test`.
  * Zagotovljeni izvajalec testov bo upošteval samo datoteke, ki ustrezajo vzorcu imena `**.test.ts`.
  * Znotraj mape `test` lahko ustvarite mape za poljubno strukturiranje testov.

## Nadaljujte

* Zmanjšajte velikost razširitve in izboljšajte čas zagona z [združevanjem svoje razširitve](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Objavite svojo razširitev](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na tržnici razširitev za VS Code.
* Avtomatizirajte gradnje z nastavitvijo [neprekinjene integracije](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitev strojnega prevajanja na osnovi umetne inteligence. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.