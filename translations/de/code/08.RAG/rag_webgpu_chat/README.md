Phi-3-mini WebGPU RAG-Chatbot

## Demo zur Präsentation von WebGPU und RAG-Muster
Das RAG-Muster mit dem gehosteten Phi-3-Onnx-Modell nutzt den Retrieval-Augmented-Generation-Ansatz und kombiniert die Leistungsfähigkeit der Phi-3-Modelle mit ONNX-Hosting für effiziente KI-Bereitstellungen. Dieses Muster ist entscheidend für die Feinabstimmung von Modellen für branchenspezifische Aufgaben und bietet eine Kombination aus Qualität, Kosteneffizienz und Verständnis für lange Kontexte. Es ist Teil der Azure AI-Suite, die eine breite Auswahl an Modellen bietet, die leicht zu finden, auszuprobieren und zu verwenden sind und auf die Anpassungsbedürfnisse verschiedener Branchen eingehen. Die Phi-3-Modelle, darunter Phi-3-mini, Phi-3-small und Phi-3-medium, sind im Azure AI Model Catalog verfügbar und können eigenständig oder über Plattformen wie HuggingFace und ONNX feinabgestimmt und bereitgestellt werden. Dies zeigt Microsofts Engagement für zugängliche und effiziente KI-Lösungen.

## Was ist WebGPU?
WebGPU ist eine moderne Web-Grafik-API, die entwickelt wurde, um einen effizienten Zugriff auf die Grafikeinheit (GPU) eines Geräts direkt aus Webbrowsern zu ermöglichen. Sie soll der Nachfolger von WebGL sein und bietet mehrere wesentliche Verbesserungen:

1. **Kompatibilität mit modernen GPUs**: WebGPU ist so konzipiert, dass es nahtlos mit aktuellen GPU-Architekturen funktioniert und System-APIs wie Vulkan, Metal und Direct3D 12 nutzt.
2. **Verbesserte Leistung**: Es unterstützt allgemeine GPU-Berechnungen und schnellere Operationen, wodurch es sowohl für die Grafikdarstellung als auch für Aufgaben des maschinellen Lernens geeignet ist.
3. **Erweiterte Funktionen**: WebGPU bietet Zugriff auf fortschrittlichere GPU-Funktionen und ermöglicht komplexere und dynamischere Grafik- und Rechenaufgaben.
4. **Reduzierte JavaScript-Belastung**: Durch die Verlagerung von mehr Aufgaben auf die GPU verringert WebGPU die Arbeitslast von JavaScript erheblich, was zu einer besseren Leistung und flüssigeren Erlebnissen führt.

WebGPU wird derzeit in Browsern wie Google Chrome unterstützt, und es wird daran gearbeitet, die Unterstützung auf andere Plattformen auszuweiten.

### 03.WebGPU
Erforderliche Umgebung:

**Unterstützte Browser:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly  

### WebGPU aktivieren:

- In Chrome/Microsoft Edge  

Aktivieren Sie das `chrome://flags/#enable-unsafe-webgpu`-Flag.

#### Browser öffnen:
Starten Sie Google Chrome oder Microsoft Edge.

#### Flags-Seite aufrufen:
Geben Sie in die Adressleiste `chrome://flags` ein und drücken Sie die Eingabetaste.

#### Nach dem Flag suchen:
Geben Sie in das Suchfeld oben auf der Seite „enable-unsafe-webgpu“ ein.

#### Flag aktivieren:
Suchen Sie in der Ergebnisliste das Flag #enable-unsafe-webgpu.

Klicken Sie auf das Dropdown-Menü daneben und wählen Sie „Enabled“.

#### Browser neu starten:
Nach der Aktivierung des Flags müssen Sie Ihren Browser neu starten, damit die Änderungen wirksam werden. Klicken Sie auf die Schaltfläche „Relaunch“, die unten auf der Seite angezeigt wird.

- Für Linux starten Sie den Browser mit `--enable-features=Vulkan`.
- Safari 18 (macOS 15) hat WebGPU standardmäßig aktiviert.
- In Firefox Nightly geben Sie in die Adressleiste about:config ein und `set dom.webgpu.enabled to true`.

### GPU für Microsoft Edge einrichten

