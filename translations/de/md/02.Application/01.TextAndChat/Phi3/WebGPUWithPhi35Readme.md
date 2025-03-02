# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo zur Präsentation von WebGPU und RAG Pattern

Das RAG Pattern mit dem Phi-3.5 Onnx Hosted Modell nutzt den Retrieval-Augmented Generation-Ansatz und kombiniert die Leistungsfähigkeit der Phi-3.5-Modelle mit ONNX-Hosting für effiziente KI-Bereitstellungen. Dieses Muster ist entscheidend für die Feinabstimmung von Modellen für domänenspezifische Aufgaben und bietet eine Mischung aus Qualität, Kosteneffizienz und Verständnis für lange Kontexte. Es ist Teil der Azure AI-Suite und bietet eine große Auswahl an Modellen, die leicht zu finden, auszuprobieren und zu nutzen sind, um den Anpassungsbedarf verschiedener Branchen zu decken.

## Was ist WebGPU
WebGPU ist eine moderne Web-Grafik-API, die entwickelt wurde, um effizienten Zugriff auf die Grafikverarbeitungseinheit (GPU) eines Geräts direkt aus Webbrowsern zu ermöglichen. Sie soll der Nachfolger von WebGL sein und bietet mehrere wichtige Verbesserungen:

1. **Kompatibilität mit modernen GPUs**: WebGPU wurde entwickelt, um nahtlos mit aktuellen GPU-Architekturen zu arbeiten und nutzt dabei System-APIs wie Vulkan, Metal und Direct3D 12.
2. **Verbesserte Leistung**: Es unterstützt allgemeine GPU-Berechnungen und schnellere Operationen, wodurch es sowohl für die Grafikdarstellung als auch für maschinelles Lernen geeignet ist.
3. **Erweiterte Funktionen**: WebGPU bietet Zugang zu fortschrittlicheren GPU-Funktionen und ermöglicht komplexere und dynamischere Grafik- und Rechenlasten.
4. **Reduzierte JavaScript-Belastung**: Durch die Verlagerung von Aufgaben auf die GPU reduziert WebGPU die Belastung von JavaScript erheblich, was zu einer besseren Leistung und flüssigeren Erlebnissen führt.

WebGPU wird derzeit in Browsern wie Google Chrome unterstützt, wobei daran gearbeitet wird, die Unterstützung auf weitere Plattformen auszudehnen.

### 03.WebGPU
Erforderliche Umgebung:

**Unterstützte Browser:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU aktivieren:

- In Chrome/Microsoft Edge 

Aktivieren Sie das `chrome://flags/#enable-unsafe-webgpu`-Flag.

#### Öffnen Sie Ihren Browser:
Starten Sie Google Chrome oder Microsoft Edge.

#### Rufen Sie die Flags-Seite auf:
Geben Sie in die Adressleiste `chrome://flags` ein und drücken Sie Enter.

#### Suchen Sie nach dem Flag:
Geben Sie im Suchfeld oben auf der Seite 'enable-unsafe-webgpu' ein.

#### Aktivieren Sie das Flag:
Suchen Sie das #enable-unsafe-webgpu-Flag in der Ergebnisliste.

Klicken Sie auf das Dropdown-Menü daneben und wählen Sie Enabled.

#### Starten Sie Ihren Browser neu:

Nachdem Sie das Flag aktiviert haben, müssen Sie Ihren Browser neu starten, damit die Änderungen wirksam werden. Klicken Sie auf die Schaltfläche Relaunch, die unten auf der Seite erscheint.

- Unter Linux starten Sie den Browser mit `--enable-features=Vulkan`.
- Safari 18 (macOS 15) hat WebGPU standardmäßig aktiviert.
- In Firefox Nightly geben Sie about:config in die Adressleiste ein und `set dom.webgpu.enabled to true`.

### GPU für Microsoft Edge einrichten 

Hier sind die Schritte, um eine Hochleistungs-GPU für Microsoft Edge unter Windows einzurichten:

- **Einstellungen öffnen:** Klicken Sie auf das Startmenü und wählen Sie Einstellungen.
- **Systemeinstellungen:** Gehen Sie zu System und dann zu Anzeige.
- **Grafikeinstellungen:** Scrollen Sie nach unten und klicken Sie auf Grafikeinstellungen.
- **App auswählen:** Unter „Wählen Sie eine App zur Festlegung der Präferenz“ wählen Sie Desktop-App und dann Durchsuchen.
- **Edge auswählen:** Navigieren Sie zum Edge-Installationsordner (in der Regel `C:\Program Files (x86)\Microsoft\Edge\Application`) und wählen Sie `msedge.exe`.
- **Präferenz festlegen:** Klicken Sie auf Optionen, wählen Sie Hohe Leistung und klicken Sie dann auf Speichern.
Damit wird sichergestellt, dass Microsoft Edge Ihre Hochleistungs-GPU für eine bessere Leistung verwendet. 
- **Starten Sie Ihren Computer neu**, damit diese Einstellungen wirksam werden.

### Beispiele: Bitte [klicken Sie auf diesen Link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner jeweiligen Originalsprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.