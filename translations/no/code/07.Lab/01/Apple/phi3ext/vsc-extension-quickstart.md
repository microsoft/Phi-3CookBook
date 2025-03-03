# Velkommen til din VS Code-utvidelse

## Hva som finnes i mappen

* Denne mappen inneholder alle filene som er nødvendige for utvidelsen din.
* `package.json` - dette er manifestfilen der du deklarerer utvidelsen og kommandoen din.
  * Eksempelpluginen registrerer en kommando og definerer dens tittel og navn. Med denne informasjonen kan VS Code vise kommandoen i kommando-paletten. Det er ennå ikke nødvendig å laste inn pluginen.
* `src/extension.ts` - dette er hovedfilen der du implementerer kommandoen din.
  * Filen eksporterer én funksjon, `activate`, som kalles første gang utvidelsen din aktiveres (i dette tilfellet ved å utføre kommandoen). Inne i `activate`-funksjonen kaller vi `registerCommand`.
  * Vi sender funksjonen som inneholder implementasjonen av kommandoen som den andre parameteren til `registerCommand`.

## Oppsett

* Installer de anbefalte utvidelsene (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner og dbaeumer.vscode-eslint).

## Kom raskt i gang

* Trykk `F5` for å åpne et nytt vindu med utvidelsen din lastet inn.
* Kjør kommandoen din fra kommando-paletten ved å trykke (`Ctrl+Shift+P` eller `Cmd+Shift+P` på Mac) og skrive `Hello World`.
* Sett opp brytepunkter i koden din inne i `src/extension.ts` for å feilsøke utvidelsen din.
* Finn utdataene fra utvidelsen din i feilsøkingskonsollen.

## Gjør endringer

* Du kan starte utvidelsen på nytt fra feilsøkingsverktøylinjen etter å ha endret koden i `src/extension.ts`.
* Du kan også laste inn (`Ctrl+R` eller `Cmd+R` på Mac) VS Code-vinduet med utvidelsen din for å laste inn endringene.

## Utforsk API-et

* Du kan åpne hele settet med vårt API ved å åpne filen `node_modules/@types/vscode/index.d.ts`.

## Kjør tester

* Installer [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Kjør "watch"-oppgaven via kommandoen **Tasks: Run Task**. Sørg for at denne kjører, ellers kan det hende at tester ikke oppdages.
* Åpne Test-visningen fra aktivitetsfeltet og klikk på "Run Test"-knappen, eller bruk hurtigtasten `Ctrl/Cmd + ; A`.
* Se testresultatene i Test Results-visningen.
* Gjør endringer i `src/test/extension.test.ts` eller opprett nye testfiler i `test`-mappen.
  * Den medfølgende testkjøreren vil kun vurdere filer som matcher navnemønsteret `**.test.ts`.
  * Du kan opprette mapper inne i `test`-mappen for å strukturere testene dine slik du ønsker.

## Gå videre

* Reduser størrelsen på utvidelsen og forbedre oppstartstiden ved å [pakke utvidelsen din](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publiser utvidelsen din](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) på VS Code-utvidelsesmarkedet.
* Automatiser bygging ved å sette opp [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.