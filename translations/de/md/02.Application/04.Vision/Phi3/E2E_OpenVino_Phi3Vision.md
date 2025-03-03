Diese Demo zeigt, wie ein vortrainiertes Modell verwendet wird, um basierend auf einem Bild und einer Textaufforderung Python-Code zu generieren.

[Beispielcode](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Hier ist eine Schritt-für-Schritt-Erklärung:

1. **Importe und Einrichtung**:
   - Die notwendigen Bibliotheken und Module werden importiert, darunter `requests`, `PIL` für die Bildverarbeitung und `transformers` für die Modellverarbeitung.

2. **Laden und Anzeigen des Bildes**:
   - Eine Bilddatei (`demo.png`) wird mit der `PIL`-Bibliothek geöffnet und angezeigt.

3. **Definition der Aufforderung**:
   - Eine Nachricht wird erstellt, die das Bild und eine Anfrage enthält, Python-Code zu generieren, um das Bild zu verarbeiten und es mit `plt` (matplotlib) zu speichern.

4. **Laden des Prozessors**:
   - Der `AutoProcessor` wird aus einem vortrainierten Modell geladen, das im Verzeichnis `out_dir` angegeben ist. Dieser Prozessor verarbeitet die Text- und Bildeingaben.

5. **Erstellen der Aufforderung**:
   - Die `apply_chat_template`-Methode wird verwendet, um die Nachricht in eine für das Modell geeignete Aufforderung zu formatieren.

6. **Verarbeitung der Eingaben**:
   - Die Aufforderung und das Bild werden in Tensoren umgewandelt, die das Modell verstehen kann.

7. **Festlegen der Generierungsparameter**:
   - Parameter für den Generierungsprozess des Modells werden definiert, einschließlich der maximalen Anzahl neuer Tokens, die generiert werden sollen, und ob die Ausgabe stichprobenartig erfolgen soll.

8. **Generierung des Codes**:
   - Das Modell generiert den Python-Code basierend auf den Eingaben und den Generierungsparametern. Der `TextStreamer` wird verwendet, um die Ausgabe zu verarbeiten, wobei die Aufforderung und spezielle Tokens übersprungen werden.

9. **Ausgabe**:
   - Der generierte Code wird ausgegeben, der Python-Code enthalten sollte, um das Bild zu verarbeiten und wie in der Aufforderung angegeben zu speichern.

Diese Demo zeigt, wie ein vortrainiertes Modell mit OpenVino genutzt werden kann, um Code dynamisch basierend auf Benutzereingaben und Bildern zu generieren.

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von KI-basierten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.