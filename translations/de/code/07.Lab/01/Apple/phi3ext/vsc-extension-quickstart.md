# Willkommen zu Ihrer VS Code-Erweiterung

## Was ist in diesem Ordner?

* Dieser Ordner enthält alle Dateien, die für Ihre Erweiterung erforderlich sind.
* `package.json` - dies ist die Manifestdatei, in der Sie Ihre Erweiterung und den Befehl deklarieren.
  * Das Beispiel-Plugin registriert einen Befehl und definiert dessen Titel und Befehlsnamen. Mit diesen Informationen kann VS Code den Befehl in der Befehlsübersicht anzeigen. Das Plugin muss dabei noch nicht geladen werden.
* `src/extension.ts` - dies ist die Hauptdatei, in der Sie die Implementierung Ihres Befehls bereitstellen.
  * Die Datei exportiert eine Funktion, `activate`, die beim ersten Aktivieren Ihrer Erweiterung aufgerufen wird (in diesem Fall durch Ausführen des Befehls). Innerhalb der `activate`-Funktion rufen wir `registerCommand` auf.
  * Wir übergeben die Funktion, die die Implementierung des Befehls enthält, als zweiten Parameter an `registerCommand`.

## Einrichtung

* Installieren Sie die empfohlenen Erweiterungen (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner und dbaeumer.vscode-eslint).

## Schnell loslegen

* Drücken Sie `F5`, um ein neues Fenster mit Ihrer geladenen Erweiterung zu öffnen.
* Führen Sie Ihren Befehl aus der Befehlsübersicht aus, indem Sie (`Ctrl+Shift+P` oder `Cmd+Shift+P` auf Mac) drücken und `Hello World` eingeben.
* Setzen Sie Breakpoints in Ihrem Code innerhalb von `src/extension.ts`, um Ihre Erweiterung zu debuggen.
* Finden Sie Ausgaben Ihrer Erweiterung in der Debug-Konsole.

## Änderungen vornehmen

* Sie können die Erweiterung aus der Debug-Symbolleiste neu starten, nachdem Sie den Code in `src/extension.ts` geändert haben.
* Sie können auch das VS Code-Fenster mit Ihrer Erweiterung neu laden (`Ctrl+R` oder `Cmd+R` auf Mac), um Ihre Änderungen zu übernehmen.

## API erkunden

* Sie können das vollständige API-Set öffnen, indem Sie die Datei `node_modules/@types/vscode/index.d.ts` öffnen.

## Tests ausführen

* Installieren Sie den [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner).
* Führen Sie die "watch"-Aufgabe über den Befehl **Tasks: Run Task** aus. Stellen Sie sicher, dass diese läuft, sonst werden Tests möglicherweise nicht erkannt.
* Öffnen Sie die Testansicht in der Aktivitätsleiste und klicken Sie auf die Schaltfläche "Run Test" oder verwenden Sie die Tastenkombination `Ctrl/Cmd + ; A`.
* Sehen Sie sich die Testergebnisse in der Test Results-Ansicht an.
* Nehmen Sie Änderungen an `src/test/extension.test.ts` vor oder erstellen Sie neue Testdateien im Ordner `test`.
  * Der bereitgestellte Test-Runner berücksichtigt nur Dateien, die dem Namensmuster `**.test.ts` entsprechen.
  * Sie können Ordner innerhalb des `test`-Ordners erstellen, um Ihre Tests beliebig zu strukturieren.

## Weiterführende Schritte

* Reduzieren Sie die Größe der Erweiterung und verbessern Sie die Startzeit, indem Sie [Ihre Erweiterung bündeln](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Veröffentlichen Sie Ihre Erweiterung](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) im VS Code-Erweiterungsmarkt.
* Automatisieren Sie Builds, indem Sie [Continuous Integration einrichten](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.