# Dobrodošli u svoj VS Code dodatak

## Što se nalazi u mapi

* Ova mapa sadrži sve datoteke potrebne za vaš dodatak.
* `package.json` - ovo je manifest datoteka u kojoj deklarirate svoj dodatak i naredbu.
  * Uzorak dodatka registrira naredbu i definira njezin naslov i naziv naredbe. S ovim informacijama VS Code može prikazati naredbu u izborniku naredbi. Još nije potrebno učitavati dodatak.
* `src/extension.ts` - ovo je glavna datoteka gdje ćete pružiti implementaciju svoje naredbe.
  * Datoteka izvozi jednu funkciju, `activate`, koja se poziva prvi put kada se vaš dodatak aktivira (u ovom slučaju izvršavanjem naredbe). Unutar funkcije `activate` pozivamo `registerCommand`.
  * Funkciju koja sadrži implementaciju naredbe prosljeđujemo kao drugi parametar u `registerCommand`.

## Postavljanje

* instalirajte preporučene dodatke (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner i dbaeumer.vscode-eslint)

## Počnite odmah s radom

* Pritisnite `F5` za otvaranje novog prozora s učitanim dodatkom.
* Pokrenite svoju naredbu iz izbornika naredbi pritiskom na (`Ctrl+Shift+P` ili `Cmd+Shift+P` na Macu) i upisivanjem `Hello World`.
* Postavite točke prekida u svom kodu unutar `src/extension.ts` kako biste otklonili pogreške u dodatku.
* Pronađite izlaz svog dodatka u konzoli za otklanjanje pogrešaka.

## Izvršite promjene

* Nakon promjene koda u `src/extension.ts`, možete ponovno pokrenuti dodatak iz alatne trake za otklanjanje pogrešaka.
* Također možete ponovno učitati (`Ctrl+R` ili `Cmd+R` na Macu) prozor VS Code-a s vašim dodatkom kako biste učitali promjene.

## Istražite API

* Možete otvoriti cijeli skup našeg API-ja otvaranjem datoteke `node_modules/@types/vscode/index.d.ts`.

## Pokrenite testove

* Instalirajte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Pokrenite zadatak "watch" putem naredbe **Tasks: Run Task**. Provjerite je li ovo pokrenuto, inače se testovi možda neće otkriti.
* Otvorite prikaz za testiranje iz trake aktivnosti i kliknite gumb "Run Test", ili koristite prečac `Ctrl/Cmd + ; A`.
* Pogledajte rezultate testova u prikazu rezultata testiranja.
* Izvršite promjene u `src/test/extension.test.ts` ili kreirajte nove testne datoteke unutar mape `test`.
  * Pruženi testni pokretač razmatrat će samo datoteke koje odgovaraju uzorku imena `**.test.ts`.
  * Možete kreirati mape unutar mape `test` kako biste strukturirali svoje testove na željeni način.

## Idite dalje

* Smanjite veličinu dodatka i poboljšajte vrijeme pokretanja [pakiranjem svog dodatka](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Objavite svoj dodatak](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na tržištu dodataka za VS Code.
* Automatizirajte izgradnje postavljanjem [kontinuirane integracije](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Odricanje odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga strojno baziranog AI prijevoda. Iako težimo točnosti, molimo vas da budete svjesni da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.