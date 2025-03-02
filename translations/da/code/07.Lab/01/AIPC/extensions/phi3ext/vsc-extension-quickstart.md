# Velkommen til din VS Code-udvidelse

## Hvad er i mappen

* Denne mappe indeholder alle de filer, der er nødvendige for din udvidelse.
* `package.json` - dette er manifestfilen, hvor du erklærer din udvidelse og kommando.
  * Eksempel-plugin'et registrerer en kommando og definerer dens titel og kommandoens navn. Med disse oplysninger kan VS Code vise kommandoen i kommando-paletten. Det behøver endnu ikke at indlæse plugin'et.
* `src/extension.ts` - dette er hovedfilen, hvor du implementerer din kommando.
  * Filen eksporterer en funktion, `activate`, som kaldes første gang, din udvidelse aktiveres (i dette tilfælde ved at udføre kommandoen). Inde i `activate`-funktionen kalder vi `registerCommand`.
  * Vi sender funktionen, der indeholder implementeringen af kommandoen, som anden parameter til `registerCommand`.

## Opsætning

* Installer de anbefalede udvidelser (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner og dbaeumer.vscode-eslint)

## Kom hurtigt i gang

* Tryk på `F5` for at åbne et nyt vindue med din udvidelse indlæst.
* Kør din kommando fra kommando-paletten ved at trykke (`Ctrl+Shift+P` eller `Cmd+Shift+P` på Mac) og skrive `Hello World`.
* Sæt breakpoints i din kode inde i `src/extension.ts` for at fejlfinde din udvidelse.
* Find output fra din udvidelse i debug-konsollen.

## Lav ændringer

* Du kan genstarte udvidelsen fra debug-værktøjslinjen efter at have ændret kode i `src/extension.ts`.
* Du kan også genindlæse (`Ctrl+R` eller `Cmd+R` på Mac) VS Code-vinduet med din udvidelse for at indlæse dine ændringer.

## Udforsk API'et

* Du kan åbne hele vores API-sæt, når du åbner filen `node_modules/@types/vscode/index.d.ts`.

## Kør tests

* Installer [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Kør "watch"-opgaven via kommandoen **Tasks: Run Task**. Sørg for, at denne kører, ellers kan tests muligvis ikke opdages.
* Åbn Test-visningen fra aktivitetsbjælken, og klik på knappen "Run Test", eller brug genvejen `Ctrl/Cmd + ; A`.
* Se testresultaternes output i Test Results-visningen.
* Lav ændringer i `src/test/extension.test.ts` eller opret nye testfiler inde i mappen `test`.
  * Den medfølgende testrunner vil kun overveje filer, der matcher navnemønsteret `**.test.ts`.
  * Du kan oprette mapper inde i mappen `test` for at strukturere dine tests, som du ønsker.

## Gå videre

* Reducer udvidelsens størrelse og forbedr opstartstiden ved at [pakke din udvidelse](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Udgiv din udvidelse](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) på VS Code-udvidelsesmarkedspladsen.
* Automatiser builds ved at opsætte [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.