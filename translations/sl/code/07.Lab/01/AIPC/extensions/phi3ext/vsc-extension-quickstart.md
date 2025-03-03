# Dobrodošli v vaši razširitvi za VS Code

## Kaj je v mapi

* Ta mapa vsebuje vse datoteke, potrebne za vašo razširitev.
* `package.json` - to je manifestna datoteka, v kateri definirate svojo razširitev in ukaz.
  * Vzorčni vtičnik registrira ukaz in določi njegov naslov ter ime ukaza. S temi informacijami lahko VS Code prikaže ukaz v paleti ukazov. Vtičnik še ni treba naložiti.
* `src/extension.ts` - to je glavna datoteka, kjer boste zagotovili implementacijo svojega ukaza.
  * Datoteka izvozi eno funkcijo, `activate`, ki se pokliče prvič, ko se vaša razširitev aktivira (v tem primeru z izvajanjem ukaza). Znotraj funkcije `activate` kličemo `registerCommand`.
  * Funkcijo, ki vsebuje implementacijo ukaza, posredujemo kot drugi parameter funkciji `registerCommand`.

## Nastavitev

* Namestite priporočene razširitve (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner in dbaeumer.vscode-eslint).


## Začnite takoj

* Pritisnite `F5`, da odprete novo okno z naloženo razširitvijo.
* Zaženite svoj ukaz iz palete ukazov s pritiskom (`Ctrl+Shift+P` ali `Cmd+Shift+P` na Macu) in vnosom `Hello World`.
* Nastavite točke zaustavitve v svoji kodi znotraj `src/extension.ts`, da razhroščujete svojo razširitev.
* Najdite izhod iz svoje razširitve v konzoli za razhroščevanje.

## Naredite spremembe

* Razširitev lahko ponovno zaženete iz orodne vrstice za razhroščevanje po spremembi kode v `src/extension.ts`.
* Prav tako lahko ponovno naložite (`Ctrl+R` ali `Cmd+R` na Macu) okno VS Code z vašo razširitvijo, da naložite spremembe.


## Raziščite API

* Celoten nabor našega API-ja lahko odprete, ko odprete datoteko `node_modules/@types/vscode/index.d.ts`.

## Zaženite teste

* Namestite [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Zaženite nalogo "watch" prek ukaza **Tasks: Run Task**. Prepričajte se, da je to v teku, sicer testi morda ne bodo zaznani.
* Odprite pogled za testiranje v orodni vrstici aktivnosti in kliknite gumb "Run Test", ali pa uporabite bližnjico `Ctrl/Cmd + ; A`.
* Oglejte si izhod rezultatov testa v pogledu rezultatov testov.
* Naredite spremembe v `src/test/extension.test.ts` ali ustvarite nove testne datoteke znotraj mape `test`.
  * Zagotovljeni izvajalnik testov bo upošteval le datoteke, ki ustrezajo imenskemu vzorcu `**.test.ts`.
  * Znotraj mape `test` lahko ustvarite mape, da strukturirate svoje teste po želji.

## Razširite svoje znanje

* Zmanjšajte velikost razširitve in izboljšajte čas zagona z [združevanjem vaše razširitve](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Objavite svojo razširitev](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) na tržnici razširitev za VS Code.
* Avtomatizirajte gradnje z nastavitvijo [neprekinjene integracije](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, prosimo, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni prevod s strani človeka. Ne prevzemamo odgovornosti za morebitna nesporazuma ali napačne razlage, ki izhajajo iz uporabe tega prevoda.