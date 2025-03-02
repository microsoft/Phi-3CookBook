### Beispiel-Szenario

Stellen Sie sich vor, Sie haben ein Bild (`demo.png`) und möchten Python-Code generieren, der dieses Bild verarbeitet und eine neue Version davon speichert (`phi-3-vision.jpg`).

Der obige Code automatisiert diesen Prozess durch:

1. Einrichten der Umgebung und der erforderlichen Konfigurationen.
2. Erstellen eines Prompts, der das Modell anweist, den benötigten Python-Code zu generieren.
3. Senden des Prompts an das Modell und Sammeln des generierten Codes.
4. Extrahieren und Ausführen des generierten Codes.
5. Anzeigen des Original- und des verarbeiteten Bildes.

Dieser Ansatz nutzt die Leistungsfähigkeit von KI, um Bildverarbeitungsaufgaben zu automatisieren und somit Ziele schneller und einfacher zu erreichen.

[Beispiel-Lösungscode](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Lassen Sie uns den gesamten Code Schritt für Schritt aufschlüsseln:

1. **Erforderliches Paket installieren**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Dieser Befehl installiert das Paket `langchain_nvidia_ai_endpoints` und stellt sicher, dass es sich um die neueste Version handelt.

2. **Notwendige Module importieren**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Diese Importe bringen die notwendigen Module mit, um mit den NVIDIA AI-Endpunkten zu interagieren, Passwörter sicher zu handhaben, mit dem Betriebssystem zu interagieren und Daten im Base64-Format zu codieren/decodieren.

3. **API-Schlüssel einrichten**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Dieser Code überprüft, ob die Umgebungsvariable `NVIDIA_API_KEY` gesetzt ist. Falls nicht, wird der Benutzer aufgefordert, seinen API-Schlüssel sicher einzugeben.

4. **Modell und Bildpfad definieren**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Hier wird das zu verwendende Modell festgelegt, eine Instanz von `ChatNVIDIA` mit dem angegebenen Modell erstellt und der Pfad zur Bilddatei definiert.

5. **Text-Prompt erstellen**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Hier wird ein Text-Prompt definiert, der das Modell anweist, Python-Code zur Bildverarbeitung zu generieren.

6. **Bild in Base64 kodieren**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Dieser Code liest die Bilddatei, kodiert sie in Base64 und erstellt ein HTML-Bild-Tag mit den kodierten Daten.

7. **Text und Bild in Prompt kombinieren**:
    ```python
    prompt = f"{text} {image}"
    ```
    Dies kombiniert den Text-Prompt und das HTML-Bild-Tag zu einem einzigen String.

8. **Code mit ChatNVIDIA generieren**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Dieser Code sendet den Prompt an `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code`-String.

9. **Python-Code aus generiertem Inhalt extrahieren**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Hier wird der eigentliche Python-Code aus dem generierten Inhalt extrahiert, indem die Markdown-Formatierung entfernt wird.

10. **Generierten Code ausführen**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Dieser Abschnitt führt den extrahierten Python-Code als Subprozess aus und erfasst dessen Ausgabe.

11. **Bilder anzeigen**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Diese Zeilen zeigen die Bilder mithilfe des Moduls `IPython.display` an.

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.