Hier sind die Schritte, um eine Hochleistungs-GPU für Microsoft Edge unter Windows einzurichten:

- **Einstellungen öffnen:** Klicken Sie auf das Startmenü und wählen Sie „Einstellungen“.
- **Systemeinstellungen:** Gehen Sie zu „System“ und dann zu „Anzeige“.
- **Grafikeinstellungen:** Scrollen Sie nach unten und klicken Sie auf „Grafikeinstellungen“.
- **App auswählen:** Unter „Eine App auswählen, um die Präferenz festzulegen“ wählen Sie „Desktop-App“ und dann „Durchsuchen“.
- **Edge auswählen:** Navigieren Sie zum Installationsordner von Edge (normalerweise `C:\Program Files (x86)\Microsoft\Edge\Application`) und wählen Sie `msedge.exe`.
- **Präferenz festlegen:** Klicken Sie auf „Optionen“, wählen Sie „Hohe Leistung“ und klicken Sie auf „Speichern“.  
So stellen Sie sicher, dass Microsoft Edge Ihre Hochleistungs-GPU für eine bessere Leistung verwendet.  
- **Starten Sie Ihren Computer neu**, damit diese Einstellungen wirksam werden.

### Codespace öffnen:
Navigieren Sie zu Ihrem Repository auf GitHub.  
Klicken Sie auf die Schaltfläche „Code“ und wählen Sie „Open with Codespaces“.  

Wenn Sie noch keinen Codespace haben, können Sie einen erstellen, indem Sie auf „New codespace“ klicken.

**Hinweis** Installation der Node-Umgebung in Ihrem Codespace  
Das Ausführen eines npm-Demos aus einem GitHub-Codespace ist eine großartige Möglichkeit, Ihr Projekt zu testen und zu entwickeln. Hier ist eine Schritt-für-Schritt-Anleitung, die Ihnen den Einstieg erleichtert:

### Ihre Umgebung einrichten:
Sobald Ihr Codespace geöffnet ist, stellen Sie sicher, dass Node.js und npm installiert sind. Sie können dies überprüfen, indem Sie Folgendes ausführen:  
```
node -v
```  
```
npm -v
```  

Falls sie nicht installiert sind, können Sie sie mit den folgenden Befehlen installieren:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```  

### Navigieren Sie zu Ihrem Projektverzeichnis:
Verwenden Sie das Terminal, um zu dem Verzeichnis zu navigieren, in dem sich Ihr npm-Projekt befindet:  
```
cd path/to/your/project
```  

### Abhängigkeiten installieren:
Führen Sie den folgenden Befehl aus, um alle erforderlichen Abhängigkeiten zu installieren, die in Ihrer package.json-Datei aufgeführt sind:  

```
npm install
```  

### Demo ausführen:
Sobald die Abhängigkeiten installiert sind, können Sie Ihr Demo-Skript ausführen. Dieses wird normalerweise im Abschnitt „scripts“ Ihrer package.json angegeben. Wenn Ihr Demo-Skript beispielsweise „start“ heißt, können Sie Folgendes ausführen:  

```
npm run build
```  
```
npm run dev
```  

### Auf die Demo zugreifen:
Wenn Ihre Demo einen Webserver umfasst, stellt Codespaces eine URL bereit, über die Sie darauf zugreifen können. Suchen Sie nach einer Benachrichtigung oder überprüfen Sie die Registerkarte „Ports“, um die URL zu finden.

**Hinweis:** Das Modell muss im Browser zwischengespeichert werden, daher kann das Laden einige Zeit in Anspruch nehmen.

### RAG-Demo
Laden Sie die Markdown-Datei `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/` hoch.

### Datei auswählen:
Klicken Sie auf die Schaltfläche „Datei auswählen“, um das Dokument auszuwählen, das Sie hochladen möchten.

### Dokument hochladen:
Nachdem Sie Ihre Datei ausgewählt haben, klicken Sie auf die Schaltfläche „Hochladen“, um Ihr Dokument für RAG (Retrieval-Augmented Generation) zu laden.

### Chat starten:
Sobald das Dokument hochgeladen ist, können Sie eine Chat-Sitzung mit RAG basierend auf dem Inhalt Ihres Dokuments starten.

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.