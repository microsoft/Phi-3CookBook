# Dobrodošli u svoju VS Code ekstenziju

## Što se nalazi u mapi

* Ova mapa sadrži sve potrebne datoteke za vašu ekstenziju.
* `package.json` - ovo je manifest datoteka u kojoj deklarirate svoju ekstenziju i naredbu.
  * Uzorak dodatka registrira naredbu i definira njezin naslov i ime naredbe. S ovim informacijama VS Code može prikazati naredbu u izborniku naredbi. Plugin se još uvijek ne mora učitati.
* `src/extension.ts` - ovo je glavna datoteka u kojoj ćete implementirati svoju naredbu.
  * Datoteka izvozi jednu funkciju, `activate`, koja se poziva prvi put kada se vaša ekstenzija aktivira (u ovom slučaju izvršavanjem naredbe). Unutar funkcije `activate` pozivamo `registerCommand`.
  * Funkciju koja sadrži implementaciju naredbe prosljeđujemo kao drugi parametar funkciji `registerCommand`.

## Postavljanje

* instalirajte preporučene ekstenzije (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner i dbaeumer.vscode-eslint)

## Počnite odmah

* Pritisnite `F5` za otvaranje novog prozora s učitanom ekstenzijom.
* Pokrenite svoju naredbu iz izbornika naredbi pritiskom na (`Ctrl+Shift+P` ili `Cmd+Shift+P` na Macu) i upisivanjem `Hello World`.
* Postavite točke prekida u svom kodu unutar `src/extension.ts` kako biste otklonili pogreške u svojoj ekstenziji.
* Pronađite izlaz svoje ekstenzije u konzoli za otklanjanje pogrešaka.

## Izvršite promjene

* Možete ponovno pokrenuti ekstenziju iz trake za otklanjanje pogrešaka nakon što promijenite kod u `src/extension.ts`.
* Također možete ponovno učitati (`Ctrl+R` ili `Cmd+R` na Macu) prozor VS Codea s vašom ekstenzijom kako biste učitali promjene.

## Istražite API

* Možete otvoriti cijeli skup našeg API-ja kada otvorite datoteku `node_modules/@types/vscode/index.d.ts`.

## Pokrenite testove

* Instalirajte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Pokrenite zadatak "watch" putem naredbe **Tasks: Run Task**. Provjerite je li ovo pokrenuto, inače testovi možda neće biti otkriveni.
* Otvorite prikaz Testing iz trake aktivnosti i kliknite gumb "Run Test" ili koristite prečac `Ctrl/Cmd + ; A`.
* Pogledajte rezultate testova u prikazu Test Results.
* Izvršite promjene u `src/test/extension.test.ts` ili kreirajte nove testne datoteke unutar mape `test`.
  * Pruženi testni pokretač uzima u obzir samo datoteke koje odgovaraju uzorku imena `**.test.ts`.
  * Možete kreirati mape unutar mape `test` kako biste strukturirali svoje testove na željeni način.

## Istražite dodatno

* Smanjite veličinu ekstenzije i poboljšajte vrijeme pokretanja [pakiranjem svoje ekstenzije](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Objavite svoju ekstenziju](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na tržištu ekstenzija za VS Code.
* Automatizirajte izgradnju postavljanjem [Kontinuirane integracije](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga strojnog prevođenja temeljenog na umjetnoj inteligenciji. Iako nastojimo osigurati točnost, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije nastale korištenjem ovog prijevoda.