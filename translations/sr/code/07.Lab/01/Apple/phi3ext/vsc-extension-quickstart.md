# Dobrodošli u svoju VS Code ekstenziju

## Šta se nalazi u folderu

* Ovaj folder sadrži sve fajlove potrebne za vašu ekstenziju.
* `package.json` - ovo je manifest fajl u kojem deklarišete svoju ekstenziju i komandu.
  * Primer dodatka registruje komandu i definiše njen naziv i ime komande. Sa ovim informacijama VS Code može prikazati komandu u paleti komandi. Još uvek nije potrebno učitavati dodatak.
* `src/extension.ts` - ovo je glavni fajl u kojem ćete implementirati svoju komandu.
  * Fajl eksportuje jednu funkciju, `activate`, koja se poziva prvi put kada se vaša ekstenzija aktivira (u ovom slučaju izvršavanjem komande). Unutar funkcije `activate` pozivamo `registerCommand`.
  * Funkciju koja sadrži implementaciju komande prosleđujemo kao drugi parametar funkciji `registerCommand`.

## Podešavanje

* Instalirajte preporučene ekstenzije (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner i dbaeumer.vscode-eslint).

## Brzi početak

* Pritisnite `F5` da otvorite novi prozor sa učitanom ekstenzijom.
* Pokrenite svoju komandu iz palete komandi pritiskom na (`Ctrl+Shift+P` ili `Cmd+Shift+P` na Mac-u) i otkucajte `Hello World`.
* Postavite tačke prekida (breakpoints) u svom kodu unutar fajla `src/extension.ts` kako biste debagirali svoju ekstenziju.
* Pronađite izlaz vaše ekstenzije u konzoli za debagovanje.

## Izmene

* Možete ponovo pokrenuti ekstenziju iz trake za debagovanje nakon što promenite kod u fajlu `src/extension.ts`.
* Takođe možete ponovo učitati (`Ctrl+R` ili `Cmd+R` na Mac-u) prozor VS Code-a sa vašom ekstenzijom kako biste učitali promene.

## Istražite API

* Možete otvoriti kompletan skup našeg API-ja otvaranjem fajla `node_modules/@types/vscode/index.d.ts`.

## Pokretanje testova

* Instalirajte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Pokrenite zadatak "watch" putem komande **Tasks: Run Task**. Uverite se da je ovo pokrenuto, inače testovi možda neće biti otkriveni.
* Otvorite prikaz Testing iz trake aktivnosti i kliknite na dugme "Run Test" ili koristite prečicu `Ctrl/Cmd + ; A`.
* Pogledajte izlaz rezultata testa u prikazu Test Results.
* Izmenite `src/test/extension.test.ts` ili kreirajte nove test fajlove unutar foldera `test`.
  * Pruženi test runner će uzeti u obzir samo fajlove koji odgovaraju šablonu imena `**.test.ts`.
  * Možete kreirati foldere unutar foldera `test` kako biste strukturirali svoje testove na bilo koji način.

## Dodatne mogućnosti

* Smanjite veličinu ekstenzije i poboljšajte vreme pokretanja [pakovanjem vaše ekstenzije](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Objavite svoju ekstenziju](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na VS Code tržištu ekstenzija.
* Automatizujte buildove postavljanjem [kontinuirane integracije](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако се трудимо да обезбедимо тачност, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна схватања или погрешна тумачења која могу произаћи из коришћења овог превода.