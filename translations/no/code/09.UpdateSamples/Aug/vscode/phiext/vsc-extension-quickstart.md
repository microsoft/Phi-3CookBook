# Velkommen til din VS Code-utvidelse

## Hva er i mappen

* Denne mappen inneholder alle filene som er nødvendige for utvidelsen din.
* `package.json` - dette er manifestfilen der du erklærer utvidelsen og kommandoen din.
  * Eksempelpluginet registrerer en kommando og definerer dens tittel og kommandoens navn. Med denne informasjonen kan VS Code vise kommandoen i kommando-paletten. Den trenger foreløpig ikke å laste inn pluginet.
* `src/extension.ts` - dette er hovedfilen der du gir implementasjonen av kommandoen din.
  * Filen eksporterer en funksjon, `activate`, som kalles første gang utvidelsen din aktiveres (i dette tilfellet ved å kjøre kommandoen). Inne i `activate`-funksjonen kaller vi `registerCommand`.
  * Vi sender funksjonen som inneholder implementasjonen av kommandoen som den andre parameteren til `registerCommand`.

## Oppsett

* Installer de anbefalte utvidelsene (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner og dbaeumer.vscode-eslint).

## Kom raskt i gang

* Trykk `F5` for å åpne et nytt vindu med utvidelsen din lastet.
* Kjør kommandoen din fra kommando-paletten ved å trykke (`Ctrl+Shift+P` eller `Cmd+Shift+P` på Mac) og skrive `Hello World`.
* Sett brytepunkter i koden din inne i `src/extension.ts` for å feilsøke utvidelsen din.
* Finn utdataene fra utvidelsen din i feilsøkingskonsollen.

## Gjør endringer

* Du kan starte utvidelsen på nytt fra feilsøkingsverktøylinjen etter å ha endret koden i `src/extension.ts`.
* Du kan også laste inn (`Ctrl+R` eller `Cmd+R` på Mac) VS Code-vinduet med utvidelsen din for å laste inn endringene.

## Utforsk API-et

* Du kan åpne hele settet med API-er når du åpner filen `node_modules/@types/vscode/index.d.ts`.

## Kjør tester

* Installer [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Kjør "watch"-oppgaven via kommandoen **Tasks: Run Task**. Sørg for at denne kjører, ellers kan det hende testene ikke blir oppdaget.
* Åpne Test-visningen fra aktivitetsfeltet og klikk på knappen "Run Test", eller bruk hurtigtasten `Ctrl/Cmd + ; A`.
* Se testresultatene i Test Results-visningen.
* Gjør endringer i `src/test/extension.test.ts` eller opprett nye testfiler i `test`-mappen.
  * Testløperen som følger med vil bare vurdere filer som samsvarer med navnemønsteret `**.test.ts`.
  * Du kan opprette mapper inne i `test`-mappen for å strukturere testene dine slik du ønsker.

## Gå videre

* Reduser størrelsen på utvidelsen og forbedre oppstartstiden ved å [pakke utvidelsen](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publiser utvidelsen din](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) på VS Code-utvidelsesmarkedet.
* Automatiser bygging ved å sette opp [Kontinuerlig integrasjon](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell, menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.