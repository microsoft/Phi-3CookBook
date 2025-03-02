# Welkom bij je VS Code-extensie

## Wat zit er in de map

* Deze map bevat alle bestanden die nodig zijn voor je extensie.
* `package.json` - dit is het manifestbestand waarin je je extensie en commando declareert.
  * De voorbeeldplugin registreert een commando en definieert de titel en de naam van het commando. Met deze informatie kan VS Code het commando in de commandopalet weergeven. De plugin hoeft op dit moment nog niet geladen te worden.
* `src/extension.ts` - dit is het hoofdbestand waarin je de implementatie van je commando levert.
  * Het bestand exporteert één functie, `activate`, die wordt aangeroepen de allereerste keer dat je extensie wordt geactiveerd (in dit geval door het commando uit te voeren). Binnen de `activate`-functie roepen we `registerCommand` aan.
  * We geven de functie met de implementatie van het commando door als tweede parameter aan `registerCommand`.

## Instellen

* Installeer de aanbevolen extensies (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner en dbaeumer.vscode-eslint)

## Meteen aan de slag

* Druk op `F5` om een nieuw venster te openen met je extensie geladen.
* Voer je commando uit vanuit de commandopalet door (`Ctrl+Shift+P` of `Cmd+Shift+P` op Mac) in te drukken en `Hello World` te typen.
* Stel breakpoints in je code in `src/extension.ts` om je extensie te debuggen.
* Vind de uitvoer van je extensie in de debugconsole.

## Wijzigingen aanbrengen

* Je kunt de extensie opnieuw starten vanuit de debugwerkbalk nadat je code in `src/extension.ts` hebt gewijzigd.
* Je kunt ook het VS Code-venster herladen (`Ctrl+R` of `Cmd+R` op Mac) om je wijzigingen te laden.

## Verken de API

* Je kunt de volledige set van onze API openen door het bestand `node_modules/@types/vscode/index.d.ts` te openen.

## Tests uitvoeren

* Installeer de [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Voer de "watch"-taak uit via het commando **Tasks: Run Task**. Zorg ervoor dat dit actief is, anders worden tests mogelijk niet gevonden.
* Open de Testweergave vanuit de activiteitenbalk en klik op de knop "Run Test", of gebruik de sneltoets `Ctrl/Cmd + ; A`.
* Bekijk de uitvoer van het testresultaat in de Test Results-weergave.
* Breng wijzigingen aan in `src/test/extension.test.ts` of maak nieuwe testbestanden aan in de map `test`.
  * De meegeleverde test runner zal alleen bestanden overwegen die overeenkomen met het naamspatroon `**.test.ts`.
  * Je kunt mappen maken binnen de map `test` om je tests op elke gewenste manier te structureren.

## Verder gaan

* Verminder de grootte van de extensie en verbeter de opstarttijd door je extensie te [bundelen](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publiceer je extensie](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) op de VS Code-extensiemarktplaats.
* Automatiseer builds door [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) in te stellen.

**Disclaimer**:  
Dit document is vertaald met behulp van machinegebaseerde AI-vertalingsdiensten. Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.