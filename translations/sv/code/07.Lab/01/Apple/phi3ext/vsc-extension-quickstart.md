# Välkommen till din VS Code-tillägg

## Vad finns i mappen

* Den här mappen innehåller alla filer som behövs för ditt tillägg.
* `package.json` - detta är manifestfilen där du deklarerar ditt tillägg och kommando.
  * Exempelpluginet registrerar ett kommando och definierar dess titel och kommandonamn. Med denna information kan VS Code visa kommandot i kommandopaletten. Pluginet behöver ännu inte laddas.
* `src/extension.ts` - detta är huvudfilen där du implementerar ditt kommando.
  * Filen exporterar en funktion, `activate`, som körs första gången ditt tillägg aktiveras (i det här fallet genom att köra kommandot). Inuti funktionen `activate` anropar vi `registerCommand`.
  * Vi skickar funktionen som innehåller implementeringen av kommandot som den andra parametern till `registerCommand`.

## Installation

* Installera de rekommenderade tilläggen (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner och dbaeumer.vscode-eslint).

## Kom igång direkt

* Tryck på `F5` för att öppna ett nytt fönster med ditt tillägg laddat.
* Kör ditt kommando från kommandopaletten genom att trycka (`Ctrl+Shift+P` eller `Cmd+Shift+P` på Mac) och skriva `Hello World`.
* Sätt ut brytpunkter i din kod i `src/extension.ts` för att felsöka ditt tillägg.
* Hitta utdata från ditt tillägg i debug-konsolen.

## Gör ändringar

* Du kan starta om tillägget från debug-verktygsfältet efter att ha ändrat koden i `src/extension.ts`.
* Du kan också ladda om (`Ctrl+R` eller `Cmd+R` på Mac) VS Code-fönstret med ditt tillägg för att ladda dina ändringar.

## Utforska API:et

* Du kan öppna hela vårt API genom att öppna filen `node_modules/@types/vscode/index.d.ts`.

## Kör tester

* Installera [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Kör "watch"-uppgiften via kommandot **Tasks: Run Task**. Se till att detta körs, annars kanske tester inte upptäcks.
* Öppna testvyn från aktivitetsfältet och klicka på knappen "Run Test", eller använd kortkommandot `Ctrl/Cmd + ; A`.
* Se testresultatets utdata i testresultatvyn.
* Gör ändringar i `src/test/extension.test.ts` eller skapa nya testfiler i mappen `test`.
  * Den medföljande testköraren kommer endast att ta hänsyn till filer som matchar namnformatet `**.test.ts`.
  * Du kan skapa mappar i mappen `test` för att strukturera dina tester på valfritt sätt.

## Gå vidare

* Minska tilläggets storlek och förbättra starttiden genom att [paketera ditt tillägg](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publicera ditt tillägg](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) på VS Code-tilläggsmarknaden.
* Automatisera byggprocesser genom att ställa in [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-baserade maskinöversättningstjänster. Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller inexaktheter. Det ursprungliga dokumentet på dess ursprungsspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.