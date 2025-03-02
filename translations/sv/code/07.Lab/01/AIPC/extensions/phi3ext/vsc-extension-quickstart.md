# Välkommen till din VS Code-extension

## Vad finns i mappen

* Den här mappen innehåller alla filer som behövs för din extension.
* `package.json` - detta är manifestfilen där du deklarerar din extension och kommando.
  * Exemplet registrerar ett kommando och definierar dess titel och kommandonamn. Med denna information kan VS Code visa kommandot i kommandopaletten. Den behöver ännu inte ladda pluginen.
* `src/extension.ts` - detta är huvudfilen där du implementerar ditt kommando.
  * Filen exporterar en funktion, `activate`, som körs första gången din extension aktiveras (i detta fall genom att köra kommandot). Inuti funktionen `activate` anropar vi `registerCommand`.
  * Vi skickar funktionen som innehåller implementationen av kommandot som den andra parametern till `registerCommand`.

## Installation

* Installera de rekommenderade extensionerna (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner och dbaeumer.vscode-eslint).

## Kom igång direkt

* Tryck på `F5` för att öppna ett nytt fönster med din extension laddad.
* Kör ditt kommando från kommandopaletten genom att trycka på (`Ctrl+Shift+P` eller `Cmd+Shift+P` på Mac) och skriva `Hello World`.
* Sätt brytpunkter i din kod inuti `src/extension.ts` för att felsöka din extension.
* Hitta output från din extension i debugkonsolen.

## Gör ändringar

* Du kan starta om extensionen från debugverktygsfältet efter att du gjort ändringar i `src/extension.ts`.
* Du kan också ladda om (`Ctrl+R` eller `Cmd+R` på Mac) VS Code-fönstret med din extension för att ladda dina ändringar.

## Utforska API:et

* Du kan öppna hela vår API-dokumentation genom att öppna filen `node_modules/@types/vscode/index.d.ts`.

## Kör tester

* Installera [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Kör "watch"-tasken via kommandot **Tasks: Run Task**. Se till att detta körs, annars kanske testerna inte upptäcks.
* Öppna testvyn från aktivitetsfältet och klicka på knappen "Run Test", eller använd snabbkommandot `Ctrl/Cmd + ; A`.
* Se testresultatens output i Test Results-vyn.
* Gör ändringar i `src/test/extension.test.ts` eller skapa nya testfiler inuti mappen `test`.
  * Den medföljande testverktyget kommer endast att ta hänsyn till filer som matchar namnmönstret `**.test.ts`.
  * Du kan skapa mappar inuti `test` för att strukturera dina tester som du vill.

## Gå vidare

* Minska storleken på din extension och förbättra uppstartstiden genom att [paketera din extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publicera din extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) på VS Code-marknadsplatsen för extensioner.
* Automatisera byggprocessen genom att sätta upp [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-baserade maskinöversättningstjänster. Även om vi strävar efter noggrannhet, vänligen notera att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell human översättning. Vi tar inget ansvar för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.