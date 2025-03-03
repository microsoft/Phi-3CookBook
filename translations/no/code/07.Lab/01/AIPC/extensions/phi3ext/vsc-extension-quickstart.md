# Velkommen til din VS Code-utvidelse

## Hva inneholder mappen

* Denne mappen inneholder alle filene som er nødvendige for utvidelsen din.
* `package.json` - dette er manifestfilen der du erklærer utvidelsen og kommandoen din.
  * Eksempelpluginet registrerer en kommando og definerer dens tittel og kommandoens navn. Med denne informasjonen kan VS Code vise kommandoen i kommando-paletten. Det er ikke nødvendig å laste inn pluginet ennå.
* `src/extension.ts` - dette er hovedfilen hvor du implementerer kommandoen din.
  * Filen eksporterer én funksjon, `activate`, som kalles første gang utvidelsen din aktiveres (i dette tilfellet ved å kjøre kommandoen). Inne i `activate`-funksjonen kaller vi `registerCommand`.
  * Vi sender funksjonen som inneholder implementasjonen av kommandoen som andre parameter til `registerCommand`.

## Oppsett

* Installer de anbefalte utvidelsene (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner og dbaeumer.vscode-eslint)

## Kom raskt i gang

* Trykk på `F5` for å åpne et nytt vindu med utvidelsen din lastet.
* Kjør kommandoen din fra kommando-paletten ved å trykke (`Ctrl+Shift+P` eller `Cmd+Shift+P` på Mac) og skrive `Hello World`.
* Sett brytepunkter i koden din inne i `src/extension.ts` for å feilsøke utvidelsen din.
* Finn utvidelsens utdata i debug-konsollen.

## Gjør endringer

* Du kan starte utvidelsen på nytt fra feilsøkingsverktøylinjen etter å ha gjort endringer i `src/extension.ts`.
* Du kan også laste inn på nytt (`Ctrl+R` eller `Cmd+R` på Mac) VS Code-vinduet med utvidelsen din for å laste inn endringene.

## Utforsk API-et

* Du kan åpne hele settet med API-er når du åpner filen `node_modules/@types/vscode/index.d.ts`.

## Kjør tester

* Installer [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Kjør "watch"-oppgaven via **Tasks: Run Task**-kommandoen. Sørg for at denne kjører, ellers kan det hende at tester ikke oppdages.
* Åpne testvisningen fra aktivitetsfeltet og klikk på "Run Test"-knappen, eller bruk hurtigtasten `Ctrl/Cmd + ; A`.
* Se testresultatene i Test Results-visningen.
* Gjør endringer i `src/test/extension.test.ts` eller opprett nye testfiler inne i mappen `test`.
  * Den medfølgende testrunneren vil kun vurdere filer som samsvarer med navnemønsteret `**.test.ts`.
  * Du kan opprette mapper inne i mappen `test` for å strukturere testene dine slik du vil.

## Gå videre

* Reduser størrelsen på utvidelsen og forbedre oppstartstiden ved å [pakke utvidelsen din](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publiser utvidelsen din](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) på VS Code-utvidelsesmarkedet.
* Automatiser bygg ved å sette opp [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.