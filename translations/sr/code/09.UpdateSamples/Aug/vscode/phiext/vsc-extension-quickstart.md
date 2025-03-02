# Dobrodošli u svoju VS Code ekstenziju

## Šta se nalazi u folderu

* Ovaj folder sadrži sve fajlove potrebne za vašu ekstenziju.
* `package.json` - ovo je manifest fajl u kojem definišete svoju ekstenziju i komandu.
  * Primer dodatka registruje komandu i definiše njen naslov i ime komande. Na osnovu ovih informacija, VS Code može da prikaže komandu u komandnoj paleti. Za sada nije potrebno da se dodatak učitava.
* `src/extension.ts` - ovo je glavni fajl gde ćete obezbediti implementaciju svoje komande.
  * Fajl eksportuje jednu funkciju, `activate`, koja se poziva prvi put kada se vaša ekstenzija aktivira (u ovom slučaju izvršavanjem komande). Unutar funkcije `activate` pozivamo `registerCommand`.
  * Funkciju koja sadrži implementaciju komande prosleđujemo kao drugi parametar funkciji `registerCommand`.

## Postavljanje

* Instalirajte preporučene ekstenzije (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner i dbaeumer.vscode-eslint)

## Pokrenite i koristite odmah

* Pritisnite `F5` da otvorite novi prozor sa vašom učitanom ekstenzijom.
* Pokrenite svoju komandu iz komandne palete pritiskom na (`Ctrl+Shift+P` ili `Cmd+Shift+P` na Mac-u) i ukucavanjem `Hello World`.
* Postavite breakpoint-ove u svom kodu unutar `src/extension.ts` kako biste debug-ovali svoju ekstenziju.
* Pronađite izlaz iz svoje ekstenzije u debug konzoli.

## Izmenite

* Možete ponovo pokrenuti ekstenziju iz debug trake nakon što izmenite kod u `src/extension.ts`.
* Takođe možete ponovo učitati (`Ctrl+R` ili `Cmd+R` na Mac-u) prozor VS Code-a sa vašom ekstenzijom kako biste učitali izmene.

## Istražite API

* Možete otvoriti kompletan API kada otvorite fajl `node_modules/@types/vscode/index.d.ts`.

## Pokrenite testove

* Instalirajte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Pokrenite zadatak "watch" putem komande **Tasks: Run Task**. Uverite se da je ovo pokrenuto, jer testovi možda neće biti prepoznati.
* Otvorite Testing prikaz iz trake aktivnosti i kliknite na dugme "Run Test", ili koristite prečicu `Ctrl/Cmd + ; A`.
* Pogledajte izlaz rezultata testiranja u prikazu Test Results.
* Izmenite `src/test/extension.test.ts` ili kreirajte nove test fajlove unutar foldera `test`.
  * Obezbeđeni test runner će uzeti u obzir samo fajlove koji odgovaraju šablonu imena `**.test.ts`.
  * Možete kreirati foldere unutar `test` foldera kako biste organizovali svoje testove na bilo koji način.

## Idite dalje

* Smanjite veličinu ekstenzije i poboljšajte vreme pokretanja [pakovanjem svoje ekstenzije](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Objavite svoju ekstenziju](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na VS Code tržištu ekstenzija.
* Automatizujte izgradnju postavljanjem [Kontinuirane integracije](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако тежимо прецизности, имајте у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било какве неспоразуме или погрешна тумачења настала употребом овог превода.