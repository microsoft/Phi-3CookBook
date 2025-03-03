# Mitwirken

Dieses Projekt begrüßt Beiträge und Vorschläge. Die meisten Beiträge erfordern, dass Sie einer Contributor License Agreement (CLA) zustimmen, die bestätigt, dass Sie das Recht haben, uns die Rechte zur Nutzung Ihres Beitrags zu gewähren, und dies auch tatsächlich tun. Weitere Details finden Sie unter [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com).

Wenn Sie eine Pull-Anfrage einreichen, wird ein CLA-Bot automatisch feststellen, ob Sie eine CLA einreichen müssen, und die PR entsprechend markieren (z. B. Statusprüfung, Kommentar). Folgen Sie einfach den Anweisungen des Bots. Dies müssen Sie nur einmal für alle Repositories tun, die unsere CLA verwenden.

## Verhaltenskodex

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) übernommen. Weitere Informationen finden Sie in den [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) oder kontaktieren Sie [opencode@microsoft.com](mailto:opencode@microsoft.com) bei zusätzlichen Fragen oder Kommentaren.

## Hinweise zum Erstellen von Issues

Bitte erstellen Sie keine GitHub-Issues für allgemeine Supportfragen, da die GitHub-Liste für Funktionsanfragen und Fehlerberichte genutzt werden sollte. So können wir tatsächliche Probleme oder Fehler im Code leichter nachverfolgen und die allgemeine Diskussion vom eigentlichen Code trennen.

## Wie man beiträgt

### Richtlinien für Pull-Anfragen

Wenn Sie eine Pull-Anfrage (PR) an das Phi-3 CookBook-Repository einreichen, verwenden Sie bitte die folgenden Richtlinien:

- **Repository forken**: Forken Sie das Repository immer in Ihr eigenes Konto, bevor Sie Änderungen vornehmen.

- **Separate Pull-Anfragen (PR)**:
  - Reichen Sie jede Art von Änderung in einer eigenen Pull-Anfrage ein. Zum Beispiel sollten Fehlerbehebungen und Dokumentationsupdates in separaten PRs eingereicht werden.
  - Tippfehlerkorrekturen und kleinere Dokumentationsupdates können, falls passend, in einer einzigen PR kombiniert werden.

- **Merge-Konflikte beheben**: Wenn Ihre Pull-Anfrage Merge-Konflikte aufweist, aktualisieren Sie Ihren lokalen `main`-Branch, um ihn mit dem Hauptrepository abzugleichen, bevor Sie Änderungen vornehmen.

- **Übersetzungsbeiträge**: Wenn Sie eine Übersetzungs-PR einreichen, stellen Sie sicher, dass der Übersetzungsordner Übersetzungen für alle Dateien im Originalordner enthält.

### Richtlinien für Übersetzungen

> [!IMPORTANT]
>
> Verwenden Sie beim Übersetzen von Texten in diesem Repository keine maschinelle Übersetzung. Arbeiten Sie nur an Übersetzungen in Sprachen, in denen Sie sicher sind.

Wenn Sie eine nicht-englische Sprache beherrschen, können Sie helfen, den Inhalt zu übersetzen. Befolgen Sie diese Schritte, um sicherzustellen, dass Ihre Übersetzungsbeiträge korrekt integriert werden. Verwenden Sie die folgenden Richtlinien:

- **Übersetzungsordner erstellen**: Navigieren Sie zum entsprechenden Abschnittsordner und erstellen Sie einen Übersetzungsordner für die Sprache, zu der Sie beitragen. Zum Beispiel:
  - Für den Einführungsabschnitt: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Für den Schnellstartabschnitt: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Setzen Sie dieses Muster für andere Abschnitte (03.Inference, 04.Finetuning usw.) fort.

- **Relative Pfade aktualisieren**: Passen Sie beim Übersetzen die Ordnerstruktur an, indem Sie `../../` am Anfang der relativen Pfade innerhalb der Markdown-Dateien hinzufügen, um sicherzustellen, dass Links korrekt funktionieren. Zum Beispiel:
  - Ändern Sie `(../../imgs/01/phi3aisafety.png)` zu `(../../../../imgs/01/phi3aisafety.png)`.

- **Organisieren Sie Ihre Übersetzungen**: Jede übersetzte Datei sollte im entsprechenden Übersetzungsordner des Abschnitts abgelegt werden. Wenn Sie beispielsweise den Einführungsabschnitt ins Spanische übersetzen, würden Sie folgendes erstellen:
  - `PhiCookBook/md/01.Introduce/translations/es/`.

- **Vollständige PR einreichen**: Stellen Sie sicher, dass alle übersetzten Dateien eines Abschnitts in einer PR enthalten sind. Wir akzeptieren keine Teilübersetzungen für einen Abschnitt. Wenn Sie eine Übersetzungs-PR einreichen, stellen Sie sicher, dass der Übersetzungsordner Übersetzungen für alle Dateien im Originalordner enthält.

### Richtlinien für das Schreiben

Um Konsistenz über alle Dokumente hinweg zu gewährleisten, verwenden Sie bitte die folgenden Richtlinien:

- **URL-Formatierung**: Setzen Sie alle URLs in eckige Klammern, gefolgt von Klammern, ohne zusätzliche Leerzeichen davor oder dazwischen. Zum Beispiel: `[example](https://www.microsoft.com)`.

