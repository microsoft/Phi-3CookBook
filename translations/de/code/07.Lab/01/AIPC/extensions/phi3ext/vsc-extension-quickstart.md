# Willkommen zu deiner VS Code-Erweiterung

## Was ist in diesem Ordner

* Dieser Ordner enthält alle Dateien, die für deine Erweiterung notwendig sind.
* `package.json` - dies ist die Manifest-Datei, in der du deine Erweiterung und den Befehl deklarierst.
  * Das Beispiel-Plugin registriert einen Befehl und definiert dessen Titel und Befehlsnamen. Mit diesen Informationen kann VS Code den Befehl in der Befehlsübersicht anzeigen. Das Plugin muss dafür noch nicht geladen werden.
* `src/extension.ts` - dies ist die Hauptdatei, in der du die Implementierung deines Befehls bereitstellst.
  * Die Datei exportiert eine Funktion, `activate`, die zum ersten Mal aufgerufen wird, wenn deine Erweiterung aktiviert wird (in diesem Fall durch Ausführen des Befehls). Innerhalb der `activate`-Funktion rufen wir `registerCommand` auf.
  * Wir übergeben die Funktion, die die Implementierung des Befehls enthält, als zweiten Parameter an `registerCommand`.

## Einrichtung

* Installiere die empfohlenen Erweiterungen (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner und dbaeumer.vscode-eslint).

## Sofort loslegen

* Drücke `F5`, um ein neues Fenster mit deiner geladenen Erweiterung zu öffnen.
* Führe deinen Befehl aus der Befehlsübersicht aus, indem du (`Ctrl+Shift+P` oder `Cmd+Shift+P` auf einem Mac) drückst und `Hello World` eingibst.
* Setze Haltepunkte in deinem Code innerhalb von `src/extension.ts`, um deine Erweiterung zu debuggen.
* Finde die Ausgabe deiner Erweiterung in der Debug-Konsole.

## Änderungen vornehmen

* Du kannst die Erweiterung aus der Debug-Symbolleiste neu starten, nachdem du den Code in `src/extension.ts` geändert hast.
* Du kannst auch das VS Code-Fenster mit deiner Erweiterung neu laden (`Ctrl+R` oder `Cmd+R` auf einem Mac), um deine Änderungen zu übernehmen.

## Die API erkunden

* Du kannst das vollständige Set unserer API öffnen, indem du die Datei `node_modules/@types/vscode/index.d.ts` öffnest.

## Tests ausführen

* Installiere den [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Führe die "watch"-Aufgabe über den Befehl **Tasks: Run Task** aus. Stelle sicher, dass dies läuft, sonst werden Tests möglicherweise nicht erkannt.
* Öffne die Test-Ansicht in der Aktivitätsleiste und klicke auf die Schaltfläche "Run Test" oder benutze den Hotkey `Ctrl/Cmd + ; A`.
* Sieh dir die Ergebnisse der Tests in der Test-Resultate-Ansicht an.
* Nimm Änderungen an `src/test/extension.test.ts` vor oder erstelle neue Testdateien im Ordner `test`.
  * Der bereitgestellte Test-Runner berücksichtigt nur Dateien, die dem Namensmuster `**.test.ts` entsprechen.
  * Du kannst Ordner im Ordner `test` erstellen, um deine Tests beliebig zu strukturieren.

## Weiterführende Schritte

* Reduziere die Größe der Erweiterung und verbessere die Startzeit, indem du [deine Erweiterung bündelst](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Veröffentliche deine Erweiterung](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) im VS Code-Erweiterungsmarktplatz.
* Automatisiere Builds, indem du [Continuous Integration einrichtest](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.