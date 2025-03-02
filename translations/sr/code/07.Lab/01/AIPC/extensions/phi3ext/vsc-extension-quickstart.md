# Dobrodošli u svoju VS Code ekstenziju

## Šta se nalazi u folderu

* Ovaj folder sadrži sve fajlove neophodne za vašu ekstenziju.
* `package.json` - ovo je manifest fajl u kojem deklarisujete svoju ekstenziju i komandu.
  * Primer dodatka registruje komandu i definiše njen naziv i ime komande. Sa ovim informacijama, VS Code može prikazati komandu u komandnoj paleti. Još uvek nije potrebno da se dodatak učita.
* `src/extension.ts` - ovo je glavni fajl gde ćete obezbediti implementaciju svoje komande.
  * Fajl eksportuje jednu funkciju, `activate`, koja se poziva prvi put kada se vaša ekstenzija aktivira (u ovom slučaju izvršavanjem komande). Unutar funkcije `activate` pozivamo `registerCommand`.
  * Prolazimo funkciju koja sadrži implementaciju komande kao drugi parametar za `registerCommand`.

## Podešavanje

* Instalirajte preporučene ekstenzije (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner i dbaeumer.vscode-eslint).

## Pokrenite ekstenziju odmah

* Pritisnite `F5` da biste otvorili novi prozor sa učitanom ekstenzijom.
* Pokrenite svoju komandu iz komandne palete pritiskom na (`Ctrl+Shift+P` ili `Cmd+Shift+P` na Mac-u) i kucanjem `Hello World`.
* Postavite breakpoint-ove u svom kodu unutar `src/extension.ts` da biste debug-ovali svoju ekstenziju.
* Pronađite izlaz iz svoje ekstenzije u debug konzoli.

## Izmenite kod

* Možete ponovo pokrenuti ekstenziju iz debug trake nakon što promenite kod u `src/extension.ts`.
* Takođe možete ponovo učitati (`Ctrl+R` ili `Cmd+R` na Mac-u) prozor VS Code-a sa svojom ekstenzijom da biste učitali promene.

## Istražite API

* Možete otvoriti kompletan set našeg API-ja kada otvorite fajl `node_modules/@types/vscode/index.d.ts`.

## Pokrenite testove

* Instalirajte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Pokrenite zadatak "watch" putem komande **Tasks: Run Task**. Uverite se da je ovo pokrenuto, inače testovi možda neće biti otkriveni.
* Otvorite pogled za testiranje iz trake aktivnosti i kliknite na dugme "Run Test", ili koristite prečicu `Ctrl/Cmd + ; A`.
* Pogledajte rezultate testova u prikazu rezultata testiranja.
* Izmenite `src/test/extension.test.ts` ili kreirajte nove test fajlove unutar foldera `test`.
  * Pruženi test pokretač će uzeti u obzir samo fajlove koji odgovaraju šablonu imena `**.test.ts`.
  * Možete kreirati foldere unutar foldera `test` kako biste strukturisali svoje testove na bilo koji način.

## Idite dalje

* Smanjite veličinu ekstenzije i poboljšajte vreme pokretanja tako što ćete [pakovati svoju ekstenziju](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Objavite svoju ekstenziju](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) na VS Code tržištu ekstenzija.
* Automatizujte build-ove podešavanjem [Kontinuirane Integracije](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако тежимо ка тачности, молимо вас да будете свесни да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неразумевања настала употребом овог превода.