- **Relative Links**: Verwenden Sie `./` für relative Links, die auf Dateien oder Ordner im aktuellen Verzeichnis zeigen, und `../` für solche in einem übergeordneten Verzeichnis. Zum Beispiel: `[example](../../path/to/file)` oder `[example](../../../path/to/file)`.

- **Keine länderspezifischen Lokalisierungen**: Stellen Sie sicher, dass Ihre Links keine länderspezifischen Lokalisierungen enthalten. Zum Beispiel vermeiden Sie `/en-us/` oder `/en/`.

- **Bildspeicherung**: Speichern Sie alle Bilder im `./imgs`-Ordner.

- **Beschreibende Bildnamen**: Benennen Sie Bilder beschreibend mit englischen Zeichen, Zahlen und Bindestrichen. Zum Beispiel: `example-image.jpg`.

## GitHub-Workflows

Wenn Sie eine Pull-Anfrage einreichen, werden die folgenden Workflows ausgelöst, um die Änderungen zu validieren. Befolgen Sie die Anweisungen unten, um sicherzustellen, dass Ihre Pull-Anfrage die Workflow-Prüfungen besteht:

- [Überprüfung auf fehlerhafte relative Pfade](../..)
- [Überprüfung, dass URLs keine Lokalisierungen enthalten](../..)

### Überprüfung auf fehlerhafte relative Pfade

Dieser Workflow stellt sicher, dass alle relativen Pfade in Ihren Dateien korrekt sind.

1. Um sicherzustellen, dass Ihre Links ordnungsgemäß funktionieren, führen Sie die folgenden Aufgaben mit VS Code aus:
    - Fahren Sie mit der Maus über einen beliebigen Link in Ihren Dateien.
    - Drücken Sie **Strg + Klick**, um zum Link zu navigieren.
    - Wenn Sie auf einen Link klicken und er lokal nicht funktioniert, wird der Workflow ausgelöst und auch auf GitHub nicht funktionieren.

1. Um dieses Problem zu beheben, führen Sie die folgenden Aufgaben mit den von VS Code vorgeschlagenen Pfaden aus:
    - Geben Sie `./` oder `../` ein.
    - VS Code wird Sie auffordern, aus den verfügbaren Optionen basierend auf Ihrer Eingabe auszuwählen.
    - Folgen Sie dem Pfad, indem Sie auf die gewünschte Datei oder den gewünschten Ordner klicken, um sicherzustellen, dass Ihr Pfad korrekt ist.

Sobald Sie den richtigen relativen Pfad hinzugefügt haben, speichern und pushen Sie Ihre Änderungen.

### Überprüfung, dass URLs keine Lokalisierungen enthalten

Dieser Workflow stellt sicher, dass keine Web-URLs eine länderspezifische Lokalisierung enthalten. Da dieses Repository weltweit zugänglich ist, ist es wichtig, dass URLs keine Lokalisierungen Ihres Landes enthalten.

1. Um zu überprüfen, dass Ihre URLs keine Lokalisierungen enthalten, führen Sie die folgenden Aufgaben aus:

    - Suchen Sie nach Text wie `/en-us/`, `/en/` oder anderen Sprachlokalisierungen in den URLs.
    - Wenn diese in Ihren URLs nicht vorhanden sind, bestehen Sie diese Prüfung.

1. Um dieses Problem zu beheben, führen Sie die folgenden Aufgaben aus:
    - Öffnen Sie den Dateipfad, der vom Workflow hervorgehoben wurde.
    - Entfernen Sie die Sprachlokalisierung aus den URLs.

Sobald Sie die Sprachlokalisierung entfernt haben, speichern und pushen Sie Ihre Änderungen.

### Überprüfung auf fehlerhafte URLs

Dieser Workflow stellt sicher, dass jede Web-URL in Ihren Dateien funktioniert und einen Statuscode 200 zurückgibt.

1. Um sicherzustellen, dass Ihre URLs korrekt funktionieren, führen Sie die folgenden Aufgaben aus:
    - Überprüfen Sie den Status der URLs in Ihren Dateien.

2. Um fehlerhafte URLs zu beheben, führen Sie die folgenden Aufgaben aus:
    - Öffnen Sie die Datei, die die fehlerhafte URL enthält.
    - Aktualisieren Sie die URL auf die korrekte.

Sobald Sie die URLs korrigiert haben, speichern und pushen Sie Ihre Änderungen.

> [!NOTE]
>
> Es kann Fälle geben, in denen die URL-Überprüfung fehlschlägt, obwohl der Link zugänglich ist. Dies kann aus mehreren Gründen passieren, einschließlich:
>
> - **Netzwerkeinschränkungen:** GitHub-Aktionsserver können Netzwerkeinschränkungen haben, die den Zugriff auf bestimmte URLs verhindern.
> - **Timeout-Probleme:** URLs, die zu lange für eine Antwort benötigen, können im Workflow einen Timeout-Fehler auslösen.
> - **Vorübergehende Serverprobleme:** Gelegentliche Serverausfälle oder Wartungsarbeiten können eine URL während der Validierung vorübergehend unzugänglich machen.

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.