## Willkommen bei den Phi-Labs mit C#

Es gibt eine Auswahl an Labs, die zeigen, wie die leistungsstarken verschiedenen Versionen der Phi-Modelle in einer .NET-Umgebung integriert werden können.

## Voraussetzungen

Bevor Sie das Beispiel ausführen, stellen Sie sicher, dass Sie Folgendes installiert haben:

**.NET 9:** Stellen Sie sicher, dass Sie die [neueste Version von .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) auf Ihrem Computer installiert haben.

**(Optional) Visual Studio oder Visual Studio Code:** Sie benötigen eine IDE oder einen Code-Editor, der .NET-Projekte ausführen kann. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) oder [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) werden empfohlen.

**Mit git** klonen Sie lokal eine der verfügbaren Versionen Phi-3, Phi3.5 oder Phi-4 von [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Laden Sie die Phi-4 ONNX-Modelle** auf Ihren lokalen Computer herunter:

### Navigieren Sie zum Ordner, in dem die Modelle gespeichert werden sollen

```bash
cd c:\phi\models
```

### Unterstützung für lfs hinzufügen

```bash
git lfs install 
```

### Klonen und Herunterladen des Phi-4 Mini Instruct-Modells und des Phi-4 Multi Modal-Modells

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Laden Sie die Phi-3 ONNX-Modelle** auf Ihren lokalen Computer herunter:

### Klonen und Herunterladen des Phi-3 Mini 4K Instruct-Modells und des Phi-3 Vision 128K-Modells

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Wichtig:** Die aktuellen Demos sind so konzipiert, dass sie die ONNX-Versionen der Modelle verwenden. Die vorherigen Schritte klonen die folgenden Modelle.

## Über die Labs

Die Hauptlösung enthält mehrere Beispiel-Labs, die die Fähigkeiten der Phi-Modelle mit C# demonstrieren.

| Projekt | Modell | Beschreibung |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 oder Phi-3.5 | Beispiel für eine Konsolen-Chat-Anwendung, die es dem Benutzer ermöglicht, Fragen zu stellen. Das Projekt lädt ein lokales ONNX Phi-3-Modell mit `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Führen Sie das Projekt mit dem Befehl aus:

    ```bash
    dotnet run
    ```

1. Das Beispielprojekt fordert eine Benutzereingabe an und antwortet im lokalen Modus.

   Die laufende Demo sieht ähnlich aus wie diese:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe maschineller KI-Übersetzungsdienste übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.