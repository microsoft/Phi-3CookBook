# Dobrodošli u svoju VS Code ekstenziju

## Što se nalazi u mapi

* Ova mapa sadrži sve datoteke potrebne za vašu ekstenziju.
* `package.json` - ovo je manifest datoteka u kojoj deklarirate svoju ekstenziju i naredbu.
  * Uzorak dodatka registrira naredbu i definira njezin naslov i naziv naredbe. S ovim informacijama VS Code može prikazati naredbu u izborniku naredbi. Plugin se još uvijek ne mora učitati.
* `src/extension.ts` - ovo je glavna datoteka gdje ćete implementirati svoju naredbu.
  * Datoteka izvozi jednu funkciju, `activate`, koja se poziva prvi put kada se vaša ekstenzija aktivira (u ovom slučaju izvršavanjem naredbe). Unutar funkcije `activate` pozivamo `registerCommand`.
  * Funkciju koja sadrži implementaciju naredbe prosljeđujemo kao drugi parametar funkciji `registerCommand`.

## Postavljanje

* instalirajte preporučene ekstenzije (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner i dbaeumer.vscode-eslint)

## Pokrenite se odmah

* Pritisnite `F5` za otvaranje novog prozora s vašom učitanom ekstenzijom.
* Pokrenite svoju naredbu iz izbornika naredbi pritiskom na (`Ctrl+Shift+P` ili `Cmd+Shift+P` na Macu) i upisivanjem `Hello World`.
* Postavite točke prekida u svom kodu unutar `src/extension.ts` kako biste otklonili pogreške u svojoj ekstenziji.
* Pronađite izlaz iz svoje ekstenzije u konzoli za otklanjanje pogrešaka.

## Izvršite promjene

* Nakon izmjene koda u `src/extension.ts`, možete ponovno pokrenuti ekstenziju s alatne trake za otklanjanje pogrešaka.
* Također možete ponovno učitati (`Ctrl+R` ili `Cmd+R` na Macu) prozor VS Code-a s vašom ekstenzijom kako biste učitali promjene.

## Istražite API

* Možete otvoriti cijeli skup našeg API-ja otvaranjem datoteke `node_modules/@types/vscode/index.d.ts`.

## Pokrenite testove

* Instalirajte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Pokrenite zadatak "watch" putem naredbe **Tasks: Run Task**. Provjerite je li ovo pokrenuto, inače testovi možda neće biti otkriveni.
* Otvorite pregled testiranja iz trake aktivnosti i kliknite gumb "Run Test" ili koristite prečac `Ctrl/Cmd + ; A`.
* Pogledajte izlaz rezultata testiranja u prikazu Test Results.
* Izvršite promjene u `src/test/extension.test.ts` ili kreirajte nove testne datoteke unutar mape `test`.
  * Pruženi pokretač testova uzet će u obzir samo datoteke koje odgovaraju uzorku naziva `**.test.ts`.
  * Možete kreirati mape unutar mape `test` kako biste strukturirali svoje testove na bilo koji način.

## Idite korak dalje

* Smanjite veličinu ekstenzije i poboljšajte vrijeme pokretanja [pakiranjem svoje ekstenzije](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Objavite svoju ekstenziju](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) na tržištu ekstenzija za VS Code.
* Automatizirajte izgradnje postavljanjem [Kontinuirane integracije](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga strojno baziranog AI prijevoda. Iako težimo točnosti, molimo vas da budete svjesni da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.