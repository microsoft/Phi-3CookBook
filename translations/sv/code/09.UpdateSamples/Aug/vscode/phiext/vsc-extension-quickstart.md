# Välkommen till din VS Code-extension

## Vad finns i mappen

* Den här mappen innehåller alla filer som behövs för din extension.
* `package.json` - detta är manifestfilen där du deklarerar din extension och kommando.
  * Exempelpluginet registrerar ett kommando och definierar dess titel och kommandonamn. Med denna information kan VS Code visa kommandot i kommandopaletten. Det behöver ännu inte ladda pluginet.
* `src/extension.ts` - detta är huvudfilen där du implementerar ditt kommando.
  * Filen exporterar en funktion, `activate`, som anropas första gången din extension aktiveras (i detta fall genom att köra kommandot). Inuti `activate`-funktionen anropar vi `registerCommand`.
  * Vi skickar funktionen som innehåller implementationen av kommandot som andra parameter till `registerCommand`.

## Installation

* Installera de rekommenderade tilläggen (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner och dbaeumer.vscode-eslint).

## Kom igång direkt

* Tryck på `F5` för att öppna ett nytt fönster med din extension laddad.
* Kör ditt kommando från kommandopaletten genom att trycka på (`Ctrl+Shift+P` eller `Cmd+Shift+P` på Mac) och skriva `Hello World`.
* Sätt brytpunkter i din kod inuti `src/extension.ts` för att felsöka din extension.
* Hitta utdata från din extension i debugkonsolen.

## Gör ändringar

* Du kan starta om extensionen från debugverktygsfältet efter att du ändrat kod i `src/extension.ts`.
* Du kan också ladda om (`Ctrl+R` eller `Cmd+R` på Mac) VS Code-fönstret med din extension för att ladda dina ändringar.

## Utforska API:et

* Du kan öppna hela vårt API när du öppnar filen `node_modules/@types/vscode/index.d.ts`.

## Kör tester

* Installera [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Kör "watch"-uppgiften via kommandot **Tasks: Run Task**. Se till att detta körs, annars kanske testerna inte upptäcks.
* Öppna Test-vyn från aktivitetsfältet och klicka på knappen "Run Test", eller använd kortkommandot `Ctrl/Cmd + ; A`.
* Se testresultatets utdata i Test Results-vyn.
* Gör ändringar i `src/test/extension.test.ts` eller skapa nya testfiler i `test`-mappen.
  * Den medföljande testköraren kommer endast att ta hänsyn till filer som matchar namnformatet `**.test.ts`.
  * Du kan skapa mappar i `test`-mappen för att strukturera dina tester som du vill.

## Gå längre

* Minska storleken på din extension och förbättra starttiden genom att [paketera din extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publicera din extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) på VS Code-tilläggsmarknaden.
* Automatisera byggprocesser genom att sätta upp [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Ansvarsfriskrivning**:  
Detta dokument har översatts med maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi tar inget ansvar för missförstånd eller feltolkningar som uppstår vid användning av denna översättning.